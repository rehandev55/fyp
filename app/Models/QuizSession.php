<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class QuizSession extends Model
{
    //
    public function results()
    {
        return $this->hasMany(QuizResult::class, 'session_id');
    }
    protected $fillable = [
        'user_id',
        'subject',
        'board',
        'class_level',
        'question_type',
        'total_score',
        'percentage',
        'grade',
        'strong_areas',
        'weak_areas',
        'overall_feedback',
        'study_tip',
        'completed_at',
    ];

    protected $casts = [
        'strong_areas' => 'array',
        'weak_areas' => 'array',
        'completed_at' => 'datetime',
    ];
}
