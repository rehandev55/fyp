<?php

use App\Http\Controllers\AboutController;
use App\Http\Controllers\Admin\ContentController;
use App\Http\Controllers\Admin\DashboardController as AdminDashboardController;
use App\Http\Controllers\Admin\UserController;
use App\Http\Controllers\AiChatController;
use App\Http\Controllers\DashboardController;
use App\Http\Controllers\PracticeController;
use App\Http\Controllers\ProfileController;
use App\Http\Controllers\ProgressController;
use App\Http\Controllers\ResourceController;
use App\Http\Controllers\SelectionController;
use Illuminate\Support\Facades\Route;
use Laravel\Fortify\Features;

Route::inertia('/', 'welcome', [
    'canRegister' => Features::enabled(Features::registration()),
])->name('home');

Route::middleware(['auth', 'verified'])->group(function () {
    Route::get('dashboard', DashboardController::class)->name('dashboard');
    Route::get('selection', SelectionController::class)->name('selection');
    Route::get('aichat', AiChatController::class)->name('aichat');
    Route::get('practice', PracticeController::class)->name('practice');
    Route::get('resources', ResourceController::class)->name('resources');
    Route::get('progress', ProgressController::class)->name('progress');
    Route::get('profile', ProfileController::class)->name('profile');
    Route::get('about', AboutController::class)->name('about');

    Route::prefix('admin')->name('admin.')->group(function () {
        Route::get('dashboard', AdminDashboardController::class)->name('dashboard');
        Route::get('users', UserController::class)->name('users');
        Route::get('content', ContentController::class)->name('content');
    });
});

require __DIR__.'/settings.php';
