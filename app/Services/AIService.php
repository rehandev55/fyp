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

    public function chat(string $question, string $board, string $classLevel, string $subject, $chatHistory = []): string
    {
        $response = Http::post("{$this->baseUrl}/chat", [
            'question' => $question,
            'board' => $board,
            'class_level' => $classLevel,
            'subject' => $subject,
            'chat_history' => $chatHistory,
        ]);

        $data = $response->json();

        // dd($data);

        return $data['reply'] ?? $data['answer'] ?? 'No response';
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
