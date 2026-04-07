import { useState, useRef, useEffect } from "react";

function AdminHeader({ onLogout, onNavigate, user, darkMode, toggleDark }) {
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
    <header className="fixed top-0 left-0 right-0 h-16 bg-gradient-to-r from-[#1E1E2E] via-[#2D1B69] to-[#1E1E2E] text-white z-50 shadow-lg">
      <div className="flex items-center justify-between h-full px-6 pl-14 md:pl-6">
        <div className="flex items-center gap-3 cursor-pointer" onClick={() => onNavigate("admin-dashboard")}>
          <div className="w-9 h-9 bg-purple-500/20 backdrop-blur-sm rounded-xl flex items-center justify-center">
            <i className="fa-solid fa-shield-halved text-purple-300" />
          </div>
          <div>
            <h1 className="text-lg font-bold tracking-tight">Admin Panel</h1>
            <p className="text-[10px] text-purple-300 -mt-0.5">Eternal Sunshine</p>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <button onClick={() => onNavigate("dashboard")} className="bg-white/10 hover:bg-white/20 px-3 py-2 rounded-xl transition text-xs font-medium flex items-center gap-2" title="Go to Student Panel">
            <i className="fa-solid fa-arrow-right-from-bracket" />
            <span className="hidden sm:inline">Student Panel</span>
          </button>
          <button onClick={toggleDark} className="bg-white/10 hover:bg-white/20 p-2 rounded-xl transition">
            <i className={`${darkMode ? "fa-solid fa-sun text-yellow-300" : "fa-solid fa-moon text-purple-200"} text-base`} />
          </button>
          <div className="relative" ref={menuRef}>
            <button onClick={() => setOpen(!open)} className="flex items-center gap-2 bg-white/10 hover:bg-white/20 pl-1.5 pr-2.5 py-1.5 rounded-xl transition">
              <div className="w-8 h-8 bg-gradient-to-br from-purple-400 to-pink-500 rounded-full flex items-center justify-center text-sm font-bold text-white">
                {user?.name?.charAt(0) || "A"}
              </div>
              <i className={`fa-solid fa-chevron-down text-xs text-white/70 transition-transform ${open ? "rotate-180" : ""}`} />
            </button>
            {open && (
              <div className="absolute right-0 mt-2 w-56 bg-white dark:bg-gray-800 rounded-xl shadow-xl border border-gray-100 dark:border-gray-700 overflow-hidden py-1 z-50">
                <div className="px-4 py-3 border-b border-gray-100 dark:border-gray-700">
                  <p className="text-sm font-semibold text-gray-800 dark:text-white">{user?.name || "Admin"}</p>
                  <p className="text-xs text-gray-400 mt-0.5">{user?.email || ""}</p>
                  <span className="text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 px-2 py-0.5 rounded-full font-semibold mt-1 inline-block">Admin</span>
                </div>
                <button onClick={() => { onNavigate("dashboard"); setOpen(false); }} className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-700 transition">
                  <i className="fa-solid fa-house w-4 text-center text-gray-400" /> Student Panel
                </button>
                <button onClick={() => { onLogout(); setOpen(false); }} className="w-full flex items-center gap-3 px-4 py-2.5 text-sm text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20 transition">
                  <i className="fa-solid fa-right-from-bracket w-4 text-center" /> Logout
                </button>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
}

export default AdminHeader;
