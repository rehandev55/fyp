<?php

namespace App\Http\Controllers;

use App\Enums\Board;
use App\Enums\ClassLevel;
use App\Enums\Subject;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Validation\Rule;
use Inertia\Response;

class ProfileController extends Controller
{
    public function show(): Response
    {
        return inertia('profile');
    }

    public function update(Request $request): RedirectResponse
    {
        $validated = $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'board' => ['nullable', Rule::enum(Board::class)],
            'class_level' => ['nullable', Rule::enum(ClassLevel::class)],
            'subject' => ['nullable', Rule::enum(Subject::class)],
        ]);

        $request->user()->update($validated);

        return back();
    }
}
