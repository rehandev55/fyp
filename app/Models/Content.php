<?php

namespace App\Models;

use App\Enums\Board;
use App\Enums\ClassLevel;
use App\Enums\Subject;
use Illuminate\Database\Eloquent\Model;

class Content extends Model
{
    protected $fillable = [
        'title',
        'type',
        'board',
        'class_level',
        'subject',
        'file_path',
        'downloads',
    ];

    protected function casts(): array
    {
        return [
            'board' => Board::class,
            'class_level' => ClassLevel::class,
            'subject' => Subject::class,
        ];
    }
}
