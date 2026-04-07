<?php

namespace App\Http\Controllers;

use Inertia\Response;

class ProgressController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('progress');
    }
}
