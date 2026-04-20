<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use Inertia\Response;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use App\Models\Content;

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
            'file' => 'required|file|max:51200'
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
            'data' => $content
        ]);
    }

    // 2. Get all content (Student)
    public function index()
    {
        $data = Content::latest()->get();

        return response()->json([
            'success' => true,
            'data' => $data
        ]);
    }

    // 3. Download
    public function download($id)
    {
        $content = Content::findOrFail($id);
        $content->increment('downloads');

        $filePath = storage_path('app/public/' . $content->file_path);

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
}
