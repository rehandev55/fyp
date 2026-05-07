<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('quiz_sessions', function (Blueprint $table) {
            $table->id();

            $table->foreignId('user_id')->constrained()->onDelete('cascade');

            $table->string('subject');
            $table->string('board');
            $table->string('class_level');
            $table->string('question_type');

            $table->string('total_score')->nullable();
            $table->integer('percentage')->nullable();
            $table->string('grade')->nullable();

            $table->json('strong_areas')->nullable();
            $table->json('weak_areas')->nullable();

            $table->text('overall_feedback')->nullable();
            $table->text('study_tip')->nullable();

            $table->timestamp('completed_at')->nullable();

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('quiz_sessions');
    }
};
