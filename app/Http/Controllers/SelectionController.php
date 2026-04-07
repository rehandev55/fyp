<?php

namespace App\Http\Controllers;

use Inertia\Response;

class SelectionController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('selection');
    }
}
