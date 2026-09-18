"""
Requirement-elicitation survey data.

Source: "Academic Research Survey", Google Forms, 48 responses, exported as a
response-summary archive. Closed questions are recorded as the option counts
reported by Google Forms. Open questions are recorded verbatim, and the
thematic coding applied to them is performed here in code so that the counts
quoted in Chapter 3 and Appendix B can be re-derived and audited.

A free-text answer may carry more than one theme, so theme counts sum to more
than the number of respondents. This is stated wherever such counts are used.
"""

N = 48

# ── closed questions ─────────────────────────────────────────────────────────
CLASS_DISTRIBUTION = [("Class 9", 6), ("Class 10", 7),
                      ("Class 11", 17), ("Class 12", 18)]

STUDY_LOCATION = [("At home", 22), ("At school", 20),
                  ("At tuition", 3), ("All of these", 3)]

WHEN_STUCK = [("Watch YouTube", 17), ("ChatGPT", 16), ("Google it", 15),
              ("Ask teacher", 11), ("Ask friend or classmate", 5),
              ("Use notes or books", 5)]
WHEN_STUCK_N = 47  # multiple selections allowed

USES_CHATGPT = [("Yes", 36), ("No", 12)]

NEEDS_HELP_WITH = [("Understanding concepts", 25), ("Both", 18),
                   ("Practising questions", 3), ("Not sure", 2)]

BOARD_SYLLABUS_APP = [("Yes", 38), ("Maybe", 8), ("No", 2)]

CHATBOT_TEST = [("Yes", 38), ("Maybe", 7), ("No", 3)]

DOWNLOADS_MATERIAL = [("Yes, but they are difficult to find", 25),
                      ("No, I do not download them", 16),
                      ("Yes, and they are easy to find", 7)]

BOARD_VS_ONLINE = [("Yes", 24), ("Sometimes", 14), ("No", 10)]

# ── open questions, recorded verbatim ────────────────────────────────────────
# (response text, number of respondents who gave it)
CHATGPT_PROBLEMS = [
    ("limited time is so problematic", 1),
    (".", 1),
    ("Difficult language", 1),
    ("Do not give proper information", 1),
    ("Don't give digrams, lengthy and wrong answers", 1),
    ("Extra explanation", 1),
    ("It doesn't completely understand what i am trying to say", 1),
    ("Its limits of models", 1),
    ("Lengthy answers", 1),
    ("Lengthy answers and difficult wording", 1),
    ("Limited data", 1),
    ("My subj are art", 1),
    ("Nil", 1),
    ("No", 5),
    ("No one", 3),
    ("No problem", 1),
    ("Not have any problem", 1),
    ("Not sure any problem", 1),
    ("Nothing", 5),
    ("Problem in solving numericals and maths questions also provide "
     "lengthy answers.", 1),
    ("Sometimes it gives unreal solutions", 1),
    ("Sometimes we have to repeat it twice.", 1),
    ("Too lengthy explanation and difficult words.", 1),
    ("Wrong answers and aslo not able to convey concepts properly", 1),
    ("Yes, accomodations in physics.", 1),
    ("answers not relted to questions", 1),
    ("chatgpt gives different answers form questions, aslo not to the point, "
     "high level answers that not suits college level students", 1),
    ("difficult wording", 1),
    ("don't provide proper answer", 1),
    ("extra explanation", 1),
    ("it takes way too long for chatgpt to understand my question", 1),
    ("language understanding", 1),
    ("lengthy answers", 1),
    ("long answers", 1),
    ("next level answers and aslo lengthy descriptions", 1),
]

