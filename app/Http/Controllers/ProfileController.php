<?php

namespace App\Http\Controllers;

use Inertia\Response;

class ProfileController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('profile');
    }
}
