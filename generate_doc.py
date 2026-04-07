from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

doc = Document()

# -- Styles --
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)
style.paragraph_format.space_after = Pt(6)

for level in range(1, 4):
    h = doc.styles[f'Heading {level}']
    h.font.name = 'Calibri'
    h.font.color.rgb = RGBColor(30, 58, 138)

def add_code(text, lang=""):
    """Add a code block with gray background feel"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(40, 40, 40)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Inches(0.3)
    return p

def add_note(text):
    p = doc.add_paragraph()
    run = p.add_run("NOTE: ")
    run.bold = True
    run.font.color.rgb = RGBColor(180, 80, 0)
    run = p.add_run(text)
    run.font.color.rgb = RGBColor(100, 100, 100)
    run.font.size = Pt(10)

def add_step(num, text):
    p = doc.add_paragraph()
    run = p.add_run(f"Step {num}: ")
    run.bold = True
    p.add_run(text)

def section_break():
    doc.add_paragraph("─" * 70)

# ============================================================
# TITLE PAGE
# ============================================================
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("\n\n\n\nEternal Sunshine")
run.font.size = Pt(36)
run.bold = True
run.font.color.rgb = RGBColor(30, 58, 138)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Project Code Manual & Documentation")
run.font.size = Pt(18)
run.font.color.rgb = RGBColor(100, 100, 100)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("\nLaravel 13 + Inertia.js v3 + React 19 + Tailwind CSS v4")
run.font.size = Pt(12)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("\n\nA step-by-step guide for every feature")
run.font.size = Pt(13)
run.italic = True

doc.add_page_break()

# ============================================================
# TABLE OF CONTENTS (manual)
# ============================================================
doc.add_heading("Table of Contents", level=1)
toc_items = [
    "1. Project Overview & How It Works",
    "2. Folder Structure (What Goes Where)",
    "3. Database & Models",
    "4. How Routing Works (The Full Flow)",
    "5. Authentication (Login / Register)",
    "6. Student Pages - Step by Step",
    "   6.1 Dashboard",
    "   6.2 Subject Selection",
    "   6.3 AI Chat",
    "   6.4 Practice Quiz",
    "   6.5 Resources",
    "   6.6 Progress",
    "   6.7 Profile",
    "   6.8 About",
    "7. Admin Pages - Step by Step",
    "   7.1 Admin Dashboard",
    "   7.2 User Management",
    "   7.3 Content Manager",
    "8. Layouts (How Headers & Sidebars Work)",
    "9. Shared Components",
    "10. Adding a New Page (Complete Example)",
    "11. Common Commands You'll Need",
    "12. When Something Goes Wrong",
]
for item in toc_items:
    doc.add_paragraph(item)

doc.add_page_break()

# ============================================================
# 1. PROJECT OVERVIEW
# ============================================================
doc.add_heading("1. Project Overview & How It Works", level=1)

doc.add_paragraph(
    "Eternal Sunshine is an AI-powered learning platform for Pakistani students. "
    "It helps students prepare for board exams with AI chat, practice quizzes, "
    "and downloadable resources."
)

doc.add_heading("Tech Stack", level=2)
doc.add_paragraph("Backend: Laravel 13 (PHP 8.4) — handles routes, auth, database")
doc.add_paragraph("Frontend: React 19 with Inertia.js v3 — renders pages in the browser")
doc.add_paragraph("Styling: Tailwind CSS v4 — utility classes for design")
doc.add_paragraph("Auth: Laravel Fortify — handles login, register, password reset")
doc.add_paragraph("Icons: Font Awesome 6 — icon library (fa-solid fa-house etc)")
doc.add_paragraph("Charts: Recharts — bar charts, pie charts in admin panel")

doc.add_heading("How a page loads (the big picture)", level=2)
doc.add_paragraph(
    "When a user visits /dashboard in their browser, here's what happens:"
)
add_step(1, "Browser sends request to /dashboard")
add_step(2, "Laravel checks routes/web.php and finds the matching route")
add_step(3, "Route points to DashboardController")
add_step(4, "Controller calls inertia('dashboard') — this tells Inertia to load the React page")
add_step(5, "Inertia finds resources/js/pages/dashboard.tsx and renders it")
add_step(6, "The page component shows up in the browser with the layout (header + sidebar)")

add_note("Inertia is the bridge between Laravel (backend) and React (frontend). You write Laravel routes and controllers like normal, but instead of Blade views, you render React components.")

doc.add_page_break()

# ============================================================
# 2. FOLDER STRUCTURE
# ============================================================
doc.add_heading("2. Folder Structure (What Goes Where)", level=1)

doc.add_heading("Backend (PHP)", level=2)
items = [
    ("routes/web.php", "All your page routes go here"),
    ("routes/settings.php", "Settings page routes (profile, security)"),
    ("app/Http/Controllers/", "Controllers — one per page, handles the request"),
    ("app/Http/Controllers/Admin/", "Admin-only controllers"),
    ("app/Models/User.php", "User model — represents the users table"),
    ("app/Http/Middleware/HandleInertiaRequests.php", "Shares data (like logged-in user) with every page"),
    ("database/migrations/", "Database table definitions"),
    ("database/factories/", "Fake data generators for testing"),
    ("config/fortify.php", "Auth configuration (login redirect, features)"),
]
for path, desc in items:
    p = doc.add_paragraph()
    run = p.add_run(path)
    run.bold = True
    run.font.name = 'Consolas'
    run.font.size = Pt(10)
    p.add_run(f"  →  {desc}")

doc.add_heading("Frontend (React/TypeScript)", level=2)
items = [
    ("resources/js/app.tsx", "Entry point — sets up Inertia, layouts, theme"),
    ("resources/js/pages/", "Page components — one .tsx file per page"),
    ("resources/js/pages/auth/", "Login, register, forgot password pages"),
    ("resources/js/pages/admin/", "Admin panel pages"),
    ("resources/js/layouts/student-layout.tsx", "Student header + sidebar layout"),
    ("resources/js/layouts/admin-layout.tsx", "Admin header + sidebar layout"),
    ("resources/js/components/", "Reusable components (logo, cards, etc)"),
    ("resources/css/app.css", "Global CSS + Tailwind config"),
]
for path, desc in items:
    p = doc.add_paragraph()
    run = p.add_run(path)
    run.bold = True
    run.font.name = 'Consolas'
    run.font.size = Pt(10)
    p.add_run(f"  →  {desc}")

doc.add_page_break()

# ============================================================
# 3. DATABASE & MODELS
# ============================================================
doc.add_heading("3. Database & Models", level=1)

doc.add_heading("Users Table", level=2)
doc.add_paragraph(
    "The main table is 'users'. It stores everyone — students and admins. "
    "The 'role' column tells us who is who."
)

doc.add_heading("Users table columns:", level=3)
cols = [
    ("id", "Auto-increment primary key"),
    ("name", "Full name of the user"),
    ("email", "Email address (unique)"),
    ("role", "Either 'student' or 'admin' (defaults to 'student')"),
    ("password", "Hashed password (never stored as plain text)"),
    ("email_verified_at", "When they verified their email (null if not verified)"),
    ("remember_token", "For 'remember me' feature"),
    ("created_at / updated_at", "Timestamps"),
]
for col, desc in cols:
    p = doc.add_paragraph()
    run = p.add_run(col)
    run.bold = True
    p.add_run(f" — {desc}")

doc.add_heading("User Model", level=2)
doc.add_paragraph("File: app/Models/User.php")
add_code("""<?php

