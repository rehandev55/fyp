import { useState, useRef, useEffect } from "react";
import Logo from "../components/Logo";

const aiResponses = {
  explain: "Let me explain this concept in detail:\n\nThe concept works by breaking down complex topics into simpler parts. In physics, for example, Newton's laws describe the relationship between a body and the forces acting upon it.\n\n1. First Law: An object at rest stays at rest, and an object in motion stays in motion unless acted upon by an external force.\n2. Second Law: Force = Mass x Acceleration (F = ma)\n3. Third Law: For every action, there is an equal and opposite reaction.\n\nThese laws form the foundation of classical mechanics.",
  simplify: "Here's a simpler way to understand it:\n\nThink of it like pushing a shopping cart. The harder you push (more force), the faster it goes (more acceleration). A heavier cart needs more push. And when you push the cart, the cart pushes back on your hands!\n\nThat's basically Newton's three laws in everyday life.",
  example: "Here's a practical example:\n\nImagine you're playing cricket:\n\n• First Law: The ball stays still on the ground until the bowler picks it up and throws it.\n• Second Law: The harder the batsman hits (force), the farther the ball goes (acceleration). A heavier ball needs a harder hit.\n• Third Law: When the bat hits the ball, the ball also pushes back on the bat (that's why you feel the impact in your hands).",
  default: "That's a great question! Let me think about this...\n\nBased on your syllabus, this topic is important for board exams. The key points to remember are:\n\n1. Understand the core concept and its definition\n2. Learn the formulas and their derivations\n3. Practice numerical problems related to this topic\n4. Review past paper questions on this topic\n\nWould you like me to explain any specific part in more detail?",
};

