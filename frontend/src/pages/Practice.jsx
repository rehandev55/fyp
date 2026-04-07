import { useState } from "react";
import QuestionCard from "../components/QuestionCard";

const chaptersData = {
  Physics: ["Measurements", "Kinematics", "Dynamics", "Work & Energy", "Waves", "Light", "Electricity", "Magnetism"],
  Chemistry: ["Fundamentals of Chemistry", "Atomic Structure", "Periodic Table", "Chemical Bonding", "States of Matter", "Solutions", "Chemical Reactions", "Acids, Bases & Salts"],
  Biology: ["Introduction to Biology", "Cell Structure", "Cell Division", "Enzymes", "Nutrition", "Transport", "Breathing", "Ecosystem"],
  Mathematics: ["Real Numbers", "Polynomials", "Linear Equations", "Quadratic Equations", "Geometry", "Trigonometry", "Statistics", "Probability"],
  English: ["Comprehension", "Grammar Basics", "Tenses", "Narration", "Voice", "Vocabulary", "Essay Writing", "Letter Writing"],
};

const questionBank = {
  Physics: {
    mcq: [
      { chapter: "Measurements", question: "What is the SI unit of force?", options: ["Joule", "Newton", "Watt", "Pascal"], correctAnswer: 1, explanation: "The SI unit of force is Newton (N), named after Sir Isaac Newton." },
      { chapter: "Kinematics", question: "What is the acceleration due to gravity on Earth?", options: ["9.8 m/s²", "10.8 m/s²", "8.9 m/s²", "11.2 m/s²"], correctAnswer: 0, explanation: "The standard acceleration due to gravity on Earth's surface is approximately 9.8 m/s²." },
      { chapter: "Dynamics", question: "Which law states that F = ma?", options: ["Newton's First Law", "Newton's Second Law", "Newton's Third Law", "Law of Gravitation"], correctAnswer: 1, explanation: "Newton's Second Law of Motion states that Force equals mass times acceleration." },
      { chapter: "Work & Energy", question: "What is the unit of energy?", options: ["Newton", "Joule", "Watt", "Pascal"], correctAnswer: 1, explanation: "The SI unit of energy is Joule (J)." },
      { chapter: "Waves", question: "What type of wave is sound?", options: ["Transverse", "Longitudinal", "Electromagnetic", "Surface"], correctAnswer: 1, explanation: "Sound waves are longitudinal waves that travel through a medium." },
      { chapter: "Light", question: "What is the speed of light in vacuum?", options: ["3 × 10⁶ m/s", "3 × 10⁸ m/s", "3 × 10¹⁰ m/s", "3 × 10⁴ m/s"], correctAnswer: 1, explanation: "The speed of light in vacuum is approximately 3 × 10⁸ m/s." },
      { chapter: "Electricity", question: "What is the unit of electric current?", options: ["Volt", "Ohm", "Ampere", "Watt"], correctAnswer: 2, explanation: "The SI unit of electric current is Ampere (A)." },
      { chapter: "Magnetism", question: "Which material is magnetic?", options: ["Copper", "Aluminium", "Iron", "Gold"], correctAnswer: 2, explanation: "Iron is a ferromagnetic material and is strongly attracted to magnets." },
    ],
    short: [
      { chapter: "Measurements", question: "Define the term 'base unit'.", answer: "A base unit is a fundamental unit of measurement defined by the International System of Units (SI) that cannot be derived from other units. Examples: meter, kilogram, second.", explanation: "There are 7 SI base units from which all other units are derived." },
      { chapter: "Kinematics", question: "What is the difference between speed and velocity?", answer: "Speed is a scalar quantity that measures how fast an object moves, while velocity is a vector quantity that includes both speed and direction of motion.", explanation: "An object moving in a circle at constant speed has changing velocity because its direction changes." },
      { chapter: "Dynamics", question: "Define Newton's First Law of Motion.", answer: "An object at rest stays at rest, and an object in motion stays in motion unless acted upon by an unbalanced external force.", explanation: "Newton's First Law is also known as the Law of Inertia." },
      { chapter: "Work & Energy", question: "Define kinetic energy.", answer: "Kinetic energy is the energy possessed by an object due to its motion. It is calculated as KE = ½mv², where m is mass and v is velocity.", explanation: "Kinetic energy depends on both mass and the square of velocity." },
      { chapter: "Waves", question: "Define wavelength.", answer: "Wavelength is the distance between two consecutive points in phase on a wave, such as two adjacent crests or troughs.", explanation: "Wavelength is denoted by the Greek letter lambda (λ) and is measured in meters." },
      { chapter: "Electricity", question: "State Ohm's Law.", answer: "Ohm's Law states that the current flowing through a conductor is directly proportional to the voltage across it, provided the temperature remains constant. V = IR.", explanation: "V is voltage, I is current, and R is resistance." },
    ],
    long: [
      { chapter: "Dynamics", question: "Explain Newton's three laws of motion with examples.", answer: "First Law (Inertia): An object remains at rest or in uniform motion unless acted upon by an external force. Example: A ball on a table stays still until pushed. Second Law (F=ma): The force on an object equals its mass times acceleration. Example: Pushing a heavier cart requires more force. Third Law (Action-Reaction): For every action there is an equal and opposite reaction. Example: A rocket pushes gas downward and the gas pushes the rocket upward.", explanation: "These three laws form the foundation of classical mechanics." },
      { chapter: "Work & Energy", question: "Explain the law of conservation of energy with examples.", answer: "The law of conservation of energy states that energy cannot be created or destroyed, only transformed from one form to another. The total energy of an isolated system remains constant. Example: A falling ball converts potential energy to kinetic energy. At a hydroelectric dam, water's potential energy converts to kinetic energy, then to electrical energy. In a pendulum, energy continuously converts between potential and kinetic forms.", explanation: "This is one of the fundamental laws of physics applicable to all physical and chemical processes." },
      { chapter: "Light", question: "Explain the phenomenon of refraction of light.", answer: "Refraction is the bending of light when it passes from one medium to another of different optical density. When light enters a denser medium (e.g., air to glass), it bends toward the normal and slows down. When it enters a less dense medium (e.g., glass to air), it bends away from the normal. Snell's Law governs this: n₁ sin θ₁ = n₂ sin θ₂. Examples include the apparent bending of a stick in water, formation of rainbows, and how lenses work.", explanation: "Refraction occurs because light travels at different speeds in different media." },
    ],
  },
  Chemistry: {
    mcq: [
      { chapter: "Fundamentals of Chemistry", question: "What is the chemical formula of water?", options: ["CO₂", "H₂O", "NaCl", "O₂"], correctAnswer: 1, explanation: "Water is composed of two hydrogen atoms and one oxygen atom: H₂O." },
      { chapter: "Atomic Structure", question: "What is the charge of an electron?", options: ["Positive", "Negative", "Neutral", "Variable"], correctAnswer: 1, explanation: "An electron carries a negative charge of -1.6 × 10⁻¹⁹ coulombs." },
      { chapter: "Periodic Table", question: "How many groups are in the modern periodic table?", options: ["7", "8", "16", "18"], correctAnswer: 3, explanation: "The modern periodic table has 18 groups (vertical columns)." },
      { chapter: "Chemical Bonding", question: "What type of bond is formed by sharing electrons?", options: ["Ionic", "Covalent", "Metallic", "Hydrogen"], correctAnswer: 1, explanation: "A covalent bond is formed when atoms share pairs of electrons." },
      { chapter: "Acids, Bases & Salts", question: "What is the pH of a neutral solution?", options: ["0", "7", "14", "1"], correctAnswer: 1, explanation: "A neutral solution has a pH of 7." },
    ],
    short: [
      { chapter: "Atomic Structure", question: "Define atomic number.", answer: "The atomic number (Z) is the number of protons found in the nucleus of an atom.", explanation: "It determines the element's identity and its position in the periodic table." },
      { chapter: "Chemical Bonding", question: "What is an ionic bond?", answer: "An ionic bond is formed by the complete transfer of one or more electrons from one atom to another, creating oppositely charged ions that attract each other.", explanation: "Ionic bonds typically form between metals and non-metals." },
      { chapter: "Solutions", question: "Define a saturated solution.", answer: "A saturated solution is one that contains the maximum amount of solute that can dissolve in a given amount of solvent at a specific temperature.", explanation: "Adding more solute to a saturated solution will not dissolve further." },
    ],
    long: [
      { chapter: "Atomic Structure", question: "Explain Bohr's atomic model and its postulates.", answer: "Bohr proposed that electrons orbit the nucleus in fixed circular paths called energy levels or shells (K, L, M, N). Electrons in each shell have a fixed energy. Electrons can jump between shells by absorbing or emitting a specific amount of energy (quantum). The energy of a shell increases with distance from the nucleus. The angular momentum of electrons is quantized: mvr = nh/2π.", explanation: "Bohr's model successfully explained the hydrogen spectrum but had limitations for multi-electron atoms." },
      { chapter: "Chemical Reactions", question: "Explain the types of chemical reactions with examples.", answer: "1. Combination: Two or more substances combine to form one product (2H₂ + O₂ → 2H₂O). 2. Decomposition: A compound breaks into simpler substances (2H₂O → 2H₂ + O₂). 3. Single displacement: One element replaces another in a compound (Zn + CuSO₄ → ZnSO₄ + Cu). 4. Double displacement: Exchange of ions between two compounds (NaCl + AgNO₃ → AgCl + NaNO₃). 5. Combustion: Substance reacts with oxygen releasing heat and light (CH₄ + 2O₂ → CO₂ + 2H₂O).", explanation: "Identifying reaction types helps predict products and balance equations." },
    ],
  },
  Biology: {
    mcq: [
      { chapter: "Cell Structure", question: "Which organelle is known as the powerhouse of the cell?", options: ["Nucleus", "Ribosome", "Mitochondria", "Golgi Apparatus"], correctAnswer: 2, explanation: "Mitochondria produce ATP through cellular respiration." },
      { chapter: "Introduction to Biology", question: "What is the basic unit of life?", options: ["Tissue", "Organ", "Cell", "Organism"], correctAnswer: 2, explanation: "The cell is the smallest structural and functional unit of living organisms." },
      { chapter: "Ecosystem", question: "Which gas is most abundant in Earth's atmosphere?", options: ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], correctAnswer: 2, explanation: "Nitrogen makes up about 78% of Earth's atmosphere." },
      { chapter: "Nutrition", question: "What is the role of chlorophyll in photosynthesis?", options: ["Absorb water", "Absorb light energy", "Release CO₂", "Store glucose"], correctAnswer: 1, explanation: "Chlorophyll absorbs light energy needed to drive the photosynthesis reaction." },
      { chapter: "Cell Division", question: "How many chromosomes do human body cells have?", options: ["23", "44", "46", "48"], correctAnswer: 2, explanation: "Human body (somatic) cells contain 46 chromosomes (23 pairs)." },
    ],
    short: [
      { chapter: "Nutrition", question: "What is photosynthesis?", answer: "Photosynthesis is the process by which green plants convert light energy, water, and CO₂ into glucose and oxygen.", explanation: "The equation: 6CO₂ + 6H₂O + light energy → C₆H₁₂O₆ + 6O₂." },
      { chapter: "Cell Structure", question: "What is the function of the cell membrane?", answer: "The cell membrane is a selectively permeable barrier that controls the movement of substances in and out of the cell, maintains cell shape, and protects internal organelles.", explanation: "It is composed of a phospholipid bilayer with embedded proteins." },
      { chapter: "Enzymes", question: "What are enzymes?", answer: "Enzymes are biological catalysts (proteins) that speed up chemical reactions in living organisms without being consumed in the reaction.", explanation: "Enzymes are specific to their substrates and work best at optimal temperature and pH." },
    ],
    long: [
      { chapter: "Transport", question: "Explain the structure and function of the human heart.", answer: "The human heart is a muscular organ with four chambers: two atria (upper) and two ventricles (lower). The right atrium receives deoxygenated blood from the body via the vena cava and passes it to the right ventricle, which pumps it to the lungs for oxygenation. The left atrium receives oxygenated blood from the lungs via pulmonary veins and passes it to the left ventricle, which pumps it to the entire body through the aorta. Valves between chambers prevent backflow of blood.", explanation: "The heart functions as a double pump — the right side handles pulmonary circulation and the left side handles systemic circulation." },
      { chapter: "Transport", question: "Describe the process of osmosis with examples.", answer: "Osmosis is the movement of water molecules through a semipermeable membrane from a region of lower solute concentration to a region of higher solute concentration. This process continues until equilibrium is reached. Examples include: plant roots absorbing water from the soil, red blood cells swelling in a hypotonic solution, and wilting of plants when placed in a hypertonic solution.", explanation: "Osmosis is a special case of diffusion that applies specifically to water/solvent molecules across a semipermeable membrane." },
    ],
  },
  Mathematics: {
    mcq: [
      { chapter: "Real Numbers", question: "Which of the following is an irrational number?", options: ["3/4", "√2", "0.5", "7"], correctAnswer: 1, explanation: "√2 cannot be expressed as a simple fraction, making it irrational." },
      { chapter: "Quadratic Equations", question: "What is the discriminant of ax² + bx + c = 0?", options: ["b² + 4ac", "b² - 4ac", "2a", "b/2a"], correctAnswer: 1, explanation: "The discriminant D = b² - 4ac determines the nature of roots." },
      { chapter: "Trigonometry", question: "What is sin(90°)?", options: ["0", "1", "½", "√2/2"], correctAnswer: 1, explanation: "Sin(90°) = 1 is a standard trigonometric value." },
      { chapter: "Geometry", question: "What is the sum of angles in a triangle?", options: ["90°", "180°", "270°", "360°"], correctAnswer: 1, explanation: "The sum of all interior angles of a triangle is always 180°." },
      { chapter: "Probability", question: "What is the probability of getting heads in a fair coin toss?", options: ["0", "0.25", "0.5", "1"], correctAnswer: 2, explanation: "A fair coin has two equally likely outcomes, so P(heads) = 1/2 = 0.5." },
    ],
    short: [
      { chapter: "Polynomials", question: "Define a polynomial.", answer: "A polynomial is an algebraic expression consisting of variables and coefficients, involving only addition, subtraction, multiplication, and non-negative integer exponents. Example: 3x² + 2x - 5.", explanation: "The degree of a polynomial is the highest power of the variable." },
      { chapter: "Linear Equations", question: "What is a linear equation?", answer: "A linear equation is an equation of the first degree, meaning the highest power of the variable is 1. Its general form is ax + b = 0, and its graph is a straight line.", explanation: "Linear equations have exactly one solution." },
      { chapter: "Statistics", question: "Define the mean of a dataset.", answer: "The mean (average) is the sum of all values in a dataset divided by the total number of values. Mean = Σx / n.", explanation: "The mean is a measure of central tendency." },
    ],
    long: [
      { chapter: "Quadratic Equations", question: "Explain the quadratic formula and how to determine the nature of roots.", answer: "For a quadratic equation ax² + bx + c = 0, the solutions are given by x = (-b ± √(b²-4ac)) / 2a. The discriminant D = b² - 4ac determines the nature of roots: If D > 0, two distinct real roots. If D = 0, two equal real roots. If D < 0, two complex conjugate roots (no real solutions). Example: For x² - 5x + 6 = 0, D = 25-24 = 1 > 0, so two distinct real roots: x = 2 and x = 3.", explanation: "The quadratic formula works for all quadratic equations, unlike factoring which only works in specific cases." },
      { chapter: "Trigonometry", question: "Prove that sin²θ + cos²θ = 1.", answer: "Consider a right triangle with hypotenuse r, opposite side y, and adjacent side x. By Pythagoras: x² + y² = r². Dividing both sides by r²: (x/r)² + (y/r)² = 1. Since cosθ = x/r and sinθ = y/r: cos²θ + sin²θ = 1. This is the fundamental Pythagorean trigonometric identity and holds for all values of θ.", explanation: "This identity is the basis for deriving other trigonometric identities." },
    ],
  },
  English: {
    mcq: [
      { chapter: "Grammar Basics", question: "Which is a proper noun?", options: ["city", "dog", "London", "river"], correctAnswer: 2, explanation: "London is a proper noun — the specific name of a city. Proper nouns are always capitalized." },
      { chapter: "Tenses", question: "Which sentence is in present perfect tense?", options: ["I go to school.", "I went to school.", "I have gone to school.", "I will go to school."], correctAnswer: 2, explanation: "Present perfect uses 'have/has + past participle'." },
      { chapter: "Voice", question: "Convert to passive: 'She writes a letter.'", options: ["A letter is written by her.", "A letter was written by her.", "A letter has been written.", "A letter is being written."], correctAnswer: 0, explanation: "Simple present active → simple present passive: is/am/are + past participle." },
      { chapter: "Narration", question: "He said, 'I am happy.' In indirect speech:", options: ["He said that I am happy.", "He said that he was happy.", "He said that he is happy.", "He told that he was happy."], correctAnswer: 1, explanation: "Direct to indirect: 'I am' changes to 'he was' (backshift of tense)." },
      { chapter: "Vocabulary", question: "What is the synonym of 'eloquent'?", options: ["Silent", "Articulate", "Confused", "Lazy"], correctAnswer: 1, explanation: "'Eloquent' means fluent and persuasive in speaking or writing, similar to 'articulate'." },
    ],
    short: [
      { chapter: "Comprehension", question: "What is a topic sentence?", answer: "A topic sentence is the first sentence of a paragraph that states the main idea or central point. All other sentences in the paragraph support or elaborate on this topic sentence.", explanation: "A good topic sentence helps the reader understand what the paragraph will discuss." },
      { chapter: "Grammar Basics", question: "Define a pronoun with examples.", answer: "A pronoun is a word used in place of a noun to avoid repetition. Examples: he, she, it, they, we, this, that, who, which. 'Ali is a boy. He goes to school.' — 'He' is a pronoun replacing 'Ali'.", explanation: "Pronouns make sentences less repetitive and more natural." },
      { chapter: "Essay Writing", question: "What are the basic parts of an essay?", answer: "An essay has three basic parts: Introduction (introduces the topic and thesis statement), Body (2-3 paragraphs developing the main points with evidence), and Conclusion (summarizes key points and restates the thesis).", explanation: "Following this structure ensures clear and organized writing." },
    ],
    long: [
      { chapter: "Essay Writing", question: "Write an essay outline on 'Importance of Education'.", answer: "Introduction: Education is the foundation of personal and societal progress. Thesis: Education empowers individuals and transforms communities. Body Para 1: Education develops critical thinking, problem-solving skills, and knowledge. It prepares individuals for careers and self-sufficiency. Body Para 2: Education promotes social awareness, tolerance, and civic responsibility. Educated societies have lower crime rates and better healthcare. Body Para 3: Education drives economic growth, innovation, and technological advancement. Countries with higher literacy rates show stronger GDP growth. Conclusion: Education is not just a right but a necessity for building a better future. Governments must prioritize accessible quality education for all.", explanation: "A well-structured essay presents arguments logically with supporting evidence." },
      { chapter: "Letter Writing", question: "Write a formal letter to the principal requesting a library upgrade.", answer: "To: The Principal, [School Name]. Subject: Request for Library Upgrade. Respected Sir/Madam, I am writing on behalf of the students to respectfully request improvements to our school library. Currently, the library has outdated books and limited seating. We propose: (1) Addition of recent textbooks and reference materials, (2) A digital section with computers for research, (3) Extended library hours. An upgraded library would greatly benefit students' academic performance and encourage a reading culture. We hope you will consider our request. Yours respectfully, [Name], Class [X].", explanation: "Formal letters follow a specific format: address, subject, salutation, body, and closing." },
    ],
  },
};