namespace App\\Models;

use Database\\Factories\\UserFactory;
use Illuminate\\Database\\Eloquent\\Attributes\\Fillable;
use Illuminate\\Database\\Eloquent\\Attributes\\Hidden;
use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Foundation\\Auth\\User as Authenticatable;
use Illuminate\\Notifications\\Notifiable;
use Laravel\\Fortify\\TwoFactorAuthenticatable;

// Fillable = columns you can mass-assign (create/update)
#[Fillable(['name', 'email', 'password', 'role'])]
// Hidden = columns hidden from JSON responses (security)
#[Hidden(['password', 'two_factor_secret', 'two_factor_recovery_codes', 'remember_token'])]
class User extends Authenticatable
{
    use HasFactory, Notifiable, TwoFactorAuthenticatable;

    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'password' => 'hashed',  // auto-hashes password when you set it
        ];
    }
}""")

doc.add_heading("Migration for role column", level=2)
doc.add_paragraph("File: database/migrations/2026_04_05_131120_add_role_to_users_table.php")
add_code("""<?php

use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('users', function (Blueprint $table) {
            // Add role column after email, default is 'student'
            $table->string('role')->default('student')->after('email');
        });
    }

    public function down(): void
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dropColumn('role');
        });
    }
};""")

add_note("Run 'php artisan migrate' to apply migrations to the database.")

doc.add_heading("How to make a user admin (in terminal)", level=2)
add_code("""php artisan tinker --execute "\\App\\Models\\User::where('email', 'rehandev55@gmail.com')->update(['role' => 'admin']);" """)

doc.add_page_break()

# ============================================================
# 4. HOW ROUTING WORKS
# ============================================================
doc.add_heading("4. How Routing Works (The Full Flow)", level=1)

doc.add_paragraph(
    "This is the most important section. Every page in the app follows the same pattern. "
    "Once you understand this, you can build anything."
)

doc.add_heading("The 3-step flow", level=2)
doc.add_paragraph("1.  Route (routes/web.php)  →  defines the URL")
doc.add_paragraph("2.  Controller (app/Http/Controllers/)  →  handles the logic")
doc.add_paragraph("3.  Page (resources/js/pages/)  →  shows the UI")

doc.add_heading("Example: Dashboard page", level=2)

doc.add_heading("Step 1 — Define the route", level=3)
doc.add_paragraph("File: routes/web.php")
add_code("""// This means: when someone visits /dashboard, call DashboardController
Route::get('dashboard', DashboardController::class)->name('dashboard');""")
doc.add_paragraph(
    "The ->name('dashboard') gives it a name so you can reference it elsewhere. "
    "The ::class syntax means this controller has a single __invoke() method."
)

doc.add_heading("Step 2 — Create the controller", level=3)
doc.add_paragraph("File: app/Http/Controllers/DashboardController.php")
add_code("""<?php

