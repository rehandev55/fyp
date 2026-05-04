<?php

namespace App\Http\Controllers\AIControllers;

use App\Http\Controllers\Controller;
use App\Services\AIService;
use Illuminate\Http\Request;

class AIController extends Controller
{
    public function __construct(private AIService $ai) {}

    public function chat(Request $request)
    {
        $reply = $this->ai->chat(
            $request->input('question', $request->input('message', '')),
            $request->input('board', ''),
            $request->input('class_level', ''),
            $request->input('subject', ''),
        );

        return response()->json(['reply' => $reply]);
    }

    public function generateQuiz(Request $request)
    {
        return response()->json($this->ai->generateQuiz($request->all()));
    }

    public function evaluateQuiz(Request $request)
    {
        return response()->json($this->ai->evaluateQuiz($request->all()));
    }
}
