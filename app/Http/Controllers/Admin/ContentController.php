<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Activity;
use App\Models\Content;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Str;
use Inertia\Response;

class ContentController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('admin/content');
    }

    // 1. Upload Content (Admin)
    public function store(Request $request)
    {
        $request->validate([
            'title' => 'required',
            'type' => 'required',
            'board' => 'required',
            'class_level' => 'required',
            'subject' => 'required',
            'file' => 'required|file|max:102400',
        ]);

        $file = $request->file('file');
        /** getSize() must be read before store() moves the temporary upload. */
        $fileSize = $file->getSize();
        $path = $file->store('contents', 'public');

        if ($path === false) {
            return response()->json([
                'success' => false,
                'message' => 'The file could not be saved. Please try again.',
            ], 500);
        }

        $content = Content::create([
            'title' => $request->title,
            'type' => $request->type,
            'board' => $request->board,
            'class_level' => $request->class_level,
            'subject' => $request->subject,
            'file_path' => $path,
            'file_size' => $fileSize,
        ]);

        return response()->json([
            'success' => true,
            'data' => $content,
        ]);
    }

    // 2. Get all content (Student)
    public function index()
    {
        $data = Content::latest()->get();

        return response()->json([
            'success' => true,
            'data' => $data,
        ]);
    }

    // 3. Download
    public function download($id)
    {
        $content = Content::findOrFail($id);
        $disk = Storage::disk('public');

        if (blank($content->file_path) || ! $disk->exists($content->file_path)) {
            return response()->json([
                'success' => false,
                'message' => 'This file is no longer available on the server.',
            ], 404);
        }

        $content->increment('downloads');

        // recent activity table
        Activity::create([
            'user_id' => Auth::id(),
            'type' => 'resource',
            'message' => 'Downloaded '.$content->title,
        ]);
        $userId = Auth::id();

        $latestIds = Activity::where('user_id', $userId)
            ->latest()
            ->take(8)
            ->pluck('id');

        Activity::where('user_id', $userId)
            ->where('created_at', '<', now()->subMinutes(3))
            ->whereNotIn('id', $latestIds)
            ->delete();

        return $disk->download($content->file_path, $this->downloadFilename($content));
    }

    /**
     * Builds a readable filename from the title rather than serving the random storage hash.
     */
    private function downloadFilename(Content $content): string
    {
        $extension = pathinfo($content->file_path, PATHINFO_EXTENSION);
        $name = Str::slug($content->title) ?: 'resource';

        return $extension ? "{$name}.{$extension}" : $name;
    }

    // 4. Delete
    public function destroy($id)
    {
        $content = Content::findOrFail($id);

        Storage::disk('public')->delete($content->file_path);
        $content->delete();

        return response()->json(['success' => true]);
    }

    public function update(Request $request, $id)
    {
        $content = Content::findOrFail($id);

        $content->update([
            'title' => $request->title,
            'type' => $request->type,
            'board' => $request->board,
            'class_level' => $request->class_level,
            'subject' => $request->subject,
        ]);

        return response()->json([
            'data' => $content,
        ]);
    }
}
