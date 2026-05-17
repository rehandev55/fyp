<?php

namespace App\Enums;

enum Subject: string
{
    case Physics = 'physics';
    case Chemistry = 'chemistry';
    case Biology = 'biology';
    case Mathematics = 'mathematics';
    case English = 'english';
    case Computer = 'computer';
    case Urdu = 'urdu';

    public function label(): string
    {
        return match ($this) {
            self::Physics => 'Physics',
            self::Chemistry => 'Chemistry',
            self::Biology => 'Biology',
            self::Mathematics => 'Mathematics',
            self::English => 'English',
            self::Computer => 'Computer',
            self::Urdu => 'Urdu',
        };
    }
}
