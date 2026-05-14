import { useState,useEffect } from 'react';
import { Head, usePage } from '@inertiajs/react';
import StudentLayout from '@/layouts/student-layout';
import QuestionCard from '@/components/question-card';
import { api } from '@/lib/api';

interface User {
    name: string;
    email: string;
    role?: string;
    subject?: string;
    class_level?: string;
    board?: string;
}

function getChapters(classLevel: string, subject: string) {
    if (!classLevel || !subject) return [];

    const classData = (CURRICULUM_DATA as any)[classLevel];
    if (!classData) return [];

    return classData[subject] || [];
}

function parseQuestions(raw: string) {
    const blocks = raw.split("\n\n");

    return blocks.map((block) => {
        const lines = block.split("\n");

        const question = lines[0]?.replace(/^Q\d+\.\s*/, "") || "";

        const options = lines
            .filter(line => line.match(/^[A-D]\)/))
            .map(line => line.replace(/^[A-D]\)\s*/, ""));

        const correctLine = lines.find(line => line.startsWith("Correct:"));
        // const correctLetter = correctLine?.split(":")[1]?.trim();
        const correctLetter = correctLine?.split(":")[1]?.trim() || "";

        const correctAnswer = ["A", "B", "C", "D"].indexOf(correctLetter);

        const explanationLine = lines.find(line => line.startsWith("Explanation:"));
        const explanation = explanationLine?.replace("Explanation:", "").trim() || "";

        // const [answers, setAnswers] = useState<{ [key: number]: number }>({});

        return {
            chapter: "", // optional (you can improve later)
            question,
            options,
            correctAnswer,
            explanation
        };
    });
}
const allSubjects = ['physics', 'chemistry', 'biology', 'mathematics','computer', 'english','urdu'];

