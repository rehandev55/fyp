"""Content blocks for Chapter 5 - Detailed System Design."""

BLOCKS = [('chapter', 'CHAPTER 5', 'DETAILED SYSTEM DESIGN'),
 ('p',
  'This chapter takes the architecture of Chapter 4 down to the level of '
  'individual components. It gives the database design and data dictionary, '
  'the class model, a specification of each software component against a '
  'fixed set of attributes, the screen and navigation design, and the design '
  'of the four prompts that determine how the agents behave.'),
 ('h2', '5.1  Introduction'),
 ('p',
  'Chapter 4 established the tiers, the subsystems and the flows between '
  'them. This chapter descends to the level at which the system was actually '
  'built. Section 5.2 gives the database design with a complete data '
  'dictionary. Section 5.3 gives the class model. Section 5.4 specifies each '
  'software component against the ten standard component attributes. Section '
  '5.5 documents the interface design and navigation model. Section 5.6 '
  'presents the prompt designs, which in a system of this kind are as much a '
  'part of the design as any class. Section 5.7 gives the principal '
  'algorithms in pseudocode.'),
 ('h2', '5.2  Database Design'),
 ('h3', '5.2.1  Design objectives and normalisation'),
 ('p',
  'The relational schema was designed to meet four objectives. Every '
  'learning artefact must be traceable to a user. Deleting a user must leave '
  'no orphaned rows. The academic scope of a record must be recoverable from '
  'the record itself. And the analytics the dashboard needs must be '
  'answerable without joining more than two tables.'),
 ('p',
  'The schema is in third normal form with two deliberate departures. First, '
  'board, class level and subject are duplicated onto chat_sessions and '
  'quiz_sessions rather than being read from the owning user row. This is '
  'intentional denormalisation. A student may change their academic profile '
  'between sessions. A chat session held under Class 11 Physics must still '
  'be scoped to Class 11 Physics when it is resumed, even if the student has '
  'since switched to Class 12 Chemistry. The scope belongs to the session, '
  'not to the user. Second, the session-level aggregates on quiz_sessions — '
  'total score, percentage, grade — are stored rather than recomputed from '
  'quiz_results. They are stored because the grade band is a function of the '
  'marking scheme in force at the time of the attempt, and because the '
  'dashboard reads them on every page load.'),
 ('h3', '5.2.2  Entity-relationship model'),
 ('fig',
  'fig_erd.png',
  'Entity-relationship diagram of the MySQL schema, showing primary keys, '
  'foreign keys, cascade behaviour and cardinalities.',
  6.3),
 ('p',
  'The model has one aggregate root, users, from which three one-to-many '
  'relationships descend: to chat_sessions, to quiz_sessions and to '
  'activities. Two second-level relationships descend further, from '
  'chat_sessions to chat_messages and from quiz_sessions to quiz_results. '
  'Every foreign key on these paths is declared with ON DELETE CASCADE, so '
  'deleting a user removes their entire learning history in one operation '
  'and no orphan can survive. The contents table stands outside this '
  'hierarchy: a resource belongs to a board, class and subject rather than '
  'to a user, and is located by filtering rather than by traversal.'),
 ('note',
  'quiz_results carries a user_id column that duplicates the owner already '
  'reachable through session_id, and that column is declared without a '
  'foreign-key constraint. It exists so that the dashboard can count a '
  "student's attempted questions with a single-table query rather than a "
  'join. The absence of the constraint is an inconsistency rather than a '
  'design decision, and correcting it is listed in Section 9.6.',
  'Known schema inconsistency'),
 ('h3', '5.2.3  Data dictionary'),
 ('table',
  'Data dictionary — users',
  ['Column', 'Type', 'Constraints', 'Description'],
  [['id', 'BIGINT UNSIGNED', 'PK, auto-increment', 'Surrogate identifier.'],
   ['name',
    'VARCHAR(255)',
    'NOT NULL',
    'Display name; taken from the Google profile for federated accounts.'],
   ['email',
    'VARCHAR(255)',
    'NOT NULL, UNIQUE',
    'Login identifier and the key used to link a Google account to an '
    'existing profile.'],
   ['role',
    'VARCHAR(255)',
    "NOT NULL, default 'student'",
    "Authorisation role; 'admin' unlocks the administrative console."],
   ['status',
    'VARCHAR(255)',
    "NOT NULL, default 'Active'",
    'Account state; an administrator may set it to Blocked.'],
   ['password',
    'VARCHAR(255)',
    'NOT NULL',
    "Bcrypt hash applied by the model's hashed cast."],
   ['board',
    'VARCHAR(255)',
    'NULLABLE',
    'Academic profile; cast to the Board enumeration.'],
   ['class_level',
    'VARCHAR(255)',
    'NULLABLE',
    'Academic profile; cast to the ClassLevel enumeration.'],
   ['subject',
    'VARCHAR(255)',
    'NULLABLE',
    'Default subject; cast to the Subject enumeration.'],
   ['email_verified_at',
    'TIMESTAMP',
    'NULLABLE',
    'Set on verification; null blocks access to learning routes.'],
   ['two_factor_secret',
    'TEXT',
    'NULLABLE, encrypted',
    'TOTP shared secret.'],
   ['two_factor_recovery_codes',
    'TEXT',
    'NULLABLE, encrypted',
    'Single-use recovery codes.'],
   ['two_factor_confirmed_at',
    'TIMESTAMP',
    'NULLABLE',
    'Set when the second factor is confirmed.'],
   ['remember_token',
    'VARCHAR(100)',
    'NULLABLE',
    'Persistent-login selector.'],
   ['created_at / updated_at',
    'TIMESTAMP',
    'NULLABLE',
    'Framework timestamps.']],
  [1.5, 1.1, 1.35, 2.0],
  9),
 ('table',
  'Data dictionary — chat_sessions',
  ['Column', 'Type', 'Constraints', 'Description'],
  [['id', 'BIGINT UNSIGNED', 'PK', 'Surrogate identifier.'],
   ['user_id',
    'BIGINT UNSIGNED',
    'FK → users.id, ON DELETE CASCADE',
    'Owning student.'],
   ['title',
    'VARCHAR(255)',
    'NULLABLE',
    'Derived from the first 40 characters of the opening question.'],
   ['board',
    'VARCHAR(255)',
    'NULLABLE',
    'Academic scope frozen at session creation.'],
   ['class_level',
    'VARCHAR(255)',
    'NULLABLE',
    'Academic scope frozen at session creation.'],
   ['subject',
    'VARCHAR(255)',
    'NULLABLE',
    'Academic scope frozen at session creation.'],
   ['existing_summary',
    'LONGTEXT',
    'NULLABLE',
    'Rolling conversation summary maintained by the memory manager.'],
   ['created_at / updated_at',
    'TIMESTAMP',
    'NULLABLE',
    'Framework timestamps; ordering key for the session list.']],
  [1.5, 1.1, 1.55, 1.8],
  9),
 ('table',
  'Data dictionary — chat_messages',
  ['Column', 'Type', 'Constraints', 'Description'],
  [['id', 'BIGINT UNSIGNED', 'PK', 'Surrogate identifier.'],
   ['session_id',
    'BIGINT UNSIGNED',
    'FK → chat_sessions.id, ON DELETE CASCADE',
    'Owning session.'],
   ['role',
    "ENUM('user','assistant')",
    'NOT NULL',
    "Speaker; maps directly onto the model's message roles."],
   ['message', 'TEXT', 'NOT NULL', 'Utterance text.'],
   ['created_at / updated_at',
    'TIMESTAMP',
    'NULLABLE',
    'Ordering key for transcript replay.']],
  [1.4, 1.35, 1.6, 1.6],
  9),
 ('table',
  'Data dictionary — quiz_sessions',
  ['Column', 'Type', 'Constraints', 'Description'],
  [['id', 'BIGINT UNSIGNED', 'PK', 'Surrogate identifier.'],
   ['user_id',
    'BIGINT UNSIGNED',
    'FK → users.id, ON DELETE CASCADE',
    'Owning student.'],
   ['subject / board / class_level',
    'VARCHAR(255)',
    'NOT NULL',
    'Academic scope of the attempt.'],
   ['question_type',
    'VARCHAR(255)',
    'NOT NULL',
    'mcq, short or long; determines the marking scale.'],
   ['total_score',
    'VARCHAR(255)',
    'NULLABLE',
    "Human-readable 'earned / possible' string computed by the application."],
   ['percentage',
    'INT',
    'NULLABLE',
    'Rounded percentage; the key input to all analytics.'],
   ['grade',
    'VARCHAR(255)',
    'NULLABLE',
    'Band: Excellent, Good, Needs Work or Poor.'],
   ['strong_areas',
    'JSON',
    'NULLABLE',
    'Topics the student answered well, identified by the session evaluator.'],
   ['weak_areas', 'JSON', 'NULLABLE', 'Topics the student struggled with.'],
   ['overall_feedback',
    'TEXT',
    'NULLABLE',
    'Two to three sentences of encouragement and assessment.'],
   ['study_tip', 'TEXT', 'NULLABLE', 'Specific revision recommendation.'],
   ['completed_at',
    'TIMESTAMP',
    'NULLABLE',
    'Set when the session-level evaluation succeeds.'],
   ['created_at / updated_at',
    'TIMESTAMP',
    'NULLABLE',
    'Framework timestamps.']],
  [1.6, 1.0, 1.25, 2.1],
  9),
 ('table',
  'Data dictionary — quiz_results',
  ['Column', 'Type', 'Constraints', 'Description'],
  [['id', 'BIGINT UNSIGNED', 'PK', 'Surrogate identifier.'],
   ['session_id',
    'BIGINT UNSIGNED',
    'FK → quiz_sessions.id, ON DELETE CASCADE',
    'Owning attempt.'],
   ['user_id',
    'BIGINT UNSIGNED',
    'NOT NULL, no FK constraint',
    'Denormalised owner for single-table analytics; see the note in Section '
    '5.2.2.'],
   ['question',
    'TEXT',
    'NOT NULL',
    'Question text including its provenance label.'],
   ['student_answer',
    'TEXT',
    'NULLABLE',
    "The student's submitted answer, stored verbatim."],
   ['score',
    'FLOAT',
    'NOT NULL, default 0',
    'Marks awarded, clamped to the maximum for the question type.'],
   ['feedback',
    'TEXT',
    'NULLABLE',
    'Two to three sentences from the evaluator.'],
   ['is_correct',
    'BOOLEAN',
    'NOT NULL, default false',
    'Convenience flag derived from the score.'],
   ['created_at / updated_at',
    'TIMESTAMP',
    'NULLABLE',
    'Framework timestamps.']],
  [1.5, 1.15, 1.55, 1.75],
  9),
 ('table',
  'Data dictionary — contents and activities',
  ['Table.Column', 'Type', 'Constraints', 'Description'],
  [['contents.id', 'BIGINT UNSIGNED', 'PK', 'Surrogate identifier.'],
   ['contents.title',
    'VARCHAR(255)',
    'NOT NULL',
    'Display name of the resource.'],
   ['contents.type',
    'VARCHAR(255)',
    'NOT NULL',
    'Book, keybook or past paper.'],
   ['contents.board / class_level / subject',
    'VARCHAR(255)',
    'NOT NULL',
    'Filter keys used by the resource library.'],
   ['contents.file_path',
    'VARCHAR(255)',
    'NOT NULL',
    'Path relative to the public storage disk.'],
   ['contents.file_size',
    'VARCHAR(255)',
    'NULLABLE',
    'Size in bytes, captured at upload.'],
   ['contents.downloads',
    'INT',
    'NOT NULL, default 0',
    'Incremented on each successful download.'],
   ['activities.id', 'BIGINT UNSIGNED', 'PK', 'Surrogate identifier.'],
   ['activities.user_id',
    'BIGINT UNSIGNED',
    'FK → users.id, ON DELETE CASCADE',
    'Owning student.'],
   ['activities.type', 'VARCHAR(255)', 'NOT NULL', 'chat, quiz or resource.'],
   ['activities.message',
    'TEXT',
    'NOT NULL',
    'Human-readable description shown in the dashboard feed.'],
   ['activities.created_at',
    'TIMESTAMP',
    'NULLABLE',
    'Ordering key; also drives the pruning rule.']],
  [1.75, 1.05, 1.4, 1.75],
  9),
 ('h3', '5.2.4  Enumerations and value normalisation'),
 ('p',
  'Board, class level and subject are modelled as backed PHP enumerations '
  'rather than as free strings. The stored values are lower-case, '
  'underscore-delimited tokens — federal, ajk; class_9 to class_12; physics '
  'through urdu — and each enumeration carries a label method that returns '
  'the human-readable form for display. This gives three benefits. The '
  'compiler rejects an invalid value at every call site. The display form is '
  'defined in exactly one place. And the stored token is identical to the '
  'metadata value written into the vector index, so a retrieval filter can '
  'be built straight from a model attribute with no translation step.'),
 ('p',
  "Early development stored display strings such as 'Federal Board' and '9'. "
  'A dedicated data migration normalised the existing rows across the users, '
  'chat_sessions and contents tables to the token form, and is reversible. '
  'Retaining that migration in the repository is deliberate: it documents '
  'that the identity between the database token and the vector metadata '
  'value is a property the system depends on, not a coincidence.'),
 ('h2', '5.3  Class Design'),
 ('fig',
  'fig_class.png',
  'Class diagram of the core application classes, showing Eloquent models, '
  'the service class, controllers and the typed enumerations.',
  6.3),
 ('p',
  'The class model is deliberately thin. Eloquent models carry their '
  'attributes, casts and relationships and no business logic beyond that. '
  'Controllers hold the orchestration for one HTTP concern each. The single '
  'service class, AIService, is the only place in the PHP codebase that '
  'knows the AI tier is reached over HTTP. Enumerations carry the '
  'vocabulary.'),
 ('table',
  'Principal classes and their responsibilities',
  ['Class', 'Stereotype', 'Responsibility'],
  [['`User`',
    'Eloquent model',
    'Identity, credentials, role, status and academic profile; casts board, '
    'class level and subject to enumerations and the password to a hash; '
    'declares hasMany relationships to chat and quiz sessions.'],
   ['`ChatSession`',
    'Eloquent model',
    'One tutoring conversation, its frozen academic scope and its rolling '
    'summary.'],
   ['`ChatMessage`',
    'Eloquent model',
    'One utterance within a session, typed by role.'],
   ['`QuizSession`',
    'Eloquent model',
    'One completed practice attempt and its aggregate result.'],
   ['`QuizResult`',
    'Eloquent model',
    'One question, the answer given, the mark awarded and the feedback '
    'returned.'],
   ['`Activity`',
    'Eloquent model',
    'A single entry in the bounded recent-activity feed.'],
   ['`Content`',
    'Eloquent model',
    'A downloadable resource and its filter keys.'],
   ['`AIService`',
    'Service',
    'The sole adapter to the FastAPI tier; exposes chat, generateQuiz, '
    'evaluateQuiz and overallQuiz.'],
   ['`ChatController`',
    'Controller',
    'Session listing, transcript retrieval, message send with memory '
    'handling, and deletion.'],
   ['`QuizController`',
    'Controller',
    'Answer evaluation pass-through and session-level aggregation with '
    'persistence.'],
   ['`AIController`',
    'Controller',
    'Thin JSON pass-through for chat and quiz generation.'],
   ['`DashboardController`',
    'Controller',
    'Computes questions practised, average score, weakest subject and the '
    'activity feed.'],
   ['`ProgressController`',
    'Controller',
    'Computes per-subject averages, status bands and the focus '
    'recommendation.'],
   ['`ResourceController`',
    'Controller',
    'Supplies the resource library to the student page.'],
   ['`Admin\\ContentController`',
    'Controller',
    'Upload, list, download, edit and delete resources.'],
   ['`Admin\\UserController`',
    'Controller',
    'List, edit, block and delete accounts.'],
   ['`Auth\\GoogleController`',
    'Controller',
    'OAuth redirect and callback, including account linking.'],
   ['`Board`, `ClassLevel`, `Subject`',
    'Enumeration',
    'Curricular vocabulary with display labels.']],
  [1.55, 0.95, 3.45],
  9),
 ('h2', '5.4  Component Specifications'),
 ('p',
  'Each major software component is specified below against the ten standard '
  'component attributes: identification, type, purpose, function, '
  'subordinates, dependencies, interfaces, resources, processing and data.'),
 ('h3', '5.4.1  Authentication and Profile Component'),
 ('table',
  'Component specification — Authentication and Profile',
  ['Attribute', 'Specification'],
  [['Identification', 'AUTH-01, Authentication and Profile Component.'],
   ['Type',
    'Composite component spanning framework packages, controllers, form '
    'requests and page components.'],
   ['Purpose',
    'Establish and maintain the identity of every actor and hold the '
    'academic profile that scopes all subsequent content. Realises REQ-1 to '
    'REQ-7 and REQ-26 to REQ-30.'],
   ['Function',
    'Registration; password authentication with rate limiting; Google OAuth '
    '2.0 sign-in with account linking; email verification; password reset; '
    'optional TOTP two-factor with recovery codes; password confirmation for '
    'sensitive operations; profile and academic-selection update; account '
    'deletion.'],
   ['Subordinates',
    'Fortify registration, login, verification and reset actions; '
    '`GoogleController`; `Settings\\ProfileController`; '
    '`Settings\\SecurityController`; `ProfileController`; '
    '`SelectionController`; the auth page components under '
    'resources/js/pages/auth.'],
   ['Dependencies',
    'Laravel Fortify; Laravel Sanctum; Laravel Socialite; the mail transport '
    'for verification and reset messages; the users table; the Board, '
    'ClassLevel and Subject enumerations.'],
   ['Interfaces',
    'Provided: the `/login`, `/register`, `/forgot-password`, '
    '`/reset-password`, `/two-factor-challenge`, `/auth/google/redirect`, '
    '`/auth/google/callback` and `/settings/*` routes, plus `POST '
    '/api/register` and `POST /api/login`. Required: the Google OAuth '
    'endpoints and an SMTP transport.'],
   ['Resources',
    'One database connection; one outbound HTTPS connection during OAuth; '
    'the session store; the mail queue.'],
   ['Processing',
    'Credentials are validated and rate-limited; a successful password '
    'authentication either establishes a session or diverts to the '
    'two-factor challenge. An OAuth callback resolves the returned email '
    'against the users table and either logs in the matching account or '
    'creates one with the email pre-verified. The verified middleware '
    'rejects any learning request whose user has a null email_verified_at.'],
   ['Data',
    'users row including role, status, academic profile, hashed password and '
    'encrypted two-factor material; the session record; password-reset '
    'tokens.']],
  [1.1, 4.85],
  9),
 ('h3', '5.4.2  Retrieval Component'),
 ('table',
  'Component specification — Retrieval',
  ['Attribute', 'Specification'],
  [['Identification',
    'RAG-01, Retrieval Component (ai-service/rag/retriever.py).'],
   ['Type',
    'Python module providing pure functions over singleton provider '
    'clients.'],
   ['Purpose',
    "Return the passages of the student's own board, class and subject that "
    'are most relevant to a query, and format them as a context block. '
    'Realises REQ-11 and REQ-32.'],
   ['Function',
    '`embed_query` normalises and embeds a query with a least-recently-used '
    'cache; `retrieve` performs a metadata-filtered vector search with an '
    'optional document-type constraint and a similarity floor; '
    '`retrieve_combined` obtains textbook and past-paper context in one '
    'embedding call and deduplicates the union; `format_context` renders '
    'ranked excerpts for prompt interpolation.'],
   ['Subordinates',
    'The cached embedding function; the metadata-filter builder; the '
    'deduplication and formatting helpers.'],
   ['Dependencies',
    'The OpenAI embeddings API; the Pinecone index; environment '
    'configuration supplying both credentials and the index name.'],
   ['Interfaces',
    'Provided: `embed_query`, `retrieve`, `retrieve_combined`, '
    '`format_context` to the four agent modules. Required: '
    '`embeddings.create` and `index.query`.'],
   ['Resources',
    'One OpenAI client and one Pinecone client created once at import; '
    'approximately 1.5 megabytes of process memory for a 256-entry embedding '
    'cache.'],
   ['Processing',
    'The query is trimmed and lower-cased to raise the cache hit rate, '
    'embedded to 1,536 dimensions, and submitted with an equality filter on '
    'board, class and subject. Matches scoring below 0.20 are discarded. In '
    'combined mode, four textbook chunks and three past-paper chunks are '
    'retrieved, deduplicated on the first hundred characters and '
    'concatenated.'],
   ['Data',
    'Query string; 1,536-dimension float vector; ranked matches carrying '
    'score, text, subject, type and chunk index.']],
  [1.1, 4.85],
  9),
 ('h3', '5.4.3  Teacher Agent Component'),
 ('table',
  'Component specification — Teacher Agent',
  ['Attribute', 'Specification'],
  [['Identification', 'AI-01, Teacher Agent (ai-service/teacher_bot.py).'],
   ['Type', 'Python module exposing a single entry point.'],
   ['Purpose',
    'Produce a syllabus-grounded, exam-oriented explanation of a concept in '
    "the student's own language. Realises REQ-12 to REQ-15 and REQ-35."],
   ['Function',
    '`get_teacher_response` composes a search query, retrieves context, '
    'builds the prompt, assembles the message list with conversation memory, '
    'calls the model and returns the answer together with an updated '
    'conversation summary.'],
   ['Subordinates',
    'The retrieval component; the memory manager; the token logger.'],
   ['Dependencies',
    'prompts/teacher.txt, read once at import; the OpenAI chat-completions '
    'API; the shared retriever client.'],
   ['Interfaces',
    'Provided: `get_teacher_response(question, board, class_level, subject, '
    'language, chat_history, existing_summary) → {answer, updated_summary}`, '
    'surfaced by `POST /chat`. Required: retrieval and chat-completion.'],
   ['Resources',
    'One outbound HTTPS call for generation, one for retrieval when the '
    'embedding is not cached, and one for summary maintenance.'],
   ['Processing',
    'For a follow-up question of fewer than six words, the first sentence of '
    'the existing summary is prepended before embedding, and the composed '
    'query is truncated to 300 characters. Generation runs at temperature '
    '0.3 with a 1,000-token ceiling. The summary is updated only when the '
    'answer exceeds ten words, and a failure to update the summary is logged '
    'and swallowed rather than being allowed to fail the request.'],
   ['Data',
    'Question; academic scope; up to twenty prior turns; existing summary; '
    'retrieved context; generated answer; updated summary; token counts.']],
  [1.1, 4.85],
  9),
 ('h3', '5.4.4  Tester and Evaluator Component'),
 ('table',
  'Component specification — Tester and Evaluator',
  ['Attribute', 'Specification'],
  [['Identification',
    'AI-02, Tester and Evaluator (ai-service/tester_bot.py).'],
   ['Type', 'Python module exposing two entry points.'],
   ['Purpose',
    'Generate board-styled practice questions and mark free-text answers '
    'against the board marking scheme. Realises REQ-16 to REQ-19, REQ-36 and '
    'REQ-37.'],
   ['Function',
    '`generate_questions` produces the requested number of items of the '
    'requested type from combined textbook and past-paper context, each '
    'labelled by provenance. `evaluate_answer` marks one answer against '
    'retrieved context and returns a parsed score and short feedback.'],
   ['Subordinates',
    'The retrieval component in combined and simple modes; the '
    'structured-response parser; the score clamp; the token logger.'],
   ['Dependencies',
    'prompts/tester.txt and prompts/evaluator.txt; the chat-completions '
    'API.'],
   ['Interfaces',
    'Provided: `generate_questions(...) → str` and `evaluate_answer(...) → '
    '{score, feedback}`, surfaced by `POST /quiz/generate` and `POST '
    '/quiz/evaluate`.'],
   ['Resources',
    'One generation call per request; one retrieval per request; up to 2,000 '
    'output tokens for generation and 200 for evaluation.'],
   ['Processing',
    'Generation runs at temperature 0.4 with past-paper content given '
    'explicit priority in the prompt. Evaluation runs at temperature 0.2 and '
    'requires a response whose first line matches SCORE: n/m and whose '
    'second begins FEEDBACK:. The score is parsed from that line and clamped '
    'to 1, 3 or 8 according to question type; a malformed response yields a '
    'score of zero and the raw text as feedback rather than an exception.'],
   ['Data',
    'Topic or question; academic scope; question type and count; student '
    'answer; retrieved context; generated items or score and feedback.']],
  [1.1, 4.85],
  9),
 ('h3', '5.4.5  Session Evaluation Component'),
 ('table',
  'Component specification — Session Evaluation',
  ['Attribute', 'Specification'],
  [['Identification',
    'AI-03, Session Evaluator (ai-service/overall_evaluator.py).'],
   ['Type', 'Python module exposing a single entry point.'],
   ['Purpose',
    'Convert a completed attempt into a grade, strong and weak topic lists, '
    'encouragement and a revision recommendation. Realises REQ-19 and '
    'REQ-38.'],
   ['Function',
    '`get_overall_feedback` computes the arithmetic totals in Python, asks '
    'the model only for qualitative judgement, parses the structured reply '
    'and merges the two.'],
   ['Subordinates',
    'The structured-response parser; the grade-band function; the token '
    'logger.'],
   ['Dependencies',
    'prompts/overall_feedback.txt; the chat-completions API.'],
   ['Interfaces',
    'Provided: `get_overall_feedback(board, class_level, subject, '
    'question_type, results) → dict`, surfaced by `POST /quiz/overall`.'],
   ['Resources',
    'One generation call of at most 600 output tokens per completed '
    'attempt.'],
   ['Processing',
    'Total possible marks are computed as the number of questions multiplied '
    'by the per-type maximum, the percentage is rounded to two decimals, and '
    'the grade band is assigned at 80, 60 and 40 per cent. These values are '
    'computed in code and then written over whatever the model returns, so a '
    'model arithmetic error cannot reach the student. The model is asked '
    'only for STRONG_AREAS, WEAK_AREAS, OVERALL_FEEDBACK and STUDY_TIP.'],
   ['Data',
    'Per-question results; computed totals; parsed qualitative fields; the '
    'merged result dictionary.']],
  [1.1, 4.85],
  9),
 ('h3', '5.4.6  Conversation Memory Component'),
 ('table',
  'Component specification — Conversation Memory',
  ['Attribute', 'Specification'],
  [['Identification',
    'MEM-01, Memory Manager (ai-service/memory_manager.py).'],
   ['Type', 'Python module of pure functions plus one model call.'],
   ['Purpose',
    'Keep the prompt of a tutoring session bounded while preserving '
    'conversational continuity. Realises REQ-34 and NFR-5.'],
   ['Function',
    '`compress_history` splits a transcript into a verbatim tail and a '
    'compressible head; `_filter_messages` discards filler, short and '
    'duplicate turns; `_update_summary` maintains the rolling summary; '
    '`build_messages_with_memory` assembles the final message list.'],
   ['Subordinates',
    'The filler regular expression; the deduplication pass; the summariser '
    'prompt.'],
   ['Dependencies', 'The shared OpenAI client from the retrieval module.'],
   ['Interfaces',
    'Provided: `build_messages_with_memory(system_prompt, chat_history, '
    'question, existing_summary) → (messages, summary)` and '
    '`_update_summary`, both used by the teacher agent.'],
   ['Resources',
    'At most one additional model call per turn, capped at 200 output tokens '
    'at temperature zero.'],
   ['Processing',
    'Transcripts of four turns or fewer are passed through untouched. Longer '
    'transcripts retain the last four turns verbatim; when a summary already '
    'exists only the four newest of the older turns are considered, which '
    'makes summarisation incremental rather than quadratic. Turns matching '
    'the filler pattern, shorter than eight words, or duplicating an earlier '
    'turn are removed. If nothing survives filtering, the existing summary '
    'is returned unchanged and no model call is made.'],
   ['Data',
    'Message list of role and content pairs; existing summary; updated '
    'summary; assembled message list.']],
  [1.1, 4.85],
  9),
 ('h3', '5.4.7  Assessment Orchestration Component'),
 ('table',
  'Component specification — Assessment Orchestration',
  ['Attribute', 'Specification'],
  [['Identification',
    'APP-02, Assessment Orchestration (`QuizController`, `AIController`).'],
   ['Type', 'Laravel controller pair with an injected service.'],
   ['Purpose',
    'Mediate between the practice interface and the AI tier and persist '
    'every attempt. Realises REQ-16 to REQ-20 and REQ-38.'],
   ['Function',
    'Forward generation and evaluation requests; on session completion, '
    'obtain the aggregate result, create the quiz_sessions row, create one '
    'quiz_results row per question, append an activity entry and prune the '
    'feed.'],
   ['Subordinates',
    '`AIService`; the `QuizSession`, `QuizResult` and `Activity` models.'],
   ['Dependencies', 'Sanctum authentication; the AI service; MySQL.'],
   ['Interfaces',
    'Provided: `POST /api/quiz/generate`, `POST /api/quiz/evaluate`, `POST '
    '/api/quiz/overall`. Required: the four AIService methods.'],
   ['Resources',
    'One database transaction context per completed attempt; one outbound '
    'HTTP call per question and one per session.'],
   ['Processing',
    'Evaluation is a pass-through, so a single slow question cannot block '
    'the others. On completion the aggregate is requested first, the session '
    'row is written with the returned aggregate fields, and each result row '
    'is written with is_correct derived from the score. The activity feed is '
    'then pruned to the eight most recent entries older than three minutes.'],
   ['Data',
    'Question type; per-question results; aggregate result; persisted '
    'session and result rows.']],
  [1.1, 4.85],
  9),
 ('h3', '5.4.8  Content Management Component'),
 ('table',
  'Component specification — Content Management',
  ['Attribute', 'Specification'],
  [['Identification',
    'APP-03, Content Management (`Admin\\ContentController`, '
    '`ResourceController`).'],
   ['Type', 'Laravel controller pair with file-storage access.'],
   ['Purpose',
    'Curate and deliver downloadable study resources. Realises REQ-21 to '
    'REQ-25, REQ-39 and REQ-42.'],
   ['Function',
    'Validated upload with storage on the public disk; listing with board, '
    'class, subject and type filters; authenticated download with counter '
    'increment and activity logging; metadata edit; delete with file '
    'removal.'],
   ['Subordinates',
    'The `Content` model; the storage disk; the `Activity` model; the '
    'resource-card page component.'],
   ['Dependencies', 'Sanctum authentication; the filesystem; MySQL.'],
   ['Interfaces',
    'Provided: `POST|GET /api/content`, `GET /api/content/download/{id}`, '
    '`PUT|DELETE /api/content/{id}`, and the `/resources` and '
    '`/admin/content` pages.'],
   ['Resources',
    'Disk capacity for uploaded documents; an upload ceiling of 100 '
    'megabytes per file.'],
   ['Processing',
    'Uploads are validated on title, type, board, class, subject, file '
    'presence and size before storage, so a rejected upload creates no '
    'record. Deletion removes the stored file before the record, so a '
    'failure cannot leave a record pointing at nothing.'],
   ['Data',
    'contents rows; stored files under storage/app/public/contents; activity '
    'rows of type resource.']],
  [1.1, 4.85],
  9),
 ('h3', '5.4.9  Analytics Component'),
 ('table',
  'Component specification — Analytics',
  ['Attribute', 'Specification'],
  [['Identification',
    'APP-04, Analytics (`DashboardController`, `ProgressController`).'],
   ['Type',
    'Single-action Laravel controllers producing Inertia page props.'],
   ['Purpose',
    'Turn stored attempt history into an actionable picture of progress. '
    'Realises REQ-40 and REQ-41.'],
   ['Function',
    'Count questions practised; average the session percentages; group by '
    'subject to find the weakest; band each subject; compose a focus '
    'recommendation; return the recent activity feed.'],
   ['Subordinates',
    'The `QuizSession`, `QuizResult` and `Activity` models; the Recharts '
    'components on the progress page.'],
   ['Dependencies', 'Session authentication; MySQL aggregate functions.'],
   ['Interfaces',
    'Provided: the `/dashboard` and `/progress` pages with their props.'],
   ['Resources',
    'Four aggregate queries per dashboard load; five per progress load.'],
   ['Processing',
    'Subject averages are computed by a grouped AVG over quiz_sessions and '
    'banded at 85, 70 and 60 per cent into Excellent, Strong, Good and Needs '
    'Work. The weakest subject is the minimum of that grouping and becomes '
    'the focus recommendation. An empty history yields defined empty states '
    'rather than division by zero.'],
   ['Data',
    'Aggregated percentages by subject; counts; the eight most recent '
    'activity rows.']],
  [1.1, 4.85],
  9),
 ('h3', '5.4.10  Ingestion Pipeline Component'),
 ('table',
  'Component specification — Ingestion Pipeline',
  ['Attribute', 'Specification'],
  [['Identification',
    'ING-01, Ingestion Pipeline (ai-service/scripts/01–03).'],
   ['Type', 'Three sequential offline command-line scripts.'],
   ['Purpose',
    'Convert scanned board documents into a filtered, metadata-tagged vector '
    'index. Realises objective O2.'],
   ['Function',
    'Stage 1 rasterises and recognises text; stage 2 cleans, detects '
    'language and chunks; stage 3 embeds and upserts with resume support.'],
   ['Subordinates',
    'The path-metadata parser; the quality reporter; the general and '
    'past-paper cleaners; the chunker; the batch uploader; the '
    'embedded-identifier log.'],
   ['Dependencies',
    'Poppler; Google Cloud Vision with a service-account credential; the '
    'OpenAI embeddings API; the Pinecone control and data planes.'],
   ['Interfaces',
    'Provided: a command-line interface per stage. Required: the three '
    'external services above.'],
   ['Resources',
    'Ten decoded page images at a time; one hundred vectors per upsert '
    'batch; local disk for intermediate JSON and JSONL artefacts.'],
   ['Processing',
    'Every stage is idempotent: extraction skips source files whose output '
    'exists, chunking skips documents already chunked, and embedding '
    'consults the identifier log. Chunking uses a 2,800-character window '
    'with 400-character overlap, breaking at line or sentence boundaries and '
    'discarding fragments under 100 characters.'],
   ['Data',
    'Source PDFs; per-page JSON; chunk JSONL; 1,536-dimension vectors with '
    'board, class, subject, type, language, chunk index and truncated text '
    'metadata.']],
  [1.1, 4.85],
  9),
 ('h2', '5.5  User Interface Design'),
 ('h3', '5.5.1  Design principles'),
 ('bullets',
  [['One decision per screen. ',
    'The practice flow asks for chapter scope, then question type, then '
    'presents questions. Presenting all three at once was tried and '
    'abandoned during review because it produced a wall of controls before '
    'any value was delivered.'],
   ['The academic profile is ambient. ',
    'Once board, class and subject are set they are applied everywhere and '
    'shown in the header rather than re-requested. A student who has not set '
    'them is offered an inline selector on the page that needs them, rather '
    'than being redirected away from their task.'],
   ['Empty states carry instruction. ',
    'Every list — chat sessions, resources, progress, activity — has a '
    'designed empty state that says what will appear there and how to make '
    'it appear, because a new account sees empty states everywhere.'],
   ['Feedback is immediate and specific. ',
    'A marked answer shows the score, the feedback and the correct answer '
    'together, rather than deferring everything to the end of the session.'],
   ['Responsive from 360 pixels. ',
    'The sidebar collapses to a sheet, tables become stacked cards and the '
    'chat occupies the full viewport on a mobile device.']]),
 ('h3', '5.5.2  Navigation model'),
 ('fig',
  'fig_navigation.png',
  'Navigation map showing the public entry point, the authentication routes, '
  'the authenticated student area, the account settings group and the '
  'role-gated administrative area.',
  6.1),
 ('h3', '5.5.3  Screen inventory'),
 ('table',
  'Screen inventory',
  ['Route', 'Screen', 'Principal elements'],
  [['`/`',
    'Welcome',
    'Product proposition, feature summary, sign-in and registration entry '
    'points.'],
   ['`/login`',
    'Sign in',
    'Email and password fields, remember-me, Google button, links to '
    'registration and password reset.'],
   ['`/register`',
    'Register',
    'Name, email, password and confirmation with inline validation.'],
   ['`/forgot-password`, `/reset-password`',
    'Password recovery',
    'Email request form and token-bound reset form.'],
   ['`/two-factor-challenge`',
    'Two-factor challenge',
    'One-time-password input with a recovery-code alternative.'],
   ['`/dashboard`',
    'Student dashboard',
    'Progress summary tiles, quick actions and the recent-activity feed.'],
   ['`/selection`',
    'Academic selection',
    'Board, class and subject pickers with dependent options.'],
   ['`/aichat`',
    'AI tutor',
    'Session list, transcript, composer, new-session and delete controls.'],
   ['`/practice`',
    'Practice',
    'Scope selection, chapter multi-select, question-type selection, '
    'question card, per-answer feedback and the session result.'],
   ['`/resources`',
    'Resource library',
    'Filter bar and resource cards with type, size and download action.'],
   ['`/progress`',
    'Progress',
    'Overall statistics, subject-wise performance chart and focus '
    'recommendation.'],
   ['`/profile`',
    'Profile',
    'Personal information and academic preference update.'],
   ['`/settings/profile`, `/settings/security`, `/settings/appearance`',
    'Account settings',
    'Name and email, password change and two-factor management, light and '
    'dark theme.'],
   ['`/about`', 'About', 'Project purpose, team and technology summary.'],
   ['`/admin/dashboard`',
    'Admin overview',
    'Aggregate counts, recent registrations and quick links.'],
   ['`/admin/users`',
    'User management',
    'Searchable, filterable account table with edit, block and delete.'],
   ['`/admin/content`',
    'Content management',
    'Upload form and resource table with edit and delete.']],
  [1.6, 1.2, 3.15],
  9),
 ('h2', '5.6  Prompt Design'),
 ('p',
  'In a retrieval-grounded system the prompts are design artefacts of the '
  'same standing as the class model. They determine behaviour, they are '
  'versioned, and they live in separate template files that are loaded once '
  'at process start. Four templates exist, one per agent, and each is '
  'interpolated with the academic scope and the retrieved context before '
  'use.'),
 ('h3', '5.6.1  Teacher prompt'),
 ('p',
  'The teacher prompt first fixes the role and the scope. It then sets a '
  'source-priority policy. Prefer the retrieved textbook or keybook content. '
  'If the exact topic is absent, answer from general knowledge but say so in '
  'a specified sentence. Never invent a textbook reference or a page number. '
  'Never reply that no response is available. It then fixes the shape of the '
  'answer by question type. A definition gets a definition, a simple '
  'explanation, key points and an example. A comparison gets an X, Y and '
  'key-difference structure. A list question gets a numbered list. '
  'Mathematics gets a Given, To Find, Method and numbered-step layout that '
  'ends with units. Finally it fixes the language policy: reply in the '
  'language the student used, and keep Urdu natural and simple.'),
 ('note',
  'The instruction never to say “no response” and the explicit permission to '
  'fall back to general knowledge were added in response to an observed '
  'failure. Early transcripts in the development database contain the reply '
  '“This topic is not in your Class class_11 biology syllabus.” to the '
  'question “cell theory” — a topic that is plainly in the syllabus but was '
  'not retrieved because that portion of the corpus had not yet been '
  'ingested. The system was refusing on the basis of a retrieval gap rather '
  'than a curriculum gap, and the prompt now distinguishes the two. The '
  'incident is discussed in Section 6.5.',
  'Design decision traced to an observed failure'),
 ('h3', '5.6.2  Tester prompt'),
 ('p',
  'The tester prompt ranks its sources explicitly: past-paper questions '
  'first, because they recur, and textbook or keybook content second, for '
  'new items. It fixes the marks weighting at one, three and eight, and '
  'requires exactly the requested number of items of exactly the requested '
  'type. It also requires a provenance label on every question: a star for '
  'an item taken directly from a past paper, a tilde for an item written in '
  'past-paper style, and a filled star for an item newly written from the '
  'textbook. It then specifies the exact output layout for each question '
  'type, including the Correct and Explanation lines that the front end '
  'parses to build a multiple-choice card.'),
 ('h3', '5.6.3  Evaluator prompt'),
 ('p',
  'The evaluator prompt states the marking scheme, then describes each band '
  'within each question type. For a three-mark short question: three for '
  'complete and correct, two for mostly correct with minor omissions, one '
  'for partially correct and zero for incorrect. It tells the model to mark '
  'only against the supplied textbook content and never from outside '
  'knowledge. It must give one sentence on what was correct and one on what '
  'was missing. For mathematics it must name the exact wrong step. It must '
  'never exceed the maximum for the question type. It closes by fixing the '
  'output format to a SCORE line and a FEEDBACK line, which is what makes '
  'the response machine-parsable.'),
 ('h3', '5.6.4  Session-evaluation prompt'),
 ('p',
  'The session-evaluation prompt receives the full record of the attempt and '
  'the totals already computed by the application, and is told in terms to '
  'use those totals and not to recalculate them. It asks for four labelled '
  'fields in a fixed format: strong areas, weak areas, overall feedback and '
  'a study tip. It tells the model to be encouraging but honest, and to name '
  'topics rather than give generic advice.'),
 ('table',
  'Summary of the four prompt templates',
  ['Template', 'Fixes', 'Guards against'],
  [['`prompts/teacher.txt`',
    'Source priority, response shape by question type, bilingual policy, '
    'disclosure of general-knowledge answers',
    'Refusing to answer because of a retrieval gap; fabricated textbook '
    'references; over-long answers'],
   ['`prompts/tester.txt`',
    'Past-paper priority, provenance labels, marks weighting, exact output '
    'layout',
    'Out-of-syllabus questions; unparsable output; wrong item count or type'],
   ['`prompts/evaluator.txt`',
    'Marking bands per question type, mark-from-context rule, two-sentence '
    'feedback, SCORE and FEEDBACK lines',
    'Marks above the maximum; discursive feedback; marking from outside '
    'knowledge'],
   ['`prompts/overall_feedback.txt`',
    'Use of application-computed totals; four labelled output fields',
    'Model arithmetic errors reaching the student; vague, non-actionable '
    'advice']],
  [1.5, 2.3, 2.15],
  9),
 ('h2', '5.7  Algorithm Design'),
 ('h3', '5.7.1  Overlapping chunk segmentation'),
 ('code',
  'Overlapping chunk segmentation with boundary preference',
  'procedure CHUNK_TEXT(text, chunk_tokens = 700, overlap_tokens = 100)\n'
  '    char_size    ← chunk_tokens   × 4          // ≈ 2800 characters\n'
  '    char_overlap ← overlap_tokens × 4          // ≈ 400 characters\n'
  '    step         ← char_size − char_overlap    // ≈ 2400 characters\n'
  '    if step ≤ 0 then step ← char_size          // guard against '
  'non-advancing loop\n'
  '\n'
  '    chunks ← [] ; start ← 0\n'
  '    while start < length(text) do\n'
  '        end ← min(start + char_size, length(text))\n'
  '\n'
  '        if end < length(text) then                        // prefer a '
  'clean boundary\n'
  "            b ← last index of '\\n' in text[start .. end]\n"
  '            if b = −1 or (end − b) > 200 then\n'
  "                b ← last index of '. ' in text[start .. end]\n"
  '            if b ≠ −1 and b > start then end ← b + 1\n'
  '\n'
  '        piece ← trim(text[start .. end])\n'
  '        if length(piece) > 100 then append piece to chunks   // drop '
  'fragments\n'
  '\n'
  '        start ← start + step                  // always advance, never on '
  '`end`\n'
  '    return chunks',
  'Implemented in ai-service/scripts/02_clean_and_chunk.py'),
 ('p',
  'Two properties of this algorithm are worth noting. The cursor advances by '
  'a fixed step rather than by the position of the chosen boundary. '
  'Advancing on the boundary would let an awkward input, one with no '
  'boundary anywhere in a 2,800-character window, make no progress at all. '
  'And the boundary search is bounded: if the nearest line break is more '
  'than 200 characters back, the algorithm prefers a sentence break rather '
  'than discarding a fifth of the window.'),
 ('h3', '5.7.2  Filtered retrieval'),
 ('code',
  'Metadata-filtered semantic retrieval',
  'procedure RETRIEVE(query, board, class_level, subject, top_k = 5, '
  'doc_type = null)\n'
  '    normalised ← lowercase(trim(query))\n'
  '    if normalised ∈ embedding_cache then\n'
  '        vector ← embedding_cache[normalised]              // no metered '
  'call\n'
  '    else\n'
  '        vector ← EMBED(normalised, "text-embedding-3-small")\n'
  '        embedding_cache[normalised] ← vector              // LRU, '
  'capacity 256\n'
  '\n'
  '    filter ← { board: eq board, class: eq class_level, subject: eq '
  'subject }\n'
  '    if doc_type ≠ null then filter.type ← eq doc_type\n'
  '\n'
  '    matches ← INDEX.query(vector, top_k, filter, include_metadata = '
  'true)\n'
  '    return [ m ∈ matches where m.score ≥ 0.20 ]            // relevance '
  'floor',
  'Implemented in ai-service/rag/retriever.py'),
 ('h3', '5.7.3  Conversation memory compression'),
 ('code',
  'Bounded-prompt conversation memory',
  'procedure BUILD_MESSAGES(system_prompt, history, question, summary)\n'
  '    if length(history) ≤ 4 then\n'
  '        recent ← history ; new_summary ← summary\n'
  '    else\n'
  '        older  ← history[0 .. −5]\n'
  '        recent ← history[−4 ..]                       // verbatim tail\n'
  '        batch  ← (summary ≠ "") ? last 4 of older : older   // '
  'incremental\n'
  '        useful ← [ m ∈ batch where not FILLER(m)\n'
  '                                and word_count(m) ≥ 8\n'
  '                                and m not already seen ]\n'
  '        if useful = ∅ then\n'
  '            new_summary ← summary                     // no model call at '
  'all\n'
  '        else\n'
  '            new_summary ← SUMMARISE(summary, useful)  // ≤ 200 tokens, '
  'temp 0\n'
  '\n'
  '    messages ← [ system: system_prompt ]\n'
  '    if new_summary ≠ "" then\n'
  '        append system: "[Conversation so far]: " + new_summary\n'
  '    append each of recent\n'
  '    append user: question\n'
  '    return (messages, new_summary)',
  'Implemented in ai-service/memory_manager.py'),
 ('h3', '5.7.4  Score parsing, clamping and session aggregation'),
 ('code',
  'Defensive score handling and session aggregation',
  'procedure PARSE_AND_CLAMP(model_text, question_type)\n'
  '    score ← 0 ; feedback ← model_text\n'
  '    for each line in model_text do\n'
  '        if line starts with "SCORE:" then\n'
  '            try\n'
  "                score ← integer( part before '/' of value(line) )\n"
  '            catch\n'
  '                score ← 0                       // malformed → zero, '
  'never an exception\n'
  '        else if line starts with "FEEDBACK:" then\n'
  '            feedback ← value(line)\n'
  '\n'
  '    max_mark ← { mcq: 1, short: 3, long: 8 }[question_type] default 10\n'
  '    score    ← clamp(score, 0, max_mark)        // the model cannot '
  'exceed the scheme\n'
  '    return (score, feedback)\n'
  '\n'
  'procedure AGGREGATE_SESSION(results, question_type)\n'
  '    max_mark       ← { mcq: 1, short: 3, long: 8 }[question_type] default '
  '10\n'
  '    total_possible ← count(results) × max_mark\n'
  '    total_earned   ← Σ r.score for r ∈ results\n'
  '    percentage     ← total_possible > 0 ? round(100 × total_earned / '
  'total_possible, 2) : 0\n'
  '    grade          ← percentage ≥ 80 ? "Excellent"\n'
  '                   : percentage ≥ 60 ? "Good"\n'
  '                   : percentage ≥ 40 ? "Needs Work"\n'
  '                   :                   "Poor"\n'
  '\n'
  '    qualitative ← MODEL_JUDGEMENT(results)      // strong / weak areas, '
  'feedback, tip\n'
  '    return qualitative ⊕ { total_earned, total_possible, percentage, '
  'grade }\n'
  '    // the computed values overwrite anything the model returned for them',
  'Implemented in ai-service/tester_bot.py and '
  'ai-service/overall_evaluator.py'),
 ('p',
  'The final comment in that listing states the most important single rule '
  "in the system's design: the model is trusted for judgement and never for "
  'arithmetic. Every number a student sees is computed in code from values '
  "the model produced, and the computed values are written over the model's "
  'own totals rather than merged with them.'),
 ('h3', '5.7.5  Bounded activity feed'),
 ('code',
  'Activity insertion with bounded retention',
  'procedure RECORD_ACTIVITY(user_id, type, message)\n'
  '    INSERT into activities (user_id, type, message, created_at = now())\n'
  '\n'
  '    keep ← ids of the 8 most recent activities of user_id\n'
  '    DELETE from activities\n'
  '      where user_id = user_id\n'
  '        and created_at < now() − 3 minutes      // never delete a '
  'just-written row\n'
  '        and id ∉ keep',
  'Implemented in ChatController, QuizController and '
  'Admin\\ContentController'),
 ('p',
  'The three-minute grace condition exists because the pruning statement '
  'runs immediately after the insert. Without it, a burst of activity within '
  'a single request could delete a row that the same request had just '
  'written.'),
 ('h2', '5.8  Summary'),
 ('p',
  'The schema has seven application tables in third normal form, with two '
  'deliberate denormalisations. Academic scope is frozen onto session rows, '
  'and aggregate results are stored rather than recomputed. Each is '
  'justified by a specific behavioural requirement. The class model is '
  'intentionally thin, with a single service class isolating the '
  'artificial-intelligence tier. Ten components have been specified against '
  'the standard ten attributes. The interface design follows five stated '
  'principles and comprises seventeen screens across four route groups. The '
  'four prompt templates are treated as versioned design artefacts, and one '
  'of them carries a rule traceable to an observed production failure. Five '
  'algorithms have been given in pseudocode, of which the score-clamping and '
  "aggregation logic expresses the system's central safety rule: the model "
  'is trusted for judgement, never for arithmetic. The next chapter '
  'documents how this design was implemented.')]
