<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use Inertia\Response;

class DashboardController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('admin/dashboard');
    }
}
