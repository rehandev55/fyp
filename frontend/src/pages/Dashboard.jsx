function Dashboard({ onNavigate, user }) {
  const greeting = () => {
    const h = new Date().getHours();
    if (h < 12) return "Good Morning";
    if (h < 17) return "Good Afternoon";
    return "Good Evening";
  };

  const quickActions = [
    { label: "Ask AI", desc: "Chat with AI tutor", page: "aichat", icon: "fa-solid fa-robot", gradient: "from-blue-500 to-indigo-600" },
    { label: "Start Practice", desc: "Take a quiz", page: "practice", icon: "fa-solid fa-clipboard-check", gradient: "from-emerald-500 to-teal-600" },
    { label: "View Resources", desc: "Download materials", page: "resources", icon: "fa-solid fa-book-open", gradient: "from-purple-500 to-pink-600" },
  ];

  return (
    <div className="space-y-8">
      <div className="bg-gradient-to-r from-[#1E3A8A] via-[#2563EB] to-[#7C3AED] rounded-2xl p-8 md:p-10 text-white relative overflow-hidden">
        <div className="absolute top-0 right-0 w-40 h-40 bg-yellow-300/10 rounded-full blur-3xl" />
        <div className="absolute bottom-0 left-20 w-32 h-32 bg-blue-300/10 rounded-full blur-2xl" />
        <div className="absolute top-10 right-20 w-3 h-3 bg-yellow-300/30 rounded-full animate-bounce" style={{ animationDuration: "3s" }} />
        <div className="relative">
          <p className="text-blue-200 text-sm font-medium mb-1">{greeting()}</p>
          <h2 className="text-2xl md:text-3xl font-bold mb-2">Welcome back, {user?.name || "Student"}</h2>
          <p className="text-blue-200 text-sm max-w-md">Continue your learning journey with Eternal Sunshine.</p>
          {user?.subject && (
            <div className="mt-4 inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm px-4 py-2 rounded-xl text-sm border border-white/10">
              <i className="fa-solid fa-book text-yellow-300 text-xs" />
              {user.subject} — Class {user.classLevel} — {user.board}
            </div>
          )}
        </div>
      </div>

      <div>
        <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-4">Quick Actions</h3>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
          {quickActions.map((a) => (
            <button key={a.label} onClick={() => onNavigate(a.page)} className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 flex items-center gap-4 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group text-left relative overflow-hidden">
              <div className={`absolute top-0 right-0 w-24 h-24 bg-gradient-to-br ${a.gradient} opacity-5 rounded-full blur-2xl -translate-y-8 translate-x-8 group-hover:opacity-10 transition-opacity`} />
              <div className={`w-14 h-14 bg-gradient-to-br ${a.gradient} rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg group-hover:scale-110 transition-transform duration-300`}>
                <i className={`${a.icon} text-white text-xl`} />
              </div>
              <div className="relative">
                <p className="font-semibold text-gray-800 dark:text-white">{a.label}</p>
                <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">{a.desc}</p>
              </div>
            </button>
          ))}
        </div>
      </div>

      <div>
        <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-4">Progress Summary</h3>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-5">
          {[
            { label: "Questions Practiced", value: "24", icon: "fa-solid fa-circle-question", gradient: "from-blue-500 to-indigo-600" },
            { label: "Average Score", value: "78%", icon: "fa-solid fa-chart-column", gradient: "from-emerald-500 to-teal-600" },
            { label: "Weak Subject", value: "Chemistry", icon: "fa-solid fa-triangle-exclamation", gradient: "from-orange-500 to-amber-600" },
          ].map((s) => (
            <div key={s.label} className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 group hover:shadow-lg transition-all duration-300">
              <div className="flex items-center justify-between mb-3">
                <div className={`w-10 h-10 bg-gradient-to-br ${s.gradient} rounded-xl flex items-center justify-center shadow-md group-hover:scale-110 transition-transform duration-300`}>
                  <i className={`${s.icon} text-white text-sm`} />
                </div>
              </div>
              <p className="text-2xl font-bold text-gray-800 dark:text-white">{s.value}</p>
              <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">{s.label}</p>
            </div>
          ))}
        </div>
      </div>

      <div>
        <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-4">Recent Activity</h3>
        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 divide-y divide-gray-50 dark:divide-gray-700">
          {[
            { text: "Asked AI: \"Explain photosynthesis in detail\"", time: "2 hours ago", icon: "fa-solid fa-robot", color: "from-blue-500 to-indigo-600" },
            { text: "Completed Physics MCQ Quiz — Score: 8/10", time: "5 hours ago", icon: "fa-solid fa-circle-check", color: "from-emerald-500 to-teal-600" },
            { text: "Downloaded Math Key Book", time: "1 day ago", icon: "fa-solid fa-download", color: "from-purple-500 to-pink-600" },
          ].map((a, i) => (
            <div key={i} className="flex items-center gap-4 p-5 hover:bg-gray-50 dark:hover:bg-gray-700/50 transition group">
              <div className={`w-10 h-10 bg-gradient-to-br ${a.color} rounded-xl flex items-center justify-center flex-shrink-0 shadow-md group-hover:scale-110 transition-transform duration-300`}>
                <i className={`${a.icon} text-white text-sm`} />
              </div>
              <div className="flex-1 min-w-0"><p className="text-sm font-medium text-gray-700 dark:text-gray-200 truncate">{a.text}</p><p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">{a.time}</p></div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
