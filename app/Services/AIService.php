<?php

namespace App\Services;

use Illuminate\Support\Facades\Http;

class AIService
{
    private string $baseUrl;

    public function __construct()
    {
        $this->baseUrl = config('services.ai.url');
    }

    public function chat(string $question, string $board, string $classLevel, string $subject, $chatHistory = [], $existingSummary = null): array
    {
        $response = Http::post("{$this->baseUrl}/chat", [
            'question' => $question,
            'board' => $board,
            'class_level' => $classLevel,
            'subject' => $subject,
            'chat_history' => $chatHistory,
            'existing_summary' => $existingSummary ?? '',
        ]);
        // dd($response->body());
        $data = $response->json();

        // dd($data);

        return [
            'reply' => $data['reply'] ?? $data['answer'] ?? 'No response',
            'updated_summary' => $data['updated_summary'] ?? null,
        ];
    }

    public function generateQuiz(array $params): array
    {
        $response = Http::post("{$this->baseUrl}/quiz/generate", $params);

        return $response->json();
    }

    public function evaluateQuiz(array $params): array
    {
        $response = Http::post("{$this->baseUrl}/quiz/evaluate", $params);

        return $response->json();
    }
}
