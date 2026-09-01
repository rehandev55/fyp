import { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import AdminLayout from '@/layouts/admin-layout';
import axios from "axios";
import { backendApi } from '@/lib/backendApi';
import { API_URL } from "@/lib/backendApi";

interface ContentItem {
    id: number;
    title: string;
    type: string;
    board: string;
    class_level: string;
    subject: string;
    date: string;
    downloads: number;
    size: string;
}

interface Modal {
    type: 'view' | 'edit' | 'delete';
    item: ContentItem;
}


const contentTypes = ['Book', 'Key Book', 'Past Paper', 'Notes', 'Solved Paper', 'Worksheet'];

function Content() {
    const [content, setContent] = useState<ContentItem[]>([]);
    const [showUpload, setShowUpload] = useState(false);
    const [filterType, setFilterType] = useState('');
    const [search, setSearch] = useState('');
    const [modal, setModal] = useState<Modal | null>(null);
    const [editForm, setEditForm] = useState<ContentItem>({} as ContentItem);
    const [form, setForm] = useState({ title: '', type: 'Book', board: 'federal', class_level: 'class_10', subject: 'physics' });

    const filtered = content.filter((c) => (!filterType || c.type === filterType) && (!search || c.title.toLowerCase().includes(search.toLowerCase())));
    const [uploadProgress, setUploadProgress] = useState(0);   //use state for upload progress

const handleUpload = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!file) return;

    const formData = new FormData();
    formData.append("title", form.title);
    formData.append("type", form.type);
    formData.append("board", form.board);
    formData.append("class_level", form.class_level);
    formData.append("subject", form.subject);
    formData.append("file", file);

    try {
        console.log("FORM DATA:", formData);
        formData.forEach((value, key) => {
    console.log(key, value);
});
        const res = await axios.post(
             `${API_URL}/api/content`,
            formData,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
                onUploadProgress: (progressEvent) => {
                    const percent = Math.round(
                        (progressEvent.loaded * 100) / (progressEvent.total || 1)
                    );
                    setUploadProgress(percent);
                },
            }
        );

        console.log(res.data); // 👈 VERY IMPORTANT

        // success reset
        setUploadProgress(0);
        setShowUpload(false);
        fetchContent();

    } catch (err: any) {
        console.error("UPLOAD ERROR:", err.response?.data || err.message);

        // ❗ reset even on error
        setUploadProgress(0);
    }
};

    const openEdit = (c: ContentItem) => {
        setEditForm({ ...c });
        setModal({ type: 'edit', item: c });
    };

    const saveEdit = async () => {
    try {
        await backendApi(`/api/content/${editForm.id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                title: editForm.title,
                type: editForm.type,
                board: editForm.board,
                class_level: editForm.class_level,
                subject: editForm.subject,
            }),
        });

        // keep your UI update (so it feels instant)
        setContent((prev) =>
            prev.map((c) => (c.id === editForm.id ? { ...editForm } : c))
        );

        setModal(null);

    } catch (err) {
        console.error("Edit failed:", err);
    }
};

const deleteContent = async (id: number) => {
    try {
        await backendApi(`/api/content/${id}`, {
            method: "DELETE",
        });

        // update UI
        setContent((prev) => prev.filter((c) => c.id !== id));

        setModal(null);

    } catch (err) {
        console.error("Delete failed:", err);
    }
};

    const sel =
        'w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#7C3AED] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white transition';
    const typeColors: Record<string, string> = {
        Book: 'bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300',
        'Key Book': 'bg-emerald-50 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-300',
        'Past Paper': 'bg-purple-50 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300',
        Notes: 'bg-amber-50 dark:bg-amber-900/30 text-amber-700 dark:text-amber-300',
        'Solved Paper': 'bg-pink-50 dark:bg-pink-900/30 text-pink-700 dark:text-pink-300',
        Worksheet: 'bg-cyan-50 dark:bg-cyan-900/30 text-cyan-700 dark:text-cyan-300',
    };
    const typeIcons: Record<string, string> = {
        Book: 'fa-solid fa-book',
        'Key Book': 'fa-solid fa-key',
        'Past Paper': 'fa-solid fa-file-lines',
        Notes: 'fa-solid fa-sticky-note',
        'Solved Paper': 'fa-solid fa-check-double',
        Worksheet: 'fa-solid fa-file-pen',
    };
const [file, setFile] = useState<File | null>(null);
    const totalDownloads = content.reduce((a, c) => a + c.downloads, 0);
    const downloadsByType = contentTypes
        .map((t) => ({
            type: t,
            downloads: content.filter((c) => c.type === t).reduce((a, c) => a + c.downloads, 0),
        }))
        .filter((d) => d.downloads > 0);


        useEffect(() => {
    fetchContent();
}, []);

const fetchContent = async () => {
    const res = await backendApi("/api/content");
    const data = await res.json();


    setContent(data.data);
};

const downloadFile = (id: number) => {
    window.open(`${API_URL}/api/content/download/${id}`);
};

    return (
        <div className="space-y-6">
            <div className="flex items-center justify-between flex-wrap gap-4">
                <div>
                    <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Content Manager</h2>
                    <p className="text-gray-400 dark:text-gray-500 text-sm mt-0.5">
                        {content.length} resources — {totalDownloads.toLocaleString()} total downloads
                    </p>
                </div>
                <button
                    onClick={() => setShowUpload(!showUpload)}
                    className="bg-gradient-to-r from-[#7C3AED] to-[#9333EA] text-white px-5 py-2.5 rounded-xl hover:shadow-lg transition-all duration-200 text-sm font-semibold flex items-center gap-2"
                >
                    <i className="fa-solid fa-plus" /> Upload Content
                </button>
            </div>

            {/* Mini stats + Chart */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
                <div className="grid grid-cols-2 gap-4 lg:col-span-1">
                    {[
                        { label: 'Total Files', value: content.length, icon: 'fa-solid fa-file', color: 'text-blue-600 bg-blue-50 dark:bg-blue-900/30' },
                        { label: 'Downloads', value: totalDownloads.toLocaleString(), icon: 'fa-solid fa-download', color: 'text-emerald-600 bg-emerald-50 dark:bg-emerald-900/30' },
                        { label: 'Types', value: new Set(content.map((c) => c.type)).size, icon: 'fa-solid fa-tags', color: 'text-purple-600 bg-purple-50 dark:bg-purple-900/30' },
                        { label: 'Subjects', value: new Set(content.map((c) => c.subject)).size, icon: 'fa-solid fa-book-open', color: 'text-amber-600 bg-amber-50 dark:bg-amber-900/30' },
                    ].map((s) => (
                        <div key={s.label} className="bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 p-4">
                            <div className={`w-9 h-9 rounded-lg flex items-center justify-center mb-2 ${s.color}`}>
                                <i className={`${s.icon} text-sm`} />
                            </div>
                            <p className="text-lg font-bold text-gray-800 dark:text-white">{s.value}</p>
                            <p className="text-xs text-gray-400">{s.label}</p>
                        </div>
                    ))}
                </div>
                <div className="lg:col-span-2 bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                    <h3 className="font-bold text-gray-800 dark:text-white mb-4 text-sm flex items-center gap-2">
                        <i className="fa-solid fa-chart-column text-purple-500 text-xs" /> Downloads by Type
                    </h3>
                    <ResponsiveContainer width="100%" height={160}>
                        <BarChart data={downloadsByType}>
                            <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
                            <XAxis dataKey="type" tick={{ fontSize: 11 }} stroke="#9CA3AF" />
                            <YAxis tick={{ fontSize: 11 }} stroke="#9CA3AF" />
                            <Tooltip contentStyle={{ borderRadius: '12px', border: '1px solid #e5e7eb', fontSize: '12px' }} />
                            <Bar dataKey="downloads" fill="#7C3AED" radius={[6, 6, 0, 0]} />
                        </BarChart>
                    </ResponsiveContainer>
                </div>
            </div>

            {/* Upload Form */}
            {showUpload && (
                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 md:p-8">
                    <h3 className="font-bold text-gray-800 dark:text-white mb-5 flex items-center gap-2">
                        <i className="fa-solid fa-cloud-arrow-up text-[#7C3AED]" /> Upload New Content
                    </h3>
                    <form onSubmit={handleUpload} className="space-y-4">
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Title</label>
                            <input
                                type="text"
                                value={form.title}
                                onChange={(e) => setForm({ ...form, title: e.target.value })}
                                className={sel}
                                placeholder="e.g., Physics Past Papers 2025"
                            />
                        </div>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Content Type</label>
                                <select value={form.type} onChange={(e) => setForm({ ...form, type: e.target.value })} className={sel}>
                                    {contentTypes.map((t) => (
                                        <option key={t} value={t}>
                                            {t}
                                        </option>
                                    ))}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Subject</label>
                                <select value={form.subject} onChange={(e) => setForm({ ...form, subject: e.target.value })} className={sel}>
                                    {['physics', 'chemistry', 'biology', 'mathematics','computer', 'english'].map((s) => (
                                        <option key={s} value={s}>
                                            {s}
                                        </option>
                                    ))}
                                </select>
                            </div>
                        </div>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Board</label>
                                <select value={form.board} onChange={(e) => setForm({ ...form, board: e.target.value })} className={sel}>
                                    <option value="federal">Federal Board</option>
                                    <option value="ajk">AJK Board</option>
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Class</label>
                                <select
    value={form.class_level}
    onChange={(e) => setForm({ ...form, class_level: e.target.value })}
    className={sel}
>
    {['class_9', 'class_10', 'class_11', 'class_12'].map((c) => (
        <option key={c} value={c}>
            Class {c.split('_')[1]}
        </option>
    ))}
</select>
                            </div>
                        </div>
                        <div>
                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">File</label>

                            {uploadProgress > 0 && (
    <div className="w-full bg-gray-200 rounded-full h-2 mb-3">
        <div
            className="bg-[#7C3AED] h-2 rounded-full transition-all"
            style={{ width: `${uploadProgress}%` }}
        ></div>
        <p className="text-xs text-gray-500 mt-1 text-right">
            {uploadProgress}%
        </p>
    </div>
)}
                            {/* <input
    type="file"
    onChange={(e) => setFile(e.target.files?.[0] || null)}
/> */}
<label className="w-full cursor-pointer">
    <div className="w-full bg-gradient-to-r from-[#7C3AED] to-[#9333EA] text-white py-3 rounded-xl text-sm font-semibold flex items-center justify-center gap-2 hover:shadow-lg active:scale-95 transition">
        <i className="fa-solid fa-upload text-xs" />
        {file ? file.name : "Choose File"}
    </div>

    <input
        type="file"
        className="hidden"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
    />
</label>

                        </div>
                        <div className="flex gap-3 pt-2">
                            <button
                                type="button"
                                onClick={() => setShowUpload(false)}
                                className="flex-1 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-3 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition text-sm font-semibold"
                            >
                                Cancel
                            </button>
                            <button
                                type="submit"
                                disabled={!form.title}
                                className="flex-1 bg-gradient-to-r from-[#7C3AED] to-[#9333EA] text-white py-3 rounded-xl
hover:shadow-lg active:scale-95 active:brightness-90
disabled:opacity-40 transition-all duration-150 text-sm font-semibold"
                            >
                                Upload
                            </button>
                        </div>
                    </form>
                </div>
            )}
            {/* Search + Type Filters */}
            <div className="space-y-4">
                <div className="relative max-w-md">
                    <i className="fa-solid fa-magnifying-glass text-gray-400 absolute left-3 top-1/2 -translate-y-1/2 text-sm" />
                    <input
                        type="text"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        placeholder="Search content..."
                        className="w-full border border-gray-200 dark:border-gray-600 rounded-xl pl-10 pr-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-[#7C3AED] bg-white dark:bg-gray-700 dark:text-white transition"
                    />
                </div>
                <div className="flex items-center gap-2 flex-wrap">
                    <button
                        onClick={() => setFilterType('')}
                        className={`px-4 py-2 rounded-xl text-sm font-semibold transition ${!filterType ? 'bg-[#7C3AED] text-white shadow-md' : 'bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-600 text-gray-600 dark:text-gray-300'}`}
                    >
                        All
                    </button>
                    {contentTypes.map((t) => (
                        <button
                            key={t}
                            onClick={() => setFilterType(t)}
                            className={`px-4 py-2 rounded-xl text-sm font-semibold transition ${filterType === t ? 'bg-[#7C3AED] text-white shadow-md' : 'bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-600 text-gray-600 dark:text-gray-300'}`}
                        >
                            {t}
                        </button>
                    ))}
                </div>
            </div>

            {/* Content List */}
            <div className="space-y-3">
                {filtered.map((c) => (
                    <div key={c.id} className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-5 flex items-center gap-4 hover:shadow-lg transition-all duration-300">
                        <div className="w-12 h-12 bg-purple-50 dark:bg-purple-900/20 rounded-xl flex items-center justify-center flex-shrink-0">
                            <i className={`${typeIcons[c.type] || 'fa-solid fa-file'} text-[#7C3AED] text-lg`} />
                        </div>
                        <div className="flex-1 min-w-0">
                            <h4 className="font-semibold text-gray-800 dark:text-white text-sm truncate">{c.title}</h4>
                            <div className="flex items-center gap-2 mt-1 flex-wrap">

                                <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${typeColors[c.type]}`}>{c.type}</span>
                                <span className="text-xs text-gray-400">{c.subject}</span>
                                <span className="text-xs text-gray-400">{c.class_level}</span>
                                <span className="text-xs text-gray-400">{c.size}</span>
                            </div>
                        </div>
                        <div className="text-right hidden sm:block flex-shrink-0 mr-2">
                            <p className="text-sm font-semibold text-gray-800 dark:text-white">{c.downloads}</p>
                            <p className="text-[10px] text-gray-400">downloads</p>
                        </div>
                        <div className="flex items-center gap-1 flex-shrink-0">
                            <button
                                onClick={() => setModal({ type: 'view', item: c })}
                                className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 hover:text-blue-500 transition"
                                title="View"
                            >
                                <i className="fa-solid fa-eye text-xs" />
                            </button>
                            <button
                                onClick={() => openEdit(c)}
                                className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:bg-amber-50 dark:hover:bg-amber-900/20 hover:text-amber-500 transition"
                                title="Edit"
                            >
                                <i className="fa-solid fa-pen text-xs" />
                            </button>
                            <button
                                onClick={() => setModal({ type: 'delete', item: c })}
                                className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:bg-red-50 dark:hover:bg-red-900/20 hover:text-red-500 transition"
                                title="Delete"
                            >
                                <i className="fa-solid fa-trash-can text-xs" />
                            </button>
                            <button onClick={() => downloadFile(c.id)}>
    Download
</button>
                        </div>
                    </div>
                ))}
                {filtered.length === 0 && (
                    <div className="text-center py-16 bg-white dark:bg-gray-800 rounded-2xl border border-gray-100 dark:border-gray-700">
                        <p className="text-gray-400 font-medium">No content found</p>
                    </div>
                )}
            </div>

            {/* Modal */}
            {modal && (
                <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-[100] flex items-center justify-center p-4" onClick={() => setModal(null)}>
                    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-2xl w-full max-w-md max-h-[90vh] overflow-y-auto" onClick={(e) => e.stopPropagation()}>
                        {modal.type === 'view' && (
                            <div className="p-6">
                                <div className="flex items-center justify-between mb-6">
                                    <h3 className="text-lg font-bold text-gray-800 dark:text-white">Content Details</h3>
                                    <button onClick={() => setModal(null)} className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700">
                                        <i className="fa-solid fa-xmark" />
                                    </button>
                                </div>
                                <div className="text-center mb-6">
                                    <div className="w-14 h-14 bg-purple-50 dark:bg-purple-900/20 rounded-2xl flex items-center justify-center mx-auto mb-3">
                                        <i className={`${typeIcons[modal.item.type]} text-[#7C3AED] text-2xl`} />
                                    </div>
                                    <h4 className="font-bold text-gray-800 dark:text-white">{modal.item.title}</h4>
                                    <span className={`text-xs px-2.5 py-1 rounded-full font-semibold mt-2 inline-block ${typeColors[modal.item.type]}`}>{modal.item.type}</span>
                                </div>
                                <div className="space-y-3 text-sm">
                                    {[
                                        { l: 'Subject', v: modal.item.subject, i: 'fa-solid fa-book' },
                                        { l: 'Class', v: `Class ${modal.item.class_level}`, i: 'fa-solid fa-graduation-cap' },
                                        { l: 'Board', v: modal.item.board, i: 'fa-solid fa-building-columns' },
                                        { l: 'Downloads', v: modal.item.downloads, i: 'fa-solid fa-download' },
                                        { l: 'File Size', v: modal.item.size, i: 'fa-solid fa-hard-drive' },
                                        { l: 'Uploaded', v: modal.item.date, i: 'fa-solid fa-calendar' },
                                    ].map((r) => (
                                        <div key={r.l} className="flex items-center justify-between py-2 border-b border-gray-100 dark:border-gray-700 last:border-0">
                                            <span className="text-gray-500 flex items-center gap-2">
                                                <i className={`${r.i} w-4 text-center text-gray-400 text-xs`} />
                                                {r.l}
                                            </span>
                                            <span className="font-medium text-gray-800 dark:text-white">{r.v}</span>
                                        </div>
                                    ))}
                                </div>
                                <button
                                    onClick={() => setModal(null)}
                                    className="w-full mt-6 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-2.5 rounded-xl text-sm font-semibold hover:bg-gray-50 dark:hover:bg-gray-700 transition"
                                >
                                    Close
                                </button>
                            </div>
                        )}
                        {modal.type === 'edit' && (
                            <div className="p-6">
                                <div className="flex items-center justify-between mb-6">
                                    <h3 className="text-lg font-bold text-gray-800 dark:text-white">Edit Content</h3>
                                    <button onClick={() => setModal(null)} className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700">
                                        <i className="fa-solid fa-xmark" />
                                    </button>
                                </div>
                                <div className="space-y-4">
                                    <div>
                                        <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Title</label>
                                        <input type="text" value={editForm.title} onChange={(e) => setEditForm({ ...editForm, title: e.target.value })} className={sel} />
                                    </div>
                                    <div className="grid grid-cols-2 gap-3">
                                        <div>
                                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Type</label>
                                            <select value={editForm.type} onChange={(e) => setEditForm({ ...editForm, type: e.target.value })} className={sel}>
                                                {contentTypes.map((t) => (
                                                    <option key={t} value={t}>
                                                        {t}
                                                    </option>
                                                ))}
                                            </select>
                                        </div>
                                        <div>
                                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Subject</label>
                                            <select value={editForm.subject} onChange={(e) => setEditForm({ ...editForm, subject: e.target.value })} className={sel}>
                                                {['physics', 'chemistry', 'biology', 'mathematics','computer', 'english'].map((s) => (
                                                    <option key={s} value={s}>
                                                        {s}
                                                    </option>
                                                ))}
                                            </select>
                                        </div>
                                    </div>
                                    <div className="grid grid-cols-2 gap-3">
                                        <div>
                                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Board</label>
                                            <select value={editForm.board} onChange={(e) => setEditForm({ ...editForm, board: e.target.value })} className={sel}>
                                                <option value="Federal Board">Federal Board</option>
                                                <option value="AJK Board">AJK Board</option>
                                            </select>
                                        </div>
                                        <div>
                                            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-1">Class</label>
                                            <select value={editForm.class_level} onChange={(e) => setEditForm({ ...editForm, class_level: e.target.value })} className={sel}>
                                                {['class_9', 'class_10', 'class_11', 'class_12'].map((c) => (
                                                    <option key={c} value={c}>
                                                        Class {c}
                                                    </option>
                                                ))}
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
                                        Save
                                    </button>
                                </div>
                            </div>
                        )}
                        {modal.type === 'delete' && (
                            <div className="p-6 text-center">
                                <div className="w-16 h-16 bg-red-50 dark:bg-red-900/30 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <i className="fa-solid fa-triangle-exclamation text-red-500 text-2xl" />
                                </div>
                                <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-2">Delete Content</h3>
                                <p className="text-sm text-gray-500 dark:text-gray-400 mb-6">
                                    Delete <strong>{modal.item.title}</strong>? This cannot be undone.
                                </p>
                                <div className="flex gap-3">
                                    <button
                                        onClick={() => setModal(null)}
                                        className="flex-1 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-2.5 rounded-xl text-sm font-semibold hover:bg-gray-50 dark:hover:bg-gray-700 transition"
                                    >
                                        Cancel
                                    </button>
                                    <button
                                        onClick={() => deleteContent(modal.item.id)}
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

Content.layout = (page: React.ReactNode) => <AdminLayout currentPage="admin-content">{page}</AdminLayout>;

export default Content;
