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

    # remove page numbers standing alone on a line
    text = re.sub(r'^\s*\d{1,3}\s*$', '', text, flags=re.MULTILINE)

    # remove common header/footer patterns
    text = re.sub(r'National Book Foundation\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Chapter \d+:.*?\n', '', text)
    text = re.sub(r'www\.\S+', '', text)

    # remove bullet point symbols
    text = re.sub(r'[⚫●•○■□◆◇►▶]+', '', text)

    # remove repeated OCR artifacts
    text = re.sub(r'(o{2,}|O{2,})', '', text)

    # remove standalone symbols
    text = re.sub(r'[©■●•●○]+', '', text)

    # keybook watermark patterns
    text = re.sub(r'studyplusplus\.com', '', text, flags=re.IGNORECASE)
    text = re.sub(r'study\+\+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'S\+\+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'www\.studyplusplus\.com', '', text, flags=re.IGNORECASE)
    text = re.sub(r'ILMI STARS', '', text, flags=re.IGNORECASE)
    text = re.sub(r'spreading the light', '', text, flags=re.IGNORECASE)

    # remove lines shorter than 3 chars
    lines = text.split('\n')
    lines = [l for l in lines if len(l.strip()) >= 3]
    text = '\n'.join(lines)

    return text.strip()


def clean_past_paper(text: str) -> str:
    """
    Deep cleaning specifically for past paper text.
    Removes exam header noise and restructures questions cleanly.
    """

    # remove roll number boxes and related text
    text = re.sub(r'ROLL\s*NUMBER.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Roll\s*No\.?.*?\n', '', text, flags=re.IGNORECASE)

    # remove page references
    text = re.sub(r'Page\s*\d+\s*of\s*\d+.*?\n', '', text, flags=re.IGNORECASE)

    # remove exam header boilerplate
    text = re.sub(r'INTERMEDIATE.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'FEDERAL.*?EDUCATION.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'SECONDARY.*?EDUCATION.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'ISLAMABAD.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Time allowed:.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Total Marks.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'NOTE:.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Note:.*?\n', '', text, flags=re.IGNORECASE)

    # remove section headers but keep the questions
    text = re.sub(r'SECTION[\s\-]*[ABC].*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Attempt any.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Answer any.*?\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'All parts carry equal marks.*?\n', '', text, flags=re.IGNORECASE)

    # remove paper codes and serial numbers
    text = re.sub(r'-?\d+HA-[I|II]*\s*\d+\s*HA-', '', text)
    text = re.sub(r'\d+HA\w*', '', text)

    # remove marks indicators like (14 x 3 = 42)
    text = re.sub(r'\(\d+\s*x\s*\d+\s*=\s*\d+\)', '', text)

    # remove standalone roman numerals on their own line
    text = re.sub(r'^\s*[IVXivx]+\s*$', '', text, flags=re.MULTILINE)

    # remove MCQ option garbage like "о о III о оо"
    text = re.sub(r'[оoО]\s*[оoО]\s*[оoО]', '', text)
    text = re.sub(r'^\s*[оoО\s]+$', '', text, flags=re.MULTILINE)

    # remove concept map garbage (short disconnected lines)
    text = re.sub(r'^\s*.{1,20}\s*$', lambda m:
        m.group() if any(c.isalpha() for c in m.group()) and
        len(m.group().strip()) > 8 else '',
        text, flags=re.MULTILINE
    )

    # clean up excessive blank lines created by removals
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()

def is_mostly_urdu(text: str) -> bool:
    """Detect if text is primarily Urdu/Arabic script."""
    urdu_chars = len(re.findall(r'[\u0600-\u06FF]', text))
    total_chars = len(text.replace(' ', ''))
    if total_chars == 0:
        return False
    return (urdu_chars / total_chars) > 0.4

def fix_line_breaks(text: str) -> str:
    lines = text.split("\n")
    fixed = []

    buffer = ""

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # if line continues previous sentence
        if buffer and not buffer.endswith(('.', ':', '?')):
            buffer += " " + line
        else:
            if buffer:
                fixed.append(buffer)
            buffer = line

    if buffer:
        fixed.append(buffer)

    return "\n".join(fixed)
# ── chunking ──────────────────────────────────────────────────────────────────
def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping chunks by character count."""

    char_size    = chunk_size * 4    # 700 * 4 = 2800 chars
    char_overlap = overlap * 4       # 100 * 4 = 400 chars
    step         = char_size - char_overlap  # 2800 - 400 = 2400 chars

    # safety check
    if step <= 0:
        step = char_size

    chunks   = []
    text_len = len(text)
    start    = 0

    while start < text_len:
        end = min(start + char_size, text_len)

        # try to break at sentence boundary
        if end < text_len:
            break_point = text.rfind('\n', start, end)
            if break_point == -1 or (end - break_point) > 200:
                break_point = text.rfind('. ', start, end)
            if break_point != -1 and break_point > start:
                end = break_point + 1

        chunk = text[start:end].strip()

        if len(chunk) > 100:
            chunks.append(chunk)

        # always move forward by step — prevents infinite loop
        start += step

        # hard safety — if we somehow didn't move forward, force it
        if start >= text_len:
            break

    return chunks
# ── process one book ──────────────────────────────────────────────────────────
def process_book(json_path: Path) -> int:
    """Clean, chunk and save one extracted book. Returns chunk count."""

    print(f"\nProcessing: {json_path.name}")

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            book = json.load(f)
    except Exception as e:
        print(f"  ERROR reading file: {e}")
        return 0

    metadata = book["metadata"]
    doc_type = metadata.get("type", "")

    # combine all pages into one text block
    full_text = ""
    for page in book["pages"]:
        page_text = page.get("text", "").strip()
        if page_text:
            full_text += f"\n{page_text}"

    # free pages from memory immediately
    del book

    # detect language
    language = "ur" if is_mostly_urdu(full_text) else "en"
    print(f"  Language detected: {language}")
    print(f"  Total characters: {len(full_text)}")

    # clean
    cleaned_text = clean_text(full_text)
    del full_text  # free memory

    if doc_type == "past_papers":
        cleaned_text = clean_past_paper(cleaned_text)
        print(f"  Applied past paper deep cleaning")

    cleaned_text = fix_line_breaks(cleaned_text)
    print(f"  After cleaning: {len(cleaned_text)} characters")

    # get clean filename
    clean_filename = Path(metadata['filename']).stem
    clean_filename = re.sub(r'[^\w\-_]', '_', clean_filename)
    clean_filename = re.sub(r'_+', '_', clean_filename).strip('_')

    # output file
    out_name = (
        f"{metadata['board']}_"
        f"{metadata['class']}_"
        f"{metadata['subject']}_"
        f"{metadata['type']}_"
        f"{clean_filename}.jsonl"
    )
    out_path = CHUNKS_DIR / out_name

    # chunk and write directly to file — no collecting in memory
    chunks = chunk_text(cleaned_text)
    del cleaned_text  # free memory

    print(f"  Total chunks: {len(chunks)}")

    chunk_count = 0
    with open(out_path, "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks):
            record = {
                "chunk_id": (
                    f"{metadata['board']}_"
                    f"{metadata['class']}_"
                    f"{metadata['subject']}_"
                    f"{metadata['type']}_"
                    f"{clean_filename}_"
                    f"{i:04d}"
                ),
                "board":        metadata["board"],
                "class":        metadata["class"],
                "subject":      metadata["subject"],
                "type":         metadata["type"],
                "language":     language,
                "chunk_index":  i,
                "total_chunks": len(chunks),
                "char_count":   len(chunk),
                "text":         chunk
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            chunk_count += 1

    del chunks  # free memory

    print(f"  Saved → {out_path}")
    return chunk_count

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