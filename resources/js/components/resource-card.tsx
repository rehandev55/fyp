interface ResourceCardProps {
  id: number;
  title: string;
  type: string;
  subject: string;
  classLevel: string;
  board: string;
  fileSize?: string;
  downloads?: number;
}

const colors: Record<string, string> = { Physics: 'from-blue-500 to-cyan-500', Chemistry: 'from-purple-500 to-pink-500', Biology: 'from-green-500 to-emerald-500', Mathematics: 'from-orange-500 to-amber-500', English: 'from-rose-500 to-red-500' };

export default function ResourceCard({ id, title, type, subject, classLevel, board, fileSize, downloads }: ResourceCardProps) {
  const handleDownload = () => {
    window.open(`/api/content/download/${id}`);
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-hidden hover:shadow-lg hover:-translate-y-1 transition-all duration-300 group">
      <div className={`h-2 bg-gradient-to-r ${colors[subject] || 'from-blue-500 to-cyan-500'}`} />
      <div className="p-5">
        <div className="flex items-start justify-between mb-3">
          <h3 className="font-semibold text-gray-800 dark:text-white group-hover:text-[#2563EB] transition">{title}</h3>
          <span className="text-xs bg-blue-50 dark:bg-blue-900/30 text-[#2563EB] px-2 py-1 rounded-full font-medium whitespace-nowrap ml-2">Class {classLevel}</span>
        </div>
        <div className="flex items-center gap-2 mb-4 flex-wrap">
          <span className="text-xs bg-purple-50 dark:bg-purple-900/30 text-purple-600 px-2 py-0.5 rounded-full font-medium">{type}</span>
          <span className="text-xs text-gray-400">{board}</span>
          {fileSize && <span className="text-xs text-gray-400">{fileSize}</span>}
          {downloads !== undefined && <span className="text-xs text-gray-400">{downloads} downloads</span>}
        </div>
        <button onClick={handleDownload} className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-2.5 rounded-xl hover:shadow-md transition text-sm font-medium flex items-center justify-center gap-2">
          <i className="fa-solid fa-download text-xs" />
          Download
        </button>
      </div>
    </div>
  );
}