namespace App\\Http\\Controllers;

use Inertia\\Response;

class DashboardController extends Controller
{
    // __invoke runs automatically when the route is hit
    public function __invoke(): Response
    {
        // This loads resources/js/pages/dashboard.tsx
        return inertia('dashboard');
    }
}""")

doc.add_paragraph(
    "The inertia('dashboard') call tells Laravel: \"Send the React component "
    "located at resources/js/pages/dashboard.tsx to the browser.\""
)

doc.add_heading("Step 3 — Create the React page", level=3)
doc.add_paragraph("File: resources/js/pages/dashboard.tsx")
add_code("""import { Link, usePage } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';

export default function Dashboard() {
    // Get the logged-in user from shared data
    const { auth } = usePage().props;
    const user = auth.user;

    return (
        <div className="space-y-8">
            <h2>Welcome back, {user.name}</h2>
            {/* Your page content here */}
        </div>
    );
}

// This wraps the page in the student layout (header + sidebar)
Dashboard.layout = (page) => (
    <StudentLayout currentPage="dashboard">{page}</StudentLayout>
);""")

doc.add_heading("How data flows from backend to frontend", level=2)
doc.add_paragraph("If you need to send data from the controller to the page:")
add_code("""// In the controller:
public function __invoke(): Response
{
    $users = User::all();  // get all users from database

    return inertia('admin/users', [
        'users' => $users,  // pass as prop
    ]);
}

// In the React page:
export default function Users({ users }) {
    // 'users' is now available as a prop
    return (
        <div>
            {users.map(user => (
                <p key={user.id}>{user.name}</p>
            ))}
        </div>
    );
}""")

doc.add_heading("Route groups explained", level=2)
doc.add_paragraph("File: routes/web.php (full file)")
add_code("""<?php

use App\\Http\\Controllers\\AboutController;
use App\\Http\\Controllers\\Admin\\ContentController;
use App\\Http\\Controllers\\Admin\\DashboardController as AdminDashboardController;
use App\\Http\\Controllers\\Admin\\UserController;
use App\\Http\\Controllers\\AiChatController;
use App\\Http\\Controllers\\DashboardController;
use App\\Http\\Controllers\\PracticeController;
use App\\Http\\Controllers\\ProfileController;
use App\\Http\\Controllers\\ProgressController;
use App\\Http\\Controllers\\ResourceController;
use App\\Http\\Controllers\\SelectionController;
use Illuminate\\Support\\Facades\\Route;
use Laravel\\Fortify\\Features;

// Public page — anyone can see this (no login needed)
Route::inertia('/', 'welcome', [
    'canRegister' => Features::enabled(Features::registration()),
])->name('home');

// Protected pages — must be logged in AND email verified
Route::middleware(['auth', 'verified'])->group(function () {

    // Student pages
    Route::get('dashboard', DashboardController::class)->name('dashboard');
    Route::get('selection', SelectionController::class)->name('selection');
    Route::get('aichat', AiChatController::class)->name('aichat');
    Route::get('practice', PracticeController::class)->name('practice');
    Route::get('resources', ResourceController::class)->name('resources');
    Route::get('progress', ProgressController::class)->name('progress');
    Route::get('profile', ProfileController::class)->name('profile');
    Route::get('about', AboutController::class)->name('about');

    // Admin pages — all URLs start with /admin
    Route::prefix('admin')->name('admin.')->group(function () {
        Route::get('dashboard', AdminDashboardController::class)->name('dashboard');
        Route::get('users', UserController::class)->name('users');
        Route::get('content', ContentController::class)->name('content');
    });
});

require __DIR__.'/settings.php';""")

doc.add_paragraph("What does middleware(['auth', 'verified']) mean?")
doc.add_paragraph("• auth → user must be logged in, otherwise redirect to /login")
doc.add_paragraph("• verified → user must have verified their email")
doc.add_paragraph("• Everything inside the group() is protected by both")

doc.add_page_break()

# ============================================================
# 5. AUTHENTICATION
# ============================================================
doc.add_heading("5. Authentication (Login / Register)", level=1)

doc.add_paragraph(
    "Authentication is handled by Laravel Fortify. You don't write login/register "
    "logic yourself — Fortify does it all. You just provide the pages."
)

doc.add_heading("How login works", level=2)
add_step(1, "User visits /login")
add_step(2, "Fortify shows the login page (resources/js/pages/auth/login.tsx)")
add_step(3, "User fills in email + password, clicks Sign In")
add_step(4, "Form POSTs to /login (Fortify handles this route automatically)")
add_step(5, "Fortify checks credentials, creates session, redirects to /dashboard")

doc.add_heading("Login page", level=2)
doc.add_paragraph("File: resources/js/pages/auth/login.tsx")
add_code("""import { Form, Head, Link } from '@inertiajs/react';
import InputError from '@/components/input-error';
import LogoES from '@/components/logo-es';
import { store } from '@/routes/login';      // Wayfinder-generated route
import { register } from '@/routes';
import { request } from '@/routes/password';

