import os
from dotenv import load_dotenv
from openai import OpenAI
from rag.retriever import retrieve, format_context
from pathlib import Path

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# load prompt template
PROMPT_TEMPLATE = Path("prompts/teacher.txt").read_text(encoding="utf-8")

def get_teacher_response(
    question:    str,
    board:       str,
    class_level: str,
    subject:     str,
    language:    str = "en"
) -> str:
    """Get AI teacher explanation for a student question."""

    # step 1 — retrieve relevant chunks
    chunks = retrieve(
        query       = question,
        board       = board,
        class_level = class_level,
        subject     = subject,
        top_k       = 5
    )

    # step 2 — format context
    context = format_context(chunks)

    # step 3 — build prompt
    prompt = PROMPT_TEMPLATE.format(
        board       = board,
        class_level = class_level,
        context     = context,
        question    = question
    )

    # step 4 — call LLM
    response = client.chat.completions.create(
        model    = "gpt-4o-mini",   # fast and cheap for teacher bot
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user",   "content": question}
        ],
        temperature = 0.3,          # low temp = focused, factual answers
        max_tokens  = 1000
    )

    return response.choices[0].message.content