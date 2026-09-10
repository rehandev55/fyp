<?php

use App\Models\Content;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Storage;

uses(RefreshDatabase::class);

beforeEach(function () {
    Storage::fake('public');
    $this->actingAs(User::factory()->create(), 'sanctum');
});

it('downloads a stored file using a readable filename', function () {
    Storage::disk('public')->put('contents/hashed-name.pdf', 'pdf-bytes');

    $content = Content::factory()->create([
        'title' => 'Maths Book',
        'file_path' => 'contents/hashed-name.pdf',
    ]);

    $response = $this->get("/api/content/download/{$content->id}");

    $response->assertOk();
    expect($response->headers->get('content-disposition'))->toContain('maths-book.pdf');
});

it('returns 404 instead of erroring when the file is missing from disk', function () {
    $content = Content::factory()->orphaned()->create();

    $response = $this->get("/api/content/download/{$content->id}");

    $response->assertNotFound();
    $response->assertJson(['success' => false]);
});

it('does not count a download when the file is missing', function () {
    $content = Content::factory()->orphaned()->create(['downloads' => 7]);

    $this->get("/api/content/download/{$content->id}")->assertNotFound();

    expect($content->fresh()->downloads)->toBe(7);
});

it('counts a download when the file is served', function () {
    Storage::disk('public')->put('contents/real.pdf', 'pdf-bytes');

    $content = Content::factory()->create([
        'file_path' => 'contents/real.pdf',
        'downloads' => 3,
    ]);

    $this->get("/api/content/download/{$content->id}")->assertOk();

    expect($content->fresh()->downloads)->toBe(4);
});

it('records the file size when uploading content', function () {
    $file = UploadedFile::fake()->create('algebra.pdf', 120, 'application/pdf');

    $response = $this->postJson('/api/content', [
        'title' => 'Algebra',
        'type' => 'Book',
        'board' => 'federal',
        'class_level' => 'class_10',
        'subject' => 'mathematics',
        'file' => $file,
    ]);

    $response->assertOk();

    $content = Content::firstOrFail();

    expect($content->file_size)->not->toBeNull()
        ->and(Storage::disk('public')->exists($content->file_path))->toBeTrue();
});
