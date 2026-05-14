import { useState, useRef, useEffect, useCallback } from 'react';
import { Head, usePage } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';
import LogoES from '@/components/logo-es';
import { api } from '@/lib/api';

interface User {
    name: string;
    email: string;
    role?: string;
    subject?: string;
    class_level?: string;
    board?: string;
}

declare global {
    interface Window {
        SpeechRecognition: new () => SpeechRecognition;
        webkitSpeechRecognition: new () => SpeechRecognition;
    }
    interface SpeechRecognition extends EventTarget {
        continuous: boolean;
        interimResults: boolean;
        lang: string;
        onresult: ((event: { results: { [index: number]: { [index: number]: { transcript: string } } } }) => void) | null;
        onerror: (() => void) | null;
        onend: (() => void) | null;
        start(): void;
        stop(): void;
    }
}

interface Message {
    role: 'user' | 'assistant';
    text: string;
}

interface ChatSession {
    id: number;
    title: string;
    subject?: string;
    class_level?: string;
    messages: Message[];
    timestamp: string;
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
    { value: 'computer', label: 'Computer' },
    { value: 'english', label: 'English' },
    { value: 'urdu', label: 'Urdu' },
];

const getLabel = (list: { value: string; label: string }[], value: string) =>
    list.find(i => i.value === value)?.label || value;

