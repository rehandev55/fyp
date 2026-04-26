import os
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv()

# ── clients ───────────────────────────────────────────────────────────────────
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc            = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index         = pc.Index(os.getenv("PINECONE_INDEX"))

EMBEDDING_MODEL = "text-embedding-3-small"

# ── embed the query ───────────────────────────────────────────────────────────
def embed_query(query: str) -> list[float]:
    """Convert student question into a vector."""
    response = openai_client.embeddings.create(
        input = query,
        model = EMBEDDING_MODEL
    )
    return response.data[0].embedding

# ── retrieve relevant chunks ──────────────────────────────────────────────────
def retrieve(
    query:   str,
    board:   str,
    class_level: str,
    subject: str,
    top_k:   int = 5
) -> list[dict]:
    """
    Query Pinecone with metadata filters.
    Only returns chunks matching the student's board, class, subject.
    """

    # embed the question
    query_vector = embed_query(query)

    # metadata filter — student only gets their own content
    metadata_filter = {
        "board":   {"$eq": board},
        "class":   {"$eq": class_level},
        "subject": {"$eq": subject}
    }

    # query pinecone
    results = index.query(
        vector          = query_vector,
        top_k           = top_k,
        filter          = metadata_filter,
        include_metadata = True
    )

    # extract chunks from results
    chunks = []
    for match in results.matches:
        chunks.append({
            "score":   round(match.score, 4),
            "text":    match.metadata.get("text", ""),
            "subject": match.metadata.get("subject", ""),
            "type":    match.metadata.get("type", ""),
            "chunk_index": match.metadata.get("chunk_index", 0)
        })

    return chunks

# ── format context for LLM ────────────────────────────────────────────────────
def format_context(chunks: list[dict]) -> str:
    """Join retrieved chunks into one context string for the LLM prompt."""
    if not chunks:
        return "No relevant content found."

    context_parts = []
    for i, chunk in enumerate(chunks, start=1):
        context_parts.append(
            f"[Excerpt {i} | Score: {chunk['score']}]\n{chunk['text']}"
        )

    return "\n\n---\n\n".join(context_parts)