export default function Login({ status, canResetPassword, canRegister }) {
    return (
        <div className="min-h-screen bg-gradient-to-br from-[#1E3A8A] via-[#2563EB] to-[#7C3AED] ...">
            <Head title="Log in" />

            <div className="bg-white rounded-3xl shadow-2xl p-8 w-full max-w-md">
                {/* Logo and heading */}
                <LogoES className="w-8 h-8" />
                <h2>Welcome Back</h2>

                {/* The Form component handles POST automatically */}
                <Form
                    {...store.form()}
                    resetOnSuccess={['password']}
                    className="space-y-5"
                >
                    {({ processing, errors }) => (
                        <>
                            <input name="email" type="email" required />
                            <InputError message={errors.email} />

                            <input name="password" type="password" required />
                            <InputError message={errors.password} />

                            <button type="submit" disabled={processing}>
                                {processing ? 'Signing in...' : 'Sign In'}
                            </button>
                        </>
                    )}
                </Form>
            </div>
        </div>
    );
}""")

doc.add_heading("Register page", level=2)
doc.add_paragraph("File: resources/js/pages/auth/register.tsx")
doc.add_paragraph("Same idea as login. The form POSTs to /register (Fortify handles it).")
add_code("""<Form {...store.form()} resetOnSuccess={['password', 'password_confirmation']}>
    {({ processing, errors }) => (
        <>
            <input name="name" type="text" required />
            <input name="email" type="email" required />
            <input name="password" type="password" required />
            <input name="password_confirmation" type="password" required />
            <button type="submit">Create Account</button>
        </>
    )}
</Form>""")

doc.add_heading("Where Fortify is configured", level=2)
doc.add_paragraph("File: app/Providers/FortifyServiceProvider.php")
doc.add_paragraph("This file tells Fortify which React pages to show for login, register, etc.")
add_code("""// This tells Fortify: for login, render auth/login.tsx page
Fortify::loginView(fn (Request $request) => Inertia::render('auth/login', [
    'canResetPassword' => Features::enabled(Features::resetPasswords()),
    'canRegister' => Features::enabled(Features::registration()),
    'status' => $request->session()->get('status'),
]));

// For register, render auth/register.tsx
Fortify::registerView(fn () => Inertia::render('auth/register'));""")

doc.add_heading("After login redirect", level=2)
doc.add_paragraph("File: config/fortify.php")
add_code("""'home' => '/dashboard',  // After login, user goes to /dashboard""")

doc.add_heading("User roles", level=2)
doc.add_paragraph(
    "Every user has a 'role' column. Default is 'student'. "
    "Admin users have role = 'admin'. "
    "The student layout checks this and shows the Admin button if role is admin."
)

doc.add_page_break()

# ============================================================
# 6. STUDENT PAGES
# ============================================================
doc.add_heading("6. Student Pages — Step by Step", level=1)

doc.add_paragraph(
    "Every student page follows the same pattern. I'll show the full flow for each one."
)

# 6.1 Dashboard
doc.add_heading("6.1 Dashboard", level=2)
doc.add_paragraph("URL: /dashboard")
doc.add_paragraph("Shows greeting, quick action buttons, progress summary, recent activity.")

doc.add_heading("Route:", level=3)
add_code("Route::get('dashboard', DashboardController::class)->name('dashboard');")

doc.add_heading("Controller:", level=3)
doc.add_paragraph("File: app/Http/Controllers/DashboardController.php")
add_code("""class DashboardController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('dashboard');
    }
}""")

doc.add_heading("Page:", level=3)
doc.add_paragraph("File: resources/js/pages/dashboard.tsx")
doc.add_paragraph("Key things in this page:")
doc.add_paragraph("• Uses usePage() to get the logged-in user's name")
doc.add_paragraph("• Quick action cards link to /aichat, /practice, /resources using <Link>")
doc.add_paragraph("• Layout is set to StudentLayout with currentPage='dashboard'")
add_code("""// How to link to another page:
<Link href="/aichat">Ask AI</Link>

// How to get user info:
const { auth } = usePage().props;
const user = auth.user;  // { name, email, role }

// How to set the layout:
Dashboard.layout = (page) => (
    <StudentLayout currentPage="dashboard">{page}</StudentLayout>
);""")

# 6.2 Selection
doc.add_heading("6.2 Subject Selection", level=2)
doc.add_paragraph("URL: /selection")
doc.add_paragraph("User picks their board, class, and subject before using AI chat or practice.")

doc.add_heading("Route:", level=3)
add_code("Route::get('selection', SelectionController::class)->name('selection');")

doc.add_heading("Controller:", level=3)
add_code("""class SelectionController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('selection');
    }
}""")

doc.add_heading("Page:", level=3)
doc.add_paragraph("File: resources/js/pages/selection.tsx")
doc.add_paragraph("Key things:")
doc.add_paragraph("• Three dropdowns: Board (Federal/AJK), Class (9-12), Subject")
doc.add_paragraph("• Sibling toggle lets you browse for someone else")
doc.add_paragraph("• 'Start Learning' button uses router.visit('/aichat') to navigate")
add_code("""import { router } from '@inertiajs/react';

// Programmatic navigation (instead of <Link>):
router.visit('/aichat');""")

# 6.3 AI Chat
doc.add_heading("6.3 AI Chat", level=2)
doc.add_paragraph("URL: /aichat")
doc.add_paragraph("Full-screen chat interface with AI. Has voice input/output support.")

