<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Laravel\Socialite\Facades\Socialite;
use App\Models\User;
use Illuminate\Support\Facades\Auth;

class GoogleController extends Controller
{
    public function redirect()
    {
        return Socialite::driver('google')->redirect();
    }
    public function callback()
    {
        $googleUser = Socialite::driver('google')->user();

        // 1. Check if user exists
        $user = User::where('email', $googleUser->email)->first();

        // 2. If not, create user
        if (!$user) {
            $user = User::create([
                'name' => $googleUser->name,
                'email' => $googleUser->email,
                'password' => bcrypt('google-auth'), // dummy password
                'role' => 'user',
                'status' => 'Active',
            ]);
        }

        // 3. Login user (session based - matches your system)
        Auth::login($user);

        // 4. Redirect to frontend
        return redirect('/dashboard');
    }
}
