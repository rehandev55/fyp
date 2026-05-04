import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# reuse singleton client
from rag.retriever import _openai_client as client

RAW_KEEP        = 4
SUMMARY_MAX_TOK = 200
NEW_BATCH_SIZE  = 4
MIN_WORDS_TO_SUMMARIZE = 8

_FILLER_PATTERNS = re.compile(
    r"^(ok|okay|thanks|thank you|got it|sure|yes|no|alright|"
    r"great|cool|nice|understood|i see|hmm+|oh|hi|hello|bye|"
    r"good|fine|perfect|sounds good|makes sense)[\s!.]*$",
    re.IGNORECASE,
)

# system prompt built once at module load — not rebuilt every call
_SUMMARY_SYSTEM_PROMPT = """You are a memory assistant for an AI tutor.
Maintain a concise summary of a student-tutor conversation.
Capture: topics covered, student understanding level, misconceptions,
helpful explanations, open questions.
Rules: 4-6 sentences max. Be specific not vague. No greetings or filler.
Plain text only."""


def _is_low_value(msg: dict) -> bool:
    content = msg.get("content", "").strip()
    if _FILLER_PATTERNS.match(content):
        return True
    if len(content.split()) < MIN_WORDS_TO_SUMMARIZE:
        return True
    return False


def _filter_messages(messages: list) -> list:
    """Remove low-value messages. O(n) single pass."""
    seen = set()
    result = []
    for msg in messages:
        content = msg.get("content", "").strip()
        if _is_low_value(msg):
            continue
        if content in seen:
            continue
        seen.add(content)
        result.append(msg)
    return result


def compress_history(
    chat_history:     list,
    existing_summary: str = "",
) -> dict:
    if len(chat_history) <= RAW_KEEP:
        return {
            "summary":         existing_summary,
            "recent":          chat_history,
            "summary_updated": False,
        }

    older  = chat_history[:-RAW_KEEP]
    recent = chat_history[-RAW_KEEP:]
    newly_older = older[-NEW_BATCH_SIZE:] if existing_summary else older
    meaningful  = _filter_messages(newly_older)

    if not meaningful:
        return {
            "summary":         existing_summary,
            "recent":          recent,
            "summary_updated": False,
        }

    updated_summary = _update_summary(existing_summary, meaningful)
    return {
        "summary":         updated_summary,
        "recent":          recent,
        "summary_updated": True,
    }


def _update_summary(existing_summary: str, new_messages: list) -> str:
    """Single API call to update summary. Reuses singleton client."""
    new_text = "\n".join(
        f"{m['role'].upper()}: {m['content']}" for m in new_messages
    )

    if existing_summary:
        user_content = (
            f"EXISTING SUMMARY:\n{existing_summary}\n\n"
            f"NEW MESSAGES:\n{new_text}\n\n"
            "Update the summary to include the new messages."
        )
    else:
        user_content = f"CONVERSATION:\n{new_text}\n\nSummarize this."

    response = client.chat.completions.create(
        model       = "gpt-4o-mini",
        max_tokens  = SUMMARY_MAX_TOK,
        temperature = 0,
        messages    = [
            {"role": "system", "content": _SUMMARY_SYSTEM_PROMPT},
            {"role": "user",   "content": user_content},
        ],
    )
    return response.choices[0].message.content.strip()


def build_messages_with_memory(
    system_prompt:    str,
    chat_history:     list,
    question:         str,
    existing_summary: str = "",
) -> tuple[list, str]:
    compressed = compress_history(chat_history, existing_summary)

    messages = [{"role": "system", "content": system_prompt}]

    if compressed["summary"]:
        messages.append({
            "role":    "system",
            "content": f"[Conversation so far]: {compressed['summary']}",
        })

    messages.extend(compressed["recent"])
    messages.append({"role": "user", "content": question})

    return messages, compressed["summary"]