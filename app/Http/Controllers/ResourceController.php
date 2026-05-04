<?php

namespace App\Http\Controllers;

use App\Models\Content;
use Inertia\Response;

class ResourceController extends Controller
{
    public function __invoke(): Response
    {
        $resources = Content::select('id', 'title', 'type', 'board', 'class_level', 'subject', 'file_path', 'file_size', 'downloads')
            ->latest()
            ->get();

        return inertia('resources', [
            'resources' => $resources,
        ]);
    }
}
