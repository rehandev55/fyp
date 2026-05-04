<?php

namespace App\Enums;

enum Board: string
{
    case Federal = 'federal';
    case Ajk = 'ajk';

    public function label(): string
    {
        return match ($this) {
            self::Federal => 'Federal Board',
            self::Ajk => 'AJK Board',
        };
    }
}
