<?php

namespace App\Http\Controllers\AIControllers;

use App\Enums\Board;
use App\Enums\ClassLevel;
use App\Enums\Subject;
use App\Http\Controllers\Controller;
use App\Models\ChatMessage;
use App\Models\ChatSession;
use App\Services\AIService;
use Illuminate\Http\Request;
use App\Models\Activity;
use SebastianBergmann\Environment\Console;

class ChatController extends Controller
{
    public function __construct(private AIService $ai) {}

    public function sessions(Request $request)
    {
        return ChatSession::where('user_id', $request->user()->id)
            ->latest()
            ->get();
    }

    public function messages($id)
    {
        return ChatMessage::where('session_id', $id)
            ->orderBy('created_at')
            ->get();
    }
    public function send(Request $request)

    {
        // dd($request->all());
        $request->validate([
            'message' => 'required|string',
        ]);

        $user = $request->user();
        $board = Board::tryFrom($request->input('board'))
            ?? $user->board
            ?? Board::Federal;

        $classLevel = ClassLevel::tryFrom($request->input('class_level'))
            ?? $user->class_level
            ?? ClassLevel::Class10;

        $subject = Subject::tryFrom($request->input('subject'))
            ?? $user->subject
            ?? Subject::Physics;
        if ($request->session_id) {
            // $session = ChatSession::find($request->session_id);
            $session = ChatSession::findOrFail($request->session_id);

            $board = $session->board;
            $classLevel = $session->class_level;
            $subject = $session->subject;
        } else {
            $session = ChatSession::create([
                'user_id' => $user->id,
                'title' => substr($request->message, 0, 40),
                'board' => $board,
                'class_level' => $classLevel,
                'subject' => $subject,
            ]);
        }
        //memory chat
        $history = ChatMessage::where('session_id', $session->id)
            ->orderBy('created_at', 'desc')
            ->take(10)
            ->get()
            ->reverse();

        $chatHistory = $history->map(function ($msg) {
            return [
                'role' => $msg->role,
                'content' => $msg->message,
            ];
        })->values()->toArray();

        ChatMessage::create([
            'session_id' => $session->id,
            'role' => 'user',
            'message' => $request->message,
        ]);

        $response = $this->ai->chat(
            $request->message,
            $board instanceof \App\Enums\Board ? $board->value : $board,
            $classLevel instanceof \App\Enums\ClassLevel ? $classLevel->value : $classLevel,
            $subject instanceof \App\Enums\Subject ? $subject->value : $subject,
            $chatHistory,
            $session->existing_summary
        );
        // dd($response);

        $updatedSummary = $response['updated_summary'] ?? null;
        // dd($reply);
        $reply = $response['reply'] ?? '';
        ChatMessage::create([
            'session_id' => $session->id,
            'role' => 'assistant',
            'message' => $reply,
        ]);
        // dd([
        //     'old' => $session->existing_summary,
        //     'new' => $updatedSummary
        // ]);

        //recent activity table
        Activity::create([
            'user_id' => $user->id,
            'type' => 'chat',
            'message' => 'Asked AI about ' . $subject->value,
        ]);
        $userId = $user->id;

        $latestIds = Activity::where('user_id', $userId)
            ->latest()
            ->take(8)
            ->pluck('id');

        Activity::where('user_id', $userId)
            ->where('created_at', '<', now()->subMinutes(3))
            ->whereNotIn('id', $latestIds)
            ->delete();
        if (!empty($updatedSummary)) {
            $session->existing_summary = $updatedSummary;
            $session->save();
        }

        return response()->json([
            'session_id' => $session->id,
            'reply' => $reply,
            'updatedSummary' => $updatedSummary,
            // dd($reply)
            'existing_summary' => $session->existing_summary,
        ]);
    }


    public function delete($id)
    {
        ChatSession::where('id', $id)->delete();
        ChatMessage::where('session_id', $id)->delete();

        return response()->json(['success' => true]);
    }

    public function history($sessionId)
    {
        $messages = ChatMessage::where('session_id', $sessionId)
            ->orderBy('created_at', 'asc')
            ->get();

        // Format for AI
        $formatted = $messages->map(function ($msg) {
            return [
                'role' => $msg->role,          // 'user' or 'ai'
                'content' => $msg->message     // actual text
            ];
        });

        return response()->json([
            'messages' => $formatted
        ]);
    }
}
