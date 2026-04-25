<?php

namespace App\Models;

use App\Enums\Board;
use App\Enums\ClassLevel;
use App\Enums\Subject;
use Illuminate\Database\Eloquent\Model;

class ChatSession extends Model
{
    protected $fillable = [
        'user_id',
        'title',
        'board',
        'class_level',
        'subject',
    ];

    protected function casts(): array
    {
        return [
            'board' => Board::class,
            'class_level' => ClassLevel::class,
            'subject' => Subject::class,
        ];
    }

    public function messages()
    {
        return $this->hasMany(ChatMessage::class, 'session_id');
    }

    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
