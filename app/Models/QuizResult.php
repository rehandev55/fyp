<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class QuizResult extends Model
{
    //
    protected $fillable = [
        'session_id',
        'user_id',
        'question',
        'student_answer',
        'score',
        'feedback',
        'is_correct',
    ];
}
