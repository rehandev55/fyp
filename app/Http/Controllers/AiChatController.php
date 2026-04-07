<?php

namespace App\Http\Controllers;

use Inertia\Response;

class AiChatController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('ai-chat');
    }
}
