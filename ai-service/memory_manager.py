import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ── tuneable knobs ─────────────────────────────────────────────────────────────
RAW_KEEP         = 4    # number of recent messages kept verbatim (2 exchanges)
SUMMARY_MAX_TOK  = 200  # max tokens for the stored summary
NEW_BATCH_SIZE   = 4    # how many "older" messages trigger an incremental update
# ──────────────────────────────────────────────────────────────────────────────

# Short filler phrases that carry no learning signal
_FILLER_PATTERNS = re.compile(
    r"^(ok|okay|thanks|thank you|got it|sure|yes|no|alright|"
    r"great|cool|nice|understood|i see|hmm+|oh|hi|hello|bye|"
    r"good|fine|perfect|sounds good|makes sense)[\s!.]*$",
    re.IGNORECASE,
)

def _is_low_value(msg: dict) -> bool:
    """
    Return True for messages that are not worth summarizing:
      - Very short filler phrases (greetings, confirmations, etc.)
      - Duplicate content already seen in the same batch
    """
    content = msg.get("content", "").strip()

    # 1. Regex filler match
    if _FILLER_PATTERNS.match(content):
        return True

    # 2. Too short to carry useful info (< 8 words)
    if len(content.split()) < 8:
        return True

    return False


def _filter_messages(messages: list) -> list:
    """Remove low-value messages and deduplicate consecutive duplicates."""
    filtered = []
    seen_contents = set()

    for msg in messages:
        content = msg.get("content", "").strip()

        if _is_low_value(msg):
            continue

        # Drop exact duplicate content within the same batch
        if content in seen_contents:
            continue

        seen_contents.add(content)
        filtered.append(msg)

    return filtered


def compress_history(
    chat_history:     list,
    existing_summary: str = "",
) -> dict:
    """
    Incrementally compress chat history.

    - Messages within RAW_KEEP are kept verbatim (no cost).
    - Messages outside RAW_KEEP that are NEW (not yet summarized) are filtered
      and folded into existing_summary with a single API call.
    - If nothing new needs summarizing, zero extra API calls are made.
    """

    # Not enough history to need compression yet
    if len(chat_history) <= RAW_KEEP:
        return {
            "summary":         existing_summary,
            "recent":          chat_history,
            "summary_updated": False,
        }

    older  = chat_history[:-RAW_KEEP]   # everything outside the raw window
    recent = chat_history[-RAW_KEEP:]   # kept verbatim

   
    if existing_summary:
        newly_older = older[-NEW_BATCH_SIZE:]
    else:
        newly_older = older  # first summarization — process everything

    # Filter noise before sending to the LLM
    meaningful = _filter_messages(newly_older)

    if not meaningful:
        # Nothing worth summarizing — reuse existing summary as-is
        return {
            "summary":         existing_summary,
            "recent":          recent,
            "summary_updated": False,
        }

    # ── ISSUE 1 FIX: incremental update, not full re-summarize ───────────────
    updated_summary = _update_summary(existing_summary, meaningful)

    return {
        "summary":         updated_summary,
        "recent":          recent,
        "summary_updated": True,
    }


def _update_summary(existing_summary: str, new_messages: list) -> str:
    """
    Fold `new_messages` into `existing_summary` with a single cheap API call.
    The prompt is tuned for educational context (not generic chat).
    """
    new_text = "\n".join(
        f"{m['role'].upper()}: {m['content']}" for m in new_messages
    )

    # Build the user content based on whether a prior summary exists
    if existing_summary:
        user_content = (
            f"EXISTING SUMMARY:\n{existing_summary}\n\n"
            f"NEW MESSAGES TO FOLD IN:\n{new_text}\n\n"
            "Update the summary to include the new messages."
        )
    else:
        user_content = (
            f"CONVERSATION:\n{new_text}\n\n"
            "Summarize this conversation."
        )

    
    system_content = """You are a memory assistant for an AI tutor.
Your job is to maintain a concise but informationally complete summary of a
student–tutor conversation.

Always capture:
1. Topics and subtopics covered so far
2. Student's demonstrated understanding level (strong / partial / weak)
3. Specific misconceptions or errors made, and whether they were corrected
4. Key explanations or analogies the tutor gave that the student found helpful
5. Any open questions or unfinished threads the student raised

Rules:
- Write 4–6 sentences maximum.
- Be specific (e.g. "Student confused velocity with speed; tutor clarified
  with a direction example") not vague ("student asked about motion").
- Never include greetings, small talk, or filler.
- Output plain text only — no bullet points, no headers."""

    response = client.chat.completions.create(
        model       = "gpt-4o-mini",
        max_tokens  = SUMMARY_MAX_TOK,
        temperature = 0,
        messages    = [
            {"role": "system",  "content": system_content},
            {"role": "user",    "content": user_content},
        ],
    )
    return response.choices[0].message.content.strip()

def build_messages_with_memory(
    system_prompt:    str,
    chat_history:     list,
    question:         str,
    existing_summary: str = "",
) -> tuple[list, str]:
    """
    Assembles the final OpenAI messages array and returns the (possibly updated)
    summary string so the caller can persist it.

    Returns:
        (messages_list, updated_summary_string)

    The caller (teacher_bot.py) should return updated_summary alongside the
    answer so Laravel can store it in the session/DB for the next request.
    """
    compressed = compress_history(chat_history, existing_summary)

    messages = [{"role": "system", "content": system_prompt}]

    # Inject summary as a lightweight system note
    if compressed["summary"]:
        messages.append({
            "role":    "system",
            "content": f"[Conversation so far]: {compressed['summary']}",
        })

    # Recent verbatim exchanges
    for msg in compressed["recent"]:
        messages.append({
            "role":    msg["role"],
            "content": msg["content"],
        })

    # Current turn
    messages.append({"role": "user", "content": question})

    return messages, compressed["summary"]