import { useState, useEffect } from 'react';
import AdminLayout from '@/layouts/admin-layout';
import { api } from '@/lib/api';

interface User {
    id: number;
    name: string;
    email: string;
    classLevel: string;
    board: string;
    subject: string;
    status: string;
    quizzes: number;
    score: number;
    joined: string;
}

interface Modal {
    type: 'view' | 'edit' | 'delete';
    user: User;
}

const initialUsers: User[] = [
    { id: 1, name: 'Ahmed Khan', email: 'ahmed@example.com', classLevel: '10', board: 'Federal Board', subject: 'Physics', status: 'Active', quizzes: 24, score: 78, joined: '2026-03-15' },
    { id: 2, name: 'Sara Ali', email: 'sara@example.com', classLevel: '9', board: 'AJK Board', subject: 'Biology', status: 'Active', quizzes: 18, score: 85, joined: '2026-03-20' },
    { id: 3, name: 'Hassan Raza', email: 'hassan@example.com', classLevel: '12', board: 'Federal Board', subject: 'Mathematics', status: 'Blocked', quizzes: 5, score: 42, joined: '2026-02-10' },
    { id: 4, name: 'Ayesha Noor', email: 'ayesha@example.com', classLevel: '11', board: 'Federal Board', subject: 'Chemistry', status: 'Active', quizzes: 31, score: 91, joined: '2026-01-25' },
    { id: 5, name: 'Usman Tariq', email: 'usman@example.com', classLevel: '10', board: 'AJK Board', subject: 'English', status: 'Active', quizzes: 12, score: 67, joined: '2026-03-28' },
    { id: 6, name: 'Fatima Zahra', email: 'fatima@example.com', classLevel: '9', board: 'Federal Board', subject: 'Physics', status: 'Inactive', quizzes: 0, score: 0, joined: '2026-04-01' },
    { id: 7, name: 'Bilal Ahmed', email: 'bilal@example.com', classLevel: '10', board: 'Federal Board', subject: 'Biology', status: 'Active', quizzes: 45, score: 88, joined: '2025-12-05' },
    { id: 8, name: 'Zainab Malik', email: 'zainab@example.com', classLevel: '11', board: 'AJK Board', subject: 'Chemistry', status: 'Active', quizzes: 22, score: 73, joined: '2026-02-18' },
];

