<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Support\Facades\Request;
use Inertia\Response;

class UserController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('admin/users');
    }

    public function index()
    {
        $users = User::all();
        return response()->json([
            'data' => $users
        ]);
    }
    public function destroy($id)
    {
        User::findOrFail($id)->delete();

        return response()->json([
            'message' => 'User deleted'
        ]);
    }
    public function update(Request $request, $id)
    {
        $user = User::findOrFail($id);

        $user->update($request->all());

        return response()->json([
            'data' => $user
        ]);
    }
    // public function update(Request $request, $id)
    // {
    //     $user = User::findOrFail($id);

    //     $validated = $request->validate([
    //         'name' => 'required|string',
    //         'email' => 'required|email',
    //         'status' => 'nullable|string',
    //     ]);

    //     $user->update($validated);

    //     return response()->json([
    //         'data' => $user
    //     ]);
    // }

    public function toggleStatus($id)
    {
        $user = User::findOrFail($id);

        $user->status = $user->status === 'Active' ? 'Blocked' : 'Active';
        $user->save();

        return response()->json([
            'data' => $user
        ]);
    }
}
