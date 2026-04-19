<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AIController;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::post('/chat', [AIController::class, 'chat']);
Route::post('/quiz/generate', [AIController::class, 'generateQuiz']);
Route::post('/quiz/evaluate', [AIController::class, 'evaluateQuiz']);