DESIRED_FEATURES = [
    "YouTube",
    "all necessary features",
    "Ai chatbot and past papers help us to prepare for paper",
    "It should be correct",
    "to fully explain the answer",
    "Ni",
    "Chapter video",
    "Quizzes, past papers and keybooks",
    "Google.it helps me to learn more",
    "I don't know!",
    "Quizzes, key books, past papers and text books data",
    "No app",
    "Learning lot of experience",
    "Meta",
    "Quizzes, past papers, key books",
    "access to past papers, chapter videos, keybooks and textbooks",
    "acess to keybooks and pastpapers",
    "Google",
    "Understand our language",
    "acess to pastpapers, mcqs, chapter videos",
    "short answers and direct, subscription free, urdu option",
    "Google because it help me to learn",
    "I think past papers and chapter videos.",
    "concept base understanding and in understadable language",
    "Key book and past papers because it helps students a lot",
    "You tube",
    "subscription free, user friendly insterface, understandable and to the "
    "point answers",
    "All",
    "Idk",
    "ChatGPT",
    "Explanation in a simple way",
    "Voice, pictures",
    "Voice answers",
    "to the point answer, correct numericalsanswers and helpful",
    "It should understand the problem according to the syllabus one is "
    "studying",
    "Deep understanding",
    "AI chatbot and chapter videos",
    "relavent content",
    "Key books",
    "I don't know",
    "Answers in voice form",
    "To the point answers and easy learning",
    "It will answer accurately",
    "access to pastpapers and chapters videos",
    "Access to past papers and keybooks",
    "It short answer shortly and to the point also in easy wording.",
    "Help in pronunciation accuracy by proving answer in voice",
]

STUDY_DIFFICULTIES = [
    "Time management",
    "long syllabus and time management",
    "long syllabus",
    "no guidence, time management and long syllabus",
    "to much burden of study",
    "No",
    "Time management and long syllabus",
    "If I don't have concept and I  read lesson",
    "Regarding the other subjects",
    ".",
    "Time maganing",
    "Internet problem",
    "Walking daily",
    "Nothing else",
    "Concepts",
    "Distraction",
    "Private student",
    "no guidence, time management and lack of focus",
    "lengthy and sifficult answers",
    "If my concepts are not clear",
    "Long Syllabus.",
    "not able to understand concept",
    "Memorization",
    "time management",
    "Can't Focus",
    "Time managment",
    "Concept clearance",
    "No",
    "Understanding topics",
    "no tto the point answers and incorrect",
    "I just can't study",
    "Limited material",
    "time management and long syllabus",
    "to finding my syllabus material",
    "Time management because sometimes it's hard to understand multiple "
    "subjects at the same time.",
    "My brain isn't working",
    "Forgetting things that already learnt",
    "lengthy syllabus",
    "Struggling to understand the topic about which internet has less details",
    "time management and hard concepts understanding",
    "Understanding hard concepts",
    "Don't understand anything",
    "In understanding topics and clearing concepts",
]

ONLINE_TOOLS = [
    ("No", 19), ("no", 4), ("No one", 2), ("Nope", 1),
    ("Chatgpt", 3), ("Yes I use chatgpt", 2), ("ChatGPT", 1), ("Chatbot", 1),
    ("Chatgpt, Filo", 1), ("Yes, chatgpt", 1), ("Youtube chatgpt", 1),
    ("Yes I use YouTube and chatgpt", 1), ("yes i use chatgpt", 1),
    ("yes I use AI and chatgpt", 1), ("chatgpt, perplexity, quizlet", 1),
    ("YouTube", 1), ("Google", 1), ("Yes, google", 1), ("Education app", 1),
    ("Yes GothAI", 1), ("Yes pw", 1), ("Studylay", 1), ("studley(physics)", 1),
]

# ── thematic coding ──────────────────────────────────────────────────────────
# Each theme is a list of lowercase substrings. A response is coded to a theme
# when any of its markers occurs in the response.

CHATGPT_PROBLEM_THEMES = [
    ("Answers too long or padded", [
        "lengthy", "long answers", "extra explanation", "not to the point",
        "lengthy descriptions"]),
    ("Wording too difficult or too advanced", [
        "difficult language", "difficult wording", "difficult words",
        "language understanding", "high level answers", "next level answers"]),
    ("Wrong, vague or irrelevant answers", [
        "wrong answers", "unreal solutions", "not relted", "not related",
        "do not give proper information", "don't provide proper answer",
        "different answers form questions", "not able to convey concepts"]),
    ("Does not understand the question", [
        "doesn't completely understand", "repeat it twice",
        "takes way too long for chatgpt to understand"]),
    ("Weak on numericals and maths", [
        "numericals", "accomodations in physics"]),
    ("Model or data limits", [
        "limits of models", "limited data", "limited time"]),
    ("No diagrams", ["digrams", "diagrams"]),
]

