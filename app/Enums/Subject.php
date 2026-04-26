<?php

namespace App\Enums;

enum Subject: string
{
    case Physics = 'physics';
    case Chemistry = 'chemistry';
    case Biology = 'biology';
    case Mathematics = 'mathematics';
    case English = 'english';

    public function label(): string
    {
        return match ($this) {
            self::Physics => 'Physics',
            self::Chemistry => 'Chemistry',
            self::Biology => 'Biology',
            self::Mathematics => 'Mathematics',
            self::English => 'English',
        };
    }
}
