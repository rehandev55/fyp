import { useState } from "react";
import ResourceCard from "../components/ResourceCard";

const allResources = [
  { title: "Physics Past Papers 2024", description: "Complete collection of past board exam papers for Physics with answer keys.", board: "Federal Board", classLevel: "10", subject: "Physics" },
  { title: "Math Key Book Solutions", description: "Step-by-step solutions and key book for Mathematics.", board: "Federal Board", classLevel: "10", subject: "Mathematics" },
  { title: "Biology Chapter Notes", description: "Comprehensive chapter-wise notes for Biology preparation.", board: "Federal Board", classLevel: "10", subject: "Biology" },
  { title: "Chemistry Formulas Sheet", description: "All important chemistry formulas and equations in one place.", board: "AJK Board", classLevel: "9", subject: "Chemistry" },
  { title: "English Grammar Guide", description: "Complete grammar reference with examples and board exam tips.", board: "AJK Board", classLevel: "9", subject: "English" },
  { title: "Physics Solved Numericals", description: "100+ solved numerical problems with detailed steps.", board: "Federal Board", classLevel: "12", subject: "Physics" },
  { title: "Biology Diagrams Pack", description: "High-quality labeled diagrams for all Biology chapters.", board: "Federal Board", classLevel: "11", subject: "Biology" },
  { title: "Math Practice Worksheets", description: "Topic-wise practice worksheets with increasing difficulty.", board: "AJK Board", classLevel: "10", subject: "Mathematics" },
  { title: "Chemistry Lab Manual", description: "Practical lab manual with procedures and viva questions.", board: "Federal Board", classLevel: "9", subject: "Chemistry" },
];

function Resources({ user }) {
  const [board, setBoard] = useState(user?.board || "");
  const [classLevel, setClassLevel] = useState(user?.classLevel || "");
  const [subject, setSubject] = useState("");

  const filtered = allResources.filter((r) => (!board || r.board === board) && (!classLevel || r.classLevel === classLevel) && (!subject || r.subject === subject));
  const sel = "border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-white dark:bg-gray-700 dark:text-white hover:border-blue-300 transition";

  return (
    <div>
      <div className="mb-8"><h2 className="text-2xl font-bold text-gray-800 dark:text-white">Resources</h2><p className="text-gray-400 dark:text-gray-500 text-sm mt-1">{filtered.length} resources available</p></div>
      <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-5 mb-8">
        <div className="flex items-center gap-2 mb-4"><i className="fa-solid fa-filter text-[#2563EB]" /><span className="text-sm font-semibold text-gray-700 dark:text-gray-200">Filter Resources</span></div>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <select value={board} onChange={(e) => setBoard(e.target.value)} className={sel}><option value="">All Boards</option><option value="Federal Board">Federal Board</option><option value="AJK Board">AJK Board</option></select>
          <select value={classLevel} onChange={(e) => setClassLevel(e.target.value)} className={sel}><option value="">All Classes</option>{["9","10","11","12"].map((c) => <option key={c} value={c}>Class {c}</option>)}</select>
          <select value={subject} onChange={(e) => setSubject(e.target.value)} className={sel}><option value="">All Subjects</option>{["Physics","Chemistry","Biology","Mathematics","English"].map((s) => <option key={s} value={s}>{s}</option>)}</select>
        </div>
      </div>
      {filtered.length > 0 ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">{filtered.map((r, i) => <ResourceCard key={i} {...r} />)}</div>
      ) : (
        <div className="text-center py-16"><p className="text-gray-400 dark:text-gray-500 font-medium">No resources found</p><p className="text-gray-300 dark:text-gray-600 text-sm mt-1">Try adjusting your filters</p></div>
      )}
    </div>
  );
}

export default Resources;
