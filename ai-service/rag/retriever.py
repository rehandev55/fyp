import os
import hashlib
import functools
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv()

# ── singleton clients — created ONCE, reused forever ──────────────────────────
_openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
_pc            = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
_index         = _pc.Index(os.getenv("PINECONE_INDEX"))

EMBEDDING_MODEL = "text-embedding-3-small"

# ── embedding cache — avoids re-embedding identical queries ───────────────────
# LRU cache: keeps last 256 unique queries in memory
# cost: ~256 × 1536 floats × 4 bytes = ~1.5 MB — acceptable
@functools.lru_cache(maxsize=256)
def _embed_cached(text: str) -> tuple:
    """Embed text and cache result. Returns tuple (hashable for lru_cache)."""
    response = _openai_client.embeddings.create(
        input = text,
        model = EMBEDDING_MODEL
    )
    return tuple(response.data[0].embedding)


def embed_query(text: str) -> list[float]:
    """Public interface — returns list for Pinecone compatibility."""
    # normalize text before caching to improve cache hit rate
    normalized = text.strip().lower()
    return list(_embed_cached(normalized))


def retrieve(
    query:       str,
    board:       str,
    class_level: str,
    subject:     str,
    top_k:       int = 5,
    doc_type:    str = None,   # optional type filter
) -> list[dict]:
    """
    Single retrieve function handles both normal and type-filtered retrieval.
    Eliminates duplicate retrieve_by_type function in tester_bot.
    """
    query_vector = embed_query(query)

    # build filter — only add type if specified
    metadata_filter = {
        "board":   {"$eq": board},
        "class":   {"$eq": class_level},
        "subject": {"$eq": subject},
    }
    if doc_type:
        metadata_filter["type"] = {"$eq": doc_type}

    results = _index.query(
        vector           = query_vector,
        top_k            = top_k,
        filter           = metadata_filter,
        include_metadata = True
    )

    chunks = [
        {
            "score":       round(m.score, 4),
            "text":        m.metadata.get("text", ""),
            "subject":     m.metadata.get("subject", ""),
            "type":        m.metadata.get("type", ""),
            "chunk_index": m.metadata.get("chunk_index", 0),
        }
        for m in results.matches
        if m.score >= 0.3   # skip low confidence results
    ]

    return chunks


def retrieve_combined(
    query:       str,
    board:       str,
    class_level: str,
    subject:     str,
) -> str:
    """
    Retrieve from textbook and past papers in ONE embed call.
    Old code embedded query twice — this saves one API call per tester request.
    """
    # embed once — reused for both queries via cache
    textbook_chunks    = retrieve(query, board, class_level, subject,
                                  top_k=4, doc_type="textbook")
    past_paper_chunks  = retrieve(query, board, class_level, subject,
                                  top_k=3, doc_type="past_papers")

    # deduplicate by text content
    seen_texts = set()
    all_chunks = []
    for chunk in textbook_chunks + past_paper_chunks:
        text_key = chunk["text"][:100]
        if text_key not in seen_texts:
            seen_texts.add(text_key)
            all_chunks.append(chunk)

    return format_context(all_chunks)


def format_context(chunks: list[dict]) -> str:
    if not chunks:
        return "No relevant content found."
    parts = [
        f"[Excerpt {i} | Score: {c['score']}]\n{c['text']}"
        for i, c in enumerate(chunks, start=1)
    ]
    return "\n\n---\n\n".join(parts)