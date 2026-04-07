import { useState } from "react";

const menuItems = [
  { key: "dashboard", label: "Dashboard", icon: "fa-solid fa-house" },
  { key: "selection", label: "Select Subject", icon: "fa-solid fa-book-open" },
  { key: "aichat", label: "AI Learning", icon: "fa-solid fa-robot" },
  { key: "practice", label: "Practice Quiz", icon: "fa-solid fa-clipboard-check" },
  { key: "resources", label: "Resources", icon: "fa-solid fa-download" },
  { key: "progress", label: "Progress", icon: "fa-solid fa-chart-line" },
  { key: "about", label: "About Us", icon: "fa-solid fa-circle-info" },
];

function Sidebar({ currentPage, onNavigate, onLogout }) {
  const [open, setOpen] = useState(false);

  return (
    <>
      <button onClick={() => setOpen(!open)} className="md:hidden fixed top-[1.1rem] left-4 z-[60] text-white p-1 rounded-lg">
        <i className={`fa-solid ${open ? "fa-xmark" : "fa-bars"} text-xl`} />
      </button>

      {open && <div className="md:hidden fixed inset-0 bg-black/40 backdrop-blur-sm z-40" onClick={() => setOpen(false)} />}

      <aside className={`fixed top-16 left-0 h-[calc(100vh-4rem)] w-64 bg-white dark:bg-gray-800 z-40 shadow-xl border-r border-gray-100 dark:border-gray-700 transition-all duration-300 ${open ? "translate-x-0" : "-translate-x-full"} md:translate-x-0`}>
        <nav className="flex flex-col h-full py-4 overflow-y-auto">
          <div className="flex-1 space-y-1 px-4">
            {menuItems.map((item) => (
              <button
                key={item.key}
                onClick={() => { onNavigate(item.key); setOpen(false); }}
                className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200
                  ${currentPage === item.key
                    ? "bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white shadow-md shadow-blue-200 dark:shadow-blue-900/30"
                    : "text-gray-600 dark:text-gray-300 hover:bg-blue-50 dark:hover:bg-blue-900/30 hover:text-[#2563EB]"}`}
              >
                <i className={`${item.icon} w-5 text-center`} />
                {item.label}
              </button>
            ))}
          </div>
          <div className="px-4 pt-4 border-t border-gray-100 dark:border-gray-700 mx-4">
            <button onClick={onLogout} className="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20 transition">
              <i className="fa-solid fa-right-from-bracket w-5 text-center" />
              Logout
            </button>
          </div>
        </nav>
      </aside>
    </>
  );
}

export default Sidebar;
