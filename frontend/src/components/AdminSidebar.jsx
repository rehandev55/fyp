import { useState } from "react";

const adminItems = [
  { key: "admin-dashboard", label: "Dashboard", icon: "fa-solid fa-gauge-high" },
  { key: "admin-users", label: "User Management", icon: "fa-solid fa-users-gear" },
  { key: "admin-content", label: "Content Manager", icon: "fa-solid fa-cloud-arrow-up" },
];

function AdminSidebar({ currentPage, onNavigate, onLogout }) {
  const [open, setOpen] = useState(false);

  return (
    <>
      <button onClick={() => setOpen(!open)} className="md:hidden fixed top-[1.1rem] left-4 z-[60] text-white p-1 rounded-lg">
        <i className={`fa-solid ${open ? "fa-xmark" : "fa-bars"} text-xl`} />
      </button>

      {open && <div className="md:hidden fixed inset-0 bg-black/40 backdrop-blur-sm z-40" onClick={() => setOpen(false)} />}

      <aside className={`fixed top-16 left-0 h-[calc(100vh-4rem)] w-64 bg-[#1E1E2E] z-40 shadow-xl border-r border-gray-800 transition-all duration-300 ${open ? "translate-x-0" : "-translate-x-full"} md:translate-x-0`}>
        <nav className="flex flex-col h-full py-4 overflow-y-auto">
          <div className="px-5 mb-4">
            <div className="bg-purple-500/10 border border-purple-500/20 rounded-xl p-3">
              <p className="text-xs font-bold text-purple-300 uppercase tracking-wider flex items-center gap-2">
                <i className="fa-solid fa-shield-halved text-[10px]" />
                Administration
              </p>
            </div>
          </div>

          <div className="flex-1 space-y-1 px-4">
            {adminItems.map((item) => (
              <button
                key={item.key}
                onClick={() => { onNavigate(item.key); setOpen(false); }}
                className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200
                  ${currentPage === item.key
                    ? "bg-gradient-to-r from-[#7C3AED] to-[#9333EA] text-white shadow-md shadow-purple-900/30"
                    : "text-gray-400 hover:bg-white/5 hover:text-purple-300"}`}
              >
                <i className={`${item.icon} w-5 text-center`} />
                {item.label}
              </button>
            ))}
          </div>

          <div className="px-4 space-y-1 mb-2">
            <button onClick={() => { onNavigate("dashboard"); setOpen(false); }} className="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-gray-400 hover:bg-white/5 hover:text-blue-300 transition">
              <i className="fa-solid fa-arrow-right-from-bracket w-5 text-center" />
              Student Panel
            </button>
          </div>

          <div className="px-4 pt-4 border-t border-gray-800 mx-4">
            <button onClick={onLogout} className="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-red-400 hover:bg-red-900/20 transition">
              <i className="fa-solid fa-right-from-bracket w-5 text-center" />
              Logout
            </button>
          </div>
        </nav>
      </aside>
    </>
  );
}

export default AdminSidebar;
