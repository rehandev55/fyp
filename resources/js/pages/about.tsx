import { Head } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';
import LogoES from '@/components/logo-es';

export default function About() {
    const team = [
        { name: 'Team member 1', role: 'Frontend Developer', color: 'from-blue-500 to-indigo-600', icon: 'fa-solid fa-laptop-code' },
        { name: 'Team member 2', role: 'Backend Developer', color: 'from-emerald-500 to-teal-600', icon: 'fa-solid fa-server' },
        { name: 'Team member 3', role: 'AI Developer', color: 'from-purple-500 to-pink-600', icon: 'fa-solid fa-brain' },
    ];

    return (
        <>
            <Head title="About" />
            <div className="max-w-3xl mx-auto space-y-8">
                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-8 text-center">
                    <div className="w-16 h-16 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-2xl flex items-center justify-center mx-auto mb-5 shadow-lg shadow-blue-200 dark:shadow-blue-900/30">
                        <LogoES className="w-9 h-9" />
                    </div>
                    <h2 className="text-2xl font-bold text-gray-800 dark:text-white mb-3">About Eternal Sunshine</h2>
                    <p className="text-gray-500 dark:text-gray-400 leading-relaxed max-w-xl mx-auto">Eternal Sunshine is an AI-powered learning assistant designed to support Pakistani students with exam preparation, AI explanations, and practice quizzes aligned with Federal Board and AJK Board syllabi.</p>
                </div>

                <div>
                    <div className="text-center mb-6">
                        <span className="text-sm font-semibold text-[#2563EB] bg-blue-50 dark:bg-blue-900/30 px-4 py-1.5 rounded-full">Our Team</span>
                    </div>
                    <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
                        {team.map((t, i) => (
                            <div key={i} className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 text-center hover:shadow-lg hover:-translate-y-1 transition-all duration-300 group">
                                <div className={`w-20 h-20 bg-gradient-to-br ${t.color} rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg group-hover:scale-110 transition-transform duration-300 relative`}>
                                    <i className="fa-solid fa-user text-white text-2xl" />
                                    <div className="absolute -bottom-1 -right-1 w-8 h-8 bg-white dark:bg-gray-800 rounded-full flex items-center justify-center shadow-md border-2 border-white dark:border-gray-800">
                                        <i className={`${t.icon} text-xs ${t.color.includes('blue') ? 'text-blue-500' : t.color.includes('emerald') ? 'text-emerald-500' : 'text-purple-500'}`} />
                                    </div>
                                </div>
                                <h4 className="font-bold text-gray-800 dark:text-white text-lg">{t.name}</h4>
                                <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">{t.role}</p>
                            </div>
                        ))}
                    </div>
                    <p className="text-sm text-gray-400 dark:text-gray-500 mt-5 text-center max-w-lg mx-auto leading-relaxed">We are final-year Software Engineering students building innovative educational technology to improve learning accessibility.</p>
                </div>

                <div className="bg-gradient-to-br from-[#1E3A8A] via-[#2563EB] to-[#7C3AED] rounded-2xl p-8 md:p-10 text-white relative overflow-hidden">
                    <div className="absolute top-0 right-0 w-40 h-40 bg-yellow-300/10 rounded-full blur-3xl" />
                    <div className="relative text-center">
                        <h3 className="font-bold text-xl mb-3"><i className="fa-solid fa-bullseye mr-2" />Our Goal</h3>
                        <p className="text-blue-100 leading-relaxed max-w-lg mx-auto">Our goal is to provide intelligent, syllabus-aligned learning tools for students preparing for board exams. Every student deserves access to quality educational resources.</p>
                    </div>
                </div>

                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-8">
                    <h3 className="font-bold text-gray-800 dark:text-white text-center mb-6"><i className="fa-solid fa-code mr-2 text-[#2563EB]" />Built With</h3>
                    <div className="flex flex-wrap justify-center gap-3">
                        {[
                            { name: 'React', icon: 'fa-brands fa-react' },
                            { name: 'Tailwind CSS', icon: 'fa-solid fa-paintbrush' },
                            { name: 'Laravel', icon: 'fa-brands fa-laravel' },
                            { name: 'AI/ML', icon: 'fa-solid fa-brain' },
                            { name: 'MySQL', icon: 'fa-solid fa-database' },
                        ].map((tech) => (
                            <span key={tech.name} className="bg-gray-50 dark:bg-gray-700 border border-gray-200 dark:border-gray-600 text-gray-600 dark:text-gray-300 px-5 py-2.5 rounded-xl text-sm font-medium hover:bg-blue-50 dark:hover:bg-blue-900/30 hover:text-[#2563EB] hover:border-blue-200 dark:hover:border-blue-800 transition-all duration-200 flex items-center gap-2">
                                <i className={`${tech.icon} text-base`} />
                                {tech.name}
                            </span>
                        ))}
                    </div>
                </div>
            </div>
        </>
    );
}

About.layout = (page: React.ReactNode) => <StudentLayout currentPage="about">{page}</StudentLayout>;
