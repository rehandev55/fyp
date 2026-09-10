<?php

namespace Database\Factories;

use App\Enums\Board;
use App\Enums\ClassLevel;
use App\Enums\Subject;
use App\Models\Content;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends Factory<Content>
 */
class ContentFactory extends Factory
{
    protected $model = Content::class;

    /**
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'title' => fake()->words(2, true),
            'type' => 'Book',
            'board' => fake()->randomElement(Board::cases())->value,
            'class_level' => fake()->randomElement(ClassLevel::cases())->value,
            'subject' => fake()->randomElement(Subject::cases())->value,
            'file_path' => 'contents/'.fake()->lexify('????????????').'.pdf',
            'file_size' => (string) fake()->numberBetween(1000, 5_000_000),
            'downloads' => 0,
        ];
    }

    /**
     * A record whose file is missing from disk, as happens when storage is wiped
     * but the database rows survive.
     */
    public function orphaned(): static
    {
        return $this->state(fn (array $attributes): array => [
            'file_path' => 'contents/does-not-exist.pdf',
        ]);
    }
}