doc.add_heading("Route + Controller:", level=3)
add_code("""// Route
Route::get('aichat', AiChatController::class)->name('aichat');

// Controller just renders the page
return inertia('ai-chat');""")

doc.add_heading("Page:", level=3)
doc.add_paragraph("File: resources/js/pages/ai-chat.tsx")
doc.add_paragraph("Key things:")
doc.add_paragraph("• Uses isChat layout prop for full-height (no scroll on body)")
doc.add_paragraph("• Speech Recognition API for voice input")
doc.add_paragraph("• Speech Synthesis API for reading answers aloud")
doc.add_paragraph("• Currently uses mock responses — you'll connect real AI later")
add_code("""// Full-height layout (no padding, fills screen):
AiChat.layout = (page) => (
    <StudentLayout currentPage="aichat" isChat>{page}</StudentLayout>
);""")

add_note("To connect real AI, replace the sendMessage function's setTimeout with an actual API call to your backend.")

# 6.4 Practice
doc.add_heading("6.4 Practice Quiz", level=2)
doc.add_paragraph("URL: /practice")
doc.add_paragraph("Multi-step quiz: select chapters → pick mode (MCQ/Short/Long) → answer questions.")

doc.add_heading("Route + Controller:", level=3)
add_code("""Route::get('practice', PracticeController::class)->name('practice');

// Controller
return inertia('practice');""")

doc.add_heading("Page:", level=3)
doc.add_paragraph("File: resources/js/pages/practice.tsx")
doc.add_paragraph("Key things:")
doc.add_paragraph("• Contains a full question bank (questionBank object) with 5 subjects")
doc.add_paragraph("• Each subject has MCQ, short, and long questions")
doc.add_paragraph("• Uses the QuestionCard component for displaying questions")
doc.add_paragraph("• 3 screens: chapter selection → mode selection → active quiz → complete")
add_code("""// The question bank structure:
const questionBank = {
    Physics: {
        mcq: [
            { chapter: "Measurements", question: "...", options: [...], correctAnswer: 1, explanation: "..." },
        ],
        short: [
            { chapter: "Kinematics", question: "...", answer: "...", explanation: "..." },
        ],
        long: [...]
    },
    Chemistry: { ... },
    // ... same for Biology, Mathematics, English
};""")

add_note("Right now questions are hardcoded. Later you can store them in a database table and load them from the controller.")

# 6.5 Resources
doc.add_heading("6.5 Resources", level=2)
doc.add_paragraph("URL: /resources")
doc.add_paragraph("Filterable list of downloadable study materials.")

doc.add_heading("Route + Controller:", level=3)
add_code("""Route::get('resources', ResourceController::class)->name('resources');
return inertia('resources');""")

doc.add_heading("Page:", level=3)
doc.add_paragraph("File: resources/js/pages/resources.tsx")
doc.add_paragraph("• Filter by board, class, subject")
doc.add_paragraph("• Uses ResourceCard component for each item")
doc.add_paragraph("• Resources are currently hardcoded in allResources array")

# 6.6 Progress
doc.add_heading("6.6 Progress", level=2)
doc.add_paragraph("URL: /progress")
add_code("""Route::get('progress', ProgressController::class)->name('progress');
return inertia('progress');""")
doc.add_paragraph("Shows stats cards, subject-wise performance bars, and focus areas.")
doc.add_paragraph("All data is hardcoded for now.")

# 6.7 Profile
doc.add_heading("6.7 Profile", level=2)
doc.add_paragraph("URL: /profile")
add_code("""Route::get('profile', ProfileController::class)->name('profile');
return inertia('profile');""")
doc.add_paragraph("Shows user info form and password change form. Currently mock (no backend save).")

add_note("To make profile saving work, you need to add a POST/PATCH route and handle the form submission in the controller. See section 10 for how to add form handling.")

# 6.8 About
doc.add_heading("6.8 About", level=2)
doc.add_paragraph("URL: /about")
add_code("""Route::get('about', AboutController::class)->name('about');
return inertia('about');""")
doc.add_paragraph("Static page with team info, goal, and tech stack.")

doc.add_page_break()

# ============================================================
# 7. ADMIN PAGES
# ============================================================
doc.add_heading("7. Admin Pages — Step by Step", level=1)

doc.add_paragraph(
    "Admin pages live under /admin/... URLs. They use AdminLayout instead of StudentLayout. "
    "Any logged-in user can access them right now — add middleware later to restrict to admin role only."
)

# 7.1 Admin Dashboard
doc.add_heading("7.1 Admin Dashboard", level=2)
doc.add_paragraph("URL: /admin/dashboard")

doc.add_heading("Route:", level=3)
add_code("""Route::prefix('admin')->name('admin.')->group(function () {
    Route::get('dashboard', AdminDashboardController::class)->name('dashboard');
});""")
doc.add_paragraph("This creates the URL /admin/dashboard with route name admin.dashboard")

