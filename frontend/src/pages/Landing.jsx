import Logo from "../components/Logo";

function Landing({ onNavigate, darkMode, toggleDark }) {
  const features = [
    { title: "AI Chat Learning", desc: "Get instant AI-powered explanations for any topic in your syllabus. Ask questions and learn interactively.", icon: "fa-solid fa-robot", color: "from-blue-500 to-indigo-600", bg: "bg-blue-50 dark:bg-blue-900/30" },
    { title: "Practice Questions", desc: "Test your knowledge with MCQs, short and long questions aligned to your board syllabus.", icon: "fa-solid fa-clipboard-check", color: "from-emerald-500 to-teal-600", bg: "bg-emerald-50 dark:bg-emerald-900/30" },
    { title: "Voice-Enabled AI", desc: "Speak your questions and hear answers read aloud. Learn naturally with voice interaction.", icon: "fa-solid fa-microphone", color: "from-purple-500 to-pink-600", bg: "bg-purple-50 dark:bg-purple-900/30" },
    { title: "Downloadable Resources", desc: "Access past papers, key books, and notes for your board exams anytime, anywhere.", icon: "fa-solid fa-book-open", color: "from-orange-500 to-amber-600", bg: "bg-orange-50 dark:bg-orange-900/30" },
    { title: "Progress Tracking", desc: "Monitor your learning journey with detailed stats and subject-wise performance insights.", icon: "fa-solid fa-chart-line", color: "from-cyan-500 to-blue-600", bg: "bg-cyan-50 dark:bg-cyan-900/30" },
    { title: "Chapter-wise Practice", desc: "Select specific chapters or the whole book to practice. Focus on your weak areas.", icon: "fa-solid fa-list-check", color: "from-rose-500 to-red-600", bg: "bg-rose-50 dark:bg-rose-900/30" },
  ];

  return (
    <div className="min-h-screen bg-[#F8FAFC] dark:bg-gray-900 transition-colors">
      {/* Navbar */}
      <nav className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-md border-b border-gray-100 dark:border-gray-700 sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Logo className="w-8 h-8" />
            <span className="text-lg font-bold text-gray-800 dark:text-white">Eternal Sunshine</span>
          </div>
          <div className="flex items-center gap-3">
            <button onClick={toggleDark} className="p-2 rounded-xl hover:bg-gray-100 dark:hover:bg-gray-700 transition" title={darkMode ? "Light Mode" : "Dark Mode"}>
              <i className={`${darkMode ? "fa-solid fa-sun text-yellow-400" : "fa-solid fa-moon text-gray-500"} text-base`} />
            </button>
            <button onClick={() => onNavigate("login")} className="text-sm text-gray-600 dark:text-gray-300 hover:text-[#2563EB] font-medium transition px-4 py-2">Login</button>
            <button onClick={() => onNavigate("register")} className="text-sm bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white px-5 py-2 rounded-xl font-medium hover:shadow-lg hover:shadow-blue-200 dark:hover:shadow-blue-900/30 transition-all duration-200">Get Started</button>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-[#1E3A8A] via-[#2563EB] to-[#7C3AED]" />
        <div className="absolute inset-0">
          <div className="absolute top-20 left-10 w-72 h-72 bg-yellow-300/10 rounded-full blur-3xl animate-pulse" style={{ animationDuration: "4s" }} />
          <div className="absolute bottom-10 right-10 w-96 h-96 bg-blue-300/10 rounded-full blur-3xl animate-pulse" style={{ animationDuration: "6s" }} />
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-purple-300/5 rounded-full blur-3xl" />
        </div>
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute top-32 left-[15%] w-3 h-3 bg-yellow-300/30 rounded-full animate-bounce" style={{ animationDuration: "3s" }} />
          <div className="absolute top-48 right-[20%] w-2 h-2 bg-blue-300/40 rounded-full animate-bounce" style={{ animationDuration: "2.5s", animationDelay: "0.5s" }} />
          <div className="absolute bottom-32 left-[25%] w-4 h-4 bg-purple-300/20 rounded-full animate-bounce" style={{ animationDuration: "3.5s", animationDelay: "1s" }} />
        </div>
        <div className="relative max-w-6xl mx-auto px-6 py-24 md:py-36 text-center text-white">
          <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm px-5 py-2.5 rounded-full mb-8 text-sm border border-white/10">
            <Logo className="w-5 h-5" />
            <span>AI-Powered Education Platform</span>
            <span className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse" />
          </div>
          <h1 className="text-4xl md:text-6xl lg:text-7xl font-extrabold mb-6 tracking-tight leading-tight">
            Eternal <span className="text-transparent bg-clip-text bg-gradient-to-r from-yellow-200 via-yellow-300 to-amber-400">Sunshine</span>
          </h1>
          <p className="text-lg md:text-xl text-blue-100 mb-12 max-w-2xl mx-auto leading-relaxed">AI-Powered Learning Assistant for Pakistani Students. Prepare for board exams with intelligent tools designed for your syllabus.</p>
          <div className="flex gap-4 justify-center flex-wrap">
            <button onClick={() => onNavigate("register")} className="bg-white text-[#2563EB] px-8 py-4 rounded-2xl font-semibold hover:shadow-xl hover:shadow-blue-900/20 hover:-translate-y-0.5 transition-all duration-200 text-sm group flex items-center gap-2">
              Get Started Free
              <i className="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform" />
            </button>
            <button onClick={() => onNavigate("login")} className="border-2 border-white/30 backdrop-blur-sm px-8 py-4 rounded-2xl font-semibold hover:bg-white/10 hover:-translate-y-0.5 transition-all duration-200 text-sm">Sign In</button>
          </div>
          <div className="grid grid-cols-3 gap-8 max-w-lg mx-auto mt-20">
            {[{ num: "2", label: "Board Syllabi" }, { num: "5+", label: "Subjects" }, { num: "100%", label: "Free Access" }].map((s) => (
              <div key={s.label} className="bg-white/5 backdrop-blur-sm rounded-2xl p-4 border border-white/10">
                <p className="text-2xl md:text-3xl font-bold text-yellow-300">{s.num}</p>
                <p className="text-xs text-blue-200 mt-1">{s.label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="max-w-6xl mx-auto px-6 py-24">
        <div className="text-center mb-16">
          <span className="text-sm font-semibold text-[#2563EB] bg-blue-50 dark:bg-blue-900/30 px-4 py-1.5 rounded-full">Features</span>
          <h2 className="text-3xl md:text-4xl font-bold text-gray-800 dark:text-white mt-5">Everything You Need to Excel</h2>
          <p className="text-gray-500 dark:text-gray-400 mt-3 max-w-xl mx-auto">Powerful tools designed specifically for Pakistani board exam preparation</p>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((f, i) => (
            <div key={i} className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-7 hover:shadow-xl hover:-translate-y-2 transition-all duration-300 group relative overflow-hidden">
              <div className={`absolute top-0 right-0 w-32 h-32 bg-gradient-to-br ${f.color} opacity-5 rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:opacity-10 transition-opacity duration-300`} />
              <div className={`w-14 h-14 bg-gradient-to-br ${f.color} rounded-2xl flex items-center justify-center mb-5 shadow-lg group-hover:scale-110 group-hover:shadow-xl transition-all duration-300`}>
                <i className={`${f.icon} text-white text-xl`} />
              </div>
              <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-2 relative">{f.title}</h3>
              <p className="text-sm text-gray-500 dark:text-gray-400 leading-relaxed relative">{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Boards */}
      <section className="bg-white dark:bg-gray-800 py-24 border-y border-gray-100 dark:border-gray-700">
        <div className="max-w-6xl mx-auto px-6 text-center">
          <span className="text-sm font-semibold text-[#2563EB] bg-blue-50 dark:bg-blue-900/30 px-4 py-1.5 rounded-full">Supported Boards</span>
          <h2 className="text-3xl md:text-4xl font-bold text-gray-800 dark:text-white mt-5 mb-12">Aligned With Your Board Syllabus</h2>
          <div className="flex justify-center gap-8 flex-wrap">
            {[{ name: "Federal Board", desc: "FBISE Islamabad", classes: "Class 9 - 12" }, { name: "AJK Board", desc: "Azad Jammu & Kashmir", classes: "Class 9 - 12" }].map((board) => (
              <div key={board.name} className="bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20 border border-blue-100 dark:border-blue-800 px-12 py-8 rounded-2xl hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group">
                <div className="w-14 h-14 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg group-hover:scale-110 transition-transform duration-300">
                  <i className="fa-solid fa-graduation-cap text-white text-xl" />
                </div>
                <h3 className="font-bold text-gray-800 dark:text-white text-lg">{board.name}</h3>
                <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">{board.desc}</p>
                <p className="text-xs text-[#2563EB] font-semibold mt-2">{board.classes}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="max-w-6xl mx-auto px-6 py-24">
        <div className="text-center mb-16">
          <span className="text-sm font-semibold text-emerald-600 bg-emerald-50 dark:bg-emerald-900/30 px-4 py-1.5 rounded-full">How It Works</span>
          <h2 className="text-3xl md:text-4xl font-bold text-gray-800 dark:text-white mt-5">Start Learning in 3 Steps</h2>
        </div>
        <div className="grid md:grid-cols-3 gap-8">
          {[
            { step: "01", title: "Create Account", desc: "Sign up for free in seconds. No credit card required.", icon: "fa-solid fa-user-plus" },
            { step: "02", title: "Select Your Subject", desc: "Choose your board, class, and subject. We'll personalize everything for you.", icon: "fa-solid fa-book-open" },
            { step: "03", title: "Start Learning", desc: "Ask AI questions, take quizzes, download resources. Your exam prep starts now!", icon: "fa-solid fa-bolt" },
          ].map((s, i) => (
            <div key={i} className="text-center group">
              <div className="relative inline-block mb-6">
                <div className="w-20 h-20 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-2xl flex items-center justify-center mx-auto shadow-lg group-hover:scale-110 group-hover:shadow-xl transition-all duration-300 rotate-3 group-hover:rotate-0">
                  <i className={`${s.icon} text-white text-2xl`} />
                </div>
                <span className="absolute -top-2 -right-2 w-8 h-8 bg-yellow-400 text-gray-900 rounded-full flex items-center justify-center text-xs font-bold shadow-md">{s.step}</span>
              </div>
              <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-2">{s.title}</h3>
              <p className="text-sm text-gray-500 dark:text-gray-400 leading-relaxed max-w-xs mx-auto">{s.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="max-w-6xl mx-auto px-6 py-20 text-center">
        <div className="bg-gradient-to-br from-[#1E3A8A] via-[#2563EB] to-[#7C3AED] rounded-3xl p-12 md:p-16 text-white relative overflow-hidden">
          <div className="absolute top-0 right-0 w-64 h-64 bg-yellow-300/10 rounded-full blur-3xl" />
          <div className="absolute bottom-0 left-0 w-48 h-48 bg-blue-300/10 rounded-full blur-3xl" />
          <h2 className="text-3xl md:text-4xl font-bold mb-4 relative">Ready to Start Learning?</h2>
          <p className="text-blue-200 mb-8 max-w-md mx-auto relative">Join Eternal Sunshine and transform your exam preparation with AI-powered tools.</p>
          <button onClick={() => onNavigate("register")} className="bg-white text-[#2563EB] px-8 py-4 rounded-2xl font-semibold hover:shadow-xl hover:-translate-y-0.5 transition-all duration-200 text-sm relative">Create Free Account</button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-400 py-12 border-t border-gray-800">
        <div className="max-w-6xl mx-auto px-6">
          <div className="flex flex-col md:flex-row items-center justify-between gap-6">
            <div className="flex items-center gap-2">
              <Logo className="w-7 h-7" />
              <span className="font-semibold text-white">Eternal Sunshine</span>
            </div>
            <div className="flex items-center gap-6 text-sm">
              <button onClick={() => onNavigate("login")} className="hover:text-white transition">Login</button>
              <button onClick={() => onNavigate("register")} className="hover:text-white transition">Register</button>
            </div>
            <p className="text-sm">&copy; 2026 Eternal Sunshine. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default Landing;
