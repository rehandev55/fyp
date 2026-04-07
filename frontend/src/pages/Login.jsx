import { useState } from "react";
import Logo from "../components/Logo";

function Login({ onNavigate, onLogin, darkMode, toggleDark }) {
  const [form, setForm] = useState({ email: "", password: "" });
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!form.email || !form.password) { setError("Please fill in all fields."); return; }
    onLogin();
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#1E3A8A] via-[#2563EB] to-[#7C3AED] flex items-center justify-center px-4 relative overflow-hidden">
      <div className="absolute top-20 left-10 w-72 h-72 bg-yellow-300/10 rounded-full blur-3xl" />
      <div className="absolute bottom-20 right-10 w-96 h-96 bg-blue-300/10 rounded-full blur-3xl" />

      <button onClick={toggleDark} className="fixed top-5 right-5 z-50 bg-white/10 hover:bg-white/20 backdrop-blur-sm p-2.5 rounded-xl transition">
        <i className={`${darkMode ? "fa-solid fa-sun text-yellow-300" : "fa-solid fa-moon text-white/70"} text-base`} />
      </button>

      <div className="bg-white dark:bg-gray-800 rounded-3xl shadow-2xl p-8 md:p-10 w-full max-w-md relative">
        <div className="text-center mb-8">
          <div className="w-14 h-14 bg-gradient-to-br from-[#2563EB] to-[#7C3AED] rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg shadow-blue-200 dark:shadow-blue-900/30">
            <Logo className="w-8 h-8" />
          </div>
          <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Welcome Back</h2>
          <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">Sign in to your account</p>
        </div>

        {error && <div className="bg-red-50 dark:bg-red-900/30 border border-red-200 dark:border-red-800 text-red-600 dark:text-red-400 text-sm px-4 py-3 rounded-xl mb-5 flex items-center gap-2"><i className="fa-solid fa-circle-exclamation" />{error}</div>}

        <form onSubmit={handleSubmit} className="space-y-5">
          <div>
            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Email Address</label>
            <input type="email" value={form.email} onChange={(e) => { setForm({ ...form, email: e.target.value }); setError(""); }} className="w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white hover:bg-white dark:hover:bg-gray-600 transition" placeholder="you@example.com" />
          </div>
          <div>
            <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Password</label>
            <input type="password" value={form.password} onChange={(e) => { setForm({ ...form, password: e.target.value }); setError(""); }} className="w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white hover:bg-white dark:hover:bg-gray-600 transition" placeholder="Enter your password" />
          </div>
          <button type="submit" className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg hover:shadow-blue-200 dark:hover:shadow-blue-900/30 transition-all duration-200 text-sm font-semibold">Sign In</button>
        </form>

        <div className="relative my-7">
          <div className="absolute inset-0 flex items-center"><div className="w-full border-t border-gray-200 dark:border-gray-600"></div></div>
          <div className="relative flex justify-center"><span className="bg-white dark:bg-gray-800 px-4 text-sm text-gray-400">or continue with</span></div>
        </div>

        <button className="w-full border-2 border-gray-200 dark:border-gray-600 py-3 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition text-sm font-semibold text-gray-700 dark:text-gray-200 flex items-center justify-center gap-3">
          <i className="fa-brands fa-google text-lg" />
          Continue with Google
        </button>

        <p className="text-center text-sm text-gray-500 dark:text-gray-400 mt-7">
          Don&apos;t have an account?{" "}
          <button onClick={() => onNavigate("register")} className="text-[#2563EB] hover:underline font-semibold">Create Account</button>
        </p>
      </div>
    </div>
  );
}

export default Login;
