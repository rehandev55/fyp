import { Head, Link } from '@inertiajs/react';
import LogoES from '@/components/logo-es';
import { useAppearance } from '@/hooks/use-appearance';

export default function Welcome() {
    const { resolvedAppearance, updateAppearance } = useAppearance();
    const isDark = resolvedAppearance === 'dark';
    const toggleDark = () => updateAppearance(isDark ? 'light' : 'dark');

    const features = [
        {
            title: 'AI Chat Learning',
            desc: 'Get instant AI-powered explanations for any topic in your syllabus. Ask questions and learn interactively.',
            icon: 'fa-solid fa-robot',
            color: 'from-blue-500 to-indigo-600',
            bg: 'bg-blue-50 dark:bg-blue-900/30',
        },
        {
            title: 'Practice Questions',
            desc: 'Test your knowledge with MCQs, short and long questions aligned to your board syllabus.',
            icon: 'fa-solid fa-clipboard-check',
            color: 'from-emerald-500 to-teal-600',
            bg: 'bg-emerald-50 dark:bg-emerald-900/30',
        },
        {
            title: 'Voice-Enabled AI',
            desc: 'Speak your questions and hear answers read aloud. Learn naturally with voice interaction.',
            icon: 'fa-solid fa-microphone',
            color: 'from-purple-500 to-pink-600',
            bg: 'bg-purple-50 dark:bg-purple-900/30',
        },
        {
            title: 'Downloadable Resources',
            desc: 'Access past papers, key books, and notes for your board exams anytime, anywhere.',
            icon: 'fa-solid fa-book-open',
            color: 'from-orange-500 to-amber-600',
            bg: 'bg-orange-50 dark:bg-orange-900/30',
        },
        {
            title: 'Progress Tracking',
            desc: 'Monitor your learning journey with detailed stats and subject-wise performance insights.',
            icon: 'fa-solid fa-chart-line',
            color: 'from-cyan-500 to-blue-600',
            bg: 'bg-cyan-50 dark:bg-cyan-900/30',
        },
        {
            title: 'Chapter-wise Practice',
            desc: 'Select specific chapters or the whole book to practice. Focus on your weak areas.',
            icon: 'fa-solid fa-list-check',
            color: 'from-rose-500 to-red-600',
            bg: 'bg-rose-50 dark:bg-rose-900/30',
        },
    ];

    const boards = [
        {
            name: 'Federal Board (FBISE)',
            desc: 'Complete syllabus coverage for Federal Board of Intermediate and Secondary Education',
            icon: 'fa-solid fa-landmark',
            color: 'from-blue-600 to-indigo-700',
        },
        {
            name: 'Punjab Board',
            desc: 'Aligned with all Punjab Board of Intermediate and Secondary Education syllabi',
            icon: 'fa-solid fa-building-columns',
            color: 'from-emerald-600 to-teal-700',
        },
    ];

    const steps = [
        {
            step: '01',
            title: 'Select Your Board & Class',
            desc: 'Choose your education board and class level to get a personalized learning experience.',
            icon: 'fa-solid fa-graduation-cap',
            color: 'from-blue-500 to-indigo-600',
        },
        {
            step: '02',
            title: 'Pick a Subject & Chapter',
            desc: 'Browse subjects and select specific chapters or topics you want to study.',
            icon: 'fa-solid fa-book',
            color: 'from-emerald-500 to-teal-600',
        },
        {
            step: '03',
            title: 'Learn with AI',
            desc: 'Chat with our AI tutor, practice questions, or download resources. Learn at your own pace.',
            icon: 'fa-solid fa-wand-magic-sparkles',
            color: 'from-purple-500 to-pink-600',
        },
    ];

    return (
        <>
            <Head title="Welcome">
                <link rel="preconnect" href="https://fonts.bunny.net" />
                <link
                    href="https://fonts.bunny.net/css?family=instrument-sans:400,500,600"
                    rel="stylesheet"
                />
            </Head>
            <div className="min-h-screen bg-[#F8FAFC] transition-colors dark:bg-gray-900">
                {/* Navbar */}
                <nav className="sticky top-0 z-50 border-b border-gray-100 bg-white/80 backdrop-blur-md dark:border-gray-700 dark:bg-gray-800/80">
                    <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
                        <div className="flex items-center gap-2">
                            <LogoES className="h-8 w-8" />
                            <span className="text-lg font-bold text-gray-800 dark:text-white">Eternal Sunshine</span>
                        </div>
                        <div className="flex items-center gap-3">
                            <button
                                onClick={toggleDark}
                                className="rounded-xl p-2 transition hover:bg-gray-100 dark:hover:bg-gray-700"
                                title={isDark ? 'Light Mode' : 'Dark Mode'}
                            >
                                <i className={`${isDark ? 'fa-solid fa-sun text-yellow-400' : 'fa-solid fa-moon text-gray-500'} text-base`} />
                            </button>
                            <Link
                                href="/login"
                                className="px-4 py-2 text-sm font-medium text-gray-600 transition hover:text-[#2563EB] dark:text-gray-300"
                            >
                                Login
                            </Link>
                            <Link
                                href="/register"
                                className="rounded-xl bg-gradient-to-r from-[#2563EB] to-[#3B82F6] px-5 py-2 text-sm font-medium text-white transition-all duration-200 hover:shadow-lg hover:shadow-blue-200 dark:hover:shadow-blue-900/30"
                            >
                                Get Started
                            </Link>
                        </div>
                    </div>
                </nav>

                {/* Hero */}
                <section className="relative overflow-hidden">
                    <div className="absolute inset-0 bg-gradient-to-br from-[#1E3A8A] via-[#2563EB] to-[#7C3AED]" />
                    <div className="absolute inset-0">
                        <div
                            className="absolute left-10 top-20 h-72 w-72 animate-pulse rounded-full bg-yellow-300/10 blur-3xl"
                            style={{ animationDuration: '4s' }}
                        />
                        <div
                            className="absolute bottom-10 right-10 h-96 w-96 animate-pulse rounded-full bg-blue-300/10 blur-3xl"
                            style={{ animationDuration: '6s' }}
                        />
                        <div className="absolute left-1/2 top-1/2 h-[600px] w-[600px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-purple-300/5 blur-3xl" />
                    </div>
                    <div className="pointer-events-none absolute inset-0 overflow-hidden">
                        <div
                            className="absolute left-[15%] top-32 h-3 w-3 animate-bounce rounded-full bg-yellow-300/30"
                            style={{ animationDuration: '3s' }}
                        />
                        <div
                            className="absolute right-[20%] top-48 h-2 w-2 animate-bounce rounded-full bg-blue-300/40"
                            style={{ animationDuration: '2.5s', animationDelay: '0.5s' }}
                        />
                        <div
                            className="absolute bottom-32 left-[25%] h-4 w-4 animate-bounce rounded-full bg-purple-300/20"
                            style={{ animationDuration: '3.5s', animationDelay: '1s' }}
                        />
                    </div>
                    <div className="relative mx-auto max-w-6xl px-6 py-24 text-center text-white md:py-36">
                        <div className="mb-8 inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/10 px-5 py-2.5 text-sm backdrop-blur-sm">
                            <LogoES className="h-5 w-5" />
                            <span>AI-Powered Education Platform</span>
                            <span className="h-2 w-2 animate-pulse rounded-full bg-emerald-400" />
                        </div>
                        <h1 className="mb-6 text-4xl font-extrabold leading-tight tracking-tight md:text-6xl lg:text-7xl">
                            Eternal{' '}
                            <span className="bg-gradient-to-r from-yellow-200 via-yellow-300 to-amber-400 bg-clip-text text-transparent">
                                Sunshine
                            </span>
                        </h1>
                        <p className="mx-auto mb-12 max-w-2xl text-lg leading-relaxed text-blue-100 md:text-xl">
                            AI-Powered Learning Assistant for Pakistani Students. Prepare for board exams with intelligent tools
                            designed for your syllabus.
                        </p>
                        <div className="flex flex-wrap justify-center gap-4">
                            <Link
                                href="/register"
                                className="group flex items-center gap-2 rounded-2xl bg-white px-8 py-4 text-sm font-semibold text-[#2563EB] transition-all duration-200 hover:-translate-y-0.5 hover:shadow-xl hover:shadow-blue-900/20"
                            >
                                Get Started Free
                                <i className="fa-solid fa-arrow-right transition-transform group-hover:translate-x-1" />
                            </Link>
                            <Link
                                href="/login"
                                className="rounded-2xl border-2 border-white/30 px-8 py-4 text-sm font-semibold text-white backdrop-blur-sm transition-all duration-200 hover:-translate-y-0.5 hover:bg-white/10"
                            >
                                Sign In
                            </Link>
                        </div>
                        <div className="mx-auto mt-20 grid max-w-lg grid-cols-3 gap-8">
                            {[
                                { num: '2', label: 'Board Syllabi' },
                                { num: '5+', label: 'Subjects' },
                                { num: '100%', label: 'Free Access' },
                            ].map((s) => (
                                <div
                                    key={s.label}
                                    className="rounded-2xl border border-white/10 bg-white/5 p-4 backdrop-blur-sm"
                                >
                                    <p className="text-2xl font-bold text-yellow-300 md:text-3xl">{s.num}</p>
                                    <p className="mt-1 text-xs text-blue-200">{s.label}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                </section>

                {/* Features */}
                <section className="mx-auto max-w-6xl px-6 py-24">
                    <div className="mb-16 text-center">
                        <span className="rounded-full bg-blue-50 px-4 py-1.5 text-sm font-semibold text-[#2563EB] dark:bg-blue-900/30">
                            Features
                        </span>
                        <h2 className="mt-5 text-3xl font-bold text-gray-800 md:text-4xl dark:text-white">
                            Everything You Need to Excel
                        </h2>
                        <p className="mx-auto mt-3 max-w-xl text-gray-500 dark:text-gray-400">
                            Powerful tools designed specifically for Pakistani board exam preparation
                        </p>
                    </div>
                    <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                        {features.map((f, i) => (
                            <div
                                key={i}
                                className="group relative overflow-hidden rounded-2xl border border-gray-100 bg-white p-7 shadow-sm transition-all duration-300 hover:-translate-y-2 hover:shadow-xl dark:border-gray-700 dark:bg-gray-800"
                            >
                                <div
                                    className={`absolute right-0 top-0 h-32 w-32 -translate-y-10 translate-x-10 rounded-full bg-gradient-to-br ${f.color} opacity-5 blur-2xl transition-opacity duration-300 group-hover:opacity-10`}
                                />
                                <div
                                    className={`mb-5 flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br ${f.color} shadow-lg transition-all duration-300 group-hover:scale-110 group-hover:shadow-xl`}
                                >
                                    <i className={`${f.icon} text-xl text-white`} />
                                </div>
                                <h3 className="relative mb-2 text-lg font-bold text-gray-800 dark:text-white">{f.title}</h3>
                                <p className="relative text-sm leading-relaxed text-gray-500 dark:text-gray-400">{f.desc}</p>
                            </div>
                        ))}
                    </div>
                </section>

                {/* Boards */}
                <section className="bg-gray-50 py-24 dark:bg-gray-800/50">
                    <div className="mx-auto max-w-6xl px-6">
                        <div className="mb-16 text-center">
                            <span className="rounded-full bg-emerald-50 px-4 py-1.5 text-sm font-semibold text-emerald-600 dark:bg-emerald-900/30">
                                Supported Boards
                            </span>
                            <h2 className="mt-5 text-3xl font-bold text-gray-800 md:text-4xl dark:text-white">
                                Pakistani Education Boards
                            </h2>
                            <p className="mx-auto mt-3 max-w-xl text-gray-500 dark:text-gray-400">
                                Content aligned with official syllabi from major education boards
                            </p>
                        </div>
                        <div className="mx-auto grid max-w-3xl gap-6 md:grid-cols-2">
                            {boards.map((b, i) => (
                                <div
                                    key={i}
                                    className="group relative overflow-hidden rounded-2xl border border-gray-100 bg-white p-8 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl dark:border-gray-700 dark:bg-gray-800"
                                >
                                    <div
                                        className={`absolute right-0 top-0 h-40 w-40 -translate-y-16 translate-x-16 rounded-full bg-gradient-to-br ${b.color} opacity-5 blur-2xl transition-opacity duration-300 group-hover:opacity-10`}
                                    />
                                    <div
                                        className={`mb-5 flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br ${b.color} shadow-lg transition-all duration-300 group-hover:scale-110`}
                                    >
                                        <i className={`${b.icon} text-2xl text-white`} />
                                    </div>
                                    <h3 className="relative mb-2 text-xl font-bold text-gray-800 dark:text-white">{b.name}</h3>
                                    <p className="relative text-sm leading-relaxed text-gray-500 dark:text-gray-400">{b.desc}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                </section>

                {/* How It Works */}
                <section className="mx-auto max-w-6xl px-6 py-24">
                    <div className="mb-16 text-center">
                        <span className="rounded-full bg-purple-50 px-4 py-1.5 text-sm font-semibold text-purple-600 dark:bg-purple-900/30">
                            How It Works
                        </span>
                        <h2 className="mt-5 text-3xl font-bold text-gray-800 md:text-4xl dark:text-white">
                            Start Learning in 3 Steps
                        </h2>
                        <p className="mx-auto mt-3 max-w-xl text-gray-500 dark:text-gray-400">
                            Getting started is simple. Follow these steps and begin your learning journey.
                        </p>
                    </div>
                    <div className="mx-auto grid max-w-4xl gap-8 md:grid-cols-3">
                        {steps.map((s, i) => (
                            <div key={i} className="relative text-center">
                                {i < steps.length - 1 && (
                                    <div className="absolute left-1/2 top-12 hidden h-0.5 w-full bg-gradient-to-r from-gray-200 to-transparent md:block dark:from-gray-700" />
                                )}
                                <div
                                    className={`relative mx-auto mb-6 flex h-24 w-24 items-center justify-center rounded-3xl bg-gradient-to-br ${s.color} shadow-lg`}
                                >
                                    <i className={`${s.icon} text-3xl text-white`} />
                                    <span className="absolute -right-2 -top-2 flex h-8 w-8 items-center justify-center rounded-full bg-white text-xs font-bold text-gray-800 shadow-md dark:bg-gray-800 dark:text-white">
                                        {s.step}
                                    </span>
                                </div>
                                <h3 className="mb-2 text-lg font-bold text-gray-800 dark:text-white">{s.title}</h3>
                                <p className="text-sm leading-relaxed text-gray-500 dark:text-gray-400">{s.desc}</p>
                            </div>
                        ))}
                    </div>
                </section>

                {/* CTA */}
                <section className="mx-auto max-w-6xl px-6 pb-24">
                    <div className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-[#1E3A8A] via-[#2563EB] to-[#7C3AED] p-12 text-center md:p-20">
                        <div className="absolute inset-0">
                            <div className="absolute left-10 top-10 h-40 w-40 animate-pulse rounded-full bg-yellow-300/10 blur-3xl" />
                            <div className="absolute bottom-10 right-10 h-56 w-56 animate-pulse rounded-full bg-blue-300/10 blur-3xl" />
                        </div>
                        <div className="relative">
                            <h2 className="mb-4 text-3xl font-bold text-white md:text-4xl">
                                Ready to Start Your Learning Journey?
                            </h2>
                            <p className="mx-auto mb-8 max-w-xl text-blue-100">
                                Join thousands of Pakistani students who are already using AI to prepare for their board exams.
                                It's completely free.
                            </p>
                            <Link
                                href="/register"
                                className="group inline-flex items-center gap-2 rounded-2xl bg-white px-8 py-4 text-sm font-semibold text-[#2563EB] transition-all duration-200 hover:-translate-y-0.5 hover:shadow-xl hover:shadow-blue-900/20"
                            >
                                Get Started Free
                                <i className="fa-solid fa-arrow-right transition-transform group-hover:translate-x-1" />
                            </Link>
                        </div>
                    </div>
                </section>

                {/* Footer */}
                <footer className="border-t border-gray-100 bg-white py-12 dark:border-gray-700 dark:bg-gray-800">
                    <div className="mx-auto max-w-6xl px-6">
                        <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
                            <div className="flex items-center gap-2">
                                <LogoES className="h-6 w-6" />
                                <span className="font-bold text-gray-800 dark:text-white">Eternal Sunshine</span>
                            </div>
                            <p className="text-sm text-gray-500 dark:text-gray-400">
                                &copy; {new Date().getFullYear()} Eternal Sunshine. Built for Pakistani students.
                            </p>
                        </div>
                    </div>
                </footer>
            </div>
        </>
    );
}