doc.add_heading("Controller:", level=3)
doc.add_paragraph("File: app/Http/Controllers/Admin/DashboardController.php")
add_code("""<?php

namespace App\\Http\\Controllers\\Admin;

use App\\Http\\Controllers\\Controller;
use Inertia\\Response;

class DashboardController extends Controller
{
    public function __invoke(): Response
    {
        return inertia('admin/dashboard');
        // loads resources/js/pages/admin/dashboard.tsx
    }
}""")

doc.add_heading("Page:", level=3)
doc.add_paragraph("File: resources/js/pages/admin/dashboard.tsx")
doc.add_paragraph("Key things:")
doc.add_paragraph("• Uses recharts for AreaChart (user growth), BarChart (quiz activity), PieChart (subjects)")
doc.add_paragraph("• Stats cards, recent users table, recent content list")
doc.add_paragraph("• All data is mock — later replace with real database queries")
add_code("""import AdminLayout from '@/layouts/admin-layout';

// Admin layout with purple theme
AdminDashboard.layout = (page) => (
    <AdminLayout currentPage="admin-dashboard">{page}</AdminLayout>
);""")

# 7.2 Admin Users
doc.add_heading("7.2 User Management", level=2)
doc.add_paragraph("URL: /admin/users")
add_code("""Route::get('users', UserController::class)->name('users');
return inertia('admin/users');""")
doc.add_paragraph("File: resources/js/pages/admin/users.tsx")
doc.add_paragraph("Features: search, filter by status/class, view/edit/delete modals, block/unblock users.")
doc.add_paragraph("All users are currently mock data in initialUsers array.")

# 7.3 Admin Content
doc.add_heading("7.3 Content Manager", level=2)
doc.add_paragraph("URL: /admin/content")
add_code("""Route::get('content', ContentController::class)->name('content');
return inertia('admin/content');""")
doc.add_paragraph("File: resources/js/pages/admin/content.tsx")
doc.add_paragraph("Features: upload form, search, type filters, edit/delete modals, downloads chart.")

doc.add_page_break()

# ============================================================
# 8. LAYOUTS
# ============================================================
doc.add_heading("8. Layouts (How Headers & Sidebars Work)", level=1)

doc.add_heading("Student Layout", level=2)
doc.add_paragraph("File: resources/js/layouts/student-layout.tsx")
doc.add_paragraph(
    "This layout wraps every student page. It provides the blue header at the top, "
    "the sidebar on the left, and the main content area."
)
add_code("""// What the layout renders:
<div>
    <Header />       {/* Blue gradient bar at top with logo, user menu */}
    <Sidebar />      {/* Left sidebar with navigation links */}
    <main>
        {children}   {/* Your page content goes here */}
    </main>
</div>""")

doc.add_paragraph("The currentPage prop highlights the active item in the sidebar:")
add_code("""// In your page file:
Dashboard.layout = (page) => (
    <StudentLayout currentPage="dashboard">{page}</StudentLayout>
);
// "dashboard" matches the key in the sidebar's menuItems array""")

doc.add_paragraph("Sidebar menu items are defined at the top of the file:")
add_code("""const menuItems = [
    { key: 'dashboard', label: 'Dashboard', icon: 'fa-solid fa-house', href: '/dashboard' },
    { key: 'selection', label: 'Select Subject', icon: 'fa-solid fa-book-open', href: '/selection' },
    { key: 'aichat', label: 'AI Learning', icon: 'fa-solid fa-robot', href: '/aichat' },
    { key: 'practice', label: 'Practice Quiz', icon: 'fa-solid fa-clipboard-check', href: '/practice' },
    { key: 'resources', label: 'Resources', icon: 'fa-solid fa-download', href: '/resources' },
    { key: 'progress', label: 'Progress', icon: 'fa-solid fa-chart-line', href: '/progress' },
    { key: 'about', label: 'About Us', icon: 'fa-solid fa-circle-info', href: '/about' },
];""")

doc.add_heading("Admin Layout", level=2)
doc.add_paragraph("File: resources/js/layouts/admin-layout.tsx")
doc.add_paragraph("Same concept but with purple/dark theme. Has 3 menu items: Dashboard, Users, Content.")

doc.add_heading("How layout assignment works in app.tsx", level=2)
doc.add_paragraph("File: resources/js/app.tsx")
add_code("""layout: (name) => {
    switch (true) {
        case name === 'welcome':       // Landing page — no layout
        case name === 'auth/login':    // Login — has its own full-page design
        case name === 'auth/register': // Register — same
            return null;
        case name.startsWith('auth/'): // Other auth pages (forgot password etc)
            return AuthLayout;
        case name.startsWith('settings/'):
            return [StudentLayout, SettingsLayout];
        default:
            return undefined;  // Let the page decide its own layout
    }
}""")
doc.add_paragraph(
    "When a page has its own .layout property (like Dashboard.layout = ...), "
    "that takes priority over the app.tsx layout function."
)

doc.add_page_break()

# ============================================================
# 9. SHARED COMPONENTS
# ============================================================
doc.add_heading("9. Shared Components", level=1)

doc.add_heading("LogoES", level=2)
doc.add_paragraph("File: resources/js/components/logo-es.tsx")
doc.add_paragraph("The sun + book SVG logo. Used in headers, chat, landing page.")
add_code("""import LogoES from '@/components/logo-es';

<LogoES className="w-8 h-8" />  {/* Pass size with className */}""")

