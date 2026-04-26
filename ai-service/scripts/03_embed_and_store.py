import os
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec

# ── load env ──────────────────────────────────────────────────────────────────
load_dotenv()
OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX  = os.getenv("PINECONE_INDEX", "eternal-sunshine")

# ── config ────────────────────────────────────────────────────────────────────
CHUNKS_DIR      = Path("data/chunks")
EMBEDDING_MODEL = "text-embedding-3-small"  # 1536 dimensions, cheap and fast
BATCH_SIZE      = 100   # upload to pinecone in batches of 100
LOG_FILE        = Path("data/embedding_log.txt")

# ── clients ───────────────────────────────────────────────────────────────────
openai_client = OpenAI(api_key=OPENAI_API_KEY)
pc            = Pinecone(api_key=PINECONE_API_KEY)

# ── logger ────────────────────────────────────────────────────────────────────
def log(msg: str):
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

# ── pinecone setup ────────────────────────────────────────────────────────────
def setup_pinecone_index():
    """Create Pinecone index if it does not exist."""
    existing = [idx.name for idx in pc.list_indexes()]

    if PINECONE_INDEX not in existing:
        log(f"Creating Pinecone index: {PINECONE_INDEX}")
        pc.create_index(
            name      = PINECONE_INDEX,
            dimension = 1536,       # text-embedding-3-small output size
            metric    = "cosine",
            spec      = ServerlessSpec(cloud="aws", region="us-east-1")
        )
        # wait for index to be ready
        time.sleep(5)
        log("Index created successfully.")
    else:
        log(f"Index '{PINECONE_INDEX}' already exists. Using it.")

    return pc.Index(PINECONE_INDEX)

# ── embedding ─────────────────────────────────────────────────────────────────
def get_embedding(text: str) -> list[float]:
    """Get embedding vector from OpenAI for one chunk."""
    response = openai_client.embeddings.create(
        input = text,
        model = EMBEDDING_MODEL
    )
    return response.data[0].embedding

# ── upload to pinecone ────────────────────────────────────────────────────────
def upload_batch(index, batch: list[dict]):
    """Upload a batch of vectors to Pinecone."""
    vectors = []
    for item in batch:
        vectors.append({
            "id":     item["chunk_id"],
            "values": item["embedding"],
            "metadata": {
                "board":       item["board"],
                "class":       item["class"],
                "subject":     item["subject"],
                "type":        item["type"],
                "language":    item["language"],
                "chunk_index": item["chunk_index"],
                "text":        item["text"][:1000]  # pinecone metadata limit
            }
        })
    index.upsert(vectors=vectors)

# ── check already embedded ────────────────────────────────────────────────────
def load_embedded_ids() -> set:
    """Load chunk IDs that were already embedded — to allow resuming."""
    embedded_file = Path("data/embedded_ids.txt")
    if embedded_file.exists():
        with open(embedded_file, "r") as f:
            return set(line.strip() for line in f.readlines())
    return set()

def save_embedded_id(chunk_id: str):
    """Save a chunk ID as embedded so we can resume if interrupted."""
    with open("data/embedded_ids.txt", "a") as f:
        f.write(chunk_id + "\n")

# ── process one jsonl file ────────────────────────────────────────────────────
def process_file(jsonl_path: Path, index, embedded_ids: set) -> int:
    log(f"Processing: {jsonl_path.name}")

    chunks = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))

    log(f"  Total chunks: {len(chunks)}")

    chunks_to_embed = [c for c in chunks if c["chunk_id"] not in embedded_ids]
    del chunks  # free memory

    log(f"  Chunks to embed: {len(chunks_to_embed)} (skipping {len(chunks_to_embed)})")

    if not chunks_to_embed:
        log("  All chunks already embedded. Skipping.")
        return 0

    total_uploaded = 0
    batch_buffer   = []

    for i, chunk in enumerate(chunks_to_embed, start=1):
        try:
            embedding = get_embedding(chunk["text"])
            chunk["embedding"] = embedding
            batch_buffer.append(chunk)
            save_embedded_id(chunk["chunk_id"])

            if i % 50 == 0:
                log(f"  Embedded {i}/{len(chunks_to_embed)}...")

            # upload when batch is full
            if len(batch_buffer) >= BATCH_SIZE:
                upload_batch(index, batch_buffer)
                log(f"  Uploaded batch ({len(batch_buffer)} vectors)")
                total_uploaded += len(batch_buffer)
                batch_buffer = []  # clear batch from memory
                time.sleep(0.5)

            time.sleep(0.05)

        except Exception as e:
            log(f"  ERROR: {chunk['chunk_id']}: {e}")
            continue

    # upload remaining
    if batch_buffer:
        upload_batch(index, batch_buffer)
        log(f"  Uploaded final batch ({len(batch_buffer)} vectors)")
        total_uploaded += len(batch_buffer)

    return total_uploaded

# ── main ──────────────────────────────────────────────────────────────────────
def main():
    log("=" * 60)
    log("Starting embedding and Pinecone upload")
    log(f"Model: {EMBEDDING_MODEL}")
    log(f"Index: {PINECONE_INDEX}")
    log("=" * 60)

    # setup pinecone
    index = setup_pinecone_index()

    # load already embedded IDs for resuming
    embedded_ids = load_embedded_ids()
    log(f"Already embedded: {len(embedded_ids)} chunks")

    # get all chunk files
    jsonl_files = list(CHUNKS_DIR.glob("*.jsonl"))
    if not jsonl_files:
        log("No chunk files found in data/chunks/")
        return

    log(f"Found {len(jsonl_files)} book(s) to embed.")

    # process each book
    total_uploaded = 0
    for jsonl_path in jsonl_files:
        count = process_file(jsonl_path, index, embedded_ids)
        total_uploaded += count

    # final stats
    log("=" * 60)
    log(f"ALL DONE. Total vectors uploaded: {total_uploaded}")

    # show pinecone index stats
    stats = index.describe_index_stats()
    log(f"Pinecone index total vectors: {stats.total_vector_count}")
    log("=" * 60)

if __name__ == "__main__":
    main()