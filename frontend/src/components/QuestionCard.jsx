import { useState } from "react";

function QuestionCard({ question, options, correctAnswer, answer, explanation, onNext }) {
  const [selected, setSelected] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [textAnswer, setTextAnswer] = useState("");

  const isMCQ = !!options;
  const handleSubmit = () => {
    if (isMCQ && selected !== null) setSubmitted(true);
    if (!isMCQ && textAnswer.trim()) setSubmitted(true);
  };
  const handleNext = () => { setSelected(null); setSubmitted(false); setTextAnswer(""); onNext(); };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 md:p-8 max-w-2xl mx-auto">
      <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-6 leading-relaxed">{question}</h3>

      {isMCQ && (
        <div className="space-y-3 mb-6">
          {options.map((opt, i) => {
            let classes = "border-gray-200 dark:border-gray-600 hover:border-blue-300 dark:hover:border-blue-500 hover:bg-blue-50/50 dark:hover:bg-blue-900/20 text-gray-700 dark:text-gray-200";
            if (submitted) {
              if (i === correctAnswer) classes = "border-emerald-400 bg-emerald-50 dark:bg-emerald-900/30 text-emerald-800 dark:text-emerald-300 ring-1 ring-emerald-200 dark:ring-emerald-800";
              else if (i === selected) classes = "border-red-400 bg-red-50 dark:bg-red-900/30 text-red-800 dark:text-red-300 ring-1 ring-red-200 dark:ring-red-800";
              else classes = "border-gray-100 dark:border-gray-700 text-gray-400 dark:text-gray-600";
            } else if (i === selected) {
              classes = "border-[#2563EB] bg-blue-50 dark:bg-blue-900/30 text-[#2563EB] ring-1 ring-blue-200 dark:ring-blue-800";
            }
            return (
              <button key={i} onClick={() => !submitted && setSelected(i)} disabled={submitted} className={`w-full text-left px-5 py-4 rounded-xl border-2 transition-all duration-200 text-sm font-medium flex items-center gap-3 ${classes}`}>
                <span className={`w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0 ${submitted && i === correctAnswer ? "bg-emerald-500 text-white" : submitted && i === selected ? "bg-red-500 text-white" : i === selected ? "bg-[#2563EB] text-white" : "bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400"}`}>
                  {String.fromCharCode(65 + i)}
                </span>
                {opt}
              </button>
            );
          })}
        </div>
      )}

      {!isMCQ && !submitted && (
        <div className="mb-6">
          <textarea
            value={textAnswer}
            onChange={(e) => setTextAnswer(e.target.value)}
            placeholder="Type your answer here..."
            rows={answer && answer.length > 200 ? 8 : 4}
            className="w-full px-4 py-3 rounded-xl border-2 border-gray-200 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-100 text-sm leading-relaxed placeholder-gray-400 dark:placeholder-gray-500 focus:border-[#2563EB] focus:ring-1 focus:ring-blue-200 dark:focus:ring-blue-800 outline-none transition-all duration-200 resize-vertical"
          />
        </div>
      )}

      {!isMCQ && submitted && (
        <div className="space-y-4 mb-6">
          <div className="p-4 rounded-xl bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800">
            <p className="text-xs font-semibold text-blue-500 dark:text-blue-400 uppercase tracking-wide mb-2"><i className="fa-solid fa-pen-to-square mr-1" /> Your Answer</p>
            <p className="text-sm text-gray-700 dark:text-gray-200 leading-relaxed">{textAnswer}</p>
          </div>
          <div className="p-4 rounded-xl bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800">
            <p className="text-xs font-semibold text-emerald-500 dark:text-emerald-400 uppercase tracking-wide mb-2"><i className="fa-solid fa-check-double mr-1" /> Model Answer</p>
            <p className="text-sm text-gray-700 dark:text-gray-200 leading-relaxed">{answer}</p>
          </div>
        </div>
      )}

      {!submitted ? (
        <button onClick={handleSubmit} disabled={isMCQ ? selected === null : !textAnswer.trim()} className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg disabled:opacity-40 disabled:cursor-not-allowed disabled:shadow-none transition-all duration-200 text-sm font-semibold">Submit Answer</button>
      ) : (
        <div className="space-y-4">
          {isMCQ && (
            <div className={`p-5 rounded-xl ${selected === correctAnswer ? "bg-emerald-50 dark:bg-emerald-900/30 border border-emerald-200 dark:border-emerald-800" : "bg-red-50 dark:bg-red-900/30 border border-red-200 dark:border-red-800"}`}>
              <p className={`font-semibold ${selected === correctAnswer ? "text-emerald-700 dark:text-emerald-300" : "text-red-700 dark:text-red-300"}`}>
                <i className={`${selected === correctAnswer ? "fa-solid fa-circle-check" : "fa-solid fa-circle-xmark"} mr-2`} />
                {selected === correctAnswer ? "Correct!" : "Incorrect!"}
              </p>
              {explanation && <p className="text-gray-600 dark:text-gray-300 text-sm mt-2 leading-relaxed">{explanation}</p>}
            </div>
          )}
          {!isMCQ && explanation && (
            <div className="p-4 rounded-xl bg-amber-50 dark:bg-amber-900/20 border border-amber-200 dark:border-amber-800">
              <p className="text-xs font-semibold text-amber-500 dark:text-amber-400 uppercase tracking-wide mb-2"><i className="fa-solid fa-lightbulb mr-1" /> Explanation</p>
              <p className="text-sm text-gray-600 dark:text-gray-300 leading-relaxed">{explanation}</p>
            </div>
          )}
          <button onClick={handleNext} className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg transition-all duration-200 text-sm font-semibold">Next Question <i className="fa-solid fa-arrow-right ml-1" /></button>
        </div>
      )}
    </div>
  );
}

export default QuestionCard;
