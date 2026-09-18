"""
Evaluation step 1 — retrieval quality of the RAG pipeline.

Measures, against the live Pinecone index:
  * hit rate           - share of queries returning at least one chunk
  * similarity scores  - top-1 and mean top-k cosine similarity
  * keyword recall@k   - share of queries whose expected terms appear in the
                         retrieved text (a proxy for topical relevance)
  * filter precision   - share of returned chunks whose metadata actually
                         matches the board/class/subject filter that was asked
                         for. This is the structural guarantee the design rests
                         on, so it is measured rather than assumed.
  * isolation          - cross-class and cross-board leakage probes
  * latency            - wall-clock embed + query time, cold and cached

Run from the ai-service directory:
    venv\\Scripts\\python.exe scripts/eval_01_retrieval.py
"""

import json
import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, ".")

from rag.retriever import _index, embed_query, retrieve

OUT_DIR = Path("evaluation_results")
OUT_DIR.mkdir(exist_ok=True)

TOP_K = 5

# (query, board, class, subject, expected terms - any one counts as a hit)
QUERIES = [
    ("What is cell theory?", "federal", "class_11", "biology",
     ["cell", "theory", "schleiden", "schwann"]),
    ("Explain the structure and function of mitochondria",
     "federal", "class_11", "biology", ["mitochondri", "atp", "respiration"]),
    ("What is photosynthesis and where does it occur?",
     "federal", "class_11", "biology", ["photosynthes", "chlorophyll", "light"]),
    ("Describe the human digestive system",
     "federal", "class_12", "biology", ["digest", "stomach", "intestine"]),
    ("What is DNA replication?", "federal", "class_12", "biology",
     ["dna", "replicat", "nucleotide"]),
    ("Define homeostasis", "federal", "class_12", "biology",
     ["homeostasis", "internal", "regulat"]),

    ("What is an atom and what are its parts?",
     "federal", "class_9", "chemistry", ["atom", "electron", "proton", "nucleus"]),
    ("Explain ionic and covalent bonding",
     "federal", "class_10", "chemistry", ["ionic", "covalent", "bond", "electron"]),
    ("What is the periodic table and how is it arranged?",
     "federal", "class_11", "chemistry", ["periodic", "group", "period", "element"]),
    ("Define oxidation and reduction",
     "federal", "class_12", "chemistry", ["oxidat", "reduct", "electron"]),
    ("What are alkanes?", "federal", "class_12", "chemistry",
     ["alkane", "hydrocarbon", "carbon"]),

    ("State Newton's three laws of motion",
     "federal", "class_9", "physics", ["newton", "law", "motion", "force"]),
    ("What is the difference between speed and velocity?",
     "federal", "class_9", "physics", ["speed", "velocity", "direction"]),
    ("Explain Ohm's law", "federal", "class_10", "physics",
     ["ohm", "current", "voltage", "resistance"]),
    ("What is refraction of light?", "federal", "class_10", "physics",
     ["refract", "light", "medium"]),
    ("Define work, energy and power",
     "federal", "class_11", "physics", ["work", "energy", "power", "joule"]),
    ("What is simple harmonic motion?",
     "federal", "class_11", "physics", ["harmonic", "motion", "oscillat"]),
    ("Explain electromagnetic induction",
     "federal", "class_12", "physics", ["induct", "magnetic", "flux", "emf"]),

    ("What is a quadratic equation and how is it solved?",
     "federal", "class_9", "mathematics", ["quadratic", "equation", "root"]),
    ("Explain the properties of matrices",
     "federal", "class_10", "mathematics", ["matri", "row", "column"]),
    ("What is differentiation in calculus?",
     "federal", "class_12", "mathematics", ["differenti", "derivative", "function"]),
    ("Define a set and its types", "federal", "class_11", "mathematics",
     ["set", "element", "subset"]),

    ("What is an operating system?", "federal", "class_11", "computer",
     ["operating system", "software", "hardware"]),
    ("Explain the difference between RAM and ROM",
     "federal", "class_9", "computer", ["ram", "rom", "memory"]),
    ("What is a database management system?",
     "federal", "class_12", "computer", ["database", "dbms", "data"]),
    ("Describe network topologies", "federal", "class_12", "computer",
     ["topolog", "network", "star", "bus"]),

    ("What are the parts of speech in English grammar?",
     "federal", "class_9", "english", ["noun", "verb", "adjective", "speech"]),
    ("How do you write a formal letter?",
     "federal", "class_10", "english", ["letter", "formal", "address"]),
    ("Explain active and passive voice",
     "federal", "class_11", "english", ["active", "passive", "voice"]),
    ("What is a summary and how is it written?",
     "federal", "class_12", "english", ["summary", "paragraph", "main"]),
]

