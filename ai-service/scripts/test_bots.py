import sys
sys.path.append(".")

from teacher_bot import get_teacher_response
from tester_bot import generate_questions, evaluate_answer

print("=" * 60)
print("TEST 1 — Teacher Bot")
print("=" * 60)
answer = get_teacher_response(
    question    = "What is a cell and what are its basic functions?",
    board       = "federal",
    class_level = "class_11",
    subject     = "biology"
)
print(answer)

print("\n" + "=" * 60)
print("TEST 2 — Tester Bot (MCQ)")
print("=" * 60)
questions = generate_questions(
    topic         = "cell theory",
    board         = "federal",
    class_level   = "class_11",
    subject       = "biology",
    question_type = "mcq",
    num_questions = 3
)
print(questions)

print("\n" + "=" * 60)
print("TEST 3 — Evaluator Bot")
print("=" * 60)
feedback = evaluate_answer(
    question       = "What is cell theory?",
    student_answer = "Cell theory says that all living things are made of cells and cells come from other cells.",
    board          = "federal",
    class_level    = "class_11",
    subject        = "biology"
)
print(feedback)