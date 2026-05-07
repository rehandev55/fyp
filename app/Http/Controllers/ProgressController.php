<?php

namespace App\Http\Controllers;

use App\Models\QuizSession;
use App\Models\QuizResult;
use Illuminate\Support\Facades\Auth;
use Inertia\Response;

class ProgressController extends Controller
{
    public function __invoke(): Response
    {
        $userId = Auth::id();

        // ======================
        // 1. SESSIONS (overall stats)
        // ======================
        $sessions = QuizSession::where('user_id', $userId)->get();

        $totalQuizzes = $sessions->count();

        $averageScore = $totalQuizzes
            ? round($sessions->avg('percentage'))
            : 0;

        // ======================
        // 2. QUESTIONS DONE (from quiz_results table)
        // ======================
        $questionsDone = QuizResult::where('user_id', $userId)->count();

        // ======================
        // 3. SUBJECT PERFORMANCE (from sessions)
        // ======================
        $subjects = QuizSession::selectRaw('subject, AVG(percentage) as score')
            ->where('user_id', $userId)
            ->groupBy('subject')
            ->get()
            ->map(function ($s) {
                $score = round($s->score);

                return [
                    'name' => ucfirst($s->subject),
                    'score' => $score,
                    'status' =>
                    $score >= 85 ? 'Excellent' : ($score >= 70 ? 'Strong' : ($score >= 60 ? 'Good' : 'Needs Work')),
                ];
            });
        //weak subject
        $weakest = $subjects->sortBy('score')->first();

        $focusArea = $weakest
            ? $weakest['name'] . " needs more practice. Try taking more quizzes and reviewing AI explanations."
            : "Great job! Keep practicing to maintain your performance.";

        // ======================
        // RESPONSE
        // ======================
        return inertia('progress', [
            'stats' => [
                'total_quizzes' => $totalQuizzes,
                'average_score'  => $averageScore,
                'questions_done' => $questionsDone,
            ],
            'subjects' => $subjects,
            'focus_area' => $focusArea,
        ]);
    }
}