# Probes that must return nothing, or content that is not the other cohort's.
ISOLATION_PROBES = [
    # (description, query, board, class, subject)
    ("cross-board: AJK board filter on a Federal-only corpus",
     "What is cell theory?", "ajk", "class_11", "biology"),
    ("cross-board: AJK board filter, physics",
     "State Newton's laws of motion", "ajk", "class_9", "physics"),
    ("unpopulated cohort: class 9 biology",
     "What is a cell?", "federal", "class_9", "biology"),
]

# Same question asked under two different class filters — the returned text
# must differ, proving the filter (not the prompt) is doing the scoping.
CROSS_CLASS_PAIRS = [
    ("Explain the structure of an atom",
     "federal", "chemistry", "class_9", "class_12"),
    ("What is motion?", "federal", "physics", "class_9", "class_11"),
]


def run_query_set() -> list[dict]:
    rows = []
    for query, board, class_level, subject, expected in QUERIES:
        t0 = time.perf_counter()
        chunks = retrieve(query, board, class_level, subject, top_k=TOP_K)
        elapsed_ms = (time.perf_counter() - t0) * 1000

        scores = [c["score"] for c in chunks]
        blob = " ".join(c["text"] for c in chunks).lower()
        matched = [term for term in expected if term.lower() in blob]

        rows.append({
            "query": query,
            "board": board,
            "class": class_level,
            "subject": subject,
            "n_chunks": len(chunks),
            "top1_score": scores[0] if scores else 0.0,
            "mean_score": round(statistics.mean(scores), 4) if scores else 0.0,
            "expected_terms": expected,
            "matched_terms": matched,
            "keyword_hit": bool(matched),
            "latency_ms": round(elapsed_ms, 1),
            "types": sorted({c["type"] for c in chunks}),
        })
        flag = "OK " if matched else "MISS"
        print(f"  [{flag}] {subject:12} {class_level:9} "
              f"n={len(chunks)} top1={rows[-1]['top1_score']:.3f} "
              f"{elapsed_ms:6.0f}ms  {query[:44]}")
    return rows


def check_filter_precision() -> dict:
    """Every returned chunk must carry the metadata that was filtered on."""
    total = 0
    correct = 0
    violations = []
    for query, board, class_level, subject, _ in QUERIES[:12]:
        vector = embed_query(query)
        res = _index.query(
            vector=vector,
            top_k=TOP_K,
            filter={
                "board": {"$eq": board},
                "class": {"$eq": class_level},
                "subject": {"$eq": subject},
            },
            include_metadata=True,
        )
        for match in res.matches:
            total += 1
            md = match.metadata
            ok = (md.get("board") == board
                  and md.get("class") == class_level
                  and md.get("subject") == subject)
            if ok:
                correct += 1
            else:
                violations.append({
                    "asked": [board, class_level, subject],
                    "got": [md.get("board"), md.get("class"), md.get("subject")],
                })
    return {
        "chunks_checked": total,
        "chunks_matching_filter": correct,
        "precision": round(correct / total, 4) if total else 0.0,
        "violations": violations,
    }


def check_isolation() -> list[dict]:
    rows = []
    for label, query, board, class_level, subject in ISOLATION_PROBES:
        chunks = retrieve(query, board, class_level, subject, top_k=TOP_K)
        rows.append({
            "probe": label,
            "filter": f"{board}/{class_level}/{subject}",
            "chunks_returned": len(chunks),
            "leaked": len(chunks) > 0,
        })
        print(f"  {label:52} -> {len(chunks)} chunks")
    return rows


