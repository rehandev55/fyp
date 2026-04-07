import { useState } from 'react';
import { Head, usePage, router } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';

interface User {
    name: string;
    email: string;
    role?: string;
    subject?: string;
    classLevel?: string;
    board?: string;
}

const subjects = ['Physics', 'Chemistry', 'Biology', 'Mathematics', 'English'];

export default function Selection() {
    const { auth } = usePage<{ auth: { user: User } }>().props;
    const user = auth.user;

    const [forSibling, setForSibling] = useState(false);
    const [board, setBoard] = useState(user?.board || '');
    const [classLevel, setClassLevel] = useState(user?.classLevel || '');
    const [subject, setSubject] = useState(user?.subject || '');

    const handleSiblingToggle = () => {
        if (!forSibling) {
            setBoard('');
            setClassLevel('');
            setSubject('');
        } else {
            setBoard(user?.board || '');
            setClassLevel(user?.classLevel || '');
            setSubject(user?.subject || '');
        }
        setForSibling(!forSibling);
    };

    const handleStartLearning = () => {
        if (board && classLevel && subject) {
            router.visit('/aichat');
        }
    };

    const sel = 'w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white hover:bg-white dark:hover:bg-gray-600 transition';

    return (
        <>
            <Head title="Select Subject" />
            <div className="max-w-lg mx-auto">
                <div className="text-center mb-8">
                    <div className="w-16 h-16 bg-gradient-to-br from-blue-100 to-indigo-100 dark:from-blue-900/30 dark:to-indigo-900/30 rounded-2xl flex items-center justify-center mx-auto mb-4">
                        <i className="fa-solid fa-book-open text-[#2563EB] text-2xl" />
                    </div>
                    <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Select Your Subject</h2>
                    <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">Choose your board, class, and subject to start learning</p>
                </div>

                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-8">
                    {user?.board && user?.classLevel && (
                        <div className="mb-6 p-4 rounded-xl bg-blue-50 dark:bg-blue-900/20 border border-blue-100 dark:border-blue-800">
                            <div className="flex items-center justify-between">
                                <div className="flex items-center gap-3">
                                    <i className="fa-solid fa-users text-[#2563EB]" />
                                    <div>
                                        <p className="text-sm font-semibold text-gray-800 dark:text-white">
                                            {forSibling ? 'Browsing for someone else' : `Using your profile (Class ${user.classLevel})`}
                                        </p>
                                        <p className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
                                            {forSibling ? 'Select different board & class below' : 'Want to explore for a sibling?'}
                                        </p>
                                    </div>
                                </div>
                                <button
                                    onClick={handleSiblingToggle}
                                    className={`relative w-11 h-6 rounded-full transition-colors duration-200 ${forSibling ? 'bg-[#2563EB]' : 'bg-gray-300 dark:bg-gray-600'}`}
                                >
                                    <span className={`absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow transition-transform duration-200 ${forSibling ? 'translate-x-5' : ''}`} />
                                </button>
                            </div>
                        </div>
                    )}

                    <div className="space-y-5">
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Board</label>
                            <select value={board} onChange={(e) => setBoard(e.target.value)} className={sel}>
                                <option value="">Select Board</option>
                                <option value="Federal Board">Federal Board</option>
                                <option value="AJK Board">AJK Board</option>
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Class</label>
                            <select value={classLevel} onChange={(e) => { setClassLevel(e.target.value); setSubject(''); }} className={sel}>
                                <option value="">Select Class</option>
                                {['9', '10', '11', '12'].map((c) => <option key={c} value={c}>Class {c}</option>)}
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Subject</label>
                            <select value={subject} onChange={(e) => setSubject(e.target.value)} disabled={!classLevel} className={`${sel} disabled:opacity-50 disabled:cursor-not-allowed`}>
                                <option value="">Select Subject</option>
                                {subjects.map((s) => <option key={s} value={s}>{s}</option>)}
                            </select>
                        </div>
                        <button
                            onClick={handleStartLearning}
                            disabled={!board || !classLevel || !subject}
                            className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3.5 rounded-xl hover:shadow-lg hover:shadow-blue-200 dark:hover:shadow-blue-900/30 disabled:opacity-40 disabled:cursor-not-allowed disabled:shadow-none transition-all duration-200 text-sm font-semibold mt-2 flex items-center justify-center gap-2"
                        >
                            Start Learning <i className="fa-solid fa-arrow-right" />
                        </button>
                    </div>
                </div>
            </div>
        </>
    );
}

Selection.layout = (page: React.ReactNode) => <StudentLayout currentPage="selection">{page}</StudentLayout>;
