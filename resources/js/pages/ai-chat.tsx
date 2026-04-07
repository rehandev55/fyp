import { useState, useRef, useEffect, useCallback } from 'react';
import { Head, usePage } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';
import LogoES from '@/components/logo-es';

interface User {
    name: string;
    email: string;
    role?: string;
    subject?: string;
    classLevel?: string;
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

const aiResponses: Record<string, string> = {
    explain: "Let me explain this concept in detail:\n\nThe concept works by breaking down complex topics into simpler parts. In physics, for example, Newton's laws describe the relationship between a body and the forces acting upon it.\n\n1. First Law: An object at rest stays at rest, and an object in motion stays in motion unless acted upon by an external force.\n2. Second Law: Force = Mass x Acceleration (F = ma)\n3. Third Law: For every action, there is an equal and opposite reaction.\n\nThese laws form the foundation of classical mechanics.",
    simplify: "Here's a simpler way to understand it:\n\nThink of it like pushing a shopping cart. The harder you push (more force), the faster it goes (more acceleration). A heavier cart needs more push. And when you push the cart, the cart pushes back on your hands!\n\nThat's basically Newton's three laws in everyday life.",
    example: "Here's a practical example:\n\nImagine you're playing cricket:\n\n\u2022 First Law: The ball stays still on the ground until the bowler picks it up and throws it.\n\u2022 Second Law: The harder the batsman hits (force), the farther the ball goes (acceleration). A heavier ball needs a harder hit.\n\u2022 Third Law: When the bat hits the ball, the ball also pushes back on the bat (that's why you feel the impact in your hands).",
    default: "That's a great question! Let me think about this...\n\nBased on your syllabus, this topic is important for board exams. The key points to remember are:\n\n1. Understand the core concept and its definition\n2. Learn the formulas and their derivations\n3. Practice numerical problems related to this topic\n4. Review past paper questions on this topic\n\nWould you like me to explain any specific part in more detail?",
};

interface Message {
    role: 'user' | 'ai';
    text: string;
}

interface ChatSession {
    id: number;
    title: string;
    messages: Message[];
    timestamp: string;
}

export default function AiChat() {
    const { auth } = usePage<{ auth: { user: User } }>().props;
    const user = auth.user;

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

    // Save current messages to session
    const saveCurrentSession = useCallback((msgs: Message[]) => {
        if (msgs.length === 0) return;
        const title = msgs[0].text.slice(0, 40) + (msgs[0].text.length > 40 ? '...' : '');
        if (activeSessionId !== null) {
            setSessions(prev => prev.map(s => s.id === activeSessionId ? { ...s, messages: msgs, title } : s));
        } else {
            const newId = Date.now();
            setSessions(prev => [{ id: newId, title, messages: msgs, timestamp: new Date().toLocaleDateString() }, ...prev]);
            setActiveSessionId(newId);
        }
    }, [activeSessionId]);

    const sendMessage = useCallback((text: string) => {
        if (!text.trim() || loading) return;
        const userMsg: Message = { role: 'user', text: text.trim() };
        const newMessages = [...messages, userMsg];
        setMessages(newMessages);
        setInput('');
        setLoading(true);
        const lower = text.trim().toLowerCase();
        const response = aiResponses[lower] || aiResponses.default;
        setTimeout(() => {
            const aiMsg: Message = { role: 'ai', text: response };
            const updated = [...newMessages, aiMsg];
            setMessages(updated);
            setLoading(false);
            speakText(response);
            saveCurrentSession(updated);
        }, 1200);
    }, [loading, speakText, messages, saveCurrentSession]);

    const startNewChat = () => {
        setMessages([]);
        setActiveSessionId(null);
        setSidebarOpen(false);
    };

    const loadSession = (session: ChatSession) => {
        setMessages(session.messages);
        setActiveSessionId(session.id);
        setSidebarOpen(false);
    };

    const deleteSession = (id: number) => {
        setSessions(prev => prev.filter(s => s.id !== id));
        if (activeSessionId === id) {
            setMessages([]);
            setActiveSessionId(null);
        }
    };

    const hasSpeechRecognition = typeof window !== 'undefined' && !!(window.SpeechRecognition || window.webkitSpeechRecognition);

    const subjectInfo = user?.subject ? `${user.subject} — Class ${user.classLevel}` : null;

    return (
        <>
            <Head title="AI Chat" />
            <div className="flex h-full overflow-hidden bg-[#F8FAFC] dark:bg-gray-900">
                {/* History Sidebar */}
                {sidebarOpen && <div className="md:hidden fixed inset-0 bg-black/40 backdrop-blur-sm z-30" onClick={() => setSidebarOpen(false)} />}
                <aside className={`fixed md:relative top-0 left-0 h-full w-72 bg-white dark:bg-gray-800 border-r border-gray-100 dark:border-gray-700 z-30 flex flex-col transition-transform duration-300 ${sidebarOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}`}>
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
                                        <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">{s.timestamp}</p>
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
                            <div className="flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400">
                                <i className="fa-solid fa-book-open" />
                                {subjectInfo}
                            </div>
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
                            <button
                                onClick={() => { setVoiceEnabled(!voiceEnabled); if (isSpeaking) stopSpeaking(); }}
                                className={`flex items-center gap-2 px-3 py-2 rounded-xl text-xs font-semibold transition-all duration-200 ${voiceEnabled ? 'bg-[#2563EB] text-white shadow-md' : 'bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600'}`}
                            >
                                <i className={`fa-solid ${voiceEnabled ? 'fa-volume-high' : 'fa-volume-xmark'}`} />
                                {voiceEnabled ? 'Voice On' : 'Voice Off'}
                            </button>
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
                                        {msg.role === 'ai' && (
                                            <div className="w-8 h-8 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-full flex items-center justify-center mr-2 mt-1 flex-shrink-0">
                                                <LogoES className="w-4 h-4" />
                                            </div>
                                        )}
                                        <div className={`max-w-[75%] text-sm leading-relaxed ${msg.role === 'user' ? 'bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white rounded-2xl rounded-br-md shadow-md shadow-blue-100 dark:shadow-blue-900/20 px-4 py-3' : ''}`}>
                                            {msg.role === 'ai' ? (
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
