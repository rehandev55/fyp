import os
import io
import json
import time
from pdf2image import convert_from_path
from pathlib import Path
from datetime import datetime
from google.cloud import vision

# ── config ────────────────────────────────────────────────────────────────────
POPPLER_PATH  = r"C:\poppler\Library\bin"
RAW_DIR       = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
LOG_FILE      = Path("data/extraction_log.txt")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# set google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google-credentials.json"

# initialize google vision client once
client = vision.ImageAnnotatorClient()

# ── logger ────────────────────────────────────────────────────────────────────
def log(msg: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

# ── google vision OCR ─────────────────────────────────────────────────────────
def ocr_page_with_google(page_image) -> str:
    """Send one page image to Google Cloud Vision and get text back."""
    try:
        # convert PIL image to PNG bytes
        img_byte_arr = io.BytesIO()
        page_image.save(img_byte_arr, format="PNG")
        img_content = img_byte_arr.getvalue()

        # send to google
        image    = vision.Image(content=img_content)
        response = client.text_detection(image=image)

        # check for errors
        if response.error.message:
            raise Exception(f"Google Vision error: {response.error.message}")

        # extract full text
        if response.full_text_annotation.text:
            return response.full_text_annotation.text
        else:
            return ""

    except Exception as e:
        log(f"    OCR error on page: {e}")
        return ""

# ── pdf processing ────────────────────────────────────────────────────────────
def extract_text_from_pdf(pdf_path: Path) -> list[str]:
    """Convert PDF pages to images then OCR each with Google Vision."""
    log(f"  Converting PDF to images (dpi=200)...")

    pages = convert_from_path(
        str(pdf_path),
        dpi=200,
        poppler_path=POPPLER_PATH
    )

    log(f"  Total pages: {len(pages)}")

    page_texts = []
    for i, page_image in enumerate(pages, start=1):
        log(f"  OCR page {i}/{len(pages)}...")

        text = ocr_page_with_google(page_image)
        page_texts.append(text)

        # small delay to avoid hitting API rate limits
        time.sleep(0.1)

    return page_texts

# ── metadata ──────────────────────────────────────────────────────────────────
def parse_path_metadata(pdf_path: Path) -> dict:
    """Extract board, class, subject, type from folder structure."""
    parts = pdf_path.parts
    # expected path: data/raw/{board}/{class}/{subject}/{type}/file.pdf
    return {
        "board":        parts[-5],
        "class":        parts[-4],
        "subject":      parts[-3],
        "type":         parts[-2],
        "filename":     pdf_path.name,
        "extracted_at": datetime.now().isoformat()
    }

# ── save output ───────────────────────────────────────────────────────────────
def save_processed(metadata: dict, page_texts: list[str], out_dir: Path):
    """Save extracted text and metadata as JSON."""
    name = (
        f"{metadata['board']}_"
        f"{metadata['class']}_"
        f"{metadata['subject']}_"
        f"{metadata['type']}"
    )
    out_path = out_dir / f"{name}.json"

    output = {
        "metadata":    metadata,
        "total_pages": len(page_texts),
        "pages": [
            {
                "page_number": i + 1,
                "text":        text,
                "char_count":  len(text)
            }
            for i, text in enumerate(page_texts)
        ]
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    log(f"  Saved → {out_path}")
    return out_path

# ── skip already processed ────────────────────────────────────────────────────
def is_already_processed(pdf_path: Path, out_dir: Path) -> bool:
    """Skip PDFs that were already extracted successfully."""
    parts = pdf_path.parts
    name = (
        f"{parts[-5]}_"
        f"{parts[-4]}_"
        f"{parts[-3]}_"
        f"{parts[-2]}.json"
    )
    return (out_dir / name).exists()

# ── quality check ─────────────────────────────────────────────────────────────
def check_extraction_quality(page_texts: list[str]) -> dict:
    """Basic quality report on extracted text."""
    total_chars  = sum(len(t) for t in page_texts)
    empty_pages  = sum(1 for t in page_texts if len(t.strip()) < 50)
    avg_chars    = total_chars // len(page_texts) if page_texts else 0

    return {
        "total_characters": total_chars,
        "empty_pages":      empty_pages,
        "avg_chars_per_page": avg_chars,
        "quality": "good" if avg_chars > 200 else "poor"
    }

# ── main ──────────────────────────────────────────────────────────────────────
def process_all_pdfs():
    pdf_files = list(RAW_DIR.rglob("*.pdf"))

    if not pdf_files:
        log("No PDFs found in data/raw/. Please add your PDFs first.")
        return

    log(f"Found {len(pdf_files)} PDF(s) to process.")
    log("=" * 60)

    success_count = 0
    error_count   = 0

    for pdf_path in pdf_files:
        # skip already processed
        if is_already_processed(pdf_path, PROCESSED_DIR):
            log(f"SKIPPING (already done): {pdf_path}")
            continue

        log(f"Starting: {pdf_path}")
        start_time = time.time()

        try:
            metadata   = parse_path_metadata(pdf_path)
            page_texts = extract_text_from_pdf(pdf_path)

            # quality check
            quality = check_extraction_quality(page_texts)
            log(f"  Quality: {quality}")

            # save
            save_processed(metadata, page_texts, PROCESSED_DIR)

            elapsed = round(time.time() - start_time, 1)
            log(f"  COMPLETED in {elapsed}s\n")
            success_count += 1

        except Exception as e:
            log(f"  ERROR: {e}\n")
            error_count += 1

    log("=" * 60)
    log(f"ALL DONE. Success: {success_count} | Errors: {error_count}")

# ── entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    process_all_pdfs()