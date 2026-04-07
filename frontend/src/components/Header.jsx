import { useState, useRef, useEffect } from "react";
import Logo from "./Logo";

function Header({ onLogout, onNavigate, user, darkMode, toggleDark, isAdmin }) {
  const [open, setOpen] = useState(false);
  const menuRef = useRef(null);

  useEffect(() => {
    const handleClick = (e) => {
      if (menuRef.current && !menuRef.current.contains(e.target)) setOpen(false);
    };
    document.addEventListener("mousedown", handleClick);
    return () => document.removeEventListener("mousedown", handleClick);
  }, []);

  return (
    <header className="fixed top-0 left-0 right-0 h-16 bg-gradient-to-r from-[#1E3A8A] via-[#2563EB] to-[#3B82F6] text-white z-50 shadow-lg">
      <div className="flex items-center justify-between h-full px-6 pl-14 md:pl-6">
        <div className="flex items-center gap-3 cursor-pointer" onClick={() => onNavigate("dashboard")}>
          <div className="w-9 h-9 bg-white/20 backdrop-blur-sm rounded-xl flex items-center justify-center">
            <Logo className="w-6 h-6" />
          </div>
          <h1 className="text-xl font-bold tracking-tight hover:text-yellow-200 transition">
            Eternal Sunshine
          </h1>
        </div>
        <div className="flex items-center gap-2">
          {isAdmin && (
            <button onClick={() => onNavigate("admin-dashboard")} className="bg-purple-500/20 hover:bg-purple-500/30 px-3 py-2 rounded-xl transition text-xs font-medium flex items-center gap-2" title="Admin Panel">
              <i className="fa-solid fa-shield-halved text-purple-200" />
              <span className="hidden sm:inline">Admin</span>
            </button>
          )}
          <button onClick={toggleDark} className="bg-white/10 hover:bg-white/20 p-2 rounded-xl transition" title={darkMode ? "Light Mode" : "Dark Mode"}>
            <i className={`${darkMode ? "fa-solid fa-sun text-yellow-300" : "fa-solid fa-moon text-blue-100"} text-base`} />
          </button>

          {/* Compact profile dropdown */}
          <div className="relative" ref={menuRef}>
            <button onClick={() => setOpen(!open)} className="flex items-center gap-2 bg-white/10 hover:bg-white/20 pl-1.5 pr-2.5 py-1.5 rounded-xl transition">
              <div className="w-8 h-8 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-full flex items-center justify-center text-sm font-bold text-white">
                {user?.name?.charAt(0) || "S"}
              </div>
              <i className={`fa-solid fa-chevron-down text-xs text-white/70 transition-transform ${open ? "rotate-180" : ""}`} />
            </button>

            {open && (
              <div className="absolute right-0 mt-2 w-56 bg-white dark:bg-gray-800 rounded-xl shadow-xl border border-gray-100 dark:border-gray-700 overflow-hidden py-1 z-50">
                <div className="px-4 py-3 border-b border-gray-100 dark:border-gray-700">
                  <p className="text-sm font-semibold text-gray-800 dark:text-white">{user?.name || "Student"}</p>
                  <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">{user?.email || ""}</p>
                </div>
                <button
                  onClick={() => { onNavigate("profile"); setOpen(false); }}
                  className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-700 transition"
                >
                  <i className="fa-solid fa-user text-gray-400 w-4 text-center" />
                  Profile
                </button>
                <button
                  onClick={() => { onLogout(); setOpen(false); }}
                  className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20 transition"
                >
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

export default Header;