NO_PROBLEM_MARKERS = ["nil", "no problem", "not have any problem",
                      "not sure any problem", "nothing", "no one"]

FEATURE_THEMES = [
    ("Past papers", ["past paper", "pastpaper"]),
    ("Simple wording and to-the-point answers", [
        "to the point", "easy wording", "simple way", "understadable",
        "understandable", "understand our language", "short answers",
        "easy learning", "fully explain", "deep understanding",
        "concept base"]),
    ("Keybooks and textbooks", ["keybook", "key book", "text book",
                                "textbook"]),
    ("Chapter videos", ["chapter video", "chapters video"]),
    ("Quizzes and MCQs", ["quizz", "mcq"]),
    ("AI chatbot", ["ai chatbot", "chatgpt", "chatbot"]),
    ("Voice answers", ["voice", "pronunciation"]),
    ("Correct and accurate answers", ["should be correct", "answer accurately",
                                      "correct numericals"]),
    ("Syllabus-aligned content", ["according to the syllabus",
                                  "relavent content", "relevant content"]),
    ("Free to use", ["subscription free"]),
    ("Urdu option", ["urdu"]),
]

DIFFICULTY_THEMES = [
    ("Time management", ["time management", "time managment", "time maganing"]),
    ("Understanding concepts", [
        "concept", "understand", "hard concepts", "memorization",
        "forgetting"]),
    ("Long syllabus", ["long syllabus", "lengthy syllabus", "burden of study",
                       "long syllabus."]),
    ("Focus and distraction", ["focus", "distraction", "can't study"]),
    ("Finding study material", ["limited material", "syllabus material",
                                "internet has less details",
                                "internet problem"]),
    ("No guidance", ["no guidence", "no guidance", "private student"]),
]


def _code(responses, themes):
    """Count responses matching each theme. `responses` is a list of strings or
    (string, count) pairs. Returns a list of (theme, count), highest first."""
    pairs = [(r, 1) if isinstance(r, str) else r for r in responses]
    counts = []
    for label, markers in themes:
        total = sum(n for text, n in pairs
                    if any(m in text.lower() for m in markers))
        counts.append((label, total))
    return sorted(counts, key=lambda kv: -kv[1])


def chatgpt_problem_themes():
    """Themes among the respondents who reported a concrete problem."""
    reported = [(t, n) for t, n in CHATGPT_PROBLEMS
                if not any(m in t.lower() for m in NO_PROBLEM_MARKERS)
                and t.strip(". ") not in ("", "No")
                and "my subj are art" not in t.lower()]
    return _code(reported, CHATGPT_PROBLEM_THEMES), sum(n for _, n in reported)


def feature_themes():
    return _code(DESIRED_FEATURES, FEATURE_THEMES)


def difficulty_themes():
    return _code(STUDY_DIFFICULTIES, DIFFICULTY_THEMES)


def online_tool_groups():
    """Collapse the free-text tool answers into three groups."""
    no_tool = sum(n for t, n in ONLINE_TOOLS
                  if t.strip().lower() in ("no", "no one", "nope"))
    chatgpt = sum(n for t, n in ONLINE_TOOLS if "chatgpt" in t.lower()
                  or t.lower() in ("chatbot",))
    other = N - no_tool - chatgpt
    return [("Uses ChatGPT or a chatbot", chatgpt),
            ("Uses no online tool", no_tool),
            ("Uses some other tool", other)]


def pct(value, total=N):
    return round(100.0 * value / total, 1)


if __name__ == "__main__":
    themes, reported = chatgpt_problem_themes()
    print(f"ChatGPT problems - {reported} respondents reported a problem")
    for label, count in themes:
        print(f"  {label:42} {count}")
    print("\nDesired features")
    for label, count in feature_themes():
        print(f"  {label:42} {count}")
    print("\nStudy difficulties")
    for label, count in difficulty_themes():
        print(f"  {label:42} {count}")
    print("\nOnline tool groups")
    for label, count in online_tool_groups():
        print(f"  {label:42} {count}  ({pct(count)}%)")
