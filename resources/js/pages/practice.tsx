import { useState,useEffect } from 'react';
import { Head, usePage } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';
import QuestionCard from '@/components/question-card';
import { api } from '@/lib/api';

interface User {
    name: string;
    email: string;
    role?: string;
    subject?: string;
    class_level?: string;
    board?: string;
}

const allSubjects = ['physics', 'chemistry', 'biology', 'mathematics', 'english'];

const chaptersData: Record<string, string[]> = {
    physics: ['Measurements', 'Kinematics', 'Dynamics', 'Work & Energy', 'Waves', 'Light', 'Electricity', 'Magnetism'],
    chemistry: ['Fundamentals of Chemistry', 'Atomic Structure', 'Periodic Table', 'Chemical Bonding', 'States of Matter', 'Solutions', 'Chemical Reactions', 'Acids, Bases & Salts'],
    biology: ['Introduction to Biology', 'Cell Structure', 'Cell Division', 'Enzymes', 'Nutrition', 'Transport', 'Breathing', 'Ecosystem'],
    mathematics: ['Real Numbers', 'Polynomials', 'Linear Equations', 'Quadratic Equations', 'Geometry', 'Trigonometry', 'Statistics', 'Probability'],
    english: ['Comprehension', 'Grammar Basics', 'Tenses', 'Narration', 'Voice', 'Vocabulary', 'Essay Writing', 'Letter Writing'],
};

interface MCQQuestion {
    chapter: string;
    question: string;
    options: string[];
    correctAnswer: number;
    explanation: string;
}

interface WrittenQuestion {
    chapter: string;
    question: string;
    answer: string;
    explanation: string;
}

interface SubjectBank {
    mcq: MCQQuestion[];
    short: WrittenQuestion[];
    long: WrittenQuestion[];
}
type QuizMode = 'mcq' | 'short' | 'long';

