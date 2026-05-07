<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class QuizResult extends Model
{
    //
    public function session()
    {
        return $this->belongsTo(QuizSession::class, 'session_id');
    }
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
