import { useState, useRef, useEffect } from 'react';
import { Link, usePage } from '@inertiajs/react';
import { useAppearance } from '@/hooks/use-appearance';

const adminItems = [
    { key: 'admin-dashboard', label: 'Dashboard', icon: 'fa-solid fa-gauge-high', href: '/admin/dashboard' },
    { key: 'admin-users', label: 'User Management', icon: 'fa-solid fa-users-gear', href: '/admin/users' },
    { key: 'admin-content', label: 'Content Manager', icon: 'fa-solid fa-cloud-arrow-up', href: '/admin/content' },
];

function AdminHeader({ user }: { user: { name: string; email: string } }) {
    const [open, setOpen] = useState(false);
    const menuRef = useRef<HTMLDivElement>(null);
    const { resolvedAppearance, updateAppearance } = useAppearance();
    const isDark = resolvedAppearance === 'dark';
    const toggleDark = () => updateAppearance(isDark ? 'light' : 'dark');

    useEffect(() => {
        const handleClick = (e: MouseEvent) => {
            if (menuRef.current && !menuRef.current.contains(e.target as Node)) setOpen(false);
        };
        document.addEventListener('mousedown', handleClick);
        return () => document.removeEventListener('mousedown', handleClick);
    }, []);

    return (
        <header className="fixed top-0 left-0 right-0 h-16 bg-gradient-to-r from-[#1E1E2E] via-[#2D1B69] to-[#1E1E2E] text-white z-50 shadow-lg">
            <div className="flex items-center justify-between h-full px-6 pl-14 md:pl-6">
                <Link href="/admin/dashboard" className="flex items-center gap-3 cursor-pointer">
                    <div className="w-9 h-9 bg-purple-500/20 backdrop-blur-sm rounded-xl flex items-center justify-center">
                        <i className="fa-solid fa-shield-halved text-purple-300" />
                    </div>
                    <div>
                        <h1 className="text-lg font-bold tracking-tight">Admin Panel</h1>
                        <p className="text-[10px] text-purple-300 -mt-0.5">Eternal Sunshine</p>
                    </div>
                </Link>
                <div className="flex items-center gap-2">
                    <Link href="/dashboard" className="bg-white/10 hover:bg-white/20 px-3 py-2 rounded-xl transition text-xs font-medium flex items-center gap-2">
                        <i className="fa-solid fa-arrow-right-from-bracket" />
                        <span className="hidden sm:inline">Student Panel</span>
                    </Link>
                    <button onClick={toggleDark} className="bg-white/10 hover:bg-white/20 p-2 rounded-xl transition" title={isDark ? 'Light Mode' : 'Dark Mode'}>
                        <i className={`${isDark ? 'fa-solid fa-sun text-yellow-300' : 'fa-solid fa-moon text-purple-200'} text-base`} />
                    </button>
                    <div className="relative" ref={menuRef}>
                        <button onClick={() => setOpen(!open)} className="flex items-center gap-2 bg-white/10 hover:bg-white/20 pl-1.5 pr-2.5 py-1.5 rounded-xl transition">
                            <div className="w-8 h-8 bg-gradient-to-br from-purple-400 to-pink-500 rounded-full flex items-center justify-center text-sm font-bold text-white">
                                {user?.name?.charAt(0) || 'A'}
                            </div>
                            <i className={`fa-solid fa-chevron-down text-xs text-white/70 transition-transform ${open ? 'rotate-180' : ''}`} />
                        </button>
                        {open && (
                            <div className="absolute right-0 mt-2 w-56 bg-white dark:bg-gray-800 rounded-xl shadow-xl border border-gray-100 dark:border-gray-700 overflow-hidden py-1 z-50">
                                <div className="px-4 py-3 border-b border-gray-100 dark:border-gray-700">
                                    <p className="text-sm font-semibold text-gray-800 dark:text-white">{user?.name || 'Admin'}</p>
                                    <p className="text-xs text-gray-400 mt-0.5">{user?.email || ''}</p>
                                    <span className="text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 px-2 py-0.5 rounded-full font-semibold mt-1 inline-block">Admin</span>
                                </div>
                                <Link href="/dashboard" onClick={() => setOpen(false)} className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-700 transition">
                                    <i className="fa-solid fa-house w-4 text-center text-gray-400" /> Student Panel
                                </Link>
                                <Link href="/logout" method="post" as="button" onClick={() => setOpen(false)} className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20 transition">
                                    <i className="fa-solid fa-right-from-bracket w-4 text-center" /> Logout
                                </Link>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </header>
    );
}

function AdminSidebar({ currentPage }: { currentPage: string }) {
    const [open, setOpen] = useState(false);

    return (
        <>
            <button onClick={() => setOpen(!open)} className="md:hidden fixed top-[1.1rem] left-4 z-[60] text-white p-1 rounded-lg">
                <i className={`fa-solid ${open ? 'fa-xmark' : 'fa-bars'} text-xl`} />
            </button>
            {open && <div className="md:hidden fixed inset-0 bg-black/40 backdrop-blur-sm z-40" onClick={() => setOpen(false)} />}
            <aside className={`fixed top-16 left-0 h-[calc(100vh-4rem)] w-64 bg-[#1E1E2E] z-40 shadow-xl border-r border-gray-800 transition-all duration-300 ${open ? 'translate-x-0' : '-translate-x-full'} md:translate-x-0`}>
                <nav className="flex flex-col h-full py-4 overflow-y-auto">
                    <div className="px-5 mb-4">
                        <div className="bg-purple-500/10 border border-purple-500/20 rounded-xl p-3">
                            <p className="text-xs font-bold text-purple-300 uppercase tracking-wider flex items-center gap-2">
                                <i className="fa-solid fa-shield-halved text-[10px]" />
                                Administration
                            </p>
                        </div>
                    </div>
                    <div className="flex-1 space-y-1 px-4">
                        {adminItems.map((item) => (
                            <Link
                                key={item.key}
                                href={item.href}
                                onClick={() => setOpen(false)}
                                className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200
                                    ${currentPage === item.key
                                        ? 'bg-gradient-to-r from-[#7C3AED] to-[#9333EA] text-white shadow-md shadow-purple-900/30'
                                        : 'text-gray-400 hover:bg-white/5 hover:text-purple-300'}`}
                            >
                                <i className={`${item.icon} w-5 text-center`} />
                                {item.label}
                            </Link>
                        ))}
                    </div>
                    <div className="px-4 space-y-1 mb-2">
                        <Link href="/dashboard" className="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-gray-400 hover:bg-white/5 hover:text-blue-300 transition">
                            <i className="fa-solid fa-arrow-right-from-bracket w-5 text-center" />
                            Student Panel
                        </Link>
                    </div>
                    <div className="px-4 pt-4 border-t border-gray-800 mx-4">
                        <Link href="/logout" method="post" as="button" className="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-red-400 hover:bg-red-900/20 transition">
                            <i className="fa-solid fa-right-from-bracket w-5 text-center" />
                            Logout
                        </Link>
                    </div>
                </nav>
            </aside>
        </>
    );
}

export default function AdminLayout({ children, currentPage = 'admin-dashboard' }: { children: React.ReactNode; currentPage?: string }) {
    const { auth } = usePage<{ auth: { user: { name: string; email: string; role?: string } } }>().props;
    const user = auth.user;

    return (
        <div className="bg-[#F0F4F8] dark:bg-gray-900 transition-colors min-h-screen">
            <AdminHeader user={user} />
            <AdminSidebar currentPage={currentPage} />
            <main className="pt-16 md:pl-64">
                <div className="p-5 md:p-8 max-w-7xl mx-auto">
                    {children}
                </div>
            </main>
        </div>
    );
}
