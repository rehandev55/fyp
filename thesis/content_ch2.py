"""Content blocks for Chapter 2 - Literature Review."""

BLOCKS = [('chapter', 'CHAPTER 2', 'LITERATURE REVIEW'),
 ('p',
  'This chapter reviews the work this project builds on. It moves from the '
  'broad field of artificial intelligence in education to the specific '
  'techniques the system uses: intelligent tutoring, conversational agents, '
  'large language models and their limits, retrieval-augmented generation, '
  'vector search, automatic marking, and how such systems are evaluated. It '
  'then surveys what is actually available to a Pakistani school student '
  'today, and states the gap this project fills.'),
 ('h2', '2.1  Introduction'),
 ('p',
  'This chapter surveys the body of work on which the project rests. It is '
  'organised as a narrowing argument. Sections 2.2 to 2.4 establish what is '
  "already known about using computers to tutor, beginning with Bloom's "
  'demonstration of the power of one-to-one instruction and ending with the '
  'modern generation of conversational agents. Sections 2.5 to 2.7 examine '
  'large language models, the technology that makes conversational tutoring '
  'newly plausible. They also cover the failure mode that makes those models '
  'dangerous in a classroom, and the retrieval architecture that contains '
  'it. Section 2.8 reviews automatic marking of free-text answers, which is '
  'the second capability the system must provide. Section 2.9 covers the '
  'document-processing problem specific to a low-resource corpus of scanned '
  'Pakistani board material. Section 2.10 surveys the educational-technology '
  'products actually available to a Pakistani secondary student today, and '
  'Section 2.11 compares them systematically. Section 2.12 states the '
  'resulting research gap, which this project occupies.'),
 ('h2', '2.2  Artificial Intelligence in Education'),
 ('p',
  'The empirical case for individual tutoring predates computing in '
  "education. Bloom's study of mastery learning reported that students "
  'taught one-to-one performed approximately two standard deviations better '
  'than students taught in a conventional classroom (Bloom 1984). The '
  'finding — universally known as the two-sigma problem — framed an agenda '
  'that has occupied educational technology ever since: the effect of '
  'individual tutoring is enormous, and individual tutoring is unaffordable '
  'at population scale. Every subsequent generation of educational '
  'technology can be read as an attempt to recover some fraction of that '
  'two-sigma effect at a cost per student that a state or a family can '
  'bear.'),
 ('p',
  'Holmes, Bialik and Fadel survey the modern field and separate three roles '
  'that artificial intelligence plays in education (Holmes, Bialik, and '
  'Fadel 2019; Luckin et al. 2016). In learning with AI the system delivers '
  'the instruction. In learning about AI the technology is itself the '
  'subject. In learning through AI, analytics inform a human teacher. This '
  'project sits firmly in the first category. Zawacki-Richter and colleagues '
  'reviewed 146 studies of artificial intelligence in higher education '
  '(2019). They found that applications fall into four groups: profiling and '
  'prediction, assessment and evaluation, adaptive and personalised systems, '
  'and intelligent tutoring systems. They also noted two persistent '
  'weaknesses. The field reflects too little on what its tools mean for '
  'teaching and ethics, and almost all of the work comes from well-resourced '
  "institutions. Nye's review of intelligent tutoring in the developing "
  'world identifies exactly the constraints this project operates under: '
  'intermittent connectivity, low-specification devices, limited local '
  'content and the absence of trained facilitators (Nye 2015).'),
 ('p',
  "UNESCO's guidance for policy-makers is explicit that equity must be the "
  'organising principle, not an afterthought (2021). It warns that systems '
  'trained and tested on the material of wealthy education systems tend to '
  'serve everyone else badly. That warning is directly applicable here: a '
  'general-purpose model has seen an enormous quantity of American and '
  'European curricular material and comparatively little Pakistani board '
  'material. The remedy adopted in this project is not to retrain the model '
  'but to supply the missing material at inference time.'),
 ('p',
  'Pardos and Heffernan situate the contemporary opportunity in the '
  'availability of large-scale learner interaction data and the maturation '
  'of machine-learning methods that can exploit it (Pardos and Heffernan '
  '2020). Rahman, Khan and Iqbal examine the specific case of Pakistan and '
  'identify infrastructure, teacher preparedness and the absence of '
  'localised content as the principal obstacles to adoption (Rahman, Khan, '
  'and Iqbal 2023). The present work addresses the third of these directly.'),
 ('h2', '2.3  Intelligent Tutoring Systems'),
 ('p',
  'An intelligent tutoring system is usually described as four components. A '
  'domain model holds what is to be learned. A student model holds what this '
  'learner currently knows. A tutoring model holds the teaching strategy. '
  "The fourth is the user interface. Anderson and colleagues' cognitive "
  'tutors, built on the ACT-R theory of cognition, remain the canonical '
  'implementation and were deployed at scale in American algebra classrooms '
  '(Anderson et al. 1995). Their student model rested on knowledge tracing, '
  'introduced by Corbett and Anderson (1994). It holds a probability that '
  'the learner has mastered each knowledge component, and updates that '
  'probability after every answer. Piech and colleagues later showed that a '
  'recurrent neural network could learn this mapping directly from '
  'interaction sequences, an approach known as deep knowledge tracing (Piech '
  'et al. 2015).'),
 ('p',
  "VanLehn's meta-analysis is the most useful single result for calibrating "
  'expectations. He compared human tutoring, intelligent tutoring systems '
  'and computer-aided instruction. Step-based tutoring systems came close to '
  'human tutors, and were considerably better than answer-based systems that '
  'only mark a final answer right or wrong (VanLehn 2011). The operative '
  'variable is granularity of feedback: systems that respond to the steps of '
  'a solution outperform systems that respond only to its conclusion.'),
 ('p',
  'This finding shaped two decisions in the present design. First, the '
  'evaluator never returns a bare score. It is told to state in one sentence '
  'what was correct and in one sentence what was missing. For mathematics it '
  'must name the exact step where the reasoning failed. Second, the '
  'session-level evaluator aggregates an attempt into named strong and weak '
  'topics rather than a single percentage, so that feedback points at '
  'content rather than at performance. What this project does not attempt is '
  'a formal student model in the knowledge-tracing sense: the mastery '
  'estimate is the empirical distribution of past scores by subject, not a '
  'Bayesian latent variable. This is a deliberate scope limitation and is '
  'revisited in Section 9.6.'),
 ('h2', '2.4  Conversational Agents in Education'),
 ('p',
  'Conversational interfaces have a long history in this domain, beginning '
  "with Weizenbaum's ELIZA, whose pattern-matching Rogerian therapist "
  'demonstrated in 1966 how readily people attribute understanding to a '
  'system that produces plausible conversational turns (Weizenbaum 1966). '
  'Adamopoulou and Moussiades trace the subsequent development from '
  'rule-based and retrieval-based designs to generative ones, and note that '
  "the field's persistent difficulty has been maintaining coherence and "
  'factual reliability across a long exchange (Adamopoulou and Moussiades '
  '2020).'),
 ('p',
  "Winkler and Söllner's state-of-the-art analysis of chatbots in education "
  'is particularly relevant because it is critical rather than promotional. '
  'Reviewing eighty studies, they report that most educational chatbots are '
  'narrow, flow-based systems. They fail as soon as a learner leaves the '
  'expected script. The studies also tend to measure satisfaction rather '
  'than learning (Winkler and Söllner 2018). Kasneci and colleagues wrote '
  'after the release of large instruction-tuned models (2023). They argue '
  'that these systems remove the brittleness problem but bring new ones: '
  'unreliable facts, reasoning that cannot be inspected, bias inherited from '
  'training data, and the risk that learners hand over their thinking '
  'instead of developing it. Baidoo-Anu and Ansah reach a similar conclusion '
  'and recommend that generative systems in education be constrained to '
  'curated content and paired with assessment that rewards process '
  '(Baidoo-Anu and Ansah 2023).'),
 ('p',
  'The design adopted here follows that recommendation. The tutor is '
  'generative, so it does not break when a student asks an unexpected '
  'question. Retrieval holds it to curated content. An assessment loop then '
  'requires the student to produce an answer before any feedback is given.'),
 ('h2', '2.5  Large Language Models and Their Limitations'),
 ('p',
  'The transformer architecture introduced by Vaswani and colleagues '
  'replaced recurrence with self-attention and made it practical to train '
  'language models at a scale previously unreachable (2017). Devlin and '
  'colleagues showed with BERT that bidirectional pre-training, followed by '
  'fine-tuning on a specific task, gave the best results then available '
  'across many language-understanding tasks (Devlin et al. 2019). Minaee and '
  'colleagues record how completely these methods replaced the earlier '
  'hand-engineered approaches to text classification (2021).'),
 ('p',
  'Brown and colleagues then demonstrated with GPT-3 that a sufficiently '
  'large autoregressive model performs many tasks from a natural-language '
  'description and a handful of examples, without any gradient update (Brown '
  'et al. 2020). This capability is called in-context learning, and it is '
  'what puts the present project within reach of a final-year team. The '
  'system gets a subject tutor, a question generator and an examiner out of '
  'one model by giving it three different prompts. No training '
  'infrastructure is needed at all. Ouyang and colleagues later showed that '
  'reinforcement learning from human feedback greatly improves how closely a '
  'model follows instructions (2022), a finding echoed in related prompting '
  'research (Wei et al. 2022). That property is exactly what this system '
  'relies on when it requires the evaluator to return a strictly formatted '
  'score line.'),
 ('p',
  'Against these capabilities stands a well-characterised failure. Ji and '
  'colleagues survey hallucination in natural language generation (2023). '
  'They define it as content that is unfaithful to the supplied source, or '
  'that no world knowledge supports. They trace its causes to both the '
  'training data and the decoding step. The GPT-4 technical report '
  'acknowledges that hallucination persists in current frontier models, '
  'though at reduced frequency (OpenAI 2023). In an educational setting the '
  'consequence is unusually severe: the reader is a novice, the output is '
  'fluent, and the whole purpose of the interaction is that the reader '
  'should commit the content to memory.'),
 ('p',
  'Two mitigations are available. Decoding can be made more conservative by '
  'lowering the sampling temperature, and the model can be given the correct '
  'material in its context window. This project uses both, with temperature '
  'values chosen per agent — 0.3 for explanation, 0.4 for question '
  'generation and 0.2 for marking — and with retrieval supplying the '
  'material.'),
 ('h2', '2.6  Retrieval-Augmented Generation'),
 ('p',
  'Lewis and colleagues introduced Retrieval-Augmented Generation as a '
  'hybrid of a parametric model and a non-parametric memory (2020). A '
  'retriever selects passages from an external index, and a generator writes '
  'its answer conditioned on them. Knowledge is then updated by changing the '
  'index rather than by retraining the model. Karpukhin and colleagues '
  'showed with Dense Passage Retrieval that a dual-encoder trained to embed '
  'questions and passages into a shared space outperforms the long-dominant '
  'sparse lexical baseline BM25 for open-domain question answering '
  '(Karpukhin et al. 2020; Robertson and Zaragoza 2009). Reimers and '
  "Gurevych's Sentence-BERT made such embeddings cheap enough to compute at "
  "scale (2019). Gao and colleagues' recent survey organises the resulting "
  'design space into naive, advanced and modular variants and identifies '
  'chunking strategy, retrieval granularity and context assembly as the '
  'principal engineering levers (Gao et al. 2024).'),
 ('p',
  'The architecture is a good fit for the present problem for four reasons '
  'that are worth stating explicitly, because they justify the central '
  'design decision of the project.'),
 ('numbers',
  ['Verifiability. Every generated answer can be traced to retrieved '
   'excerpts, which means the claim that the system answers from the board '
   'textbook is auditable rather than rhetorical.',
   'Updatability. When a board revises a textbook, the corpus is '
   're-ingested. No model is retrained and no code changes.',
   'Access control by construction. Because retrieval is filtered on '
   'metadata, curricular scoping is enforced by the query rather than '
   'requested in a prompt. A Class 9 student cannot be answered from a Class '
   '12 textbook even if the model would prefer to.',
   'Economy. A compact, inexpensive model supplied with the right two '
   'thousand words of context outperforms a far larger model supplied with '
   'none, at a fraction of the cost per request.']),
 ('fig',
  'fig_rag_flow.jpg',
  'The Retrieval-Augmented Generation request path implemented in this '
  'project. The metadata filter applied to the vector query is what makes '
  'curricular scoping a structural guarantee rather than a prompt '
  'instruction.',
  5.4),
 ('h2', '2.7  Vector Databases and Semantic Search'),
 ('p',
  'Retrieval at interactive latency requires an index structure that answers '
  'nearest-neighbour queries in high-dimensional space without exhaustive '
  "comparison. Johnson, Douze and Jégou's work on billion-scale similarity "
  'search established the practicality of GPU-accelerated approximate search '
  'and produced the FAISS library that underpins much of the field (Johnson, '
  "Douze, and Jégou 2021). Malkov and Yashunin's Hierarchical Navigable "
  'Small World graphs give logarithmic-time approximate search with high '
  'recall and are the algorithm behind most current managed vector services '
  '(Malkov and Yashunin 2020).'),
 ('p',
  'Managed services such as Pinecone package these structures behind an API '
  'and add the feature that matters most for this project: metadata '
  'filtering applied during the search rather than after it (Pinecone '
  'Systems 2024). A post-filter would first retrieve the k nearest '
  'neighbours globally and then discard those from the wrong class, '
  'frequently returning nothing. A pre-filter restricts the candidate set to '
  'vectors whose metadata matches before ranking, so the k results returned '
  "are the k best results within the student's own syllabus. This "
  'distinction is the reason the project uses a managed vector service '
  'rather than an in-process index.'),
 ('p',
  'The embedding model chosen, text-embedding-3-small, produces '
  '1,536-dimensional vectors at roughly two United States cents per million '
  'tokens. Embedding an entire board corpus is therefore a one-off cost of a '
  'few dollars. Cosine similarity is used as the distance metric, which is '
  'standard for normalised text embeddings.'),
 ('h2', '2.8  Automated Assessment of Free-Text Answers'),
 ('p',
  "Automatic grading is older than the personal computer. Page's Project "
  'Essay Grade, reported in 1966, predicted human essay scores from surface '
  'features such as word length and sentence count (1966). Burrows, Gurevych '
  'and Stein survey automatic short answer grading and divide the following '
  'half-century into five eras: concept mapping, information extraction, '
  'corpus-based methods, machine learning and evaluation (Burrows, Gurevych, '
  'and Stein 2015). They observe that until recently every approach needed a '
  'large set of human-marked answers for the specific question being graded. '
  'That requirement is fatal for the present application: the questions are '
  'generated on demand and have never been marked by anybody.'),
 ('p',
  'Instruction-tuned large language models remove the requirement. Mizumoto '
  'and Eguchi evaluated automated essay scoring with a general-purpose model '
  'and reported correlations with human raters that, while below the best '
  'purpose-built systems, were achieved with no training data at all '
  '(Mizumoto and Eguchi 2023). Board examinations ask for short, structured '
  'answers, and their marking scheme is a list of expected points rather '
  'than a judgement on the quality of the prose. That makes the task '
  'considerably easier than essay scoring.'),
 ('p',
  'The design adopted here reflects three lessons from this literature. The '
  "marking rubric is stated in the prompt in the board's own terms: one mark "
  'for a multiple-choice item, three for a short question and eight for a '
  'long question. Each score band carries its own description. The evaluator '
  'is given the retrieved textbook passage and instructed to mark against it '
  'rather than against its own knowledge. The numeric score is never trusted '
  'blindly. It is parsed from a structured response line, then clamped in '
  'application code to the maximum allowed for that question type. A model '
  'error cannot award nine marks out of three.'),
 ('h2', '2.9  Evaluating Retrieval-Augmented Systems'),
 ('p',
  'A system that retrieves before it generates has two places where it can '
  'fail, and they need separate measurement. The retriever can fetch the '
  'wrong passages, and the generator can ignore the right ones. Reporting a '
  'single end-to-end accuracy figure hides which of the two is at fault, so '
  'the literature has settled on measuring them apart. Gao and colleagues, '
  'in their survey of retrieval-augmented generation (2024), organise the '
  'field exactly this way and treat retrieval quality and generation '
  'faithfulness as distinct axes.'),
 ('p',
  'On the retrieval side the measures are inherited from classical '
  'information retrieval (Robertson and Zaragoza 2009). Precision at k asks '
  'how many of the k returned passages are relevant, and recall at k asks '
  'how many of the relevant passages were returned. Dense retrievers such as '
  'Dense Passage Retrieval (Karpukhin et al. 2020) are normally reported '
  'this way. A judgement of relevance requires either human annotation or a '
  'proxy, and for a closed corpus with known subject matter a keyword proxy '
  'is a common and defensible substitute. Similarity score alone is a weak '
  'measure, because cosine similarity is not calibrated across queries, and '
  'is best reported alongside a relevance judgement rather than in place of '
  'one (Reimers and Gurevych 2019).'),
 ('p',
  'On the generation side the property of interest is faithfulness, '
  'sometimes called groundedness: whether every claim in the answer is '
  'supported by the retrieved passages. Ji and colleagues separate '
  'faithfulness from factuality (2023). An answer can be true in general '
  'while still being unfaithful to its source. That is precisely the failure '
  'mode that matters for a tutor bound to a syllabus. Measuring faithfulness '
  'at scale by hand is impractical, so recent work uses a stronger model as '
  'an automatic judge. Mizumoto and Eguchi (2023) show that a language model '
  'scoring written work agrees usefully with human raters. They caution that '
  'the judge inherits the biases of its training, and is not a substitute '
  'for an examiner.'),
 ('p',
  'Two methodological points from this literature shape the evaluation '
  'reported in Chapter 7. The first is the need for an ablation: the '
  'contribution of retrieval can only be seen by running the same model, on '
  'the same questions, with retrieval switched off, and comparing. Without '
  'that control a groundedness score is a number without a scale. The second '
  'is that the automatic marking literature (Burrows, Gurevych, and Stein '
  '2015) reports agreement with human marks as both exact agreement and mean '
  'absolute error, not as accuracy alone. A marking error of one point on an '
  'eight-mark question is not the same thing as a wrong answer. Both '
  'conventions are adopted in this project.'),
 ('p',
  'What the literature does not supply is a benchmark for this setting. The '
  'public retrieval benchmarks are open-domain and English-language, and no '
  'dataset exists of Pakistani board questions paired with ground-truth '
  'passages from the prescribed textbooks. The evaluation in this project '
  'therefore uses a purpose-built query set and a gold set of marked '
  'answers, with the limitations of that choice stated openly in Section '
  '7.6.3.'),
 ('h2', '2.10  Document Processing for Low-Resource Educational Corpora'),
 ('p',
  'The corpus this project depends on does not exist in machine-readable '
  'form. Board textbooks, keybooks and past papers circulate as scanned PDF '
  'images. They are often of poor quality and often carry publisher '
  'watermarks. Urdu and Islamiat material adds a right-to-left script with '
  'complex ligatures. Extracting usable text is therefore an optical '
  'character recognition problem rather than a text-extraction problem.'),
 ('p',
  'Commercial cloud OCR services materially outperform open-source engines '
  'on degraded scans and on non-Latin scripts, and Google Cloud Vision was '
  'selected for this reason after preliminary trials. Its document-text '
  'detection endpoint returns a full-page transcription with layout '
  'preserved, which is sufficient for the downstream chunking step.'),
 ('p',
  'OCR output alone is not usable for retrieval. Page numbers, running '
  'headers, publisher marks, examination roll-number boxes, section '
  'instructions and recognition artefacts all become text, and because such '
  'fragments repeat across hundreds of pages they act as high-frequency '
  'noise that degrades embedding quality. The literature offers no standard '
  'recipe for this material, so a rule-based cleaning stage was developed '
  'specifically for the corpus, with a separate and more aggressive rule set '
  'for past papers than for textbooks. The chunking strategy follows the '
  "recommendation in Gao and colleagues' survey: a moderate chunk size with "
  'overlap (2024). Here that is about 2,800 characters with a 400-character '
  'overlap, breaking at a sentence or line boundary wherever possible.'),
 ('fig',
  'fig_ingestion.png',
  'The four-stage offline ingestion pipeline that converts scanned board '
  'material into a filtered, metadata-tagged vector index.',
  6.2),
 ('h2', '2.11  The Educational Technology Landscape in Pakistan'),
 ('p',
  'A student of class nine to twelve in Pakistan has access to several '
  'categories of digital study support, none of which combines '
  'board-specific grounding with generative tutoring and automatic marking.'),
 ('bullets',
  [['Video lecture platforms. ',
    'Sabaq Foundation and Taleemabad provide free, curriculum-mapped video '
    'lessons and are the most widely used domestic offerings. They are '
    'strong on explanation and weak on interaction: a student cannot ask a '
    'question, cannot generate a practice paper and cannot have an answer '
    'marked.'],
   ['Past-paper repositories. ',
    'Sites such as ilmkidunya and a large number of smaller portals host '
    'board past papers and guess papers. They solve the availability problem '
    'and nothing else; the material is unstructured, of uncertain provenance '
    'and heavily advertisement-laden.'],
   ['Test-preparation platforms. ',
    'Nearpeer and comparable services target entry-test preparation with '
    'recorded courses and question banks. Coverage of the board syllabus '
    'proper is incidental, and the model is paid.'],
   ['Global open courseware. ',
    'Khan Academy provides high-quality instruction and an Urdu '
    'localisation, but its scope and sequence follow an American curriculum. '
    'It cannot tell a Federal Board Class 11 student what their board asks.'],
   ['General-purpose assistants. ',
    'ChatGPT and similar systems are conversational, always available and '
    'free at the entry tier. They are also board-agnostic, unable to cite '
    'the prescribed textbook and subject to the hallucination risk discussed '
    'in Section 2.5.'],
   ['Single-purpose solvers. ',
    'Photomath and comparable applications solve a photographed mathematics '
    'problem step by step. They are excellent within a narrow domain and do '
    'not address conceptual explanation, question generation or '
    'non-mathematical subjects.']]),
 ('h2', '2.12  Comparative Analysis'),
 ('p',
  'Table 2.1 compares the platforms discussed above against the capabilities '
  'this project treats as essential. The comparison is drawn from the '
  'publicly documented feature sets of each platform at the time of '
  'writing.'),
 ('table',
  'Comparison of existing platforms against the capability set targeted by '
  'this project',
  ['Capability',
   'Sabaq / Taleemabad',
   'Past-paper portals',
   'Nearpeer',
   'Khan Academy',
   'ChatGPT',
   'Eternal Sunshine'],
  [['Aligned to a named Pakistani board',
    'Partial',
    'Yes',
    'Partial',
    'No',
    'No',
    'Yes'],
   ['Class- and subject-scoped content filter',
    'Yes',
    'Partial',
    'Yes',
    'Yes',
    'No',
    'Yes'],
   ['Conversational concept explanation',
    'No',
    'No',
    'No',
    'No',
    'Yes',
    'Yes'],
   ['Answers grounded in the prescribed textbook',
    'n/a',
    'n/a',
    'n/a',
    'No',
    'No',
    'Yes'],
   ['Auto-generated practice questions',
    'No',
    'No',
    'Partial',
    'Partial',
    'Yes',
    'Yes'],
   ['Questions labelled by past-paper provenance',
    'No',
    'No',
    'No',
    'No',
    'No',
    'Yes'],
   ['Automatic marking of free-text answers',
    'No',
    'No',
    'No',
    'No',
    'Partial',
    'Yes'],
   ['Board marking scheme (1 / 3 / 8 marks)',
    'No',
    'No',
    'No',
    'No',
    'No',
    'Yes'],
   ['Weak-topic identification per session',
    'No',
    'No',
    'Partial',
    'Yes',
    'No',
    'Yes'],
   ['Downloadable past papers and textbooks',
    'Partial',
    'Yes',
    'No',
    'No',
    'No',
    'Yes'],
   ['Urdu-language support', 'Yes', 'Yes', 'Partial', 'Yes', 'Yes', 'Yes'],
   ['Free to the student', 'Yes', 'Yes', 'No', 'Yes', 'Partial', 'Yes']],
  [1.9, 0.85, 0.75, 0.6, 0.7, 0.6, 0.75],
  8.5),
 ('p',
  'Two observations follow from the table. First, no existing platform '
  'occupies the intersection of board-specific grounding and generative '
  'interaction: the products that know the board cannot converse, and the '
  'products that can converse do not know the board. Second, three '
  'capabilities appear in the final column alone — grounding answers in the '
  'prescribed textbook, labelling generated questions by past-paper '
  "provenance, and marking free-text answers against the board's own marking "
  'scheme. These three constitute the novel contribution of the work.'),
 ('h2', '2.13  Summary of the Reviewed Literature'),
 ('p',
  'Table 2.2 summarises the principal works reviewed in this chapter, '
  'grouped by the theme they inform, and records what each contributes to '
  'the design of this project. The table is not a complete bibliography; the '
  'full list of fifty-two sources appears in the references.'),
 ('table',
  'Principal reviewed literature and its bearing on this project',
  ['Theme', 'Key sources', 'What it contributes here'],
  [['Artificial intelligence in education',
    'Holmes et al. (2019); Luckin et al. (2016); UNESCO (2021); '
    'Zawacki-Richter et al. (2019)',
    'Establishes the field and its evidence base, and warns that educational '
    'tools are often built without educators, which is why this project '
    'began with a student survey.'],
   ['Intelligent tutoring systems',
    'Bloom (1984); VanLehn (2011); Anderson et al. (1995); Corbett and '
    'Anderson (1994); Piech et al. (2015)',
    'Bloom sets the two-sigma benchmark that motivates one-to-one tutoring; '
    'VanLehn identifies step-level feedback as the active ingredient, which '
    'the evaluator agent implements.'],
   ['Conversational agents',
    'Weizenbaum (1966); Adamopoulou and Moussiades (2020); Winkler and '
    'Söllner (2018)',
    'Establishes the chat interface as the expected interaction model and '
    'documents where earlier rule-based agents failed.'],
   ['Large language models and their limits',
    'Vaswani et al. (2017); Devlin et al. (2019); Brown et al. (2020); '
    'Ouyang et al. (2022); Wei et al. (2022); Ji et al. (2023)',
    'Explains the capability the project builds on and the hallucination '
    'failure mode that retrieval is introduced to contain.'],
   ['Retrieval-augmented generation',
    'Lewis et al. (2020); Gao et al. (2024); Karpukhin et al. (2020)',
    'Supplies the core architectural pattern and the separation of retrieval '
    'quality from generation faithfulness.'],
   ['Vector search',
    'Reimers and Gurevych (2019); Johnson et al. (2021); Malkov and Yashunin '
    '(2020); Robertson and Zaragoza (2009); Pinecone (2024)',
    'Justifies dense embeddings over keyword search and identifies metadata '
    'pre-filtering as the mechanism that makes board scoping structural.'],
   ['Automatic marking of free text',
    'Page (1966); Burrows et al. (2015); Mizumoto and Eguchi (2023)',
    'Supplies the marking measures used in Chapter 8 and the evidence that a '
    'language model can mark written answers usefully.'],
   ['Document processing',
    'Google Cloud Vision (2024); Minaee et al. (2021)',
    'Informs the optical character recognition and cleaning stages of the '
    'ingestion pipeline.'],
   ['Educational technology in Pakistan',
    'Ministry of Federal Education (2022); FBISE (Federal Board of '
    'Intermediate and Secondary Education 2024); Rahman et al. (2023); Nye '
    '(2015)',
    'Documents the board-centred structure of the curriculum and the absence '
    'of board-specific digital provision.'],
   ['Engineering practice',
    'Fowler (2003); Sommerville (2016); Beck et al. (2001); Schwaber and '
    'Sutherland (2020); IEEE 830 (1998); OWASP (2021)',
    'Supplies the architectural patterns, the Agile process and the '
    'requirements and security standards followed.']],
  [1.25, 1.95, 2.25],
  9),
 ('h2', '2.14  Research Gap and Positioning'),
 ('p',
  'The literature and the market together define the gap this project '
  'addresses. The pedagogical case for individualised tutoring is settled '
  'and large (Bloom 1984; VanLehn 2011). The technology for a plausible '
  'conversational tutor now exists and is inexpensive (Brown et al. 2020; '
  'Ouyang et al. 2022). Its central defect in an educational context — '
  'unverifiable, occasionally false output — has a known architectural '
  'remedy in Retrieval-Augmented Generation (Lewis et al. 2020; Gao et al. '
  '2024). Automatic marking of short structured answers, historically '
  'blocked by the need for question-specific training data, is now '
  'achievable from a rubric stated in a prompt (Burrows, Gurevych, and Stein '
  '2015; Mizumoto and Eguchi 2023). Every ingredient is available.'),
 ('p',
  'What is missing is the assembly of those ingredients around a specific, '
  'under-served curriculum. No published system, and no product available to '
  'a Pakistani secondary student, grounds a generative tutor in the '
  'textbooks and past papers of a named Pakistani examination board, '
  "generates practice questions in that board's style with an indication of "
  "past-paper provenance, and marks free-text answers against that board's "
  'marking scheme — while also containing and measuring the operating cost '
  'sufficiently well that the service could plausibly be offered free.'),
 ('p',
  'This project therefore positions itself not as a contribution to the '
  'machine learning literature but as a contribution in applied software '
  'engineering: the design, implementation, verification and cost '
  'characterisation of a retrieval-grounded, multi-agent educational system '
  'for a low-resource national curriculum. The technical claims made in '
  'later chapters are correspondingly engineering claims — about '
  'architecture, correctness, latency and cost — rather than claims about '
  'model capability.'),
 ('h2', '2.15  Summary'),
 ('p',
  'Individual tutoring produces very large learning gains but is '
  'unaffordable at scale; this is the problem educational technology has '
  'pursued for four decades. Intelligent tutoring systems recovered part of '
  'the effect, and the literature identifies step-level rather than '
  'answer-level feedback as the mechanism. Conversational agents were '
  'historically too brittle to sustain an educational dialogue; large '
  'language models remove the brittleness but introduce factual '
  'unreliability. Retrieval-Augmented Generation, supported by modern vector '
  'search with metadata pre-filtering, converts that unreliability into a '
  'manageable engineering property by supplying the model with authoritative '
  'material at inference time. Automatic marking of short answers is now '
  'possible from a stated rubric. The material required to ground such a '
  'system for Pakistani board students exists only as scanned documents and '
  'must be processed through OCR and domain-specific cleaning before it can '
  'be indexed. No available platform combines these capabilities. The '
  'following chapter converts this position into a validated requirement '
  'set.')]
