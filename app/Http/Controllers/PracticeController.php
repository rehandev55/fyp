<?php

namespace App\Http\Controllers;

use Inertia\Response;

class PracticeController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('practice');
    }
}
