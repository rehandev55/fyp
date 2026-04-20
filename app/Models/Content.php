<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Attributes\Guarded;
use Illuminate\Database\Eloquent\Model;

class Content extends Model
{
    //
    // protected $guarded = [];
    protected $fillable = [
        'title',
        'type',
        'board',
        'class_level',
        'subject',
        'file_path',
        'downloads'
    ];
}