function Users() {
    const [users, setUsers] = useState<User[]>(initialUsers);
    const [search, setSearch] = useState('');
    const [filterStatus, setFilterStatus] = useState('');
    const [filterClass, setFilterClass] = useState('');
    const [modal, setModal] = useState<Modal | null>(null);
    const [editForm, setEditForm] = useState<User>({} as User);

    const filtered = users.filter(
        (u) =>
            (!search || u.name.toLowerCase().includes(search.toLowerCase()) || u.email.toLowerCase().includes(search.toLowerCase())) &&
            (!filterStatus || u.status === filterStatus) &&
            (!filterClass || u.classLevel === filterClass),
    );

    const toggleStatus = async (id: number) => {
        try {
            const res = await api(`/users/toggle/${id}`, {
                method: "PATCH",
            });

            const updated = await res.json();

            setUsers((prev) =>
                prev.map((u) => (u.id === id ? updated.data : u))
            );
        } catch (err) {
            console.error("Status update failed:", err);
        }
    };

    const openEdit = (u: User) => {
        setEditForm({ ...u });
        setModal({ type: 'edit', user: u });
    };
    const saveEdit = async () => {
        try {
            await api(`/users/${editForm.id}`, {
                method: "PUT",
                body: JSON.stringify({
                    name: editForm.name,
                    email: editForm.email,
                }),
            });

            setUsers((prev) =>
                prev.map((u) =>
                    u.id === editForm.id ? { ...u, ...editForm } : u
                )
            );

            setModal(null);
        } catch (err) {
            console.error("Update failed:", err);
        }
    };

    const deleteUser = async (id: number) => {
        try {
            await api(`/users/${id}`, {
                method: "DELETE",
            });

            setUsers((prev) => prev.filter((u) => u.id !== id));
            setModal(null);
        } catch (err) {
            console.error("Delete failed:", err);
        }
    };

    const sel =
        'border border-gray-200 dark:border-gray-600 rounded-xl px-3 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#7C3AED] focus:border-transparent bg-white dark:bg-gray-700 dark:text-white transition';
    const inp =
        'w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#7C3AED] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white transition';

    const totalActive = users.filter((u) => u.status === 'Active').length;
    const totalBlocked = users.filter((u) => u.status === 'Blocked').length;
    const avgScore = Math.round(users.reduce((a, u) => a + u.score, 0) / users.length);

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        try {
            const res = await api('/users');
            const data = await res.json();

            setUsers(data.data);
        } catch (err) {
            console.error("Error fetching users:", err);
        }
    };


    return (
        <div className="space-y-6">
            {/* Header */}
            <div>
                <h2 className="text-2xl font-bold text-gray-800 dark:text-white">User Management</h2>
                <p className="text-gray-400 dark:text-gray-500 text-sm mt-0.5">{users.length} total users registered</p>
            </div>

            {/* Mini stats */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
                {[
                    { label: 'Total', value: users.length, icon: 'fa-solid fa-users', color: 'text-blue-600 bg-blue-50 dark:bg-blue-900/30' },
                    { label: 'Active', value: totalActive, icon: 'fa-solid fa-circle-check', color: 'text-emerald-600 bg-emerald-50 dark:bg-emerald-900/30' },
                    { label: 'Blocked', value: totalBlocked, icon: 'fa-solid fa-ban', color: 'text-red-600 bg-red-50 dark:bg-red-900/30' },
                    { label: 'Avg Score', value: `${avgScore}%`, icon: 'fa-solid fa-chart-line', color: 'text-purple-600 bg-purple-50 dark:bg-purple-900/30' },
                ].map((s) => (
                    <div key={s.label} className="bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 p-4 flex items-center gap-3">
                        <div className={`w-10 h-10 rounded-xl flex items-center justify-center ${s.color}`}>
                            <i className={`${s.icon} text-sm`} />
                        </div>
                        <div>
                            <p className="text-lg font-bold text-gray-800 dark:text-white">{s.value}</p>
                            <p className="text-xs text-gray-400">{s.label}</p>
                        </div>
                    </div>
                ))}
            </div>

            {/* Filters */}
            <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-5">
                <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
                    <div className="sm:col-span-2 relative">
                        <i className="fa-solid fa-magnifying-glass text-gray-400 absolute left-3 top-1/2 -translate-y-1/2 text-sm" />
                        <input
                            type="text"
                            value={search}
                            onChange={(e) => setSearch(e.target.value)}
                            placeholder="Search by name or email..."
                            className="w-full border border-gray-200 dark:border-gray-600 rounded-xl pl-10 pr-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#7C3AED] focus:border-transparent bg-white dark:bg-gray-700 dark:text-white transition"
                        />
                    </div>
                    <select value={filterStatus} onChange={(e) => setFilterStatus(e.target.value)} className={sel}>
                        <option value="">All Status</option>
                        <option value="Active">Active</option>
                        <option value="Blocked">Blocked</option>
                        <option value="Inactive">Inactive</option>
                    </select>
                    <select value={filterClass} onChange={(e) => setFilterClass(e.target.value)} className={sel}>
                        <option value="">All Classes</option>
                        {['9', '10', '11', '12'].map((c) => (
                            <option key={c} value={c}>
                                Class {c}
                            </option>
                        ))}
                    </select>
                </div>
            </div>

            {/* Table */}
            <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-hidden">
                <div className="overflow-x-auto">
                    <table className="w-full">
                        <thead>
                            <tr className="border-b border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-gray-700/50">
                                <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">Student</th>
                                <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider hidden sm:table-cell">Class</th>
                                <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider hidden md:table-cell">Subject</th>
                                <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider hidden lg:table-cell">Quizzes</th>
                                <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider hidden lg:table-cell">Score</th>
                                <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">Status</th>
                                <th className="text-left px-5 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">Actions</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-gray-50 dark:divide-gray-700">
                            {filtered.map((u) => (
                                <tr key={u.id} className="hover:bg-gray-50 dark:hover:bg-gray-700/50 transition">
                                    <td className="px-5 py-4">
                                        <div className="flex items-center gap-3">
                                            <div className="w-9 h-9 bg-gradient-to-br from-purple-500 to-indigo-600 rounded-full flex items-center justify-center text-white text-sm font-bold flex-shrink-0">
                                                {u.name.charAt(0)}
                                            </div>
                                            <div>
                                                <p className="text-sm font-medium text-gray-800 dark:text-white">{u.name}</p>
                                                <p className="text-xs text-gray-400">{u.email}</p>
                                            </div>
                                        </div>
                                    </td>
                                    <td className="px-5 py-4 text-sm text-gray-600 dark:text-gray-300 hidden sm:table-cell">Class {u.classLevel}</td>
                                    <td className="px-5 py-4 text-sm text-gray-600 dark:text-gray-300 hidden md:table-cell">{u.subject}</td>
                                    <td className="px-5 py-4 text-sm font-semibold text-gray-800 dark:text-white hidden lg:table-cell">{u.quizzes}</td>
                                    <td className="px-5 py-4 hidden lg:table-cell">
                                        <span className={`text-sm font-semibold ${u.score >= 70 ? 'text-emerald-600' : u.score >= 50 ? 'text-amber-600' : 'text-red-600'}`}>{u.score}%</span>
                                    </td>
                                    <td className="px-5 py-4">
                                        <span
                                            className={`text-xs px-2.5 py-1 rounded-full font-semibold ${u.status === 'Active' ? 'bg-emerald-50 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-300' : u.status === 'Blocked' ? 'bg-red-50 dark:bg-red-900/30 text-red-700 dark:text-red-300' : 'bg-gray-100 dark:bg-gray-700 text-gray-500'}`}
                                        >
                                            {u.status}
                                        </span>
                                    </td>
                                    <td className="px-5 py-4">
                                        <div className="flex items-center gap-1">
                                            <button
                                                onClick={() => setModal({ type: 'view', user: u })}
                                                className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 hover:text-blue-500 transition"
                                                title="View"
                                            >
                                                <i className="fa-solid fa-eye text-xs" />
                                            </button>
                                            <button
                                                onClick={() => openEdit(u)}
                                                className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:bg-amber-50 dark:hover:bg-amber-900/20 hover:text-amber-500 transition"
                                                title="Edit"
                                            >
                                                <i className="fa-solid fa-pen text-xs" />
                                            </button>
                                            <button
                                                onClick={() => toggleStatus(u.id)}
                                                className={`w-8 h-8 rounded-lg flex items-center justify-center transition ${u.status === 'Blocked' ? 'text-gray-400 hover:bg-emerald-50 hover:text-emerald-500' : 'text-gray-400 hover:bg-orange-50 hover:text-orange-500'}`}
                                                title={u.status === 'Blocked' ? 'Unblock' : 'Block'}
                                            >
                                                <i className={`fa-solid ${u.status === 'Blocked' ? 'fa-lock-open' : 'fa-ban'} text-xs`} />
                                            </button>
                                            <button
                                                onClick={() => setModal({ type: 'delete', user: u })}
                                                className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:bg-red-50 dark:hover:bg-red-900/20 hover:text-red-500 transition"
                                                title="Delete"
                                            >
                                                <i className="fa-solid fa-trash-can text-xs" />
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
                {filtered.length === 0 && (
                    <div className="text-center py-12">
                        <p className="text-gray-400 font-medium">No users found</p>
                    </div>
                )}
            </div>

            {/* Modal Overlay */}
            {modal && (
                <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-[100] flex items-center justify-center p-4" onClick={() => setModal(null)}>
                    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-2xl w-full max-w-md max-h-[90vh] overflow-y-auto" onClick={(e) => e.stopPropagation()}>
                        {/* VIEW */}
                        {modal.type === 'view' && (
                            <div className="p-6">
                                <div className="flex items-center justify-between mb-6">
                                    <h3 className="text-lg font-bold text-gray-800 dark:text-white">User Details</h3>
                                    <button onClick={() => setModal(null)} className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700">
                                        <i className="fa-solid fa-xmark" />
                                    </button>
                                </div>
                                <div className="text-center mb-6">
                                    <div className="w-16 h-16 bg-gradient-to-br from-purple-500 to-indigo-600 rounded-full flex items-center justify-center text-white text-2xl font-bold mx-auto mb-3">
                                        {modal.user.name.charAt(0)}
                                    </div>
                                    <h4 className="font-bold text-gray-800 dark:text-white text-lg">{modal.user.name}</h4>
                                    <p className="text-sm text-gray-400">{modal.user.email}</p>
                                    <span
                                        className={`text-xs px-2.5 py-1 rounded-full font-semibold mt-2 inline-block ${modal.user.status === 'Active' ? 'bg-emerald-50 dark:bg-emerald-900/30 text-emerald-700' : modal.user.status === 'Blocked' ? 'bg-red-50 dark:bg-red-900/30 text-red-700' : 'bg-gray-100 text-gray-500'}`}
                                    >
                                        {modal.user.status}
                                    </span>
                                </div>
                                <div className="space-y-3 text-sm">
                                    {[
                                        { label: 'Class', value: `Class ${modal.user.classLevel}`, icon: 'fa-solid fa-graduation-cap' },
                                        { label: 'Board', value: modal.user.board, icon: 'fa-solid fa-building-columns' },
                                        { label: 'Subject', value: modal.user.subject, icon: 'fa-solid fa-book' },
                                        { label: 'Quizzes Taken', value: modal.user.quizzes, icon: 'fa-solid fa-clipboard-check' },
                                        { label: 'Average Score', value: `${modal.user.score}%`, icon: 'fa-solid fa-chart-line' },
                                        { label: 'Joined', value: modal.user.joined, icon: 'fa-solid fa-calendar' },
                                    ].map((r) => (
                                        <div key={r.label} className="flex items-center justify-between py-2 border-b border-gray-100 dark:border-gray-700 last:border-0">
                                            <span className="text-gray-500 flex items-center gap-2">
                                                <i className={`${r.icon} w-4 text-center text-gray-400 text-xs`} />
                                                {r.label}
                                            </span>
                                            <span className="font-medium text-gray-800 dark:text-white">{r.value}</span>
                                        </div>
                                    ))}
                                </div>
                                <div className="flex gap-3 mt-6">
                                    <button
                                        onClick={() => {
                                            setModal(null);
                                            openEdit(modal.user);
                                        }}
                                        className="flex-1 bg-gradient-to-r from-[#7C3AED] to-[#9333EA] text-white py-2.5 rounded-xl text-sm font-semibold hover:shadow-lg transition flex items-center justify-center gap-2"
                                    >
                                        <i className="fa-solid fa-pen text-xs" /> Edit
                                    </button>
                                    <button
                                        onClick={() => setModal(null)}
                                        className="flex-1 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-2.5 rounded-xl text-sm font-semibold hover:bg-gray-50 dark:hover:bg-gray-700 transition"
                                    >
                                        Close
                                    </button>
                                </div>
                            </div>
                        )}

                        {/* EDIT */}
                        {modal.type === 'edit' && (
                            <div className="p-6">
                                <div className="flex items-center justify-between mb-6">
                                    <h3 className="text-lg font-bold text-gray-800 dark:text-white">Edit User</h3>
                                    <button onClick={() => setModal(null)} className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700">
                                        <i className="fa-solid fa-xmark" />
                                    </button>
                                </div>
                                <div className="space-y-4">
                                    <div>
                                        <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Name</label>
                                        <input type="text" value={editForm.name} onChange={(e) => setEditForm({ ...editForm, name: e.target.value })} className={inp} />
                                    </div>
                                    <div>
                                        <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Email</label>
                                        <input type="email" value={editForm.email} onChange={(e) => setEditForm({ ...editForm, email: e.target.value })} className={inp} />
                                    </div>
                                    <div className="grid grid-cols-2 gap-3">
                                        <div>
                                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Class</label>
                                            <select value={editForm.classLevel} onChange={(e) => setEditForm({ ...editForm, classLevel: e.target.value })} className={inp}>
                                                {['9', '10', '11', '12'].map((c) => (
                                                    <option key={c} value={c}>
                                                        Class {c}
                                                    </option>
                                                ))}
                                            </select>
                                        </div>
                                        <div>
                                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Board</label>
                                            <select value={editForm.board} onChange={(e) => setEditForm({ ...editForm, board: e.target.value })} className={inp}>
                                                <option value="Federal Board">Federal Board</option>
                                                <option value="AJK Board">AJK Board</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div className="grid grid-cols-2 gap-3">
                                        <div>
                                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Subject</label>
                                            <select value={editForm.subject} onChange={(e) => setEditForm({ ...editForm, subject: e.target.value })} className={inp}>
                                                {['Physics', 'Chemistry', 'Biology', 'Mathematics', 'English'].map((s) => (
                                                    <option key={s} value={s}>
                                                        {s}
                                                    </option>
                                                ))}
                                            </select>
                                        </div>
                                        <div>
                                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Status</label>
                                            <select value={editForm.status} onChange={(e) => setEditForm({ ...editForm, status: e.target.value })} className={inp}>
                                                <option value="Active">Active</option>
                                                <option value="Blocked">Blocked</option>
                                                <option value="Inactive">Inactive</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <div className="flex gap-3 mt-6">
                                    <button
                                        onClick={() => setModal(null)}
                                        className="flex-1 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-2.5 rounded-xl text-sm font-semibold hover:bg-gray-50 dark:hover:bg-gray-700 transition"
                                    >
                                        Cancel
                                    </button>
                                    <button onClick={saveEdit} className="flex-1 bg-gradient-to-r from-[#7C3AED] to-[#9333EA] text-white py-2.5 rounded-xl text-sm font-semibold hover:shadow-lg transition">
                                        Save Changes
                                    </button>
                                </div>
                            </div>
                        )}

                        {/* DELETE */}
                        {modal.type === 'delete' && (
                            <div className="p-6 text-center">
                                <div className="w-16 h-16 bg-red-50 dark:bg-red-900/30 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <i className="fa-solid fa-triangle-exclamation text-red-500 text-2xl" />
                                </div>
                                <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-2">Delete User</h3>
                                <p className="text-sm text-gray-500 dark:text-gray-400 mb-6">
                                    Are you sure you want to delete <strong>{modal.user.name}</strong>? This action cannot be undone.
                                </p>
                                <div className="flex gap-3">
                                    <button
                                        onClick={() => setModal(null)}
                                        className="flex-1 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-2.5 rounded-xl text-sm font-semibold hover:bg-gray-50 dark:hover:bg-gray-700 transition"
                                    >
                                        Cancel
                                    </button>
                                    <button
                                        onClick={() => deleteUser(modal.user.id)}
                                        className="flex-1 bg-red-500 text-white py-2.5 rounded-xl text-sm font-semibold hover:bg-red-600 transition flex items-center justify-center gap-2"
                                    >
                                        <i className="fa-solid fa-trash-can text-xs" /> Delete
                                    </button>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            )}
        </div>
    );
}

Users.layout = (page: React.ReactNode) => <AdminLayout currentPage="admin-users">{page}</AdminLayout>;

export default Users;