def check_cross_class() -> list[dict]:
    rows = []
    for query, board, subject, class_a, class_b in CROSS_CLASS_PAIRS:
        a = retrieve(query, board, class_a, subject, top_k=TOP_K)
        b = retrieve(query, board, class_b, subject, top_k=TOP_K)
        texts_a = {c["text"][:120] for c in a}
        texts_b = {c["text"][:120] for c in b}
        overlap = texts_a & texts_b
        rows.append({
            "query": query,
            "subject": subject,
            "class_a": class_a,
            "class_b": class_b,
            "n_a": len(a),
            "n_b": len(b),
            "identical_chunks": len(overlap),
            "disjoint": len(overlap) == 0,
        })
        print(f"  {subject:12} {class_a} vs {class_b}: "
              f"{len(a)} / {len(b)} chunks, {len(overlap)} shared")
    return rows


def measure_cache() -> dict:
    """Cold embed versus cached embed for an identical query string."""
    probe = "A distinctive cache probe query about thermodynamic equilibrium"
    t0 = time.perf_counter()
    embed_query(probe)
    cold_ms = (time.perf_counter() - t0) * 1000
    timings = []
    for _ in range(5):
        t0 = time.perf_counter()
        embed_query(probe)
        timings.append((time.perf_counter() - t0) * 1000)
    warm_ms = statistics.mean(timings)
    return {
        "cold_embed_ms": round(cold_ms, 2),
        "warm_embed_ms": round(warm_ms, 4),
        "speedup": round(cold_ms / warm_ms, 1) if warm_ms else None,
    }


def main() -> None:
    print("=" * 62)
    print("RAG RETRIEVAL EVALUATION")
    print("=" * 62)

    print(f"\n[1] Retrieval over {len(QUERIES)} curriculum queries (top_k={TOP_K})")
    rows = run_query_set()

    non_empty = [r for r in rows if r["n_chunks"] > 0]
    hits = [r for r in rows if r["keyword_hit"]]
    top1 = [r["top1_score"] for r in non_empty]
    means = [r["mean_score"] for r in non_empty]
    lat = [r["latency_ms"] for r in rows]

    summary = {
        "queries": len(rows),
        "hit_rate": round(len(non_empty) / len(rows), 4),
        "keyword_recall_at_k": round(len(hits) / len(rows), 4),
        "mean_top1_score": round(statistics.mean(top1), 4) if top1 else 0,
        "mean_topk_score": round(statistics.mean(means), 4) if means else 0,
        "min_top1_score": round(min(top1), 4) if top1 else 0,
        "max_top1_score": round(max(top1), 4) if top1 else 0,
        "mean_latency_ms": round(statistics.mean(lat), 1),
        "median_latency_ms": round(statistics.median(lat), 1),
        "p95_latency_ms": round(sorted(lat)[int(0.95 * len(lat)) - 1], 1),
    }

    print("\n[2] Metadata filter precision")
    filter_stats = check_filter_precision()
    print(f"  {filter_stats['chunks_matching_filter']}/"
          f"{filter_stats['chunks_checked']} chunks matched the requested "
          f"filter (precision = {filter_stats['precision']:.4f})")

    print("\n[3] Isolation probes (expected: 0 chunks)")
    isolation = check_isolation()

    print("\n[4] Cross-class separation (expected: disjoint chunk sets)")
    cross_class = check_cross_class()

    print("\n[5] Embedding cache")
    cache = measure_cache()
    print(f"  cold={cache['cold_embed_ms']:.1f} ms  "
          f"warm={cache['warm_embed_ms']:.4f} ms  "
          f"speedup={cache['speedup']}x")

    print("\n" + "=" * 62)
    print("SUMMARY")
    print("=" * 62)
    for k, v in summary.items():
        print(f"  {k:24} {v}")

    payload = {
        "config": {"top_k": TOP_K, "n_queries": len(QUERIES)},
        "summary": summary,
        "per_query": rows,
        "filter_precision": filter_stats,
        "isolation": isolation,
        "cross_class": cross_class,
        "cache": cache,
    }
    out = OUT_DIR / "retrieval_eval.json"
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"\nWritten: {out}")


if __name__ == "__main__":
    main()
