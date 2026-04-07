import { useState, useEffect } from "react";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import AdminHeader from "./components/AdminHeader";
import AdminSidebar from "./components/AdminSidebar";
import Landing from "./pages/Landing";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Selection from "./pages/Selection";
import AIChat from "./pages/AIChat";
import Practice from "./pages/Practice";
import Resources from "./pages/Resources";
import Progress from "./pages/Progress";
import Profile from "./pages/Profile";
import About from "./pages/About";
import AdminDashboard from "./pages/AdminDashboard";
import AdminUsers from "./pages/AdminUsers";
import AdminContent from "./pages/AdminContent";

function getHashPage() {
  const hash = window.location.hash.replace("#/", "").replace("#", "");
  return hash || "landing";
}

function App() {
  const [page, setPage] = useState(getHashPage);
  const [user, setUser] = useState(() => {
    const saved = localStorage.getItem("es_user");
    return saved ? JSON.parse(saved) : null;
  });
  const [darkMode, setDarkMode] = useState(() => localStorage.getItem("es_theme") === "dark");

  useEffect(() => {
    const onHash = () => setPage(getHashPage());
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, []);

  useEffect(() => {
    if (user) localStorage.setItem("es_user", JSON.stringify(user));
    else localStorage.removeItem("es_user");
  }, [user]);

  useEffect(() => {
    document.documentElement.classList.toggle("dark", darkMode);
    localStorage.setItem("es_theme", darkMode ? "dark" : "light");
  }, [darkMode]);

  useEffect(() => {
    if (page === "aichat" && user) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
    return () => { document.body.style.overflow = ""; };
  }, [page, user]);

  const navigate = (p) => { window.location.hash = `#/${p}`; };
  const toggleDark = () => setDarkMode((prev) => !prev);

  const handleLogin = () => {
    setUser({ name: "Munaza", email: "munaza@example.com", classLevel: "10", board: "Federal Board", role: "admin" });
    navigate("dashboard");
  };
  const handleLogout = () => {
    setUser(null);
    localStorage.removeItem("es_user");
    navigate("landing");
  };
  const handleSelection = (selection) => {
    setUser((prev) => ({ ...prev, ...selection }));
    navigate("aichat");
  };

  // Unauthenticated
  if (!user) {
    switch (page) {
      case "login": return <Login onNavigate={navigate} onLogin={handleLogin} darkMode={darkMode} toggleDark={toggleDark} />;
      case "register": return <Register onNavigate={navigate} onLogin={handleLogin} darkMode={darkMode} toggleDark={toggleDark} />;
      default: return <Landing onNavigate={navigate} darkMode={darkMode} toggleDark={toggleDark} />;
    }
  }

  const isAdmin = user?.role === "admin";
  const isAdminPage = page.startsWith("admin-");
  const isChat = page === "aichat";

  // Admin panel (separate layout)
  if (isAdmin && isAdminPage) {
    const renderAdminPage = () => {
      switch (page) {
        case "admin-dashboard": return <AdminDashboard onNavigate={navigate} />;
        case "admin-users": return <AdminUsers onNavigate={navigate} />;
        case "admin-content": return <AdminContent onNavigate={navigate} />;
        default: return <AdminDashboard onNavigate={navigate} />;
      }
    };

    return (
      <div className="bg-[#F0F4F8] dark:bg-gray-900 transition-colors min-h-screen">
        <AdminHeader onLogout={handleLogout} onNavigate={navigate} user={user} darkMode={darkMode} toggleDark={toggleDark} />
        <AdminSidebar currentPage={page} onNavigate={navigate} onLogout={handleLogout} />
        <main className="pt-16 md:pl-64">
          <div className="p-5 md:p-8 max-w-7xl mx-auto">
            {renderAdminPage()}
          </div>
        </main>
      </div>
    );
  }

  // Student panel
  const renderPage = () => {
    switch (page) {
      case "dashboard": return <Dashboard onNavigate={navigate} user={user} />;
      case "selection": return <Selection onSelect={handleSelection} user={user} />;
      case "aichat": return <AIChat />;
      case "practice": return <Practice user={user} onNavigate={navigate} />;
      case "resources": return <Resources user={user} />;
      case "progress": return <Progress />;
      case "profile": return <Profile user={user} setUser={setUser} />;
      case "about": return <About />;
      default: return <Dashboard onNavigate={navigate} user={user} />;
    }
  };

  return (
    <div className={`bg-[#F0F4F8] dark:bg-gray-900 transition-colors ${isChat ? "h-screen overflow-hidden" : "min-h-screen"}`}>
      <Header onLogout={handleLogout} onNavigate={navigate} user={user} darkMode={darkMode} toggleDark={toggleDark} isAdmin={isAdmin} />
      <Sidebar currentPage={page} onNavigate={navigate} onLogout={handleLogout} />
      <main className={`pt-16 md:pl-64 ${isChat ? "h-[calc(100vh)] overflow-hidden" : ""}`}>
        <div className={isChat ? "h-[calc(100vh-4rem)]" : "p-5 md:p-8 max-w-7xl mx-auto"}>
          {renderPage()}
        </div>
      </main>
    </div>
  );
}

export default App;
