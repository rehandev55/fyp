import { useState } from 'react';
import { Head, usePage } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';

interface User {
    name: string;
    email: string;
    role?: string;
    subject?: string;
    classLevel?: string;
    board?: string;
}

export default function Profile() {
    const { auth } = usePage<{ auth: { user: User } }>().props;
    const user = auth.user;

    const [form, setForm] = useState({
        name: user?.name || '',
        email: user?.email || '',
        classLevel: user?.classLevel || '',
        board: user?.board || '',
    });
    const [message, setMessage] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [passwords, setPasswords] = useState({ current: '', newPass: '', confirm: '' });

    const handleUpdate = (e: React.FormEvent) => {
        e.preventDefault();
        setMessage('Profile updated successfully!');
        setTimeout(() => setMessage(''), 3000);
    };

    const handlePasswordChange = (e: React.FormEvent) => {
        e.preventDefault();
        if (passwords.newPass !== passwords.confirm) {
            setMessage('Passwords do not match!');
            setTimeout(() => setMessage(''), 3000);
            return;
        }
        setPasswords({ current: '', newPass: '', confirm: '' });
        setShowPassword(false);
        setMessage('Password changed successfully!');
        setTimeout(() => setMessage(''), 3000);
    };

    const inp = 'w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white hover:bg-white dark:hover:bg-gray-600 transition';

    return (
        <>
            <Head title="Profile" />
            <div className="max-w-lg mx-auto space-y-6">
                <div className="text-center mb-2">
                    <div className="w-20 h-20 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg shadow-blue-200 dark:shadow-blue-900/30 text-3xl font-bold text-white">
                        {form.name?.charAt(0) || 'S'}
                    </div>
                    <h2 className="text-2xl font-bold text-gray-800 dark:text-white">{form.name || 'Student'}</h2>
                    <p className="text-gray-400 dark:text-gray-500 text-sm">{form.email}</p>
                </div>

                {message && (
                    <div className={`px-5 py-3 rounded-xl text-sm font-medium ${message.includes('success') ? 'bg-emerald-50 dark:bg-emerald-900/30 border border-emerald-200 dark:border-emerald-800 text-emerald-700 dark:text-emerald-300' : 'bg-red-50 dark:bg-red-900/30 border border-red-200 dark:border-red-800 text-red-700 dark:text-red-300'}`}>
                        {message}
                    </div>
                )}

                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 md:p-8">
                    <h3 className="font-bold text-gray-800 dark:text-white mb-5">Personal Information</h3>
                    <form onSubmit={handleUpdate} className="space-y-4">
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Full Name</label>
                            <input type="text" value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} className={inp} />
                        </div>
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Email</label>
                            <input type="email" value={form.email} disabled className="w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm bg-gray-100 dark:bg-gray-700 text-gray-400 dark:text-gray-500 cursor-not-allowed" />
                        </div>
                        <div className="grid grid-cols-2 gap-4">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Class</label>
                                <select value={form.classLevel} onChange={(e) => setForm({ ...form, classLevel: e.target.value })} className={inp}>
                                    <option value="">Select</option>
                                    {['9', '10', '11', '12'].map((c) => <option key={c} value={c}>Class {c}</option>)}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Board</label>
                                <select value={form.board} onChange={(e) => setForm({ ...form, board: e.target.value })} className={inp}>
                                    <option value="">Select</option>
                                    <option value="Federal Board">Federal Board</option>
                                    <option value="AJK Board">AJK Board</option>
                                </select>
                            </div>
                        </div>
                        <button type="submit" className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg transition text-sm font-semibold">Update Profile</button>
                    </form>
                </div>

                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 md:p-8">
                    <div className="flex items-center justify-between mb-5">
                        <h3 className="font-bold text-gray-800 dark:text-white">Change Password</h3>
                        {!showPassword && <button onClick={() => setShowPassword(true)} className="text-sm text-[#2563EB] font-semibold hover:underline">Change</button>}
                    </div>
                    {showPassword ? (
                        <form onSubmit={handlePasswordChange} className="space-y-4">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Current Password</label>
                                <input type="password" value={passwords.current} onChange={(e) => setPasswords({ ...passwords, current: e.target.value })} className={inp} placeholder="Current password" />
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">New Password</label>
                                <input type="password" value={passwords.newPass} onChange={(e) => setPasswords({ ...passwords, newPass: e.target.value })} className={inp} placeholder="New password" />
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Confirm</label>
                                <input type="password" value={passwords.confirm} onChange={(e) => setPasswords({ ...passwords, confirm: e.target.value })} className={inp} placeholder="Confirm new password" />
                            </div>
                            <div className="flex gap-3">
                                <button type="button" onClick={() => { setShowPassword(false); setPasswords({ current: '', newPass: '', confirm: '' }); }} className="flex-1 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-3 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition text-sm font-semibold">Cancel</button>
                                <button type="submit" className="flex-1 bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg transition text-sm font-semibold">Save</button>
                            </div>
                        </form>
                    ) : (
                        <p className="text-sm text-gray-400 dark:text-gray-500">Click &quot;Change&quot; to update your password.</p>
                    )}
                </div>
            </div>
        </>
    );
}

Profile.layout = (page: React.ReactNode) => <StudentLayout currentPage="profile">{page}</StudentLayout>;
