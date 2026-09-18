"""Content blocks for Chapter 9 - Conclusion and Future Work."""

BLOCKS = [('chapter', 'CHAPTER 9', 'CONCLUSION AND FUTURE WORK'),
 ('p',
  'This chapter closes the report. It states what the project set out to do '
  'and what it achieved, lists the contributions, sets out the strengths and '
  'the limitations openly, gives the cost position, and sets out the work '
  'that should follow.'),
 ('h2', '9.1  Conclusion'),
 ('p',
  'This project set out to answer a specific engineering question. How can a '
  'large language model be held, at acceptable cost and speed, to teaching, '
  'examining and marking strictly within the syllabus of a named Pakistani '
  'board, class and subject? And how can that capability be delivered '
  'through a secure, maintainable and usable web application?'),
 ('p',
  'The answer developed here is that curricular constraint must be '
  'structural rather than instructional. Asking a model in a prompt to stay '
  'within a syllabus is advice that it may or may not follow, and that it '
  'cannot follow at all for material it has never seen. The alternative is '
  'to filter the index during the search, on board, class and subject, and '
  'then require the model to answer from the passages that come back. That '
  'turns the constraint into a property of the architecture. A Class 9 '
  'student cannot be answered from a Class 12 textbook, not because the '
  'model was asked not to, but because the Class 12 vectors were never '
  'candidates for retrieval.'),
 ('p',
  'That claim was tested rather than asserted. Over thirty curriculum '
  'questions every retrieval returned relevant material, and all sixty '
  'passages that were read back carried exactly the board, class and subject '
  'that had been requested, a filter precision of 1.00. Three probes for '
  'material outside the indexed corpus returned nothing at all, and the same '
  'question asked under two different class filters returned two sets of '
  'passages with nothing in common. The scoping is therefore structural in '
  'the measured sense as well as the intended one: there is no observed path '
  'by which one cohort’s textbook can reach another cohort’s student.'),
 ('p',
  'Around that single idea a complete platform was built. Board textbooks, '
  'keybooks and past papers were converted from scanned images into a '
  'searchable, metadata-tagged vector index through a four-stage idempotent '
  'pipeline built specifically for the noise characteristics of Pakistani '
  'board material. Four agents share that index: a teacher, a tester, an '
  'evaluator and a session evaluator. They differ only in prompt, decoding '
  'temperature and token budget. That is enough to obtain distinct and '
  'reliable behaviour from one inexpensive general-purpose model, with no '
  'fine-tuning of any kind. A Laravel application provides authentication, '
  'persistence, authorisation and orchestration; a React interface delivers '
  'it; and a conversation-memory design keeps the cost of a tutoring session '
  'approximately constant in its depth rather than linear in it.'),
 ('p',
  'The result is a working system of approximately 18,500 lines of '
  'first-party code across three runtimes. It covers four classes, seven '
  'subjects and 379 mapped chapters, with the Federal Board corpus indexed '
  'and the AJK Board supported by the design but not yet ingested. It is '
  'verified by 45 automated tests and 72 documented test cases, and it costs '
  'on the order of half a rupee to serve a complete practice session. Ten of '
  'the twelve stated objectives were fully achieved, one partially and one '
  'substantially, and every shortfall is recorded in this report with the '
  'specific correction required.'),
 ('p',
  'The effect of that scoping on what the model writes was measured by '
  'ablation. Twelve questions were answered twice, once through the '
  'retrieval path and once with retrieval disabled, and both answers were '
  'graded by an independent model against the same passages. Grounding rose '
  'from 1.92 to 2.75 out of five, unsupported claims fell, and retrieval '
  'produced a worse answer on none of the twelve. The evaluator agent agreed '
  'exactly with a pre-agreed mark on 73.3 per cent of a fifteen-answer gold '
  'set and was within one mark on every single item, a mean error of 0.27 '
  'marks. Generated question sets passed all twenty-one structural checks. '
  'The memory manager held prompt size flat where an unmanaged session grew '
  'without limit, saving 37 per cent of tokens by the tenth turn.'),
 ('p',
  'The wider conclusion is an economic one. One thing separates passing from '
  'excelling in a Pakistani board examination: a tutor who explains from the '
  "prescribed book, sets questions in the board's own style and marks "
  'honestly. That guidance has historically been available only to students '
  'whose families can pay for it. This project shows that the same guidance '
  'can be delivered for a fraction of a rupee per interaction by grounding a '
  'small, cheap model in a corpus that costs a few dollars to build. The '
  'barrier to educational equity in this particular respect is no longer '
  'technical, and it is no longer financial. It is only a matter of somebody '
  'assembling the pieces.'),
 ('h2', '9.2  Contributions'),
 ('numbers',
  ['A board-, class- and subject-filtered retrieval design in which '
   'curricular scoping is a metadata pre-filter applied during the vector '
   'search, making syllabus alignment a structural guarantee rather than a '
   'prompt instruction.',
   'An ingestion pipeline tuned to the specific noise of Pakistani board '
   'material — scanned pages requiring optical character recognition, '
   'keybook watermarks, examination headers and roll-number boxes, and mixed '
   'English–Urdu script — with auditable rule-based cleaning and idempotence '
   'at every stage.',
   'A four-agent decomposition over a single shared retriever, showing that '
   'specialisation by prompt, temperature and token budget replaces '
   'fine-tuning for this class of application.',
   'A provenance-labelling scheme for generated questions that tells a '
   'student whether an item is drawn from a past paper, modelled on one, or '
   'newly written — reported during acceptance testing as one of the most '
   'valued features.',
   "A rubric-driven marking design that applies the board's own 1, 3 and 8 "
   'mark scheme, returns what was correct and what was missing as separate '
   'statements, and defends every displayed number by parsing, clamping and '
   'recomputation in application code.',
   'A conversation-memory strategy that bounds prompt growth, making '
   'per-turn cost approximately independent of session depth.',
   'Per-call token and cost instrumentation attributed by board, class and '
   'subject, which turns the economics of the platform into a measured '
   'engineering property and is the basis of the affordability claim.',
   'A reproducible evaluation harness for the retrieval and language-model '
   'layers, which measures filter precision, grounding against a '
   'no-retrieval control, marking accuracy against a gold set, structural '
   'validity of generated questions and prompt growth, and writes its '
   'results to disk so that every figure quoted in this report can be traced '
   'to the run that produced it.',
   'A complete, working, documented and tested implementation, together with '
   'an honest defect log and a candid statement of what was not tested.']),
 ('h2', '9.3  Strengths'),
 ('bullets',
  [["Architectural honesty about the model's role. ",
    'The model is trusted for judgement and never for arithmetic. Every '
    'score, total, percentage and grade a student sees is computed in '
    'application code from values the model produced, and the computed '
    "values overwrite the model's own."],
   ['Genuine substitutability. ',
    'The artificial-intelligence tier is reachable through four JSON '
    'endpoints and one configuration value. It can be replaced by a '
    'different provider, a self-hosted open-weight model or a test stub '
    'without touching application code.'],
   ['Cost as an engineered property. ',
    'Because every call is metered at the point of use, a change that '
    'doubles token consumption is visible on the next request rather than on '
    'the next invoice.'],
   ['Curriculum depth. ',
    '379 named chapters across 28 class-and-subject combinations allow '
    'practice to be scoped to what a student is actually revising this '
    'week.'],
   ['Failures documented rather than hidden. ',
    'Fifteen defects are logged, five of them still open, and three testing '
    'gaps are declared. The two automated tests that failed for most of the '
    'project were retained rather than deleted, because deleting them would '
    'have removed real information.']]),
 ('h2', '9.4  Limitations'),
 ('bullets',
  [['Five open defects. ',
    'Two of them are security findings and are the first items of future '
    'work in Section 9.6.1: cross-user chat-session access (D-05) and '
    'route-layer authorisation for administrative endpoints (D-04). The '
    'other three are low severity and are recorded with their reasoning in '
    'Table 7.10.'],
   ['Only one board is actually indexed. ',
    'The data model, the interface and the retrieval filter all carry the '
    'board field, and the Federal Board corpus holds 8,057 chunks across 27 '
    'class-and-subject combinations. No AJK Board material has been '
    'ingested, so a student who selects that board is answered without '
    'retrieved context. Class 9 Biology is likewise unpopulated. Closing '
    'both gaps is an ingestion run rather than a code change, but until it '
    'is done the claim of two-board coverage is a claim about the design and '
    'not about the delivered corpus.'],
   ['No adaptive sequencing. ',
    'Without a student model the system cannot choose the next question on '
    'the basis of what the learner has just demonstrated.'],
   ['No learning-outcome evidence. ',
    'The evaluation establishes what the system does, not that students who '
    'use it perform better in examinations.'],
   ['Hard dependence on external services. ',
    'There is no offline mode and no self-hosted fallback for either '
    'retrieval or generation.'],
   ['Unverified concurrency. ',
    'The 50-to-500 concurrent-user requirement is a design target; no load '
    'test was performed.'],
   ['The evaluation judge is a model, not an examiner. ',
    'Grounding and answer quality were scored automatically. That makes the '
    'measurement repeatable and affordable, but a model judge inherits its '
    'own biases, and the query and gold sets were written by the project '
    'team. The numbers show a direction reliably; they are not an '
    'independent benchmark.']]),
 ('h2', '9.5  Cost Position'),
 ('p',
  'The development cost of the project was effectively limited to metered '
  'third-party usage. Building the corpus cost a few dollars of embedding. '
  'Optical character recognition stayed within the free monthly allowance '
  'because ingestion was staged. A free serverless vector tier was adequate '
  'for the indexed material, and language-model usage ran at a fraction of a '
  'cent per interaction. Hardware, tooling and identity services were free. '
  'Projected production hosting is a small cloud instance or shared PHP '
  'hosting at roughly PKR 1,500 to 3,000 per month plus PKR 1,500 per year '
  'for a domain.'),
 ('p',
  'The operating position matters more than the development position. '
  'Section 8.6 puts a five-question practice session at about PKR 0.50 and a '
  'twenty-turn tutoring session at about PKR 3.47. A student using the '
  'platform heavily every day for a month therefore costs a few tens of '
  'rupees to serve. A cohort of a thousand such students costs less per '
  "month than a single tuition-academy salary. That ratio is the project's "
  'economic result, and it is the reason the equity claim in Section 1.7 is '
  'stated as a conclusion rather than an aspiration.'),
 ('h2', '9.6  Future Work'),
 ('h3', '9.6.1  Immediate remediation'),
 ('numbers',
  ['Scope every chat-session query to the authenticated user (D-05). This is '
   'the highest priority item in this report: `ChatController::messages`, '
   '`history` and `delete` must constrain by user_id, or a policy must be '
   'applied. Two lines per method.',
   'Apply role middleware to the administrative API route groups (D-04) so '
   'that authorisation does not depend on the caller having arrived through '
   'the administrative interface.',
   'Derive the is_correct threshold from question_type (D-01) so the flag is '
   'meaningful for multiple-choice and short answers.',
   "Assign the 'student' role and a random placeholder password on the "
   'federated sign-in path (D-07, D-08).']),
 ('h3', '9.6.2  Short-term enhancements'),
 ('numbers',
  ['Spoken answers. Voice input is delivered, so a student can dictate a '
   'question, but the system does not read its replies aloud. Four students '
   'asked for voice answers in the survey, and text-to-speech is the natural '
   'completion of the feature.',
   'Structured model output. Replacing the prompt-and-regular-expression '
   'contract for generated questions with a JSON schema enforced by the '
   "provider's structured output mode would remove the coupling described in "
   'Section 8.10.2 and eliminate an entire class of rendering defect.',
   'Automated testing of the artificial-intelligence path against a stubbed '
   'model, asserting on structural properties — the presence of a SCORE '
   'line, the item count, the score range, the presence of a provenance '
   'label — rather than on content.',
   'Load testing to verify NFR-4 and to establish the concurrency ceiling of '
   'the single-instance deployment.',
   'Corpus completion, so that every one of the 28 class-and-subject '
   'combinations is ingested to the same depth.',
   'A larger evaluation set. The harness of Section 7.6 uses thirty '
   'retrieval queries and fifteen marked answers, which is enough to show a '
   'direction but not to quote a confidence interval. Expanding both, and '
   'having a teacher rather than a model mark the gold set, would turn '
   'indicative results into defensible ones.',
   'A strict grounding mode. The teacher prompt currently allows a '
   'general-knowledge fallback when the corpus does not cover a topic, which '
   'is why the measured groundedness of 2.75 out of five is a lower bound. '
   'Adding a strict mode that refuses instead, and comparing the two '
   'policies on the same questions, would separate the cost of the fallback '
   'from its benefit.']),
 ('h3', '9.6.3  Medium-term extensions'),
 ('numbers',
  ['Additional boards. Punjab, Sindh, Khyber Pakhtunkhwa and Balochistan are '
   'architecturally supported already; adding one is a data-ingestion '
   'exercise, not a code change. This is the single highest-leverage '
   'extension available.',
   'A student model with knowledge tracing, so that mastery is estimated per '
   'topic and the next question is chosen adaptively rather than sampled '
   'from the selected chapters.',
   'A teacher dashboard allowing a class to be created, progress to be '
   'viewed in aggregate and weak topics to be identified across a cohort — '
   'the feature most likely to drive institutional adoption.',
   'A parent view giving a summary of activity and progress without exposing '
   'individual transcripts.',
   'Native mobile applications, or at minimum a progressive web application '
   'with an installable shell and cached resources.',
   'Spaced-repetition revision that reintroduces items from previously '
   'identified weak topics at increasing intervals.']),
 ('h3', '9.6.4  Longer-term research directions'),
 ('numbers',
  ['A controlled evaluation of learning outcomes over an academic term, '
   'comparing board results between students who use the platform and a '
   'matched group who do not. This is the only evaluation that ultimately '
   "establishes the system's value.",
   'Hybrid retrieval combining dense vectors with sparse lexical matching, '
   'which the literature reports as superior to either alone for factual '
   'queries where exact terminology matters — as it does in a textbook '
   'definition.',
   'Self-hosted open-weight models, which would remove the dependence on a '
   'commercial provider and the network, at the cost of graphics hardware. '
   'Falling inference costs make this progressively more attractive.',
   'Automatic provenance verification, matching a generated question against '
   'the indexed past-paper corpus so that a past-paper label is a verified '
   'fact rather than a model assertion.',
   'Extension beyond the school curriculum to university entry-test '
   'preparation, where the same architecture applies to a different '
   'corpus.']),
 ('h2', '9.7  Reflection on the Design Process'),
 ('p',
  'Three lessons from the process deserve recording, because they generalise '
  'beyond this project.'),
 ('p',
  'The first is that instrumentation should precede optimisation. The token '
  'logger was written before anyone knew what the system cost, and it was '
  'that log which revealed that conversation cost grew with session length. '
  'Without it the problem would have surfaced as a billing surprise rather '
  'than as an engineering observation, and the memory manager would probably '
  'never have been built. Measuring a property is what makes it possible to '
  'design for it.'),
 ('p',
  'The second is that the absence of evidence is not evidence of absence. '
  'The most instructive defect of the project was a tutor that told a '
  'student a topic was not in their syllabus when in fact it was simply not '
  'yet in the index. A retrieval-grounded system knows only what it has '
  'retrieved, and a design that conflates “I found nothing” with “there is '
  'nothing” will confidently mislead exactly the users least equipped to '
  'detect it. Distinguishing the two cases explicitly is now the single most '
  'important rule in the teacher prompt.'),
 ('p',
  'The third is that validating assumptions with real users before building '
  'is worth more than any amount of subsequent cleverness. The survey '
  'changed the design. The finding that students study unsupervised at home '
  'made automatic marking essential rather than optional. The split between '
  'those needing conceptual help and those needing both concepts and '
  'practice is the reason the system has two agents rather than one. Every '
  'one of those decisions would have been a guess without forty-eight honest '
  'answers, and at least one of them would have been the wrong guess.'),
 ('p',
  'The project ends with a system that works, a set of defects it does not '
  'hide, and a clear view of what should be built next. That is a '
  'satisfactory place for a final year project to finish.')]
