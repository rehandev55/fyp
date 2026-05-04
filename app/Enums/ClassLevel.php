<?php

namespace App\Enums;

enum ClassLevel: string
{
    case Class9 = 'class_9';
    case Class10 = 'class_10';
    case Class11 = 'class_11';
    case Class12 = 'class_12';

    public function label(): string
    {
        return match ($this) {
            self::Class9 => 'Class 9',
            self::Class10 => 'Class 10',
            self::Class11 => 'Class 11',
            self::Class12 => 'Class 12',
        };
    }
}
