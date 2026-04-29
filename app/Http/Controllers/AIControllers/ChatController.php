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

        // $board = $request->input('board', $user->board?->value ?? Board::Federal->value);
        // $classLevel = $request->input('class_level', $user->class_level?->value ?? ClassLevel::Class10->value);
        // $subject = $request->input('subject', $user->subject?->value ?? Subject::Physics->value);
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
            $session = ChatSession::find($request->session_id);
        } else {
            $session = ChatSession::create([
                'user_id' => $user->id,
                'title' => substr($request->message, 0, 40),
                'board' => $board,
                'class_level' => $classLevel,
                'subject' => $subject,
            ]);
        }

        ChatMessage::create([
            'session_id' => $session->id,
            'role' => 'user',
            'message' => $request->message,
        ]);

        // $reply = $this->ai->chat($request->message, $board, $classLevel, $subject);
        $reply = $this->ai->chat(
            $request->message,
            $board instanceof \App\Enums\Board ? $board->value : $board,
            $classLevel instanceof \App\Enums\ClassLevel ? $classLevel->value : $classLevel,
            $subject instanceof \App\Enums\Subject ? $subject->value : $subject,
        );

        ChatMessage::create([
            'session_id' => $session->id,
            'role' => 'ai',
            'message' => $reply,
        ]);

        return response()->json([
            'session_id' => $session->id,
            'reply' => $reply,
            // dd($reply)
        ]);
    }


    public function delete($id)
    {
        ChatSession::where('id', $id)->delete();
        ChatMessage::where('session_id', $id)->delete();

        return response()->json(['success' => true]);
    }
}
