"""Content blocks for Chapter 3 - Requirement Analysis and Methodology."""

BLOCKS = [('chapter', 'CHAPTER 3', 'REQUIREMENT ANALYSIS AND METHODOLOGY'),
 ('p',
  'This chapter explains how the requirements were established and how the '
  'work was organised. It describes the development process, the survey of '
  'forty-eight students that drove the design, the stakeholders and user '
  'classes, the functional and non-functional requirements, the behavioural '
  'models carried over from the Software Requirements Specification, the '
  'feasibility study and the traceability matrix.'),
 ('h2', '3.1  Introduction'),
 ('p',
  'This chapter documents how the project was run and how its requirements '
  'were established. Section 3.2 describes the development methodology and '
  'the sprint structure actually followed. Sections 3.3 and 3.4 present the '
  'requirement elicitation instrument and its results, which are the '
  'empirical basis for every functional decision in the system. Section 3.5 '
  'analyses the stakeholders and user classes. Sections 3.6 and 3.7 give the '
  'complete functional and non-functional requirement sets. Section 3.8 '
  'presents the behavioural models — use cases, state machine and '
  'interaction sequence. Section 3.9 reports the feasibility study, Section '
  '3.10 the requirement traceability matrix, and Section 3.11 the tools and '
  'technologies selected together with the justification for each.'),
 ('h2', '3.2  Development Methodology'),
 ('h3', '3.2.1  Selection of an Agile process'),
 ('p',
  'The project adopted an Agile, Scrum-inspired process. The choice was made '
  'on the basis of two properties of the problem rather than on fashion. '
  "First, a large part of the system's behaviour could not be specified in "
  'advance. Nobody on the team could say, before building it, what chunk '
  'size would retrieve good context from a Pakistani physics textbook. Nor '
  'could anyone say what prompt would make a model mark a short answer '
  'consistently. These were empirical questions that had to be answered by '
  'building, measuring and revising. A plan-driven waterfall process, which '
  'assumes requirements can be fixed before construction begins, would have '
  'been actively harmful (Sommerville 2016). Second, the project had a fixed '
  'academic deadline and a fixed team size, so scope was the only variable '
  'left to adjust. An iterative process with a prioritised backlog makes '
  'that adjustment visible and deliberate rather than accidental (Beck et '
  'al. 2001; Schwaber and Sutherland 2020).'),
 ('fig',
  'fig_agile.png',
  'The Agile process applied to the project. Supervisor feedback and defects '
  'found during testing re-enter the product backlog, which is why the '
  'requirement set grew between the Software Requirements Specification and '
  'the delivered system.',
  5.9),
 ('h3', '3.2.2  Sprint structure and outcomes'),
 ('p',
  'Work was organised into two-week sprints. Each sprint began with planning '
  'against the backlog, ended with a demonstration to the supervisor, and '
  'produced an increment merged into the main branch. Table 3.1 records the '
  'sprints as they actually ran, with the principal outcome of each. The '
  'version history of the repository, which contains 114 commits, 89 of them '
  'excluding merges, across the development period, corroborates this '
  'schedule.'),
 ('table',
  'Sprint plan and outcomes',
  ['Sprint', 'Focus', 'Principal outcome'],
  [['S1',
    'Requirement elicitation',
    'Survey instrument designed and administered; 48 responses collected and '
    'analysed; module list revised against the evidence.'],
   ['S2',
    'Specification and modelling',
    'Software Requirements Specification produced; use-case, state-machine '
    'and sequence models drawn; REQ-1 to REQ-25 baselined.'],
   ['S3',
    'Project skeleton and authentication',
    'Laravel 13 and Inertia React scaffold; Fortify registration, login, '
    'email verification, password reset and two-factor authentication.'],
   ['S4',
    'Database and academic profile',
    'Users, chat and content schema migrated; Board, ClassLevel and Subject '
    'enumerations introduced; selection and profile pages.'],
   ['S5',
    'Corpus ingestion',
    'Google Cloud Vision OCR extraction, cleaning and chunking scripts; '
    'first textbooks embedded into Pinecone.'],
   ['S6',
    'Teacher agent',
    'FastAPI service, retriever with metadata filtering, teacher prompt, '
    'chat session and message persistence.'],
   ['S7',
    'Conversation memory',
    'Memory manager with rolling summarisation; existing_summary persisted '
    'per session; prompt growth bounded.'],
   ['S8',
    'Tester agent and practice UI',
    'Question generation for MCQ, short and long formats; provenance '
    'labelling; curriculum map of 379 chapters wired into the practice '
    'page.'],
   ['S9',
    'Evaluator and session results',
    'Per-answer marking with score clamping; overall session evaluator; '
    'quiz_sessions and quiz_results persistence.'],
   ['S10',
    'Analytics, resources and admin',
    'Progress dashboard, activity feed, resource library with download '
    'counting, administrative console for users and content.'],
   ['S11',
    'Optimisation and instrumentation',
    'Embedding LRU cache; single-embed combined retrieval; per-call token '
    'and cost logging; evaluator response budget reduced.'],
   ['S12',
    'Hardening, testing and documentation',
    'Google OAuth sign-in; automated test suite run and defects logged; '
    'system and acceptance testing; this report.']],
  [0.6, 1.5, 4.0],
  10),
 ('h3', '3.2.3  Version control and collaboration'),
 ('p',
  'The team used Git with a branch-per-concern convention. A long-lived '
  'branch carried backend work, a separate branch carried the '
  'artificial-intelligence service, and both were merged into the main '
  'branch at the end of each sprint after demonstration. Static analysis and '
  'formatting were enforced by Laravel Pint for PHP, ESLint and Prettier for '
  'TypeScript, so that review effort could be spent on logic rather than on '
  'style.'),
 ('h2', '3.3  Requirement Elicitation'),
 ('p',
  'Requirements were gathered in three ways that complement each other. A '
  'structured online questionnaire was given to students of classes nine to '
  'twelve and produced forty-eight complete responses. Short, informal '
  'interviews with some of those students were used to clarify free-text '
  'answers that were ambiguous. Finally, a competitive analysis of the '
  'platforms reviewed in Section 2.10 established the baseline feature set '
  'that any credible new entrant has to meet.'),
 ('p',
  'Wherever possible the questionnaire asked about behaviour rather than '
  'preference. Where do you study? What do you already use? What do you find '
  'difficult? Stated preferences about products that do not yet exist are '
  'unreliable, so questions about behaviour carry more weight in the '
  'analysis that follows. Fourteen questions were asked in total, nine of '
  'them closed and five open. The full instrument and the complete results '
  'are reproduced in Appendix B. The sample was a convenience sample of '
  'students the team could reach, which is a limitation recorded in Section '
  '8.11.'),
 ('h2', '3.4  Survey Results and Analysis'),
 ('h3', '3.4.1  Respondent profile'),
 ('p',
  'Responses came from all four target classes. Class 12 gave 37.5 per cent '
  'of responses and Class 11 gave 35.4 per cent, followed by Class 10 at '
  '14.6 per cent and Class 9 at 12.5 per cent. The lean towards the senior '
  'classes is expected, because examination pressure, and therefore interest '
  'in study tools, rises sharply in the final two years. It also confirmed '
  'that the system had to support the intermediate curriculum properly '
  'rather than treat it as an extension of the matriculation curriculum. '
  'Seventy-two per cent of respondents were therefore in the two classes '
  'whose results decide university entry.'),
 ('fig',
  'fig_survey_class.png',
  'Class of survey respondents (n = 48).',
  5.2),
 ('h3', '3.4.2  Study environment and habits'),
 ('p',
  'Most students study on their own. 45.8 per cent reported studying mainly '
  'at home and 41.7 per cent mainly at school, against only 6.3 per cent at '
  'a tuition centre and 6.3 per cent who said all of these. This result '
  'influenced the design more than any other. A tool used at home, with no '
  'teacher present, has to be self-explanatory. It must answer questions '
  'rather than only present material, and it must tell the student whether '
  'their answer was right, because nobody else is there to do it.'),
 ('fig',
  'fig_survey_location.png',
  'Where respondents study most (n = 48).',
  5.2),
 ('p',
  'The students were then asked what they actually do when they do not '
  'understand a topic. More than one answer was allowed, and forty-seven '
  'students replied. Watching YouTube was the most common action, reported '
  'seventeen times, followed closely by ChatGPT with sixteen and a general '
  'web search with fifteen. Asking a teacher came fourth with eleven. Asking '
  'a friend and using notes or books tied for last with five each. The '
  'ordering is significant. For this population an artificial-intelligence '
  'assistant is already a more common first response to confusion than a '
  'human teacher.'),
 ('fig',
  'fig_survey_stuck.png',
  'What students do when a topic is unclear (n = 47).',
  5.6),
 ('h3', '3.4.3  Existing tool use and its problems'),
 ('p',
  'Answers to the question on existing online study tools were spread '
  'widely, so the free text was grouped into three categories. The largest '
  'group, 54.2 per cent, uses no online study tool at all. A further 29.2 '
  'per cent named ChatGPT or another chatbot, and 16.7 per cent named some '
  'other tool such as YouTube, Google or a subject application. Two '
  'conclusions follow. First, a little over half of the target population is '
  'not served by any digital tool, which is the opportunity. Second, among '
  'those who are served, the incumbent is a general chatbot. That fixes the '
  'interaction model students already expect, a chat box, and it identifies '
  'the competitor the system has to beat on the one dimension that matters '
  'here, which is fidelity to the syllabus.'),
 ('fig', 'fig_survey_tools.png', 'Use of online study tools (n = 48).', 5.2),
 ('p',
  'Asked directly, 75 per cent of respondents said they use ChatGPT. Those '
  'students were then asked what problems they face when they use it for '
  'learning. Forty-five answered, and twenty-six of them described a '
  'concrete problem; the remaining nineteen said they had none. The '
  'free-text answers were coded into themes, and a single answer could carry '
  'more than one theme. Answers that are too long or padded was the largest '
  'theme with eleven mentions. Wording that is too difficult or pitched too '
  'high followed with seven, as did wrong, vague or unrelated answers. Three '
  'students said the model fails to understand their question, three pointed '
  'to limits of the model or its data, two reported weakness on numerical '
  'and mathematics questions, and one noted the absence of diagrams.'),
 ('fig',
  'fig_survey_chatgpt_problems.png',
  'Problems reported with general-purpose assistants.',
  5.6),
 ('p',
  'These complaints are not vague dissatisfaction. Each one maps onto a '
  'specific design decision, and together they account for four of the '
  'requirements in Section 3.6. Those are a prompt that limits answer length '
  'and reading level, retrieval that ties answers to the prescribed book, '
  'and a marking scheme that tells the student where they actually lost '
  'marks.'),
 ('h3', '3.4.4  What students find difficult'),
 ('p',
  'Asked what they need more help with, 52.1 per cent of respondents said '
  'understanding concepts, 37.5 per cent said both understanding concepts '
  'and practising questions, 6.3 per cent said practising questions alone '
  'and 4.2 per cent were unsure. Taken together, 89.6 per cent need help '
  'with concepts and 43.8 per cent need help with practice. That '
  'distribution is the direct justification for building two separate agents '
  'rather than one. A system that only explains would fail nearly half the '
  'population, and a system that only tests would fail almost all of it.'),
 ('fig',
  'fig_survey_help.png',
  'What students need more help with (n = 48).',
  5.2),
 ('p',
  'A separate open question asked what the biggest difficulty is while '
  'studying. Forty-six students answered, and the responses were coded into '
  'themes. Understanding concepts led with fourteen mentions, followed by '
  'time management with eleven and a long syllabus with eight. Focus and '
  'distraction accounted for four, difficulty finding study material for '
  'four, and lack of guidance for three. The combination of a long syllabus '
  'and limited time is the reason the practice module allows a student to '
  'select a single chapter rather than always being tested on a whole book.'),
 ('fig',
  'fig_survey_difficulty.png',
  'Biggest difficulty reported while studying (n = 46).',
  5.6),
 ('h3', '3.4.5  Demand for board-specific support'),
 ('p',
  'Three questions tested the premise of the project directly, and all three '
  'supported it. Asked whether board examination content differs from the '
  'study material available online, 50 per cent said yes and a further 29.2 '
  'per cent said sometimes. Only 20.8 per cent saw no difference. Nearly '
  'four students in five therefore report, unprompted, exactly the mismatch '
  'this project sets out to remove.'),
 ('fig',
  'fig_survey_boardvsonline.png',
  'Reported mismatch between board and online material (n = 48).',
  5.2),
 ('p',
  'Asked whether an application that gave questions and explanations based '
  'on their own board syllabus would help, 79.2 per cent said yes, 16.7 per '
  'cent said maybe and only 4.2 per cent said no. Asked whether a chatbot '
  'that tests them, shows their mistakes and explains the correct answer '
  'would help them learn better, the same 79.2 per cent said yes, 14.6 per '
  'cent said maybe and 6.3 per cent said no. A clear yes from four students '
  'in five, on two separate and specific product propositions, is a strong '
  'demand signal from a sample of this size.'),
 ('fig',
  'fig_survey_boardapp.png',
  'Value of an application tied to the board syllabus (n = 48).',
  5.2),
 ('p',
  'A fourth question established the need for the resource library. Asked '
  'whether they download past papers or textbooks from the internet, 52.1 '
  'per cent said they do but find them difficult to find, 33.3 per cent said '
  'they do not download them at all, and only 14.6 per cent said the '
  'material was easy to find. The problem is therefore not that the '
  'documents are unavailable. It is that they are scattered, and students '
  'cannot filter them by their own board, class and subject.'),
 ('fig',
  'fig_survey_downloads.png',
  'Ease of finding past papers and textbooks online (n = 48).',
  5.2),
 ('h3', '3.4.6  Features students asked for'),
 ('p',
  'The final open question asked what features a good learning application '
  'should have. All forty-eight students answered, and the free text was '
  'coded into themes. Access to past papers led with eleven mentions. Simple '
  'wording and to-the-point answers followed with ten, then keybooks and '
  'textbooks with eight and chapter videos with six. Quizzes and '
  'multiple-choice questions and voice answers tied at four each, ahead of '
  'an artificial-intelligence chatbot and correct answers at three each. '
  'Syllabus-aligned content and freedom from subscription charges drew two '
  'mentions each, and an Urdu option one.'),
 ('fig',
  'fig_survey_features.png',
  'Features students asked for in a learning application (n = 48).',
  5.6),
 ('p',
  'Two of these deserve comment. The request for voice answers, made by four '
  'students, was not anticipated when the proposal was written and was added '
  'to the backlog during Sprint 6; voice input is delivered in the final '
  'system. The request for freedom from subscription charges confirms that '
  'cost per interaction is a product requirement and not only an engineering '
  'concern, which is why the system measures it. Six of the eleven themes '
  'map onto features that were already planned, and the platform delivers '
  'past papers, keybooks, textbooks, quizzes, an artificial-intelligence '
  'chatbot, syllabus-aligned content, free access, an Urdu option and voice '
  'input. Chapter videos are the one frequently requested feature the '
  'platform does not provide, and it is recorded as future work in Section '
  '9.6.'),
 ('h3', '3.4.7  Requirements derived from the survey'),
 ('p',
  'Table 3.2 traces each significant survey finding through to the design '
  'decision it forced and the requirements that record it. Every row is '
  'evidence-backed; no requirement in the table was introduced on the team’s '
  'own assumption alone.'),
 ('table',
  'From survey findings to system requirements',
  ['Survey finding', 'Design consequence', 'Requirements'],
  [['45.8 % study at home, unsupervised',
    'The system must explain, test and mark on its own, with no teacher in '
    'the loop.',
    'REQ-12, REQ-18, REQ-19'],
   ['89.6 % need help with concepts',
    'A conversational teacher agent grounded in the prescribed textbook.',
    'REQ-12 to REQ-15'],
   ['43.8 % also need question practice',
    'A tester agent that generates MCQ, short and long questions.',
    'REQ-16, REQ-17'],
   ['75 % use ChatGPT; 11 complain answers are too long',
    'The teacher prompt constrains answers to a short, exam-focused form.',
    'REQ-15'],
   ['7 complain the wording is too difficult',
    'The prompt fixes the reading level to the class and prefers textbook '
    'wording.',
    'REQ-14, REQ-15'],
   ['7 report wrong or unrelated answers',
    'Retrieval grounds every answer in the board corpus, and marking '
    'explains what was missed.',
    'REQ-8 to REQ-11, REQ-19'],
   ['79.2 % report a board-versus-online mismatch',
    'Board, class and subject become a hard retrieval filter rather than a '
    'preference.',
    'REQ-8 to REQ-11'],
   ['Long syllabus and poor time management dominate difficulties',
    'Chapter-scoped practice, so a student can drill one chapter instead of '
    'a whole book.',
    'REQ-17, REQ-31'],
   ['52.1 % find past papers hard to locate',
    'A filtered, downloadable resource library scoped to the student’s own '
    'board and class.',
    'REQ-21 to REQ-25'],
   ['Requests for simpler and Urdu explanations',
    'A bilingual response policy in the teacher prompt.',
    'REQ-14'],
   ['Requests for voice answers',
    'Browser speech recognition on the tutor composer.',
    'REQ-13'],
   ['Requests for a subscription-free product',
    'Per-call cost accounting, so affordability can be demonstrated.',
    'REQ-32']],
  [1.85, 2.4, 1.15],
  9),
 ('h2', '3.5  Stakeholder and User Class Analysis'),
 ('table',
  'Stakeholder analysis',
  ['Stakeholder', 'Interest in the system', 'Influence on requirements'],
  [['Students of classes 9–12',
    'Primary beneficiaries; want faster understanding and better examination '
    'results.',
    'High — the survey population; requirements were derived directly from '
    'their reported behaviour.'],
   ['Project supervisor',
    'Academic quality, engineering rigour and defensibility of the work.',
    'High — review feedback entered the backlog each sprint.'],
   ['Department and evaluation panel',
    'Conformance to programme learning outcomes and report standards.',
    'Medium — shaped documentation and evaluation requirements.'],
   ['Examination boards and publishers',
    'Correct representation and lawful use of curricular material.',
    'Medium — constrains what may be redistributed; see Section 3.7.5.'],
   ['Parents',
    'Value for money and safety of the material their child studies.',
    'Low direct, high indirect — motivates the grounding requirement.'],
   ['Platform administrator',
    'Ability to curate content and manage accounts without developer '
    'involvement.',
    'Medium — produced the administrative console requirements REQ-33 to '
    'REQ-38.']],
  [1.35, 2.3, 2.3],
  9.5),
 ('h3', '3.5.1  User classes'),
 ('bullets',
  [['Student (primary). ',
    'A learner aged approximately fourteen to nineteen, enrolled in class '
    'nine to twelve under the Federal or AJK board. Basic computer literacy '
    'is assumed; technical knowledge is not. Uses the system unsupervised, '
    'frequently on a mobile browser, in sessions of ten to forty minutes. '
    'Represents the overwhelming majority of traffic and every AI-driven '
    'interaction.'],
   ['Administrator (secondary). ',
    'A technical or academic staff member responsible for uploading and '
    'curating downloadable resources, monitoring registered accounts, and '
    'blocking or reactivating accounts. Small in number, high in privilege, '
    'and therefore the focus of the role-based access control described in '
    'Section 4.11.'],
   ['System operator (implicit). ',
    'The person responsible for running the ingestion pipeline when a new '
    'board, class or subject is added. Interacts through command-line '
    'scripts rather than the web interface.']]),
 ('h3', '3.5.2  Representative personas'),
 ('table',
  'User personas used to guide interface decisions',
  ['Persona', 'Situation', 'What the system must do for them'],
  [['Ayesha, 17, Class 12 Pre-Medical, AJK Board',
    'Studies at home after school; cannot afford a tuition academy; two '
    'months from the board examination.',
    "Generate long questions in her board's style from her own Biology "
    'textbook, mark her written answers honestly and tell her which chapters '
    'to revise.'],
   ['Bilal, 15, Class 9, Federal Board',
    "Comfortable in Urdu, less so in English; finds the Chemistry textbook's "
    'phrasing difficult.',
    'Explain a concept in simple language, in Urdu when he asks in Urdu, '
    'using the definitions his own book uses.'],
   ['Hina, 16, Class 11, Federal Board',
    'Strong student, short of time, wants to know what is likely to be '
    'asked.',
    'Produce practice items labelled by past-paper provenance so she can '
    'prioritise what recurs.'],
   ['Mr. Tariq, platform administrator',
    'Non-developer; maintains the resource library each term.',
    'Upload, categorise, edit and remove resources and manage accounts '
    'through a web console with no database access.']],
  [1.5, 2.2, 2.25],
  9.5),
 ('h2', '3.6  Functional Requirements'),
 ('p',
  'Requirements REQ-1 to REQ-25 are those baselined in the Software '
  'Requirements Specification defended at the end of Phase I. Requirements '
  'REQ-26 to REQ-42 were added during Phase II as the implementation '
  'matured, principally to cover security hardening, administration, '
  'analytics and the artificial-intelligence service contract that the '
  'original specification treated as a single opaque feature. Both sets are '
  'listed here so that the delivered system can be assessed against a '
  'complete specification. The requirement statements follow the recommended '
  'practice of IEEE Std 830 (1998): each is uniquely identified, singular, '
  'and expressed as a verifiable “shall” statement. Priority is recorded as '
  'High, Medium or Low.'),
 ('h3', '3.6.1  Authentication and profile management'),
 ('table',
  'Functional requirements — authentication and profile',
  ['ID', 'Requirement', 'Priority'],
  [['REQ-1',
    'The system shall allow users to register using an email address and a '
    'password.',
    'High'],
   ['REQ-2',
    'The system shall authenticate users securely during login.',
    'High'],
   ['REQ-3',
    'The system shall allow users to register and log in using a Google '
    'account via OAuth 2.0.',
    'High'],
   ['REQ-4',
    'The system shall allow users to update their profile information.',
    'Medium'],
   ['REQ-5',
    'The system shall provide password-recovery functionality.',
    'High'],
   ['REQ-6',
    'The system shall prevent unauthorised access to user data.',
    'High'],
   ['REQ-7',
    'The system shall link a Google-authenticated account to an existing '
    'profile where the email address matches.',
    'Medium'],
   ['REQ-26',
    'The system shall require email-address verification before granting '
    'access to learning features.',
    'High'],
   ['REQ-27',
    'The system shall offer optional time-based one-time-password two-factor '
    'authentication with recovery codes.',
    'Medium'],
   ['REQ-28',
    'The system shall rate-limit authentication attempts to resist '
    'credential-stuffing attacks.',
    'High'],
   ['REQ-29',
    'The system shall require password confirmation before '
    'security-sensitive operations.',
    'Medium']],
  [0.75, 4.45, 0.75],
  10),
 ('h3', '3.6.2  Academic selection and curriculum scoping'),
 ('table',
  'Functional requirements — academic selection',
  ['ID', 'Requirement', 'Priority'],
  [['REQ-8',
    'The system shall allow a student to select their board (Federal or '
    'AJK).',
    'High'],
   ['REQ-9', 'The system shall allow class selection from 9 to 12.', 'High'],
   ['REQ-10',
    'The system shall display subject options appropriate to the selected '
    'class.',
    'High'],
   ['REQ-11',
    'The system shall automatically scope all board-specific content — '
    'textbooks, keybooks and past papers — to the selected board, class and '
    'subject.',
    'High'],
   ['REQ-30',
    'The system shall persist the academic selection to the user profile so '
    'that it is applied on subsequent visits.',
    'Medium'],
   ['REQ-31',
    'The system shall expose the chapter list of the selected class and '
    'subject and allow practice to be scoped to selected chapters or to the '
    'whole book.',
    'High']],
  [0.75, 4.45, 0.75],
  10),
 ('h3', '3.6.3  Conversational tutoring'),
 ('table',
  'Functional requirements — AI tutoring',
  ['ID', 'Requirement', 'Priority'],
  [['REQ-12',
    'The system shall provide an AI chatbot for learning support.',
    'High'],
   ['REQ-13',
    'The chatbot shall generate syllabus-aligned responses.',
    'High'],
   ['REQ-14', 'The chatbot shall support both English and Urdu.', 'Medium'],
   ['REQ-15',
    'The chatbot shall provide short, exam-focused explanations.',
    'High'],
   ['REQ-32',
    'The system shall retrieve context from the vector index under a hard '
    'metadata filter on board, class and subject before every generation.',
    'High'],
   ['REQ-33',
    'The system shall maintain multiple named chat sessions per user and '
    'allow a session to be resumed or deleted.',
    'Medium'],
   ['REQ-34',
    'The system shall maintain a rolling summary of each conversation so '
    'that context is preserved without unbounded prompt growth.',
    'Medium'],
   ['REQ-35',
    'The chatbot shall state explicitly when an answer is drawn from general '
    'knowledge rather than the prescribed textbook.',
    'High']],
  [0.75, 4.45, 0.75],
  10),
 ('h3', '3.6.4  Practice, assessment and evaluation'),
 ('table',
  'Functional requirements — practice and assessment',
  ['ID', 'Requirement', 'Priority'],
  [['REQ-16',
    'The system shall allow a student to select a practice type before '
    'starting: MCQ, short question or long question.',
    'High'],
   ['REQ-17',
    'The system shall generate a mock test of the selected type, aligned to '
    "the student's board, class and subject.",
    'High'],
   ['REQ-18',
    'The system shall evaluate student answers and provide detailed '
    'feedback.',
    'High'],
   ['REQ-19',
    'The system shall identify mistakes and highlight weak areas after each '
    'practice session.',
    'High'],
   ['REQ-20',
    'The system shall store quiz and mock-test results for progress '
    'tracking.',
    'High'],
   ['REQ-36',
    'The system shall label each generated question according to whether it '
    'is taken from a past paper, modelled on past-paper style, or newly '
    'written from the textbook.',
    'Medium'],
   ['REQ-37',
    'The system shall apply the board marking scheme of 1 mark per MCQ, 3 '
    'per short question and 8 per long question, and shall never award more '
    'than the permitted maximum.',
    'High'],
   ['REQ-38',
    'The system shall produce a session-level result comprising total score, '
    'percentage, grade band, strong areas, weak areas and a study '
    'recommendation.',
    'High']],
  [0.75, 4.45, 0.75],
  10),
 ('h3', '3.6.5  Resources, analytics and administration'),
 ('table',
  'Functional requirements — resources, analytics and administration',
  ['ID', 'Requirement', 'Priority'],
  [['REQ-21',
    'The system shall allow students to filter downloadable resources by '
    'board, class and subject.',
    'High'],
   ['REQ-22',
    'The system shall provide past papers for download for the selected '
    'board, class and subject.',
    'High'],
   ['REQ-23',
    'The system shall provide textbooks and keybooks for download where '
    'lawfully permitted.',
    'Medium'],
   ['REQ-24',
    'The system shall organise all downloadable resources by board, class '
    'and subject.',
    'Medium'],
   ['REQ-25',
    'The system shall display a clear message when no resource exists for a '
    'selected combination.',
    'Medium'],
   ['REQ-39',
    'The system shall record a download count per resource.',
    'Low'],
   ['REQ-40',
    'The system shall present a progress dashboard showing quizzes taken, '
    'questions attempted, average score and subject-wise performance with a '
    'focus recommendation.',
    'High'],
   ['REQ-41',
    'The system shall maintain a bounded recent-activity feed per user '
    'covering chat, quiz and download events.',
    'Low'],
   ['REQ-42',
    'The system shall provide an administrative console, restricted by role, '
    'for uploading, editing and deleting resources and for listing, editing, '
    'blocking and deleting user accounts.',
    'High']],
  [0.75, 4.45, 0.75],
  10),
 ('h2', '3.7  Non-Functional Requirements'),
 ('h3', '3.7.1  Performance'),
 ('table',
  'Non-functional requirements — performance',
  ['ID', 'Requirement', 'Acceptance criterion'],
  [['NFR-1',
    'Ordinary page and API requests that do not invoke a language model '
    'shall respond quickly.',
    'Between 1 and 3 seconds under normal load.'],
   ['NFR-2',
    'AI-generated responses shall be returned within an acceptable '
    'interactive window.',
    'Between 2 and 5 seconds depending on query complexity.'],
   ['NFR-3',
    'Resource downloads shall begin promptly after the request.',
    'Between 1 and 4 seconds.'],
   ['NFR-4',
    'The system shall support concurrent use without degradation.',
    'Minimum 50 and target 500 concurrent users.'],
   ['NFR-5',
    'Prompt size for a tutoring session shall not grow without bound as the '
    'session lengthens.',
    'Verbatim history capped at four turns; older turns compressed to a '
    'summary of at most 200 tokens.']],
  [0.75, 2.7, 2.45],
  9.5),
 ('h3', '3.7.2  Security'),
 ('table',
  'Non-functional requirements — security',
  ['ID', 'Requirement', 'Acceptance criterion'],
  [['NFR-6',
    'Passwords shall never be stored in recoverable form.',
    "Bcrypt hashing through the framework's hashed cast."],
   ['NFR-7',
    'All state-changing requests shall be protected against cross-site '
    'request forgery.',
    'CSRF token verified on every non-idempotent request.'],
   ['NFR-8',
    'Administrative capability shall be restricted by role.',
    'Administrative routes reachable only by accounts whose role attribute '
    'is administrator.'],
   ['NFR-9',
    'Communication with third-party services shall be encrypted.',
    'TLS enforced for all outbound API calls.'],
   ['NFR-10',
    'Secrets shall not appear in the source repository.',
    'All credentials supplied through environment variables.'],
   ['NFR-11',
    'Two-factor secrets and recovery codes shall be stored encrypted.',
    'Framework-level encryption at rest.']],
  [0.75, 2.7, 2.45],
  9.5),
 ('h3', '3.7.3  Usability, reliability and maintainability'),
 ('table',
  'Non-functional requirements — quality attributes',
  ['ID', 'Attribute', 'Requirement'],
  [['NFR-12',
    'Usability',
    'The interface shall be operable by a student with basic computer '
    'literacy and no training, and shall be responsive from a 360-pixel '
    'mobile viewport upward.'],
   ['NFR-13',
    'Reliability',
    'The system shall target 99.5 per cent availability and shall degrade '
    'gracefully — with an explanatory message rather than an error page — '
    'when a third-party AI service is unavailable.'],
   ['NFR-14',
    'Scalability',
    'Additional boards, classes and subjects shall be addable by ingesting '
    'data, without modification to application code.'],
   ['NFR-15',
    'Maintainability',
    'The codebase shall be modular, statically analysed and consistently '
    'formatted, with the AI workload isolated behind an HTTP boundary so it '
    'can be replaced independently.'],
   ['NFR-16',
    'Interoperability',
    'The system shall integrate with external identity, embedding, '
    'vector-search and OCR services through documented APIs.'],
   ['NFR-17',
    'Privacy',
    'Personal data shall be limited to what the service requires, and '
    'student answers shall not be shared with any party other than the model '
    'provider processing the request.'],
   ['NFR-18',
    'Portability',
    'The system shall run on Windows, Linux and macOS servers and in any '
    'modern browser.'],
   ['NFR-19',
    'Observability',
    'Every language-model call shall be logged with its endpoint, token '
    'counts and computed monetary cost.']],
  [0.75, 1.25, 3.9],
  9.5),
 ('h3', '3.7.4  Safety'),
 ('bullets',
  ['The system shall not expose students to inappropriate or misleading '
   'content; grounding in curated curricular material is the primary '
   'control.',
   "The system shall not lose a student's work through accidental navigation "
   'during an active practice session.',
   'The system shall warn on incomplete submission rather than silently '
   'discarding an answer.']),
 ('h3', '3.7.5  Legal and ethical constraints'),
 ('bullets',
  ['Only material that is lawfully and publicly available shall be offered '
   'for download. Ingested copyrighted material is used for retrieval '
   'grounding, not for redistribution.',
   'The system processes data belonging to minors and shall therefore '
   'collect the minimum necessary: name, email address, academic selection '
   'and learning history.',
   'Generated content shall be presented as study assistance rather than as '
   'an authoritative substitute for the prescribed textbook, and the tutor '
   'shall declare when it is answering from general knowledge.']),
 ('h2', '3.8  Behavioural Models'),
 ('h3', '3.8.1  Use case model'),
 ('p',
  'Figure 3.13 shows the use-case model as baselined in the Software '
  'Requirements Specification. Two human actors interact with the system. '
  'The Student registers, selects board, class and subject, asks the tutor '
  'questions, practises questions, downloads resources and views performance '
  'analysis. The Administrator logs in, uploads study resources, manages '
  'users and logs out. Two external systems participate: the AI chatbot '
  'system, which generates responses and evaluations, and the database '
  'system, which stores and retrieves all persistent state. Both human '
  'actors pass through authentication before any other capability becomes '
  'reachable.'),
 ('fig',
  'fig_usecase.jpg',
  'Use case diagram for the Eternal Sunshine platform, as baselined in the '
  'Software Requirements Specification.',
  5.7),
 ('h3', '3.8.2  Use case specifications'),
 ('p',
  'Four representative use cases are specified in full. The remainder follow '
  'the same template and are omitted for brevity.'),
 ('table',
  'Use case UC-01 — Ask the AI tutor a question',
  ['Field', 'Description'],
  [['Identifier', 'UC-01'],
   ['Actors',
    'Student (primary); AI chatbot system, database system (supporting)'],
   ['Preconditions',
    'The student is authenticated, their email is verified, and a board, '
    'class and subject have been selected.'],
   ['Trigger', 'The student submits a question in the chat interface.'],
   ['Main flow',
    '1. The student types a question and submits it.  2. The system resolves '
    'the board, class and subject from the session, falling back to the '
    'profile.  3. The system loads the most recent ten messages of the '
    'session and the stored conversation summary.  4. The system persists '
    "the student's message.  5. The system calls the AI service with the "
    'question, the academic scope, the recent history and the summary.  6. '
    'The AI service embeds the query, retrieves filtered context and '
    'generates an answer.  7. The system persists the answer, updates the '
    'stored summary and records an activity entry.  8. The answer is '
    'displayed.'],
   ['Alternative flows',
    '3a. No session exists: a new session is created and titled from the '
    'first 40 characters of the question.  6a. No sufficiently similar '
    'context is retrieved: the tutor answers from general knowledge and '
    'states that it is doing so.'],
   ['Exception flows',
    '5a. The AI service is unreachable: an explanatory message is shown and '
    "the student's message remains in the transcript."],
   ['Postconditions',
    'The exchange is persisted; the session summary reflects it; the '
    'activity feed contains an entry.'],
   ['Requirements', 'REQ-12 to REQ-15, REQ-32 to REQ-35']],
  [1.1, 4.85],
  9.5),
 ('table',
  'Use case UC-02 — Take a practice test',
  ['Field', 'Description'],
  [['Identifier', 'UC-02'],
   ['Actors',
    'Student (primary); AI chatbot system, database system (supporting)'],
   ['Preconditions',
    'The student is authenticated and has a board, class and subject either '
    'in profile or selected inline.'],
   ['Trigger', 'The student opens the practice page and starts a test.'],
   ['Main flow',
    '1. The student chooses whole-book or selected-chapter scope.  2. The '
    'student chooses MCQ, short or long format.  3. The system requests '
    'generation from the tester agent.  4. Questions are rendered one at a '
    'time.  5. For each answer submitted, the system requests evaluation and '
    'displays the score and feedback.  6. After the final question the '
    'system requests session-level evaluation.  7. The session and every '
    'answer are persisted and the summary is displayed.'],
   ['Alternative flows',
    '1a. The student selects no chapter: the whole book is used.  5a. The '
    'student leaves an answer blank: it is submitted as empty and scored '
    'zero with explanatory feedback.'],
   ['Exception flows',
    '3a. Generation fails: an error is displayed and the student may retry '
    'without losing the selection.'],
   ['Postconditions',
    'A quiz_sessions row and one quiz_results row per question exist; the '
    'dashboard reflects the new attempt.'],
   ['Requirements', 'REQ-16 to REQ-20, REQ-31, REQ-36 to REQ-38']],
  [1.1, 4.85],
  9.5),
 ('table',
  'Use case UC-03 — Download a resource',
  ['Field', 'Description'],
  [['Identifier', 'UC-03'],
   ['Actors', 'Student (primary); database system (supporting)'],
   ['Preconditions', 'The student is authenticated.'],
   ['Trigger', 'The student selects a resource and requests a download.'],
   ['Main flow',
    '1. The student filters the library by board, class, subject and '
    'resource type.  2. The matching resources are listed with title, type '
    'and size.  3. The student requests a download.  4. The system '
    'increments the download counter, records an activity entry and streams '
    'the file.'],
   ['Alternative flows',
    '2a. No resource matches: an explanatory empty state is shown (REQ-25).'],
   ['Exception flows',
    '4a. The stored file is missing: an error is reported and the counter is '
    'not incremented.'],
   ['Postconditions', 'The download counter and activity feed are updated.'],
   ['Requirements', 'REQ-21 to REQ-25, REQ-39, REQ-41']],
  [1.1, 4.85],
  9.5),
 ('table',
  'Use case UC-04 — Administer content',
  ['Field', 'Description'],
  [['Identifier', 'UC-04'],
   ['Actors',
    'Administrator (primary); database system, file storage (supporting)'],
   ['Preconditions',
    'The actor is authenticated and holds the administrator role.'],
   ['Trigger', 'The administrator opens the content console.'],
   ['Main flow',
    '1. The console lists all resources with filters.  2. The administrator '
    'uploads a file with title, type, board, class and subject.  3. The '
    'system validates the request and the file size limit, stores the file '
    'on the public disk and creates a content record.  4. The administrator '
    'may subsequently edit metadata or delete a resource, in which case the '
    'stored file is also removed.'],
   ['Alternative flows',
    '2a. Validation fails: field-level errors are returned and no record is '
    'created.'],
   ['Exception flows',
    '3a. Storage is unavailable: the upload is rejected and no orphan record '
    'is created.'],
   ['Postconditions',
    'The resource library reflects the change immediately for all students.'],
   ['Requirements', 'REQ-42']],
  [1.1, 4.85],
  9.5),
 ('h3', '3.8.3  State machine model'),
 ('p',
  'Figure 3.14 shows the state transition model for a user session. The user '
  'moves between registration, login, the authenticated dashboard, learning, '
  'practice, evaluation and logout in response to their own actions and the '
  "system's responses. The model was used to verify that every state has a "
  'defined exit and that no learning state is reachable without passing '
  'through authentication.'),
 ('fig',
  'fig_state.jpg',
  'State transition diagram for a user session, as baselined in the Software '
  'Requirements Specification.',
  5.9),
 ('h3', '3.8.4  Interaction sequence model'),
 ('p',
  'Figure 3.15 shows the principal interaction sequences: login and '
  'authentication, content loading after academic selection, the AI question '
  'loop, the practice and evaluation flow, resource download and logout. The '
  'loop fragment around the question exchange captures an important fact. A '
  'tutoring session is any number of turns against one persistent session '
  'record. That observation later drove the conversation-memory design of '
  'Section 4.9.'),
 ('fig',
  'fig_sequence.jpg',
  'Sequence diagram covering login, content loading, AI questioning, '
  'practice evaluation, resource download and logout.',
  4.9),
 ('h2', '3.9  Feasibility Study'),
 ('h3', '3.9.1  Technical feasibility'),
 ('p',
  'Every technical component required by the design either existed as a '
  "mature commodity or was demonstrably within the team's competence. "
  'Laravel, React and MySQL are established and well documented. Managed '
  'vector search removes the need to implement or operate an approximate '
  'nearest-neighbour index. Language-model capability is consumed through an '
  'API, so no training infrastructure, no graphics hardware and no '
  'machine-learning expertise beyond prompt design is required. The only '
  'genuinely uncertain element at the outset was retrieval quality over '
  'recognised text from scanned board material. That risk was retired in '
  'Sprint 5 by ingesting a single textbook end to end and reading the '
  'retrieved excerpts by hand before committing to the architecture.'),
 ('h3', '3.9.2  Economic feasibility'),
 ('p',
  "The project's direct cost is dominated by third-party service "
  'consumption. Table 3.17 gives the development-phase position. The pricing '
  'used is the published rate for gpt-4o-mini: 0.150 United States dollars '
  'per million input tokens and 0.600 per million output tokens. The '
  'embedding model is 0.020 per million tokens. These are the same constants '
  'the system uses internally to compute the cost of every call. The '
  'consequence is that the marginal cost of serving a student is small '
  'enough that free access is a realistic operating model, which is the '
  'economic precondition for the equity claim in Section 1.7.'),
 ('table',
  'Development-phase cost position',
  ['Item', 'Basis', 'Cost'],
  [['Language-model usage (gpt-4o-mini)',
    'USD 0.150 per 1M input tokens; USD 0.600 per 1M output tokens; metered '
    'per call by the built-in token logger',
    'Usage-dependent; see Section 8.6'],
   ['Embedding generation (text-embedding-3-small)',
    'USD 0.020 per 1M tokens; one-off for corpus ingestion plus a small '
    'per-query cost',
    'A few US dollars for the whole corpus'],
   ['Vector index (Pinecone serverless)',
    'Free starter tier sufficient for the ingested corpus',
    'Nil during development'],
   ['Google Cloud Vision OCR',
    'First 1,000 units per month free; billed thereafter',
    'Within free tier for staged ingestion'],
   ['Google OAuth 2.0', 'No charge', 'Nil'],
   ['Development hardware and tooling',
    'Team-owned laptops; open-source toolchain; free tiers of Figma and '
    'GitHub',
    'Nil'],
   ['Production hosting (projected)',
    'Shared PHP hosting or a small cloud instance plus a domain',
    'Approximately PKR 1,500–3,000 per month plus PKR 1,500 per year']],
  [1.8, 3.0, 1.15],
  9.5),
 ('h3', '3.9.3  Operational feasibility'),
 ('p',
  'The interaction model — a chat box, a multiple-choice card, a download '
  'list — is already familiar to the target users, which minimises the '
  'adoption barrier. The administrative console requires no database or '
  'command-line knowledge. The only operational task that requires technical '
  'skill is corpus ingestion, which is performed by the operator through '
  'three scripts and is required only when a new board, class or subject is '
  'added.'),
 ('h3', '3.9.4  Schedule feasibility'),
 ('p',
  'The work was scoped to twelve two-week sprints across the academic year. '
  'The highest-risk item, corpus ingestion and retrieval quality, was '
  'deliberately scheduled in the middle rather than at the end. A negative '
  'result would then still leave time to adjust the scope. The schedule was '
  'met, with the two-factor authentication and Google sign-in features '
  'arriving later than originally planned and voice support being dropped, '
  'as recorded in Section 1.5.2.'),
 ('h3', '3.9.5  Risk assessment'),
 ('table',
  'Principal project risks and mitigations',
  ['Risk', 'Likelihood', 'Impact', 'Mitigation adopted'],
  [['Retrieval returns irrelevant context from OCR-degraded text',
    'Medium',
    'High',
    'Aggressive rule-based cleaning; similarity floor of 0.20; manual '
    'inspection of retrieved excerpts before architectural commitment.'],
   ['Language-model cost grows uncontrollably with session length',
    'Medium',
    'High',
    'Rolling conversation summarisation; verbatim history capped at four '
    'turns; per-call cost logging to detect regressions.'],
   ['Model awards impossible scores',
    'Medium',
    'Medium',
    'Score parsed from a structured line and clamped in application code to '
    'the maximum for the question type.'],
   ['Third-party API outage during demonstration',
    'Low',
    'High',
    'Graceful degradation with an explanatory message; persisted transcripts '
    'so no student input is lost.'],
   ['Copyright exposure from redistributing textbooks',
    'Medium',
    'High',
    'Ingested material used for grounding only; downloads restricted to '
    'lawfully available documents.'],
   ['Scope growth beyond the available time',
    'High',
    'Medium',
    'Prioritised backlog; voice interaction and native mobile applications '
    'explicitly deferred.']],
  [1.9, 0.75, 0.65, 2.65],
  9.5),
 ('h2', '3.10  Requirement Traceability Matrix'),
 ('p',
  'Table 3.19 traces each requirement group forward to the design element '
  'that realises it, the implementation artefact that contains it and the '
  'test case that verifies it. The full test-case catalogue is given in '
  'Chapter 7.'),
 ('table',
  'Requirement traceability matrix',
  ['Requirements',
   'Design element',
   'Implementation artefact',
   'Verified by'],
  [['REQ-1 to REQ-7, REQ-26 to REQ-29',
    'Authentication subsystem (§4.4, §4.11)',
    '`Fortify` actions, `GoogleController`, `SecurityController`',
    'TC-01 to TC-12'],
   ['REQ-8 to REQ-11, REQ-30, REQ-31',
    'Academic scoping model (§5.2, §5.5)',
    '`Board`, `ClassLevel`, `Subject` enums; `SelectionController`; '
    '`CURRICULUM_DATA`',
    'TC-13 to TC-17'],
   ['REQ-12 to REQ-15, REQ-32 to REQ-35',
    'Teacher agent and retriever (§4.6–4.9)',
    '`teacher_bot.py`, `retriever.py`, `memory_manager.py`, `ChatController`',
    'TC-18 to TC-26'],
   ['REQ-16 to REQ-20, REQ-36 to REQ-38',
    'Assessment subsystem (§4.6, §5.7)',
    '`tester_bot.py`, `overall_evaluator.py`, `QuizController`',
    'TC-27 to TC-36'],
   ['REQ-21 to REQ-25, REQ-39',
    'Resource subsystem (§5.2, §5.5)',
    '`ResourceController`, `Admin\\ContentController`, `Content` model',
    'TC-37 to TC-42'],
   ['REQ-40, REQ-41',
    'Analytics subsystem (§5.2)',
    '`DashboardController`, `ProgressController`, `Activity` model',
    'TC-43 to TC-46'],
   ['REQ-42',
    'Administration subsystem (§4.11)',
    '`Admin\\UserController`, `Admin\\ContentController`, role attribute',
    'TC-47 to TC-52'],
   ['NFR-1 to NFR-5',
    'Performance design (§4.7, §4.9)',
    'LRU embedding cache, combined retrieval, summarisation',
    'TC-53 to TC-57'],
   ['NFR-6 to NFR-11',
    'Security architecture (§4.11)',
    'Middleware pipeline, hashed casts, environment configuration',
    'TC-58 to TC-63'],
   ['NFR-12 to NFR-19',
    'Quality attributes (§4.12, §6.1)',
    'Component structure, Pint and ESLint configuration, token logger',
    'TC-64 to TC-70']],
  [1.5, 1.5, 1.9, 1.05],
  9),
 ('h2', '3.11  Tools and Technologies'),
 ('p',
  'Table 3.20 records the technology selections and the reason each was '
  'chosen. Where the choice departs from the proposal, the reason for the '
  'change is stated. The official documentation of the principal frameworks '
  'and services was the primary reference throughout implementation (Google '
  'Cloud 2024)-(Inertia.js 2025).'),
 ('table',
  'Tools and technologies with selection rationale',
  ['Layer', 'Technology', 'Rationale'],
  [['Language (backend)',
    'PHP 8.4',
    'Typed enumerations, constructor property promotion and readonly '
    'properties give the domain model real type safety; widely available on '
    'inexpensive Pakistani hosting.'],
   ['Backend framework',
    'Laravel 13 (2025)',
    'Batteries-included authentication, migrations, validation, queueing and '
    'an expressive ORM; the largest team-familiar ecosystem.'],
   ['Authentication',
    'Laravel Fortify, Sanctum, Socialite',
    'Headless, audited implementations of registration, verification, '
    'password reset, TOTP two-factor and OAuth 2.0 — none of which should be '
    'written by hand.'],
   ['Frontend library',
    'React 19 (Meta Open Source 2025)',
    'Component model matched the interface; large ecosystem; team '
    'familiarity.'],
   ['SPA bridge',
    'Inertia.js v3',
    'Gives single-page navigation without building or versioning a separate '
    'REST API for page data, halving the integration surface.'],
   ['Styling',
    'Tailwind CSS v4 with shadcn/ui and Radix primitives',
    'Utility-first styling with accessible, unstyled component primitives; '
    'consistent design without a bespoke design system.'],
   ['Type-safe routing',
    'Laravel Wayfinder',
    'Generates TypeScript functions from Laravel routes so a renamed route '
    'becomes a compile-time error rather than a broken link.'],
   ['Charting',
    'Recharts',
    'Declarative React charts for the progress dashboard.'],
   ['Build tooling',
    'Vite 8',
    'Fast development server and optimised production bundles.'],
   ['AI service',
    'FastAPI on Uvicorn (Ramírez 2025)',
    "Python is where the AI client libraries live; FastAPI's Pydantic models "
    'give request validation and a typed contract at the service boundary.'],
   ['Language model',
    'OpenAI gpt-4o-mini',
    'Sufficient quality for grounded explanation and rubric-based marking at '
    'roughly one-sixteenth the input cost of the frontier model; cost is a '
    'first-class requirement here.'],
   ['Embeddings',
    'text-embedding-3-small (1,536-d)',
    'Inexpensive, strong retrieval quality, compact vectors.'],
   ['Vector store',
    'Pinecone (serverless, AWS us-east-1)',
    'Metadata pre-filtering during search — the property that makes board '
    'scoping structural — plus a free tier adequate for the corpus.'],
   ['OCR',
    'Google Cloud Vision',
    'Materially better than open-source engines on degraded scans and on '
    'Urdu script.'],
   ['Relational store',
    'MySQL 8',
    'Ubiquitous on target hosting; adequate JSON support for the areas '
    'columns.'],
   ['Testing',
    'Pest 4 on PHPUnit 12',
    'Expressive syntax over a mature runner; fast feedback in a small team.'],
   ['Code quality',
    'Laravel Pint, ESLint 9, Prettier 3, TypeScript 5.7',
    'Automated style and static analysis so review effort is spent on '
    'logic.'],
   ['Version control',
    'Git and GitHub',
    'Branch-per-concern workflow with merge points at sprint boundaries.'],
   ['Design',
    'Figma',
    'Wireframing and interface iteration before implementation.']],
  [1.15, 1.55, 3.25],
  9),
 ('note',
  'The proposal listed open-weight HuggingFace models (Hugging Face 2024) as '
  'an alternative AI provider and left the final model choice as a '
  'to-be-determined item in the Software Requirements Specification. The '
  'decision to use a hosted OpenAI model with an external vector index, '
  'rather than self-hosted open-weight models, was taken in Sprint 5 on '
  'grounds of cost and of the hardware available to the team: self-hosting '
  'an open-weight model of comparable quality would have required GPU '
  'infrastructure the project could not fund, whereas the metered API cost '
  'proved to be a fraction of a cent per interaction.',
  'Deviation from the proposal'),
 ('h2', '3.12  Summary'),
 ('p',
  'The project followed a twelve-sprint Agile process with '
  'demonstration-driven increments. Requirements were elicited from '
  'forty-eight students and were validated against their reported behaviour '
  'rather than against team assumptions; the survey results map onto '
  'specific requirements in Table 3.1. Two user classes were identified, '
  'with the student class dominating every design decision. Forty-two '
  'functional requirements and nineteen non-functional requirements were '
  'specified, the first twenty-five of the former carried forward unchanged '
  'from the defended Software Requirements Specification. Behavioural models '
  'were produced for use cases, state transitions and interaction sequences. '
  'The project was found feasible on technical, economic, operational and '
  'schedule grounds, with retrieval quality over OCR output identified as '
  'the principal risk and retired early by experiment. The next chapter '
  'turns this requirement set into an architecture.')]
