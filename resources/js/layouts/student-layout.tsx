import { useState, useRef, useEffect } from 'react';
import { Link, usePage, router } from '@inertiajs/react';
import LogoES from '@/components/logo-es';
import { useAppearance } from '@/hooks/use-appearance';

const menuItems = [
    { key: 'dashboard', label: 'Dashboard', icon: 'fa-solid fa-house', href: '/dashboard' },
    { key: 'aichat', label: 'AI Learning', icon: 'fa-solid fa-robot', href: '/aichat' },
    { key: 'practice', label: 'Practice Quiz', icon: 'fa-solid fa-clipboard-check', href: '/practice' },
    { key: 'resources', label: 'Resources', icon: 'fa-solid fa-download', href: '/resources' },
    { key: 'progress', label: 'Progress', icon: 'fa-solid fa-chart-line', href: '/progress' },
    { key: 'about', label: 'About Us', icon: 'fa-solid fa-circle-info', href: '/about' },
];

function Header({ user, isAdmin, onLogout }: { user: { name: string; email: string; role?: string }; isAdmin: boolean; onLogout: () => void }) {
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
        <header className="fixed top-0 left-0 right-0 h-16 bg-gradient-to-r from-[#1E3A8A] via-[#2563EB] to-[#3B82F6] text-white z-50 shadow-lg">
            <div className="flex items-center justify-between h-full px-6 pl-14 md:pl-6">
                <Link href="/dashboard" className="flex items-center gap-3 cursor-pointer">
                    <div className="w-9 h-9 bg-white/20 backdrop-blur-sm rounded-xl flex items-center justify-center">
                        <LogoES className="w-6 h-6" />
                    </div>
                    <h1 className="text-xl font-bold tracking-tight hover:text-yellow-200 transition">
                        Eternal Sunshine
                    </h1>
                </Link>
                <div className="flex items-center gap-2">
                    {isAdmin && (
                        <Link href="/admin/dashboard" className="bg-purple-500/20 hover:bg-purple-500/30 px-3 py-2 rounded-xl transition text-xs font-medium flex items-center gap-2">
                            <i className="fa-solid fa-shield-halved text-purple-200" />
                            <span className="hidden sm:inline">Admin</span>
                        </Link>
                    )}
                    <button onClick={toggleDark} className="bg-white/10 hover:bg-white/20 p-2 rounded-xl transition" title={isDark ? 'Light Mode' : 'Dark Mode'}>
                        <i className={`${isDark ? 'fa-solid fa-sun text-yellow-300' : 'fa-solid fa-moon text-blue-100'} text-base`} />
                    </button>
                    <div className="relative" ref={menuRef}>
                        <button onClick={() => setOpen(!open)} className="flex items-center gap-2 bg-white/10 hover:bg-white/20 pl-1.5 pr-2.5 py-1.5 rounded-xl transition">
                            <div className="w-8 h-8 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-full flex items-center justify-center text-sm font-bold text-white">
                                {user?.name?.charAt(0) || 'S'}
                            </div>
                            <i className={`fa-solid fa-chevron-down text-xs text-white/70 transition-transform ${open ? 'rotate-180' : ''}`} />
                        </button>
                        {open && (
                            <div className="absolute right-0 mt-2 w-56 bg-white dark:bg-gray-800 rounded-xl shadow-xl border border-gray-100 dark:border-gray-700 overflow-hidden py-1 z-50">
                                <div className="px-4 py-3 border-b border-gray-100 dark:border-gray-700">
                                    <p className="text-sm font-semibold text-gray-800 dark:text-white">{user?.name || 'Student'}</p>
                                    <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">{user?.email || ''}</p>
                                </div>
                                <Link href="/profile" onClick={() => setOpen(false)} className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-700 transition">
                                    <i className="fa-solid fa-user text-gray-400 w-4 text-center" />
                                    Profile
                                </Link>
                                <button onClick={() => { setOpen(false); onLogout(); }} className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20 transition">
                                    <i className="fa-solid fa-right-from-bracket w-4 text-center" />
                                    Logout
                                </button>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </header>
    );
}

function Sidebar({ currentPage, collapsed, onToggle }: { currentPage: string; collapsed: boolean; onToggle: () => void }) {
    const [open, setOpen] = useState(false);

    return (
        <>
            <button onClick={() => setOpen(!open)} className="md:hidden fixed top-[1.1rem] left-4 z-[60] text-white p-1 rounded-lg">
                <i className={`fa-solid ${open ? 'fa-xmark' : 'fa-bars'} text-xl`} />
            </button>
            {open && <div className="md:hidden fixed inset-0 bg-black/40 backdrop-blur-sm z-40" onClick={() => setOpen(false)} />}
            <aside className={`fixed top-16 left-0 h-[calc(100vh-4rem)] bg-white dark:bg-gray-800 z-40 shadow-xl border-r border-gray-100 dark:border-gray-700 transition-all duration-300 ${collapsed ? 'md:w-[4.5rem]' : 'md:w-64'} w-64 ${open ? 'translate-x-0' : '-translate-x-full'} md:translate-x-0`}>
                <nav className="flex flex-col h-full py-4 overflow-y-auto">
                    <div className="flex-1 space-y-1 px-3">
                        {menuItems.map((item) => (
                            <Link
                                key={item.key}
                                href={item.href}
                                onClick={() => setOpen(false)}
                                title={collapsed ? item.label : undefined}
                                className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200 ${collapsed ? 'justify-center' : ''}
                                    ${currentPage === item.key
                                        ? 'bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white shadow-md shadow-blue-200 dark:shadow-blue-900/30'
                                        : 'text-gray-600 dark:text-gray-300 hover:bg-blue-50 dark:hover:bg-blue-900/30 hover:text-[#2563EB]'}`}
                            >
                                <i className={`${item.icon} w-5 text-center ${collapsed ? 'text-lg' : ''}`} />
                                {!collapsed && item.label}
                            </Link>
                        ))}
                    </div>
                    <div className={`hidden md:block pt-4 border-t border-gray-100 dark:border-gray-700 ${collapsed ? 'mx-2 px-2' : 'mx-4 px-4'}`}>
                        <button onClick={onToggle} className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-gray-400 dark:text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-600 dark:hover:text-gray-300 transition ${collapsed ? 'justify-center' : ''}`} title={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}>
                            <i className={`fa-solid ${collapsed ? 'fa-angles-right' : 'fa-angles-left'} w-5 text-center`} />
                            {!collapsed && 'Collapse'}
                        </button>
                    </div>
                </nav>
            </aside>
        </>
    );
}

export default function StudentLayout({ children, currentPage = 'dashboard', isChat = false }: { children: React.ReactNode; currentPage?: string; isChat?: boolean }) {
    const { auth } = usePage<{ auth: { user: { name: string; email: string; role?: string } } }>().props;
    const user = auth.user;
    const isAdmin = user?.role === 'admin';
    const [sidebarCollapsed, setSidebarCollapsed] = useState(() => {
        if (typeof window !== 'undefined') {
            return localStorage.getItem('sidebar-collapsed') === 'true';
        }
        return false;
    });
    const [showLogoutConfirm, setShowLogoutConfirm] = useState(false);

    const toggleSidebar = () => {
        const next = !sidebarCollapsed;
        setSidebarCollapsed(next);
        localStorage.setItem('sidebar-collapsed', String(next));
    };

    const handleLogout = () => router.post('/logout');

    return (
        <div className={`bg-[#F0F4F8] dark:bg-gray-900 transition-colors ${isChat ? 'h-screen overflow-hidden' : 'min-h-screen'}`}>
            <Header user={user} isAdmin={isAdmin} onLogout={() => setShowLogoutConfirm(true)} />
            <Sidebar currentPage={currentPage} collapsed={sidebarCollapsed} onToggle={toggleSidebar} />
            <main className={`pt-16 transition-all duration-300 ${sidebarCollapsed ? 'md:pl-[4.5rem]' : 'md:pl-64'} ${isChat ? 'h-screen overflow-hidden' : ''}`}>
                <div className={isChat ? 'h-[calc(100vh-4rem)]' : 'p-5 md:p-8 max-w-7xl mx-auto'}>
                    {children}
                </div>
            </main>

            {showLogoutConfirm && (
                <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-[100] flex items-center justify-center p-4">
                    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 w-full max-w-sm p-6 text-center">
                        <div className="w-14 h-14 bg-red-50 dark:bg-red-900/20 rounded-full flex items-center justify-center mx-auto mb-4">
                            <i className="fa-solid fa-right-from-bracket text-red-500 text-xl" />
                        </div>
                        <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-1">Logout</h3>
                        <p className="text-sm text-gray-500 dark:text-gray-400 mb-6">Are you sure you want to logout?</p>
                        <div className="flex gap-3">
                            <button onClick={() => setShowLogoutConfirm(false)} className="flex-1 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-2.5 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition text-sm font-semibold">
                                Cancel
                            </button>
                            <button onClick={handleLogout} className="flex-1 bg-red-500 hover:bg-red-600 text-white py-2.5 rounded-xl transition text-sm font-semibold">
                                Logout
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}
