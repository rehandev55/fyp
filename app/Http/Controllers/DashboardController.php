<?php

namespace App\Http\Controllers;

use App\Models\QuizSession;
use App\Models\QuizResult;
use Illuminate\Support\Facades\Auth;
use Inertia\Response;
use App\Models\Activity;

class DashboardController extends Controller
{
    public function __invoke(): Response
    {
        $userId = Auth::id();

        // =========================
        // BASIC STATS
        // =========================

        $questionsPracticed = QuizResult::where('user_id', $userId)->count();

        $averageScore = round(
            QuizSession::where('user_id', $userId)->avg('percentage') ?? 0
        );

        // =========================
        // WEAK SUBJECT DETECTION
        // =========================

        $weakSubjectRow = QuizSession::selectRaw('subject, AVG(percentage) as score')
            ->where('user_id', $userId)
            ->groupBy('subject')
            ->orderBy('score', 'asc')
            ->first();

        $weakSubject = $weakSubjectRow
            ? ucfirst($weakSubjectRow->subject)
            : 'None';


        //recent activity
        $recentActivities = Activity::where('user_id', $userId)
            ->latest()
            ->take(8)
            ->get();


        // =========================
        // SEND TO FRONTEND
        // =========================

        return inertia('dashboard', [
            'progressSummary' => [
                'questions_practiced' => $questionsPracticed,
                'average_score' => $averageScore,
                'weak_subject' => $weakSubject,
            ],
            'recentActivities' => $recentActivities,
        ]);
    }
}
