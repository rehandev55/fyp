<?php

namespace App\Http\Controllers\Admin;

use App\Enums\Board;
use App\Enums\ClassLevel;
use App\Enums\Subject;
use App\Http\Controllers\Controller;
use App\Models\Content;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use Illuminate\Validation\Rule;
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
            'board' => ['required', Rule::enum(Board::class)],
            'class_level' => ['required', Rule::enum(ClassLevel::class)],
            'subject' => ['required', Rule::enum(Subject::class)],
            'file' => 'required|file|max:102400',
        ]);

        $file = $request->file('file');
        $path = $file->store('contents', 'public');

        $content = Content::create([
            'title' => $request->title,
            'type' => $request->type,
            'board' => $request->board,
            'class_level' => $request->class_level,
            'subject' => $request->subject,
            'file_path' => $path,
            'file_size' => $file->getSize(),
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
        $content->increment('downloads');

        $filePath = storage_path('app/public/'.$content->file_path);

        return response()->download($filePath);
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
