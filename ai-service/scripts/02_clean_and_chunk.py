import json
import re
from pathlib import Path
from datetime import datetime

# ── config ────────────────────────────────────────────────────────────────────
PROCESSED_DIR = Path("data/processed")
CHUNKS_DIR    = Path("data/chunks")
CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

CHUNK_SIZE    = 700   # target tokens per chunk (approx 1 token = 4 chars)
CHUNK_OVERLAP = 100   # overlap between chunks to preserve context

# ── text cleaning ─────────────────────────────────────────────────────────────
def clean_text(text: str) -> str:
    """Remove noise from OCR extracted text."""

    # remove excessive whitespace and blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)

    # remove page numbers standing alone on a line (e.g. just "7" or "42")
    text = re.sub(r'^\s*\d{1,3}\s*$', '', text, flags=re.MULTILINE)

    # remove common header/footer patterns
    text = re.sub(r'National Book Foundation\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Chapter \d+:.*?\n', '', text)
    text = re.sub(r'www\.\S+', '', text)

    # remove lines that are too short to be useful (less than 3 chars)
    lines = text.split('\n')
    lines = [l for l in lines if len(l.strip()) >= 3]
    text = '\n'.join(lines)

    # final strip
    text = text.strip()

    return text


def is_mostly_urdu(text: str) -> bool:
    """Detect if text is primarily Urdu/Arabic script."""
    urdu_chars = len(re.findall(r'[\u0600-\u06FF]', text))
    total_chars = len(text.replace(' ', ''))
    if total_chars == 0:
        return False
    return (urdu_chars / total_chars) > 0.4


# ── chunking ──────────────────────────────────────────────────────────────────
def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping chunks by character count."""

    # approximate: 1 token ≈ 4 characters
    char_size    = chunk_size * 4
    char_overlap = overlap * 4

    chunks = []
    start  = 0

    while start < len(text):
        end = start + char_size

        # try to break at a sentence boundary (. or \n) near the end
        if end < len(text):
            # look back up to 200 chars for a good break point
            break_point = text.rfind('\n', start, end)
            if break_point == -1 or (end - break_point) > 200:
                break_point = text.rfind('. ', start, end)
            if break_point != -1:
                end = break_point + 1

        chunk = text[start:end].strip()

        if len(chunk) > 100:  # skip very small chunks
            chunks.append(chunk)

        start = end - char_overlap  # overlap for context continuity

    return chunks


# ── process one book ──────────────────────────────────────────────────────────
def process_book(json_path: Path) -> int:
    """Clean, chunk and save one extracted book. Returns chunk count."""

    print(f"\nProcessing: {json_path.name}")

    with open(json_path, "r", encoding="utf-8") as f:
        book = json.load(f)

    metadata = book["metadata"]

    # combine all pages into one text block
    full_text = ""
    for page in book["pages"]:
        page_text = page.get("text", "").strip()
        if page_text:
            full_text += f"\n{page_text}"

    # detect language
    language = "ur" if is_mostly_urdu(full_text) else "en"
    print(f"  Language detected: {language}")
    print(f"  Total characters: {len(full_text)}")

    # clean
    cleaned_text = clean_text(full_text)
    print(f"  After cleaning: {len(cleaned_text)} characters")

    # chunk
    chunks = chunk_text(cleaned_text)
    print(f"  Total chunks: {len(chunks)}")

    # build chunk records with full metadata
    chunk_records = []
    for i, chunk in enumerate(chunks):
        record = {
            "chunk_id": (
                f"{metadata['board']}_"
                f"{metadata['class']}_"
                f"{metadata['subject']}_"
                f"{metadata['type']}_"
                f"{i:04d}"
            ),
            "board":    metadata["board"],
            "class":    metadata["class"],
            "subject":  metadata["subject"],
            "type":     metadata["type"],
            "language": language,
            "chunk_index": i,
            "total_chunks": len(chunks),
            "char_count": len(chunk),
            "text": chunk
        }
        chunk_records.append(record)

    # save as JSONL (one chunk per line — easy to stream later)
    out_name = (
        f"{metadata['board']}_"
        f"{metadata['class']}_"
        f"{metadata['subject']}_"
        f"{metadata['type']}.jsonl"
    )
    out_path = CHUNKS_DIR / out_name

    with open(out_path, "w", encoding="utf-8") as f:
        for record in chunk_records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"  Saved → {out_path}")
    return len(chunks)


# ── main ──────────────────────────────────────────────────────────────────────
def main():
    json_files = list(PROCESSED_DIR.glob("*.json"))

    if not json_files:
        print("No extracted JSON files found in data/processed/")
        return

    print(f"Found {len(json_files)} extracted book(s).")

    total_chunks = 0
    skipped      = 0

    for json_path in json_files:
        # skip if already chunked
        out_name = json_path.stem + ".jsonl"
        if (CHUNKS_DIR / out_name).exists():
            print(f"SKIPPING (already chunked): {json_path.name}")
            skipped += 1
            continue

        count = process_book(json_path)
        total_chunks += count

    print(f"\n{'='*50}")
    print(f"ALL DONE.")
    print(f"Skipped:       {skipped} (already chunked)")
    print(f"Newly chunked: {total_chunks} chunks created")
    print(f"Chunks saved in: {CHUNKS_DIR}")


if __name__ == "__main__":
    main()