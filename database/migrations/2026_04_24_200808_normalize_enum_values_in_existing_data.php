<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Support\Facades\DB;

return new class extends Migration
{
    public function up(): void
    {
        $tables = ['users', 'chat_sessions', 'contents'];

        foreach ($tables as $table) {
            // Board
            DB::update("UPDATE `{$table}` SET `board` = 'federal' WHERE `board` = 'Federal Board'");
            DB::update("UPDATE `{$table}` SET `board` = 'ajk' WHERE `board` = 'AJK Board'");

            // Class level
            DB::update("UPDATE `{$table}` SET `class_level` = 'class_9' WHERE `class_level` = '9'");
            DB::update("UPDATE `{$table}` SET `class_level` = 'class_10' WHERE `class_level` = '10'");
            DB::update("UPDATE `{$table}` SET `class_level` = 'class_11' WHERE `class_level` = '11'");
            DB::update("UPDATE `{$table}` SET `class_level` = 'class_12' WHERE `class_level` = '12'");

            // Subject
            DB::update("UPDATE `{$table}` SET `subject` = 'physics' WHERE `subject` = 'Physics'");
            DB::update("UPDATE `{$table}` SET `subject` = 'chemistry' WHERE `subject` = 'Chemistry'");
            DB::update("UPDATE `{$table}` SET `subject` = 'biology' WHERE `subject` = 'Biology'");
            DB::update("UPDATE `{$table}` SET `subject` = 'mathematics' WHERE `subject` = 'Mathematics'");
            DB::update("UPDATE `{$table}` SET `subject` = 'english' WHERE `subject` = 'English'");
            DB::update("UPDATE `{$table}` SET `subject` = 'computer' WHERE `subject` = 'Computer'");
            DB::update("UPDATE `{$table}` SET `subject` = 'urdu' WHERE `subject` = 'Urdu'");
        }
    }

    public function down(): void
    {
        $tables = ['users', 'chat_sessions', 'contents'];

        foreach ($tables as $table) {
            DB::update("UPDATE `{$table}` SET `board` = 'Federal Board' WHERE `board` = 'federal'");
            DB::update("UPDATE `{$table}` SET `board` = 'AJK Board' WHERE `board` = 'ajk'");

            DB::update("UPDATE `{$table}` SET `class_level` = '9' WHERE `class_level` = 'class_9'");
            DB::update("UPDATE `{$table}` SET `class_level` = '10' WHERE `class_level` = 'class_10'");
            DB::update("UPDATE `{$table}` SET `class_level` = '11' WHERE `class_level` = 'class_11'");
            DB::update("UPDATE `{$table}` SET `class_level` = '12' WHERE `class_level` = 'class_12'");

            DB::update("UPDATE `{$table}` SET `subject` = 'Physics' WHERE `subject` = 'physics'");
            DB::update("UPDATE `{$table}` SET `subject` = 'Chemistry' WHERE `subject` = 'chemistry'");
            DB::update("UPDATE `{$table}` SET `subject` = 'Biology' WHERE `subject` = 'biology'");
            DB::update("UPDATE `{$table}` SET `subject` = 'Mathematics' WHERE `subject` = 'mathematics'");
            DB::update("UPDATE `{$table}` SET `subject` = 'English' WHERE `subject` = 'english'");
            DB::update("UPDATE `{$table}` SET `subject` = 'computer' WHERE `subject` = 'Computer'");
            DB::update("UPDATE `{$table}` SET `subject` = 'urdu' WHERE `subject` = 'Urdu'");
        }
    }
};
