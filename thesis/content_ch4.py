"""Content blocks for Chapter 4 - System Architecture."""

BLOCKS = [('chapter', 'CHAPTER 4', 'SYSTEM ARCHITECTURE'),
 ('p',
  'This chapter presents the architecture of the system. It sets out the '
  'principles behind the split into tiers, the subsystems that resulted, the '
  'flow of data between them, the design of the artificial-intelligence tier '
  'that forms the technical core of the project, the contract between tiers, '
  'the security model and the deployment view.'),
 ('h2', '4.1  Introduction'),
 ('p',
  'This chapter presents the architecture of the Eternal Sunshine platform. '
  'It sets out the principles that guided the split into parts, the tiers '
  'and subsystems that resulted, and the flow of data between them. It then '
  'covers the design of the artificial-intelligence subsystem, which is the '
  'technical core of the work, followed by the interface contract between '
  'tiers, the security architecture and the design patterns applied. '
  'Detailed component-level design — the database schema, the class model '
  'and the algorithms — follows in Chapter 5.'),
 ('h2', '4.2  Architectural Design Approach'),
 ('p',
  'The architecture combines two styles. Vertically, the system is a layered '
  'architecture in the classical sense: presentation, application, '
  'artificial intelligence, and data. Each layer depends only on the layer '
  'beneath it, and no layer reaches upward. Horizontally, the boundary '
  'between the application layer and the artificial-intelligence layer is '
  'service-oriented: the two are separate processes in separate language '
  'runtimes communicating over HTTP with a JSON contract.'),
 ('p',
  'The decision to split the artificial-intelligence workload into its own '
  'service, rather than calling the model provider directly from PHP, was '
  'the single most consequential architectural decision in the project. Four '
  'considerations drove it.'),
 ('numbers',
  ['Ecosystem. The client libraries for embedding models, vector databases '
   'and language models are first-class in Python and second-class or absent '
   'in PHP. Writing the AI layer in Python meant using supported, '
   'documented, actively maintained libraries rather than reimplementing '
   'them.',
   'Independent evolution. Prompt text, model selection, retrieval '
   'parameters and chunking strategy changed far more often during '
   "development than the application's data model or its routes. Isolating "
   'them behind an HTTP boundary meant the AI service could be restarted and '
   'redeployed on its own cadence.',
   'Substitutability. Because the contract is four JSON endpoints, the '
   'entire AI service could be replaced — by a self-hosted open-weight '
   'model, by a different provider, or by a stub during testing — without '
   'touching a line of application code. This is the property that makes the '
   'requirement in Section 3.7.3 for maintainability real rather than '
   'aspirational.',
   'Failure isolation. A slow or failing model call cannot exhaust the web '
   "server's worker pool in the way an in-process synchronous call would; it "
   'fails at a clearly defined boundary where it can be caught and '
   'reported.']),
 ('p',
  'The cost of this decision is one additional network hop per AI request '
  'and one more process to deploy and supervise. Both were judged '
  'acceptable, and Section 8.5 quantifies the latency contribution of the '
  'hop as negligible relative to model inference time.'),
 ('h3', '4.2.1  Architectural principles'),
 ('bullets',
  [['Curricular scoping is structural. ',
    'Board, class and subject constrain retrieval as a metadata filter on '
    'the vector query. They are not requested in a prompt, because a prompt '
    'is advice and a filter is a guarantee.'],
   ['The application layer owns truth. ',
    'Scores, grades, totals and percentages are computed in application code '
    'from values the model produced, never accepted verbatim from the model. '
    'The model contributes judgement; the application contributes '
    'arithmetic.'],
   ["Persistence is the application layer's responsibility alone. ",
    'The AI service is stateless. It holds no database connection and no '
    'session state, which is what allows it to be scaled or replaced '
    'independently.'],
   ['Cost is a measured property. ',
    'Every model call is metered at the point of use and written to a '
    'structured log, so that a change which doubles token consumption is '
    'visible immediately rather than at the end of a billing period.'],
   ['Degrade with an explanation. ',
    'When an external dependency fails, the user sees a sentence describing '
    'what happened, and no user input is discarded.']]),
 ('h2', '4.3  High-Level Architecture'),
 ('p',
  'Figure 4.1 shows the complete architecture. Reading downward, the browser '
  'runs a React application whose page components are resolved by Inertia. '
  'The Laravel application server terminates every browser request, applies '
  'the middleware pipeline, and either renders an Inertia page or returns a '
  'JSON response. The FastAPI service performs retrieval and generation. The '
  'data layer holds relational state in MySQL, vector state in Pinecone and '
  'uploaded documents on disk, alongside the third-party identity and model '
  'services.'),
 ('fig',
  'fig_architecture.png',
  'Complete layered architecture with the components of each tier and the '
  'protocols used between them.',
  6.2),
 ('p',
  'Two properties of this diagram deserve emphasis. First, the browser never '
  'communicates with the AI service, with the vector index or with the model '
  'provider. Every such call is proxied through the Laravel application. '
  'That is what lets authentication, authorisation, rate limiting, '
  'persistence and activity logging be applied in one place, and it keeps '
  'the provider API key out of client code. Second, the Eloquent path from '
  'the application layer to MySQL bypasses the AI layer entirely: the AI '
  'service has no database access, by design.'),
 ('h2', '4.4  Subsystem Architecture'),
 ('h3', '4.4.1  Presentation subsystem'),
 ('p',
  'The presentation subsystem is a React 19 application of 100 components '
  'and pages totalling approximately 10,640 lines of TypeScript. Page '
  'components live under resources/js/pages and are resolved by name when '
  'the server returns an Inertia response. Three layout components — an '
  'authentication layout, a student layout with the sidebar navigation, and '
  'an administrative layout — wrap the pages and provide consistent chrome. '
  'Shared interface primitives such as buttons, dialogs, selects, tables and '
  'form inputs are Radix-based components under resources/js/components/ui. '
  'Two domain components, the question card and the resource card, hold the '
  'presentation logic that would otherwise be repeated across pages.'),
 ('p',
  'Communication with the server takes two forms. Page navigation and form '
  "submission use Inertia's router, which issues an XHR request and receives "
  'the props for the next page component, giving single-page behaviour '
  'without a separately versioned REST API for page data. Some operations do '
  'not change the page: sending a chat message, generating a quiz, '
  'submitting an answer for marking, uploading a file. These use a thin '
  'fetch wrapper in resources/js/lib/api.ts. The wrapper makes sure the CSRF '
  'cookie has been obtained, attaches the token header and sets the correct '
  'content type. It omits the content type for multipart uploads, so the '
  'browser can supply the boundary itself.'),
 ('h3', '4.4.2  Application subsystem'),
 ('p',
  'The Laravel application comprises 42 PHP classes and approximately 1,845 '
  'lines of code across controllers, models, enumerations, form requests, '
  'middleware and one service class. Its responsibilities are authentication '
  'and session management, authorisation, request validation, persistence '
  'through Eloquent, orchestration of calls to the AI service, activity '
  'logging, and the assembly of page props.'),
 ('p',
  'Routing is split by purpose. Session-authenticated page routes are '
  'declared in routes/web.php inside an auth and verified middleware group, '
  'with the administrative routes nested in a further prefixed group. Token- '
  'and cookie-authenticated JSON routes are declared in routes/api.php '
  'behind Sanctum. Account settings routes are separated into '
  'routes/settings.php. Several page controllers are single-action invokable '
  'classes, which keeps a controller that renders exactly one page from '
  'acquiring unrelated methods over time.'),
 ('h3', '4.4.3  Artificial-intelligence subsystem'),
 ('p',
  'The AI service is a FastAPI application of 18 Python modules and '
  'approximately 2,868 lines. It exposes four functional endpoints and two '
  'health endpoints. Every request and response shape is declared as a '
  'Pydantic model with explicit length and range bounds. The endpoints '
  'delegate to four agent modules, which share one retrieval module and one '
  'set of provider clients. The service is stateless: conversation history '
  'and the rolling summary are supplied by the caller on every request and '
  'returned in the response for the caller to persist.'),
 ('h3', '4.4.4  Data subsystem'),
 ('p',
  'Persistent state is divided across three stores according to its shape. '
  'MySQL holds the relational state — users, chat sessions and messages, '
  'quiz sessions and results, activities and content records — across nine '
  "application tables plus the framework's session, cache and queue tables. "
  'Pinecone holds the embedded corpus as 1,536-dimensional vectors with '
  'board, class, subject, type, language and chunk-index metadata. The local '
  'public disk holds uploaded resource files, referenced from the contents '
  'table by relative path so that the storage backend can later be changed '
  'to object storage without a schema change.'),
 ('fig',
  'fig_component.png',
  'Component diagram showing the provided and required interfaces across the '
  'application, artificial-intelligence, persistence and external-provider '
  'subsystems.',
  6.0),
 ('h2', '4.5  Data Flow'),
 ('h3', '4.5.1  Context diagram'),
 ('p',
  'Figure 4.3 places the system in its environment. Two human actors and '
  'three external service providers exchange data with the platform. The '
  'student supplies questions, answers and an academic selection, and '
  'receives explanations, generated questions, marks, feedback and '
  'downloadable files. The administrator supplies uploads and account '
  'actions and receives content records and usage statistics. The OpenAI '
  'platform receives prompts and text to embed, and returns completions and '
  'vectors. Pinecone receives filtered vector queries and returns ranked '
  'chunks. The Google platform supplies identity assertions at run time, and '
  'optical character recognition during offline ingestion.'),
 ('fig',
  'fig_context_dfd.jpg',
  'Context diagram (Data Flow Diagram level 0) showing the system boundary '
  'and the external entities that exchange data with it.',
  5.9),
 ('h3', '4.5.2  Level 1 decomposition'),
 ('p',
  'Figure 4.4 decomposes the system into five processes and six data stores. '
  'Process 1.0 authenticates users and maintains the academic profile '
  'against store D1. Process 2.0 conducts tutoring sessions, reading and '
  'writing the session and message stores D2 and calling the teacher agent. '
  'Process 3.0 generates and administers practice, and process 4.0 evaluates '
  'answers; both write to D3 and both call the tester and evaluator agents. '
  'Process 5.0 provides administration over the content store D4. Every '
  'process that represents a meaningful student action also appends to the '
  'activity store D5. Store D6, the vector index, is read exclusively by the '
  'AI agents and never by the application layer, which is the diagrammatic '
  'expression of the boundary described in Section 4.2.'),
 ('fig',
  'fig_dfd1.png',
  'Level 1 Data Flow Diagram showing the five principal processes, the six '
  'data stores and the interaction with the artificial-intelligence agents.',
  6.3),
 ('h2', '4.6  Artificial-Intelligence Subsystem Design'),
 ('p',
  'The AI subsystem is organised as four agents over one shared retrieval '
  'layer. The agents differ only in prompt, decoding parameters and token '
  'budget; they use the same model and the same retriever. This is a '
  'deliberate demonstration. Specialising by prompt, combined with retrieval '
  'grounding, is enough to get clearly different and reliable behaviour out '
  'of one general-purpose model. No fine-tuning was performed, and none was '
  'needed.'),
 ('table',
  'The four agents of the artificial-intelligence subsystem',
  ['Agent', 'Endpoint', 'Purpose', 'Temp.', 'Max tokens', 'Retrieval'],
  [['Teacher',
    '`POST /chat`',
    "Explain a concept in exam-oriented language, in the student's language, "
    'from the prescribed textbook.',
    '0.3',
    '1,000',
    'top-k = 5, unfiltered by type'],
   ['Tester',
    '`POST /quiz/generate`',
    "Generate MCQ, short or long questions in the board's style with "
    'provenance labels.',
    '0.4',
    '2,000',
    'top-k = 4 textbook + 3 past papers, combined and deduplicated'],
   ['Evaluator',
    '`POST /quiz/evaluate`',
    'Mark one free-text answer against the retrieved passage and the board '
    'marking scheme.',
    '0.2',
    '200',
    'top-k = 3'],
   ['Session evaluator',
    '`POST /quiz/overall`',
    'Aggregate a completed attempt into strong areas, weak areas, '
    'encouragement and a study recommendation.',
    '0.2',
    '600',
    'none — reasons over the session record'],
   ['Memory summariser',
    '(internal)',
    'Compress older conversation turns into a rolling four-to-six-sentence '
    'summary.',
    '0.0',
    '200',
    'none']],
  [1.05, 1.15, 2.0, 0.5, 0.65, 1.4],
  9),
 ('p',
  'Three observations about this table are worth drawing out. The '
  'temperature falls as the task becomes more nearly deterministic: question '
  'generation benefits from some variety, explanation from a little, marking '
  'from as little as possible, and summarisation from none at all. The token '
  "budget is matched closely to the expected output. The evaluator's ceiling "
  'was cut from 500 tokens to 200 once it became clear that two sentences is '
  'what a student actually reads. That change cut the output cost of the '
  'most frequently called endpoint by roughly sixty per cent. And the '
  'session evaluator performs no retrieval at all, because its input is the '
  "student's own session record rather than the textbook."),
 ('h2', '4.7  Knowledge Ingestion Pipeline'),
 ('p',
  'The corpus that grounds every generated answer is built offline by a '
  'four-stage pipeline, shown in Figure 4.5. The pipeline is run by the '
  'operator when a board, class or subject is added, and never at request '
  'time.'),
 ('fig',
  'fig_ingestion.png',
  'The four-stage offline ingestion pipeline, its intermediate artefacts and '
  'its idempotence property.',
  6.2),
 ('h3', '4.7.1  Stage 1 — acquisition and metadata by convention'),
 ('p',
  'Source documents are placed in a directory tree whose shape carries the '
  'metadata: data/raw/{board}/{class}/{subject}/{type}/file.pdf. The '
  'extraction script derives board, class, subject and document type from '
  'the path components rather than from a manifest file. Choosing convention '
  'over configuration removed a whole class of metadata-entry error. A Class '
  '9 chemistry past paper cannot be filed in the wrong place and still be '
  'tagged correctly, because the place is the tag.'),
 ('h3', '4.7.2  Stage 2 — optical character recognition'),
 ('p',
  'Pages are rasterised at 150 dots per inch through Poppler and submitted '
  "to Google Cloud Vision's text-detection endpoint one page at a time. "
  'Pages are processed in batches of ten and each page image is released '
  'immediately after recognition, because holding an entire six-hundred-page '
  'textbook as decoded images exhausts memory on a laptop. The output is one '
  'JSON document per source file. It holds the text of each page, character '
  'counts and the metadata derived in stage 1. Alongside it sits a quality '
  'report giving total characters, the number of near-empty pages and the '
  'mean characters per page. That report flags any document whose scan is '
  'too poor to be useful.'),
 ('h3', '4.7.3  Stage 3 — cleaning and chunking'),
 ('p',
  'Recognition output is not usable for retrieval without cleaning. Two rule '
  'sets are applied. The general set removes standalone page numbers, '
  'collapses runs of blank lines and spaces, strips publisher names and web '
  'addresses, removes bullet glyphs and repeated recognition artefacts, and '
  'deletes keybook watermarks. A second, more aggressive set of rules '
  'applies only to documents typed as past papers. It strips roll-number '
  'boxes, page-of-page references, board and examination headers, time and '
  'marks allocations, instruction lines, section headers and paper codes. It '
  'also removes the characteristic garbage produced by recognising empty '
  'multiple-choice bubbles. Language is then detected by measuring the '
  'proportion of characters in the Arabic-script Unicode range, and short '
  'broken lines are rejoined into sentences.'),
 ('p',
  'Cleaned text is segmented into chunks of approximately 2,800 characters '
  'with a 400-character overlap, preferring to break at a line boundary and '
  'falling back to a sentence boundary. The overlap exists because a '
  'definition that straddles a chunk boundary would otherwise be retrievable '
  'in neither half. Each chunk is written as one line of a JSONL file '
  'carrying a deterministic identifier composed of board, class, subject, '
  'type, source filename and chunk index.'),
 ('h3', '4.7.4  Stage 4 — embedding and indexing'),
 ('p',
  'Each chunk is embedded with text-embedding-3-small and upserted into a '
  'Pinecone serverless index of 1,536 dimensions using the cosine metric, in '
  'batches of one hundred vectors. The metadata written alongside each '
  'vector is board, class, subject, type, language, chunk index, and the '
  'first thousand characters of the chunk text. The text is stored so that '
  'retrieval returns readable context without a second lookup. Every '
  'successfully embedded identifier is appended to a log file, and the '
  'script consults that log on start-up, so an interrupted ingestion resumes '
  'without paying twice for the same embedding.'),
 ('note',
  'Idempotence is a property of every stage: extraction skips source files '
  'whose output JSON already exists, chunking skips documents already '
  'chunked, and embedding skips identifiers already recorded. This was not '
  'an elegance exercise. Optical character recognition and embedding are the '
  'only two metered operations in the pipeline, and a pipeline that must be '
  'restarted from the beginning after a failure at page 480 is a pipeline '
  'that costs money every time the network drops.',
  'Design rationale'),
 ('h2', '4.8  Retrieval and Generation at Request Time'),
 ('p',
  "Figure 4.6 traces a single tutoring request from the student's question "
  'to the displayed answer.'),
 ('fig',
  'fig_rag_flow.jpg',
  'Request-time Retrieval-Augmented Generation flow, including the embedding '
  'cache, the metadata-filtered vector search and the injection of '
  'conversation memory.',
  5.6),
 ('h3', '4.8.1  Query construction'),
 ('p',
  "The search query is not always the student's raw question. A short "
  'follow-up such as “why?” or “give an example” carries almost no '
  'retrievable signal on its own. When the question is shorter than six '
  'words and a conversation summary exists, the first sentence of the '
  'summary is prepended to the question to restore topical context before '
  'embedding. The composed query is truncated to 300 characters, which '
  'bounds the payload and prevents a long question from diluting the '
  'embedding with incidental words.'),
 ('h3', '4.8.2  Embedding with a cache'),
 ('p',
  'The query is normalised — trimmed and lower-cased — and embedded. A '
  'least-recently-used cache of 256 entries sits in front of the embedding '
  "call. The normalisation step exists to raise the hit rate: “What is Ohm's "
  "law” and “what is ohm's law  ” are the same cache key. The cache costs "
  'about 1.5 megabytes of process memory. In return it removes a network '
  'round trip and a metered API call on every repeated query. In a '
  'classroom, where many students ask the same question, that is a '
  'meaningful share of the traffic.'),
 ('h3', '4.8.3  Filtered vector search'),
 ('p',
  'The query vector is submitted to Pinecone with a metadata filter '
  'requiring exact equality on board, class and subject, and optionally on '
  'document type. This is the architectural heart of the system. The filter '
  'is applied during the search, not after it. The k results are therefore '
  "the k best matches within the student's own syllabus. They are not the k "
  'best matches overall, some of which happen to come from the right book. A '
  'similarity floor of 0.20 is then applied in application code, and matches '
  'below it are discarded. It is better to return no context at all, and let '
  'the teacher agent say it is answering from general knowledge. Returning '
  'an irrelevant passage would invite the model to invent a connection to '
  'it.'),
 ('h3', '4.8.4  Combined retrieval for question generation'),
 ('p',
  'The tester agent needs two kinds of material: past papers, from which '
  'real examination questions can be extracted, and textbook or keybook '
  'content, from which new questions can be written. A naive implementation '
  'embeds the topic twice and issues two independent searches. The '
  'implementation here embeds the query once, because the second call is '
  'served from the cache. It then issues one type-filtered search for four '
  'textbook chunks and another for three past-paper chunks. The union is '
  'de-duplicated on the first hundred characters of each chunk and formatted '
  'as a single context block. This removed one metered embedding call from '
  'every question-generation request.'),
 ('h3', '4.8.5  Context assembly and generation'),
 ('p',
  'Retrieved chunks are rendered as numbered excerpts, each annotated with '
  "its similarity score, and interpolated into the agent's prompt template "
  'together with the board, class and subject. The message list submitted to '
  'the model is then assembled as the system prompt, followed by the '
  'conversation summary if one exists, followed by the recent verbatim '
  "turns, followed by the student's question. The model's reply is returned "
  'to the application layer, which persists it and displays it.'),
 ('h2', '4.9  Conversation Memory Architecture'),
 ('p',
  'A tutoring conversation is inherently multi-turn: a student asks about '
  'photosynthesis, then asks a follow-up, then asks for an example. Naively, '
  'the entire transcript is resent on every turn, so the prompt — and '
  'therefore the input cost and the latency — grows linearly with the length '
  'of the session. A session of forty turns would cost roughly twenty times '
  'as much per turn as a session of two.'),
 ('p',
  'The memory manager bounds this growth. Figure 4.7 shows the strategy.'),
 ('fig',
  'fig_memory.png',
  'Conversation memory compression. Only the four most recent turns are '
  'resent verbatim; everything older is represented by a rolling summary '
  'that is itself capped at 200 tokens.',
  5.9),
 ('bullets',
  [['Recency window. ',
    'The four most recent turns are always resent verbatim, because the '
    'immediately preceding exchange is what a follow-up question refers to '
    'and paraphrasing it loses the referent.'],
   ['Filtering. ',
    'Before older turns are summarised they are filtered. A regular '
    'expression removes conversational filler — acknowledgements, greetings, '
    'single-word confirmations; messages of fewer than eight words are '
    'dropped; and exact duplicates are removed. Summarising “ok thanks” '
    'consumes tokens and contributes nothing.'],
   ['Rolling summarisation. ',
    'Surviving older turns are sent to the model with a dedicated system '
    'prompt instructing it to maintain four to six sentences capturing '
    "topics covered, the student's apparent level of understanding, "
    'misconceptions observed, explanations that worked and questions left '
    'open. Temperature is zero and the output is capped at 200 tokens. The '
    'result replaces the previous summary.'],
   ['Persistence. ',
    'The summary is stored on the chat session row, so it survives the '
    'student closing the browser and is reloaded when the session is '
    'resumed.']]),
 ('p',
  'The effect is that prompt size approaches a constant as a session '
  'lengthens: a system prompt with retrieved context, plus a bounded '
  'summary, plus four turns. Cost per turn therefore becomes approximately '
  'independent of session depth. The trade-off is one extra model call per '
  'turn to maintain the summary. That call runs at temperature zero against '
  'a 200-token output ceiling, so it costs far less than the input tokens it '
  'prevents. Section 8.6 quantifies the saving.'),
 ('h2', '4.10  Interface Contract Between Tiers'),
 ('p',
  'The application layer reaches the AI service through a single class, '
  'AIService, which owns the base URL and exposes one method per endpoint. '
  'No other application class knows that the AI service exists as an HTTP '
  'resource. Table 4.2 records the contract.'),
 ('table',
  'Contract between the Laravel application and the FastAPI AI service',
  ['Endpoint', 'Request fields', 'Response fields'],
  [['`POST /chat`',
    '`question` (≤1000), `board`, `class_level`, `subject`, `language`, '
    '`chat_history` (≤20), `existing_summary` (≤2000)',
    '`answer`, `updated_summary`, `success`'],
   ['`POST /quiz/generate`',
    '`topic` (≤500), `board`, `class_level`, `subject`, `question_type`, '
    '`num_questions` (1–20)',
    '`questions` (formatted text), `success`'],
   ['`POST /quiz/evaluate`',
    '`question` (≤1000), `student_answer` (≤3000), `board`, `class_level`, '
    '`subject`, `question_type`',
    '`feedback`, `score`, `success`'],
   ['`POST /quiz/overall`',
    '`board`, `class_level`, `subject`, `question_type`, `results` (≤50 '
    'objects of question, student_answer, score 0–10, feedback)',
    '`total_score`, `percentage`, `grade`, `strong_areas`, `weak_areas`, '
    '`overall_feedback`, `study_tip`, `success`'],
   ['`GET /`, `GET /health`', 'none', 'service status and version']],
  [1.15, 2.5, 2.3],
  9),
 ('p',
  'Every bound in the request column is enforced by a Pydantic field '
  'constraint rather than a hand-written check. A malformed or oversized '
  'request is therefore rejected with a structured validation error before '
  'any metered operation begins. The upper bounds are cost controls as much '
  'as correctness controls: they place a hard ceiling on the number of '
  'tokens any single request can cause to be billed.'),
 ('h3', '4.10.1  Application API surface'),
 ('table',
  'HTTP API exposed by the Laravel application',
  ['Method and path', 'Purpose', 'Guard'],
  [['`POST /api/register`, `POST /api/login`',
    'Token-based authentication for API clients',
    'public'],
   ['`POST /api/logout`, `GET /api/user`',
    'Session teardown and identity',
    'sanctum'],
   ['`POST /api/chat/send`',
    'Send a tutoring message; creates a session on first use',
    'sanctum'],
   ['`GET /api/chat/sessions`',
    "List the caller's chat sessions, most recent first",
    'sanctum'],
   ['`GET /api/chat/messages/{id}`',
    'Load the transcript of one session',
    'sanctum'],
   ['`GET /api/chat/history/{id}`',
    'Transcript formatted as role/content pairs for the model',
    'sanctum'],
   ['`DELETE /api/chat/{id}`',
    'Delete a session and its messages',
    'sanctum'],
   ['`POST /api/quiz/generate`', 'Generate practice questions', 'sanctum'],
   ['`POST /api/quiz/evaluate`', 'Mark one submitted answer', 'sanctum'],
   ['`POST /api/quiz/overall`',
    'Aggregate and persist a completed attempt',
    'sanctum'],
   ['`GET|POST /api/content`', 'List and upload resources', 'sanctum'],
   ['`GET /api/content/download/{id}`',
    'Stream a resource and increment its counter',
    'sanctum'],
   ['`PUT|DELETE /api/content/{id}`', 'Edit or remove a resource', 'sanctum'],
   ['`GET /api/users`, `PUT|DELETE /api/users/{id}`, `PATCH '
    '/api/users/toggle/{id}`',
    'Administrative account management',
    'sanctum']],
  [2.15, 2.75, 1.05],
  9),
 ('note',
  'The administrative endpoints under /api are guarded by authentication but '
  'their role check is applied at the page layer rather than at the route '
  'layer. This is recorded as a known weakness in Section 7.7 and as a '
  'recommendation in Section 9.6: the correct fix is a dedicated role '
  'middleware applied to the route group, so that authorisation does not '
  'depend on the caller having arrived through the administrative interface.',
  'Known limitation'),
 ('h2', '4.11  Security Architecture'),
 ('p',
  'Security is applied in depth across five bands, informed by the OWASP '
  'catalogue of web application risks (2021).'),
 ('table',
  'Security controls by architectural band',
  ['Band', 'Control', 'Implementation'],
  [['Transport',
    'Encryption in transit',
    'HTTPS to the browser; TLS on every outbound call to OpenAI, Pinecone '
    'and Google.'],
   ['Identity',
    'Credential handling',
    "Bcrypt hashing via the framework's hashed cast; passwords never logged; "
    'password-reset tokens single-use and expiring.'],
   ['Identity',
    'Federated sign-in',
    'Google OAuth 2.0 through Socialite; the account is linked by email '
    'address if one already exists, otherwise created with the email marked '
    'verified.'],
   ['Identity',
    'Second factor',
    'Optional TOTP with encrypted secret and encrypted recovery codes; '
    'challenge screen enforced before session establishment.'],
   ['Session',
    'Request integrity',
    'CSRF token required on every state-changing request; the client wrapper '
    'obtains and attaches it automatically.'],
   ['Session',
    'Abuse resistance',
    'Rate limiting on login and on password update; email verification '
    'required before learning features are reachable.'],
   ['Authorisation',
    'Role separation',
    'A role attribute on the user record distinguishes student from '
    'administrator and gates the administrative interface and navigation.'],
   ['Data',
    'Ownership scoping',
    'Chat, quiz and activity queries are constrained to the authenticated '
    "user's identifier; cascading deletes remove dependent rows with the "
    'parent.'],
   ['Data',
    'Input bounds',
    'Length and range constraints on every AI request field; upload size '
    'limit of 100 megabytes; validation of every content field.'],
   ['Secrets',
    'Credential storage',
    'All API keys and database credentials supplied through environment '
    'variables and excluded from version control.']],
  [0.95, 1.5, 3.5],
  9),
 ('fig',
  'fig_auth.png',
  'Authentication and authorisation flow covering password sign-in, Google '
  'OAuth sign-in, account linking, two-factor challenge and role resolution.',
  6.0),
 ('h2', '4.12  Design Patterns Applied'),
 ('table',
  'Design patterns used and where they appear',
  ['Pattern', 'Where applied', 'Benefit obtained'],
  [['Layered architecture',
    'The four tiers of Figure 4.1',
    'Dependencies point in one direction only; each tier is separately '
    'comprehensible and separately testable.'],
   ['Model-View-Controller',
    'Laravel controllers, Eloquent models, React pages as views',
    'Conventional separation that a maintainer already understands.'],
   ['Service layer',
    '`AIService`',
    'The HTTP nature of the AI tier is known to exactly one class; four '
    'controllers depend on a method signature rather than on a protocol.'],
   ['Active Record',
    'Eloquent models',
    'Domain objects carry their own persistence, which suits a schema of '
    'this size (Fowler 2003).'],
   ['Repository-by-convention',
    'Metadata-derived corpus paths',
    'Board, class, subject and type are structural rather than declared, '
    'removing a class of tagging error.'],
   ['Dependency injection',
    'Constructor promotion of `AIService` into controllers',
    'The service can be substituted with a fake in tests without touching '
    'the controller.'],
   ['Strategy',
    'One prompt template file per agent',
    'Behaviour is changed by editing a text file, with no code change and no '
    'redeployment of application logic.'],
   ['Adapter',
    '`resources/js/lib/api.ts`',
    'CSRF acquisition, header assembly and content-type selection are '
    'handled once rather than at every call site.'],
   ['Cache-aside',
    'LRU cache in front of the embedding call',
    'Repeated queries avoid a metered network call.'],
   ['Memento',
    '`chat_sessions.existing_summary`',
    'Conversation state is captured, persisted and restored without '
    'retaining the full transcript in the prompt.'],
   ['Template method',
    'The four-stage ingestion pipeline',
    'Each stage has the same skip-if-done, process, log structure, so a new '
    'document type slots into the existing shape.']],
  [1.25, 1.85, 2.85],
  9),
 ('h2', '4.13  Deployment Architecture'),
 ('p',
  'Figure 4.9 shows the deployment view. In development, and in the modest '
  'production configuration the project targets, the Laravel application and '
  'the FastAPI service run on the same host, the AI service bound to port '
  '8001 and reachable only from localhost. MySQL may be co-located or on a '
  'separate host. The browser holds only the compiled front-end bundle. All '
  'four third-party services are reached over TLS. The AI service is '
  'stateless. If concurrent load ever requires it, the natural first scaling '
  'step is to run several instances behind a local load balancer, with no '
  'change to the application layer.'),
 ('fig',
  'fig_deployment.png',
  'Deployment diagram showing devices, execution environments, deployed '
  'artefacts and the communication paths between them.',
  6.0),
 ('h2', '4.14  Summary'),
 ('p',
  'The system is a four-tier layered architecture with a service-oriented '
  'boundary between the application and artificial-intelligence tiers, '
  'adopted for ecosystem access, independent evolution, substitutability and '
  'failure isolation. Curricular scoping is enforced as a metadata '
  'pre-filter on the vector query rather than as a prompt instruction, which '
  'is what converts board alignment from a claim into a structural '
  'guarantee. A four-stage idempotent pipeline converts scanned board '
  'material into a filtered vector index. Four agents share one retriever '
  'and differ only in prompt and decoding parameters. Conversation cost is '
  'bounded by rolling summarisation, and embedding cost by a normalised '
  'cache. Security is applied across transport, identity, session, '
  'authorisation and secret-handling bands, with one known authorisation '
  'weakness recorded honestly. The next chapter descends from this '
  'architecture to the detailed design of each component.')]
