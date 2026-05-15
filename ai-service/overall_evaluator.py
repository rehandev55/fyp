import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path
from utils.token_logger import log_token_usage

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_TEMPLATE = Path("prompts/overall_feedback.txt").read_text(encoding="utf-8")


def parse_overall_response(text: str) -> dict:
    """Parse the structured response from LLM into a dict."""
    result = {
    "strong_areas":     [],
    "weak_areas":       [],
    "overall_feedback": "",
    "study_tip":        ""
    }

    for line in text.strip().split("\n"):
        line = line.strip()
        if not line or ":" not in line:
            continue

        key, _, value = line.partition(":")
        key   = key.strip().upper()
        value = value.strip()

        if key == "STRONG_AREAS":
            result["strong_areas"] = [
                a.strip() for a in value.split(",") if a.strip()
            ]
        elif key == "WEAK_AREAS":
            result["weak_areas"] = [
                a.strip() for a in value.split(",") if a.strip()
            ]
        elif key == "OVERALL_FEEDBACK":
            result["overall_feedback"] = value
        elif key == "STUDY_TIP":
            result["study_tip"] = value

    return result


def get_overall_feedback(
    board:         str,
    class_level:   str,
    subject:       str,
    question_type: str,
    results:       list[dict],
) -> dict:
    score_limits = {
    "mcq": 1,
    "short": 3,
    "long": 8,
    }

    max_per_question = score_limits.get(question_type.lower(), 10)

    total_possible = len(results) * max_per_question
    total_earned = sum(r.get("score", 0) for r in results)

    percentage = round(
        (total_earned / total_possible) * 100, 2
    ) if total_possible else 0

    if percentage >= 80:
        grade = "Excellent"
    elif percentage >= 60:
        grade = "Good"
    elif percentage >= 40:
        grade = "Needs Work"
    else:
        grade = "Poor"

    session_lines = []
    for i, r in enumerate(results, start=1):
        session_lines.append(
            f"Q{i}: {r['question']}\n"
            f"Student Answer: {r['student_answer']}\n"
            f"Score: {r.get('score', 0)}/{max_per_question}\n"
            f"Feedback: {r.get('feedback', '')}\n"
        )

    session_results = "\n---\n".join(session_lines)

    # build prompt
    prompt = PROMPT_TEMPLATE.format(
        board          = board,
        class_level    = class_level,
        subject        = subject,
        question_type  = question_type,
        session_results = session_results,
        total_earned=total_earned,
        total_possible=total_possible,
    )

    response = client.chat.completions.create(
        model    = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user",   "content": "Provide overall session feedback."}
        ],
        temperature = 0.2,
        max_tokens  = 600,
    )

    # log tokens
    log_token_usage(
        endpoint          = "quiz_overall",
        model             = "gpt-4o-mini",
        board             = board,
        class_level       = class_level,
        subject           = subject,
        prompt_tokens     = response.usage.prompt_tokens,
        completion_tokens = response.usage.completion_tokens,
    )

    raw_text = response.choices[0].message.content
    parsed   = parse_overall_response(raw_text)
    # backend-controlled calculations
    parsed["total_score"] = f"{total_earned} / {total_possible}"
    parsed["percentage"] = percentage
    parsed["grade"] = grade

    return parsed
    