function AIChat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [isListening, setIsListening] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [voiceEnabled, setVoiceEnabled] = useState(false);
  const endRef = useRef(null);
  const recognitionRef = useRef(null);

  useEffect(() => { endRef.current?.scrollIntoView({ behavior: "smooth" }); }, [messages]);

  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
      const recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = false;
      recognition.lang = "en-US";
      recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        if (transcript.trim()) sendMessage(transcript);
        setIsListening(false);
      };
      recognition.onerror = () => setIsListening(false);
      recognition.onend = () => setIsListening(false);
      recognitionRef.current = recognition;
    }
  }, []);

  const speakText = (text) => {
    if (!voiceEnabled) return;
    window.speechSynthesis.cancel();
    const clean = text.replace(/[•\n]/g, ". ").replace(/\d+\.\s/g, "");
    const utterance = new SpeechSynthesisUtterance(clean);
    utterance.rate = 0.95;
    utterance.pitch = 1;
    utterance.onstart = () => setIsSpeaking(true);
    utterance.onend = () => setIsSpeaking(false);
    utterance.onerror = () => setIsSpeaking(false);
    window.speechSynthesis.speak(utterance);
  };

  const stopSpeaking = () => { window.speechSynthesis.cancel(); setIsSpeaking(false); };

  const toggleListening = () => {
    if (!recognitionRef.current) return;
    if (isListening) { recognitionRef.current.stop(); setIsListening(false); }
    else { recognitionRef.current.start(); setIsListening(true); }
  };

  const sendMessage = (text) => {
    if (!text.trim() || loading) return;
    setMessages((prev) => [...prev, { role: "user", text: text.trim() }]);
    setInput("");
    setLoading(true);
    const lower = text.trim().toLowerCase();
    let response = aiResponses[lower] || aiResponses.default;
    setTimeout(() => {
      setMessages((prev) => [...prev, { role: "ai", text: response }]);
      setLoading(false);
      speakText(response);
    }, 1200);
  };

  const hasSpeechRecognition = !!(window.SpeechRecognition || window.webkitSpeechRecognition);

  return (
    <div className="flex flex-col h-full overflow-hidden bg-[#F8FAFC] dark:bg-gray-900">
      <div className="px-6 py-4 bg-white dark:bg-gray-800 border-b border-gray-100 dark:border-gray-700 flex-shrink-0">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-xl flex items-center justify-center shadow-md shadow-blue-100 dark:shadow-blue-900/30">
              <Logo className="w-6 h-6" />
            </div>
            <div>
              <h2 className="font-bold text-gray-800 dark:text-white">AI Learning Assistant</h2>
              <p className="text-xs text-emerald-500 flex items-center gap-1"><span className="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-pulse" />Online</p>
            </div>
          </div>
          <button
            onClick={() => { setVoiceEnabled(!voiceEnabled); if (isSpeaking) stopSpeaking(); }}
            className={`flex items-center gap-2 px-3 py-2 rounded-xl text-xs font-semibold transition-all duration-200 ${voiceEnabled ? "bg-[#2563EB] text-white shadow-md" : "bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600"}`}
          >
            <i className={`fa-solid ${voiceEnabled ? "fa-volume-high" : "fa-volume-xmark"}`} />
            {voiceEnabled ? "Voice On" : "Voice Off"}
          </button>
        </div>
      </div>

      <div className="flex-1 min-h-0 overflow-y-auto px-4 md:px-6 py-4">
        {messages.length === 0 ? (
          <div className="flex items-center justify-center h-full">
            <div className="text-center">
              <div className="w-20 h-20 bg-gradient-to-br from-blue-100 to-indigo-100 dark:from-blue-900/30 dark:to-indigo-900/30 rounded-full flex items-center justify-center mx-auto mb-5">
                <Logo className="w-10 h-10" />
              </div>
              <h3 className="text-lg font-semibold text-gray-700 dark:text-gray-200 mb-2">How can I help you today?</h3>
              <p className="text-sm text-gray-400 dark:text-gray-500 max-w-sm mx-auto mb-8">Ask me anything about your syllabus — Physics, Chemistry, Biology, Maths, or English.</p>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 max-w-md mx-auto">
                {["Explain Newton's Laws", "What is photosynthesis?", "Solve: 2x + 5 = 15", "Define atomic number"].map((q) => (
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
              <div key={i} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
                {msg.role === "ai" && (
                  <div className="w-8 h-8 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-full flex items-center justify-center mr-2 mt-1 flex-shrink-0">
                    <Logo className="w-4 h-4" />
                  </div>
                )}
                <div className={`max-w-[75%] text-sm leading-relaxed ${msg.role === "user" ? "bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white rounded-2xl rounded-br-md shadow-md shadow-blue-100 dark:shadow-blue-900/20 px-4 py-3" : ""}`}>
                  {msg.role === "ai" ? (
                    <div className="bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-200 rounded-2xl rounded-bl-md shadow-sm border border-gray-100 dark:border-gray-700 overflow-hidden">
                      <div className="px-4 py-3 whitespace-pre-wrap">{msg.text}</div>
                      {voiceEnabled && (
                        <div className="px-4 py-2 border-t border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-gray-700/50">
                          <button onClick={() => isSpeaking ? stopSpeaking() : speakText(msg.text)} className="flex items-center gap-1.5 text-xs text-gray-500 dark:text-gray-400 hover:text-[#2563EB] transition">
                            <i className={`fa-solid ${isSpeaking ? "fa-stop" : "fa-volume-high"} text-[10px]`} />
                            {isSpeaking ? "Stop" : "Listen"}
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
                <div className="w-8 h-8 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-full flex items-center justify-center flex-shrink-0"><Logo className="w-4 h-4" /></div>
                <div className="bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 rounded-2xl rounded-bl-md shadow-sm px-4 py-3">
                  <div className="flex gap-1.5">
                    <span className="w-2 h-2 bg-[#2563EB] rounded-full animate-bounce" style={{ animationDelay: "0ms" }} />
                    <span className="w-2 h-2 bg-[#2563EB] rounded-full animate-bounce" style={{ animationDelay: "150ms" }} />
                    <span className="w-2 h-2 bg-[#2563EB] rounded-full animate-bounce" style={{ animationDelay: "300ms" }} />
                  </div>
                </div>
              </div>
            )}
            <div ref={endRef} />
          </div>
        )}
      </div>

      <div className="p-4 bg-white dark:bg-gray-800 border-t border-gray-100 dark:border-gray-700 flex-shrink-0">
        <div className="flex gap-2 mb-3">
          {["Explain", "Simplify", "Example"].map((action) => (
            <button key={action} onClick={() => sendMessage(action)} disabled={loading} className="px-4 py-2 bg-blue-50 dark:bg-blue-900/30 text-[#2563EB] rounded-xl text-xs font-semibold hover:bg-blue-100 dark:hover:bg-blue-900/50 disabled:opacity-50 transition">
              {action}
            </button>
          ))}
        </div>
        <form onSubmit={(e) => { e.preventDefault(); sendMessage(input); }} className="flex gap-3">
          <input type="text" value={input} onChange={(e) => setInput(e.target.value)} placeholder={isListening ? "Listening..." : "Ask any question..."} className={`flex-1 border rounded-xl px-5 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white ${isListening ? "border-red-400 ring-2 ring-red-200 dark:ring-red-800 animate-pulse" : "border-gray-200 dark:border-gray-600"}`} />
          {hasSpeechRecognition && (
            <button type="button" onClick={toggleListening} className={`px-4 py-3 rounded-xl transition-all duration-200 text-sm font-semibold ${isListening ? "bg-red-500 text-white shadow-lg animate-pulse" : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600"}`} title={isListening ? "Stop listening" : "Voice input"}>
              <i className="fa-solid fa-microphone text-lg" />
            </button>
          )}
          <button type="submit" disabled={!input.trim() || loading} className="bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white px-6 py-3 rounded-xl hover:shadow-lg disabled:opacity-40 disabled:shadow-none transition-all duration-200 text-sm font-semibold flex items-center gap-2">
            <i className="fa-solid fa-paper-plane" />
            Send
          </button>
        </form>
      </div>
    </div>
  );
}

export default AIChat;
