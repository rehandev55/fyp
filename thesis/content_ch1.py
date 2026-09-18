"""Content blocks for Chapter 1 - Introduction."""

BLOCKS = [('chapter', 'CHAPTER 1', 'INTRODUCTION'),
 ('p',
  'This chapter introduces the project. It explains the problem that '
  'Pakistani school students face when they study for board examinations, '
  'gives the evidence collected from students themselves, states the aim and '
  'objectives of the work, sets the scope, and describes how the rest of the '
  'report is organised.'),
 ('h2', '1.1  OVERVIEW'),
 ('p',
  'School education in Pakistan is built around examination boards. A '
  'student in Mirpur takes a paper set by the Azad Jammu and Kashmir Board '
  'of Intermediate and Secondary Education. A student in Islamabad takes a '
  'paper set by the Federal Board of Intermediate and Secondary Education. '
  'The two boards prescribe different textbooks. They order chapters '
  'differently, give different weight to topics, and ask questions in '
  'different styles. For the four years that shape a young person’s future, '
  'classes nine to twelve, the board is not a small administrative detail '
  '(Ministry of Federal Education 2022; Federal Board of Intermediate and '
  'Secondary Education 2024). It is the single most important factor in what '
  'a student must learn and how they will be marked.'),
 ('p',
  'The digital help available to those students is not organised in the same '
  'way. A search engine returns pages written for the Punjab syllabus, an '
  'Indian syllabus, or no syllabus at all. Video sites host lectures of '
  'unknown origin. Since 2023, a growing number of students have turned to '
  'general chatbots such as ChatGPT. These tools answer fluently, but they '
  'answer from the whole internet rather than from the book the student will '
  'be examined on. They cannot say which questions have appeared in a '
  'particular board’s papers. They write long, flowing prose where the '
  'marking scheme rewards three short sentences. They also state wrong facts '
  'with complete confidence. The research literature calls this '
  'hallucination. It is especially harmful when the reader is a '
  'fifteen-year-old who has no way to detect it.'),
 ('p',
  'This project attacks that gap directly. Eternal Sunshine is a web '
  'platform for learning, testing and study resources. Its central design '
  'promise is simple. Every sentence the artificial intelligence produces '
  'for a student is grounded in the real textbooks, keybooks and past papers '
  'of that student’s own board, class and subject. The promise is kept by '
  'the architecture, not by an instruction in a prompt. The model is never '
  'asked a question until it has first been handed passages retrieved from a '
  'vector index that is filtered, at query time, on the student’s board, '
  'class and subject. The same grounded pipeline drives three abilities: '
  'explanation, question generation and answer marking. A student can '
  'therefore learn a topic, be tested on it in the style of their own board, '
  'and receive a mark with useful feedback, all from one curated set of '
  'books.'),
 ('fig',
  'fig_architecture.png',
  'Layered architecture of the Eternal Sunshine platform.',
  6.0),
 ('h2', '1.2  BACKGROUND AND MOTIVATION'),
 ('h3', '1.2.1  The examination-centred reality of Pakistani schooling'),
 ('p',
  'In practice, Pakistani secondary education is an examination-preparation '
  'exercise. Entry to a professional degree in medicine, engineering or '
  'computer science is decided almost entirely by the marks obtained in the '
  'Class 10 and Class 12 board examinations. This puts heavy pressure on a '
  'narrow set of skills. A student must reproduce textbook definitions '
  'accurately, organise a long answer under the headings an examiner '
  'expects, and recognise the question patterns that a particular board '
  'repeats. Students who can afford a tuition academy buy exactly this. They '
  'get a tutor who knows the board, knows the paper and drills the pattern. '
  'Students who cannot afford tuition are left with a textbook and a guess '
  'paper.'),
 ('p',
  'The result is a problem of fairness rather than a problem of content. The '
  'textbooks exist. The past papers exist. What is scarce and expensive is '
  'the guidance that joins them together. Someone has to explain a concept '
  'in the words the book uses, say which questions matter, and mark an '
  'attempt honestly. That guidance layer is exactly what a well-grounded '
  'language model can supply, at a running cost measured in fractions of a '
  'cent.'),
 ('h3', '1.2.2  Why general chatbots are not enough'),
 ('p',
  'During requirement gathering, students who said they used ChatGPT for '
  'study were asked what frustrated them about it. Twenty-six of the '
  'forty-five students who answered this question reported a concrete '
  'problem. Their answers group into a small number of themes, and each '
  'theme maps onto a known technical limit of general language models.'),
 ('bullets',
  [['Answers are too long and not shaped for an exam. ',
    'Eleven students said the answers were lengthy or padded. A model tuned '
    'to be helpful writes a full essay. A board examiner gives three marks '
    'for three specific points. The student is left to do the shortening, '
    'which is the very skill they have not yet learned.'],
   ['The wording is too difficult. ',
    'Seven students said the language was hard, or pitched above their '
    'level. One wrote that the model gives "high level answers that not '
    'suits college level students". A tutor has to match the reading level '
    'of the book in front of the student.'],
   ['Answers are sometimes wrong or off the point. ',
    'Seven students reported wrong, vague or unrelated answers. '
    'Hallucination in open-domain generation is well documented. In a study '
    'setting the damage is one-sided. A student who cannot judge the answer '
    'will memorise the error.']]),
 ('p',
  'Retrieval-Augmented Generation, introduced by Lewis and colleagues in '
  '2020 (2020), answers all three complaints. The system fetches relevant '
  'passages from a trusted set of documents and places them in the model’s '
  'context before it writes anything. This keeps the answer tied to material '
  'the system can point at, shortens it because the source is explicit, and '
  'greatly narrows the space in which the model can invent. The central idea '
  'of this project is that the trusted corpus for a Pakistani board student '
  'is not the internet. It is a shelf of eight or ten specific books.'),
 ('h3', '1.2.3  Evidence from the requirement survey'),
 ('p',
  'Before any architecture was fixed, a structured survey was given to '
  'students of classes nine to twelve. Forty-eight complete responses were '
  'received. The full results appear in Chapter 3 and in Appendix B. Five '
  'findings shaped the whole design.'),
 ('numbers',
  ['Students study mostly on their own. 45.8 per cent study mainly at home '
   'and 41.7 per cent at school, so the product must work without a teacher '
   'standing beside the student.',
   'The main need is conceptual. 52.1 per cent need help with understanding '
   'concepts and a further 37.5 per cent need help with both concepts and '
   'question practice. This is why the system provides a teacher agent and a '
   'tester agent rather than only one of them.',
   'Students already reach for artificial intelligence without being told '
   'to. 75 per cent said they use ChatGPT, and it was the second most common '
   'response to the question of what they do when a topic is unclear.',
   'Board material and online material do not match. 50 per cent said there '
   'is a difference between board examination content and online study '
   'material, and a further 29.2 per cent said there is sometimes a '
   'difference. Only 20.8 per cent saw no difference. This is the strongest '
   'single piece of evidence for the premise of the project.',
   'Official material is hard to find. 52.1 per cent said they do download '
   'past papers and textbooks but find them difficult to locate, which is '
   'the reason the platform includes a filtered resource library.']),
 ('p',
  'Two further results confirmed the shape of the product. 79.2 per cent '
  'said an application that gave questions and explanations based on their '
  'own board syllabus would help them, against 4.2 per cent who said it '
  'would not. The same share, 79.2 per cent, said a chatbot that tests them, '
  'shows their mistakes and explains the correct answer would help them '
  'learn better.'),
 ('fig',
  'fig_survey_boardvsonline.png',
  'Reported mismatch between board content and online material (n = 48).',
  5.2),
 ('h2', '1.3  PROBLEM STATEMENT'),
 ('p',
  'Students of classes nine to twelve in Pakistan prepare for board-specific '
  'examinations using digital tools that are not board-specific. The '
  'material returned by search engines, video sites and general chatbots is '
  'not aligned with the textbook the student owns. It cannot tell one '
  'board’s question patterns from another’s. It is not shaped to the marking '
  'scheme the student will be judged against. It also carries an unmeasured '
  'risk of factual error. The guidance that would fix all of this is a tutor '
  'who explains from the prescribed book, sets questions in the board’s own '
  'style and marks honestly. That guidance is available only through private '
  'tuition, which a large share of students cannot afford.'),
 ('p',
  'No existing system combines board-filtered curricular grounding, '
  'conversational explanation, automatic generation of board-styled practice '
  'questions and automatic marking of written answers in a single platform '
  'that a student can reach with a browser. The absence of such a system '
  'keeps an unfairness in place that is economic in origin but technical in '
  'remedy.'),
 ('p',
  'This project therefore addresses the following problem. How can a large '
  'language model be constrained, at acceptable cost and acceptable speed, '
  'to teach, examine and mark strictly within the syllabus of a named '
  'Pakistani examination board, class and subject? And how can that ability '
  'be delivered through a secure, maintainable and usable web application?'),
 ('h2', '1.4  AIM AND OBJECTIVES'),
 ('h3', '1.4.1  Aim'),
 ('p',
  'To design, build, test and evaluate an intelligent, board-specific web '
  'platform that lets Pakistani students of classes nine to twelve learn, '
  'practise and be assessed in their school subjects, using artificial '
  'intelligence that is verifiably grounded in their own curriculum.'),
 ('h3', '1.4.2  Objectives'),
 ('p',
  'The aim was broken into the measurable objectives listed in Table 1.1. '
  'Each one is revisited in Section 8.9, where the degree of achievement is '
  'judged against evidence.'),
 ('table',
  'Project objectives and where each is addressed',
  ['ID', 'Objective', 'Addressed in'],
  [['O1',
    'Make board, class and subject the scope that drives every piece of '
    'content the student sees.',
    'Chapters 3, 5, 6'],
   ['O2',
    'Build an offline ingestion pipeline that turns scanned board material '
    'into a metadata-tagged vector index.',
    'Chapters 4, 6, 8'],
   ['O3',
    'Provide a retriever that applies board, class and subject as a hard '
    'filter during the search, not as a request in a prompt.',
    'Chapters 4, 7, 8'],
   ['O4',
    'Provide a teacher agent that explains in exam language, supports '
    'English and Urdu, and is honest about what the corpus does not cover.',
    'Chapters 4, 6, 8'],
   ['O5',
    'Provide a tester agent that writes board-styled items and labels each '
    'one with its source.',
    'Chapters 4, 6, 8'],
   ['O6',
    'Provide an evaluator that marks written answers to the board scheme of '
    'one, three and eight marks.',
    'Chapters 4, 6, 8'],
   ['O7',
    'Aggregate a practice session into a grade, strong and weak topics and a '
    'study recommendation.',
    'Chapters 5, 6, 8'],
   ['O8',
    'Deliver a filtered resource library with download accounting.',
    'Chapters 5, 6, 7'],
   ['O9',
    'Deliver a progress dashboard with subject-wise analysis.',
    'Chapters 5, 6, 8'],
   ['O10',
    'Deliver an administrative console behind role-based access.',
    'Chapters 5, 6, 7'],
   ['O11',
    'Contain and measure the operating cost of the artificial-intelligence '
    'tier.',
    'Chapters 4, 6, 8'],
   ['O12',
    'Verify the system by automated, integration, system and acceptance '
    'testing, and evaluate the retrieval and language-model layers directly.',
    'Chapters 7, 8']],
  [0.55, 3.55, 1.3],
  10),
 ('h2', '1.5  SCOPE OF THE PROJECT'),
 ('h3', '1.5.1  In scope'),
 ('p',
  'The delivered system models two examination boards, Federal and Azad '
  'Jammu and Kashmir, four class levels from nine to twelve, and seven '
  'subjects: Physics, Chemistry, Biology, Mathematics, English, Computer '
  'Science and Urdu. This gives 28 class-and-subject combinations and a '
  'curriculum map of 379 named chapters. Within that scope the platform '
  'provides account management with email verification, Google sign-in and '
  'optional two-factor authentication; an academic profile; a conversational '
  'tutor with saved, summarised session memory and voice input; '
  'chapter-scoped practice generation in three question formats; automatic '
  'marking and session-level evaluation; a resource library; a progress '
  'dashboard; and an administrative console.'),
 ('note',
  'The board, class and subject model supports both boards, and the '
  'interface offers both. The indexed corpus delivered with this project '
  'covers the Federal Board only, across 27 class-and-subject combinations '
  'and 8,057 chunks. Adding the AJK Board is a data-ingestion task rather '
  'than a code change, because the ingestion scripts, the metadata schema '
  'and the retrieval filter already carry the board field. Section 8.2 '
  'reports the measured corpus and Section 9.5 states this as a limitation.',
  'Scope of the indexed corpus'),
 ('h3', '1.5.2  Out of scope'),
 ('p',
  'The following were left out on purpose, either because they were beyond '
  'the time available or because they bring duties the project cannot '
  'responsibly meet. They are revisited as future work in Section 9.6.'),
 ('bullets',
  [['Native mobile applications. ',
    'The interface is responsive and works in a mobile browser, but no '
    'Android or iOS package is produced.'],
   ['Spoken replies. ',
    'Voice input is delivered, using the browser speech-recognition '
    'interface, so a student can dictate a question. The system does not '
    'read its answers aloud.'],
   ['Offline operation. ',
    'Both retrieval and generation need network access to third-party '
    'services.'],
   ['Boards beyond Federal and AJK. ',
    'The Punjab, Sindh, Khyber Pakhtunkhwa and Balochistan boards are '
    'supported by the design. Adding one is a data-ingestion exercise, not a '
    'change to the code.'],
   ['Redistribution of copyrighted material. ',
    'Only documents that are already lawfully and publicly available are '
    'offered for download. The indexed corpus is used for retrieval only and '
    'is never served back as a whole document.'],
   ['Teacher and parent portals. ',
    'The system models two roles, student and administrator. Classroom '
    'management is not addressed.']]),
 ('h2', '1.6  SIGNIFICANCE AND CONTRIBUTIONS'),
 ('p',
  'The contribution of this project is not the invention of '
  'Retrieval-Augmented Generation, and it is not the training of a new '
  'model. It is the demonstration that a carefully engineered retrieval '
  'layer over a small, deliberately chosen corpus can turn a cheap '
  'general-purpose model into a credible subject tutor for a curriculum that '
  'no commercial provider serves. The specific contributions are listed '
  'below.'),
 ('numbers',
  ['A board, class and subject filtered retrieval design in which curricular '
   'scoping is a hard constraint on the vector query rather than a request '
   'made in a prompt. Section 8.3 shows this filter holding at a measured '
   'precision of 1.00 over sixty inspected passages, with no leakage across '
   'boards or classes.',
   'An ingestion pipeline tuned to the particular noise found in Pakistani '
   'board material: scanned pages that need optical character recognition, '
   'running headers, watermarks and examination-paper furniture.',
   'A three-agent split into teacher, tester and evaluator that shares one '
   'retrieval layer but differs in prompt, temperature and token budget, '
   'showing that one model can be specialised by configuration rather than '
   'by training.',
   'A labelling scheme for generated questions that separates items taken '
   'from past papers, items modelled on past-paper style, and items newly '
   'written from the textbook.',
   'A conversation-memory strategy that bounds prompt growth, so the '
   'per-turn cost of a tutoring session stays roughly constant instead of '
   'rising with its length. Section 8.6 measures the saving.',
   'Per-call token and cost instrumentation that turns the economics of the '
   'system into a measured, engineered property. This is a precondition for '
   'any claim that the platform is affordable at scale.',
   'A reproducible evaluation harness for the retrieval and language-model '
   'layers, reported in Chapters 7 and 8, which tests grounding, marking '
   'accuracy, question validity and prompt growth against recorded baselines '
   'rather than by demonstration alone.']),
 ('h2', '1.7  ALIGNMENT WITH THE SUSTAINABLE DEVELOPMENT GOALS'),
 ('p',
  'The project was mapped against the United Nations Sustainable Development '
  'Goals during the proposal phase. The mapping is repeated here with the '
  'delivered features that realise each goal, so that the claim can be '
  'checked rather than merely asserted.'),
 ('table',
  'Sustainable Development Goals and the features that meet them',
  ['SDG', 'Goal', 'How the delivered system contributes'],
  [['SDG 4',
    'Quality Education',
    'Free, board-aligned explanation, practice and marking for classes nine '
    'to twelve, available to any student with a browser.'],
   ['SDG 10',
    'Reduced Inequalities',
    'Supplies the guidance layer that is otherwise bought through private '
    'tuition, at a running cost of well under one cent per exchange.'],
   ['SDG 9',
    'Industry, Innovation and Infrastructure',
    'Demonstrates a low-cost, locally relevant application of '
    'retrieval-augmented artificial intelligence built on standard cloud '
    'services.']],
  [0.75, 1.5, 3.15],
  10),
 ('h2', '1.8  COMPLEX ENGINEERING PROBLEM ATTRIBUTES'),
 ('p',
  'The project was assessed against the complex engineering problem '
  'attributes required of a final year project in an accredited engineering '
  'programme. Table 1.3 records each attribute with the specific part of '
  'this system that shows it.'),
 ('table',
  'Complex engineering problem attributes shown by the project',
  ['Attribute', 'How it appears in this project'],
  [['Depth of knowledge',
    'Requires information retrieval, vector embeddings, prompt design, '
    'relational modelling, web security and cloud cost control.'],
   ['Range of conflicting requirements',
    'Answer quality pulls towards longer prompts and larger models, while '
    'cost and latency pull the other way. The memory manager and the '
    'retrieval budget are the negotiated settlement.'],
   ['Depth of analysis',
    'No standard answer exists for how much curricular context to retrieve, '
    'or how to mark free text against a board scheme. Both were settled by '
    'measurement, reported in Chapter 8.'],
   ['Familiarity of issues',
    'Grounding a language model in a scanned, low-resource, '
    'non-English-first curriculum is not a routine problem with a published '
    'recipe.'],
   ['Extent of applicable codes',
    'Copyright over board material, protection of minors’ data and '
    'examination integrity all constrain the design.'],
   ['Stakeholder involvement',
    'Students, teachers, the supervisor and the examination boards have '
    'different and partly opposed interests.'],
   ['Interdependence',
    'The system spans four tiers and two external providers. A change in the '
    'chunking strategy alters retrieval quality, prompt size, cost and '
    'answer quality together.']],
  [1.35, 4.05],
  10),
 ('h2', '1.9  REPORT ORGANISATION'),
 ('p', 'The rest of this report is organised as follows.'),
 ('bullets',
  [['Chapter 2, Literature Review. ',
    'Surveys artificial intelligence in education, intelligent tutoring '
    'systems, conversational agents, large language models and their limits, '
    'retrieval-augmented generation, vector search, automatic marking and '
    'the Pakistani educational technology market, and states the research '
    'gap this project fills.'],
   ['Chapter 3, Requirement Analysis and Methodology. ',
    'Describes the Agile process followed, the survey and its results, the '
    'stakeholder and user analysis, the functional and non-functional '
    'requirements, the behavioural models taken from the Software '
    'Requirements Specification, the feasibility study and the traceability '
    'matrix.'],
   ['Chapter 4, System Architecture. ',
    'Presents the architectural approach, the subsystem split, the data flow '
    'diagrams, the design of the artificial-intelligence subsystem, the '
    'ingestion pipeline, the request-time retrieval path, the security model '
    'and the deployment view.'],
   ['Chapter 5, Detailed System Design. ',
    'Gives the database design and data dictionary, the class model, a '
    'ten-attribute specification of each software component, the interface '
    'design and the prompt design.'],
   ['Chapter 6, Implementation. ',
    'Documents the development environment, the repository and its history, '
    'and the module-by-module implementation with annotated code listings.'],
   ['Chapter 7, System Testing. ',
    'States the testing strategy, reports the automated suite, presents the '
    'functional and non-functional test cases, and describes the dedicated '
    'retrieval and language-model evaluation harness.'],
   ['Chapter 8, Results and Evaluation. ',
    'Presents the working system, the measured corpus, the retrieval '
    'results, the grounding and marking experiments, the performance and '
    'cost measurements, the acceptance testing and the assessment against '
    'the objectives.'],
   ['Chapter 9, Conclusion and Future Work. ',
    'Summarises the contribution, states the strengths and limitations '
    'openly, gives the cost position and sets out future work.']]),
 ('p',
  'References follow in Chicago author-date style. Five appendices give the '
  'glossary, the survey instrument and full results, additional code '
  'listings, a user manual and the similarity report.')]
