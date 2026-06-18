import { Link } from '@inertiajs/react';
import { useState, useEffect } from 'react';
import { backendApi } from '@/lib/backendApi';

import {
    AreaChart,
    Area,
    BarChart,
    Bar,
    PieChart,
    Pie,
    Cell,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
} from 'recharts';
import AdminLayout from '@/layouts/admin-layout';


const userGrowth = [
    { month: 'Oct', users: 420 },
    { month: 'Nov', users: 580 },
    { month: 'Dec', users: 710 },
    { month: 'Jan', users: 860 },
    { month: 'Feb', users: 1050 },
    { month: 'Mar', users: 1247 },
];

const quizActivity = [
    { day: 'Mon', quizzes: 142 },
    { day: 'Tue', quizzes: 198 },
    { day: 'Wed', quizzes: 167 },
    { day: 'Thu', quizzes: 231 },
    { day: 'Fri', quizzes: 189 },
    { day: 'Sat', quizzes: 276 },
    { day: 'Sun', quizzes: 203 },
];

const subjectDistribution = [
    { name: 'Physics', value: 320, color: '#3B82F6' },
    { name: 'Chemistry', value: 245, color: '#8B5CF6' },
    { name: 'Biology', value: 280, color: '#10B981' },
    { name: 'Mathematics', value: 260, color: '#F59E0B' },
    { name: 'English', value: 142, color: '#EF4444' },
];

