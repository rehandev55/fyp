import os
from dotenv import load_dotenv
from openai import OpenAI
from rag.retriever import retrieve, format_context
from pathlib import Path

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TESTER_TEMPLATE    = Path("prompts/tester.txt").read_text(encoding="utf-8")
EVALUATOR_TEMPLATE = Path("prompts/evaluator.txt").read_text(encoding="utf-8")

def generate_questions(
    topic:         str,
    board:         str,
    class_level:   str,
    subject:       str,
    question_type: str = "mcq",    # mcq | short | long
    num_questions: int = 5
) -> str:
    """Generate exam questions on a topic."""

    # retrieve relevant chunks
    chunks = retrieve(
        query       = topic,
        board       = board,
        class_level = class_level,
        subject     = subject,
        top_k       = 5
    )
    context = format_context(chunks)

    # build prompt
    prompt = TESTER_TEMPLATE.format(
        board         = board,
        class_level   = class_level,
        context       = context,
        question_type = question_type,
        num_questions = num_questions,
        topic         = topic,
        subject     = subject
    )

    response = client.chat.completions.create(
        model    = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user",   "content": f"Generate {num_questions} {question_type} questions on: {topic}"}
        ],
        temperature = 0.4,
        max_tokens  = 2000
    )

    return response.choices[0].message.content


def evaluate_answer(
    question:      str,
    student_answer: str,
    board:         str,
    class_level:   str,
    subject:       str
) -> str:
    """Evaluate a student's answer and give feedback."""

    # retrieve relevant chunks for context
    chunks = retrieve(
        query       = question,
        board       = board,
        class_level = class_level,
        subject     = subject,
        top_k       = 3
    )
    context = format_context(chunks)

    # build prompt
    prompt = EVALUATOR_TEMPLATE.format(
        board          = board,
        class_level    = class_level,
        context        = context,
        question       = question,
        student_answer = student_answer,
        subject = subject
    )

    response = client.chat.completions.create(
        model    = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user",   "content": f"Evaluate this answer: {student_answer}"}
        ],
        temperature = 0.2,
        max_tokens  = 500
    )

    return response.choices[0].message.content