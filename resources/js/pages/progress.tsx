import { Head } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';

export default function Progress({ stats, subjects, focus_area }: any) {
    const statsData = [
  {
    label: 'Total Quizzes',
    value: stats.total_quizzes,
    max: 50,
    color: 'from-[#2563EB] to-[#3B82F6]',
    icon: 'fa-solid fa-clipboard-check'
  },
  {
    label: 'Average Score',
    value: stats.average_score,
    max: 100,
    suffix: '%',
    color: 'from-emerald-500 to-teal-500',
    icon: 'fa-solid fa-chart-column'
  },
  {
    label: 'Questions Done',
    value: stats.questions_done,
    max: 100,
    color: 'from-purple-500 to-pink-500',
    icon: 'fa-solid fa-circle-question'
  },
];

    const getBarColor = (s: number) => s >= 80 ? 'from-emerald-400 to-emerald-500' : s >= 60 ? 'from-blue-400 to-blue-500' : 'from-orange-400 to-red-400';
    const getStatusColor = (s: string) => s === 'Excellent' ? 'bg-emerald-50 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-300' : s === 'Strong' ? 'bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300' : s === 'Good' ? 'bg-indigo-50 dark:bg-indigo-900/30 text-indigo-700 dark:text-indigo-300' : 'bg-orange-50 dark:bg-orange-900/30 text-orange-700 dark:text-orange-300';

    return (
        <>
            <Head title="Progress" />
            <div className="space-y-8 max-w-3xl mx-auto">
                <div className="text-center">
                    <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Your Progress</h2>
                    <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">Track your learning journey</p>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
                    {statsData.map((s) => (
                        <div key={s.label} className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                            <div className="flex items-center justify-between mb-4">
                                <div className={`w-12 h-12 bg-gradient-to-br ${s.color} rounded-xl flex items-center justify-center shadow-lg`}>
                                    <i className={`${s.icon} text-white`} />
                                </div>
                                <span className="text-3xl font-bold text-gray-800 dark:text-white">{s.value}{s.suffix || ''}</span>
                            </div>
                            <p className="text-sm text-gray-500 dark:text-gray-400 mb-3">{s.label}</p>
                            <div className="w-full bg-gray-100 dark:bg-gray-700 rounded-full h-2.5">
                                <div className={`bg-gradient-to-r ${s.color} h-2.5 rounded-full transition-all duration-700`} style={{ width: `${(s.value / s.max) * 100}%` }} />
                            </div>
                        </div>
                    ))}
                </div>
                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 md:p-8">
                    <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-6">Subject Performance</h3>
                    <div className="space-y-5">
                       {subjects.map((s: any) => (
                            <div key={s.name} className="flex items-center gap-4">
                                <span className="text-sm font-medium text-gray-700 dark:text-gray-200 w-24 flex-shrink-0">{s.name}</span>
                                <div className="flex-1">
                                    <div className="w-full bg-gray-100 dark:bg-gray-700 rounded-full h-3">
                                        <div className={`bg-gradient-to-r ${getBarColor(s.score)} h-3 rounded-full transition-all duration-700`} style={{ width: `${s.score}%` }} />
                                    </div>
                                </div>
                                <span className="text-sm font-bold text-gray-800 dark:text-white w-10 text-right">{s.score}%</span>
                                <span className={`text-xs px-2.5 py-1 rounded-full font-semibold whitespace-nowrap ${getStatusColor(s.status)}`}>{s.status}</span>
                            </div>
                        ))}
                    </div>
                </div>
                <div className="bg-gradient-to-r from-orange-50 to-amber-50 dark:from-orange-900/20 dark:to-amber-900/20 border border-orange-200 dark:border-orange-800 rounded-2xl p-6">
                    <div className="flex items-start gap-4">
                        <div className="w-10 h-10 bg-orange-100 dark:bg-orange-900/40 rounded-xl flex items-center justify-center flex-shrink-0">
                            <i className="fa-solid fa-triangle-exclamation text-orange-600 dark:text-orange-400" />
                        </div>
                        <div>
                            <h4 className="font-semibold text-orange-800 dark:text-orange-300">Focus Areas</h4>
                            {/* <p className="text-sm text-orange-700 dark:text-orange-400 mt-1">Chemistry needs more practice. Try taking more quizzes and reviewing AI explanations.</p> */}
                            <p>
    {focus_area ?? "Loading focus area..."}
</p>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}

Progress.layout = (page: React.ReactNode) => <StudentLayout currentPage="progress">{page}</StudentLayout>;