doc.add_heading("QuestionCard", level=2)
doc.add_paragraph("File: resources/js/components/question-card.tsx")
doc.add_paragraph("Handles both MCQ and text-answer questions with submit/next flow.")
add_code("""import QuestionCard from '@/components/question-card';

<QuestionCard
    question="What is the SI unit of force?"
    options={["Joule", "Newton", "Watt", "Pascal"]}
    correctAnswer={1}
    explanation="The SI unit of force is Newton."
    onNext={() => goToNextQuestion()}
/>

{/* For short/long answer (no options): */}
<QuestionCard
    question="Define the term 'base unit'."
    answer="A base unit is a fundamental unit..."
    explanation="There are 7 SI base units."
    onNext={() => goToNextQuestion()}
/>""")

doc.add_heading("ResourceCard", level=2)
doc.add_paragraph("File: resources/js/components/resource-card.tsx")
add_code("""import ResourceCard from '@/components/resource-card';

<ResourceCard
    title="Physics Past Papers 2024"
    description="Complete collection of past board exam papers."
    subject="Physics"
    classLevel="10"
/>""")

doc.add_heading("InputError", level=2)
doc.add_paragraph("File: resources/js/components/input-error.tsx")
doc.add_paragraph("Shows form validation errors from the server.")
add_code("""<InputError message={errors.email} />
{/* Shows red error text if errors.email exists */}""")

doc.add_page_break()

# ============================================================
# 10. ADDING A NEW PAGE
# ============================================================
doc.add_heading("10. Adding a New Page (Complete Example)", level=1)

doc.add_paragraph(
    "Let's say you want to add a 'Notifications' page at /notifications. "
    "Here's exactly what to do, step by step."
)

doc.add_heading("Step 1 — Create the controller", level=2)
doc.add_paragraph("Run this command in terminal:")
add_code("php artisan make:controller NotificationController --no-interaction")
doc.add_paragraph("Then edit app/Http/Controllers/NotificationController.php:")
add_code("""<?php

namespace App\\Http\\Controllers;

use Inertia\\Response;

class NotificationController extends Controller
{
    public function __invoke(): Response
    {
        // If you need data from the database:
        // $notifications = auth()->user()->notifications;
        // return inertia('notifications', ['notifications' => $notifications]);

        return inertia('notifications');
    }
}""")

doc.add_heading("Step 2 — Add the route", level=2)
doc.add_paragraph("In routes/web.php, add inside the auth middleware group:")
add_code("""Route::middleware(['auth', 'verified'])->group(function () {
    // ... existing routes ...
    Route::get('notifications', NotificationController::class)->name('notifications');
});""")

doc.add_heading("Step 3 — Create the page component", level=2)
doc.add_paragraph("Create file: resources/js/pages/notifications.tsx")
add_code("""import { Head, usePage } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';

export default function Notifications() {
    const { auth } = usePage().props;

    return (
        <>
            <Head title="Notifications" />
            <div>
                <h2 className="text-2xl font-bold text-gray-800 dark:text-white">
                    Notifications
                </h2>
                <p className="text-gray-500 mt-2">
                    Hello {auth.user.name}, you have no new notifications.
                </p>
            </div>
        </>
    );
}

Notifications.layout = (page) => (
    <StudentLayout currentPage="notifications">{page}</StudentLayout>
);""")

doc.add_heading("Step 4 — Add to sidebar (optional)", level=2)
doc.add_paragraph("In resources/js/layouts/student-layout.tsx, add to menuItems array:")
add_code("""{ key: 'notifications', label: 'Notifications', icon: 'fa-solid fa-bell', href: '/notifications' },""")

doc.add_heading("Step 5 — Build and test", level=2)
add_code("""npm run build
# Then visit /notifications in your browser""")

doc.add_page_break()

# ============================================================
# 10b. ADDING FORM HANDLING
# ============================================================
doc.add_heading("Bonus: Adding a Form That Saves to Database", level=1)

doc.add_paragraph("Let's say you want the profile page to actually save changes.")

doc.add_heading("Step 1 — Add a POST route", level=2)
add_code("""// routes/web.php
Route::get('profile', ProfileController::class)->name('profile');
Route::post('profile', [ProfileController::class, 'update'])->name('profile.update');""")

doc.add_heading("Step 2 — Update the controller", level=2)
add_code("""<?php

namespace App\\Http\\Controllers;

use Illuminate\\Http\\Request;
use Inertia\\Response;

class ProfileController extends Controller
{
    // Show the page
    public function __invoke(): Response
    {
        return inertia('profile');
    }

    // Handle form submission
    public function update(Request $request)
    {
        // Validate the input
        $validated = $request->validate([
            'name' => 'required|string|max:255',
        ]);

        // Update the user
        $request->user()->update($validated);

        // Redirect back with success message
        return back()->with('success', 'Profile updated!');
    }
}""")

add_note("When using a non-invokable controller (multiple methods), change the route from ::class to [Controller::class, 'methodName'].")

