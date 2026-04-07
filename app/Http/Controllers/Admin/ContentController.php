<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use Inertia\Response;

class ContentController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('admin/content');
    }
}