function Dashboard() {
    const [users, setUsers] = useState<any[]>([]);
    const [content, setContent] = useState<any[]>([]);

    const userGrowth = Object.values(
    (users || []).reduce((acc: any, u: any) => {
        if (!u.created_at) return acc;

        const date = new Date(u.created_at);
        const month = date.toLocaleString('default', { month: 'short' });

        if (!acc[month]) {
            acc[month] = { month, users: 0 };
        }

        acc[month].users += 1;

        return acc;
    }, {})
);
const subjectDistribution = Object.values(
    (content || []).reduce((acc: any, c: any) => {
        if (!c.subject) return acc;

        if (!acc[c.subject]) {
            acc[c.subject] = {
                name: c.subject,
                value: 0
            };
        }

        acc[c.subject].value += 1;

        return acc;
    }, {})
);
const COLORS = ['#3B82F6', '#8B5CF6', '#10B981', '#F59E0B', '#EF4444'];

    const stats = [
    {
        label: 'Total Users',
        value: users?.length || 0,
        change: '',
        up: true,
        icon: 'fa-solid fa-users',
        color: 'from-blue-500 to-indigo-600'
    },
    {
        label: 'Resources',
        value: content?.length || 0,
        change: '',
        up: true,
        icon: 'fa-solid fa-book',
        color: 'from-purple-500 to-pink-600'
    },
    {
        label: 'Downloads',
        value: (content || []).reduce((a, c) => a + (c.downloads || 0), 0),
        change: '',
        up: true,
        icon: 'fa-solid fa-download',
        color: 'from-emerald-500 to-teal-600'
    },
    {
        label: 'Active Today',
        value: users?.length || 0,
        change: '',
        up: true,
        icon: 'fa-solid fa-user-check',
        color: 'from-orange-500 to-amber-600'
    },
];

    useEffect(() => {
    fetchUsers();
    fetchContent();
}, []);
const fetchUsers = async () => {
    try {
        const res = await backendApi("/api/users");

        if (!res.ok) throw new Error("Users API failed");

        const data = await res.json();
        setUsers(data.data || []);
    } catch (err) {
        console.error("Users fetch error:", err);
        setUsers([]); // prevents crash
    }
};

const fetchContent = async () => {
    try {
        const res = await backendApi("/api/content");

        if (!res.ok) throw new Error("Content API failed");

        const data = await res.json();
        setContent(data.data || []);
    } catch (err) {
        console.error("Content fetch error:", err);
        setContent([]); // prevents crash
    }
};

    return (
        <div className="space-y-8">
            {/* Header */}
            <div>
                <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Dashboard Overview</h2>
                <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">Welcome back, here's what's happening</p>
            </div>

            {/* Stats */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                {stats.map((s) => (
                    <div key={s.label} className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 hover:shadow-lg transition-all duration-300 group">
                        <div className="flex items-center justify-between mb-4">
                            <div className={`w-12 h-12 bg-gradient-to-br ${s.color} rounded-xl flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300`}>
                                <i className={`${s.icon} text-white`} />
                            </div>
                            <span className={`text-xs font-semibold px-2 py-1 rounded-full flex items-center gap-1 ${s.up ? 'text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-900/30' : 'text-red-600 dark:text-red-400 bg-red-50 dark:bg-red-900/30'}`}>
                                <i className={`fa-solid ${s.up ? 'fa-arrow-up' : 'fa-arrow-down'} text-[10px]`} />
                                {s.change}
                            </span>
                        </div>
                        <p className="text-2xl font-bold text-gray-800 dark:text-white">{s.value}</p>
                        <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">{s.label}</p>
                    </div>
                ))}
            </div>

            {/* Charts Row */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {/* User Growth */}
                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                    <div className="flex items-center justify-between mb-6">
                        <h3 className="font-bold text-gray-800 dark:text-white flex items-center gap-2">
                            <i className="fa-solid fa-chart-line text-[#2563EB] text-sm" /> User Growth
                        </h3>
                        <span className="text-xs text-gray-400">Last 6 months</span>
                    </div>
                    <ResponsiveContainer width="100%" height={220}>
                        <AreaChart data={userGrowth}>
                            <defs>
                                <linearGradient id="colorUsers" x1="0" y1="0" x2="0" y2="1">
                                    <stop offset="5%" stopColor="#2563EB" stopOpacity={0.3} />
                                    <stop offset="95%" stopColor="#2563EB" stopOpacity={0} />
                                </linearGradient>
                            </defs>
                            <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
                            <XAxis dataKey="month" tick={{ fontSize: 12 }} stroke="#9CA3AF" />
                            <YAxis tick={{ fontSize: 12 }} stroke="#9CA3AF" />
                            <Tooltip contentStyle={{ borderRadius: '12px', border: '1px solid #e5e7eb', fontSize: '12px' }} />
                            <Area type="monotone" dataKey="users" stroke="#2563EB" strokeWidth={2} fill="url(#colorUsers)" />
                        </AreaChart>
                    </ResponsiveContainer>
                </div>

                {/* Quiz Activity */}
                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                    <div className="flex items-center justify-between mb-6">
                        <h3 className="font-bold text-gray-800 dark:text-white flex items-center gap-2">
                            <i className="fa-solid fa-chart-column text-emerald-500 text-sm" /> Quiz Activity
                        </h3>
                        <span className="text-xs text-gray-400">This week</span>
                    </div>
                    <ResponsiveContainer width="100%" height={220}>
                        <BarChart data={quizActivity}>
                            <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
                            <XAxis dataKey="day" tick={{ fontSize: 12 }} stroke="#9CA3AF" />
                            <YAxis tick={{ fontSize: 12 }} stroke="#9CA3AF" />
                            <Tooltip contentStyle={{ borderRadius: '12px', border: '1px solid #e5e7eb', fontSize: '12px' }} />
                            <Bar dataKey="quizzes" fill="#10B981" radius={[6, 6, 0, 0]} />
                        </BarChart>
                    </ResponsiveContainer>
                </div>
            </div>

            {/* Subject Distribution + Recent Content */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                    <h3 className="font-bold text-gray-800 dark:text-white mb-4 flex items-center gap-2">
                        <i className="fa-solid fa-chart-pie text-purple-500 text-sm" /> By Subject
                    </h3>
                    <ResponsiveContainer width="100%" height={200}>
                        <PieChart>
                            <Pie data={subjectDistribution} dataKey="value">
    {subjectDistribution.map((entry, i) => (
        <Cell key={i} fill={COLORS[i % COLORS.length]} />
    ))}
</Pie>
                            <Tooltip contentStyle={{ borderRadius: '12px', border: '1px solid #e5e7eb', fontSize: '12px' }} />
                        </PieChart>
                    </ResponsiveContainer>
                    <div className="grid grid-cols-2 gap-2 mt-2">
                        {subjectDistribution.map((s: any, index: number) => (
                            <div key={s.name} className="flex items-center gap-2 text-xs text-gray-600 dark:text-gray-300">
                                {/* <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: s.color }} /> */}
                                <span
    className="w-2.5 h-2.5 rounded-full"
    style={{ backgroundColor: COLORS[index % COLORS.length] }}
/>
                                {s.name}
                            </div>
                        ))}
                    </div>
                </div>

                <div className="lg:col-span-2 bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="font-bold text-gray-800 dark:text-white flex items-center gap-2">
                            <i className="fa-solid fa-clock-rotate-left text-orange-500 text-sm" /> Recent Uploads
                        </h3>
                        <Link href="/admin/content" className="text-xs text-[#2563EB] font-semibold hover:underline">
                            View All
                        </Link>
                    </div>
                    <div className="space-y-3">
                        {content.slice(0, 5).map((c: any) => (
    <div key={c.id} className="flex items-center gap-4 p-3 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700/50 transition">

        <div className="w-10 h-10 bg-blue-50 dark:bg-blue-900/30 rounded-xl flex items-center justify-center">
            <i className="fa-solid fa-file-lines text-[#2563EB]" />
        </div>

        <div className="flex-1 min-w-0">
            <p className="text-sm font-medium text-gray-800 dark:text-white truncate">
                {c.title}
            </p>
            <p className="text-xs text-gray-400 mt-0.5">
                {c.type} — {c.created_at ? new Date(c.created_at).toLocaleDateString() : ''}
            </p>
        </div>

        <div className="text-right">
            <p className="text-sm font-semibold text-gray-800 dark:text-white">
                {c.downloads || 0}
            </p>
            <p className="text-[10px] text-gray-400">downloads</p>
        </div>
    </div>
))}
                    </div>
                </div>
            </div>

            {/* Recent Users */}
            <div>
                <div className="flex items-center justify-between mb-4">
                    <h3 className="text-lg font-bold text-gray-800 dark:text-white">Recent Users</h3>
                    <Link href="/admin/users" className="text-sm text-[#2563EB] font-semibold hover:underline flex items-center gap-1">
                        View All <i className="fa-solid fa-arrow-right text-xs" />
                    </Link>
                </div>
                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-hidden">
                    <div className="overflow-x-auto">
                        <table className="w-full">
                            <thead>
                                <tr className="border-b border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-gray-700/50">
                                    <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Student</th>
                                    <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider hidden sm:table-cell">Class</th>
                                    <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider hidden md:table-cell">Board</th>
                                    <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Status</th>
                                    <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider hidden sm:table-cell">Joined</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-gray-50 dark:divide-gray-700">
                                {users.slice(0, 5).map((u: any) => (
    <tr key={u.id} className="hover:bg-gray-50 dark:hover:bg-gray-700/50 transition">
        <td className="px-5 py-4">
            <div className="flex items-center gap-3">
                <div className="w-9 h-9 bg-blue-500 rounded-full flex items-center justify-center text-white">
                    {u.name?.charAt(0)}
                </div>
                <div>
                    <p className="text-sm font-medium text-gray-800 dark:text-white">{u.name}</p>
                    <p className="text-xs text-gray-400">{u.email}</p>
                </div>
            </div>
        </td>

        <td className="px-5 py-4 text-sm text-gray-500">{u.class_level || '—'}</td>
        <td className="px-5 py-4 text-sm text-gray-500">{u.board || '—'}</td>

        <td className="px-5 py-4">
            <span className="text-xs px-2 py-1 bg-green-100 text-green-600 rounded">
                Active
            </span>
        </td>

        <td className="px-5 py-4 text-sm text-gray-400">
            {u.created_at ? new Date(u.created_at).toLocaleDateString() : '-'}
        </td>
    </tr>
))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    );
}

Dashboard.layout = (page: React.ReactNode) => <AdminLayout currentPage="admin-dashboard">{page}</AdminLayout>;

export default Dashboard;
