import os
from dotenv import load_dotenv
from openai import OpenAI
from rag.retriever import retrieve, format_context
from memory_manager import build_messages_with_memory, _update_summary  # ← import at top
from pathlib import Path

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_TEMPLATE = Path("prompts/teacher.txt").read_text(encoding="utf-8")


def get_teacher_response(
    question:         str,
    board:            str,
    class_level:      str,
    subject:          str,
    language:         str  = "en",
    chat_history:     list = [],
    existing_summary: str  = "",
) -> dict:

    if existing_summary and len(question.split()) < 6:
        summary_context = existing_summary.split('.')[0]
        search_query = f"{summary_context}. {question}"
    else:
        search_query = question
    chunks = retrieve(
        query       = search_query,
        board       = board,
        class_level = class_level,
        subject     = subject,
        top_k       = 5,
    )
    context = format_context(chunks)

    system_prompt = PROMPT_TEMPLATE.format(
        board       = board,
        class_level = class_level,
        subject     = subject,
        context     = context,
        question    = question,
    )

    messages, updated_summary = build_messages_with_memory(
        system_prompt    = system_prompt,
        chat_history     = chat_history,
        question         = question,
        existing_summary = existing_summary,
    )

    response = client.chat.completions.create(
        model       = "gpt-4o-mini",
        messages    = messages,
        temperature = 0.3,
        max_tokens  = 1000,
    )

    answer = response.choices[0].message.content

    # always update summary with current exchange
    try:
        current_exchange = [
            {"role": "user",      "content": question},
            {"role": "assistant", "content": answer},
        ]
        final_summary = _update_summary(
            existing_summary = updated_summary or existing_summary,
            new_messages     = current_exchange
        )
    except Exception as e:
        print(f"[WARNING] Summary update failed: {e}")
        final_summary = updated_summary or existing_summary

    return {
        "answer":          answer,
        "updated_summary": final_summary,
    }