export default function Practice() {
    const [profileConfirmed, setProfileConfirmed] = useState(false);
    const { auth } = usePage<{ auth: { user: User } }>().props;
    const user = auth.user;

    const [questions, setQuestions] = useState<any[]>([]);
const [loading, setLoading] = useState(false);

    // Quiz state
    const [chapterScope, setChapterScope] = useState<'whole' | 'selected' | null>(null);
    const [selectedChapters, setSelectedChapters] = useState<string[]>([]);
    const [mode, setMode] = useState<QuizMode | null>(null);
    const [currentQ, setCurrentQ] = useState(0);
    const [finished, setFinished] = useState(false);
    const hasProfile = !!(user?.board && user?.class_level && user?.subject);

const [board, setBoard] = useState('');
const [classLevel, setClassLevel] = useState('');
const [subject, setSubject] = useState('');

const activeSubject = subject;
const activeClass = classLevel;
const activeBoard = board;

useEffect(() => {
    if (user) {
        setBoard(user.board || '');
        setClassLevel(user.class_level || '');
        setSubject(user.subject || '');
    }
}, [user]);

    const hasSelection = !!(activeSubject && activeClass && activeBoard);
    const subjectChapters = hasSelection ? (chaptersData[activeSubject] || []) : [];

    const toggleChapter = (ch: string) => {
        setSelectedChapters((prev) => prev.includes(ch) ? prev.filter((c) => c !== ch) : [...prev, ch]);
    };

    const selectAllChapters = () => {
        setSelectedChapters(selectedChapters.length === subjectChapters.length ? [] : [...subjectChapters]);
    };

    const handleNext = () => {
        currentQ < questions.length - 1 ? setCurrentQ(currentQ + 1) : setFinished(true);
    };
    const resetToMode = () => { setMode(null); setCurrentQ(0); setFinished(false); };
    const resetToChapters = () => { setChapterScope(null); setSelectedChapters([]); setMode(null); setCurrentQ(0); setFinished(false); };

    const modes = [
        { key: 'mcq' as QuizMode, label: 'MCQ', desc: 'Multiple choice questions to test your knowledge', icon: 'fa-solid fa-list-check', gradient: 'from-blue-500 to-indigo-600' },
        { key: 'short' as QuizMode, label: 'Short Questions', desc: 'Brief answer questions for quick review', icon: 'fa-solid fa-pen-to-square', gradient: 'from-emerald-500 to-teal-600' },
        { key: 'long' as QuizMode, label: 'Long Questions', desc: 'Detailed questions for deep understanding', icon: 'fa-solid fa-file-lines', gradient: 'from-purple-500 to-pink-600' },
    ];

    const sel = 'w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white hover:bg-white dark:hover:bg-gray-600 transition';

    // Screen 1: Subject selection
    // if (!hasSelection) {
    if (!profileConfirmed) {
        // console.log(user);
        return (
            <>
                <Head title="Practice Quiz" />
                <div>
                    <div className="text-center mb-8">
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Practice Quiz</h2>
                        <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">Choose your subject and start practicing</p>
                    </div>
                    <div className="max-w-lg mx-auto">


                        {/* Selection dropdowns */}
                        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 space-y-4 mb-6">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Board</label>

                                   <select value={board} onChange={(e) => setBoard(e.target.value)} className={sel}>
                                    <option value="">Select Board</option>
                                    <option value="federal">Federal Board</option>
                                    <option value="ajk">AJK Board</option>
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Class</label>

                                    <select value={classLevel} onChange={(e) => {
    setClassLevel(e.target.value);

}} className={sel}>
                                    <option value="">Select Class</option>
                                    {['class_9', 'class_10', 'class_11', 'class_12'].map((c) => <option key={c} value={c}>Class {c}</option>)}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Subject</label>

                                   <select value={subject} onChange={(e) => setSubject(e.target.value)} className={sel}>
                                    <option value="">Select Subject</option>
                                    {allSubjects.map((s) => <option key={s} value={s}>{s}</option>)}
                                </select>
                            </div>
                        </div>

                        {/* Hand icon card */}
                        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-10 text-center">
                            <div className="w-20 h-20 bg-gradient-to-br from-blue-100 to-indigo-100 dark:from-blue-900/30 dark:to-indigo-900/30 rounded-full flex items-center justify-center mx-auto mb-5">
                                <i className="fa-solid fa-hand-pointer text-[#2563EB] text-3xl" />
                            </div>
                            <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-2">Select Your Subject</h3>
                            <p className="text-gray-500 dark:text-gray-400 text-sm">Choose your board, class, and subject above to start practicing.</p>
                        </div>
                        <button
    onClick={() => setProfileConfirmed(true)}
    disabled={!hasSelection}
    className="w-full mt-6 bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl font-semibold disabled:opacity-40"
>
    Continue
</button>
                    </div>
                </div>
            </>
        );
    }

    // Screen 2: Chapter selection (Whole Book / Select Chapters)
    if (chapterScope === null) {
        return (
            <>
                <Head title="Practice Quiz - Chapters" />
                <div>
                    <div className="text-center mb-8">
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Select Chapters</h2>
                        <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">
                            {activeSubject} — Class {activeClass} — {activeBoard}
                        </p>
                    </div>
                    <div className="max-w-2xl mx-auto space-y-5">
                        <button onClick={() => { setChapterScope('whole'); setSelectedChapters([...subjectChapters]); }} className="w-full bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 text-left hover:shadow-lg hover:-translate-y-1 transition-all duration-300 group flex items-center gap-5">
                            <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg group-hover:scale-110 transition-transform duration-300">
                                <i className="fa-solid fa-book text-white text-xl" />
                            </div>
                            <div className="flex-1">
                                <h3 className="font-bold text-gray-800 dark:text-white text-lg">Whole Book</h3>
                                <p className="text-sm text-gray-500 dark:text-gray-400 mt-0.5">Practice questions from all {subjectChapters.length} chapters</p>
                            </div>
                            <i className="fa-solid fa-chevron-right text-gray-400 group-hover:text-[#2563EB] transition" />
                        </button>

                        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                            <div className="flex items-center gap-5 mb-5">
                                <div className="w-14 h-14 bg-gradient-to-br from-emerald-500 to-teal-600 rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg">
                                    <i className="fa-solid fa-list text-white text-xl" />
                                </div>
                                <div className="flex-1">
                                    <h3 className="font-bold text-gray-800 dark:text-white text-lg">Select Chapters</h3>
                                    <p className="text-sm text-gray-500 dark:text-gray-400 mt-0.5">Choose specific chapters to practice</p>
                                </div>
                            </div>

                            <div className="mb-4">
                                <button onClick={selectAllChapters} className="text-xs font-semibold text-[#2563EB] hover:text-blue-700 transition">
                                    {selectedChapters.length === subjectChapters.length ? 'Deselect All' : 'Select All'}
                                </button>
                            </div>

                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-5">
                                {subjectChapters.map((ch, i) => (
                                    <button
                                        key={ch}
                                        onClick={() => toggleChapter(ch)}
                                        className={`flex items-center gap-3 px-4 py-3 rounded-xl border-2 text-sm font-medium transition-all duration-200 text-left ${
                                            selectedChapters.includes(ch)
                                                ? 'border-[#2563EB] bg-blue-50 dark:bg-blue-900/30 text-[#2563EB]'
                                                : 'border-gray-200 dark:border-gray-600 text-gray-600 dark:text-gray-300 hover:border-blue-300 hover:bg-blue-50/50 dark:hover:bg-blue-900/20'
                                        }`}
                                    >
                                        <span className={`w-6 h-6 rounded-md flex items-center justify-center text-xs flex-shrink-0 ${
                                            selectedChapters.includes(ch) ? 'bg-[#2563EB] text-white' : 'bg-gray-100 dark:bg-gray-700 text-gray-400'
                                        }`}>
                                            {selectedChapters.includes(ch) ? <i className="fa-solid fa-check text-xs" /> : (i + 1)}
                                        </span>
                                        {ch}
                                    </button>
                                ))}
                            </div>

                            <button
                                onClick={() => { if (selectedChapters.length > 0) setChapterScope('selected'); }}
                                disabled={selectedChapters.length === 0}
                                className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg disabled:opacity-40 disabled:cursor-not-allowed disabled:shadow-none transition-all duration-200 text-sm font-semibold flex items-center justify-center gap-2"
                            >
                                Continue with {selectedChapters.length} chapter{selectedChapters.length !== 1 ? 's' : ''} <i className="fa-solid fa-arrow-right" />
                            </button>
                        </div>
                    </div>
                </div>
            </>
        );
    }

    // Screen 3: Quiz mode selection (MCQ / Short / Long)
    if (!mode) {
        return (
            <>
                <Head title="Practice Quiz" />
                <div>
                    <div className="text-center mb-8">
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Practice Quiz</h2>
                        <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">Choose a quiz mode</p>
                    </div>
                    <div className="grid gap-5 max-w-2xl mx-auto">
                        {modes.map((m) => {
                            // const count = getFilteredQuestions(m.key).length;
                            const count = 10; // or any default number
                            return (
                                <button key={m.key} onClick={async () => {
    setMode(m.key);
   setLoading(true);

try {
    const res = await api('/quiz/generate', {
        method: 'POST',
        body: JSON.stringify({
            topic: (chapterScope === 'whole'
        ? subjectChapters.join(', ')
        : selectedChapters.join(', ')
    ),
            board: activeBoard,
            class_level: activeClass,
            subject: activeSubject,
            chapters: chapterScope === 'whole' ? subjectChapters : selectedChapters,
            question_type: m.key,
            num_questions: 10
        })
    });

    const data = await res.json();

    console.log(data); // debug once

    // setQuestions(data.questions || []);
    setQuestions(Array.isArray(data.questions) ? data.questions : []);
} catch (err) {
    console.error(err);
} finally {
    setLoading(false);
}
    // ${count === 0 ? 'opacity-50 cursor-not-allowed hover:shadow-sm hover:translate-y-0' : ''}
}} disabled={false} className={`bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 text-left hover:shadow-lg hover:-translate-y-1 transition-all duration-300 group flex items-center gap-5 `}>
                                    <div className={`w-14 h-14 bg-gradient-to-br ${m.gradient} rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg group-hover:scale-110 transition-transform duration-300`}>
                                        <i className={`${m.icon} text-white text-xl`} />
                                    </div>
                                    <div className="flex-1">
                                        <h3 className="font-bold text-gray-800 dark:text-white text-lg">{m.label}</h3>
                                        <p className="text-sm text-gray-500 dark:text-gray-400 mt-0.5">{m.desc}</p>
                                    </div>
                                    <span className={`text-xs px-3 py-1.5 rounded-full font-semibold ${count > 0 ? 'bg-blue-50 dark:bg-blue-900/30 text-[#2563EB]' : 'bg-gray-100 dark:bg-gray-700 text-gray-400'}`}>{count} Qs</span>
                                </button>
                            );
                        })}
                        <button onClick={resetToChapters} className="text-sm text-gray-500 hover:text-[#2563EB] transition mt-2 flex items-center justify-center gap-1">
                            <i className="fa-solid fa-chevron-left text-xs" />
                            Change chapters
                        </button>
                    </div>
                </div>
            </>
        );
    }

    // Quiz complete
    if (finished) {
        return (
            <>
                <Head title="Practice Quiz" />
                <div className="max-w-md mx-auto text-center">
                    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-10">
                        <div className="w-20 h-20 bg-gradient-to-br from-emerald-400 to-teal-500 rounded-full flex items-center justify-center mx-auto mb-5 shadow-lg">
                            <i className="fa-solid fa-check text-white text-3xl" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-white mb-2">Quiz Complete!</h2>
                        <p className="text-gray-500 dark:text-gray-400 mb-6">You completed all {questions.length} questions.</p>
                        <div className="flex gap-3">
                            <button onClick={() => { setCurrentQ(0); setFinished(false); }} className="flex-1 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-3 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition text-sm font-semibold">Retry</button>
                            <button onClick={resetToChapters} className="flex-1 bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg transition text-sm font-semibold">New Quiz</button>
                        </div>
                    </div>
                </div>
            </>
        );
    }
    // Show loading while fetching AI questions
if (loading) {
    return (
        <div className="text-center mt-20">
            Generating Questions...
        </div>
    );
}

    // Active quiz
    return (
        <>
           <Head title="Practice Quiz" />
            <div>
                <div className="flex items-center justify-between mb-6">
                    <div className="flex items-center gap-3">
                        <button onClick={resetToMode} className="w-10 h-10 bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-600 flex items-center justify-center hover:bg-gray-50 dark:hover:bg-gray-700 transition">
                            <i className="fa-solid fa-chevron-left text-gray-600 dark:text-gray-300 text-sm" />
                        </button>
                        <div>
                            <h2 className="text-lg font-bold text-gray-800 dark:text-white">{mode === 'mcq' ? 'MCQ' : mode === 'short' ? 'Short Questions' : 'Long Questions'}</h2>
                            <p className="text-xs text-gray-400 dark:text-gray-500">Question {currentQ + 1} of {questions.length}</p>
                        </div>
                    </div>
                    <div className="hidden sm:flex items-center gap-3">
                        <div className="w-32 bg-gray-100 dark:bg-gray-700 rounded-full h-2">
                            <div className="bg-gradient-to-r from-[#2563EB] to-[#3B82F6] h-2 rounded-full transition-all duration-500" style={{ width: `${(currentQ / questions.length) * 100}%` }} />
                        </div>
                        <span className="text-xs font-semibold text-gray-500 dark:text-gray-400">{Math.round((currentQ / questions.length) * 100)}%</span>
                    </div>
                </div>
                {/* <QuestionCard {...questions[currentQ]} onNext={handleNext} /> */}
                {questions[currentQ] && (
    <QuestionCard {...questions[currentQ]} onNext={handleNext} />
)}
            </div>
        </>
    );
}

Practice.layout = (page: React.ReactNode) => <StudentLayout currentPage="practice">{page}</StudentLayout>;
