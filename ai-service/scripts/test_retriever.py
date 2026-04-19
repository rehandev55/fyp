import sys
sys.path.append(".")

from rag.retriever import retrieve, format_context

# test query
query   = "What is a cell and what are its basic functions?"
board   = "federal"
class_level = "class_11"
subject = "biology"

print(f"Query: {query}")
print(f"Filter: {board} | {class_level} | {subject}")
print("=" * 60)

chunks = retrieve(query, board, class_level, subject, top_k=3)

print(f"Retrieved {len(chunks)} chunks:\n")
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i} — Score: {chunk['score']}")
    print(chunk['text'][:300])
    print("---")