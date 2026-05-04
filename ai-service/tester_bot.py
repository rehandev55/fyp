import os
from dotenv import load_dotenv
from openai import OpenAI
from rag.retriever import retrieve, retrieve_combined, format_context, _openai_client as client
from utils.token_logger import log_token_usage
from pathlib import Path

load_dotenv()

TESTER_TEMPLATE    = Path("prompts/tester.txt").read_text(encoding="utf-8")
EVALUATOR_TEMPLATE = Path("prompts/evaluator.txt").read_text(encoding="utf-8")


def generate_questions(
    topic:         str,
    board:         str,
    class_level:   str,
    subject:       str,
    question_type: str = "mcq",
    num_questions: int = 5,
) -> str:
    # single embed call for both textbook and past paper retrieval
    context = retrieve_combined(topic, board, class_level, subject)

    prompt = TESTER_TEMPLATE.format(
        board         = board,
        class_level   = class_level,
        subject       = subject,
        context       = context,
        question_type = question_type,
        num_questions = num_questions,
        topic         = topic,
    )

    response = client.chat.completions.create(
        model       = "gpt-4o-mini",
        messages    = [
            {"role": "system", "content": prompt},
            {"role": "user",   "content": f"Generate {num_questions} {question_type} on: {topic}"},
        ],
        temperature = 0.4,
        max_tokens  = 2000,
    )

    log_token_usage(
        endpoint          = "quiz_generate",
        model             = "gpt-4o-mini",
        board             = board,
        class_level       = class_level,
        subject           = subject,
        prompt_tokens     = response.usage.prompt_tokens,
        completion_tokens = response.usage.completion_tokens,
    )

    return response.choices[0].message.content


def evaluate_answer(
    question:       str,
    student_answer: str,
    board:          str,
    class_level:    str,
    subject:        str,
) -> str:
    chunks  = retrieve(query=question, board=board,
                       class_level=class_level, subject=subject, top_k=3)
    context = format_context(chunks)

    prompt = EVALUATOR_TEMPLATE.format(
        board          = board,
        class_level    = class_level,
        subject        = subject,
        context        = context,
        question       = question,
        student_answer = student_answer,
    )

    response = client.chat.completions.create(
        model       = "gpt-4o-mini",
        messages    = [
            {"role": "system", "content": prompt},
            {"role": "user",   "content": f"Evaluate: {student_answer}"},
        ],
        temperature = 0.2,
        max_tokens  = 500,
    )

    log_token_usage(
        endpoint          = "quiz_evaluate",
        model             = "gpt-4o-mini",
        board             = board,
        class_level       = class_level,
        subject           = subject,
        prompt_tokens     = response.usage.prompt_tokens,
        completion_tokens = response.usage.completion_tokens,
    )

    return response.choices[0].message.content