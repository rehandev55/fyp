import json
import time
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

# ── clients ───────────────────────────────────────────────────────────────────
pc            = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
INDEX_NAME    = os.getenv("PINECONE_INDEX", "eternal-sunshine")

CHUNKS_DIR      = Path("data/chunks")
EMBEDDING_MODEL = "text-embedding-3-small"
BATCH_SIZE      = 100

# ── create index if not exists ────────────────────────────────────────────────
def get_or_create_index():
    existing = [idx.name for idx in pc.list_indexes()]
    if INDEX_NAME not in existing:
        print(f"Creating index '{INDEX_NAME}' with 1536 dimensions...")
        pc.create_index(
            name      = INDEX_NAME,
            dimension = 1536,
            metric    = "cosine",
            spec      = ServerlessSpec(cloud="aws", region="us-east-1")
        )
        time.sleep(10)  # wait for index to be ready
        print("Index created.")
    else:
        print(f"Index '{INDEX_NAME}' already exists.")
    return pc.Index(INDEX_NAME)

index = get_or_create_index()
# ── step 1: get all IDs already in Pinecone ───────────────────────────────────
def get_pinecone_ids() -> set:
    """Fetch all vector IDs currently in Pinecone."""
    print("Fetching existing Pinecone IDs...")
    pinecone_ids = set()

    # list all IDs using pagination
    for ids_page in index.list():
        pinecone_ids.update(ids_page)

    print(f"Pinecone has {len(pinecone_ids)} vectors.")
    return pinecone_ids

# ── step 2: get all chunk IDs from local files ────────────────────────────────
def get_all_local_chunks() -> list[dict]:
    """Load all chunks from all jsonl files."""
    all_chunks = []
    for jsonl_path in CHUNKS_DIR.glob("*.jsonl"):
        with open(jsonl_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    all_chunks.append(json.loads(line))
    print(f"Local chunks total: {len(all_chunks)}")
    return all_chunks

# ── step 3: find missing chunks ───────────────────────────────────────────────
def find_missing(all_chunks: list, pinecone_ids: set) -> list:
    missing = [c for c in all_chunks if c["chunk_id"] not in pinecone_ids]
    print(f"Missing chunks: {len(missing)}")
    return missing

# ── step 4: embed and upload only missing ─────────────────────────────────────
def embed_and_upload_missing(missing_chunks: list):
    print(f"Embedding and uploading {len(missing_chunks)} missing chunks...")

    embedded = []
    for i, chunk in enumerate(missing_chunks, start=1):
        try:
            response = openai_client.embeddings.create(
                input = chunk["text"],
                model = EMBEDDING_MODEL
            )
            chunk["embedding"] = response.data[0].embedding
            embedded.append(chunk)
            print(f"  Embedded {i}/{len(missing_chunks)}")
            time.sleep(0.05)
        except Exception as e:
            print(f"  ERROR embedding {chunk['chunk_id']}: {e}")

    # upload in batches
    for i in range(0, len(embedded), BATCH_SIZE):
        batch = embedded[i:i + BATCH_SIZE]
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
                    "text":        item["text"][:1000]
                }
            })
        index.upsert(vectors=vectors)
        print(f"  Uploaded batch {i // BATCH_SIZE + 1} ({len(batch)} vectors)")
        time.sleep(0.5)

# ── main ──────────────────────────────────────────────────────────────────────
def main():
    pinecone_ids  = get_pinecone_ids()
    all_chunks    = get_all_local_chunks()
    missing       = find_missing(all_chunks, pinecone_ids)

    if not missing:
        print("Nothing missing. Pinecone is complete.")
        return

    embed_and_upload_missing(missing)

    # verify
    time.sleep(3)
    stats = index.describe_index_stats()
    print(f"\nDone. Pinecone total vectors: {stats.total_vector_count}")

if __name__ == "__main__":
    main()