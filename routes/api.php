<?php

use App\Http\Controllers\Admin\ContentController;
use App\Http\Controllers\Admin\UserController;
use App\Http\Controllers\AIControllers\AIController;
use App\Http\Controllers\AIControllers\ChatController;
use App\Http\Controllers\Api\AuthController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

// Public auth routes
Route::post('/register', [AuthController::class, 'register']);
Route::post('/login', [AuthController::class, 'login']);

// Protected routes
Route::middleware('auth:sanctum')->group(function () {
    // Auth
    Route::post('/logout', [AuthController::class, 'logout']);
    Route::get('/user', function (Request $request) {
        return $request->user();
    });

    // AI
    Route::post('/chat', [AIController::class, 'chat']);
    Route::post('/quiz/generate', [AIController::class, 'generateQuiz']);
    Route::post('/quiz/evaluate', [AIController::class, 'evaluateQuiz']);

    // Chat
    Route::get('/chat/sessions', [ChatController::class, 'sessions']);
    Route::get('/chat/messages/{id}', [ChatController::class, 'messages']);
    Route::post('/chat/send', [ChatController::class, 'send']);
    Route::delete('/chat/{id}', [ChatController::class, 'delete']);

    // Content
    Route::prefix('content')->group(function () {
        Route::post('/', [ContentController::class, 'store']);
        Route::get('/', [ContentController::class, 'index']);
        Route::get('/download/{id}', [ContentController::class, 'download']);
        Route::put('/{id}', [ContentController::class, 'update']);
        Route::delete('/{id}', [ContentController::class, 'destroy']);
    });

    // Users (admin)
    Route::get('/users', [UserController::class, 'index']);
    Route::put('/users/{id}', [UserController::class, 'update']);
    Route::delete('/users/{id}', [UserController::class, 'destroy']);
    Route::patch('/users/toggle/{id}', [UserController::class, 'toggleStatus']);
});