const CURRICULUM_DATA = {
    class_9 : {
physics: ['PHYSICAL QUANTITIES AND MEASUREMENT', 'KINEMATICS', 'DYNAMICS - I', 'DYNAMICS - II', 'PRESSURE AND DEFORMATION IN SOLIDS', 'WORK AND ENERGY', 'DENSITY AND TEMPERATURE', 'MAGNETISM', 'NATURE OF SCIENCE AND PHYSICS'],
chemistry: ['Nature of Science in Chemistry', 'Matter', 'Atomic Structure', 'Periodic Table and Periodicity of Properties', 'Chemical Bonding', 'Stoichimetery', 'Electrochemistry', 'Energetics', 'Chemical Equilibrium', 'Acids, Bases & Salts', 'Enviromental Chemistry-Air', 'Enviromental Chemistry-Water', 'Organic Chemistry', 'Hydrocarbons', 'Biochemistry', 'Empirical Data Collection and Analysis', 'Separation Techniques', 'Qualitative Analysis', 'Chromatography'],
biology: ['The Science of Biology', 'Biodiversity', 'Cell', 'Cell Cycle', 'Tissues, Organ and Organ System', 'Molecular Biology', 'Metabolism', 'Plant Physiology', 'Plant Reproduction', 'Evolution'],
mathematics: ['Real Numbers', 'Logarithms', 'Sets and Relations', 'Factorization and Algebraic Manipulation', 'Linear Equations and Inequalities', 'Trigonometry and Bearing', 'Coordinate Geometry', 'Geometry of Straight Lines', 'Geometry and Polygons', 'Practical Geometry', 'Basic Statistics'],
english: ['Hazrat Muhammad Rasulullah (ﷺ): A Mercy for All Creation', "The Art of Muslim Women's Entrepreneurship", 'Modern World and Age of Digital Globalization', 'Nothing is Impossible-The Construction of Spectacular Brooklyn Bridge', "5 of Jeff Benzo's best lessons for success from his 27 year as Amazon CEO", 'Say No to Drugs', 'Mowing by Robert Frost', 'The Eagle by Alfred Tennyson (Poem)', 'Travel and Tourism', 'Two Mothers Remembered by Joann Snow Duncanson', 'The Metamorphosis', 'Good Health and Well being'],
computer: ['Computer System', 'Computational Thinking and Algorithms', 'Programming Fundamentals', 'Data and Analysis', 'Application of Computer Science', 'Impacts of Computing', 'Entrepreneuship'],
urdu: ['Ikhlaq-e-Hasna', 'Katba', 'Bheriya', 'Aaram o Sukoon', 'Kaleem aur Mirza Zahir Dar Baig', 'Naam Deo Mali', 'Ibtidai Hisab', 'Lari Mein Paroye Hue Manzar', 'Apni Madad Aap', 'Hamd', 'Naat', 'Javed Ke Naam', 'Mehnat Ki Barkat', 'Cricket aur Mushaira', 'Payam-e-Latif', 'Faqirana Aaye Sada Kar Chale', 'Sun To Sahi Jahan Mein Hai Tera Fasana Kya', 'Gham Hai Ya Khushi Hai Tu', 'Kash Tufan Mein Safine Ko Utara Hota'],
},

class_10 : {
physics: ['Heat Capacity and Modes of Heat Transfer', 'Thermal Expansion and Change of State', 'Waves', 'Sound', 'Optics', 'Electrostatics', 'Current Electricity', 'Electric Circuits', 'Electronics', 'Electromagnetism', 'Electromagnetic Waves', 'Nuclear Physics'],
chemistry: ['History of Chemistry', 'Matter', 'Stoichiometry', 'Electrochemistry', 'Reaction Kinetics', 'Salts', 'Nitrogen, Sulphur and Metals', 'Organic Chemistry', 'Hydrocarbons', 'Hydroxy Compounds', 'Carboxylic Compounds', 'Polymers', 'Biochemistry'],
biology: ['Digestive system', 'Circulatory system', 'Respiratory system', 'Urinary system', 'Nervous system', 'Reproduction', 'Inheritance', 'Diseases', 'Immunity', 'Biotechnology', 'Biostatistics and data analysis'],
mathematics: ['Complex Numbers', 'Quadratic Equations', 'Matrices And Determinants', 'Linear and Quadratic Inequalities', 'Algebraic Fractions', 'Functions And Graphs', 'Vectors in Plane', 'Application of Trigonometry', 'Chord and Arcs of a Circle', 'Tangents and Angles of a Circle', 'Practical Geometry of Circles', 'Basic Statistics'],
english: ['Animal Rights in Islam: Showing Compassion', 'Cultural Festivals of Pakistan: Unity in Diversity', 'Media Literacy in the Modern Age', "Thank You, Ma'am: (Langston Hughes)", 'Mother Nature (Poem)', 'How to Make Better Decisions About Your Career', 'The Alchemist', 'Blue (Poem)', 'The Menace of Drugs', 'Earth and Environment', 'Adventure Sports', 'Importance of Life Skills', 'The Oyster and the Pearl (Play)'],
computer: ['Computer Systems', 'Computational Thinking and Algorithms', 'Programming Fundamentals', 'Data and Analysis', 'Application of Computer Science', 'Impacts of Computing', 'Data Literacy', 'Entrepreneuship in Digital Age'],
urdu: ['Ikhlaq-e-Nabwi ﷺ', 'Mohsin Muhalla', 'Kaffara', 'Chughal Khor', 'Dastak', 'Old Age Home', 'Mera Gaon', 'Sir Syed Ka Bachpan', 'Sawere Jo Kal Aankh Meri Khuli', 'Babul Ke Khandar', 'Kuch Zariya-e-Taleem Ke Bare Mein', 'Hamd', 'Naat', 'Khitab Ba Jawan-e-Islam', 'Aya-e-Subh', 'Admi Nama', 'Waghera', 'Bazicha-e-Atfal Hai Duniya Mere Aage', 'Asar Is Ko Zara Nahin Hota', 'Hai Mashq-e-Sukhan Jari Chakki Ki Mashaqqat Bhi', 'Yun Kehne Ko Mir Ik Bimar Bohat Hai'],
},
  class_11: {
    biology: ['Cells and Sub-Cellular Organelles', 'Molecular Biology', 'Enzymes', 'Bioenergetics', 'Acellular Life', 'Prokaryotes', 'Protista and Fungi', 'Plantae', 'Diversity in Plant Functions', 'Animalia', 'Reproduction', 'Inheritance', 'Chromosome and DNA', 'Evolution', 'Ecology'],
    physics: ['Physical Quantities and Measurements', 'Vectors', 'Translatory Motion', 'Rotational and Circular Motion', 'Work and Kinetic Energy', 'Fluid Mechanics', 'Physics of Solids', 'Heat and Thermodynamics', 'Waves', 'Electrostatics', 'Electricity', 'Magnetism', 'Relativity', 'Particle Physics'],
    mathematics: ['Complex Numbers', 'Matrices and Determinants', 'Vectors', 'Sequences and Series', 'Polynomials', 'Permutation and Combination', 'Mathematical Induction and Binomial Theorem', 'Fundamentals of Trigonometry', 'Trigonometric Functions'],
    chemistry: ['History of Chemistry', 'Atomic Structure', 'Chemical Bonding', 'Stoichiometry', 'States and Phases of Matter', 'Energetics', 'Chemical Kinetics', 'Chemical Equilibrium', 'Acids - Bases Chemistry', 'Periodic Table', 'Nitrogen and Sulphur', 'Halogens', 'Environmental Chemistry-Air', 'Environmental Chemistry-Water', 'Organic Chemistry', 'Hydrocarbons', 'Halogenoalkanes', 'Alcohol', 'Carbonyl Compounds', 'Nitrogen Compounds-Amines', 'Organic Synthesis', 'Energy'],
    computer: ['Computer Systems', 'Computational Thinking & Algorithms', 'Programming Fundamentals', 'Data and Analysis', 'Application of Computer Science', 'Impacts of Computing', 'Digital Literacy', 'Entrepreneurship in Digital Age'],
    english: ['Family Values In Pakistan', 'Shooting Stars', 'The Wind', 'Butterflies', 'Clean water and Sanitation', 'The Darkling Thrush', 'World Heritage Sites in Pakistan', 'Social Media: A Blessing or a Curse?', 'Sunshine After Rain', 'The Small Woman', 'The Three Questions', 'Break Break Break', 'Blow, Blow, Thou', 'Choice of a Profession', 'The Ninny', 'Fourteen', 'The Last Leaf', 'The Necklace'],
    urdu: ['Ikhlaq-e-Hasna', 'Naya Qanoon', 'Tareekh Ka Kafan', 'Dahliz', 'Aur Pakistan Ban Gaya', 'Ek Ustad Adalat Ke Kat-hare Mein', 'Makateeb-e-Ghalib', 'Faqah Mein Rozah', 'Pakistani Zabanein Aur Un Ka Bahami Rishta', 'Charpai', 'Hamd', 'Naat', 'Milli Naghma', 'Ae Wadi-e-Lulab', 'Katba', 'Azadi', 'Rehman Baba', 'Pata Pata Boota Boota Hal Hamara Jane Hai', 'Sar Mein Sauda Bhi Nahin Dil Mein Tamanna Bhi Nahin', 'Be Chain Bohat Phirna Ghabraye Hue Rehna', 'Silsile Tor Gaya Woh Sabhi Jate Jate', 'Baadbaan Khulne Se Pehle Ka Ishara Dekhna'],
},
  class_12: {
    chemistry: ['s AND p - BLOCK ELEMENTS', 'd AND f BLOCK ELEMENTS', 'ORGANIC COMPOUNDS', 'HYDROCARBONS', 'ALKYL HALIDE AND AMINE', 'ALCOHOL, PHENOLS AND ETHRS', 'ALDEHYDES AND KETONES', 'CARBONYL COMPOUNDS', 'BIOCHEMISTRY', 'INDUSTRIAL CHEMISTRY', 'ENVIRONMENTAL CHEMISTRY', 'ANALYTICAL CHEMISTRY'],
    mathematics: ['Functions and Graphs', 'Limit, Continuity and Derivative', 'Integration', 'Differential Equations', 'Kinematics of Motion in a Straight Line', 'Analytical Geometry', 'Conic Section', 'Inverse Trigonometric Functions and Their Graphs', 'Solution of Trigonometric Equations', 'Numerical Methods'],
    urdu: ['Kamali Nafs aur Makarim-e-Akhlaq', 'Mashar', 'Ma-G-Ni', 'Rustum o Sohrab', 'Shakhon Par Jalte Hue Basere', 'Shuru-e-Qissa Ka', 'Bahadur Khan Ki Sarguzasht', 'Kafi', 'Beetay', 'Nazria-e-Pakistan', 'Hamd', 'Naat', 'Main Rozay Say Hun', 'Shehr Main Teri Galiyon Ke', 'Insan-e-Kamil Ki Barkat', 'Nayi Nasl Ka Nauha', 'Dastan Tayyari Main Bagh Ki', 'Jag Main Aa Kar Idhar Udhar Dekha', 'Sab Kahan Kuch Lala o Gul Main Numayan Ho Gayin', 'Sitaron Se Aage Jahan Aur Bhi Hain', 'Wohi Khwab Aankhon Main Daal De Jo Nizam-e-Sham o Visal De', 'Ye Fakhr To Hasil Hai Buray Hain Ke Bhallay Hain'],
    physics: ['Gravitation', 'Statistical Mechanics and Thermodynamics', 'Simple Harmonic Motion', 'Diffraction and Interference', 'Electric Potential and Capacitor', 'Alternating Current', 'Quantum Physics', 'Nuclear Physics', 'Cosmology', 'Earth Climate', 'Medical Imaging', 'Nature of Science: A Debate'],
    english: ['LINGKUAN GORGE', 'POPULATION EXPLOSION IN PAKISTAN', 'THE INCOME-TAX MAN', 'Rubaiyat of Omar Khayam', 'THE BLANKET', 'STAY HUNGRY - STAY FOOLISH', 'TOBACCO AND YOUR HEALTH', 'THE SEA', 'First Year At Harrow', 'THERE’S A NEW PLANET IN SIGHT', 'HARVEST HYMN', 'THE KAGHAN VALLEY', 'AFTER TWENTY YEARS', 'The Solitary Reaper', 'The Pearl'],
    biology: ['Respiration', 'Homeostasis', 'Support and Movement', 'Nervous Coordination', 'Chemical Coordination', 'Behaviour', 'Reproduction', 'Development and Aging', 'Inheritance', 'Chromosome and DNA', 'Evolution', 'Man and His Environment', 'Biotechnology', 'Biology and Human Welfare'],
    computer: ['Operating System', 'System Development Life Cycle', 'Object Oriented Programming in C++', 'Control Structures', 'Arrays and Strings', 'Functions', 'Pointers', 'Objects and Classes', 'File Handling'],

  }
};

