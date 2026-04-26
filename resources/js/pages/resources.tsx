import { useState } from 'react';
import { Head, usePage } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';
import ResourceCard from '@/components/resource-card';

interface User {
    name: string;
    email: string;
    role?: string;
    subject?: string;
    classLevel?: string;
    board?: string;
}

interface Resource {
    id: number;
    title: string;
    type: string;
    board: string;
    class_level: string;
    subject: string;
    file_path: string;
    file_size: string | null;
    downloads: number;
}

export default function Resources() {
    const { auth, resources } = usePage<{ auth: { user: User }; resources: Resource[] }>().props;

    const [board, setBoard] = useState('');
    const [classLevel, setClassLevel] = useState('');
    const [subject, setSubject] = useState('');

    const classOptions = [
    { value: 'class_9', label: 'Class 9' },
    { value: 'class_10', label: 'Class 10' },
    { value: 'class_11', label: 'Class 11' },
    { value: 'class_12', label: 'Class 12' },
];

    const filtered = resources.filter(
        (r) =>
            (!board || r.board === board) &&
            (!classLevel || r.class_level === classLevel) &&
            (!subject || r.subject === subject),
    );

    const sel = 'border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-white dark:bg-gray-700 dark:text-white hover:border-blue-300 transition';

    return (
        <>
            <Head title="Resources" />
            <div>
                <div className="mb-8">
                    <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Resources</h2>
                    <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">{filtered.length} resources available</p>
                </div>
                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-5 mb-8">
                    <div className="flex items-center gap-2 mb-4">
                        <i className="fa-solid fa-filter text-[#2563EB]" />
                        <span className="text-sm font-semibold text-gray-700 dark:text-gray-200">Filter Resources</span>
                    </div>
                    <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <select value={board} onChange={(e) => setBoard(e.target.value)} className={sel}>
                            <option value="">All Boards</option>
                            <option value="federal">Federal Board</option>
                            <option value="ajk">AJK Board</option>
                        </select>
                        <select value={classLevel} onChange={(e) => setClassLevel(e.target.value)} className={sel}>
                            <option value="">All Classes</option>
                            {classOptions.map((c) => (
    <option key={c.value} value={c.value}>
        {c.label}
    </option>
))}
                        </select>
                        <select value={subject} onChange={(e) => setSubject(e.target.value)} className={sel}>
                            <option value="">All Subjects</option>
                            {['physics', 'chemistry', 'biology', 'mathematics', 'english'].map((s) => <option key={s} value={s}>{s}</option>)}
                        </select>
                    </div>
                </div>
                {filtered.length > 0 ? (
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
                        {filtered.map((r) => (
                            <ResourceCard
                                key={r.id}
                                id={r.id}
                                title={r.title}
                                type={r.type}
                                subject={r.subject}
                                classLevel={r.class_level}
                                board={r.board}
                                fileSize={r.file_size ?? undefined}
                                downloads={r.downloads}
                            />
                        ))}
                    </div>
                ) : (
                    <div className="text-center py-16">
                        <p className="text-gray-400 dark:text-gray-500 font-medium">No resources found</p>
                        <p className="text-gray-300 dark:text-gray-600 text-sm mt-1">Try adjusting your filters</p>
                    </div>
                )}
            </div>
        </>
    );
}

Resources.layout = (page: React.ReactNode) => <StudentLayout currentPage="resources">{page}</StudentLayout>;
