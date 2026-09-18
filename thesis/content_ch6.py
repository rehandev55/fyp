"""Content blocks for Chapter 6 - Implementation."""

BLOCKS = [('chapter', 'CHAPTER 6', 'IMPLEMENTATION'),
 ('p',
  'This chapter documents how the design was realised in code. It records '
  'the size of the delivered system, the development environment, the '
  'repository and its history, and then walks module by module through the '
  'implementation, with annotated listings taken directly from the delivered '
  'source.'),
 ('h2', '6.1  Introduction'),
 ('p',
  'This chapter documents how the design of Chapters 4 and 5 was realised in '
  'code. Section 6.2 records the development environment and the repository '
  'layout. Section 6.3 walks through the implementation of each module with '
  'annotated listings and screenshots of the resulting interface. Section '
  '6.4 describes the integration between the two runtimes. Section 6.5 '
  'records the engineering problems that were encountered and how each was '
  'resolved — including two that changed the design.'),
 ('h3', '6.1.1  Implementation statistics'),
 ('table',
  'Size of the delivered codebase',
  ['Part of the system', 'Files', 'Lines', 'Language'],
  [['Laravel application (app/)', '42', '1,845', 'PHP 8.4'],
   ['Routes and configuration', '17', '1,709', 'PHP 8.4'],
   ['Migrations, factories and seeders', '18', '698', 'PHP 8.4'],
   ['React interface, hand written', '100', '10,640', 'TypeScript / TSX'],
   ['FastAPI artificial-intelligence service', '18', '2,868', 'Python 3.12'],
   ['Automated test suite', '15', '753', 'PHP (Pest)'],
   ['Prompt templates', '4', '—', 'Plain text'],
   ['Total, excluding vendor and generated code', '214', '18,513', '—'],
   ['Wayfinder-generated route helpers (not counted above)',
    '71',
    '8,795',
    'TypeScript']],
  [2.55, 0.6, 0.8, 1.45],
  9),
 ('p',
  'Line counts exclude third-party dependencies and build output. The '
  'generated route helpers are listed separately because the Wayfinder tool '
  'produces them from the route definitions rather than a person writing '
  'them. They are real code that ships, but counting them as authored work '
  'would overstate the effort. Within the Python service the 2,868 lines '
  'divide into 828 lines of running service code, 879 lines of one-off '
  'ingestion scripts and 1,161 lines of test and evaluation harness.'),
 ('fig', 'fig_repo_codebase.png', 'Size of the delivered codebase.', 5.4),
 ('h2', '6.2  Development Environment and Repository Structure'),
 ('h3', '6.2.1  Environment'),
 ('table',
  'Development environment',
  ['Element', 'Configuration'],
  [['Operating system',
    'Windows 11 (development); Linux-compatible for deployment'],
   ['PHP runtime', 'PHP 8.4 with Composer 2'],
   ['Node runtime', 'Node.js with npm; Vite 8 development server'],
   ['Python runtime', 'Python 3.12 in a project-local virtual environment'],
   ['Database', 'MySQL 8 (`fyp_db`)'],
   ['Application server', '`php artisan serve` in development'],
   ['AI service', '`uvicorn main:app --port 8001`'],
   ['Concurrent start-up',
    '`composer run dev` starts the web server, the queue listener and Vite '
    'together'],
   ['Editors and tooling',
    'Visual Studio Code; Laravel Pint; ESLint; Prettier; TypeScript compiler '
    'in no-emit mode'],
   ['Version control', 'Git with a branch-per-concern workflow on GitHub']],
  [1.5, 4.45],
  10),
 ('h3', '6.2.2  Repository layout'),
 ('code',
  'Repository structure (abridged)',
  'fyp_backend/\n'
  '├── app/\n'
  '│   ├── Enums/                Board.php  ClassLevel.php  Subject.php\n'
  '│   ├── Http/\n'
  '│   │   ├── Controllers/\n'
  '│   │   │   ├── AIControllers/ AIController  ChatController  '
  'QuizController\n'
  '│   │   │   ├── Admin/         ContentController  DashboardController  '
  'UserController\n'
  '│   │   │   ├── Api/           AuthController\n'
  '│   │   │   ├── Auth/          GoogleController\n'
  '│   │   │   ├── Settings/      ProfileController  SecurityController\n'
  '│   │   │   └── DashboardController  PracticeController  '
  'ProgressController\n'
  '│   │   │       ResourceController   SelectionController  '
  'ProfileController\n'
  '│   │   ├── Middleware/        HandleAppearance  HandleInertiaRequests\n'
  '│   │   └── Requests/Settings/ ProfileUpdateRequest  '
  'PasswordUpdateRequest …\n'
  '│   ├── Models/                User  ChatSession  ChatMessage  '
  'QuizSession\n'
  '│   │                          QuizResult  Activity  Content\n'
  '│   ├── Providers/             AppServiceProvider  '
  'FortifyServiceProvider\n'
  '│   └── Services/              AIService.php\n'
  '├── ai-service/\n'
  '│   ├── main.py                FastAPI application and request/response '
  'models\n'
  '│   ├── teacher_bot.py         explanation agent\n'
  '│   ├── tester_bot.py          question generation and answer evaluation\n'
  '│   ├── overall_evaluator.py   session-level aggregation\n'
  '│   ├── memory_manager.py      conversation compression\n'
  '│   ├── rag/retriever.py       embedding cache, filtered vector search\n'
  '│   ├── prompts/               teacher.txt  tester.txt  evaluator.txt\n'
  '│   │                          overall_feedback.txt\n'
  '│   ├── utils/token_logger.py  per-call token and cost accounting\n'
  '│   └── scripts/               01_extract_text.py  02_clean_and_chunk.py\n'
  '│                              03_embed_and_store.py  test_*.py\n'
  '├── database/migrations/       15 migrations\n'
  '├── resources/js/\n'
  '│   ├── pages/                 welcome  dashboard  selection  ai-chat  '
  'practice\n'
  '│   │                          resources  progress  profile  about\n'
  '│   │                          auth/*  settings/*  admin/*\n'
  '│   ├── layouts/               app  auth  student  admin\n'
  '│   ├── components/            question-card  resource-card  app-sidebar  '
  'ui/*\n'
  '│   └── lib/api.ts             CSRF-aware fetch wrapper\n'
  '├── routes/                    web.php  api.php  settings.php  '
  'console.php\n'
  '└── tests/                     Feature/Auth/*  Feature/Settings/*  '
  'Unit/*'),
 ('h3', '6.2.3  Repository and version history'),
 ('p',
  'The project is held in a single Git repository at '
  'https://github.com/rehandev55/fyp, which contains the Laravel '
  'application, the React interface, the FastAPI service and the report '
  'build scripts together. A single repository was chosen over one per tier '
  'because the three tiers are versioned together. A change to the request '
  'contract in Section 4.9 touches a Python model, a PHP service class and a '
  'TypeScript type in the same commit. Splitting the repository would make '
  'such a change impossible to review as one unit.'),
 ('table',
  'Repository at the time of submission',
  ['Property', 'Value'],
  [['Remote', 'https://github.com/rehandev55/fyp'],
   ['Commits', '114 in total, 89 excluding merge commits'],
   ['Contributing accounts', '3'],
   ['Branches', 'main, backend, latest, pc and feature/ai-service'],
   ['First commit', '7 April 2026'],
   ['Most recent commit', '10 September 2026'],
   ['Active development window', 'Five months'],
   ['Largest month', 'May 2026, with 49 commits']],
  [1.85, 3.55],
  10),
 ('p',
  'Work followed a branch-per-concern pattern. The main branch holds '
  'integrated work. The backend branch carried the Laravel and database '
  'work, and feature/ai-service carried the FastAPI service while its '
  'contract was still moving. The pc and latest branches were short-lived, '
  'and were used to move work between the machines the team used. Branches '
  'were merged into main once the automated suite passed, which is the point '
  'at which the suite began to earn its keep.'),
 ('fig',
  'fig_repo_commits.png',
  'Commits to the project repository by month.',
  5.4),
 ('p',
  'The commit profile follows the sprint plan in Table 3.1 closely. April '
  'and May 2026 account for 76 of the 89 non-merge commits and cover the '
  'bulk of construction, from the first scaffold through authentication, the '
  'ingestion pipeline, the three agents and the practice module. Activity '
  'falls sharply in June, when effort moved from writing code to writing the '
  'Software Requirements Specification and preparing the mid-project review. '
  'The September commits are the final round: administrative user '
  'management, the dark theme, voice input on the tutor composer, the '
  'download redirect fix recorded in the defect log, and the evaluation '
  'harness of Section 7.6. This shape is typical of a student project with a '
  'fixed academic calendar, and is not in itself a fault in the process. It '
  'does mean the code was written faster than it was reviewed, which Section '
  '9.5 records as a limitation.'),
 ('h2', '6.3  Module Implementation'),
 ('h3', '6.3.1  Curricular vocabulary'),
 ('p',
  'The three enumerations are the smallest classes in the system and the '
  'most widely depended upon. Every retrieval filter, every page prop and '
  'every database column that carries academic scope resolves back to one of '
  'them.'),
 ('code',
  'Backed enumeration with display label',
  'namespace App\\Enums;\n'
  '\n'
  'enum ClassLevel: string\n'
  '{\n'
  "    case Class9  = 'class_9';\n"
  "    case Class10 = 'class_10';\n"
  "    case Class11 = 'class_11';\n"
  "    case Class12 = 'class_12';\n"
  '\n'
  '    public function label(): string\n'
  '    {\n'
  '        return match ($this) {\n'
  "            self::Class9  => 'Class 9',\n"
  "            self::Class10 => 'Class 10',\n"
  "            self::Class11 => 'Class 11',\n"
  "            self::Class12 => 'Class 12',\n"
  '        };\n'
  '    }\n'
  '}',
  'app/Enums/ClassLevel.php — Board and Subject follow the same shape'),
 ('p',
  'The stored value class_11 is precisely the value written into the class '
  'metadata field of every vector during ingestion, so a retrieval filter '
  'can be built directly from a model attribute with no mapping table. The '
  'label method is the only place the display form exists.'),
 ('code',
  'Attribute casting on the User model',
  'protected function casts(): array\n'
  '{\n'
  '    return [\n'
  "        'email_verified_at'       => 'datetime',\n"
  "        'password'                => 'hashed',\n"
  "        'two_factor_confirmed_at' => 'datetime',\n"
  "        'board'                   => Board::class,\n"
  "        'class_level'             => ClassLevel::class,\n"
  "        'subject'                 => Subject::class,\n"
  '    ];\n'
  '}',
  'app/Models/User.php'),
 ('p',
  'The hashed cast means a plain-text password assigned to the attribute is '
  'hashed on write, so it is not possible to store a password in recoverable '
  'form by forgetting to call the hasher. The three enumeration casts mean '
  'an invalid academic value cannot be read out of the database as a valid '
  'one.'),
 ('h3', '6.3.2  Authentication'),
 ('p',
  'Registration, login, email verification, password reset, password '
  'confirmation and two-factor authentication are provided by Laravel '
  'Fortify, configured headlessly so that the interface remains a set of '
  'React pages. Nothing in this area was written by hand, which is '
  'deliberate: authentication is the part of a web application where '
  'original work is least welcome.'),
 ('shot',
  'login',
  'The sign-in screen, showing email and password authentication alongside '
  'the federated Google option.',
  'Capture http://localhost:8000/login at 1440 × 900 in a clean browser '
  'window.'),
 ('p',
  'Federated sign-in is the one authentication path implemented directly. '
  'The controller redirects to Google, and on callback resolves the returned '
  'profile against the users table.'),
 ('code',
  'Google OAuth callback with account linking',
  'public function callback()\n'
  '{\n'
  "    $googleUser = Socialite::driver('google')->user();\n"
  '\n'
  "    $user = User::where('email', $googleUser->email)->first();\n"
  '\n'
  '    if (! $user) {\n'
  '        $user = User::create([\n'
  "            'name'              => $googleUser->name,\n"
  "            'email'             => $googleUser->email,\n"
  "            'password'          => bcrypt('google-auth'),\n"
  "            'role'              => 'user',\n"
  "            'status'            => 'Active',\n"
  "            'email_verified_at' => now(),\n"
  '        ]);\n'
  '    }\n'
  '\n'
  '    Auth::login($user);\n'
  '\n'
  "    return redirect('/dashboard');\n"
  '}',
  'app/Http/Controllers/Auth/GoogleController.php'),
 ('p',
  'Two details realise REQ-7 and REQ-26. The lookup by email address is what '
  'links a Google sign-in to an account first created with a password. A '
  'student who registers by email and later clicks the Google button '
  'therefore reaches the same profile, not a duplicate. And '
  'email_verified_at is set at creation, because Google has already verified '
  'the address and asking the student to verify it again would be a '
  'pointless obstacle.'),
 ('note',
  'Two weaknesses in this method are recorded honestly. The placeholder '
  'password is a fixed literal rather than a random string, and the role '
  "assigned on creation is 'user' where the rest of the system uses "
  "'student'. Neither is exploitable as written — the placeholder is "
  'bcrypt-hashed and the role string is only compared for equality with '
  "'admin' — but both are latent defects and are recorded as D-07 and D-08 "
  'in Section 7.7.',
  'Known defect'),
 ('shot',
  'security-2fa',
  'Two-factor authentication set-up on the account security page, showing '
  'the QR code and recovery codes.',
  'Capture http://localhost:8000/settings/security after enabling two-factor '
  'authentication; blur or replace the QR code before submission.'),
 ('h3', '6.3.3  Academic selection and profile'),
 ('p',
  'The selection page writes board, class and subject to the user record; '
  'every subsequent page reads them from the shared Inertia props. Some '
  'pages need the selection and may find the profile empty. The practice '
  'page is the important case. Those pages offer an inline selector instead '
  'of redirecting the student away from what they were trying to do.'),
 ('shot',
  'selection',
  'Academic selection: board, class and subject, with subject options '
  'dependent on the selected class.',
  'Capture http://localhost:8000/selection with a board and class already '
  'chosen so the dependent subject list is visible.'),
 ('shot',
  'profile',
  'The student profile page, showing personal information alongside the '
  'academic preferences that scope all generated content.',
  'Capture http://localhost:8000/profile for a signed-in student.'),
 ('h3', '6.3.4  The AI service boundary'),
 ('p', 'One class stands between the entire PHP codebase and the AI tier.'),
 ('code',
  'The sole adapter to the FastAPI service',
  'class AIService\n'
  '{\n'
  '    private string $baseUrl;\n'
  '\n'
  '    public function __construct()\n'
  '    {\n'
  "        $this->baseUrl = config('services.ai.url');\n"
  '    }\n'
  '\n'
  '    public function chat(string $question, string $board, string '
  '$classLevel,\n'
  '                         string $subject, $chatHistory = [], '
  '$existingSummary = null): array\n'
  '    {\n'
  '        $response = Http::post("{$this->baseUrl}/chat", [\n'
  "            'question'         => $question,\n"
  "            'board'            => $board,\n"
  "            'class_level'      => $classLevel,\n"
  "            'subject'          => $subject,\n"
  "            'chat_history'     => $chatHistory,\n"
  "            'existing_summary' => $existingSummary ?? '',\n"
  '        ]);\n'
  '\n'
  '        $data = $response->json();\n'
  '\n'
  '        return [\n'
  "            'reply'           => $data['reply'] ?? $data['answer'] ?? 'No "
  "response',\n"
  "            'updated_summary' => $data['updated_summary'] ?? null,\n"
  '        ];\n'
  '    }\n'
  '\n'
  '    public function generateQuiz(array $params): array  { … }\n'
  '    public function evaluateQuiz(array $params): array  { … }\n'
  '    public function overallQuiz(array $params): array   { … }\n'
  '}',
  'app/Services/AIService.php'),
 ('p',
  'The base URL comes from configuration rather than from a literal, so the '
  'service can be moved to another host without a code change. The '
  'null-coalescing chain on the response accommodates both possible key '
  'names and degrades to a readable string rather than a null-pointer error '
  'if the service returns something unexpected.'),
 ('h3', '6.3.5  Retrieval'),
 ('p',
  "The retriever is the component on which the project's central claim "
  'depends.'),
 ('code',
  'Cached embedding and metadata-filtered search',
  '_openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))\n'
  '_pc            = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))\n'
  '_index         = _pc.Index(os.getenv("PINECONE_INDEX"))\n'
  '\n'
  'EMBEDDING_MODEL = "text-embedding-3-small"\n'
  '\n'
  '\n'
  '@functools.lru_cache(maxsize=256)\n'
  'def _embed_cached(text: str) -> tuple:\n'
  '    response = _openai_client.embeddings.create(input=text, '
  'model=EMBEDDING_MODEL)\n'
  '    return tuple(response.data[0].embedding)      # tuple: hashable for '
  'the cache\n'
  '\n'
  '\n'
  'def embed_query(text: str) -> list[float]:\n'
  '    normalized = text.strip().lower()             # raises the cache hit '
  'rate\n'
  '    return list(_embed_cached(normalized))\n'
  '\n'
  '\n'
  'def retrieve(query, board, class_level, subject, top_k=5, doc_type=None) '
  '-> list[dict]:\n'
  '    query_vector = embed_query(query)\n'
  '\n'
  '    metadata_filter = {\n'
  '        "board":   {"$eq": board},\n'
  '        "class":   {"$eq": class_level},\n'
  '        "subject": {"$eq": subject},\n'
  '    }\n'
  '    if doc_type:\n'
  '        metadata_filter["type"] = {"$eq": doc_type}\n'
  '\n'
  '    results = _index.query(vector=query_vector, top_k=top_k,\n'
  '                           filter=metadata_filter, '
  'include_metadata=True)\n'
  '\n'
  '    return [\n'
  '        {"score": round(m.score, 4), "text": m.metadata.get("text", ""),\n'
  '         "subject": m.metadata.get("subject", ""), "type": '
  'm.metadata.get("type", ""),\n'
  '         "chunk_index": m.metadata.get("chunk_index", 0)}\n'
  '        for m in results.matches\n'
  '        if m.score >= 0.2                          # relevance floor\n'
  '    ]',
  'ai-service/rag/retriever.py'),
 ('p',
  'The provider clients are created once at import rather than per request, '
  'which removes connection set-up from the critical path. The cache returns '
  "a tuple because the standard library's cache requires a hashable result; "
  'the public wrapper converts it back to a list for the vector client. The '
  'three-way equality filter is the mechanism by which curricular scoping '
  'becomes structural.'),
 ('code',
  'Single-embedding combined retrieval for question generation',
  'def retrieve_combined(query, board, class_level, subject) -> str:\n'
  '    textbook_chunks   = retrieve(query, board, class_level, subject,\n'
  '                                 top_k=4, doc_type="textbook")\n'
  '    past_paper_chunks = retrieve(query, board, class_level, subject,\n'
  '                                 top_k=3, doc_type="past_papers")\n'
  '\n'
  '    seen_texts, all_chunks = set(), []\n'
  '    for chunk in textbook_chunks + past_paper_chunks:\n'
  '        key = chunk["text"][:100]\n'
  '        if key not in seen_texts:\n'
  '            seen_texts.add(key)\n'
  '            all_chunks.append(chunk)\n'
  '\n'
  '    return format_context(all_chunks)',
  'ai-service/rag/retriever.py'),
 ('p',
  'Both calls embed the same query string, so the second is served from the '
  'cache and costs nothing. An earlier version embedded the topic twice; '
  'consolidating it removed one metered API call from every '
  'question-generation request.'),
 ('h3', '6.3.6  The teacher agent and the chat module'),
 ('p',
  'The teacher agent composes the search query, retrieves, builds the '
  'message list through the memory manager, calls the model, logs the token '
  'usage and maintains the summary.'),
 ('code',
  'Context-aware query construction and generation',
  'if existing_summary and len(question.split()) < 6:\n'
  '    summary_context = existing_summary.split(".")[0]        # first '
  'sentence only\n'
  '    search_query = f"{summary_context}. '
  '{question}"[:MAX_SEARCH_QUERY_CHARS]\n'
  'else:\n'
  '    search_query = question[:MAX_SEARCH_QUERY_CHARS]        # 300 '
  'characters\n'
  '\n'
  'chunks  = retrieve(search_query, board, class_level, subject, top_k=5)\n'
  'context = format_context(chunks)\n'
  '\n'
  'system_prompt = PROMPT_TEMPLATE.format(board=board, '
  'class_level=class_level,\n'
  '                                       subject=subject, context=context,\n'
  '                                       question=question)\n'
  '\n'
  'messages, updated_summary = build_messages_with_memory(\n'
  '    system_prompt=system_prompt, chat_history=chat_history,\n'
  '    question=question, existing_summary=existing_summary)\n'
  '\n'
  'response = client.chat.completions.create(\n'
  '    model="gpt-4o-mini", messages=messages, temperature=0.3, '
  'max_tokens=1000)\n'
  '\n'
  'answer = response.choices[0].message.content',
  'ai-service/teacher_bot.py'),
 ('p',
  'The first branch fixes a real usability problem. A student who types '
  '“explain more” after an answer about the nitrogen cycle is still asking '
  'about the nitrogen cycle, but those two words on their own retrieve '
  'nothing. Prefixing the first sentence of the running summary restores the '
  'topic without lengthening the prompt materially.'),
 ('code',
  'Summary maintenance that cannot fail the request',
  'final_summary = updated_summary or existing_summary\n'
  'if answer and len(answer.split()) > 10:\n'
  '    try:\n'
  '        final_summary = _update_summary(\n'
  '            existing_summary=updated_summary or existing_summary,\n'
  '            new_messages=[{"role": "user",      "content": question},\n'
  '                          {"role": "assistant", "content": answer}])\n'
  '    except Exception as e:\n'
  '        print(f"[WARNING] Summary update failed: {e}")\n'
  '\n'
  'return {"answer": answer, "updated_summary": final_summary}',
  'ai-service/teacher_bot.py'),
 ('p',
  'Summary maintenance is a convenience, not a correctness requirement. If '
  'it fails, the student must still receive their answer, so the failure is '
  'logged and the previous summary is retained. The ten-word guard prevents '
  'a trivial exchange from consuming a summarisation call.'),
 ('p',
  'On the application side, ChatController resolves the academic scope, '
  'loads recent history, persists both sides of the exchange and updates the '
  'stored summary.'),
 ('code',
  'Scope resolution and history assembly in the chat controller',
  "$board = Board::tryFrom($request->input('board')) ?? $user->board ?? "
  'Board::Federal;\n'
  "$classLevel = ClassLevel::tryFrom($request->input('class_level'))\n"
  '              ?? $user->class_level ?? ClassLevel::Class10;\n'
  "$subject = Subject::tryFrom($request->input('subject'))\n"
  '              ?? $user->subject ?? Subject::Physics;\n'
  '\n'
  'if ($request->session_id) {\n'
  '    $session    = ChatSession::findOrFail($request->session_id);\n'
  '    $board      = $session->board;          // an existing session keeps '
  'its own scope\n'
  '    $classLevel = $session->class_level;\n'
  '    $subject    = $session->subject;\n'
  '} else {\n'
  '    $session = ChatSession::create([\n'
  "        'user_id'     => $user->id,\n"
  "        'title'       => substr($request->message, 0, 40),\n"
  "        'board'       => $board,\n"
  "        'class_level' => $classLevel,\n"
  "        'subject'     => $subject,\n"
  '    ]);\n'
  '}\n'
  '\n'
  "$history = ChatMessage::where('session_id', $session->id)\n"
  "    ->orderBy('created_at', 'desc')->take(10)->get()->reverse();\n"
  '\n'
  '$chatHistory = $history->map(fn ($m) => [\n'
  "    'role' => $m->role, 'content' => $m->message,\n"
  '])->values()->toArray();',
  'app/Http/Controllers/AIControllers/ChatController.php'),
 ('p',
  'The three-level fallback — request, then profile, then a safe default — '
  'means the chat endpoint never fails for want of an academic scope. The '
  'reassignment inside the first branch implements the design decision of '
  'Section 5.2.1: a resumed session keeps the scope it was created with, '
  'even if the student has since changed their profile.'),
 ('shot',
  'aichat',
  'The AI tutor interface: session list on the left, transcript in the '
  'centre and the composer beneath.',
  'Capture http://localhost:8000/aichat with an active conversation of at '
  'least four exchanges visible.'),
 ('shot',
  'aichat-answer',
  'A grounded explanation produced by the teacher agent, structured as '
  'definition, key points and example.',
  'Capture a single answer in the transcript, scrolled so the full response '
  'is visible; a Biology or Physics definition question works well.'),
 ('h3', '6.3.7  The practice and assessment module'),
 ('p',
  'The practice page holds the curriculum map — 379 chapters across 28 '
  'class-and-subject combinations — as a static structure keyed by class and '
  'subject. It is static because it is a curriculum, not data: it changes '
  'when a board revises its syllabus, not when a user acts.'),
 ('code',
  'Curriculum map and chapter lookup (abridged)',
  'const CURRICULUM_DATA = {\n'
  '  class_9: {\n'
  "    physics:   ['PHYSICAL QUANTITIES AND MEASUREMENT', 'KINEMATICS',\n"
  "                'DYNAMICS - I', 'DYNAMICS - II', … ],\n"
  "    chemistry: ['Nature of Science in Chemistry', 'Matter', 'Atomic "
  "Structure', … ],\n"
  '    …\n'
  '  },\n'
  '  class_10: { … }, class_11: { … }, class_12: { … },\n'
  '};\n'
  '\n'
  'function getChapters(classLevel: string, subject: string) {\n'
  '    if (!classLevel || !subject) return [];\n'
  '    const classData = (CURRICULUM_DATA as any)[classLevel];\n'
  '    if (!classData) return [];\n'
  '    return classData[subject] || [];\n'
  '}',
  'resources/js/pages/practice.tsx'),
 ('shot',
  'practice-scope',
  'Practice set-up: whole-book or selected-chapter scope with the chapter '
  "list of the student's class and subject.",
  'Capture http://localhost:8000/practice at the chapter-selection step with '
  'several chapters ticked.'),
 ('shot',
  'practice-type',
  'Question-type selection between multiple-choice, short and long formats, '
  'with the marks weighting shown.',
  'Capture the practice page at the question-type step.'),
 ('p',
  'Generated multiple-choice questions arrive as formatted text and are '
  'parsed on the client into a structure the question card can render.'),
 ('code',
  'Parsing generated multiple-choice items',
  'function parseQuestions(raw: string) {\n'
  '    return raw.split("\\n\\n").map((block) => {\n'
  '        const lines   = block.split("\\n");\n'
  '        const question = lines[0]?.replace(/^Q\\d+\\.\\s*/, "") || "";\n'
  '\n'
  '        const options = lines\n'
  '            .filter(line => line.match(/^[A-D]\\)/))\n'
  '            .map(line => line.replace(/^[A-D]\\)\\s*/, ""));\n'
  '\n'
  '        const correctLine   = lines.find(line => '
  'line.startsWith("Correct:"));\n'
  '        const correctLetter = correctLine?.split(":")[1]?.trim() || "";\n'
  '        const correctAnswer = ["A", "B", "C", '
  '"D"].indexOf(correctLetter);\n'
  '\n'
  '        const explanationLine = lines.find(line => '
  'line.startsWith("Explanation:"));\n'
  '        const explanation = explanationLine?.replace("Explanation:", '
  '"").trim() || "";\n'
  '\n'
  '        return { chapter: "", question, options, correctAnswer, '
  'explanation };\n'
  '    });\n'
  '}',
  'resources/js/pages/practice.tsx'),
 ('p',
  'This parser is the reason the tester prompt fixes an exact output format. '
  'The coupling between a prompt and a parser is a real and somewhat '
  'uncomfortable property of systems like this. The prompt is, in effect, an '
  'interface definition. Section 9.6 recommends replacing it with structured '
  'JSON output.'),
 ('shot',
  'practice-question',
  'A generated multiple-choice question with its past-paper provenance label '
  'and four options.',
  'Capture a rendered question card showing the ⭐ Past Paper or ~ Similar '
  'label.'),
 ('shot',
  'practice-feedback',
  'Per-answer feedback from the evaluator, showing the mark awarded and a '
  'two-sentence explanation of what was correct and what was missing.',
  'Capture the feedback state after submitting a short-question answer.'),
 ('p',
  'Marking is a pass-through on the application side. Aggregation, by '
  'contrast, is where the application takes control of every number the '
  'student sees.'),
 ('code',
  'Session aggregation and persistence',
  'public function overall(Request $request)\n'
  '{\n'
  '    $response = $this->ai->overallQuiz($request->all());\n'
  '\n'
  '    $session = QuizSession::create([\n'
  "        'user_id'          => $request->user()->id,\n"
  "        'subject'          => $request->subject,\n"
  "        'board'            => $request->board,\n"
  "        'class_level'      => $request->class_level,\n"
  "        'question_type'    => $request->question_type,\n"
  "        'total_score'      => $response['total_score'] ?? null,\n"
  "        'percentage'       => $response['percentage']  ?? null,\n"
  "        'grade'            => $response['grade']       ?? null,\n"
  "        'strong_areas'     => $response['strong_areas'] ?? [],\n"
  "        'weak_areas'       => $response['weak_areas']   ?? [],\n"
  "        'overall_feedback' => $response['overall_feedback'] ?? null,\n"
  "        'study_tip'        => $response['study_tip']        ?? null,\n"
  "        'completed_at'     => now(),\n"
  '    ]);\n'
  '\n'
  '    foreach ($request->results as $result) {\n'
  '        QuizResult::create([\n'
  "            'session_id'     => $session->id,\n"
  "            'user_id'        => $request->user()->id,\n"
  "            'question'       => $result['question']       ?? '',\n"
  "            'student_answer' => $result['student_answer'] ?? '',\n"
  "            'score'          => (float) ($result['score'] ?? 0),\n"
  "            'feedback'       => $result['feedback']       ?? '',\n"
  "            'is_correct'     => (float) ($result['score'] ?? 0) >= 5,\n"
  '        ]);\n'
  '    }\n'
  '\n'
  "    return response()->json(['session_id' => $session->id, "
  '...$response]);\n'
  '}',
  'app/Http/Controllers/AIControllers/QuizController.php'),
 ('note',
  'The is_correct flag is derived with a fixed threshold of five marks, '
  'which is correct for long questions and wrong for the other two types: a '
  'perfect multiple-choice answer scores one and is therefore recorded as '
  'incorrect. The flag is not used in any calculation the student sees — '
  'every displayed figure derives from the score column — so no reported '
  'result is affected, but the column is unreliable for future analytics. '
  'This is recorded as defect D-01 in Section 7.7 and the corrected form is '
  'given there.',
  'Known defect'),
 ('shot',
  'practice-result',
  'The session result: total score, percentage, grade band, strong and weak '
  'areas, encouragement and a study tip.',
  'Capture the completed-session summary after finishing a five-question '
  'practice test.'),
 ('h3', '6.3.8  Progress analytics'),
 ('code',
  'Subject-wise performance banding',
  "$subjects = QuizSession::selectRaw('subject, AVG(percentage) as score')\n"
  "    ->where('user_id', $userId)\n"
  "    ->groupBy('subject')\n"
  '    ->get()\n'
  '    ->map(function ($s) {\n'
  '        $score = round($s->score);\n'
  '        return [\n'
  "            'name'   => ucfirst($s->subject),\n"
  "            'score'  => $score,\n"
  "            'status' => $score >= 85 ? 'Excellent'\n"
  "                      : ($score >= 70 ? 'Strong'\n"
  "                      : ($score >= 60 ? 'Good' : 'Needs Work')),\n"
  '        ];\n'
  '    });\n'
  '\n'
  "$weakest    = $subjects->sortBy('score')->first();\n"
  '$focusArea  = $weakest\n'
  '    ? $weakest[\'name\'] . " needs more practice. Try taking more quizzes '
  'and "\n'
  '      . "reviewing AI explanations."\n'
  '    : "Great job! Keep practicing to maintain your performance.";',
  'app/Http/Controllers/ProgressController.php'),
 ('p',
  'Aggregation is performed in SQL rather than in PHP, so the number of rows '
  'transferred is the number of subjects rather than the number of attempts. '
  'The empty history case is handled explicitly, which is the state every '
  'new account is in.'),
 ('shot',
  'dashboard',
  'The student dashboard: progress summary tiles, quick actions and the '
  'recent activity feed.',
  'Capture http://localhost:8000/dashboard for an account with several '
  'completed quizzes so the tiles carry real values.'),
 ('shot',
  'progress',
  'The progress page: overall statistics, subject-wise performance with '
  'status bands and the focus recommendation.',
  'Capture http://localhost:8000/progress for an account with attempts in at '
  'least three subjects.'),
 ('h3', '6.3.9  Resource library and administration'),
 ('code',
  'Validated upload and accounted download',
  'public function store(Request $request)\n'
  '{\n'
  '    $request->validate([\n'
  "        'title'       => 'required',\n"
  "        'type'        => 'required',\n"
  "        'board'       => 'required',\n"
  "        'class_level' => 'required',\n"
  "        'subject'     => 'required',\n"
  "        'file'        => 'required|file|max:102400',      // 100 MB "
  'ceiling\n'
  '    ]);\n'
  '\n'
  "    $file = $request->file('file');\n"
  "    $path = $file->store('contents', 'public');\n"
  '\n'
  "    $content = Content::create([… 'file_path' => $path,\n"
  "                                   'file_size' => $file->getSize()]);\n"
  '\n'
  "    return response()->json(['success' => true, 'data' => $content]);\n"
  '}\n'
  '\n'
  'public function download($id)\n'
  '{\n'
  '    $content = Content::findOrFail($id);\n'
  "    $content->increment('downloads');\n"
  '\n'
  '    Activity::create([\n'
  "        'user_id' => Auth::id(),\n"
  "        'type'    => 'resource',\n"
  "        'message' => 'Downloaded ' . $content->title,\n"
  '    ]);\n'
  '\n'
  "    return response()->download(storage_path('app/public/' . "
  '$content->file_path));\n'
  '}',
  'app/Http/Controllers/Admin/ContentController.php'),
 ('shot',
  'resources',
  'The student resource library with board, class, subject and type filters.',
  'Capture http://localhost:8000/resources with several resources listed and '
  'a filter applied.'),
 ('shot',
  'admin-content',
  'The administrative content console: upload form and the resource table '
  'with edit and delete actions.',
  'Capture http://localhost:8000/admin/content signed in as an '
  'administrator.'),
 ('shot',
  'admin-users',
  'The administrative user console with search, role and status filters and '
  'per-account actions.',
  'Capture http://localhost:8000/admin/users; obscure real email addresses '
  'before submission.'),
 ('shot',
  'admin-dashboard',
  'The administrative overview showing aggregate counts and recent '
  'registrations.',
  'Capture http://localhost:8000/admin/dashboard.'),
 ('h3', '6.3.10  Cost instrumentation'),
 ('p',
  'Every call to a metered model passes through one logging function, which '
  'computes the monetary cost from the published rates and appends a '
  'structured record.'),
 ('code',
  'Per-call token and cost accounting',
  'PRICING = {\n'
  '    "gpt-4o-mini":            {"input": 0.150, "output": 0.600},   # USD '
  'per 1M tokens\n'
  '    "gpt-4o":                 {"input": 2.50,  "output": 10.00},\n'
  '    "text-embedding-3-small": {"input": 0.020, "output": 0.000},\n'
  '}\n'
  '\n'
  'def log_token_usage(endpoint, model, board, class_level, subject,\n'
  '                    prompt_tokens, completion_tokens):\n'
  '    pricing     = PRICING.get(model, {"input": 0, "output": 0})\n'
  '    input_cost  = (prompt_tokens     / 1_000_000) * pricing["input"]\n'
  '    output_cost = (completion_tokens / 1_000_000) * pricing["output"]\n'
  '    total_cost  = round(input_cost + output_cost, 8)\n'
  '\n'
  '    record = {\n'
  '        "timestamp": datetime.now().isoformat(), "endpoint": endpoint,\n'
  '        "model": model, "board": board, "class_level": class_level,\n'
  '        "subject": subject, "prompt_tokens": prompt_tokens,\n'
  '        "completion_tokens": completion_tokens,\n'
  '        "total_tokens": prompt_tokens + completion_tokens,\n'
  '        "cost_usd": total_cost,\n'
  '    }\n'
  '    with open(LOG_FILE, "a", encoding="utf-8") as f:\n'
  '        f.write(json.dumps(record) + "\\n")',
  'ai-service/utils/token_logger.py'),
 ('p',
  'Recording board, class and subject alongside the token counts lets the '
  'log answer questions the billing dashboard cannot. Which subject is most '
  'expensive to serve? Does long-question marking cost more than '
  'short-question marking? Has a prompt change increased consumption? The '
  'output is JSON Lines, so it can be analysed with a few lines of Python. '
  'Section 8.6 reports the analysis.'),
 ('h2', '6.4  Integration Between the Two Runtimes'),
 ('p',
  'The two runtimes are joined by four HTTP calls and one configuration '
  'value. The application reads services.ai.url from the environment, '
  'defaulting to http://127.0.0.1:8001 in development, and the AI service '
  'listens there. The service holds no database credential and issues no '
  'query; everything it needs arrives in the request body and everything it '
  'produces is returned for the caller to persist.'),
 ('p',
  'Request validation lives at the boundary rather than on both sides of it. '
  'Every field of every endpoint is declared as a Pydantic model attribute '
  'with explicit bounds. A question may be at most a thousand characters and '
  'an answer at most three thousand. A request may carry at most twenty '
  'history items, between one and twenty questions, and at most fifty '
  'results in a session aggregation. An over-long or malformed request is '
  'therefore rejected with a structured error before any metered operation '
  'begins.'),
 ('code',
  'Typed request contract at the service boundary',
  'class ChatRequest(BaseModel):\n'
  '    question:         str  = Field(..., max_length=MAX_QUESTION_LEN)   # '
  '1000\n'
  '    board:            str\n'
  '    class_level:      str\n'
  '    subject:          str\n'
  '    language:         str  = "en"\n'
  '    chat_history:     list = Field(default_factory=list, '
  'max_length=MAX_HISTORY_ITEMS)\n'
  '    existing_summary: str  = Field(default="", max_length=2000)\n'
  '\n'
  '\n'
  '@app.post("/chat", response_model=ChatResponse)\n'
  'def chat(req: ChatRequest):\n'
  '    try:\n'
  '        result = get_teacher_response(\n'
  '            question=req.question, board=req.board, '
  'class_level=req.class_level,\n'
  '            subject=req.subject, language=req.language,\n'
  '            chat_history=req.chat_history, '
  'existing_summary=req.existing_summary)\n'
  '        return ChatResponse(answer=result["answer"],\n'
  '                            updated_summary=result["updated_summary"])\n'
  '    except Exception as e:\n'
  '        raise HTTPException(status_code=500, detail=str(e))',
  'ai-service/main.py'),
 ('p',
  'These bounds are cost controls as well as correctness controls. They put '
  'a hard ceiling on the tokens any single request can be billed for. That '
  'is the difference between a bug that produces an error and a bug that '
  'produces an invoice.'),
 ('h2', '6.5  Engineering Challenges and Resolutions'),
 ('h3', '6.5.1  Refusing to answer because of a retrieval gap'),
 ('p',
  'The most instructive failure of the project appears in the development '
  'database. To the question “cell theory”, asked by a Class 11 Biology '
  'student, the system replied “This topic is not in your Class class_11 '
  'biology syllabus.” Cell theory is unambiguously in that syllabus. The '
  'problem was architectural, not curricular. That part of the corpus had '
  'not yet been ingested, so retrieval returned nothing above the similarity '
  'floor. The prompt of the time then told the model to decline whenever it '
  'had no context. The system was reporting a gap in its own index as a gap '
  "in the student's syllabus."),
 ('p',
  'Two other defects are visible in the same reply. The raw enumeration '
  'token class_11 leaked into user-facing text instead of the display label, '
  'and the refusal was worded as a statement of fact about the syllabus '
  "rather than about the system's own coverage. The fix was to rewrite the "
  'teacher prompt so that it separates the two cases. Prefer textbook '
  'content when it is retrieved. When it is not, answer from general '
  'knowledge and say so in a specified sentence. Never invent a textbook '
  'reference, and never reply that no response is available. Later '
  'transcripts in the same database show the corrected behaviour — a '
  'structured explanation of what software is, with system and application '
  'software distinguished and examples given, for a question that no '
  'textbook chunk matched.'),
 ('p',
  'The general lesson is the one the team regards as the most valuable of '
  'the project. In a retrieval-grounded system, absence of evidence is not '
  'evidence of absence. A design that treats the two as the same thing will '
  'confidently mislead the very users it is meant to help.'),
 ('h3', '6.5.2  Cost growth with conversation length'),
 ('p',
  'The first working chat implementation resent the entire transcript on '
  'every turn. The token log made the consequence visible immediately: input '
  'tokens, and therefore cost and latency, grew linearly with session '
  'length, so a productive forty-turn study session was disproportionately '
  'expensive precisely because it was productive. The resolution was the '
  'memory manager described in Sections 4.9 and 5.4.6. The instrumentation '
  'that made the problem visible was itself the reason it was caught in '
  'development rather than in an invoice.'),
 ('h3', '6.5.3  Optical character recognition noise'),
 ('p',
  'Raw recognition output from scanned board material proved unusable for '
  'retrieval. Publisher watermarks appeared on every page of the keybooks; '
  'examination papers carried roll-number boxes, board headers, time '
  'allocations and instruction lines; empty multiple-choice bubbles were '
  'recognised as strings of the letter o. Because these fragments repeat '
  'across hundreds of pages they behave as high-frequency noise and degrade '
  'the embedding of every chunk that contains them. The fix was two distinct '
  'rule sets: a general one, and a much more aggressive one applied only to '
  'documents typed as past papers. Both were developed by reading the '
  'recognised text of sample documents. Both are written as explicit regular '
  'expressions rather than as a learned filter, so that a wrongly deleted '
  'passage can be traced to the rule that deleted it.'),
 ('h3', '6.5.4  Memory exhaustion during ingestion'),
 ('p',
  'The first extraction script converted an entire PDF to page images before '
  'recognising any of them. On a six-hundred-page textbook this exhausted '
  'the memory of a development laptop. The resolution was to determine the '
  'page count first through pdfinfo, convert in batches of ten, and release '
  'each decoded image immediately after recognition. The resolution rate was '
  'also lowered from 200 to 150 dots per inch after comparison showed no '
  'measurable loss of recognition quality on this material.'),
 ('h3', '6.5.5  Losing an ingestion run to a network failure'),
 ('p',
  'Optical character recognition and embedding are the two metered '
  'operations in the pipeline, and an interruption after four hundred pages '
  'meant paying for those pages again. Every stage was made idempotent: '
  'extraction skips source files whose output JSON already exists, chunking '
  'skips documents already chunked, and embedding consults a log of '
  'successfully embedded identifiers written incrementally. A restart '
  'resumes where it stopped.'),
 ('h3', '6.5.6  Impossible marks'),
 ('p',
  'During evaluation testing the model occasionally returned a score outside '
  'the permitted range for the question type, and occasionally returned a '
  'response that did not match the required format at all. Trusting the '
  "model's number would have produced percentages above one hundred. The fix "
  'has two parts. The score is parsed from a designated line and clamped in '
  'code to the maximum for the question type. If parsing fails, the result '
  'is a score of zero with the raw text as feedback, rather than an '
  'exception. The same principle was then applied to session aggregation, '
  'where the totals, percentage and grade are computed in Python and written '
  'over whatever the model returned.'),
 ('h3', '6.5.7  Inconsistent stored vocabulary'),
 ('p',
  "Early development stored display strings — 'Federal Board', '9', "
  "'Physics' — while the vector index carried tokens — 'federal', 'class_9', "
  "'physics'. Retrieval filters therefore matched nothing for records "
  'created before the enumerations were introduced. The resolution was a '
  'reversible data migration that normalised the existing rows across three '
  'tables, and the introduction of backed enumerations so that the two '
  'vocabularies cannot diverge again.'),
 ('h3', '6.5.8  Cross-site request forgery in asynchronous calls'),
 ('p',
  'Inertia form submissions carry the CSRF token automatically; the '
  'asynchronous fetch calls used for chat, marking and file upload did not, '
  'and failed with a token mismatch. Rather than add the header at each of '
  'the several dozen call sites, one wrapper was written. It obtains the '
  'cookie if it is absent, attaches the token header and sets the content '
  'type. It deliberately omits the content type for FormData, so the browser '
  'can supply the multipart boundary itself. Setting that header by hand '
  'silently breaks uploads.'),
 ('code',
  'CSRF-aware fetch wrapper',
  'export async function api(path: string, options: RequestInit = {}): '
  'Promise<Response> {\n'
  '    await ensureCsrf();                                  // fetch cookie '
  'if missing\n'
  '\n'
  '    const headers: Record<string, string> = {\n'
  "        Accept: 'application/json',\n"
  '        ...(options.headers as Record<string, string>),\n'
  '    };\n'
  '\n'
  "    const xsrf = getCookie('XSRF-TOKEN');\n"
  "    if (xsrf) headers['X-XSRF-TOKEN'] = xsrf;\n"
  '\n'
  '    // do not set Content-Type for FormData — the browser must add the '
  'boundary\n'
  "    if (!(options.body instanceof FormData) && !headers['Content-Type']) "
  '{\n'
  "        headers['Content-Type'] = 'application/json';\n"
  '    }\n'
  '\n'
  "    return fetch(`/api${path}`, { credentials: 'include', ...options, "
  'headers });\n'
  '}',
  'resources/js/lib/api.ts'),
 ('h3', '6.5.9  Unbounded activity growth'),
 ('p',
  'The activity feed shows eight entries but was accumulating a row for '
  'every chat message, quiz completion and download indefinitely. Pruning '
  'immediately after insertion introduced a second problem: the pruning '
  'statement could delete the row the same request had just written. The '
  'resolution retains the eight most recent rows and deletes only rows older '
  'than three minutes, so a just-written row is never a candidate.'),
 ('h2', '6.6  Summary'),
 ('p',
  'The delivered system comprises approximately 18,500 lines of first-party '
  'code across three runtimes. Curricular vocabulary is expressed as backed '
  'enumerations whose stored values are identical to the metadata written '
  'into the vector index. Authentication is delegated to audited framework '
  'packages, with only the federated sign-in path written by hand. A single '
  'service class isolates the artificial-intelligence tier from the rest of '
  'the application. The retriever enforces curricular scoping as a metadata '
  'pre-filter and caches embeddings to avoid repeated metered calls. Marking '
  'is defended by parsing and clamping, and every displayed number is '
  'computed in application code. Nine engineering problems were encountered '
  'and resolved, two of which — the refusal caused by a retrieval gap and '
  'the cost growth with conversation length — changed the design rather than '
  'merely the code. The next chapter reports how the result was verified.')]
