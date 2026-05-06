<?php

namespace App\Http\Controllers\AIControllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\AIService;

class QuizController extends Controller
{
    //
    public function __construct(private AIService $ai) {}
    public function evaluate(Request $request)
    {
        // directly forward everything to AIService (NO DB, NO LOGIC CHANGE)
        return response()->json(
            $this->ai->evaluateQuiz($request->all())
        );
    }
    public function overall(Request $request)
    {
        return response()->json(
            $this->ai->overallQuiz($request->all())
        );
    }
}