doc.add_heading("Step 3 — Use Inertia Form in the page", level=2)
add_code("""import { useForm } from '@inertiajs/react';

export default function Profile() {
    const { auth } = usePage().props;

    const { data, setData, post, processing, errors } = useForm({
        name: auth.user.name,
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        post('/profile');  // POST to /profile
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                value={data.name}
                onChange={e => setData('name', e.target.value)}
            />
            {errors.name && <p className="text-red-500">{errors.name}</p>}

            <button type="submit" disabled={processing}>
                {processing ? 'Saving...' : 'Save'}
            </button>
        </form>
    );
}""")

doc.add_page_break()

# ============================================================
# 11. COMMON COMMANDS
# ============================================================
doc.add_heading("11. Common Commands You'll Need", level=1)

commands = [
    ("npm run dev", "Start the frontend dev server (auto-reloads on changes)"),
    ("npm run build", "Build frontend for production"),
    ("php artisan serve", "Start Laravel dev server (if not using Herd)"),
    ("php artisan migrate", "Run pending database migrations"),
    ("php artisan migrate:fresh", "Drop all tables and re-run all migrations (loses data!)"),
    ("php artisan make:controller NameController", "Create a new controller"),
    ("php artisan make:model Name -mf", "Create model + migration + factory"),
    ("php artisan make:migration create_xyz_table", "Create a new migration"),
    ("php artisan route:list --except-vendor", "Show all your routes"),
    ("php artisan tinker", "Open interactive PHP shell with your app loaded"),
    ("php artisan test --compact", "Run all tests"),
    ("php artisan test --filter=LoginTest", "Run specific test"),
    ("php vendor/bin/pint", "Format all PHP code"),
]
for cmd, desc in commands:
    p = doc.add_paragraph()
    run = p.add_run(cmd)
    run.bold = True
    run.font.name = 'Consolas'
    run.font.size = Pt(10)
    p.add_run(f"\n{desc}")

doc.add_page_break()

# ============================================================
# 12. TROUBLESHOOTING
# ============================================================
doc.add_heading("12. When Something Goes Wrong", level=1)

problems = [
    (
        "Page shows old content after code change",
        "Run 'npm run build' or make sure 'npm run dev' is running."
    ),
    (
        "Vite manifest error",
        "Run 'npm run build' to generate the manifest file."
    ),
    (
        "404 Not Found for a page",
        "Check routes/web.php — is the route defined? Run 'php artisan route:list' to see all routes."
    ),
    (
        "419 Page Expired",
        "CSRF token issue. Make sure you're using Inertia <Form> or <Link> components, not raw HTML forms."
    ),
    (
        "500 Server Error",
        "Check storage/logs/laravel.log for the actual error message."
    ),
    (
        "Login redirects back to login",
        "Your email might not be verified. Check if 'verified' middleware is on the route."
    ),
    (
        "Changes to PHP not reflected",
        "Clear cache: php artisan optimize:clear"
    ),
    (
        "New migration not working",
        "Run: php artisan migrate"
    ),
    (
        "Admin button not showing",
        "Make sure your user's role is 'admin' in the database. Check with tinker."
    ),
]

for problem, solution in problems:
    p = doc.add_paragraph()
    run = p.add_run(f"Problem: {problem}")
    run.bold = True
    doc.add_paragraph(f"Fix: {solution}")
    doc.add_paragraph("")

section_break()

doc.add_heading("Quick Reference: URL → File Mapping", level=1)
doc.add_paragraph("")

table = doc.add_table(rows=1, cols=3)
table.style = 'Light Grid Accent 1'
hdr = table.rows[0].cells
hdr[0].text = 'URL'
hdr[1].text = 'Controller'
hdr[2].text = 'Page File'

rows_data = [
    ("/", "(inline route)", "pages/welcome.tsx"),
    ("/login", "(Fortify)", "pages/auth/login.tsx"),
    ("/register", "(Fortify)", "pages/auth/register.tsx"),
    ("/dashboard", "DashboardController", "pages/dashboard.tsx"),
    ("/selection", "SelectionController", "pages/selection.tsx"),
    ("/aichat", "AiChatController", "pages/ai-chat.tsx"),
    ("/practice", "PracticeController", "pages/practice.tsx"),
    ("/resources", "ResourceController", "pages/resources.tsx"),
    ("/progress", "ProgressController", "pages/progress.tsx"),
    ("/profile", "ProfileController", "pages/profile.tsx"),
    ("/about", "AboutController", "pages/about.tsx"),
    ("/admin/dashboard", "Admin\\DashboardController", "pages/admin/dashboard.tsx"),
    ("/admin/users", "Admin\\UserController", "pages/admin/users.tsx"),
    ("/admin/content", "Admin\\ContentController", "pages/admin/content.tsx"),
]

for url, ctrl, page in rows_data:
    row = table.add_row().cells
    row[0].text = url
    row[1].text = ctrl
    row[2].text = page

# Make table fonts smaller
for row in table.rows:
    for cell in row.cells:
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(9)
                run.font.name = 'Consolas'

doc.add_paragraph("")
doc.add_paragraph("")
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("— End of Documentation —")
run.italic = True
run.font.color.rgb = RGBColor(150, 150, 150)

# Save
doc.save('D:/projects/fyp/Eternal_Sunshine_Code_Manual.docx')
print("Done! File saved.")
