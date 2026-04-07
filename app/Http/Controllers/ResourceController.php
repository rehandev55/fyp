<?php

namespace App\Http\Controllers;

use Inertia\Response;

class ResourceController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('resources');
    }
}
