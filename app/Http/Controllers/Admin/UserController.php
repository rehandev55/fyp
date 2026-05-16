<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
// use Illuminate\Http\Client\Request;
use Illuminate\Http\Request;
use Inertia\Response;
// use Illuminate\Support\Facades\Request;
use App\Models\User;

class UserController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('admin/users');
    }

    public function index()
    {
        $users = User::with('quizSessions')->get();

        $users->map(function ($user) {

            $sessions = $user->quizSessions;

            // total quizzes
            $user->quizzes = $sessions->count();

            // average score
            $user->score = $sessions->count()
                ? round($sessions->avg('percentage'))
                : 0;

            // weak subject
            $user->weakSubject = $sessions
                ->groupBy('subject')
                ->map(fn($s) => round($s->avg('percentage')))
                ->sort()
                ->keys()
                ->first() ?? 'N/A';

            return $user;
        });

        return response()->json([
            'data' => $users
        ]);
    }
    public function destroy($id)
    {
        $user = User::findOrFail($id);

        if ($user->role === 'admin') {
            return response()->json([
                'message' => 'Admin cannot be deleted'
            ], 403);
        }

        $user->delete();

        return response()->json([
            'message' => 'User deleted'
        ]);
    }
    public function update(Request $request, $id)
    {
        $user = User::findOrFail($id);

        $data = $request->only([
            'name',
            'email',
            'class_level',
            'board',
            'subject',
            'status'
        ]);

        $user->update($data);

        return response()->json([
            'data' => $user
        ]);
    }

    public function toggleStatus($id)
    {
        $user = User::findOrFail($id);
        if ($user->role === 'admin') {
            return response()->json([
                'message' => 'Admin cannot be blocked'
            ], 403);
        }
        $user->status = $user->status === 'Active' ? 'Blocked' : 'Active';
        $user->save();

        return response()->json([
            'data' => $user
        ]);
    }
}
