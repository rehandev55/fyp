<?php

use App\Http\Controllers\Admin\ContentController;
use App\Http\Controllers\Admin\UserController;
use App\Http\Controllers\AIControllers\AIController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::post('/chat', [AIController::class, 'chat']);
// Route::get('/chat', function () {
//     return response()->json([
//         'status' => 'API WORKING'
//     ]);
// });
Route::post('/quiz/generate', [AIController::class, 'generateQuiz']);
Route::post('/quiz/evaluate', [AIController::class, 'evaluateQuiz']);

Route::prefix('content')->group(function () {

    Route::post('/', [ContentController::class, 'store']);        // upload
    Route::get('/', [ContentController::class, 'index']);         // get all
    Route::get('/download/{id}', [ContentController::class, 'download']);
    Route::delete('/{id}', [ContentController::class, 'destroy']);
});

Route::get('/users', [UserController::class, 'index']);
Route::delete('/users/{id}', [UserController::class, 'destroy']);
Route::put('/users/{id}', [UserController::class, 'update']);
Route::patch('/users/toggle/{id}', [UserController::class, 'toggleStatus']);

Route::put('/content/{id}', [ContentController::class, 'update']);
Route::get('/content', [ContentController::class, 'index']);
