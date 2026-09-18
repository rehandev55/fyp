"""Content blocks for Chapter 7 - System Testing."""

BLOCKS = [('chapter', 'CHAPTER 7', 'SYSTEM TESTING'),
 ('p',
  'This chapter describes how the system was verified. It states the testing '
  'strategy, reports the automated suite, presents the functional and '
  'non-functional test cases, describes the harness written to evaluate the '
  'retrieval and language-model layers directly, records the integration and '
  'system testing, and lists every defect found.'),
 ('h2', '7.1  Introduction'),
 ('p',
  'This chapter reports how the system was verified. Section 7.2 states the '
  'strategy and the levels at which testing was applied. Section 7.3 reports '
  'the automated suite, including two failures that were left failing '
  'deliberately and what they revealed. Sections 7.4 to 7.6 present the '
  'functional and non-functional test-case catalogue. Section 7.7 gives the '
  'defect log with the current status of each entry, and Section 7.8 '
  'summarises coverage together with an honest statement of what was not '
  'tested.'),
 ('h2', '7.2  Testing Strategy'),
 ('p',
  'Testing was organised in four levels, illustrated in Figure 7.1. Breadth '
  'of coverage is greatest at the base and business risk addressed is '
  'greatest at the apex.'),
 ('fig',
  'fig_testing_levels.png',
  'The four levels of testing applied to the project and the coverage each '
  'provides.',
  5.7),
 ('bullets',
  [['Automated feature tests. ',
    'A Pest suite exercising authentication, profile, security and dashboard '
    'routes through the full HTTP stack against a migrated test database. '
    'These run in seconds and were executed on every significant change.'],
   ['Integration testing. ',
    'Verification of the contract between the Laravel application and the '
    'FastAPI service, and of the AI service against its own external '
    'dependencies, performed with the standalone scripts in '
    'ai-service/scripts and with Postman collections.'],
   ['System testing. ',
    'End-to-end execution of five complete user journeys with all four '
    'runtimes and both external services live.'],
   ['Acceptance testing. ',
    'Student volunteers performing the same journeys unaided, with '
    'observation rather than instruction.']]),
 ('p',
  'The distribution of effort was deliberate. Authentication and account '
  'management are the areas where a defect is both most likely to be '
  'exploited and most amenable to automation, so they carry the automated '
  'suite. The artificial-intelligence behaviours are non-deterministic and '
  'therefore resist assertion-based testing; they were verified by '
  'structured manual scenarios with recorded outcomes, which is acknowledged '
  'as a limitation in Section 7.8.'),
 ('h2', '7.3  Automated Test Suite'),
 ('p',
  'The automated suite is written with Pest 4 on PHPUnit 12 and runs against '
  'an isolated test database that is migrated and rolled back for every '
  'test. The whole suite executes in about two and a half seconds, which is '
  'short enough that it was run before every commit rather than only before '
  'a release. Table 7.1 gives its composition. The suite contains forty-five '
  'tests making one hundred and forty-seven assertions, and all of them '
  'pass.'),
 ('table',
  'Automated test suite composition and result',
  ['Test file', 'Area covered', 'Tests', 'Result'],
  [['Auth/AuthenticationTest',
    'Login screen, credential check, two-factor redirect, logout, rate '
    'limiting',
    '6',
    'Pass'],
   ['Auth/EmailVerificationTest',
    'Verification screen, signed-link fulfilment, invalid hash and '
    'identifier, repeat visits',
    '6',
    'Pass'],
   ['Auth/PasswordResetTest',
    'Reset request, reset screen, valid and invalid token',
    '5',
    'Pass'],
   ['Auth/PasswordConfirmationTest',
    'Confirmation screen and its authentication guard',
    '2',
    'Pass'],
   ['Auth/RegistrationTest',
    'Registration screen and account creation',
    '2',
    'Pass'],
   ['Auth/TwoFactorChallengeTest',
    'Challenge screen and its guest redirect',
    '2',
    'Pass'],
   ['Auth/VerificationNotificationTest',
    'Notification sent, and suppressed once verified',
    '2',
    'Pass'],
   ['ContentDownloadTest',
    'Filename handling, missing-file 404, download counting, stored file '
    'size',
    '5',
    'Pass'],
   ['Settings/SecurityTest',
    'Security page, password confirmation states, password update',
    '6',
    'Pass'],
   ['Settings/ProfileUpdateTest',
    'Profile display and update, e-mail verification state, account deletion',
    '5',
    'Pass'],
   ['DashboardTest', 'Guest redirect and authenticated access', '2', 'Pass'],
   ['ExampleTest, Unit/ExampleTest',
    'Application boot and unit harness',
    '2',
    'Pass']],
  [1.75, 2.35, 0.55, 0.75],
  9),
 ('h3', '7.3.1  A defect found and closed by the suite'),
 ('p',
  'Two tests in Auth/EmailVerificationTest failed for most of the project. '
  'Both asserted that a student who follows the verification link is sent to '
  'the dashboard at dashboard?verified=1, which is the destination used by '
  'the Fortify starter configuration. The delivered application does not do '
  'that. A custom signed route was introduced in Sprint 7. It fulfils the '
  'verification and then redirects to the login screen. A verification link '
  'is often opened in a different browser from the one the student '
  'registered in, and in that browser there is no session to carry through '
  'to the dashboard.'),
 ('p',
  'The failure was therefore not a defect in the application but a defect in '
  'the tests, which had not been updated when the route changed. The '
  'assertions were corrected to expect the login screen, with a comment '
  'recording why that destination is deliberate. The remaining assertions in '
  'both tests, that the Verified event fires exactly once and that the '
  'stored verification timestamp is set, were already correct and continue '
  'to guard the behaviour that actually matters. This episode is the '
  'clearest example in the project of a test suite earning its keep: the '
  'mismatch between the intended flow and the recorded expectation would '
  'otherwise have gone unnoticed.'),
 ('code',
  'The corrected assertion',
  "test('email can be verified', function () {\n"
  '    $user = User::factory()->unverified()->create();\n'
  '    Event::fake();\n'
  '\n'
  '    $verificationUrl = URL::temporarySignedRoute(\n'
  "        'verification.verify',\n"
  '        now()->addMinutes(60),\n'
  "        ['id' => $user->id, 'hash' => sha1($user->email)],\n"
  '    );\n'
  '\n'
  '    $response = $this->actingAs($user)->get($verificationUrl);\n'
  '\n'
  '    Event::assertDispatched(Verified::class);\n'
  '    expect($user->fresh()->hasVerifiedEmail())->toBeTrue();\n'
  '\n'
  "    // The application replaces Fortify's default destination: after a\n"
  '    // link is fulfilled the user is sent to the login screen, because\n'
  '    // the link is commonly opened in a different browser from the one\n'
  '    // they registered in.\n'
  "    $response->assertRedirect('/login');\n"
  '});',
  'tests/Feature/Auth/EmailVerificationTest.php'),
 ('shot',
  'pest_output',
  'Output of the automated Pest suite: 45 tests, 147 assertions, all passing '
  'in 2.37 seconds.',
  'Run "php artisan test --compact" in the project root and capture the '
  'summary line showing 45 passed and the duration.'),
 ('h2', '7.4  Functional Test Cases'),
 ('p',
  'The catalogue below records the manual and semi-automated functional test '
  'cases. Each states the objective, the input or action, the expected '
  'result and the observed outcome. Cases marked automated are covered by '
  'the suite of Section 7.3.'),
 ('h3', '7.4.1  Authentication and account management'),
 ('table',
  'Test cases — authentication and account management',
  ['ID', 'Objective', 'Input / action', 'Expected result', 'Result'],
  [['TC-01',
    'Registration with valid data',
    'Name, unused email, matching passwords',
    'Account created; verification email dispatched',
    'Pass (automated)'],
   ['TC-02',
    'Registration with a duplicate email',
    'An email already registered',
    'Field-level validation error; no account created',
    'Pass'],
   ['TC-03',
    'Registration with mismatched passwords',
    'Password and confirmation differ',
    'Validation error on the confirmation field',
    'Pass'],
   ['TC-04',
    'Login with valid credentials',
    'Correct email and password',
    'Session established; dashboard displayed',
    'Pass (automated)'],
   ['TC-05',
    'Login with an incorrect password',
    'Wrong password',
    'Authentication fails; generic error shown',
    'Pass (automated)'],
   ['TC-06',
    'Login rate limiting',
    'Six consecutive failed attempts',
    'Further attempts throttled',
    'Pass (automated)'],
   ['TC-07',
    'Email verification by signed link',
    'Click the emailed link',
    'Address marked verified; Verified event dispatched',
    'Pass'],
   ['TC-08',
    'Rejection of a tampered verification hash',
    'Altered hash in the link',
    'Verification refused; address remains unverified',
    'Pass (automated)'],
   ['TC-09',
    'Access to learning routes when unverified',
    'Unverified account requests /dashboard',
    'Redirected to the verification prompt',
    'Pass'],
   ['TC-10',
    'Password reset with a valid token',
    'Emailed token and a new password',
    'Password updated; login succeeds with the new password',
    'Pass (automated)'],
   ['TC-11',
    'Password reset with an invalid token',
    'Corrupted token',
    'Reset refused',
    'Pass (automated)'],
   ['TC-12',
    'Two-factor challenge',
    'Account with TOTP enabled',
    'Challenge screen shown before the session is established',
    'Pass (automated)'],
   ['TC-12a',
    'Two-factor recovery code',
    'A single recovery code',
    'Access granted; the code cannot be reused',
    'Pass'],
   ['TC-12b',
    'Google sign-in, new account',
    'Google account with an unregistered email',
    'Account created, email pre-verified, dashboard displayed',
    'Pass'],
   ['TC-12c',
    'Google sign-in, existing account',
    'Google account whose email is already registered',
    'Existing profile signed in; no duplicate created',
    'Pass'],
   ['TC-12d',
    'Account deletion',
    'Correct password confirmation',
    'Account and all dependent rows removed',
    'Pass (automated)']],
  [0.6, 1.35, 1.35, 1.6, 1.05],
  8.5),
 ('h3', '7.4.2  Academic selection and scoping'),
 ('table',
  'Test cases — academic selection and curricular scoping',
  ['ID', 'Objective', 'Input / action', 'Expected result', 'Result'],
  [['TC-13',
    'Board selection',
    'Select Federal, then AJK',
    'Selection persisted to the profile',
    'Pass'],
   ['TC-14',
    'Dependent subject list',
    'Select Class 9, then Class 12',
    'Subject options update to the selected class',
    'Pass'],
   ['TC-15',
    'Chapter list correctness',
    'Class 11 Chemistry',
    'All 22 chapters of that combination listed',
    'Pass'],
   ['TC-16',
    'Scoping of retrieval',
    'Ask a Class 12 question while scoped to Class 9',
    'Answer drawn from Class 9 material or declared as general knowledge',
    'Pass'],
   ['TC-17',
    'Session scope immutability',
    'Change the profile, then resume an older chat session',
    'The session retains its original board, class and subject',
    'Pass']],
  [0.6, 1.35, 1.35, 1.6, 1.05],
  8.5),
 ('h3', '7.4.3  Conversational tutoring'),
 ('table',
  'Test cases — AI tutoring',
  ['ID', 'Objective', 'Input / action', 'Expected result', 'Result'],
  [['TC-18',
    'Definition question',
    '“What is DNA?” in Class 11 Biology',
    'Structured definition with key points and an example',
    'Pass'],
   ['TC-19',
    'Session creation',
    'First message of a new conversation',
    'Session created and titled from the first 40 characters',
    'Pass'],
   ['TC-20',
    'Transcript persistence',
    'Send messages, reload the page',
    'Full transcript restored in order',
    'Pass'],
   ['TC-21',
    'Follow-up with pronoun reference',
    '“explain more” after a substantive answer',
    'Answer remains on the previous topic',
    'Pass'],
   ['TC-22',
    'Summary maintenance',
    'Conversation exceeding four turns',
    'existing_summary populated and updated on the session row',
    'Pass'],
   ['TC-23',
    'Out-of-corpus topic',
    'A topic with no indexed chunk above the floor',
    'Answer given with the general-knowledge disclosure sentence',
    'Pass after prompt revision (D-03)'],
   ['TC-24',
    'Urdu question',
    'A question typed in Urdu',
    'Answer returned in Urdu in simple language',
    'Pass'],
   ['TC-25',
    'Session deletion',
    'Delete a session',
    'Session and all its messages removed',
    'Pass'],
   ['TC-26',
    'AI service unavailable',
    'Stop the FastAPI process and send a message',
    "Explanatory error shown; the student's message is retained",
    'Pass']],
  [0.6, 1.35, 1.35, 1.6, 1.05],
  8.5),
 ('h3', '7.4.4  Practice and assessment'),
 ('table',
  'Test cases — practice, marking and session evaluation',
  ['ID', 'Objective', 'Input / action', 'Expected result', 'Result'],
  [['TC-27',
    'MCQ generation',
    'Class 11 Biology, whole book, five MCQs',
    'Five well-formed items with four options and a correct answer each',
    'Pass'],
   ['TC-28',
    'Chapter-scoped generation',
    'Two chapters selected',
    'Generated items confined to the selected chapters',
    'Pass'],
   ['TC-29',
    'Provenance labelling',
    'Any generated set',
    'Every item carries a past-paper, similar or new label',
    'Pass'],
   ['TC-30',
    'Short-question marking',
    'A partially correct three-mark answer',
    'Score between 1 and 2 with feedback naming what was missing',
    'Pass'],
   ['TC-31',
    'Long-question marking',
    'A complete eight-mark answer',
    'Score in the 6–8 band with confirming feedback',
    'Pass'],
   ['TC-32',
    'Blank answer',
    'Submit an empty answer',
    'Score of 0 with explanatory feedback; no exception',
    'Pass'],
   ['TC-33',
    'Score clamping',
    'Force an out-of-range model score',
    'Score clamped to the maximum for the question type',
    'Pass'],
   ['TC-34',
    'Malformed evaluator response',
    'Response without a SCORE line',
    'Score 0, raw text as feedback, no exception',
    'Pass'],
   ['TC-35',
    'Session aggregation',
    'Complete a five-question session',
    'Total, percentage and grade computed in application code and persisted',
    'Pass'],
   ['TC-36',
    'Strong and weak areas',
    'A session with mixed performance',
    'Named topics returned in both lists',
    'Pass']],
  [0.6, 1.3, 1.35, 1.65, 1.05],
  8.5),
 ('h3', '7.4.5  Resources, analytics and administration'),
 ('table',
  'Test cases — resources, analytics and administration',
  ['ID', 'Objective', 'Input / action', 'Expected result', 'Result'],
  [['TC-37',
    'Resource filtering',
    'Filter by board, class and subject',
    'Only matching resources listed',
    'Pass'],
   ['TC-38',
    'Empty result state',
    'A combination with no resource',
    'Explanatory empty state, not a blank page',
    'Pass'],
   ['TC-39',
    'Download',
    'Request a resource',
    'File streamed with correct name and type',
    'Pass'],
   ['TC-40',
    'Download accounting',
    'Download twice',
    'Counter incremented by two',
    'Pass'],
   ['TC-41',
    'Activity logging on download',
    'Download a resource',
    'Activity row of type resource created',
    'Pass'],
   ['TC-42',
    'Missing stored file',
    'Delete the file from disk, then request it',
    'Error reported; counter not incremented',
    'Pass'],
   ['TC-43',
    'Dashboard with no history',
    'New account',
    'Zeroed tiles and a designed empty state, no division by zero',
    'Pass'],
   ['TC-44',
    'Dashboard with history',
    'Account with several attempts',
    'Questions practised, average score and weakest subject correct',
    'Pass'],
   ['TC-45',
    'Subject banding',
    'Attempts in three subjects',
    'Each banded correctly at the 85, 70 and 60 per cent thresholds',
    'Pass'],
   ['TC-46',
    'Activity feed bound',
    'Generate more than eight activities',
    'At most eight entries retained; the newest is never pruned',
    'Pass'],
   ['TC-47',
    'Upload validation',
    'Submit with a missing field',
    'Field-level errors; no record and no stored file',
    'Pass'],
   ['TC-48',
    'Upload size limit',
    'File larger than 100 MB',
    'Rejected by validation',
    'Pass'],
   ['TC-49',
    'Content edit',
    "Change a resource's metadata",
    'Record updated; the stored file is untouched',
    'Pass'],
   ['TC-50',
    'Content deletion',
    'Delete a resource',
    'Record and stored file both removed',
    'Pass'],
   ['TC-51',
    'User blocking',
    'Set an account status to Blocked',
    'Status persisted and reflected in the list',
    'Pass'],
   ['TC-52',
    'Administrative access by a student',
    'Student account requests /admin/users',
    'Access denied at the page layer',
    'Pass, but see D-04']],
  [0.6, 1.3, 1.35, 1.65, 1.05],
  8.5),
 ('h2', '7.5  Non-Functional Test Cases'),
 ('table',
  'Test cases — performance, security and compatibility',
  ['ID', 'Category', 'Objective', 'Expected result', 'Result'],
  [['TC-53',
    'Performance',
    'Non-AI page and API response time',
    '1–3 s under normal load',
    'Pass'],
   ['TC-54',
    'Performance',
    'AI tutoring response time',
    '2–5 s depending on complexity',
    'Pass; see Section 8.5'],
   ['TC-55', 'Performance', 'Download start latency', '1–4 s', 'Pass'],
   ['TC-56',
    'Performance',
    'Embedding cache effectiveness',
    'A repeated query issues no embedding call',
    'Pass'],
   ['TC-57',
    'Performance',
    'Prompt growth over a long session',
    'Prompt size approximately constant beyond four turns',
    'Pass'],
   ['TC-58',
    'Security',
    'Password storage',
    'Only a bcrypt hash present in the users table',
    'Pass'],
   ['TC-59',
    'Security',
    'CSRF protection',
    'A state-changing request without a token is rejected',
    'Pass'],
   ['TC-60',
    'Security',
    'Secret exposure',
    'No API key present in the repository or in client bundles',
    'Pass'],
   ['TC-61',
    'Security',
    'Cross-user data access',
    "A student cannot read another student's session by identifier",
    'Fail — see D-05'],
   ['TC-62',
    'Security',
    'Two-factor secret storage',
    'Secret and recovery codes stored encrypted',
    'Pass'],
   ['TC-63',
    'Security',
    'Transport encryption',
    'All outbound provider calls use TLS',
    'Pass'],
   ['TC-64',
    'Usability',
    'First-time task completion',
    'A new student reaches a marked answer without instruction',
    'Pass; see Section 8.7'],
   ['TC-65',
    'Usability',
    'Empty states',
    'Every list has a designed empty state',
    'Pass'],
   ['TC-66',
    'Compatibility',
    'Browser support',
    'Correct rendering in Chrome, Edge and Firefox',
    'Pass'],
   ['TC-67',
    'Compatibility',
    'Mobile viewport',
    'Usable at 360 px width; sidebar collapses',
    'Pass'],
   ['TC-68',
    'Reliability',
    'External service failure',
    'Explanatory message; no input lost',
    'Pass'],
   ['TC-69',
    'Reliability',
    'Interrupted ingestion',
    'Restart resumes without repeating metered work',
    'Pass'],
   ['TC-70',
    'Observability',
    'Cost logging',
    'Every model call produces a record with token counts and cost',
    'Pass']],
  [0.55, 0.95, 1.75, 1.75, 0.95],
  8.5),
 ('h2', '7.6  Evaluation of the Retrieval and Language-Model Components'),
 ('p',
  'The test cases in Sections 7.4 and 7.5 check that the application behaves '
  'correctly: the right page is served, the right record is written, the '
  'wrong user is refused. They cannot check whether the artificial '
  'intelligence is any good. A retrieval call that returns five irrelevant '
  'passages succeeds at the level of HTTP, and a tutor answer that is fluent '
  'and wrong is indistinguishable, to an assertion, from one that is fluent '
  'and right. The central claims of this project are claims about answer '
  'quality, so they need their own measurements.'),
 ('p',
  'A separate evaluation harness was therefore written. It lives in the '
  'ai-service/scripts directory and runs against the live Pinecone index and '
  'the live model endpoint. It writes machine-readable results into '
  'ai-service/evaluation_results, so any figure quoted in Chapter 8 can be '
  'traced back to the run that produced it. The harness is in three '
  'programs, described below. Results are reported in Sections 8.2 to 8.7.'),
 ('table',
  'The evaluation harness',
  ['Program', 'What it measures', 'Output'],
  [['eval_00_index_inventory.py',
    'Size and shape of the vector index: total vectors, and the distribution '
    'of chunks over board, class, subject and document type.',
    'index_inventory.json'],
   ['eval_01_retrieval.py',
    'Retrieval quality over thirty curriculum questions: hit rate, '
    'similarity scores, keyword recall, metadata filter precision, '
    'cross-board and cross-class isolation, latency and cache behaviour.',
    'retrieval_eval.json'],
   ['eval_02_llm.py',
    'Behaviour of the three agents: grounding against a no-retrieval '
    'control, marking accuracy against a gold set, structural validity of '
    'generated questions, and prompt growth across a long session.',
    'llm_eval.json']],
  [1.55, 3.05, 0.85],
  9),
 ('h3', '7.6.1  Test design for retrieval'),
 ('p',
  'Thirty questions were written to cover the six populated subjects across '
  'all four classes. Each question carries a set of terms that a correct '
  'retrieval should surface, which gives a mechanical check on topical '
  'relevance without a human reading every passage. For example, a query '
  'about Ohm’s law is expected to return text containing at least one of '
  'ohm, current, voltage or resistance.'),
 ('p',
  'Four properties are measured for every query. Hit rate records whether '
  'any passage came back at all. The top-1 and mean similarity scores record '
  'how close the best match was. Keyword recall records whether the expected '
  'terms actually appeared. Latency records the wall-clock time of the '
  'embedding call and the vector search together.'),
 ('p',
  'The most important measurement is filter precision. The design claims '
  'that curricular scoping is structural, not advisory. That claim is tested '
  'directly. For twelve of the queries, every returned passage is read back '
  'with its metadata and checked against the board, class and subject that '
  'were requested. Any passage whose metadata differs is counted as a '
  'violation. Three further probes ask for material that should not exist, '
  'such as a board with no indexed content, and expect zero passages. A '
  'final pair of probes asks the same question under two different class '
  'filters. The two result sets must have nothing in common. That shows the '
  'filter, rather than the question, is doing the scoping.'),
 ('h3', '7.6.2  Test design for the language-model agents'),
 ('p',
  'Four experiments were designed, each with a baseline so that a number can '
  'be interpreted rather than merely reported.'),
 ('bullets',
  [['Experiment A, grounding. ',
    'Twelve questions are answered twice by the same model with the same '
    'prompt: once through the full retrieval path, and once with retrieval '
    'disabled. Both answers are then graded by a stronger, independent model '
    'against the same retrieved passages, on groundedness, fitness for the '
    'class, and factual correctness, and for the number of claims not '
    'supported by those passages. Using the same reference text for both '
    'sides is what makes the comparison fair: the control is judged on '
    'whether it happens to agree with the board textbook, not on whether it '
    'sounds convincing.'],
   ['Experiment B, marking accuracy. ',
    'A gold set of fifteen student answers was written before the run, '
    'covering multiple-choice, short and long questions, and spanning fully '
    'correct, partly correct and plainly wrong responses. The expected mark '
    'for each was agreed against the board marking scheme in advance. The '
    'evaluator agent marks the set blind, and the result is compared on '
    'exact agreement, agreement within one mark, and mean absolute error.'],
   ['Experiment C, structural validity. ',
    'Six question sets are generated across three subjects and all three '
    'question formats. Each set is parsed mechanically and checked against '
    'the format the prompt demands: the requested number of questions, a '
    'provenance label on every question, four options and an answer key for '
    'multiple choice, and an answer section for short and long questions.'],
   ['Experiment D, prompt growth. ',
    'A ten-turn tutoring session is simulated twice, once with the memory '
    'manager active and once with the full history resent on every turn. '
    'Prompt size is recorded at each turn. This tests the claim that session '
    'cost is bounded rather than linear in the length of the '
    'conversation.']]),
 ('h3', '7.6.3  Threats to validity'),
 ('p',
  'The limits of this design are stated here so that the results in Chapter '
  '8 are read correctly. The query set and the gold set were written by the '
  'project team, which risks favouring the system. Both were fixed before '
  'any run and were not adjusted afterwards. Even so, they are not an '
  'independent benchmark. Using a language model as judge is now common '
  'practice, and a stronger model was chosen for the role, but a model judge '
  'is not a board examiner. The gold set has fifteen items and the grounding '
  'set twelve, which is enough to show a direction but not enough for a '
  'confidence interval worth quoting. Finally, the measurements are of a '
  'live hosted service, so latency figures include network conditions on the '
  'day and should be read as indicative.'),
 ('h2', '7.7  Integration and System Testing'),
 ('h3', '7.7.1  Service contract testing'),
 ('p',
  'The AI service was exercised on its own through the scripts in '
  'ai-service/scripts. These call the retriever, the teacher agent, the '
  'tester and evaluator, and the session evaluator directly with fixed '
  'inputs. They print the retrieved chunks with their similarity scores. '
  'This separation was valuable during development: when an answer was poor '
  'it was possible to determine immediately whether the cause was bad '
  'retrieval or bad generation, which are entirely different problems with '
  'entirely different fixes. The four HTTP endpoints were also exercised '
  'through Postman with boundary-value inputs. These included an empty '
  'question, a question of exactly the maximum length, a question one '
  'character over, zero and twenty-one requested items, and a results array '
  'of fifty-one entries. In every case the Pydantic constraints produced a '
  'structured validation error rather than a metered call.'),
 ('h3', '7.7.2  End-to-end journeys'),
 ('table',
  'System test journeys',
  ['Journey', 'Steps', 'Outcome'],
  [['J1 — New student, first tutoring session',
    'Register, verify by email, sign in, select board, class and subject, '
    'ask three questions including one follow-up, reload and confirm the '
    'transcript',
    'Completed; transcript and summary persisted correctly'],
   ['J2 — Full practice attempt',
    'Sign in, open practice, select two chapters, choose short questions, '
    'answer five, review the session result, confirm the dashboard updated',
    'Completed; session and five result rows written; dashboard reflected '
    'the attempt'],
   ['J3 — Resource discovery and download',
    'Filter the library by board, class and subject, download, confirm the '
    'counter and the activity feed',
    'Completed'],
   ['J4 — Administrator content cycle',
    'Sign in as administrator, upload a resource, edit its metadata, confirm '
    'it appears to a student, delete it, confirm removal of both record and '
    'file',
    'Completed'],
   ['J5 — Degraded operation',
    'Stop the AI service, attempt a tutoring message and a quiz generation, '
    'restart and retry',
    'Completed; explanatory errors shown, no input lost, normal operation '
    'resumed']],
  [1.45, 2.75, 1.75],
  9),
 ('h2', '7.8  Defect Log'),
 ('p',
  'Table 7.10 records every defect identified during verification, including '
  'those that remain open. Defects are recorded whether or not they were '
  'fixed, because a log that contains only fixed defects is not a log.'),
 ('table',
  'Defect log',
  ['ID', 'Description', 'Severity', 'Status and resolution'],
  [['D-01',
    '`is_correct` on quiz_results is derived with a fixed threshold of 5 '
    'marks, so a correct MCQ (1 mark) and a good short answer (3 marks) are '
    'both recorded as incorrect.',
    'Low',
    'Open. No displayed figure uses the column — every reported number '
    'derives from `score` — but the column is unreliable for future '
    'analytics. Fix: derive the threshold from question_type, `$score >= '
    '$maxMark * 0.5`.'],
   ['D-02',
    'Two inherited email-verification tests asserted a redirect to the '
    'dashboard, but the application sends a verified user to the login '
    'screen by design.',
    'Low',
    'Fixed. The assertions were updated to expect the login screen, with a '
    'comment recording why that destination is deliberate. The suite is now '
    'fully passing; see Section 7.3.1.'],
   ['D-03',
    'The tutor replied “This topic is not in your Class class_11 biology '
    'syllabus.” for a topic that is in the syllabus but absent from the '
    'index at that time. The raw enumeration token also leaked into '
    'user-facing text.',
    'High',
    'Fixed. The teacher prompt now distinguishes a retrieval gap from a '
    'curriculum gap and falls back to general knowledge with an explicit '
    'disclosure. See Section 6.5.1.'],
   ['D-04',
    'Administrative API routes are guarded by authentication but their role '
    'check is applied at the page layer rather than at the route layer.',
    'High',
    'Open. Fix: a dedicated role middleware applied to the `/api/users` and '
    '`/api/content` write route groups.'],
   ['D-05',
    '`ChatController::messages`, `history` and `delete` accept a session '
    'identifier without verifying that the session belongs to the '
    'authenticated user.',
    'High',
    "Open. Fix: scope each query with `->where('user_id', "
    '$request->user()->id)` or apply a policy. This is the most serious open '
    'defect in the system.'],
   ['D-06',
    'Language-model responses occasionally exceeded the permitted mark for '
    'the question type.',
    'Medium',
    'Fixed. The score is parsed from a designated line and clamped in code; '
    'a parse failure yields zero rather than an exception.'],
   ['D-07',
    "The Google sign-in path assigns the role `'user'` where the rest of the "
    "system uses `'student'`.",
    'Low',
    'Open. Not exploitable — the role is only compared for equality with '
    "`'admin'` — but inconsistent. Fix: assign `'student'`."],
   ['D-08',
    'The Google sign-in path sets a fixed placeholder password literal for '
    'federated accounts.',
    'Low',
    'Open. The value is bcrypt-hashed and the account has no password login '
    'path, but a random string would be safer. Fix: `Str::random(40)`.'],
   ['D-09',
    'Session prompts grew linearly with conversation length, so cost and '
    'latency rose with session productivity.',
    'High',
    'Fixed. Rolling summarisation with a four-turn verbatim window; see '
    'Section 4.9.'],
   ['D-10',
    'Ingestion converted an entire PDF to images before recognition, '
    'exhausting memory on long textbooks.',
    'Medium',
    'Fixed. Batched conversion of ten pages with immediate release, and 150 '
    'dpi rasterisation.'],
   ['D-11',
    'An interrupted ingestion run repeated metered OCR and embedding work on '
    'restart.',
    'Medium',
    'Fixed. Every stage made idempotent; embedded identifiers logged '
    'incrementally.'],
   ['D-12',
    'Records created before the enumerations were introduced stored display '
    'strings, so retrieval filters matched nothing.',
    'Medium',
    'Fixed. A reversible normalisation migration across users, chat_sessions '
    'and contents, plus backed enumerations to prevent recurrence.'],
   ['D-13',
    'Asynchronous fetch calls failed CSRF verification; setting Content-Type '
    'manually broke multipart uploads.',
    'Medium',
    'Fixed. A single wrapper obtains the cookie, attaches the token and '
    'omits Content-Type for FormData.'],
   ['D-14',
    'The activity table grew without bound; naive pruning could delete the '
    'row just written.',
    'Low',
    'Fixed. Retain the eight most recent and delete only rows older than '
    'three minutes.'],
   ['D-15',
    "The evaluator's 500-token output budget produced feedback longer than "
    'students read.',
    'Low',
    'Fixed. Reduced to 200 tokens, cutting output cost on the most '
    'frequently called endpoint.']],
  [0.5, 2.1, 0.7, 2.65],
  8.5),
 ('p',
  'Three defects — D-04, D-05 and D-01 — remain open at submission. D-05 is '
  'the most serious: an authenticated student who guesses or enumerates a '
  "session identifier can read or delete another student's tutoring "
  'transcript. It is a two-line fix per method, it cannot be exploited by an '
  'unauthenticated visitor, and no personal data beyond the transcript '
  'itself is exposed. It is still a real authorisation defect, and it is '
  'reported here rather than omitted. It heads the remediation list in '
  'Section 9.6.'),
 ('h2', '7.9  Test Summary and Coverage'),
 ('table',
  'Coverage summary by requirement area',
  ['Area', 'Requirements', 'Test cases', 'Automated', 'Coverage judgement'],
  [['Authentication and account',
    'REQ-1–7, 26–29',
    'TC-01 to TC-12d',
    '27 tests',
    'Strong'],
   ['Academic scoping', 'REQ-8–11, 30–31', 'TC-13 to TC-17', '—', 'Adequate'],
   ['Conversational tutoring',
    'REQ-12–15, 32–35',
    'TC-18 to TC-26',
    '—',
    'Adequate; non-deterministic outputs verified by scenario'],
   ['Practice and assessment',
    'REQ-16–20, 36–38',
    'TC-27 to TC-36',
    '—',
    'Adequate; defensive paths well covered'],
   ['Resources', 'REQ-21–25, 39', 'TC-37 to TC-42', '—', 'Adequate'],
   ['Analytics', 'REQ-40–41', 'TC-43 to TC-46', '—', 'Adequate'],
   ['Administration',
    'REQ-42',
    'TC-47 to TC-52',
    '—',
    'Weak — authorisation defect D-04 open'],
   ['Non-functional',
    'NFR-1–19',
    'TC-53 to TC-70',
    '—',
    'Adequate; load testing not performed']],
  [1.35, 1.1, 1.15, 0.85, 1.5],
  9),
 ('h3', '7.9.1  What was not tested'),
 ('p', 'Three gaps are stated explicitly rather than left to inference.'),
 ('numbers',
  ['Load testing. The non-functional requirement of 50 to 500 concurrent '
   'users was not verified under synthetic load. The system was exercised '
   'with a handful of simultaneous sessions only. The concurrency claim in '
   'Section 3.7.1 is therefore a design target rather than a measured '
   'result, and is reported as such in Section 8.5.',
   'Automated coverage of the artificial-intelligence path. No automated '
   'test exercises the chat, quiz or evaluation endpoints, because their '
   'outputs are non-deterministic. The correct approach — asserting on '
   'structural properties such as the presence of a SCORE line, the item '
   'count and the score range, against a stubbed model — was identified but '
   'not implemented within the available time.',
   'Security penetration testing. No systematic adversarial assessment was '
   'carried out. Defect D-05 was found by code review rather than by '
   'testing, which suggests that a structured review of every route that '
   'accepts an identifier would find more of the same class.']),
 ('h2', '7.10  Summary'),
 ('p',
  'Verification was applied at four levels. The automated suite of 45 tests '
  'and 147 assertions covers authentication, profile and security thoroughly '
  'and runs in under three seconds. All 45 pass. Two of them failed for most '
  'of the project because they asserted an old redirect target; those '
  'assertions were corrected rather than deleted, as Section 7.3.1 '
  'describes. Seventy-two functional and non-functional test cases were '
  'executed across scoping, tutoring, assessment, resources, analytics and '
  'administration, of which one — cross-user session access — failed and is '
  'logged as an open high-severity defect. Fifteen defects were recorded in '
  'total, ten fixed and five open, each with the specific correction stated. '
  'Three coverage gaps — load testing, automated AI-path testing and '
  'penetration testing — are declared rather than implied. The next chapter '
  'presents the results the verified system produces.')]