export default function AiChat() {
    const [sidebarWidth, setSidebarWidth] = useState(250);

    const { auth } = usePage<{ auth: { user: User } }>().props;
    const user = auth.user;

    // Read subject/board/class from URL query params, fall back to user profile
    const urlParams = new URLSearchParams(window.location.search);
    const initialBoard = urlParams.get('board') || user?.board || '';
    const initialClassLevel = urlParams.get('class_level') || user?.class_level || '';
    const initialSubject = urlParams.get('subject') || user?.subject || '';

    // Active preferences (can be changed via popup)
    const [activeBoard, setActiveBoard] = useState(initialBoard);
    const [activeClassLevel, setActiveClassLevel] = useState(initialClassLevel);
    const [activeSubject, setActiveSubject] = useState(initialSubject);

    // Subject selector popup
    const needsSelection = !activeBoard || !activeClassLevel || !activeSubject;
    const [showSelector, setShowSelector] = useState(needsSelection);
    const [selectorBoard, setSelectorBoard] = useState(activeBoard);
    const [selectorClass, setSelectorClass] = useState(activeClassLevel);
    const [selectorSubject, setSelectorSubject] = useState(activeSubject);

    // Chat history
    const [sessions, setSessions] = useState<ChatSession[]>([]);
    const [activeSessionId, setActiveSessionId] = useState<number | null>(null);
    const [sidebarOpen, setSidebarOpen] = useState(false);

    // Chat state
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
    const [isListening, setIsListening] = useState(false);
    const [isSpeaking, setIsSpeaking] = useState(false);
    const [voiceEnabled, setVoiceEnabled] = useState(false);
    const endRef = useRef<HTMLDivElement>(null);
    const recognitionRef = useRef<SpeechRecognition | null>(null);

// chat memory

// useEffect(() => {
//     if (!activeSessionId) return;

//     const fetchMessages = async () => {
//         const res = await api(`/chat/history/${activeSessionId}`);
//         const data = await res.json();

//         setMessages(data.messages || []);
//     };

//     fetchMessages();
// }, [activeSessionId]);

    useEffect(() => {
        endRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    useEffect(() => {
        const SpeechRecognitionAPI = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (SpeechRecognitionAPI) {
            const recognition = new SpeechRecognitionAPI();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-US';
            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                if (transcript.trim()) {
                    sendMessage(transcript);
                }
                setIsListening(false);
            };
            recognition.onerror = () => setIsListening(false);
            recognition.onend = () => setIsListening(false);
            recognitionRef.current = recognition;
        }
    }, []);

    const speakText = useCallback((text: string) => {
        if (!voiceEnabled) return;
        window.speechSynthesis.cancel();
        const clean = text.replace(/[\u2022\n]/g, '. ').replace(/\d+\.\s/g, '');
        const utterance = new SpeechSynthesisUtterance(clean);
        utterance.rate = 0.95;
        utterance.pitch = 1;
        utterance.onstart = () => setIsSpeaking(true);
        utterance.onend = () => setIsSpeaking(false);
        utterance.onerror = () => setIsSpeaking(false);
        window.speechSynthesis.speak(utterance);
    }, [voiceEnabled]);

    const stopSpeaking = () => {
        window.speechSynthesis.cancel();
        setIsSpeaking(false);
    };

    const toggleListening = () => {
        if (!recognitionRef.current) return;
        if (isListening) {
            recognitionRef.current.stop();
            setIsListening(false);
        } else {
            recognitionRef.current.start();
            setIsListening(true);
        }
    };

    const saveCurrentSession = useCallback(async (msgs: Message[]) => {
        if (msgs.length === 0) return;

        const title = msgs[0].text.slice(0, 40);

        try {
            const res = await api('/chats', {
                method: 'POST',
                body: JSON.stringify({
                    id: activeSessionId,
                    title,
                    messages: msgs,
                    subject: activeSubject,
    class_level: activeClassLevel,
    board: activeBoard,
                }),
            });

            const data = await res.json();
            setActiveSessionId(data.chat_id);
        } catch (err) {
            console.error(err);
        }
    }, [activeSessionId, activeSubject, activeClassLevel, activeBoard]);





    const sendMessage = useCallback(async (text: string) => {
        if (!text.trim() || loading) return;

        const userMsg: Message = { role: 'user', text };

        const updatedMessages = [...messages, userMsg];
        setMessages(updatedMessages);
        setInput('');
        setLoading(true);

        try {
            // const res = await api('/chat/send', {
            //     method: 'POST',
            //     body: JSON.stringify({
            //         message: text,
            //         session_id: activeSessionId,
            //         board: activeBoard,
            //         class_level: activeClassLevel,
            //         subject: activeSubject,
            //     }),
            // });
            const chatHistory = messages
    .slice(-10)
    .map((m) => ({
        // role: m.role,
        // role: m.role === 'ai' ? 'assistant' : 'user',
        role: m.role,
        content: m.text,
    }));

const res = await api('/chat/send', {
    method: 'POST',
    body: JSON.stringify({
        message: text,
        session_id: activeSessionId,
        board: activeBoard,
        class_level: activeClassLevel,
        subject: activeSubject,
        chat_history: chatHistory,

    }),
});


            const data = await res.json();

           const aiMsg: Message = {
    role: 'assistant',
    text: data.reply ?? 'No response',
};

            const finalMessages = [...updatedMessages, aiMsg];
            setMessages(finalMessages);

            if (!activeSessionId && data.session_id) {
                setActiveSessionId(data.session_id);
                fetchSessions();
            }
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    }, [messages, activeSessionId, loading, activeBoard, activeClassLevel, activeSubject]);

    const startNewChat = () => {
        setMessages([]);
        setActiveSessionId(null);
        setSidebarOpen(false);

        localStorage.removeItem('active_chat_id');
    };

    const loadSession = async (session: ChatSession) => {
        setActiveSessionId(session.id);
        setSidebarOpen(false);

         // restore chat context
    if (session.subject) {
        setActiveSubject(session.subject);
    }

    if (session.class_level) {
        setActiveClassLevel(session.class_level);
    }

    if (session.board) {
        setActiveBoard(session.board);
    }

        try {
            const res = await api(`/chat/messages/${session.id}`);
            const data = await res.json();

            const formatted = data.map((m: any) => ({
                role: m.role,
                text: m.message,
            }));

            setMessages(formatted);
        } catch (err) {
            console.error(err);
        }
    };

    const deleteSession = async (id: number) => {
        try {
            await api(`/chat/${id}`, { method: 'DELETE' });
            setSessions(prev => prev.filter(s => s.id !== id));

            if (activeSessionId === id) {
                setMessages([]);
                setActiveSessionId(null);
            }
        } catch (err) {
            console.error(err);
        }
    };

    const hasSpeechRecognition = typeof window !== 'undefined' && !!(window.SpeechRecognition || window.webkitSpeechRecognition);

    const subjectLabel = activeSubject ? getLabel(subjects, activeSubject) : '';
    const classLabel = activeClassLevel ? getLabel(classes, activeClassLevel) : '';
    const subjectInfo = activeSubject && activeClassLevel ? `${subjectLabel} — ${classLabel}` : null;

    // useEffect(() => {
    //     fetchSessions();
    // }, []);
    useEffect(() => {
    const restoreChat = async () => {
        try {
            // load all sessions
            const res = await api('/chat/sessions');
            const data = await res.json();

            const allSessions = Array.isArray(data) ? data : [];

            setSessions(allSessions);

            // restore active session
            const savedId = localStorage.getItem('active_chat_id');

            if (savedId) {
                const sessionId = Number(savedId);

                const foundSession = allSessions.find(
                    (s: ChatSession) => s.id === sessionId
                );

                if (foundSession) {

                    // restore subject/class/board
                    if (foundSession.subject) {
                        setActiveSubject(foundSession.subject);
                    }

                    if (foundSession.class_level) {
                        setActiveClassLevel(foundSession.class_level);
                    }

                    if (foundSession.board) {
                        setActiveBoard(foundSession.board);
                    }

                    // restore session id
                    // setActiveSessionId(foundSession.id);
                    await loadSession(foundSession);
                }
            }
        } catch (err) {
            console.error(err);
        }
    };

    restoreChat();
}, []);

useEffect(() => {
    if (activeSessionId) {
        localStorage.setItem(
            'active_chat_id',
            activeSessionId.toString()
        );
    }
}, [activeSessionId]);

    const fetchSessions = async () => {
        try {
            const res = await api('/chat/sessions');
            const data = await res.json();
            setSessions(Array.isArray(data) ? data : []);
        } catch (err) {
            console.error(err);
        }
    };

    const handleSelectorConfirm = () => {
        if (selectorBoard && selectorClass && selectorSubject) {
            setActiveBoard(selectorBoard);
            setActiveClassLevel(selectorClass);
            setActiveSubject(selectorSubject);
            setShowSelector(false);
            // Start a new chat when subject changes
            setMessages([]);
            setActiveSessionId(null);
        }
    };

    const sel = 'w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white hover:bg-white dark:hover:bg-gray-600 transition';

    return (
        <>
            <Head title="AI Chat" />

            {/* Subject Selector Popup */}
            {showSelector && (
                <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4">
                    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 w-full max-w-md p-6">
                        <div className="text-center mb-6">
                            <div className="w-14 h-14 bg-gradient-to-br from-blue-100 to-indigo-100 dark:from-blue-900/30 dark:to-indigo-900/30 rounded-2xl flex items-center justify-center mx-auto mb-3">
                                <i className="fa-solid fa-book-open text-[#2563EB] text-xl" />
                            </div>
                            <h3 className="text-lg font-bold text-gray-800 dark:text-white">Select Your Subject</h3>
                            <p className="text-xs text-gray-400 dark:text-gray-500 mt-1">Choose what you want to study</p>
                        </div>
                        <div className="space-y-4">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Board</label>
                                <select value={selectorBoard} onChange={(e) => setSelectorBoard(e.target.value)} className={sel}>
                                    <option value="">Select Board</option>
                                    {boards.map((b) => <option key={b.value} value={b.value}>{b.label}</option>)}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Class</label>
                                <select value={selectorClass} onChange={(e) => { setSelectorClass(e.target.value); setSelectorSubject(''); }} className={sel}>
                                    <option value="">Select Class</option>
                                    {classes.map((c) => <option key={c.value} value={c.value}>{c.label}</option>)}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Subject</label>
                                <select value={selectorSubject} onChange={(e) => setSelectorSubject(e.target.value)} disabled={!selectorClass} className={`${sel} disabled:opacity-50 disabled:cursor-not-allowed`}>
                                    <option value="">Select Subject</option>
                                    {subjects.map((s) => <option key={s.value} value={s.value}>{s.label}</option>)}
                                </select>
                            </div>
                            <button
                                onClick={handleSelectorConfirm}
                                disabled={!selectorBoard || !selectorClass || !selectorSubject}
                                className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg disabled:opacity-40 disabled:cursor-not-allowed transition-all duration-200 text-sm font-semibold flex items-center justify-center gap-2"
                            >
                                Start Learning <i className="fa-solid fa-arrow-right" />
                            </button>
                        </div>
                        {!needsSelection && (
                            <button onClick={() => setShowSelector(false)} className="w-full mt-3 text-sm text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 transition">
                                Cancel
                            </button>
                        )}
                    </div>
                </div>
            )}

            <div className="flex h-full overflow-hidden bg-[#F8FAFC] dark:bg-gray-900">
                {/* History Sidebar */}
                {sidebarOpen && <div className="md:hidden fixed inset-0 bg-black/40 backdrop-blur-sm z-30" onClick={() => setSidebarOpen(false)} />}
                <aside
                    style={{ width: sidebarWidth }}
                    className={`fixed md:relative top-0 left-0 h-full bg-white dark:bg-gray-800 border-r border-gray-100 dark:border-gray-700 z-30 flex flex-col transition-transform duration-300 ${sidebarOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}`}
                >
                    <div
                        onMouseDown={(e) => {
                            e.preventDefault();
                            const startX = e.clientX;
                            const startWidth = sidebarWidth;
                            const onMouseMove = (e: MouseEvent) => {
                                const newWidth = startWidth + (e.clientX - startX);
                                if (newWidth > 220 && newWidth < 500) setSidebarWidth(newWidth);
                            };
                            const onMouseUp = () => {
                                document.removeEventListener('mousemove', onMouseMove);
                                document.removeEventListener('mouseup', onMouseUp);
                            };
                            document.addEventListener('mousemove', onMouseMove);
                            document.addEventListener('mouseup', onMouseUp);
                        }}
                        className="absolute top-0 right-0 w-1 h-full cursor-col-resize bg-gray-300 dark:bg-gray-600 hover:bg-blue-500 z-50"
                    />
                    <div className="p-4 border-b border-gray-100 dark:border-gray-700">
                        <button
                            onClick={startNewChat}
                            className="w-full flex items-center justify-center gap-2 bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg transition-all duration-200 text-sm font-semibold"
                        >
                            <i className="fa-solid fa-plus" />
                            New Chat
                        </button>
                    </div>
                    <div className="flex-1 overflow-y-auto p-3 space-y-1">
                        {sessions.length === 0 ? (
                            <div className="text-center py-10">
                                <i className="fa-solid fa-clock-rotate-left text-gray-300 dark:text-gray-600 text-3xl mb-3" />
                                <p className="text-xs text-gray-400 dark:text-gray-500">No chat history yet</p>
                            </div>
                        ) : (
                            sessions.map((s) => (
                                <div
                                    key={s.id}
                                    className={`group flex items-center gap-2 px-3 py-2.5 rounded-xl cursor-pointer transition-all duration-200 ${activeSessionId === s.id ? 'bg-blue-50 dark:bg-blue-900/30 text-[#2563EB]' : 'text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700'}`}
                                >
                                    <button onClick={() => loadSession(s)} className="flex-1 text-left min-w-0">
                                        <p className="text-sm font-medium truncate">{s.title}</p>
                                        {s.subject && (
                                            <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5 flex items-center gap-1">
                                                <i className="fa-solid fa-book-open text-[10px]" />
                                                {getLabel(subjects, s.subject)} — {getLabel(classes, s.class_level || '')}
                                            </p>
                                        )}
                                    </button>
                                    <button
                                        onClick={(e) => { e.stopPropagation(); deleteSession(s.id); }}
                                        className="opacity-0 group-hover:opacity-100 p-1 text-gray-400 hover:text-red-500 transition"
                                    >
                                        <i className="fa-solid fa-trash text-xs" />
                                    </button>
                                </div>
                            ))
                        )}
                    </div>
                    {subjectInfo && (
                        <div className="p-4 border-t border-gray-100 dark:border-gray-700">
                            <button
                                onClick={() => { setSelectorBoard(activeBoard); setSelectorClass(activeClassLevel); setSelectorSubject(activeSubject); setShowSelector(true); }}
                                className="w-full flex items-center justify-between gap-2 text-xs text-gray-500 dark:text-gray-400 hover:text-[#2563EB] dark:hover:text-[#2563EB] transition"
                            >
                                <span className="flex items-center gap-2">
                                    <i className="fa-solid fa-book-open" />
                                    {subjectInfo}
                                </span>
                                <i className="fa-solid fa-pen-to-square" />
                            </button>
                        </div>
                    )}
                </aside>

                {/* Main Chat Area */}
                <div className="flex-1 flex flex-col min-w-0">
                    {/* Header */}
                    <div className="px-4 md:px-6 py-4 bg-white dark:bg-gray-800 border-b border-gray-100 dark:border-gray-700 flex-shrink-0">
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-3">
                                <button onClick={() => setSidebarOpen(!sidebarOpen)} className="md:hidden p-2 -ml-2 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200">
                                    <i className="fa-solid fa-bars" />
                                </button>
                                <div className="w-10 h-10 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-xl flex items-center justify-center shadow-md shadow-blue-100 dark:shadow-blue-900/30">
                                    <LogoES className="w-6 h-6" />
                                </div>
                                <div>
                                    <h2 className="font-bold text-gray-800 dark:text-white">AI Learning Assistant</h2>
                                    <p className="text-xs text-emerald-500 flex items-center gap-1">
                                        <span className="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-pulse" />
                                        Online{subjectInfo ? ` — ${subjectInfo}` : ''}
                                    </p>
                                </div>
                            </div>
                            <div className="flex items-center gap-2">
                                <button
                                    onClick={() => { setSelectorBoard(activeBoard); setSelectorClass(activeClassLevel); setSelectorSubject(activeSubject); setShowSelector(true); }}
                                    className="flex items-center gap-2 px-3 py-2 rounded-xl text-xs font-semibold bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600 transition-all duration-200"
                                    title="Change subject"
                                >
                                    <i className="fa-solid fa-exchange-alt" />
                                    Change
                                </button>
                                <button
                                    onClick={() => { setVoiceEnabled(!voiceEnabled); if (isSpeaking) stopSpeaking(); }}
                                    className={`flex items-center gap-2 px-3 py-2 rounded-xl text-xs font-semibold transition-all duration-200 ${voiceEnabled ? 'bg-[#2563EB] text-white shadow-md' : 'bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600'}`}
                                >
                                    <i className={`fa-solid ${voiceEnabled ? 'fa-volume-high' : 'fa-volume-xmark'}`} />
                                    {voiceEnabled ? 'Voice On' : 'Voice Off'}
                                </button>
                            </div>
                        </div>
                    </div>

                    {/* Messages */}
                    <div className="flex-1 min-h-0 overflow-y-auto px-4 md:px-6 py-4">
                        {messages.length === 0 ? (
                            <div className="flex items-center justify-center h-full">
                                <div className="text-center">
                                    <div className="w-20 h-20 bg-gradient-to-br from-blue-100 to-indigo-100 dark:from-blue-900/30 dark:to-indigo-900/30 rounded-full flex items-center justify-center mx-auto mb-5">
                                        <LogoES className="w-10 h-10" />
                                    </div>
                                    <h3 className="text-lg font-semibold text-gray-700 dark:text-gray-200 mb-2">How can I help you today?</h3>
                                    <p className="text-sm text-gray-400 dark:text-gray-500 max-w-sm mx-auto mb-8">Ask me anything about your syllabus — Physics, Chemistry, Biology, Maths, or English.</p>
                                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 max-w-md mx-auto">
                                        {["Explain Newton's Laws", 'What is photosynthesis?', 'Solve: 2x + 5 = 15', 'Define atomic number'].map((q) => (
                                            <button key={q} onClick={() => sendMessage(q)} className="text-left bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl px-4 py-3 text-sm text-gray-600 dark:text-gray-300 hover:border-[#2563EB] hover:text-[#2563EB] transition">
                                                {q}
                                            </button>
                                        ))}
                                    </div>
                                </div>
                            </div>
                        ) : (
                            <div className="space-y-4">
                                {messages.map((msg, i) => (
                                    <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                                        {msg.role === 'assistant' && (
                                            <div className="w-8 h-8 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-full flex items-center justify-center mr-2 mt-1 flex-shrink-0">
                                                <LogoES className="w-4 h-4" />
                                            </div>
                                        )}
                                        <div className={`max-w-[75%] text-sm leading-relaxed ${msg.role === 'user' ? 'bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white rounded-2xl rounded-br-md shadow-md shadow-blue-100 dark:shadow-blue-900/20 px-4 py-3' : ''}`}>
                                            {msg.role === 'assistant' ? (
                                                <div className="bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-200 rounded-2xl rounded-bl-md shadow-sm border border-gray-100 dark:border-gray-700 overflow-hidden">
                                                    <div className="px-4 py-3 whitespace-pre-wrap">{msg.text}</div>
                                                    {voiceEnabled && (
                                                        <div className="px-4 py-2 border-t border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-gray-700/50">
                                                            <button onClick={() => isSpeaking ? stopSpeaking() : speakText(msg.text)} className="flex items-center gap-1.5 text-xs text-gray-500 dark:text-gray-400 hover:text-[#2563EB] transition">
                                                                <i className={`fa-solid ${isSpeaking ? 'fa-stop' : 'fa-volume-high'} text-[10px]`} />
                                                                {isSpeaking ? 'Stop' : 'Listen'}
                                                            </button>
                                                        </div>
                                                    )}
                                                </div>
                                            ) : msg.text}
                                        </div>
                                    </div>
                                ))}
                                {loading && (
                                    <div className="flex items-center gap-2">
                                        <div className="w-8 h-8 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-full flex items-center justify-center flex-shrink-0">
                                            <LogoES className="w-4 h-4" />
                                        </div>
                                        <div className="bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 rounded-2xl rounded-bl-md shadow-sm px-4 py-3">
                                            <div className="flex gap-1.5">
                                                <span className="w-2 h-2 bg-[#2563EB] rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                                                <span className="w-2 h-2 bg-[#2563EB] rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                                                <span className="w-2 h-2 bg-[#2563EB] rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                                            </div>
                                        </div>
                                    </div>
                                )}
                                <div ref={endRef} />
                            </div>
                        )}
                    </div>

                    {/* Input */}
                    <div className="p-4 bg-white dark:bg-gray-800 border-t border-gray-100 dark:border-gray-700 flex-shrink-0">
                        <div className="flex gap-2 mb-3">
                            {['Explain', 'Simplify', 'Example'].map((action) => (
                                <button key={action} onClick={() => sendMessage(action)} disabled={loading} className="px-4 py-2 bg-blue-50 dark:bg-blue-900/30 text-[#2563EB] rounded-xl text-xs font-semibold hover:bg-blue-100 dark:hover:bg-blue-900/50 disabled:opacity-50 transition">
                                    {action}
                                </button>
                            ))}
                        </div>
                        <form onSubmit={(e) => { e.preventDefault(); sendMessage(input); }} className="flex gap-3">
                            <input
                                type="text"
                                value={input}
                                onChange={(e) => setInput(e.target.value)}
                                placeholder={isListening ? 'Listening...' : 'Ask any question...'}
                                className={`flex-1 border rounded-xl px-5 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white ${isListening ? 'border-red-400 ring-2 ring-red-200 dark:ring-red-800 animate-pulse' : 'border-gray-200 dark:border-gray-600'}`}
                            />
                            {hasSpeechRecognition && (
                                <button
                                    type="button"
                                    onClick={toggleListening}
                                    className={`px-4 py-3 rounded-xl transition-all duration-200 text-sm font-semibold ${isListening ? 'bg-red-500 text-white shadow-lg animate-pulse' : 'bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'}`}
                                    title={isListening ? 'Stop listening' : 'Voice input'}
                                >
                                    <i className="fa-solid fa-microphone text-lg" />
                                </button>
                            )}
                            <button
                                type="submit"
                                disabled={!input.trim() || loading}
                                className="bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white px-6 py-3 rounded-xl hover:shadow-lg disabled:opacity-40 disabled:shadow-none transition-all duration-200 text-sm font-semibold flex items-center gap-2"
                            >
                                <i className="fa-solid fa-paper-plane" />
                                Send
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </>
    );
}

AiChat.layout = (page: React.ReactNode) => <StudentLayout currentPage="aichat" isChat>{page}</StudentLayout>;