interface MCQQuestion {
    chapter: string;
    question: string;
    options: string[];
    correctAnswer: number;
    explanation: string;
}

interface WrittenQuestion {
    chapter: string;
    question: string;
    answer: string;
    explanation: string;
}

type QuizMode = 'mcq' | 'short' | 'long';

export default function Practice() {
    const [profileConfirmed, setProfileConfirmed] = useState(false);
    const { auth } = usePage<{ auth: { user: User } }>().props;
    const user = auth.user;

    const [questions, setQuestions] = useState<any[]>([]);
const [loading, setLoading] = useState(false);

const [userAnswers, setUserAnswers] = useState<string[]>([]);
const [score, setScore] = useState(0);
const [mcqAnswers, setMcqAnswers] = useState<number[]>([]);

    // Quiz state
    const [chapterScope, setChapterScope] = useState<'whole' | 'selected' | null>(null);
    const [selectedChapters, setSelectedChapters] = useState<string[]>([]);
    const [mode, setMode] = useState<QuizMode | null>(null);
    const [currentQ, setCurrentQ] = useState(0);
    const [finished, setFinished] = useState(false);
    const hasProfile = !!(user?.board && user?.class_level && user?.subject);

const [board, setBoard] = useState('');
const [classLevel, setClassLevel] = useState('');
const [subject, setSubject] = useState('');

const activeSubject = subject;
const activeClass = classLevel;
const activeBoard = board;

useEffect(() => {
    if (user) {
        setBoard(user.board || '');
        setClassLevel(user.class_level || '');
        setSubject(user.subject || '');
    }
}, [user]);
const subjectChapters = getChapters(activeClass, activeSubject);
    // const hasSelection = !!(activeSubject && activeClass && activeBoard);
    const hasSelection =
    !!activeSubject &&
    !!activeClass &&
    !!activeBoard &&
    subjectChapters.length > 0;


    const toggleChapter = (ch: string) => {
        setSelectedChapters((prev) => prev.includes(ch) ? prev.filter((c) => c !== ch) : [...prev, ch]);
    };

    const selectAllChapters = () => {
        setSelectedChapters(selectedChapters.length === subjectChapters.length ? [] : [...subjectChapters]);
    };

    // const [feedbacks, setFeedbacks] = useState<string[]>([]);
const [checked, setChecked] = useState(false);
const [loadingEval, setLoadingEval] = useState(false);

const handleNext = async () => {

    let latestFeedbacks = [...feedbacks];
    let latestScores = [...scores];

    // MCQ evaluation
    if (mode === 'mcq') {

        const currentQuestion = questions[currentQ];
        const selectedIndex = mcqAnswers[currentQ];

        const selectedOption =
            currentQuestion.options[selectedIndex];

        const correctOption =
            currentQuestion.options[currentQuestion.correctAnswer];

        const result = await evaluateMcq(
            currentQuestion.question,
            selectedOption,
            correctOption
        );

        // save feedback
        latestFeedbacks[currentQ] =
            String(result?.feedback || '');

        setFeedbacks(latestFeedbacks);

        // save score
        latestScores[currentQ] =
            result?.score || 0;

        setScores(latestScores);

        // optional frontend display score
        setScore((prev) => prev + (result?.score || 0));
    }

    setChecked(false);

    if (currentQ < questions.length - 1) {
        setCurrentQ(currentQ + 1);
        return;
    }

    setFinished(true);

    // PASS FRESH DATA HERE
    const overall = await evaluateOverall(
        latestFeedbacks,
        latestScores
    );

    setOverallResult(overall);
};

const handleCheckAnswer = async () => {
    const currentQuestion = questions[currentQ];
    const answer = userAnswers[currentQ];

    setLoadingEval(true);

    const result = await evaluateAnswer(
        currentQuestion.question,
        answer
    );

   const updatedFeedbacks = [...feedbacks];
updatedFeedbacks[currentQ] = result?.feedback || "No feedback";

setFeedbacks(updatedFeedbacks);

const updatedScores = [...scores];
updatedScores[currentQ] = result?.score || 0;

setScores(updatedScores);
    setChecked(true);

    setLoadingEval(false);
};


    const resetToMode = () => { setMode(null); setCurrentQ(0); setFinished(false); };
    const resetToChapters = () => { setChapterScope(null); setSelectedChapters([]); setMode(null); setCurrentQ(0); setFinished(false);    setOverallResult(null);};

    const modes = [
        { key: 'mcq' as QuizMode, label: 'MCQ', desc: 'Multiple choice questions to test your knowledge', icon: 'fa-solid fa-list-check', gradient: 'from-blue-500 to-indigo-600' },
        { key: 'short' as QuizMode, label: 'Short Questions', desc: 'Brief answer questions for quick review', icon: 'fa-solid fa-pen-to-square', gradient: 'from-emerald-500 to-teal-600' },
        { key: 'long' as QuizMode, label: 'Long Questions', desc: 'Detailed questions for deep understanding', icon: 'fa-solid fa-file-lines', gradient: 'from-purple-500 to-pink-600' },
    ];

    const sel = 'w-full border border-gray-200 dark:border-gray-600 rounded-xl px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-transparent bg-gray-50 dark:bg-gray-700 dark:text-white hover:bg-white dark:hover:bg-gray-600 transition';
const [feedbacks, setFeedbacks] = useState<string[]>([]);
const [scores, setScores] = useState<number[]>([]);

const [overallResult, setOverallResult] = useState<any>(null);
    const evaluateAnswer = async (question: string, answer: string) => {
    try {
        const res = await api('/quiz/evaluate', {
            method: 'POST',
            body: JSON.stringify({
                question,
                student_answer: answer,
                 type: mode,
                board: activeBoard,
                class_level: activeClass,
                subject: activeSubject,
            }),
        });

        return await res.json();
    } catch (err) {
        console.error(err);
        return null;
    }
};


// mcqs evaluate
const evaluateMcq = async (
    question: string,
    studentAnswer: string,
    correctAnswer: string | number
) => {
    try {
        const res = await api('/quiz/evaluate', {
            method: 'POST',
            body: JSON.stringify({
                question,
                student_answer: studentAnswer,
                correct_answer: correctAnswer,
                type: 'mcq',
                board: activeBoard,
                class_level: activeClass,
                subject: activeSubject,
            }),
        });

        return await res.json();
    } catch (err) {
        console.error(err);
        return null;
    }
};
const evaluateOverall = async (
    latestFeedbacks = feedbacks,
    latestScores = scores
) => {
    const results = questions.map((q, index) => ({
        question: q.question,
       student_answer:
    mode === 'mcq'
        ? questions[index].options[mcqAnswers[index]] || ''
        : userAnswers[index] || '',
      score: latestScores[index] || 0,

feedback:
    String(latestFeedbacks?.[index] || ''),
    }));

    const payload = {
        board: activeBoard,
        class_level: activeClass,
        subject: activeSubject,
        question_type: mode,
        results,
    };

    const res = await api('/quiz/overall', {
        method: 'POST',
        body: JSON.stringify(payload),
    });

    return await res.json();
};


    // Screen 1: Subject selection
    // if (!hasSelection) {
    if (!profileConfirmed) {
        // console.log(user);
        return (
            <>
                <Head title="Practice Quiz" />
                <div>
                    <div className="text-center mb-8">
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Practice Quiz</h2>
                        <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">Choose your subject and start practicing</p>
                    </div>
                    <div className="max-w-lg mx-auto">


                        {/* Selection dropdowns */}
                        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 space-y-4 mb-6">
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Board</label>

                                   <select value={board} onChange={(e) => setBoard(e.target.value)} className={sel}>
                                    <option value="">Select Board</option>
                                    <option value="federal">Federal Board</option>
                                    <option value="ajk">AJK Board</option>
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Class</label>

                                    <select value={classLevel} onChange={(e) => {
    setClassLevel(e.target.value);

}} className={sel}>
                                    <option value="">Select Class</option>
                                    {['class_9', 'class_10', 'class_11', 'class_12'].map((c) => <option key={c} value={c}>{c}</option>)}
                                </select>
                            </div>
                            <div>
                                <label className="block text-sm font-semibold text-gray-700 dark:text-gray-200 mb-2">Subject</label>

                                   <select value={subject} onChange={(e) => setSubject(e.target.value)} className={sel}>
                                    <option value="">Select Subject</option>
                                    {allSubjects.map((s) => <option key={s} value={s}>{s}</option>)}
                                </select>
                            </div>
                        </div>

                        {/* Hand icon card */}
                        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-10 text-center">
                            <div className="w-20 h-20 bg-gradient-to-br from-blue-100 to-indigo-100 dark:from-blue-900/30 dark:to-indigo-900/30 rounded-full flex items-center justify-center mx-auto mb-5">
                                <i className="fa-solid fa-hand-pointer text-[#2563EB] text-3xl" />
                            </div>
                            <h3 className="text-lg font-bold text-gray-800 dark:text-white mb-2">Select Your Subject</h3>
                            <p className="text-gray-500 dark:text-gray-400 text-sm">Choose your board, class, and subject above to start practicing.</p>
                        </div>
                        <button
    onClick={() => setProfileConfirmed(true)}
    disabled={!hasSelection}
    className="w-full mt-6 bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl font-semibold disabled:opacity-40"
>
    Continue
</button>
                    </div>
                </div>
            </>
        );
    }

    // Screen 2: Chapter selection (Whole Book / Select Chapters)
    if (chapterScope === null) {
        return (
            <>
                <Head title="Practice Quiz - Chapters" />
                <div>
                    <div className="text-center mb-8">
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Select Chapters</h2>
                        <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">
                            {activeSubject} — Class {activeClass} — {activeBoard}
                        </p>
                    </div>
                    <div className="max-w-2xl mx-auto space-y-5">
                        <button onClick={() => { setChapterScope('whole'); setSelectedChapters([...subjectChapters]); }} className="w-full bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 text-left hover:shadow-lg hover:-translate-y-1 transition-all duration-300 group flex items-center gap-5">
                            <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg group-hover:scale-110 transition-transform duration-300">
                                <i className="fa-solid fa-book text-white text-xl" />
                            </div>
                            <div className="flex-1">
                                <h3 className="font-bold text-gray-800 dark:text-white text-lg">Whole Book</h3>
                                <p className="text-sm text-gray-500 dark:text-gray-400 mt-0.5">Practice questions from all {subjectChapters.length} chapters</p>
                            </div>
                            <i className="fa-solid fa-chevron-right text-gray-400 group-hover:text-[#2563EB] transition" />
                        </button>

                        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6">
                            <div className="flex items-center gap-5 mb-5">
                                <div className="w-14 h-14 bg-gradient-to-br from-emerald-500 to-teal-600 rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg">
                                    <i className="fa-solid fa-list text-white text-xl" />
                                </div>
                                <div className="flex-1">
                                    <h3 className="font-bold text-gray-800 dark:text-white text-lg">Select Chapters</h3>
                                    <p className="text-sm text-gray-500 dark:text-gray-400 mt-0.5">Choose specific chapters to practice</p>
                                </div>
                            </div>

                            <div className="mb-4">
                                <button onClick={selectAllChapters} className="text-xs font-semibold text-[#2563EB] hover:text-blue-700 transition">
                                    {selectedChapters.length === subjectChapters.length ? 'Deselect All' : 'Select All'}
                                </button>
                            </div>

                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-5">
                                {subjectChapters.map((ch: string, i: string) => (
                                    <button
                                        key={ch}
                                        onClick={() => toggleChapter(ch)}
                                        className={`flex items-center gap-3 px-4 py-3 rounded-xl border-2 text-sm font-medium transition-all duration-200 text-left ${
                                            selectedChapters.includes(ch)
                                                ? 'border-[#2563EB] bg-blue-50 dark:bg-blue-900/30 text-[#2563EB]'
                                                : 'border-gray-200 dark:border-gray-600 text-gray-600 dark:text-gray-300 hover:border-blue-300 hover:bg-blue-50/50 dark:hover:bg-blue-900/20'
                                        }`}
                                    >
                                        <span className={`w-6 h-6 rounded-md flex items-center justify-center text-xs flex-shrink-0 ${
                                            selectedChapters.includes(ch) ? 'bg-[#2563EB] text-white' : 'bg-gray-100 dark:bg-gray-700 text-gray-400'
                                        }`}>
                                            {selectedChapters.includes(ch) ? <i className="fa-solid fa-check text-xs" /> : (i + 1)}
                                        </span>
                                        {ch}
                                    </button>
                                ))}
                            </div>

                            <button
                                onClick={() => { if (selectedChapters.length > 0) setChapterScope('selected'); }}
                                disabled={selectedChapters.length === 0}
                                className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg disabled:opacity-40 disabled:cursor-not-allowed disabled:shadow-none transition-all duration-200 text-sm font-semibold flex items-center justify-center gap-2"
                            >
                                Continue with {selectedChapters.length} chapter{selectedChapters.length !== 1 ? 's' : ''} <i className="fa-solid fa-arrow-right" />
                            </button>
                        </div>
                    </div>
                </div>
            </>
        );
    }

    // Screen 3: Quiz mode selection (MCQ / Short / Long)
    if (!mode) {
        return (
            <>
                <Head title="Practice Quiz" />
                <div>
                    <div className="text-center mb-8">
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Practice Quiz</h2>
                        <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">Choose a quiz mode</p>
                    </div>
                    <div className="grid gap-5 max-w-2xl mx-auto">
                        {modes.map((m) => {
                            // const count = getFilteredQuestions(m.key).length;
                            const count = 10; // or any default number
                            return (
                                <button key={m.key} onClick={async () => {
    setMode(m.key);
   setLoading(true);
   setScore(0);
setMcqAnswers([]);

try {
    const res = await api('/quiz/generate', {
        method: 'POST',
        body: JSON.stringify({
            topic: (chapterScope === 'whole'
        ? subjectChapters.join(', ')
        : selectedChapters.join(', ')
    ),
            board: activeBoard,
            class_level: activeClass,
            subject: activeSubject,
            chapters: chapterScope === 'whole' ? subjectChapters : selectedChapters,
            question_type: m.key,
            num_questions: 2
        })
    });

    const data = await res.json();

    // console.log(data);

    // setQuestions(Array.isArray(data.questions) ? data.questions : []);
    if (typeof data.questions === "string") {
    setQuestions(parseQuestions(data.questions));
} else {
    setQuestions(data.questions || []);
}
} catch (err) {
    console.error(err);
} finally {
    setLoading(false);
}
    // ${count === 0 ? 'opacity-50 cursor-not-allowed hover:shadow-sm hover:translate-y-0' : ''}
}} disabled={false} className={`bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 text-left hover:shadow-lg hover:-translate-y-1 transition-all duration-300 group flex items-center gap-5 `}>
                                    <div className={`w-14 h-14 bg-gradient-to-br ${m.gradient} rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg group-hover:scale-110 transition-transform duration-300`}>
                                        <i className={`${m.icon} text-white text-xl`} />
                                    </div>
                                    <div className="flex-1">
                                        <h3 className="font-bold text-gray-800 dark:text-white text-lg">{m.label}</h3>
                                        <p className="text-sm text-gray-500 dark:text-gray-400 mt-0.5">{m.desc}</p>
                                    </div>
                                    <span className={`text-xs px-3 py-1.5 rounded-full font-semibold ${count > 0 ? 'bg-blue-50 dark:bg-blue-900/30 text-[#2563EB]' : 'bg-gray-100 dark:bg-gray-700 text-gray-400'}`}>{count} Qs</span>
                                </button>
                            );
                        })}
                        <button onClick={resetToChapters} className="text-sm text-gray-500 hover:text-[#2563EB] transition mt-2 flex items-center justify-center gap-1">
                            <i className="fa-solid fa-chevron-left text-xs" />
                            Change chapters
                        </button>
                    </div>
                </div>
            </>
        );
    }

    // Quiz complete
    if (finished) {
        return (
            <>
                <Head title="Practice Quiz" />
                <div className="max-w-md mx-auto text-center">
                    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-10">
                        <div className="w-20 h-20 bg-gradient-to-br from-emerald-400 to-teal-500 rounded-full flex items-center justify-center mx-auto mb-5 shadow-lg">
                            <i className="fa-solid fa-check text-white text-3xl" />
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800 dark:text-white mb-2">Quiz Complete!</h2>
                        <p className="text-gray-500 dark:text-gray-400 mb-6">You completed all {questions.length} questions.</p>
                        {/* {mode === 'mcq' && (
    <p className="text-lg font-semibold text-blue-500 mb-4">
        Score: {score} / {questions.length}
    </p>
)} */}

                        <div className="flex gap-3">

                            <button onClick={() => {
    setCurrentQ(0);
    setFinished(false);

    setOverallResult(null);

    // RESET EVERYTHING
    setScore(0);
    setMcqAnswers([]);
    setUserAnswers([]);
    setFeedbacks([]);
    setChecked(false);
}} className="flex-1 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-3 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition text-sm font-semibold">Retry</button>
                            <button onClick={resetToChapters} className="flex-1 bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg transition text-sm font-semibold">New Quiz</button>


                        </div>
                        {overallResult && (
    <div className="mt-6 text-left border-t pt-5">

        <h3 className="text-lg font-bold mb-4 text-center">
            Overall Performance
        </h3>

        <div className="space-y-3 text-sm">

            <div>
                <span className="font-semibold">Total Score:</span>{" "}
                {overallResult.total_score}
            </div>

            <div>
                <span className="font-semibold">Percentage:</span>{" "}
                {overallResult.percentage}%
            </div>

            <div>
                <span className="font-semibold">Grade:</span>{" "}
                {overallResult.grade}
            </div>

            <div>
                <span className="font-semibold">Strong Areas:</span>{" "}
                {overallResult.strong_areas?.join(", ")}
            </div>

            <div>
                <span className="font-semibold">Weak Areas:</span>{" "}
                {overallResult.weak_areas?.join(", ")}
            </div>

            <div>
                <span className="font-semibold">Feedback:</span>
                <p className="mt-1 text-gray-600 dark:text-gray-300">
                    {overallResult.overall_feedback}
                </p>
            </div>

            <div>
                <span className="font-semibold">Study Tip:</span>
                <p className="mt-1 text-gray-600 dark:text-gray-300">
                    {overallResult.study_tip}
                </p>
            </div>

        </div>
    </div>
)}
                    </div>

                </div>
            </>
        );
    }
    // Show loading while fetching AI questions
if (loading) {
    return (
        <div className="text-center mt-20">
            Generating Questions...
        </div>
    );
}

    // Active quiz
    return (
        <>
           <Head title="Practice Quiz" />
            <div>
                <div className="flex items-center justify-between mb-6">
                    <div className="flex items-center gap-3">
                        <button onClick={resetToMode} className="w-10 h-10 bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-600 flex items-center justify-center hover:bg-gray-50 dark:hover:bg-gray-700 transition">
                            <i className="fa-solid fa-chevron-left text-gray-600 dark:text-gray-300 text-sm" />
                        </button>
                        <div>
                            <h2 className="text-lg font-bold text-gray-800 dark:text-white">{mode === 'mcq' ? 'MCQ' : mode === 'short' ? 'Short Questions' : 'Long Questions'}</h2>
                            <p className="text-xs text-gray-400 dark:text-gray-500">Question {currentQ + 1} of {questions.length}</p>
                        </div>
                    </div>
                    <div className="hidden sm:flex items-center gap-3">
                        <div className="w-32 bg-gray-100 dark:bg-gray-700 rounded-full h-2">
                            <div className="bg-gradient-to-r from-[#2563EB] to-[#3B82F6] h-2 rounded-full transition-all duration-500" style={{ width: `${(currentQ / questions.length) * 100}%` }} />
                        </div>
                        <span className="text-xs font-semibold text-gray-500 dark:text-gray-400">{Math.round((currentQ / questions.length) * 100)}%</span>
                    </div>
                </div>


{questions[currentQ] && mode === 'mcq' && (
    <QuestionCard
        {...questions[currentQ]}
        onNext={handleNext}
        onAnswer={(index: number) => {
            const updated = [...mcqAnswers];
            updated[currentQ] = index;
            setMcqAnswers(updated);
        }}
    />
)}

{questions[currentQ] && (mode === 'short' || mode === 'long') && (
    <div className="bg-white dark:bg-gray-800 p-6 rounded-xl border">
        <h3 className="text-lg font-semibold mb-4">
            {questions[currentQ].question}
        </h3>

        <textarea
            className="w-full border rounded-lg p-3 text-sm dark:bg-gray-700"
            rows={mode === 'long' ? 6 : 3}
            placeholder="Write your answer..."
            value={userAnswers[currentQ] || ""}
            onChange={(e) => {
                const updated = [...userAnswers];
                updated[currentQ] = e.target.value;
                setUserAnswers(updated);
            }}
        />
        {feedbacks[currentQ] && (
    <div className="mt-4 p-3 bg-blue-50 dark:bg-blue-900/30 rounded-lg border">
        <h4 className="font-semibold text-sm mb-1">AI Feedback</h4>
        <p className="text-sm">{feedbacks[currentQ]}</p>
    </div>
)}

        <div className="mt-4 flex gap-3">
    {!checked ? (
        <button
            onClick={handleCheckAnswer}
            disabled={loadingEval}
            className="bg-blue-500 text-white px-4 py-2 rounded-lg"
        >
            {loadingEval ? "Checking..." : "Check Answer"}
        </button>
    ) : (
        <button
            onClick={handleNext}
            className="bg-green-500 text-white px-4 py-2 rounded-lg"
        >
            Next Question
        </button>
    )}
</div>
    </div>
)}
            </div>
        </>
    );
}

Practice.layout = (page: React.ReactNode) => <StudentLayout currentPage="practice">{page}</StudentLayout>;
