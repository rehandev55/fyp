interface ResourceCardProps {
  title: string;
  description: string;
  subject: string;
  classLevel: string;
}

const colors: Record<string, string> = { Physics: 'from-blue-500 to-cyan-500', Chemistry: 'from-purple-500 to-pink-500', Biology: 'from-green-500 to-emerald-500', Mathematics: 'from-orange-500 to-amber-500', English: 'from-rose-500 to-red-500' };

export default function ResourceCard({ title, description, subject, classLevel }: ResourceCardProps) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-hidden hover:shadow-lg hover:-translate-y-1 transition-all duration-300 group">
      <div className={`h-2 bg-gradient-to-r ${colors[subject] || 'from-blue-500 to-cyan-500'}`} />
      <div className="p-5">
        <div className="flex items-start justify-between mb-3">
          <h3 className="font-semibold text-gray-800 dark:text-white group-hover:text-[#2563EB] transition">{title}</h3>
          <span className="text-xs bg-blue-50 dark:bg-blue-900/30 text-[#2563EB] px-2 py-1 rounded-full font-medium whitespace-nowrap ml-2">Class {classLevel}</span>
        </div>
        <p className="text-sm text-gray-500 dark:text-gray-400 mb-4 leading-relaxed">{description}</p>
        <button className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-2.5 rounded-xl hover:shadow-md transition text-sm font-medium flex items-center justify-center gap-2">
          <i className="fa-solid fa-download text-xs" />
          Download
        </button>
      </div>
    </div>
  );
}
