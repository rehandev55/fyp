import { useState } from 'react';
import { Head, usePage, router } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';
import { useEffect } from 'react';
import { api } from '@/lib/api';

interface User {
    name: string;
    email: string;
    role?: string;
    subject?: string;
    class_level?: string;
    board?: string;
}

const boards = [
    { value: 'federal', label: 'Federal Board' },
    { value: 'ajk', label: 'AJK Board' },
];

const classes = [
    { value: 'class_9', label: 'Class 9' },
    { value: 'class_10', label: 'Class 10' },
    { value: 'class_11', label: 'Class 11' },
    { value: 'class_12', label: 'Class 12' },
];

const subjects = [
    { value: 'physics', label: 'Physics' },
    { value: 'chemistry', label: 'Chemistry' },
    { value: 'biology', label: 'Biology' },
    { value: 'mathematics', label: 'Mathematics' },
    { value: 'computer', label: 'Computer Science' },
    { value: 'english', label: 'English' },
    { value: 'islamiyat', label: 'Islamiyat' },
    { value: 'pakistan_studies', label: 'Pakistan Studies' },
];

export default function Selection() {
    console.log("SELECTION COMPONENT RENDERED");
        const page = usePage();
console.log("FULL PAGE PROPS:", page.props);
const { auth } = usePage<{ auth: { user: User } }>().props;
const user = auth?.user;
// useEffect(() => {
//     console.log("USE EFFECT RUNNING");
//     async function loadUser() {
//         // 1. Try Inertia user first
//         if (user) {
//             setBoard(user.board || '');
//             setClassLevel(user.class_level || '');
//             setSubject(user.subject || '');
//             return;
//         }

//         // 2. Fallback to API
//         try {
//             const res = await api('/user');
//             const data = await res.json();

//             console.log("USER FROM API:", data);

//             if (data) {
//                 setBoard(data.board || '');
//                 setClassLevel(data.class_level || '');
//                 setSubject(data.subject || '');
//             }
//         } catch (err) {
//             console.error(err);
//         }
//     }

//     loadUser();
// }, [user]);
useEffect(() => {
    console.log("USE EFFECT RUNNING");
    if (user) {
        setBoard(user.board || '');
        setClassLevel(user.class_level || '');
        setSubject(user.subject || '');
    } else {
        // fallback API
        (async () => {
            try {
                const res = await api('/user');
                const data = await res.json();

                setBoard(data.board || '');
                setClassLevel(data.class_level || '');
                setSubject(data.subject || '');
            } catch (err) {
                console.error(err);
            }
        })();
    }
}, []);

    const [forSibling, setForSibling] = useState(false);
     const [board, setBoard] = useState(user?.board || '');
const [classLevel, setClassLevel] = useState(user?.class_level || '');
const [subject, setSubject] = useState(user?.subject || '');

    // const classLabel = classes.find(c => c.value === user?.class_level)?.label || user?.class_level;
const classLabel = classes.find(c => c.value === classLevel)?.label || classLevel;

   const handleSiblingToggle = () => {
    if (!forSibling) {
        setBoard('');
        setClassLevel('');
        setSubject('');
    } else {
        // just leave as is OR keep previous values
    }
    setForSibling(!forSibling);
};

    const handleStartLearning = () => {
        if (board && classLevel && subject) {
            // router.visit(`/aichat?board=${encodeURIComponent(board)}&class_level=${encodeURIComponent(classLevel)}&subject=${encodeURIComponent(subject)}`);
            router.visit(`/practice?board=${encodeURIComponent(board)}&class_level=${encodeURIComponent(classLevel)}&subject=${encodeURIComponent(subject)}`);
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
                    {board && classLevel && (
                        <div className="mb-6 p-4 rounded-xl bg-blue-50 dark:bg-blue-900/20 border border-blue-100 dark:border-blue-800">
                            <div className="flex items-center justify-between">
                                <div className="flex items-center gap-3">
                                    <i className="fa-solid fa-users text-[#2563EB]" />
                                    <div>
                                        <p className="text-sm font-semibold text-gray-800 dark:text-white">
                                            {forSibling ? 'Browsing for someone else' : `Using your profile (${classLabel})`}
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
                                {boards.map((b) => <option key={b.value} value={b.value}>{b.label}</option>)}
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Class</label>
                            <select value={classLevel} onChange={(e) => { setClassLevel(e.target.value); setSubject(''); }} className={sel}>
                                <option value="">Select Class</option>
                                {classes.map((c) => <option key={c.value} value={c.value}>{c.label}</option>)}
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Subject</label>
                            <select value={subject} onChange={(e) => setSubject(e.target.value)} disabled={!classLevel} className={`${sel} disabled:opacity-50 disabled:cursor-not-allowed`}>
                                <option value="">Select Subject</option>
                                {subjects.map((s) => <option key={s.value} value={s.value}>{s.label}</option>)}
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
