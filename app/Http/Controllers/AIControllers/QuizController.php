<?php

namespace App\Http\Controllers\AIControllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\AIService;
use App\Models\QuizSession;
use App\Models\QuizResult;
use App\Models\Activity;

class QuizController extends Controller
{
    //
    public function __construct(private AIService $ai) {}
    public function evaluate(Request $request)
    {
        // directly forward everything to AIService (NO DB, NO LOGIC CHANGE)
        return response()->json(
            $this->ai->evaluateQuiz($request->all())
        );
    }
    // public function overall(Request $request)
    // {
    //     return response()->json(
    //         $this->ai->overallQuiz($request->all())
    //     );
    // }
    public function overall(Request $request)
    {
        $response = $this->ai->overallQuiz($request->all());

        $session = QuizSession::create([
            'user_id' => $request->user()->id,
            'subject' => $request->subject,
            'board' => $request->board,
            'class_level' => $request->class_level,
            'question_type' => $request->question_type,

            'total_score' => $response['total_score'] ?? null,
            'percentage' => $response['percentage'] ?? null,
            'grade' => $response['grade'] ?? null,

            'strong_areas' => $response['strong_areas'] ?? [],
            'weak_areas' => $response['weak_areas'] ?? [],

            'overall_feedback' => $response['overall_feedback'] ?? null,
            'study_tip' => $response['study_tip'] ?? null,

            'completed_at' => now(),
        ]);
        //recent activity table
        Activity::create([
            'user_id' => $request->user()->id,
            'type' => 'quiz',
            'message' => 'Completed ' . ucfirst($request->subject) . ' Quiz — Score: ' . ($response['percentage'] ?? 0) . '%',
        ]);
        $userId = $request->user()->id;

        $latestIds = Activity::where('user_id', $userId)
            ->latest()
            ->take(8)
            ->pluck('id');

        Activity::where('user_id', $userId)
            ->where('created_at', '<', now()->subMinutes(3))
            ->whereNotIn('id', $latestIds)
            ->delete();
        foreach ($request->results as $result) {

            QuizResult::create([
                'session_id' => $session->id,
                'user_id' => $request->user()->id,

                'question' => $result['question'] ?? '',
                'student_answer' => $result['student_answer'] ?? '',

                'score' => (float) ($result['score'] ?? 0),

                'feedback' => $result['feedback'] ?? '',

                'is_correct' => (float) ($result['score'] ?? 0) >= 5,
            ]);
        }

        return response()->json([
            'session_id' => $session->id,
            ...$response
        ]);
    }
}
