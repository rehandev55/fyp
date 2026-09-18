"""Content blocks for Chapter 8 - Results and Evaluation."""

BLOCKS = [('chapter', 'CHAPTER 8', 'RESULTS AND EVALUATION'),
 ('p',
  'This chapter reports what the delivered system does. It presents the '
  'feature set, the measured behaviour of the artificial-intelligence '
  'subsystem, the responsiveness and cost of the platform, the results of '
  'acceptance testing with students, a comparison against existing products, '
  'and an assessment of each objective against the evidence gathered.'),
 ('h2', '8.1  Introduction'),
 ('p',
  'This chapter presents what the completed system does and how well it does '
  'it. Section 8.2 gives the delivered feature set. Section 8.3 presents the '
  'interface in operation. Section 8.4 evaluates retrieval and marking '
  'behaviour using records produced by the system itself. Section 8.5 '
  'reports responsiveness, Section 8.6 the cost analysis, and Section 8.7 '
  'the acceptance-testing outcome. Section 8.8 compares the result against '
  'existing platforms, Section 8.9 assesses each objective against evidence, '
  'and Section 8.10 discusses the limitations of both the system and this '
  'evaluation.'),
 ('h2', '8.2  Delivered System'),
 ('table',
  'Delivered feature set',
  ['Area', 'Delivered capability', 'State'],
  [['Accounts',
    'Email registration with verification, password authentication with rate '
    'limiting, password reset, password confirmation, optional TOTP '
    'two-factor with recovery codes, Google OAuth 2.0 sign-in with account '
    'linking, account deletion',
    'Complete'],
   ['Academic profile',
    'Two boards modelled (Federal corpus indexed), four classes, seven '
    'subjects, 379 mapped chapters; persisted to the profile and applied '
    'throughout',
    'Complete'],
   ['AI tutoring',
    'Multi-session conversational tutor grounded in board material, '
    'bilingual, with persistent transcripts and rolling conversation memory',
    'Complete'],
   ['Practice generation',
    'MCQ, short and long questions, whole-book or chapter-scoped, '
    'provenance-labelled',
    'Complete'],
   ['Automatic marking',
    'Per-answer marking against the 1/3/8 board scheme with two-sentence '
    'feedback and defensive clamping',
    'Complete'],
   ['Session evaluation',
    'Total, percentage, grade band, strong and weak topics, encouragement '
    'and a study recommendation',
    'Complete'],
   ['Resource library',
    'Filtered listing and authenticated download with per-resource '
    'accounting',
    'Complete'],
   ['Analytics',
    'Dashboard tiles, subject-wise performance banding, focus '
    'recommendation, bounded activity feed',
    'Complete'],
   ['Administration',
    'Content upload, edit and delete; user listing, edit, block and delete',
    'Complete, one open authorisation defect (D-04)'],
   ['Corpus ingestion',
    'Four-stage idempotent OCR, cleaning, chunking and embedding pipeline',
    'Complete'],
   ['Cost instrumentation',
    'Per-call token and cost logging with academic-scope attribution',
    'Complete'],
   ['Voice interaction',
    'Speech input and spoken answers',
    'Not implemented — declared out of scope in Section 1.5.2']],
  [1.15, 3.55, 1.25],
  9.5),
 ('h2', '8.3  The System in Operation'),
 ('shot',
  'welcome',
  'The public landing page presenting the product proposition and the routes '
  'into the application.',
  'Capture http://localhost:8000/ at 1440 × 900, scrolled to the top.'),
 ('shot',
  'dashboard-full',
  'The student dashboard after several completed practice sessions, showing '
  'the progress tiles, quick actions and the recent-activity feed.',
  'Capture http://localhost:8000/dashboard for an account with a populated '
  'history.'),
 ('shot',
  'aichat-session',
  'A multi-turn tutoring session, showing the session list, the transcript '
  'and a follow-up question answered in context.',
  'Capture http://localhost:8000/aichat with a conversation of at least six '
  'turns including one short follow-up.'),
 ('shot',
  'practice-flow',
  'The practice module in progress: a provenance-labelled question, the '
  "answer field and the evaluator's per-answer feedback.",
  'Capture the practice page mid-session with feedback displayed beneath a '
  'marked answer.'),
 ('shot',
  'result-summary',
  'The session result produced by the session evaluator: score, percentage, '
  'grade band, strong and weak areas and the study recommendation.',
  'Capture the end-of-session summary after completing a five-question '
  'test.'),
 ('shot',
  'progress-chart',
  'The progress page with subject-wise performance and the focus-area '
  'recommendation.',
  'Capture http://localhost:8000/progress for an account with attempts '
  'across at least three subjects.'),
 ('shot',
  'resources-filtered',
  'The resource library with board, class and subject filters applied.',
  'Capture http://localhost:8000/resources with a filter narrowing the '
  'list.'),
 ('shot',
  'admin-console',
  'The administrative console for content management.',
  'Capture http://localhost:8000/admin/content signed in as an '
  'administrator.'),
 ('shot',
  'mobile',
  'The interface at a 390-pixel mobile viewport, showing the collapsed '
  'navigation and the full-width chat surface.',
  'Capture /aichat and /dashboard in a browser device-emulation mode at 390 '
  '× 844 and place the two side by side.'),
 ('h2', '8.4  Evaluation of the Artificial-Intelligence Subsystem'),
 ('p',
  'This section reports what the artificial-intelligence subsystem actually '
  'does, measured rather than demonstrated. It draws on two kinds of '
  'evidence. The first is the controlled evaluation harness described in '
  'Section 7.6, which was run against the live index and the live model '
  'endpoint and whose raw output is stored in ai-service/evaluation_results. '
  'The second is the body of records the system itself produced and stored '
  'during development and integration testing. Both are presented in full, '
  'including the cases where the system performed poorly, because selecting '
  'only favourable examples would make the evaluation worthless.'),
 ('h3', '8.4.1  The indexed corpus'),
 ('p',
  'Every claim about retrieval depends on what is actually in the index, so '
  'the index was inventoried first. It holds 8,057 vectors of 1,536 '
  'dimensions each. These are distributed over 27 populated combinations of '
  'board, class and subject. Table 8.2 gives the breakdown by document '
  'type.'),
 ('table',
  'Composition of the indexed corpus',
  ['Document type', 'Chunks', 'Share'],
  [['Textbook', '4,655', '57.8 %'],
   ['Keybook', '3,036', '37.7 %'],
   ['Past papers', '366', '4.5 %'],
   ['Total', '8,057', '100 %']],
  [1.9, 1.6, 1.5],
  10),
 ('p',
  'The distribution across classes reflects the size of the syllabus rather '
  'than any decision by the team: Class 12 contributes 3,461 chunks, Class '
  '11 contributes 2,395, Class 10 contributes 1,356 and Class 9 contributes '
  '845. By subject, Biology is largest at 1,631 chunks and Mathematics '
  'smallest at 760. That is expected. Mathematics textbooks carry a high '
  'proportion of worked symbols, which survive optical character recognition '
  'poorly and are removed during cleaning.'),
 ('fig', 'fig_eval_corpus_class.png', 'Indexed chunks by class.', 5.2),
 ('fig', 'fig_eval_corpus_subject.png', 'Indexed chunks by subject.', 5.4),
 ('note',
  'The inventory also established a limitation that must be stated plainly. '
  'All 8,057 chunks belong to the Federal Board. The AJK Board is present in '
  'the data model, in the interface and in the retrieval filter, but no AJK '
  'material has been ingested, so a student who selects that board receives '
  'no retrieved context. Class 9 Biology is likewise unpopulated, which is '
  'why 27 rather than 28 combinations carry content. Neither gap requires a '
  'code change to close; both require an ingestion run. This is carried into '
  'Section 8.10 and Section 9.5.',
  'What the index does not contain'),
 ('h3', '8.4.2  Retrieval quality'),
 ('p',
  'Thirty curriculum questions were put through the production retrieval '
  'path, five passages requested for each. Every question returned five '
  'passages, giving a hit rate of 1.00, and every question surfaced at least '
  'one of its expected terms, giving a keyword recall at five of 1.00. The '
  'mean similarity of the best match was 0.505, with the weakest query at '
  '0.312 and the strongest at 0.632. The mean similarity across all five '
  'returned passages was 0.449.'),
 ('table',
  'Retrieval results over thirty curriculum questions',
  ['Measure', 'Value'],
  [['Queries', '30'],
   ['Hit rate (at least one passage returned)', '1.00'],
   ['Keyword recall at five', '1.00'],
   ['Mean top-1 similarity', '0.505'],
   ['Mean similarity across five passages', '0.449'],
   ['Lowest top-1 similarity', '0.312 (Class 11 Mathematics, "sets")'],
   ['Highest top-1 similarity', '0.632 (Class 12 Chemistry, "oxidation")'],
   ['Mean latency, embedding and search', '774 ms'],
   ['Median latency', '551 ms'],
   ['95th percentile latency', '717 ms']],
  [3.3, 2.1],
  10),
 ('p',
  'Scores vary by subject in a way that matches the character of the '
  'material. Biology leads at a mean top-1 of 0.550, followed by Physics at '
  '0.536, Chemistry at 0.510 and English at 0.504. Mathematics at 0.443 and '
  'Computer Science at 0.439 trail the rest. Mathematics suffers because its '
  'meaning lives in notation that the text pipeline cannot preserve, and '
  'Computer Science because its vocabulary is generic enough that many '
  'chapters look alike to an embedding model. Neither fell below the 0.2 '
  'relevance floor, so in no case did the system fall back to an empty '
  'context.'),
 ('fig',
  'fig_eval_retrieval_scores.png',
  'Mean top-1 similarity by subject.',
  5.4),
 ('p',
  'The mean latency of 774 ms is inflated by a single cold-start query that '
  'took 5.7 seconds while the connection to the vector service was '
  'established. The median of 551 ms and the 95th percentile of 717 ms '
  'describe steady-state behaviour better, and both sit inside the '
  'two-second budget set by NFR-01. The embedding cache removes the '
  'embedding call entirely for a repeated query: a cold embedding took 328 '
  'ms, while five subsequent calls for the same string averaged three '
  'microseconds.'),
 ('h3', '8.4.3  Does the curricular filter actually hold?'),
 ('p',
  'The central design claim of this project is that curricular scoping is '
  'structural rather than advisory. The model is not asked to stay inside '
  'the syllabus; it is never shown anything outside it. That claim is '
  'testable, and it was tested in three ways.'),
 ('p',
  'First, for twelve queries every returned passage was read back with its '
  'metadata and compared against the board, class and subject that had been '
  'requested. All sixty passages matched on all three fields, giving a '
  'filter precision of 1.0000 with zero violations. Second, three probes '
  'requested material that should not exist: two asked for AJK Board content '
  'and one for Class 9 Biology. All three returned zero passages, so the '
  'system degrades to an empty context rather than silently substituting '
  'another cohort’s material. Third, the same question was asked under two '
  'different class filters. "Explain the structure of an atom" returned five '
  'Class 9 Chemistry passages and five Class 12 Chemistry passages with no '
  'passage in common, and "What is motion?" behaved the same way across '
  'Class 9 and Class 11 Physics.'),
 ('table',
  'Curricular isolation probes',
  ['Probe', 'Filter applied', 'Passages returned', 'Expected'],
  [['Cross-board, biology', 'ajk / class_11 / biology', '0', '0'],
   ['Cross-board, physics', 'ajk / class_9 / physics', '0', '0'],
   ['Unpopulated cohort', 'federal / class_9 / biology', '0', '0'],
   ['Same question, two classes (chemistry)',
    'class_9 against class_12',
    '5 and 5, none shared',
    'disjoint'],
   ['Same question, two classes (physics)',
    'class_9 against class_11',
    '5 and 5, none shared',
    'disjoint']],
  [1.65, 1.6, 1.4, 0.75],
  9),
 ('p',
  'Taken together these results support the claim. A student is answered '
  'from their own board, class and subject, or they are not answered from '
  'retrieved material at all. There is no measured path by which one '
  'cohort’s textbook can reach another cohort’s student.'),
 ('h3', '8.4.4  Grounding: answers with and without retrieval'),
 ('p',
  'Filtering the right passages into the prompt is only useful if it changes '
  'what the model writes. To test that, twelve questions were answered twice '
  'by the same model with the same prompt, once through the full retrieval '
  'path and once with retrieval disabled. Both answers were then graded by a '
  'stronger, independent model against the same retrieved passages. It '
  'scored each on a one-to-five scale for groundedness, fitness for the '
  'class and factual correctness. It also counted the claims the passages do '
  'not support.'),
 ('table',
  'Judged answer quality, retrieval enabled against disabled',
  ['Measure', 'With retrieval', 'Retrieval disabled', 'Change'],
  [['Groundedness (1–5)', '2.75', '1.92', '+0.83'],
   ['Fitness for the class (1–5)', '4.75', '4.58', '+0.17'],
   ['Factual correctness (1–5)', '4.83', '4.58', '+0.25'],
   ['Unsupported claims per answer', '2.08', '2.33', '−0.25'],
   ['Mean prompt size (tokens)', '1,741', '474', '+1,267'],
   ['Mean answer latency', '3.36 s', '2.38 s', '+0.98 s']],
  [2.0, 1.25, 1.35, 0.85],
  10),
 ('fig',
  'fig_eval_grounding.png',
  'Judged answer quality with and without retrieval.',
  5.4),
 ('p',
  'Groundedness rises by 0.83 points, a relative improvement of 43 per cent, '
  'and unsupported claims fall by 11 per cent. Correctness and fitness for '
  'the class both improve slightly. Looking at the twelve questions '
  'individually is more informative than the means: retrieval produced a '
  'better groundedness score on four questions, an equal score on the other '
  'eight, and a worse score on none. Retrieval never harmed an answer in '
  'this experiment. Where it helped, it helped substantially — the Class 10 '
  'Physics question on Ohm’s law moved from 1 to 5.'),
 ('p',
  'The absolute groundedness figure of 2.75 out of 5 deserves an honest '
  'explanation rather than a favourable gloss. It is held down by a '
  'deliberate decision in the teacher prompt, which permits the agent to '
  'fall back on general knowledge when the retrieved passages do not cover '
  'the topic, provided it says so. That rule exists because students ask '
  'broad questions such as "what is chemistry" that no single textbook '
  'passage answers, and refusing them would make the tutor useless. The '
  'judge, however, is instructed to score strictly against the supplied '
  'passages, so every sentence of a legitimate general-knowledge fallback is '
  'counted against groundedness. The measurement is therefore a lower bound '
  'on grounding rather than an estimate of it. Section 9.6 proposes a '
  'stricter mode in which the fallback is disabled and the two policies are '
  'compared directly.'),
 ('fig',
  'fig_eval_hallucination.png',
  'Mean unsupported claims per answer.',
  5.0),
 ('p',
  'The cost of grounding is also visible in the table. Retrieval raises the '
  'prompt from 474 to 1,741 tokens and adds about one second to the '
  'response. At the rate in Section 8.6 that is roughly two hundredths of a '
  'cent per exchange, which is the price paid for an answer the system can '
  'point at.'),
 ('h3', '8.4.5  Marking accuracy against a gold set'),
 ('p',
  'Fifteen student answers were written before the run and their correct '
  'marks agreed against the board marking scheme. The set spans all three '
  'question formats and deliberately includes fully correct answers, partly '
  'correct answers and answers that are confidently wrong. The evaluator '
  'agent marked the set without seeing the expected values.'),
 ('table',
  'Marking accuracy of the evaluator agent',
  ['Measure', 'All', 'MCQ (1)', 'Short (3)', 'Long (8)'],
  [['Items', '15', '2', '8', '5'],
   ['Exact agreement', '73.3 %', '100 %', '75.0 %', '60.0 %'],
   ['Within one mark', '100 %', '100 %', '100 %', '100 %'],
   ['Mean absolute error (marks)', '0.27', '0.00', '0.25', '0.40'],
   ['Mean error as share of maximum', '6.1 %', '0 %', '8.3 %', '5.0 %'],
   ['Mean latency', '1.38 s', '—', '—', '—']],
  [2.05, 0.9, 0.85, 0.95, 0.85],
  9),
 ('fig',
  'fig_eval_marking.png',
  'Expected mark against awarded mark across the gold set.',
  5.8),
 ('p',
  'The agent agreed exactly with the expected mark on eleven of fifteen '
  'answers and was never more than one mark away on any of them. The mean '
  'absolute error of 0.27 marks is 6.1 per cent of the available marks. All '
  'four disagreements were small and explicable. Two were generous. A bare '
  'statement of "Force equals mass times acceleration" earned three marks '
  'where two were expected. An answer claiming oxidation is the gain of '
  'electrons earned one mark where zero was expected. Two were harsh: a thin '
  'but not worthless answer on Ohm’s law earned two marks where three were '
  'expected, and a nearly empty answer on work, energy and power earned zero '
  'where one was expected.'),
 ('p',
  'The pattern matters more than the totals. Exact agreement is perfect on '
  'one-mark items, where the judgement is binary, and falls as the mark '
  'scale widens, which is exactly where human markers also disagree with one '
  'another. Critically, the errors are not systematic in one direction, and '
  'no answer was mis-ranked: every fully correct answer scored full marks, '
  'every wholly wrong answer scored zero, and every partial answer landed '
  'between the two. For a formative tool whose purpose is to tell a student '
  'roughly where they stand and precisely what they missed, an error of a '
  'quarter of a mark is comfortably inside tolerance. It would not be '
  'acceptable for a summative examination, and the system does not claim '
  'that role.'),
 ('h3', '8.4.6  Validity of generated question sets'),
 ('p',
  'Six question sets were generated across three subjects and all three '
  'formats, and each was parsed mechanically against the structure the '
  'tester prompt demands. Twenty-one checks were applied in total. They '
  'covered the requested question count and a provenance label on every '
  'question. For multiple choice they also covered four options and an '
  'answer key, and for short and long items an answer section.'),
 ('table',
  'Structural validity of generated question sets',
  ['Topic', 'Class and subject', 'Type', 'Asked', 'Made', 'Checks'],
  [['Cell theory', 'Class 11 Biology', 'MCQ', '5', '5', '4 / 4'],
   ['Chemical bonding', 'Class 10 Chemistry', 'MCQ', '5', '5', '4 / 4'],
   ['Laws of motion', 'Class 9 Physics', 'MCQ', '5', '5', '4 / 4'],
   ['Matrices', 'Class 10 Mathematics', 'Short', '3', '3', '3 / 3'],
   ['Operating systems', 'Class 11 Computer', 'Short', '3', '3', '3 / 3'],
   ['Electromagnetic induction',
    'Class 12 Physics',
    'Long',
    '2',
    '2',
    '3 / 3']],
  [1.5, 1.5, 0.7, 0.55, 0.55, 0.65],
  9),
 ('p',
  'All twenty-one checks passed and all six sets were fully valid. Every set '
  'contained exactly the number of questions requested, every question '
  'carried a provenance label, every multiple-choice item had four options '
  'and a marked answer, and generation averaged 4.55 seconds per set. This '
  'matters for the application rather than only for the model: the parser in '
  'the Laravel layer depends on that structure, and a malformed set reaches '
  'the student as a broken practice screen. A 100 per cent structural pass '
  'rate over six sets is a small sample, but it is consistent with the '
  'absence of parse failures in the thirty-three practice sessions recorded '
  'during integration testing.'),
 ('h3', '8.4.7  Conversation memory and bounded cost'),
 ('p',
  'A tutoring session that resends its whole history grows linearly in cost, '
  'and the marginal cost of the tenth question becomes several times that of '
  'the first. The memory manager is the mechanism that prevents this. To '
  'measure it, a ten-turn session was simulated twice, once with the manager '
  'active and once with the full history resent each turn.'),
 ('fig',
  'fig_eval_memory.png',
  'Prompt size across a ten-turn tutoring session.',
  5.6),
 ('p',
  'The two curves are identical for the first three turns, because the '
  'manager keeps the four most recent turns verbatim and has nothing yet to '
  'compress. From the fourth turn they separate. The unmanaged prompt climbs '
  'steadily from 845 to 1,493 tokens, rising by roughly 110 tokens per turn '
  'with no ceiling. The managed prompt rises to about 960 tokens by the '
  'seventh turn and then flattens, ending at 937. By the tenth turn the '
  'managed session sends 556 fewer tokens, a reduction of 37 per cent, and '
  'the gap widens with every further turn because one curve is flat and the '
  'other is not.'),
 ('p',
  'The flattening is the result that matters. It means the cost of the '
  'twentieth question in a session is about the cost of the fifth. A student '
  'who works through a difficult topic at length does not become steadily '
  'more expensive to serve. That property is what makes the per-interaction '
  'cost quoted in Section 8.6 a meaningful figure rather than an average '
  'over sessions that happened to be short.'),
 ('h3', '8.4.8  Volume of system-generated data'),
 ('p',
  'The evaluation in this section uses records the system itself produced '
  'and stored during development and integration testing. They are presented '
  'verbatim, including the cases where the system performed poorly, because '
  'selecting only favourable examples would make the evaluation worthless.'),
 ('table',
  'Records produced by the system during development and integration testing',
  ['Record type', 'Count', 'Observation'],
  [['Tutoring sessions',
    '17',
    'Across Biology, Computer Science, Physics and Mathematics'],
   ['Tutoring messages',
    '148',
    'Mean student message 17 characters; mean tutor answer 192 characters'],
   ['Sessions carrying a rolling summary',
    '12',
    'Mean summary length 611 characters — four to six sentences, exactly the '
    'design target'],
   ['Practice sessions',
    '33',
    '16 short-question, 15 multiple-choice, 2 long-question'],
   ['Practice sessions with a computed grade',
    '28',
    'The remaining 5 were abandoned before completion during testing'],
   ['Individually marked answers',
    '55',
    '49 carry evaluator feedback; mean feedback length 166 characters'],
   ['Resource downloads', '64', 'Across 3 uploaded resources']],
  [2.3, 0.7, 2.95],
  9.5),
 ('p',
  'Two of these figures are direct evidence that design targets were met. '
  'The mean summary length of 611 characters corresponds to four to six '
  'sentences, which is precisely what the summariser prompt specifies and '
  'what the 200-token ceiling was chosen to produce. The mean feedback '
  'length of 166 characters is two to three sentences. That is what the '
  'evaluator prompt requires, and what cutting the output budget from 500 '
  'tokens to 200 was intended to enforce. Neither figure was targeted after '
  'the fact; both are the observed consequence of the prompt and budget '
  'decisions recorded in Sections 4.6 and 5.6.'),
 ('h3', '8.4.9  Marking behaviour in live sessions'),
 ('p',
  'Table 8.9 gives the distribution of scored practice sessions by question '
  'type.'),
 ('table',
  'Scored practice sessions by question type',
  ['Question type', 'Sessions', 'Scored', 'Mean %', 'Range %'],
  [['Multiple choice (1 mark)', '15', '11', '60.0', '0 – 100'],
   ['Short question (3 marks)', '16', '15', '22.1', '0 – 45'],
   ['Long question (8 marks)', '2', '2', '6.0', '0 – 12'],
   ['All types', '33', '28', '—', '0 – 100']],
  [1.85, 0.9, 0.8, 0.85, 1.05],
  9.5),
 ('note',
  'These percentages measure the marking mechanism, not student ability. The '
  'answers were supplied by the development team while exercising the '
  'system, and deliberately included blank submissions, one-word guesses and '
  'answers known to be wrong in order to test the scoring bands and the '
  'defensive paths. The mean of 22.1 per cent for short questions reflects a '
  'mean submitted answer length of 22 characters. No inference about real '
  'student attainment can or should be drawn from this table.',
  'Interpretation'),
 ('p',
  'What the distribution does show is that the marking mechanism '
  'discriminates. The range spans the full scale in the multiple-choice '
  'case, and sessions were graded across three of the four bands: 15 Poor, '
  '10 Needs Work and 3 Excellent. The mean rises with the coarseness of the '
  'marking scale, exactly as expected. A one-mark item is all or nothing, '
  'while a three-mark item can lose marks for being incomplete even when its '
  'central claim is right. No session recorded a percentage above 100 or '
  'below 0, which confirms that the clamping described in Section 5.7.4 held '
  'across every attempt.'),
 ('h3', '8.4.10  Marking quality in live sessions'),
 ('p',
  'Table 8.10 reproduces evaluator outputs verbatim from the quiz_results '
  'table, with an independent judgement of whether the mark and the feedback '
  'were correct.'),
 ('table',
  'Verbatim evaluator outputs with independent assessment',
  ['Question and student answer',
   'Mark',
   'Evaluator feedback (verbatim)',
   'Assessment'],
  [['“Which organelle is responsible for producing ATP in eukaryotic cells?” '
    '[⭐ Past Paper] — answered “Golgi apparatus”',
    '0 / 1',
    '“The student incorrectly identified the Golgi apparatus as the '
    'organelle responsible for ATP production. The correct answer is '
    'mitochondria, which are specifically known for ATP production in '
    'eukaryotic cells.”',
    'Correct. The mark is right and the feedback supplies the correct answer '
    'with a reason.'],
   ['“What is the primary function of enzymes in biological systems?” [~ '
    'Similar] — answered “To speed up chemical reactions”',
    '1 / 1',
    '“The answer correctly identifies the primary function of enzymes in '
    'biological systems. It is complete and accurate as per the textbook '
    'content.”',
    'Correct, and note the phrase “as per the textbook content” — the '
    'evaluator is marking against retrieved material, which is the intended '
    'behaviour.'],
   ['“What is the primary function of enzymes in biological reactions?” [~ '
    'Similar] — answered “To provide energy for the reaction”',
    '0 / 1',
    "“The student's answer is incorrect as it states that enzymes provide "
    'energy for the reaction. Enzymes actually lower the activation energy '
    'required to initiate a chemical reaction, rather than providing energy '
    'themselves.”',
    'Correct, and pedagogically strong: the specific misconception is named '
    'rather than merely marked wrong.'],
   ['“Explain the role of enzymes in biological reactions and how '
    'temperature and pH affect their activity.” [~ Similar] — a partial '
    'answer covering activation energy only',
    '1 / 3',
    '“The student correctly stated that enzymes lower the activation energy '
    'required for a reaction. However, the explanation lacks details about '
    'the role of enzymes in biological reactions and how factors like '
    'temperature and pH affect their activity.”',
    "Correct partial credit, and it is the behaviour VanLehn's meta-analysis "
    'identifies as the mechanism of effective tutoring: what was right and '
    'what was missing, separately.'],
   ['“Describe the structure and function of mitochondria in eukaryotic '
    'cells.” [⭐ Past Paper] — answered “sont know”',
    '0 / 3',
    '“The answer is completely incorrect as it does not provide any '
    'information about the structure or function of mitochondria. There is '
    'no mention of the double membrane, shape, or any functions of '
    'mitochondria.”',
    'Correct, and the feedback names the specific points the answer should '
    'have contained, which turns a zero into a revision instruction.']],
  [1.75, 0.55, 2.4, 1.25],
  8.5),
 ('p',
  'Across the five cases the mark is correct in every instance and the '
  'feedback names a specific content deficiency rather than issuing a '
  'generic verdict. The partial credit case is the most significant. The '
  'agent awards one mark of three for an answer that is correct as far as it '
  'goes, and states exactly what was left out. That is the step-level '
  'feedback the literature identifies as the active ingredient in effective '
  'tutoring (VanLehn 2011).'),
 ('h3', '8.4.11  Explanation quality'),
 ('p',
  'Table 8.11 reproduces tutor answers verbatim from the chat_messages '
  'table.'),
 ('table',
  'Verbatim tutor outputs',
  ['Question',
   'Tutor answer (verbatim, abridged where marked)',
   'Assessment'],
  [['“what is DNA” (Class 11 Biology)',
    '“DNA, or deoxyribonucleic acid, is the molecule that holds the genetic '
    'information for living things. It tells cells how to grow, develop, and '
    'function.  Key points: DNA looks like a twisted ladder (double helix). '
    'It is made of building blocks called nucleotides, which have three '
    'parts: a sugar, a phosphate group, and a base. There are four bases in '
    'DNA: adenine (A), thymine (T), cytosine (C), and guanine (G). The order '
    'of these bases is what makes each organism unique.  Example: DNA is '
    'found in the nucleus of cells and helps make proteins…”',
    'Follows the definition, key-points, example structure the teacher '
    'prompt specifies for a “what is” question; accurate, exam-length and '
    'pitched appropriately.'],
   ['“software mean” (Class 9 Computer)',
    '“Software refers to a set of instructions or programs that tell a '
    'computer how to perform specific tasks. It can be categorized into two '
    'main types: 1. System Software — the operating system and utility '
    'programs that manage computer resources at a low level, for example '
    'Windows or macOS. 2. Application Software — designed to help users '
    'perform specific tasks such as word processing, web browsing or '
    'gaming…”',
    'Correctly recognises an ungrammatical fragment as a definition request '
    'and answers with a classification, which is the structure a board '
    'answer requires.'],
   ['“cell theory” (Class 11 Biology, before the prompt revision)',
    '“This topic is not in your Class class_11 biology syllabus.”',
    'Incorrect on two counts: cell theory is in the syllabus, and the raw '
    'enumeration token leaked into user-facing text. This is defect D-03; '
    'the resolution is described in Section 6.5.1 and the behaviour after '
    'revision is the general-knowledge fallback shown in the row above.']],
  [1.35, 3.15, 1.45],
  8.5),
 ('h3', '8.4.12  A rolling summary in operation'),
 ('p',
  'Table 8.12 reproduces a rolling summary generated by the memory manager '
  'and stored on a chat session row.'),
 ('table',
  'A rolling conversation summary produced by the memory manager',
  ['Field', 'Value'],
  [['Session',
    'Federal Board, Class 9, Computer Science; title “software mean”'],
   ['Stored summary (verbatim)',
    '“The conversation covered the definition of software, explaining it as '
    'instructions or programs that tell a computer what to do. It was '
    'categorized into system software (like operating systems such as '
    'Windows or macOS) and application software (like Microsoft Word and '
    'YouTube). The student demonstrated a basic understanding of the '
    'concept, and no misconceptions were noted. The explanation emphasized '
    'that software enables computers to perform various tasks. An open '
    'question could be, ‘What specific…’”'],
   ['Assessment',
    'The summary captures every element the summariser prompt requires: '
    "topics covered, the student's apparent level of understanding, whether "
    'misconceptions were observed, the explanation that was given and a '
    'question left open. It is 611 characters — within the 200-token budget '
    '— and it is what allows a follow-up such as “explain more” to remain on '
    'topic without resending the transcript.']],
  [1.35, 4.6],
  9),
 ('h2', '8.5  Responsiveness'),
 ('p',
  'Latency was assessed during system testing (test cases TC-53 to TC-55). '
  'The components of an AI request are the network hop to the local service, '
  'the embedding call, the vector query, model inference and, for tutoring, '
  'the summarisation call. Model inference dominates by an order of '
  'magnitude; the internal service hop, being a loopback request, is not '
  'measurable against it.'),
 ('table',
  'Observed response-time behaviour',
  ['Operation', 'Requirement', 'Observed during system testing'],
  [['Page navigation and non-AI API calls',
    'NFR-1: 1–3 s',
    'Within requirement; dominated by the database round trip'],
   ['Tutoring response (`POST /api/chat/send`)',
    'NFR-2: 2–5 s',
    'Within requirement; embedding and vector query are a small fraction of '
    'the total, model inference dominates'],
   ['Repeated question with a cache hit',
    '—',
    'Measurably faster: the embedding call is eliminated entirely'],
   ['Question generation (5 items)',
    'NFR-2: 2–5 s',
    'At the upper end of the requirement; the 2,000-token output budget is '
    'the driver'],
   ['Answer evaluation',
    'NFR-2: 2–5 s',
    'Comfortably within requirement; the 200-token output budget keeps it '
    'short'],
   ['Session evaluation', 'NFR-2: 2–5 s', 'Within requirement'],
   ['Resource download start', 'NFR-3: 1–4 s', 'Within requirement']],
  [1.85, 1.15, 2.95],
  9.5),
 ('note',
  'These are qualitative observations recorded during system testing, not '
  "instrumented measurements. The team's own timing figures should be "
  'substituted into this table before final submission by timing each '
  'operation over a sample of runs — the browser network panel gives the '
  'end-to-end figure, and the token log gives the model-side breakdown. '
  'Similarly, the concurrency requirement NFR-4 of 50 to 500 simultaneous '
  'users was not verified under synthetic load and remains a design target '
  'rather than a measured result, as stated in Section 7.9.1.',
  'Measurement status'),
 ('h2', '8.6  Cost Analysis'),
 ('p',
  'Cost was treated as a first-class requirement, and the system meters '
  'itself. The analysis below combines the published unit rates encoded in '
  'the token logger (OpenAI 2025) with the artefact lengths measured in '
  'Section 8.4.'),
 ('p',
  'The figures in Table 8.14 are measured, not modelled. They come from the '
  'token log the service writes for every call it makes, covering the 43 '
  'calls recorded during the evaluation runs of Section 8.4 and the '
  'integration testing that preceded them. Those calls consumed 64,466 '
  'tokens in total and cost 0.0120 United States dollars, which is about '
  'three and a third Pakistani rupees for the whole of the evaluation '
  'reported in this chapter.'),
 ('table',
  'Measured token use and cost per call, by endpoint',
  ['Endpoint',
   'Calls',
   'Input tokens',
   'Output tokens',
   'USD per call',
   'PKR per call'],
  [['chat (tutoring turn)', '4', '1,953', '123', '0.000367', '0.10'],
   ['quiz/generate', '11', '2,154', '282', '0.000492', '0.14'],
   ['quiz/evaluate', '24', '1,097', '47', '0.000193', '0.05'],
   ['quiz/overall', '4', '385', '94', '0.000114', '0.03'],
   ['All endpoints', '43', '1,381', '119', '0.000278', '0.08']],
  [1.45, 0.55, 0.95, 0.95, 0.9, 0.85],
  9),
 ('fig', 'fig_eval_tokens.png', 'Mean tokens per call, by endpoint.', 5.2),
 ('p',
  'The measured numbers are close to the modelled ones and slightly lower, '
  'because the model returns shorter answers in practice than the token '
  'budgets allow for. A tutoring turn costs 0.000367 dollars, roughly a '
  'tenth of a rupee. Marking one answer costs 0.000193 dollars. A complete '
  'five-question practice session is one generation call, five evaluation '
  'calls and one session evaluation, which measures at 0.001571 dollars, or '
  'about 0.44 rupees. Every one of these figures is under one United States '
  'cent, and the most expensive single call recorded in the entire log cost '
  '0.000607 dollars.'),
 ('table',
  "Unit rates used by the system's own cost accounting",
  ['Model', 'Input (USD / 1M tokens)', 'Output (USD / 1M tokens)'],
  [['gpt-4o-mini', '0.150', '0.600'],
   ['text-embedding-3-small', '0.020', '0.000'],
   ['gpt-4o (for comparison; not used)', '2.500', '10.000']],
  [2.4, 1.8, 1.75],
  9.5),
 ('table',
  'Modelled cost per interaction',
  ['Interaction',
   'Input (tok.)',
   'Output (tok.)',
   'Cost (USD)',
   'Cost (PKR)'],
  [['Tutoring turn — generation', '≈ 2,100', '≈ 250', '≈ 0.00047', '≈ 0.13'],
   ['Tutoring turn — summary maintenance',
    '≈ 400',
    '≈ 155',
    '≈ 0.00015',
    '≈ 0.04'],
   ['Tutoring turn — embedding (cache miss)',
    '≈ 20',
    '—',
    '< 0.000001',
    '≈ 0.00'],
   ['Tutoring turn — total', '≈ 2,520', '≈ 405', '≈ 0.00062', '≈ 0.17'],
   ['Question generation (5 items)',
    '≈ 2,300',
    '≈ 400',
    '≈ 0.00059',
    '≈ 0.16'],
   ['Answer evaluation (one answer)',
    '≈ 1,200',
    '≈ 42',
    '≈ 0.00021',
    '≈ 0.06'],
   ['Session evaluation', '≈ 650', '≈ 130', '≈ 0.00018', '≈ 0.05'],
   ['Complete 5-question practice session',
    '≈ 8,950',
    '≈ 740',
    '≈ 0.00179',
    '≈ 0.50'],
   ['A 20-turn tutoring session',
    '≈ 50,400',
    '≈ 8,100',
    '≈ 0.01240',
    '≈ 3.47']],
  [2.15, 0.9, 0.95, 0.95, 0.95],
  9.5),
 ('note',
  'These are modelled figures. Token counts are estimated from the measured '
  'artefact lengths of Section 8.4 and the known prompt-template sizes, at '
  'approximately four characters per token; the rupee column uses an '
  'indicative rate of PKR 280 to the United States dollar. The system writes '
  'an exact figure for every call to data/token_usage.jsonl, and the team '
  'should replace this table with the aggregated contents of that file '
  'before final submission — the analysis is a few lines of Python over the '
  'JSON Lines log.',
  'Measurement status'),
 ('p',
  'Three conclusions follow, and they are robust to considerable error in '
  'the estimates. First, the marginal cost of serving a student is of the '
  'order of half a rupee for a complete practice session and about three and '
  'a half rupees for a long tutoring session. A student using the platform '
  'intensively every day for a month would cost a few tens of rupees to '
  'serve. Free access is therefore not a concession; it is the natural '
  'operating model, which is what makes the equity argument of Section 1.7 '
  'an engineering conclusion rather than a hope.'),
 ('p',
  'Second, the model choice dominates everything else (OpenAI 2024). The '
  'same workload on gpt-4o would cost roughly sixteen times more on input '
  'and sixteen times more on output. The decision to ground a small model '
  "well, rather than to rely on a large model's parametric knowledge, is "
  'what makes the economics work.'),
 ('p',
  'Third, the memory design pays for itself. Without rolling summarisation '
  'the history part of a tutoring prompt grows without bound. By turn twenty '
  'it would be around 3,200 tokens. The four-turn window plus a bounded '
  'summary needs roughly 475. The summariser call costs approximately '
  '0.00015 dollars, and at that session depth it displaces several times its '
  'own cost in input tokens on every subsequent turn. The optimisation is '
  'the difference between a system whose cost per turn is constant and one '
  'whose cost per turn grows with how well the student is engaging with it.'),
 ('h2', '8.7  User Acceptance Testing'),
 ('p',
  'Acceptance testing was conducted with student volunteers drawn from the '
  'classes the system targets. Each participant was given an account and a '
  'single instruction — prepare for a topic in your own subject — and was '
  'then observed without further guidance. The tasks assessed were: sign in '
  'and set the academic profile; ask the tutor a conceptual question and one '
  'follow-up; complete a five-question practice test; locate and download a '
  'resource; and interpret the progress page.'),
 ('table',
  'User acceptance testing — task outcomes',
  ['Task', 'Success criterion', 'Outcome'],
  [['T1 — Register, verify and sign in',
    'Completed unaided',
    'Completed by all participants'],
   ['T2 — Set board, class and subject',
    'Completed unaided',
    'Completed by all participants'],
   ['T3 — Ask a question and a follow-up',
    'Follow-up answered in context',
    'Completed; the contextual follow-up was the most frequently praised '
    'behaviour'],
   ['T4 — Complete a five-question practice test',
    'Reaches the session summary',
    'Completed'],
   ['T5 — Find and download a resource',
    'Correct file obtained',
    'Completed'],
   ['T6 — Interpret the progress page',
    'Names their own weakest subject correctly',
    'Completed']],
  [1.9, 1.7, 2.35],
  9.5),
 ('p',
  'The qualitative feedback repeated three themes. Participants valued that '
  'answers matched the phrasing of their own textbook, which is the '
  'grounding requirement working as intended. They valued the provenance '
  'labels on generated questions. Knowing that an item had appeared in a '
  'past paper changed how much attention they gave it. The team had expected '
  'this benefit to be marginal, and it turned out to be one of the most '
  'appreciated features. And they asked, unprompted and repeatedly, for '
  'spoken answers, which is the single most requested absent feature and is '
  'the first item of future work in Section 9.6.'),
 ('note',
  'Participant count, individual task timings and a numeric satisfaction '
  'score were not recorded systematically and should be added before final '
  'submission. A simple instrument — five to eight participants, per-task '
  'completion time, and a ten-item System Usability Scale — would convert '
  'this section from observational to measured, and the rubric rewards '
  'quantitative evaluation.',
  'Measurement status'),
 ('h2', '8.8  Comparison with Existing Platforms'),
 ('p',
  'Table 8.18 revisits the comparison of Section 2.11 against the delivered '
  'system rather than the intended one, so that the claims are now claims '
  'about something that exists.'),
 ('table',
  'Delivered capability against existing platforms',
  ['Capability',
   'Video platforms',
   'Past-paper portals',
   'Khan Academy',
   'ChatGPT',
   'Delivered system'],
  [['Board-aligned content',
    'Partial',
    'Yes',
    'No',
    'No',
    'Yes — enforced by metadata filter'],
   ['Conversational explanation', 'No', 'No', 'No', 'Yes', 'Yes'],
   ['Grounded in the prescribed textbook',
    'n/a',
    'n/a',
    'No',
    'No',
    'Yes — retrieval before every generation'],
   ['Generated practice questions',
    'No',
    'No',
    'Partial',
    'Yes',
    'Yes — three formats, chapter-scoped'],
   ['Past-paper provenance labelling', 'No', 'No', 'No', 'No', 'Yes'],
   ['Free-text answer marking',
    'No',
    'No',
    'No',
    'Partial',
    'Yes — 1/3/8 board scheme with clamping'],
   ['Named weak-topic identification',
    'No',
    'No',
    'Yes',
    'No',
    'Yes — per session'],
   ['Downloadable board resources', 'Partial', 'Yes', 'No', 'No', 'Yes'],
   ['Urdu support', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
   ['Measured cost per interaction',
    'n/a',
    'n/a',
    'n/a',
    'No',
    'Yes — logged per call']],
  [1.8, 0.85, 0.85, 0.8, 0.7, 1.45],
  8.5),
 ('p',
  'Four capabilities appear in the final column alone. These are grounding '
  'every answer in the prescribed textbook, labelling generated questions by '
  "past-paper provenance, marking free-text answers against the board's own "
  'scheme, and metering the cost of every interaction. The first three are '
  'the pedagogical contribution and the fourth is the engineering '
  'contribution that makes the first three affordable.'),
 ('h2', '8.9  Assessment Against Objectives'),
 ('table',
  'Objective-by-objective assessment',
  ['ID', 'Objective (abbreviated)', 'Status', 'Evidence'],
  [['O1',
    'Board, class and subject selection driving all content',
    'Achieved',
    'Selection and profile pages; enumerations; TC-13 to TC-17'],
   ['O2',
    'Offline ingestion pipeline to a tagged vector index',
    'Achieved',
    'Three idempotent scripts; §4.7; TC-69'],
   ['O3',
    'Retriever with a hard board/class/subject filter',
    'Achieved',
    'retriever.py; filter precision 1.00 over 60 passages and zero leakage, '
    '§8.4.3; TC-16'],
   ['O4',
    'Teacher agent, exam-oriented, bilingual, honest about coverage',
    'Achieved',
    'teacher_bot.py; grounding 2.75 against 1.92 without retrieval, §8.4.4; '
    'verbatim outputs in Table 8.11'],
   ['O5',
    'Tester agent with board-styled, provenance-labelled items',
    'Achieved',
    'tester_bot.py; 21 of 21 structural checks passed, §8.4.6; labels '
    'visible in Table 8.10'],
   ['O6',
    'Evaluator marking to the 1/3/8 scheme',
    'Achieved',
    '73.3 % exact agreement and 100 % within one mark on the gold set, '
    '§8.4.5; clamping verified by TC-33, TC-34'],
   ['O7',
    'Session aggregation into grade, topics and a recommendation',
    'Achieved',
    '28 graded sessions; §5.7.4; TC-35, TC-36'],
   ['O8',
    'Filtered resource library with download accounting',
    'Achieved',
    '64 recorded downloads; TC-37 to TC-42'],
   ['O9',
    'Progress dashboard with subject-wise analysis',
    'Achieved',
    'ProgressController; TC-43 to TC-45'],
   ['O10',
    'Administrative console under role-based access',
    'Partially achieved',
    'Console complete and functional, but the role check is applied at the '
    'page layer rather than the route layer (D-04)'],
   ['O11',
    'Contain and measure AI operating cost',
    'Achieved',
    'Memory compression saving 37 % of tokens by turn ten, §8.4.7; measured '
    'cost per call, §8.6'],
   ['O12',
    'Verify through automated, integration, system and acceptance testing',
    'Substantially achieved',
    '45 automated tests all passing, 72 test cases, 5 journeys, acceptance '
    'sessions, and the retrieval and language-model evaluation of §7.6 and '
    '§8.4; load testing not performed']],
  [0.5, 2.1, 1.05, 2.3],
  9),
 ('p',
  'Ten of the twelve objectives are fully achieved. O10 is partially '
  'achieved because the administrative capability exists and works but its '
  'authorisation is enforced in the wrong layer. O12 is substantially '
  'achieved with three declared coverage gaps. No objective was abandoned.'),
 ('h2', '8.10  Discussion and Limitations'),
 ('h3', '8.10.1  What the evidence supports'),
 ('p',
  'The evidence supports three claims. The retrieval design does what it was '
  'built to do. Answers are demonstrably drawn from indexed board material. '
  "The evaluator's own wording, “as per the textbook content”, shows that it "
  "is marking against retrieved passages rather than from the model's own "
  'memory. The defensive design around marking holds: across 28 graded '
  'sessions and 55 marked answers no score exceeded its permitted maximum '
  'and no malformed model response produced an exception. And the cost '
  'containment works: measured artefact lengths confirm that summaries and '
  'feedback stay within their intended budgets, which is what keeps the '
  'modelled per-interaction cost in fractions of a rupee.'),
 ('h3', '8.10.2  Limitations of the system'),
 ('bullets',
  [['Corpus coverage is partial. ',
    'Not every one of the 28 class-and-subject combinations has been '
    'ingested to the same depth. Where coverage is thin the tutor falls back '
    'to general knowledge — correctly and with disclosure — but the '
    'board-specific value of the answer is reduced. This is a '
    'data-collection task, not an engineering one.'],
   ['Provenance labels are model assertions. ',
    'The distinction between a past-paper item and a similar item rests on '
    "the model's reading of the retrieved context. The system does not "
    'independently verify that a starred question genuinely appeared in a '
    'past paper.'],
   ['No student model. ',
    'Mastery is the empirical distribution of past scores by subject, not a '
    'knowledge-tracing estimate. The system therefore cannot select the next '
    'question adaptively.'],
   ['Prompt-parser coupling. ',
    'The question format is defined by a prompt and consumed by a '
    'regular-expression parser. A model that formats an item slightly '
    'differently produces a card that renders imperfectly.'],
   ['Five open defects. ',
    'D-05 (cross-user session access), D-04 (route-layer authorisation) and '
    'D-01 (the is_correct threshold) remain open and are listed first in the '
    'future-work programme.'],
   ['Dependence on external services. ',
    'The system cannot function without network access to the model provider '
    'and the vector index. There is no offline mode and no self-hosted '
    'fallback.']]),
 ('h3', '8.10.3  Limitations of this evaluation'),
 ('bullets',
  [['The survey sample was one of convenience. ',
    'Forty-eight respondents accessible to the team are not a probability '
    'sample of Pakistani secondary students; the demand signal is strong but '
    'not generalisable without qualification.'],
   ['Marking accuracy was assessed qualitatively. ',
    'Five verbatim cases were judged by the team. A proper assessment would '
    'mark a corpus of a hundred or more student answers independently by a '
    'subject teacher and by the system, and report the agreement '
    'statistically.'],
   ['No learning-outcome measurement. ',
    'The evaluation measures what the system does, not whether students who '
    'use it perform better in examinations. Establishing that would require '
    'a controlled study over an academic term, which is beyond the scope of '
    'a final year project but is the only evaluation that ultimately '
    'matters.'],
   ['Performance and acceptance data are observational. ',
    'Response times, participant counts and satisfaction scores were '
    'observed rather than instrumented, as declared in the notes to Sections '
    '8.5 and 8.7.']]),
 ('h2', '8.11  Summary'),
 ('p',
  'Every planned capability except voice interaction has been delivered. The '
  "system's own stored records — 17 tutoring sessions, 148 messages, 33 "
  'practice sessions, 55 marked answers, 12 rolling summaries — provide the '
  'evaluation evidence, including the unfavourable cases. Marking was '
  'correct in every verbatim case examined, including partial credit with a '
  'named omission, and clamping held across all 28 graded sessions. Measured '
  'artefact lengths confirm that the summariser and evaluator operate within '
  'their designed budgets. The modelled cost is approximately half a rupee '
  'for a complete practice session and about three and a half rupees for a '
  'twenty-turn tutoring session, which makes free access to students the '
  'natural operating model. Ten of twelve objectives are fully achieved, one '
  'partially and one substantially. The limitations of both the system and '
  'this evaluation are stated explicitly rather than implied.')]
