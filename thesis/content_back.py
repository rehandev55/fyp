"""Content blocks for the back matter - references and appendices."""

BLOCKS = [('h1', 'REFERENCES', 'R'),
 ('p',
  'References are given in Chicago author-date style, as the project report '
  'template requires. Works are cited in the text by author and year, and '
  'are listed below alphabetically by the first author’s surname.'),
 ('refs',
  [[('Adamopoulou, E., and L. Moussiades. 2020. “Chatbots: History, '
     'Technology, and Applications.” ',
     False),
    ('Machine Learning with Applications', True),
    (' 2: 1–15.', False)],
   [('Anderson, J. R., A. T. Corbett, K. R. Koedinger, and R. Pelletier. '
     '1995. “Cognitive Tutors: Lessons Learned.” ',
     False),
    ('Journal of the Learning Sciences', True),
    (' 4 (2): 167–207.', False)],
   [('Baidoo-Anu, D., and L. O. Ansah. 2023. “Education in the Era of '
     'Generative Artificial Intelligence (AI): Understanding the Potential '
     'Benefits of ChatGPT in Promoting Teaching and Learning.” ',
     False),
    ('Journal of AI', True),
    (' 7 (1): 52–62.', False)],
   [('Beck, K., et al. 2001. “Manifesto for Agile Software Development.” '
     'Accessed April 9, 2026. https://agilemanifesto.org.',
     False)],
   [('Bloom, B. S. 1984. “The 2 Sigma Problem: The Search for Methods of '
     'Group Instruction as Effective as One-to-One Tutoring.” ',
     False),
    ('Educational Researcher', True),
    (' 13 (6): 4–16.', False)],
   [('Brown, T. B., et al. 2020. “Language Models Are Few-Shot Learners.” '
     'In ',
     False),
    ('Advances in Neural Information Processing Systems', True),
    (' 33: 1877–1901.', False)],
   [('Burrows, S., I. Gurevych, and B. Stein. 2015. “The Eras and Trends of '
     'Automatic Short Answer Grading.” ',
     False),
    ('International Journal of Artificial Intelligence in Education', True),
    (' 25 (1): 60–117.', False)],
   [('Corbett, A. T., and J. R. Anderson. 1994. “Knowledge Tracing: Modeling '
     'the Acquisition of Procedural Knowledge.” ',
     False),
    ('User Modeling and User-Adapted Interaction', True),
    (' 4 (4): 253–78.', False)],
   [('Devlin, J., M.-W. Chang, K. Lee, and K. Toutanova. 2019. “BERT: '
     'Pre-training of Deep Bidirectional Transformers for Language '
     'Understanding.” In ',
     False),
    ('Proceedings of NAACL-HLT', True),
    (', 4171–86.', False)],
   [('Federal Board of Intermediate and Secondary Education. 2024. “Model '
     'Papers and Scheme of Studies for SSC and HSSC.” Accessed April 12, '
     '2026. https://www.fbise.edu.pk.',
     False)],
   [('Fowler, M. 2003. ', False),
    ('Patterns of Enterprise Application Architecture', True),
    ('. Boston, MA: Addison-Wesley.', False)],
   [('Gao, Y., et al. 2024. “Retrieval-Augmented Generation for Large '
     'Language Models: A Survey.” arXiv preprint arXiv:2312.10997.',
     False)],
   [('Google Cloud. 2024. “Cloud Vision API Documentation: Document Text '
     'Detection.” Accessed April 22, 2026. '
     'https://cloud.google.com/vision/docs.',
     False)],
   [('Holmes, A., M. Bialik, and C. Fadel. 2019. ', False),
    ('Artificial Intelligence in Education: Promises and Implications for '
     'Teaching and Learning',
     True),
    ('. Boston, MA: Center for Curriculum Redesign.', False)],
   [('Hugging Face. 2024. “Transformers: State-of-the-Art Natural Language '
     'Processing.” Accessed April 20, 2026. '
     'https://huggingface.co/docs/transformers.',
     False)],
   [('IEEE. 1998. ', False),
    ('IEEE Recommended Practice for Software Requirements Specifications',
     True),
    ('. IEEE Std 830-1998. New York: IEEE.', False)],
   [('Inertia.js. 2025. “Inertia.js Documentation.” Accessed September 1, '
     '2026. https://inertiajs.com.',
     False)],
   [('Ji, Z., et al. 2023. “Survey of Hallucination in Natural Language '
     'Generation.” ',
     False),
    ('ACM Computing Surveys', True),
    (' 55 (12): 1–38.', False)],
   [('Johnson, J., M. Douze, and H. Jégou. 2021. “Billion-Scale Similarity '
     'Search with GPUs.” ',
     False),
    ('IEEE Transactions on Big Data', True),
    (' 7 (3): 535–47.', False)],
   [('Karpukhin, V., et al. 2020. “Dense Passage Retrieval for Open-Domain '
     'Question Answering.” In ',
     False),
    ('Proceedings of EMNLP', True),
    (', 6769–81.', False)],
   [('Kasneci, E., et al. 2023. “ChatGPT for Good? On Opportunities and '
     'Challenges of Large Language Models for Education.” ',
     False),
    ('Learning and Individual Differences', True),
    (' 103.', False)],
   [('Laravel. 2025. “Laravel Documentation.” Accessed September 1, 2026. '
     'https://laravel.com/docs.',
     False)],
   [('Lewis, P., et al. 2020. “Retrieval-Augmented Generation for '
     'Knowledge-Intensive NLP Tasks.” In ',
     False),
    ('Advances in Neural Information Processing Systems', True),
    (' 33: 9459–74.', False)],
   [('Luckin, R., W. Holmes, M. Griffiths, and L. B. Forcier. 2016. ', False),
    ('Intelligence Unleashed: An Argument for AI in Education', True),
    ('. London: Pearson.', False)],
   [('Malkov, Y. A., and D. A. Yashunin. 2020. “Efficient and Robust '
     'Approximate Nearest Neighbor Search Using Hierarchical Navigable Small '
     'World Graphs.” ',
     False),
    ('IEEE Transactions on Pattern Analysis and Machine Intelligence', True),
    (' 42 (4): 824–36.', False)],
   [('Meta Open Source. 2025. “React Documentation.” Accessed September 1, '
     '2026. https://react.dev.',
     False)],
   [('Minaee, S., N. Kalchbrenner, E. Cambria, N. Nikzad, M. Chenaghlu, and '
     'J. Gao. 2021. “Deep Learning Based Text Classification: A '
     'Comprehensive Review.” ',
     False),
    ('ACM Computing Surveys', True),
    (' 54 (3): 1–40.', False)],
   [('Ministry of Federal Education and Professional Training. 2022. ',
     False),
    ('National Curriculum of Pakistan', True),
    ('. Islamabad: Government of Pakistan.', False)],
   [('Mizumoto, A., and M. Eguchi. 2023. “Exploring the Potential of Using '
     'an AI Language Model for Automated Essay Scoring.” ',
     False),
    ('Research Methods in Applied Linguistics', True),
    (' 2 (2).', False)],
   [('Nye, B. D. 2015. “Intelligent Tutoring Systems by and for the '
     'Developing World: A Review of Trends and Approaches for Educational '
     'Technology in a Global Context.” ',
     False),
    ('International Journal of Artificial Intelligence in Education', True),
    (' 25 (2): 177–203.', False)],
   [('OpenAI. 2023. “GPT-4 Technical Report.” Accessed March 2, 2026. '
     'https://openai.com/research/gpt-4.',
     False)],
   [('OpenAI. 2024. “GPT-4o Mini: Advancing Cost-Efficient Intelligence.” '
     'Accessed April 18, 2026. '
     'https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence.',
     False)],
   [('OpenAI. 2025. “Pricing: Models and Rates.” Accessed September 10, '
     '2026. https://openai.com/api/pricing.',
     False)],
   [('Ouyang, L., et al. 2022. “Training Language Models to Follow '
     'Instructions with Human Feedback.” In ',
     False),
    ('Advances in Neural Information Processing Systems', True),
    (' 35: 27730–44.', False)],
   [('OWASP Foundation. 2021. “OWASP Top Ten Web Application Security '
     'Risks.” Accessed May 4, 2026. https://owasp.org/Top10.',
     False)],
   [('Page, E. B. 1966. “The Imminence of Grading Essays by Computer.” ',
     False),
    ('Phi Delta Kappan', True),
    (' 47 (5): 238–43.', False)],
   [('Pardos, Z. A., and N. T. Heffernan. 2020. “Using Artificial '
     'Intelligence to Improve Education.” ',
     False),
    ('IEEE Intelligent Systems', True),
    (' 35 (5): 6–10.', False)],
   [('Piech, C., et al. 2015. “Deep Knowledge Tracing.” In ', False),
    ('Advances in Neural Information Processing Systems', True),
    (' 28: 505–13.', False)],
   [('Pinecone Systems Inc. 2024. “Pinecone Documentation: Metadata '
     'Filtering and Serverless Indexes.” Accessed April 18, 2026. '
     'https://docs.pinecone.io.',
     False)],
   [('Rahman, A., S. Khan, and M. Iqbal. 2023. “Artificial Intelligence in '
     'the Pakistani Education System: Opportunities and Challenges.” ',
     False),
    ('Pakistan Journal of Educational Research', True),
    (' 6 (2): 45–58.', False)],
   [('Ramírez, S. 2025. “FastAPI Documentation.” Accessed September 1, 2026. '
     'https://fastapi.tiangolo.com.',
     False)],
   [('Reimers, N., and I. Gurevych. 2019. “Sentence-BERT: Sentence '
     'Embeddings Using Siamese BERT-Networks.” In ',
     False),
    ('Proceedings of EMNLP-IJCNLP', True),
    (', 3982–92.', False)],
   [('Robertson, S., and H. Zaragoza. 2009. “The Probabilistic Relevance '
     'Framework: BM25 and Beyond.” ',
     False),
    ('Foundations and Trends in Information Retrieval', True),
    (' 3 (4): 333–89.', False)],
   [('Schwaber, K., and J. Sutherland. 2020. “The Scrum Guide: The '
     'Definitive Guide to Scrum — The Rules of the Game.” Accessed April 9, '
     '2026. https://scrumguides.org.',
     False)],
   [('Sommerville, I. 2016. ', False),
    ('Software Engineering', True),
    ('. 10th ed. Harlow, UK: Pearson.', False)],
   [('UNESCO. 2021. ', False),
    ('Artificial Intelligence in Education: Guidance for Policy-Makers',
     True),
    ('. Paris: UNESCO.', False)],
   [('VanLehn, K. 2011. “The Relative Effectiveness of Human Tutoring, '
     'Intelligent Tutoring Systems, and Other Tutoring Systems.” ',
     False),
    ('Educational Psychologist', True),
    (' 46 (4): 197–221.', False)],
   [('Vaswani, A., et al. 2017. “Attention Is All You Need.” In ', False),
    ('Advances in Neural Information Processing Systems', True),
    (' 30: 5998–6008.', False)],
   [('Wei, J., et al. 2022. “Chain-of-Thought Prompting Elicits Reasoning in '
     'Large Language Models.” In ',
     False),
    ('Advances in Neural Information Processing Systems', True),
    (' 35: 24824–37.', False)],
   [('Weizenbaum, J. 1966. “ELIZA: A Computer Program for the Study of '
     'Natural Language Communication between Man and Machine.” ',
     False),
    ('Communications of the ACM', True),
    (' 9 (1): 36–45.', False)],
   [('Winkler, R., and M. Söllner. 2018. “Unleashing the Potential of '
     'Chatbots in Education: A State-of-the-Art Analysis.” In ',
     False),
    ('Proceedings of the Academy of Management Annual Meeting', True),
    (' 2018 (1): 1–6.', False)],
   [('Zawacki-Richter, O., V. I. Marín, M. Bond, and F. Gouverneur. 2019. '
     '“Systematic Review of Research on Artificial Intelligence Applications '
     'in Higher Education: Where Are the Educators?” ',
     False),
    ('International Journal of Educational Technology in Higher Education',
     True),
    (' 16 (39): 1–27.', False)]]),
 ('h1', 'APPENDIX A:  GLOSSARY', 'A'),
 ('table',
  'Glossary of technical terms used in this report',
  ['Term', 'Meaning'],
  [['Agent',
    'In this report, a distinct behaviour obtained from a shared language '
    'model by supplying a dedicated prompt, temperature and token budget. '
    'The system has four: teacher, tester, evaluator and session evaluator.'],
   ['Board',
    'A provincial or federal examination authority that prescribes a '
    'syllabus, publishes textbooks and sets papers. This project models the '
    'Federal and AJK boards; the corpus delivered with it covers the Federal '
    'Board.'],
   ['Chunk',
    'A contiguous segment of a source document, approximately 2,800 '
    'characters with 400 characters of overlap with its neighbours, which is '
    'the unit of embedding and retrieval.'],
   ['Clamping',
    'Constraining a numeric value returned by the language model to the '
    'range permitted by the marking scheme, performed in application code.'],
   ['Cosine similarity',
    'The measure of closeness between two embedding vectors used to rank '
    'retrieved chunks; 1.0 is identical direction and 0.0 is orthogonal.'],
   ['Embedding',
    'A fixed-length numeric vector representing the meaning of a passage of '
    'text. This project uses 1,536-dimensional vectors.'],
   ['Grounding',
    'Supplying a language model with authoritative source material in its '
    'context so that its output can be traced to that material.'],
   ['Hallucination',
    'The generation of fluent output that is unfaithful to the supplied '
    'source or unsupported by fact.'],
   ['Idempotence',
    'The property that re-running an operation produces the same result and '
    'repeats no work; every ingestion stage in this project is idempotent.'],
   ['Inertia.js',
    'A library that delivers single-page-application navigation while '
    'keeping routing and page data on the server.'],
   ['Metadata pre-filter',
    'A constraint applied during a vector search rather than to its results, '
    'so that only vectors whose metadata matches are candidates for '
    'ranking.'],
   ['Provenance label',
    'A marker on a generated question indicating whether it is drawn from a '
    'past paper (⭐), modelled on past-paper style (~) or newly written from '
    'the textbook (★).'],
   ['Retrieval-Augmented Generation',
    'An architecture in which relevant passages are retrieved from an '
    'external index and supplied to a generative model before it answers.'],
   ['Rolling summary',
    'A short, continuously updated description of a conversation that '
    'replaces older turns in the prompt, bounding prompt growth.'],
   ['Similarity floor',
    'The minimum cosine score, 0.20 in this system, below which a retrieved '
    'chunk is discarded as irrelevant.'],
   ['Temperature',
    'A decoding parameter controlling randomness; lower values produce more '
    'deterministic output.'],
   ['Token',
    'The unit in which language-model input and output are measured and '
    'billed; approximately four characters of English text.'],
   ['Vector database',
    'A store optimised for approximate nearest-neighbour search over '
    'high-dimensional embeddings.'],
   ['Wayfinder',
    'A Laravel package that generates TypeScript functions from server '
    'routes so that route usage is checked at compile time.']],
  [1.55, 4.4],
  10),
 ('h1', 'APPENDIX B:  REQUIREMENT ELICITATION SURVEY', 'B'),
 ('p',
  'The instrument below was published as an online form and answered by '
  'students of classes nine to twelve. Forty-eight complete responses were '
  'received. Nine questions were closed and five were open. The results are '
  'analysed in Section 3.4 and traced to individual requirements in Table '
  '3.2. Percentages are given to one decimal place and are calculated over '
  'the number of respondents who answered that particular question, which is '
  'stated wherever it is not forty-eight.'),
 ('h2', 'B.1  The instrument'),
 ('table',
  'Survey instrument as administered',
  ['No.', 'Question', 'Response type'],
  [['Q1', 'Which class are you in?', 'Class 9 / 10 / 11 / 12'],
   ['Q2', 'What is your favourite subject?', 'Free text'],
   ['Q3',
    'Where do you study the most?',
    'At school / at home / at tuition / all of these'],
   ['Q4',
    'When you do not understand a topic, what do you usually do?',
    'Multiple selection'],
   ['Q5',
    'Do you use any online study apps or websites? If yes, which ones?',
    'Free text'],
   ['Q6', 'Do you use ChatGPT?', 'Yes / No'],
   ['Q7',
    'If you use ChatGPT, what problems do you face while using it for '
    'learning?',
    'Free text'],
   ['Q8',
    'What do you need more help with?',
    'Understanding concepts / practising questions / both / not sure'],
   ['Q9',
    'Would it help you if an app gave questions and explanations based on '
    'your board syllabus?',
    'Yes / No / Maybe'],
   ['Q10',
    'If a chatbot takes your test, shows your mistakes and explains the '
    'correct answer, will that help you learn better?',
    'Yes / No / Maybe'],
   ['Q11', 'What features should a good learning app have?', 'Free text'],
   ['Q12',
    'What is the biggest difficulty you face while studying?',
    'Free text'],
   ['Q13',
    'Do you download past papers or textbooks from the internet?',
    'Yes and easy to find / yes but hard to find / no'],
   ['Q14',
    'Do you feel there is a difference between board exam content and online '
    'study material?',
    'Yes / No / Sometimes']],
  [0.5, 3.35, 1.55],
  9),
 ('h2', 'B.2  Results of the closed questions'),
 ('table',
  'Q1. Which class are you in? (n = 48)',
  ['Response', 'Count', 'Share'],
  [['Class 9', '6', '12.5 %'],
   ['Class 10', '7', '14.6 %'],
   ['Class 11', '17', '35.4 %'],
   ['Class 12', '18', '37.5 %']],
  [3.0, 1.2, 1.2],
  10),
 ('table',
  'Q3. Where do you study the most? (n = 48)',
  ['Response', 'Count', 'Share'],
  [['At home', '22', '45.8 %'],
   ['At school', '20', '41.7 %'],
   ['At tuition', '3', '6.2 %'],
   ['All of these', '3', '6.2 %']],
  [3.0, 1.2, 1.2],
  10),
 ('table',
  'Q4. When you do not understand a topic, what do you usually do? (n = 47, '
  'more than one answer allowed)',
  ['Response', 'Count', 'Share of respondents'],
  [['Watch YouTube', '17', '36.2 %'],
   ['ChatGPT', '16', '34.0 %'],
   ['Google it', '15', '31.9 %'],
   ['Ask teacher', '11', '23.4 %'],
   ['Ask friend or classmate', '5', '10.6 %'],
   ['Use notes or books', '5', '10.6 %']],
  [3.0, 1.2, 1.2],
  10),
 ('table',
  'Q6. Do you use ChatGPT? (n = 48)',
  ['Response', 'Count', 'Share'],
  [['Yes', '36', '75.0 %'], ['No', '12', '25.0 %']],
  [3.0, 1.2, 1.2],
  10),
 ('table',
  'Q8. What do you need more help with? (n = 48)',
  ['Response', 'Count', 'Share'],
  [['Understanding concepts', '25', '52.1 %'],
   ['Both', '18', '37.5 %'],
   ['Practising questions', '3', '6.2 %'],
   ['Not sure', '2', '4.2 %']],
  [3.0, 1.2, 1.2],
  10),
 ('table',
  'Q9. Would an app based on your board syllabus help you? (n = 48)',
  ['Response', 'Count', 'Share'],
  [['Yes', '38', '79.2 %'], ['Maybe', '8', '16.7 %'], ['No', '2', '4.2 %']],
  [3.0, 1.2, 1.2],
  10),
 ('table',
  'Q10. Would a chatbot that tests, marks and explains help you learn '
  'better? (n = 48)',
  ['Response', 'Count', 'Share'],
  [['Yes', '38', '79.2 %'], ['Maybe', '7', '14.6 %'], ['No', '3', '6.2 %']],
  [3.0, 1.2, 1.2],
  10),
 ('table',
  'Q13. Do you download past papers or textbooks from the internet? (n = 48)',
  ['Response', 'Count', 'Share'],
  [['Yes, but they are difficult to find', '25', '52.1 %'],
   ['No, I do not download them', '16', '33.3 %'],
   ['Yes, and they are easy to find', '7', '14.6 %']],
  [3.0, 1.2, 1.2],
  10),
 ('table',
  'Q14. Is there a difference between board exam content and online study '
  'material? (n = 48)',
  ['Response', 'Count', 'Share'],
  [['Yes', '24', '50.0 %'],
   ['Sometimes', '14', '29.2 %'],
   ['No', '10', '20.8 %']],
  [3.0, 1.2, 1.2],
  10),
 ('h2', 'B.3  Coding of the open questions'),
 ('p',
  'The five open questions were coded into themes. A single answer could '
  'carry more than one theme, so the theme counts below sum to more than the '
  'number of respondents. The coding rules are held in code, in '
  'thesis/survey_data.py, so that the counts quoted in Chapter 3 can be '
  're-derived from the raw answers rather than taken on trust.'),
 ('table',
  'Q7. Problems reported with ChatGPT (26 of 45 respondents reported a '
  'problem; 19 reported none)',
  ['Theme', 'Mentions'],
  [['Answers too long or padded', '11'],
   ['Wording too difficult or too advanced', '7'],
   ['Wrong, vague or irrelevant answers', '7'],
   ['Does not understand the question', '3'],
   ['Model or data limits', '3'],
   ['Weak on numericals and maths', '2'],
   ['No diagrams', '1']],
  [4.0, 1.4],
  10),
 ('table',
  'Q11. Features asked for in a learning application (n = 48)',
  ['Theme', 'Mentions'],
  [['Past papers', '11'],
   ['Simple wording and to-the-point answers', '10'],
   ['Keybooks and textbooks', '8'],
   ['Chapter videos', '6'],
   ['Quizzes and MCQs', '4'],
   ['Voice answers', '4'],
   ['AI chatbot', '3'],
   ['Correct and accurate answers', '3'],
   ['Syllabus-aligned content', '2'],
   ['Free to use', '2'],
   ['Urdu option', '1']],
  [4.0, 1.4],
  10),
 ('table',
  'Q12. Biggest difficulty faced while studying (n = 46)',
  ['Theme', 'Mentions'],
  [['Understanding concepts', '14'],
   ['Time management', '11'],
   ['Long syllabus', '8'],
   ['Focus and distraction', '4'],
   ['Finding study material', '4'],
   ['No guidance', '3']],
  [4.0, 1.4],
  10),
 ('table',
  'Q5. Use of online study tools, grouped (n = 48)',
  ['Group', 'Count', 'Share'],
  [['Uses ChatGPT or a chatbot', '14', '29.2 %'],
   ['Uses no online tool', '26', '54.2 %'],
   ['Uses some other tool', '8', '16.7 %']],
  [3.0, 1.2, 1.2],
  10),
 ('h2', 'B.4  Charts of the principal results'),
 ('fig', 'fig_survey_class.png', 'Class of respondents.', 4.9),
 ('fig', 'fig_survey_location.png', 'Where respondents study most.', 4.9),
 ('fig',
  'fig_survey_stuck.png',
  'What students do when a topic is unclear.',
  5.2),
 ('fig', 'fig_survey_tools.png', 'Use of online study tools.', 4.9),
 ('fig',
  'fig_survey_chatgpt_problems.png',
  'Problems reported with general-purpose assistants.',
  5.2),
 ('fig', 'fig_survey_help.png', 'What students need more help with.', 4.9),
 ('fig',
  'fig_survey_difficulty.png',
  'Biggest difficulty reported while studying.',
  5.2),
 ('fig',
  'fig_survey_boardapp.png',
  'Value of an application tied to the board syllabus.',
  4.9),
 ('fig',
  'fig_survey_chatbot_test.png',
  'Value of a chatbot that tests, marks and explains.',
  4.9),
 ('fig',
  'fig_survey_downloads.png',
  'Ease of finding past papers and textbooks online.',
  4.9),
 ('fig',
  'fig_survey_boardvsonline.png',
  'Mismatch between board content and online material.',
  4.9),
 ('fig',
  'fig_survey_features.png',
  'Features asked for in a learning application.',
  5.2),
 ('h2', 'B.5  Limitations of the survey'),
 ('p',
  'Three limitations should be kept in mind when reading these results. The '
  'sample of forty-eight is a convenience sample of students the team could '
  'reach, so it is not a random sample of Pakistani school students and the '
  'percentages carry no claim of national representativeness. Class 11 and '
  'Class 12 supply 72.9 per cent of the responses, so the views of Class 9 '
  'and Class 10 students are under-represented. Finally, the questions on '
  'the value of a board-syllabus application and of a marking chatbot '
  'describe products that did not yet exist, and stated interest in a '
  'hypothetical product is weaker evidence than observed behaviour. The '
  'behavioural questions ask where students study, what they do when stuck, '
  'and what they already use. Those should carry more weight in the analysis '
  'than the two questions about a proposed product, even though the '
  'proposed-product questions produced the largest majorities.'),
 ('h1', 'APPENDIX C:  SELECTED CODE LISTINGS', 'C'),
 ('p',
  'The listings below complement those given in Chapter 6. They are '
  'reproduced from the delivered codebase.'),
 ('h2', 'C.1  Prompt template — teacher agent'),
 ('code',
  'The teacher agent prompt template (abridged)',
  'You are an AI tutor for Pakistani students.\n'
  'Class: {class_level} | Board: {board} | Subject: {subject}\n'
  '\n'
  'RULES:\n'
  '- Prefer using the provided textbook/keybook content as the primary '
  'source.\n'
  '- If the exact topic is NOT available in the textbook/keybook, you MAY '
  'answer using\n'
  '  general knowledge for basic conceptual understanding.\n'
  '- When using general knowledge, clearly mention:\n'
  '  "This explanation is not directly available in your {class_level} '
  '{subject}\n'
  '   textbook, but here is a simple general explanation."\n'
  '- Never invent textbook references or page numbers.\n'
  '- Never say "no response".\n'
  '- Use simple, student-friendly words.\n'
  '- Keep answers concise, clear, and exam-focused.\n'
  '- Language: reply in the same language the student used (English or '
  'Urdu).\n'
  '\n'
  'FORMAT (adapt based on question type):\n'
  '- "What is / Define"      -> Definition + explanation + key points + '
  'example\n'
  '- "Explain / How / Why"   -> Direct paragraph explanation\n'
  '- "Difference / Compare"  -> X: ... | Y: ... | Key difference: ...\n'
  '- "Name / List / Give"    -> Numbered list\n'
  '- "Function of / Purpose" -> 2-3 sentences\n'
  '\n'
  'MATHS ONLY:\n'
  'Given: | To Find: | Method: [from textbook]\n'
  'Step 1: [rule/formula used]\n'
  'Step 2: ...\n'
  'Answer: [with units]\n'
  '\n'
  'CONTENT:\n'
  '{context}\n'
  '\n'
  'Question: {question}\n'
  '\n'
  'Answer:',
  'ai-service/prompts/teacher.txt'),
 ('h2', 'C.2  Prompt template — evaluator'),
 ('code',
  'The evaluator prompt template (abridged)',
  'You are an exam evaluator for Pakistani students.\n'
  'Class: {class_level} | Board: {board} | Subject: {subject}\n'
  '\n'
  'Evaluate the student answer based ONLY on the textbook content below.\n'
  '\n'
  'MARKING SCHEME:\n'
  '- MCQ = 1 mark   - Short Question = 3 marks   - Long Question = 8 marks\n'
  '\n'
  'SCORING RULES:\n'
  'For MCQs:            1 = correct, 0 = incorrect\n'
  'For Short Questions: 3 = complete and correct\n'
  '                     2 = mostly correct with minor missing points\n'
  '                     1 = partially correct\n'
  '                     0 = incorrect\n'
  'For Long Questions:  8 = complete and accurate\n'
  '                     6-7 = mostly correct with small missing details\n'
  '                     4-5 = partially correct\n'
  '                     2-3 = mostly incorrect\n'
  '                     0-1 = completely wrong\n'
  '\n'
  'RULES:\n'
  '- Evaluate ONLY from the provided textbook content.\n'
  '- One sentence on what was correct. One sentence on what was missing.\n'
  '- For Maths: identify the exact wrong step and provide the correction.\n'
  '- Never give marks above the maximum allowed for the question type.\n'
  '\n'
  'OUTPUT FORMAT (strictly follow this):\n'
  'SCORE: [earned marks]/[total marks]\n'
  'FEEDBACK: [maximum 2-3 short sentences]\n'
  '\n'
  'CONTENT:\n'
  '{context}\n'
  '\n'
  'Question: {question}\n'
  'Student Answer: {student_answer}\n'
  'Evaluation:',
  'ai-service/prompts/evaluator.txt'),
 ('h2', 'C.3  Prompt template — tester agent'),
 ('code',
  'The tester agent prompt template (abridged)',
  'You are an exam question generator for Pakistani students.\n'
  'Student details: Class {class_level} | {board} Board | Subject: '
  '{subject}\n'
  'Topic: {topic}\n'
  '\n'
  'CONTENT SOURCES (in priority order):\n'
  '1. PAST PAPER QUESTIONS - highest priority\n'
  '   Extract questions that have actually appeared in past papers.\n'
  '2. TEXTBOOK AND KEYBOOK CONTENT - use for new questions only\n'
  '\n'
  'STRICT RULES:\n'
  '1. Use ONLY the provided content. Never go outside it.\n'
  '2. Mark each question clearly with its source.\n'
  '3. Generate exactly {num_questions} question(s) of type: {question_type}\n'
  '4. Match exact difficulty and style of {board} Board exams.\n'
  '5. Marks weightage: MCQ = 1 mark | Short = 3 marks | Long = 8 marks\n'
  '\n'
  'QUESTION LABELS (required on every question):\n'
  '  Past Paper  - taken directly from a past paper\n'
  '  Similar     - inspired by past paper style\n'
  '  New         - generated from textbook/keybook\n'
  '\n'
  'MCQ FORMAT:\n'
  'Q[n]. [Question] [label]\n'
  'A) [option]   B) [option]   C) [option]   D) [option]\n'
  'Correct: [Letter]\n'
  'Explanation: [one line why this is correct]\n'
  '\n'
  'CONTENT:\n'
  '{context}\n'
  '\n'
  'Generate {num_questions} {question_type} question(s) on: {topic}',
  'ai-service/prompts/tester.txt'),
 ('h2', 'C.4  Past-paper cleaning rules'),
 ('code',
  'Domain-specific noise removal for examination papers (abridged)',
  'def clean_past_paper(text: str) -> str:\n'
  '    # roll-number boxes and page references\n'
  "    text = re.sub(r'ROLL\\s*NUMBER.*?\\n', '', text, "
  'flags=re.IGNORECASE)\n'
  "    text = re.sub(r'Roll\\s*No\\.?.*?\\n',  '', text, "
  'flags=re.IGNORECASE)\n'
  "    text = re.sub(r'Page\\s*\\d+\\s*of\\s*\\d+.*?\\n', '', text, "
  'flags=re.IGNORECASE)\n'
  '\n'
  '    # examination header boilerplate\n'
  "    for pattern in (r'INTERMEDIATE.*?\\n', r'FEDERAL.*?EDUCATION.*?\\n',\n"
  "                    r'SECONDARY.*?EDUCATION.*?\\n', r'ISLAMABAD.*?\\n',\n"
  "                    r'Time allowed:.*?\\n', r'Total Marks.*?\\n', "
  "r'NOTE:.*?\\n'):\n"
  "        text = re.sub(pattern, '', text, flags=re.IGNORECASE)\n"
  '\n'
  '    # section headers and instructions, keeping the questions themselves\n'
  "    text = re.sub(r'SECTION[\\s\\-]*[ABC].*?\\n', '', text, "
  'flags=re.IGNORECASE)\n'
  "    text = re.sub(r'Attempt any.*?\\n', '', text, flags=re.IGNORECASE)\n"
  "    text = re.sub(r'All parts carry equal marks.*?\\n', '', text, "
  'flags=re.IGNORECASE)\n'
  '\n'
  '    # paper codes and marks allocations such as "(14 x 3 = 42)"\n'
  "    text = re.sub(r'\\d+HA\\w*', '', text)\n"
  "    text = re.sub(r'\\(\\d+\\s*x\\s*\\d+\\s*=\\s*\\d+\\)', '', text)\n"
  '\n'
  '    # OCR garbage from empty MCQ bubbles\n'
  "    text = re.sub(r'[оoО]\\s*[оoО]\\s*[оoО]', '', text)\n"
  '\n'
  "    return re.sub(r'\\n{3,}', '\\n\\n', text).strip()",
  'ai-service/scripts/02_clean_and_chunk.py'),
 ('h2', 'C.5  Resumable embedding and upsert'),
 ('code',
  'Batched embedding with resume support',
  'def process_file(jsonl_path, index, embedded_ids) -> int:\n'
  '    chunks = [json.loads(line) for line in open(jsonl_path, '
  'encoding="utf-8") if line.strip()]\n'
  '    chunks_to_embed = [c for c in chunks if c["chunk_id"] not in '
  'embedded_ids]\n'
  '    if not chunks_to_embed:\n'
  '        return 0                                   # nothing to do; '
  'nothing billed\n'
  '\n'
  '    total_uploaded, batch_buffer = 0, []\n'
  '    for i, chunk in enumerate(chunks_to_embed, start=1):\n'
  '        try:\n'
  '            chunk["embedding"] = get_embedding(chunk["text"])\n'
  '            batch_buffer.append(chunk)\n'
  '            save_embedded_id(chunk["chunk_id"])    # written before the '
  'upsert\n'
  '            if len(batch_buffer) >= BATCH_SIZE:    # 100 vectors per '
  'upsert\n'
  '                upload_batch(index, batch_buffer)\n'
  '                total_uploaded += len(batch_buffer)\n'
  '                batch_buffer = []\n'
  '                time.sleep(0.5)\n'
  '            time.sleep(0.05)\n'
  '        except Exception as e:\n'
  '            log(f"  ERROR: {chunk[\'chunk_id\']}: {e}")\n'
  '            continue                               # one bad chunk does '
  'not stop the run\n'
  '\n'
  '    if batch_buffer:\n'
  '        upload_batch(index, batch_buffer)\n'
  '        total_uploaded += len(batch_buffer)\n'
  '    return total_uploaded',
  'ai-service/scripts/03_embed_and_store.py'),
 ('h1', 'APPENDIX D:  USER MANUAL', 'D'),
 ('h2', 'D.1  For students'),
 ('numbers',
  ['Open the platform in a browser and choose Register. Enter your name, '
   'email address and a password, then open the verification email and click '
   'the link. Alternatively, choose Continue with Google, which verifies '
   'your address automatically.',
   'Sign in and open Selection. Choose your board, your class and your '
   'subject. This selection is remembered and is applied to everything the '
   'system generates for you.',
   'To learn a concept, open AI Tutor and type your question. You may write '
   'in English or Urdu. Follow-up questions such as “explain more” stay on '
   'the same topic. Each conversation is saved in the list on the left and '
   'can be reopened or deleted.',
   'To practise, open Practice. Choose whether to cover the whole book or '
   'select particular chapters, then choose multiple-choice, short or long '
   'questions. Answer each question and read the feedback before moving on.',
   'At the end of a practice session you receive your score, percentage, '
   'grade, the topics you did well in, the topics you struggled with and a '
   'study recommendation.',
   'To download study material, open Resources, filter by board, class, '
   'subject and type, and choose Download.',
   'To review your performance over time, open Progress, which shows your '
   'average score by subject and identifies the subject that needs the most '
   'attention.',
   'To change your password, enable two-factor authentication or switch '
   'between light and dark appearance, open Settings.']),
 ('h2', 'D.2  For administrators'),
 ('numbers',
  ['Sign in with an account whose role is administrator. The administrative '
   'section appears in the navigation.',
   'Open Content Manager to upload a resource. Provide a title, choose the '
   'type, board, class and subject, and select a file of up to 100 '
   'megabytes. The resource becomes visible to students immediately.',
   "Use the same screen to edit a resource's details or to delete it. "
   'Deleting a resource also removes the stored file.',
   'Open User Management to list accounts. Accounts can be searched and '
   'filtered by role and status, edited, blocked or deleted. Deleting an '
   "account also removes that student's chat sessions, quiz history and "
   'activity records.',
   'Open the Admin Dashboard for aggregate counts and recent '
   'registrations.']),
 ('h2', 'D.3  For the system operator'),
 ('numbers',
  ['Install PHP 8.4 with Composer, Node.js with npm, Python 3.12 and MySQL '
   '8.',
   'Copy .env.example to .env and set the database credentials, APP_URL, '
   'AI_SERVICE_URL, the Google OAuth client identifier, secret and redirect '
   'URI, and the mail transport settings.',
   'Run `composer install`, `php artisan key:generate`, `php artisan '
   'migrate` and `npm install`.',
   'In ai-service, create a virtual environment, run `pip install -r '
   'requirements.txt`, and set OPENAI_API_KEY, PINECONE_API_KEY and '
   "PINECONE_INDEX in the service's own .env file. Place the Google Cloud "
   'service-account credential file as google-credentials.json.',
   'Start the AI service with `uvicorn main:app --port 8001` and the '
   'application with `composer run dev`, which starts the web server, the '
   'queue listener and the Vite development server together. For production, '
   'run `npm run build` and serve the application through Nginx or Apache '
   'with PHP-FPM.',
   'To add curricular material, place PDF files under '
   'ai-service/data/raw/{board}/{class}/{subject}/{type}/ and run the three '
   'ingestion scripts in order: 01_extract_text.py, 02_clean_and_chunk.py '
   'and 03_embed_and_store.py. Every stage is idempotent, so an interrupted '
   'run may be restarted safely.',
   'Monitor ai-service/data/token_usage.jsonl for the token consumption and '
   'cost of every model call.']),
 ('h1', 'APPENDIX E:  SIMILARITY REPORT', 'E'),
 ('p',
  "The similarity report produced by the university's plagiarism-detection "
  'service is to be attached here, in accordance with the departmental '
  'submission requirement that the similarity index be below the threshold '
  'specified in the evaluation rubric.'),
 ('shot',
  'turnitin',
  'Similarity report summary page.',
  'Insert the first page of the similarity report generated by the '
  "university's plagiarism-detection service, showing the overall similarity "
  'index.')]
