"""
Evaluation step 0 — inventory of the Pinecone vector index.

Reports the total vector count and the distribution of chunks across the
board / class / subject / document-type metadata that the retrieval filter
uses. Results feed Table 7.x (corpus composition) of the project report.

Run from the ai-service directory:
    venv\\Scripts\\python.exe scripts/eval_00_index_inventory.py
"""

import json
import os
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, ".")

from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

OUT_DIR = Path("evaluation_results")
OUT_DIR.mkdir(exist_ok=True)

BOARDS = ["federal", "ajk"]
CLASSES = ["class_9", "class_10", "class_11", "class_12"]
SUBJECTS = [
    "biology", "chemistry", "physics", "mathematics",
    "computer", "english", "urdu",
]
DOC_TYPES = ["textbook", "keybook", "past_papers"]


def main() -> None:
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index_name = os.getenv("PINECONE_INDEX")
    index = pc.Index(index_name)

    stats = index.describe_index_stats()
    stats_dict = stats.to_dict() if hasattr(stats, "to_dict") else dict(stats)

    print("=" * 62)
    print("PINECONE INDEX INVENTORY")
    print("=" * 62)
    print(f"Index name      : {index_name}")
    print(f"Dimension       : {stats_dict.get('dimension')}")
    print(f"Total vectors   : {stats_dict.get('total_vector_count'):,}")
    print(f"Index fullness  : {stats_dict.get('index_fullness')}")
    print()

    # A zero vector is a legal query vector for a pure metadata count probe.
    dim = int(stats_dict.get("dimension") or 1536)
    zero = [0.0] * dim

    def count(metadata_filter: dict) -> int:
        """Upper-bounded count of vectors matching a metadata filter."""
        res = index.query(
            vector=zero,
            top_k=10_000,
            filter=metadata_filter,
            include_metadata=False,
        )
        return len(res.matches)

    rows = []
    print("── Chunks per board / class / subject ──────────────────────")
    for board in BOARDS:
        for class_level in CLASSES:
            for subject in SUBJECTS:
                n = count({
                    "board": {"$eq": board},
                    "class": {"$eq": class_level},
                    "subject": {"$eq": subject},
                })
                if n:
                    rows.append({
                        "board": board,
                        "class": class_level,
                        "subject": subject,
                        "chunks": n,
                    })
                    print(f"  {board:8} {class_level:9} {subject:12} {n:6,}")

    print()
    print("── Chunks per document type ────────────────────────────────")
    type_rows = []
    for doc_type in DOC_TYPES:
        n = count({"type": {"$eq": doc_type}})
        type_rows.append({"type": doc_type, "chunks": n})
        print(f"  {doc_type:14} {n:6,}")

    by_board = Counter()
    by_class = Counter()
    by_subject = Counter()
    for r in rows:
        by_board[r["board"]] += r["chunks"]
        by_class[r["class"]] += r["chunks"]
        by_subject[r["subject"]] += r["chunks"]

    print()
    print("── Totals ──────────────────────────────────────────────────")
    print(f"  populated (board, class, subject) combinations : {len(rows)}")
    print(f"  by board   : {dict(by_board)}")
    print(f"  by class   : {dict(by_class)}")
    print(f"  by subject : {dict(by_subject)}")

    payload = {
        "index_name": index_name,
        "stats": stats_dict,
        "combinations": rows,
        "doc_types": type_rows,
        "by_board": dict(by_board),
        "by_class": dict(by_class),
        "by_subject": dict(by_subject),
    }
    out = OUT_DIR / "index_inventory.json"
    out.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print(f"\nWritten: {out}")


if __name__ == "__main__":
    main()
