<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use Inertia\Response;

class UserController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('admin/users');
    }
}
