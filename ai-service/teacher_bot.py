import os
from dotenv import load_dotenv
from openai import OpenAI
from rag.retriever import retrieve, format_context, _openai_client as client
from memory_manager import build_messages_with_memory, _update_summary
from utils.token_logger import log_token_usage
from pathlib import Path

load_dotenv()

# read prompt once at startup
PROMPT_TEMPLATE = Path("prompts/teacher.txt").read_text(encoding="utf-8")

# max chars for search query to avoid Pinecone payload limits
MAX_SEARCH_QUERY_CHARS = 300


def get_teacher_response(
    question:         str,
    board:            str,
    class_level:      str,
    subject:          str,
    language:         str  = "en",
    chat_history:     list = None,   # None not [] — avoids mutable default bug
    existing_summary: str  = "",
) -> dict:

    # safe default
    if chat_history is None:
        chat_history = []

    # build focused search query — cap length to avoid dilution
    if existing_summary and len(question.split()) < 6:
        # short follow-up — prepend first sentence of summary for context
        summary_context = existing_summary.split(".")[0]
        search_query = f"{summary_context}. {question}"[:MAX_SEARCH_QUERY_CHARS]
    else:
        search_query = question[:MAX_SEARCH_QUERY_CHARS]

    chunks  = retrieve(
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

    log_token_usage(
        endpoint          = "chat",
        model             = "gpt-4o-mini",
        board             = board,
        class_level       = class_level,
        subject           = subject,
        prompt_tokens     = response.usage.prompt_tokens,
        completion_tokens = response.usage.completion_tokens,
    )

    # only update summary if there was actual content exchanged
    final_summary = updated_summary or existing_summary
    if answer and len(answer.split()) > 10:
        try:
            final_summary = _update_summary(
                existing_summary = updated_summary or existing_summary,
                new_messages     = [
                    {"role": "user",      "content": question},
                    {"role": "assistant", "content": answer},
                ]
            )
        except Exception as e:
            print(f"[WARNING] Summary update failed: {e}")

    return {
        "answer":          answer,
        "updated_summary": final_summary,
    }