function Practice({ user, onNavigate }) {
  const [mode, setMode] = useState(null);
  const [currentQ, setCurrentQ] = useState(0);
  const [finished, setFinished] = useState(false);
  const [chapterScope, setChapterScope] = useState(null); // "whole" or "selected"
  const [selectedChapters, setSelectedChapters] = useState([]);

  const hasSelection = user?.classLevel && user?.board && user?.subject;
  const subjectChapters = hasSelection ? (chaptersData[user.subject] || []) : [];

  const getFilteredQuestions = (type) => {
    const subjectBank = questionBank[user?.subject];
    if (!subjectBank || !subjectBank[type]) return [];
    const questions = subjectBank[type];
    if (chapterScope === "whole") return questions;
    return questions.filter((q) => selectedChapters.includes(q.chapter));
  };

  const toggleChapter = (ch) => {
    setSelectedChapters((prev) =>
      prev.includes(ch) ? prev.filter((c) => c !== ch) : [...prev, ch]
    );
  };

  const selectAllChapters = () => {
    if (selectedChapters.length === subjectChapters.length) setSelectedChapters([]);
    else setSelectedChapters([...subjectChapters]);
  };

  const questions = mode ? getFilteredQuestions(mode) : [];
  const handleNext = () => { currentQ < questions.length - 1 ? setCurrentQ(currentQ + 1) : setFinished(true); };
  const reset = () => { setMode(null); setCurrentQ(0); setFinished(false); };
  const fullReset = () => { setMode(null); setCurrentQ(0); setFinished(false); setChapterScope(null); setSelectedChapters([]); };

  const modes = [
    { key: "mcq", label: "MCQ", desc: "Multiple choice questions to test your knowledge", icon: "fa-solid fa-list-check", gradient: "from-blue-500 to-indigo-600" },
    { key: "short", label: "Short Questions", desc: "Brief answer questions for quick review", icon: "fa-solid fa-pen-to-square", gradient: "from-emerald-500 to-teal-600" },
    { key: "long", label: "Long Questions", desc: "Detailed questions for deep understanding", icon: "fa-solid fa-file-lines", gradient: "from-purple-500 to-pink-600" },
  ];

  // Gate: must select class/board/subject first
  if (!hasSelection) return (
    <div className="max-w-md mx-auto text-center">
      <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-10">
        <div className="w-20 h-20 bg-gradient-to-br from-amber-100 to-orange-100 dark:from-amber-900/30 dark:to-orange-900/30 rounded-full flex items-center justify-center mx-auto mb-5">
          <i className="fa-solid fa-circle-exclamation text-amber-500 text-4xl" />
        </div>
        <h2 className="text-xl font-bold text-gray-800 dark:text-white mb-2">Select Your Subject First</h2>
        <p className="text-gray-500 dark:text-gray-400 text-sm mb-6">Please choose your board, class, and subject before starting a practice quiz.</p>
        <button onClick={() => onNavigate("selection")} className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg transition-all duration-200 text-sm font-semibold flex items-center justify-center gap-2">
          Go to Subject Selection <i className="fa-solid fa-arrow-right" />
        </button>
      </div>
    </div>
  );

  // Step 1: Chapter selection
  if (!chapterScope) return (
    <div>
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Practice Quiz</h2>
        <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">
          {user.subject} — Class {user.classLevel} — {user.board}
        </p>
      </div>
      <div className="max-w-2xl mx-auto space-y-5">
        {/* Whole Book option */}
        <button onClick={() => { setChapterScope("whole"); setSelectedChapters([...subjectChapters]); }} className="w-full bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 text-left hover:shadow-lg hover:-translate-y-1 transition-all duration-300 group flex items-center gap-5">
          <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg group-hover:scale-110 transition-transform duration-300">
            <i className="fa-solid fa-book text-white text-xl" />
          </div>
          <div className="flex-1">
            <h3 className="font-bold text-gray-800 dark:text-white text-lg">Whole Book</h3>
            <p className="text-sm text-gray-500 dark:text-gray-400 mt-0.5">Practice questions from all {subjectChapters.length} chapters</p>
          </div>
          <i className="fa-solid fa-chevron-right text-gray-400 group-hover:text-[#2563EB] transition" />
        </button>

        {/* Select Chapters option */}
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
              {selectedChapters.length === subjectChapters.length ? "Deselect All" : "Select All"}
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-5">
            {subjectChapters.map((ch, i) => (
              <button
                key={ch}
                onClick={() => toggleChapter(ch)}
                className={`flex items-center gap-3 px-4 py-3 rounded-xl border-2 text-sm font-medium transition-all duration-200 text-left ${
                  selectedChapters.includes(ch)
                    ? "border-[#2563EB] bg-blue-50 dark:bg-blue-900/30 text-[#2563EB]"
                    : "border-gray-200 dark:border-gray-600 text-gray-600 dark:text-gray-300 hover:border-blue-300 hover:bg-blue-50/50 dark:hover:bg-blue-900/20"
                }`}
              >
                <span className={`w-6 h-6 rounded-md flex items-center justify-center text-xs flex-shrink-0 ${
                  selectedChapters.includes(ch) ? "bg-[#2563EB] text-white" : "bg-gray-100 dark:bg-gray-700 text-gray-400"
                }`}>
                  {selectedChapters.includes(ch) ? (
                    <i className="fa-solid fa-check text-xs" />
                  ) : (i + 1)}
                </span>
                {ch}
              </button>
            ))}
          </div>

          <button
            onClick={() => { if (selectedChapters.length > 0) setChapterScope("selected"); }}
            disabled={selectedChapters.length === 0}
            className="w-full bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg disabled:opacity-40 disabled:cursor-not-allowed disabled:shadow-none transition-all duration-200 text-sm font-semibold flex items-center justify-center gap-2"
          >
            Continue with {selectedChapters.length} chapter{selectedChapters.length !== 1 ? "s" : ""} <i className="fa-solid fa-arrow-right" />
          </button>
        </div>
      </div>
    </div>
  );

  // Step 2: Quiz mode selection
  if (!mode) return (
    <div>
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-white">Practice Quiz</h2>
        <p className="text-gray-400 dark:text-gray-500 text-sm mt-1">
          {user.subject} — {chapterScope === "whole" ? "Whole Book" : `${selectedChapters.length} chapter${selectedChapters.length !== 1 ? "s" : ""}`}
        </p>
      </div>
      <div className="grid gap-5 max-w-2xl mx-auto">
        {modes.map((m) => {
          const count = getFilteredQuestions(m.key).length;
          return (
            <button key={m.key} onClick={() => { if (count > 0) setMode(m.key); }} disabled={count === 0} className={`bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 text-left hover:shadow-lg hover:-translate-y-1 transition-all duration-300 group flex items-center gap-5 ${count === 0 ? "opacity-50 cursor-not-allowed hover:shadow-sm hover:translate-y-0" : ""}`}>
              <div className={`w-14 h-14 bg-gradient-to-br ${m.gradient} rounded-2xl flex items-center justify-center flex-shrink-0 shadow-lg group-hover:scale-110 transition-transform duration-300`}><i className={`${m.icon} text-white text-xl`} /></div>
              <div className="flex-1"><h3 className="font-bold text-gray-800 dark:text-white text-lg">{m.label}</h3><p className="text-sm text-gray-500 dark:text-gray-400 mt-0.5">{m.desc}</p></div>
              <span className={`text-xs px-3 py-1.5 rounded-full font-semibold ${count > 0 ? "bg-blue-50 dark:bg-blue-900/30 text-[#2563EB]" : "bg-gray-100 dark:bg-gray-700 text-gray-400"}`}>{count} Qs</span>
            </button>
          );
        })}
        <button onClick={fullReset} className="text-sm text-gray-500 hover:text-[#2563EB] transition mt-2 flex items-center justify-center gap-1">
          <i className="fa-solid fa-chevron-left text-xs" />
          Change chapters
        </button>
      </div>
    </div>
  );

  // Quiz complete screen
  if (finished) return (
    <div className="max-w-md mx-auto text-center">
      <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 p-10">
        <div className="w-20 h-20 bg-gradient-to-br from-emerald-400 to-teal-500 rounded-full flex items-center justify-center mx-auto mb-5 shadow-lg"><i className="fa-solid fa-check text-white text-3xl" /></div>
        <h2 className="text-2xl font-bold text-gray-800 dark:text-white mb-2">Quiz Complete!</h2>
        <p className="text-gray-500 dark:text-gray-400 mb-6">You completed all {questions.length} questions.</p>
        <div className="flex gap-3">
          <button onClick={() => { setCurrentQ(0); setFinished(false); }} className="flex-1 border-2 border-gray-200 dark:border-gray-600 text-gray-700 dark:text-gray-200 py-3 rounded-xl hover:bg-gray-50 dark:hover:bg-gray-700 transition text-sm font-semibold">Retry</button>
          <button onClick={fullReset} className="flex-1 bg-gradient-to-r from-[#2563EB] to-[#3B82F6] text-white py-3 rounded-xl hover:shadow-lg transition text-sm font-semibold">New Quiz</button>
        </div>
      </div>
    </div>
  );

  // Active quiz
  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <button onClick={reset} className="w-10 h-10 bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-600 flex items-center justify-center hover:bg-gray-50 dark:hover:bg-gray-700 transition"><i className="fa-solid fa-chevron-left text-gray-600 dark:text-gray-300 text-sm" /></button>
          <div><h2 className="text-lg font-bold text-gray-800 dark:text-white">{mode === "mcq" ? "MCQ" : mode === "short" ? "Short Questions" : "Long Questions"}</h2><p className="text-xs text-gray-400 dark:text-gray-500">Question {currentQ + 1} of {questions.length}</p></div>
        </div>
        <div className="hidden sm:flex items-center gap-3">
          <div className="w-32 bg-gray-100 dark:bg-gray-700 rounded-full h-2"><div className="bg-gradient-to-r from-[#2563EB] to-[#3B82F6] h-2 rounded-full transition-all duration-500" style={{ width: `${((currentQ + 1) / questions.length) * 100}%` }} /></div>
          <span className="text-xs font-semibold text-gray-500 dark:text-gray-400">{Math.round(((currentQ + 1) / questions.length) * 100)}%</span>
        </div>
      </div>
      <QuestionCard {...questions[currentQ]} onNext={handleNext} />
    </div>
  );
}

export default Practice;
