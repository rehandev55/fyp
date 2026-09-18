"""
Bibliography in Chicago author-date style.

The template's red note reads: "Reference should be in Chicago format and
students can refer to scholar.google.com and use cite tab to copy the exact
format." Chicago author-date is used throughout: the reference list is
alphabetical by the first author's surname with a hanging indent, and works
are cited in the text as (Surname Year).

Author initials are kept as the sources give them rather than expanded to full
forenames, so that nothing is asserted about a person that the cited work does
not itself state.

Each record carries:
    key      the old IEEE bracket number, used to rewrite existing citations
    sort     the string the list is alphabetised on
    intext   the parenthetical form, without brackets
    surname  the family name used to detect an author already named in a
             sentence, so the citation can shorten to the year alone
    entry    the full reference-list line
"""

REFERENCES = [
    dict(key=1, sort="Holmes", surname="Holmes",
         intext="Holmes, Bialik, and Fadel 2019",
         entry="Holmes, A., M. Bialik, and C. Fadel. 2019. Artificial "
               "Intelligence in Education: Promises and Implications for "
               "Teaching and Learning. Boston, MA: Center for Curriculum "
               "Redesign."),
    dict(key=2, sort="Pardos", surname="Pardos",
         intext="Pardos and Heffernan 2020",
         entry="Pardos, Z. A., and N. T. Heffernan. 2020. “Using "
               "Artificial Intelligence to Improve Education.” IEEE "
               "Intelligent Systems 35 (5): 6–10."),
    dict(key=3, sort="Winkler", surname="Winkler",
         intext="Winkler and Söllner 2018",
         entry="Winkler, R., and M. Söllner. 2018. “Unleashing the "
               "Potential of Chatbots in Education: A State-of-the-Art "
               "Analysis.” In Proceedings of the Academy of Management "
               "Annual Meeting 2018 (1): 1–6."),
    dict(key=4, sort="Brown", surname="Brown", intext="Brown et al. 2020",
         entry="Brown, T. B., et al. 2020. “Language Models Are Few-Shot "
               "Learners.” In Advances in Neural Information Processing "
               "Systems 33: 1877–1901."),
    dict(key=5, sort="Lewis", surname="Lewis", intext="Lewis et al. 2020",
         entry="Lewis, P., et al. 2020. “Retrieval-Augmented Generation "
               "for Knowledge-Intensive NLP Tasks.” In Advances in "
               "Neural Information Processing Systems 33: 9459–74."),
    dict(key=6, sort="Devlin", surname="Devlin", intext="Devlin et al. 2019",
         entry="Devlin, J., M.-W. Chang, K. Lee, and K. Toutanova. 2019. "
               "“BERT: Pre-training of Deep Bidirectional Transformers "
               "for Language Understanding.” In Proceedings of NAACL-"
               "HLT, 4171–86."),
    dict(key=7, sort="Minaee", surname="Minaee", intext="Minaee et al. 2021",
         entry="Minaee, S., N. Kalchbrenner, E. Cambria, N. Nikzad, M. "
               "Chenaghlu, and J. Gao. 2021. “Deep Learning Based Text "
               "Classification: A Comprehensive Review.” ACM Computing "
               "Surveys 54 (3): 1–40."),
    dict(key=8, sort="OpenAI 2023", surname="OpenAI", intext="OpenAI 2023",
         entry="OpenAI. 2023. “GPT-4 Technical Report.” Accessed "
               "March 2, 2026. https://openai.com/research/gpt-4."),
    dict(key=9, sort="Pinecone", surname="Pinecone",
         intext="Pinecone Systems 2024",
         entry="Pinecone Systems Inc. 2024. “Pinecone Documentation: "
               "Metadata Filtering and Serverless Indexes.” Accessed "
               "April 18, 2026. https://docs.pinecone.io."),
    dict(key=10, sort="Johnson", surname="Johnson",
         intext="Johnson, Douze, and Jégou 2021",
         entry="Johnson, J., M. Douze, and H. Jégou. 2021. "
               "“Billion-Scale Similarity Search with GPUs.” IEEE "
               "Transactions on Big Data 7 (3): 535–47."),
    dict(key=11, sort="Ministry of Federal Education", surname="Ministry",
         intext="Ministry of Federal Education 2022",
         entry="Ministry of Federal Education and Professional Training. "
               "2022. National Curriculum of Pakistan. Islamabad: Government "
               "of Pakistan."),
    dict(key=12, sort="Rahman", surname="Rahman",
         intext="Rahman, Khan, and Iqbal 2023",
         entry="Rahman, A., S. Khan, and M. Iqbal. 2023. “Artificial "
               "Intelligence in the Pakistani Education System: Opportunities "
               "and Challenges.” Pakistan Journal of Educational "
               "Research 6 (2): 45–58."),
    dict(key=13, sort="Adamopoulou", surname="Adamopoulou",
         intext="Adamopoulou and Moussiades 2020",
         entry="Adamopoulou, E., and L. Moussiades. 2020. “Chatbots: "
               "History, Technology, and Applications.” Machine Learning "
               "with Applications 2: 1–15."),
    dict(key=14, sort="Hugging Face", surname="Hugging Face",
         intext="Hugging Face 2024",
         entry="Hugging Face. 2024. “Transformers: State-of-the-Art "
               "Natural Language Processing.” Accessed April 20, 2026. "
               "https://huggingface.co/docs/transformers."),
    dict(key=15, sort="UNESCO", surname="UNESCO", intext="UNESCO 2021",
         entry="UNESCO. 2021. Artificial Intelligence in Education: Guidance "
               "for Policy-Makers. Paris: UNESCO."),
    dict(key=16, sort="Vaswani", surname="Vaswani",
         intext="Vaswani et al. 2017",
         entry="Vaswani, A., et al. 2017. “Attention Is All You "
               "Need.” In Advances in Neural Information Processing "
               "Systems 30: 5998–6008."),
    dict(key=17, sort="Ji", surname="Ji", intext="Ji et al. 2023",
         entry="Ji, Z., et al. 2023. “Survey of Hallucination in Natural "
               "Language Generation.” ACM Computing Surveys 55 (12): "
               "1–38."),
    dict(key=18, sort="Bloom", surname="Bloom", intext="Bloom 1984",
         entry="Bloom, B. S. 1984. “The 2 Sigma Problem: The Search for "
               "Methods of Group Instruction as Effective as One-to-One "
               "Tutoring.” Educational Researcher 13 (6): 4–16."),
    dict(key=19, sort="VanLehn", surname="VanLehn", intext="VanLehn 2011",
         entry="VanLehn, K. 2011. “The Relative Effectiveness of Human "
               "Tutoring, Intelligent Tutoring Systems, and Other Tutoring "
               "Systems.” Educational Psychologist 46 (4): "
               "197–221."),
    dict(key=20, sort="Anderson", surname="Anderson",
         intext="Anderson et al. 1995",
         entry="Anderson, J. R., A. T. Corbett, K. R. Koedinger, and R. "
               "Pelletier. 1995. “Cognitive Tutors: Lessons "
               "Learned.” Journal of the Learning Sciences 4 (2): "
               "167–207."),
    dict(key=21, sort="Corbett", surname="Corbett",
         intext="Corbett and Anderson 1994",
         entry="Corbett, A. T., and J. R. Anderson. 1994. “Knowledge "
               "Tracing: Modeling the Acquisition of Procedural "
               "Knowledge.” User Modeling and User-Adapted Interaction 4 "
               "(4): 253–78."),
    dict(key=22, sort="Piech", surname="Piech", intext="Piech et al. 2015",
         entry="Piech, C., et al. 2015. “Deep Knowledge Tracing.” "
               "In Advances in Neural Information Processing Systems 28: "
               "505–13."),
    dict(key=23, sort="Weizenbaum", surname="Weizenbaum",
         intext="Weizenbaum 1966",
         entry="Weizenbaum, J. 1966. “ELIZA: A Computer Program for the "
               "Study of Natural Language Communication between Man and "
               "Machine.” Communications of the ACM 9 (1): 36–45."),
    dict(key=24, sort="Karpukhin", surname="Karpukhin",
         intext="Karpukhin et al. 2020",
         entry="Karpukhin, V., et al. 2020. “Dense Passage Retrieval for "
               "Open-Domain Question Answering.” In Proceedings of "
               "EMNLP, 6769–81."),
    dict(key=25, sort="Robertson", surname="Robertson",
         intext="Robertson and Zaragoza 2009",
         entry="Robertson, S., and H. Zaragoza. 2009. “The Probabilistic "
               "Relevance Framework: BM25 and Beyond.” Foundations and "
               "Trends in Information Retrieval 3 (4): 333–89."),
    dict(key=26, sort="Reimers", surname="Reimers",
         intext="Reimers and Gurevych 2019",
         entry="Reimers, N., and I. Gurevych. 2019. “Sentence-BERT: "
               "Sentence Embeddings Using Siamese BERT-Networks.” In "
               "Proceedings of EMNLP-IJCNLP, 3982–92."),
    dict(key=27, sort="Malkov", surname="Malkov",
         intext="Malkov and Yashunin 2020",
         entry="Malkov, Y. A., and D. A. Yashunin. 2020. “Efficient and "
               "Robust Approximate Nearest Neighbor Search Using Hierarchical "
               "Navigable Small World Graphs.” IEEE Transactions on "
               "Pattern Analysis and Machine Intelligence 42 (4): "
               "824–36."),
    dict(key=28, sort="Gao", surname="Gao", intext="Gao et al. 2024",
         entry="Gao, Y., et al. 2024. “Retrieval-Augmented Generation "
               "for Large Language Models: A Survey.” arXiv preprint "
               "arXiv:2312.10997."),
    dict(key=29, sort="Wei", surname="Wei", intext="Wei et al. 2022",
         entry="Wei, J., et al. 2022. “Chain-of-Thought Prompting "
               "Elicits Reasoning in Large Language Models.” In Advances "
               "in Neural Information Processing Systems 35: "
               "24824–37."),
    dict(key=30, sort="Ouyang", surname="Ouyang", intext="Ouyang et al. 2022",
         entry="Ouyang, L., et al. 2022. “Training Language Models to "
               "Follow Instructions with Human Feedback.” In Advances in "
               "Neural Information Processing Systems 35: 27730–44."),
    dict(key=31, sort="Burrows", surname="Burrows",
         intext="Burrows, Gurevych, and Stein 2015",
         entry="Burrows, S., I. Gurevych, and B. Stein. 2015. “The Eras "
               "and Trends of Automatic Short Answer Grading.” "
               "International Journal of Artificial Intelligence in Education "
               "25 (1): 60–117."),
    dict(key=32, sort="Page", surname="Page", intext="Page 1966",
         entry="Page, E. B. 1966. “The Imminence of Grading Essays by "
               "Computer.” Phi Delta Kappan 47 (5): 238–43."),
    dict(key=33, sort="Mizumoto", surname="Mizumoto",
         intext="Mizumoto and Eguchi 2023",
         entry="Mizumoto, A., and M. Eguchi. 2023. “Exploring the "
               "Potential of Using an AI Language Model for Automated Essay "
               "Scoring.” Research Methods in Applied Linguistics 2 "
               "(2)."),
    dict(key=34, sort="Luckin", surname="Luckin", intext="Luckin et al. 2016",
         entry="Luckin, R., W. Holmes, M. Griffiths, and L. B. Forcier. 2016. "
               "Intelligence Unleashed: An Argument for AI in Education. "
               "London: Pearson."),
    dict(key=35, sort="Kasneci", surname="Kasneci",
         intext="Kasneci et al. 2023",
         entry="Kasneci, E., et al. 2023. “ChatGPT for Good? On "
               "Opportunities and Challenges of Large Language Models for "
               "Education.” Learning and Individual Differences 103."),
    dict(key=36, sort="Baidoo-Anu", surname="Baidoo-Anu",
         intext="Baidoo-Anu and Ansah 2023",
         entry="Baidoo-Anu, D., and L. O. Ansah. 2023. “Education in the "
               "Era of Generative Artificial Intelligence (AI): Understanding "
               "the Potential Benefits of ChatGPT in Promoting Teaching and "
               "Learning.” Journal of AI 7 (1): 52–62."),
    dict(key=37, sort="OpenAI 2024", surname="OpenAI", intext="OpenAI 2024",
         entry="OpenAI. 2024. “GPT-4o Mini: Advancing Cost-Efficient "
               "Intelligence.” Accessed April 18, 2026. "
               "https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-"
               "intelligence."),
    dict(key=38, sort="Fowler", surname="Fowler", intext="Fowler 2003",
         entry="Fowler, M. 2003. Patterns of Enterprise Application "
               "Architecture. Boston, MA: Addison-Wesley."),
    dict(key=39, sort="Sommerville", surname="Sommerville",
         intext="Sommerville 2016",
         entry="Sommerville, I. 2016. Software Engineering. 10th ed. Harlow, "
               "UK: Pearson."),
    dict(key=40, sort="Beck", surname="Beck", intext="Beck et al. 2001",
         entry="Beck, K., et al. 2001. “Manifesto for Agile Software "
               "Development.” Accessed April 9, 2026. "
               "https://agilemanifesto.org."),
    dict(key=41, sort="IEEE", surname="IEEE", intext="IEEE 1998",
         entry="IEEE. 1998. IEEE Recommended Practice for Software "
               "Requirements Specifications. IEEE Std 830-1998. New York: "
               "IEEE."),
    dict(key=42, sort="Schwaber", surname="Schwaber",
         intext="Schwaber and Sutherland 2020",
         entry="Schwaber, K., and J. Sutherland. 2020. “The Scrum Guide: "
               "The Definitive Guide to Scrum — The Rules of the "
               "Game.” Accessed April 9, 2026. https://scrumguides.org."),
    dict(key=43, sort="Google Cloud", surname="Google Cloud",
         intext="Google Cloud 2024",
         entry="Google Cloud. 2024. “Cloud Vision API Documentation: "
               "Document Text Detection.” Accessed April 22, 2026. "
               "https://cloud.google.com/vision/docs."),
    dict(key=44, sort="Laravel", surname="Laravel", intext="Laravel 2025",
         entry="Laravel. 2025. “Laravel Documentation.” Accessed "
               "September 1, 2026. https://laravel.com/docs."),
    dict(key=45, sort="Meta Open Source", surname="Meta Open Source",
         intext="Meta Open Source 2025",
         entry="Meta Open Source. 2025. “React Documentation.” "
               "Accessed September 1, 2026. https://react.dev."),
    dict(key=46, sort="Ramírez", surname="Ramírez",
         intext="Ramírez 2025",
         entry="Ramírez, S. 2025. “FastAPI Documentation.” "
               "Accessed September 1, 2026. https://fastapi.tiangolo.com."),
    dict(key=47, sort="Inertia.js", surname="Inertia.js",
         intext="Inertia.js 2025",
         entry="Inertia.js. 2025. “Inertia.js Documentation.” "
               "Accessed September 1, 2026. https://inertiajs.com."),
    dict(key=48, sort="OWASP", surname="OWASP",
         intext="OWASP Foundation 2021",
         entry="OWASP Foundation. 2021. “OWASP Top Ten Web Application "
               "Security Risks.” Accessed May 4, 2026. "
               "https://owasp.org/Top10."),
    dict(key=49, sort="Nye", surname="Nye", intext="Nye 2015",
         entry="Nye, B. D. 2015. “Intelligent Tutoring Systems by and "
               "for the Developing World: A Review of Trends and Approaches "
               "for Educational Technology in a Global Context.” "
               "International Journal of Artificial Intelligence in Education "
               "25 (2): 177–203."),
    dict(key=50, sort="Zawacki-Richter", surname="Zawacki-Richter",
         intext="Zawacki-Richter et al. 2019",
         entry="Zawacki-Richter, O., V. I. Marín, M. Bond, and F. "
               "Gouverneur. 2019. “Systematic Review of Research on "
               "Artificial Intelligence Applications in Higher Education: "
               "Where Are the Educators?” International Journal of "
               "Educational Technology in Higher Education 16 (39): "
               "1–27."),
    dict(key=51, sort="OpenAI 2025", surname="OpenAI", intext="OpenAI 2025",
         entry="OpenAI. 2025. “Pricing: Models and Rates.” Accessed "
               "September 10, 2026. https://openai.com/api/pricing."),
    dict(key=52, sort="Federal Board", surname="Federal Board",
         intext="Federal Board of Intermediate and Secondary Education 2024",
         entry="Federal Board of Intermediate and Secondary Education. 2024. "
               "“Model Papers and Scheme of Studies for SSC and "
               "HSSC.” Accessed April 12, 2026. "
               "https://www.fbise.edu.pk."),
]

