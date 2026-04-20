<?php

namespace App\Http\Controllers\AIControllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;


class AIController extends Controller
{
    //
    private $baseUrl = "http://localhost:8001";

    public function chat(Request $request)
    {
        $response = Http::post($this->baseUrl . '/chat', $request->all());
        return response()->json($response->json());
    }

    public function generateQuiz(Request $request)
    {
        $response = Http::post($this->baseUrl . '/quiz/generate', $request->all());
        return response()->json($response->json());
    }

    public function evaluateQuiz(Request $request)
    {
        $response = Http::post($this->baseUrl . '/quiz/evaluate', $request->all());
        return response()->json($response->json());
    }
}