BY_KEY = {r["key"]: r for r in REFERENCES}

#: the reference list, alphabetised as Chicago requires
SORTED = sorted(REFERENCES, key=lambda r: r["sort"].lower())

#: Chicago italicises the title of the containing work: the journal or
#: proceedings for an article, the book title for a monograph. The span is
#: derived from the entry, with an override where the derivation would sweep
#: up an edition or standard number that belongs in roman type.
_ITALIC_OVERRIDE = {
    39: "Software Engineering",
    41: "IEEE Recommended Practice for Software Requirements Specifications",
}


def italic_span(record):
    """The part of a reference-list entry that Chicago sets in italics, or
    None for a web page or preprint, where nothing is italicised."""
    import re

    if record["key"] in _ITALIC_OVERRIDE:
        return _ITALIC_OVERRIDE[record["key"]]

    entry = record["entry"]
    if "”" in entry:                       # an article: quoted title
        tail = entry.split("”", 1)[1].strip()
        if not tail or tail.startswith(("Accessed", "http", "arXiv")):
            return None
        if tail.startswith("In "):
            tail = tail[3:]
        match = re.match(r"([A-Za-zÀ-ɏ][^0-9]*?)(?=\s+\d|\.\s*$|,\s)",
                         tail)
        return match.group(1).strip().rstrip(".,") if match else None

    match = re.search(                          # a book: title before the city
        r"\.\s\d{4}\.\s(.+?)\.\s[A-Z]", entry)
    return match.group(1).strip() if match else None


def entries():
    """Reference-list lines in alphabetical order, each as a list of
    (text, italic) runs ready for the renderer."""
    out = []
    for record in SORTED:
        entry, span = record["entry"], italic_span(record)
        if span and span in entry:
            head, _, tail = entry.partition(span)
            out.append([(head, False), (span, True), (tail, False)])
        else:
            out.append([(entry, False)])
    return out


if __name__ == "__main__":
    import io
    import sys
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    print(f"{len(REFERENCES)} references\n")
    for r in SORTED:
        print(f"  ({r['intext']})")
        print(f"      {r['entry'][:96]}")
