"""
Build the final year project report.

The document is produced in two passes. The first pass lays out the whole
report with the contents lists left empty, and renders it to PDF with
LibreOffice. The rendered PDF is then read back and each heading, figure
caption and table caption is located by its own text, which gives the page it
falls on. The second pass rebuilds the document with those page numbers
written into the contents, the list of figures and the list of tables, and
renders the final PDF.

Body page numbers are stable between the passes because Chapter 1 restarts
page numbering at 1 in its own section, so the length of the front matter
cannot shift them.

    python thesis/build.py            build both passes and export the PDF
    python thesis/build.py --fast     first pass only, no rendering, no PDF
"""

import os
import re
import shutil
import subprocess
import tempfile
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import content_back
import content_ch1
import content_ch2
import content_ch3
import content_ch4
import content_ch5
import content_ch6
import content_ch7
import content_ch8
import content_ch9
import content_front
from pypdf import PdfReader

from docx_kit import Counter, front_matter_section, new_document, new_section, render

OUT_DIR = os.path.join(ROOT, "thesis", "out")
DRAFT = os.path.join(OUT_DIR, "_pass1.docx")
FINAL = os.path.join(OUT_DIR, "Eternal_Sunshine_FYP_Report.docx")
PDF = os.path.join(OUT_DIR, "Eternal_Sunshine_FYP_Report.pdf")

CHAPTERS = [
    ("Chapter 01", content_ch1),
    ("Chapter 02", content_ch2),
    ("Chapter 03", content_ch3),
    ("Chapter 04", content_ch4),
    ("Chapter 05", content_ch5),
    ("Chapter 06", content_ch6),
    ("Chapter 07", content_ch7),
    ("Chapter 08", content_ch8),
    ("Chapter 09", content_ch9),
]


def _split_back_matter():
    """Split the back matter into one run of blocks per h1, so that each can be
    given its own section and running header."""
    groups, current, header = [], [], "References"
    for block in content_back.BLOCKS:
        if block[0] == "h1" and current:
            groups.append((header, current))
            current = []
        if block[0] == "h1":
            title = block[1]
            header = ("References" if title.startswith("REFERENCES")
                      else title.split(":")[0].title())
        current.append(block)
    if current:
        groups.append((header, current))
    return groups


def build_document(toc=None, lof=None, lot=None, front=None):
    doc = new_document()
    front_matter_section(doc)
    content_front.build(doc, toc, lof, lot, front)

    counters = Counter()
    index = []

    for header, module in CHAPTERS:
        new_section(doc, header_text=header, numbering="decimal",
                    start=1, restart=(header == "Chapter 01"))
        render(doc, module.BLOCKS, counters, index)

    for header, blocks in _split_back_matter():
        new_section(doc, header_text=header, numbering="decimal")
        render(doc, blocks, counters, index)

    return doc, index


# ── LibreOffice interop ──────────────────────────────────────────────────────
SOFFICE_CANDIDATES = [
    r"C:\Program Files\LibreOffice\program\soffice.exe",
    r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
    "/usr/bin/soffice",
    "soffice",
]


def find_soffice():
    for candidate in SOFFICE_CANDIDATES:
        if os.path.isabs(candidate):
            if os.path.exists(candidate):
                return candidate
        elif shutil.which(candidate):
            return shutil.which(candidate)
    raise RuntimeError(
        "LibreOffice was not found. Install it, or run with --fast to skip "
        "page-number resolution and PDF export.")


def render_pdf(docx_path, out_dir, target=None):
    """Render a .docx to PDF with LibreOffice and return the PDF path.

    The conversion writes into a scratch directory first and the result is
    then moved into place. LibreOffice aborts the whole conversion if the
    destination file is open in a viewer, and rendering to a scratch path
    keeps that failure at the final move, where it can be reported clearly
    instead of losing the render.
    """
    soffice = find_soffice()
    scratch = tempfile.mkdtemp(prefix="thesis-pdf-", dir=out_dir)
    try:
        result = subprocess.run(
            [soffice, "--headless", "--norestore", "--convert-to", "pdf",
             "--outdir", scratch, os.path.abspath(docx_path)],
            capture_output=True, timeout=900, text=True,
        )
        produced = os.path.join(
            scratch,
            os.path.splitext(os.path.basename(docx_path))[0] + ".pdf")
        if not os.path.exists(produced):
            raise RuntimeError(
                f"LibreOffice produced no PDF for {docx_path}\n"
                f"{result.stdout}\n{result.stderr}")

        destination = target or os.path.join(
            out_dir, os.path.basename(produced))
        try:
            os.replace(produced, destination)
        except OSError as exc:
            raise RuntimeError(
                f"Could not write {destination}: {exc}. The file is most "
                f"likely open in a PDF viewer - close it and run the build "
                f"again.") from exc
        return destination
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


_ROMAN = [(1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"),
          (90, "xc"), (50, "l"), (40, "xl"), (10, "x"), (9, "ix"),
          (5, "v"), (4, "iv"), (1, "i")]


def roman(n):
    """Lower-case roman numeral, as used for the front-matter page numbers."""
    out = []
    for value, glyph in _ROMAN:
        while n >= value:
            out.append(glyph)
            n -= value
    return "".join(out)


#: Front-matter pages listed inside CONTENTS, located by their heading text.
FRONT_PAGES = [
    ("fm_lof", "LISTOFFIGURES"),
    ("fm_lot", "LISTOFTABLES"),
    ("fm_abbrev", "LISTOFABBREVIATIONS"),
    ("fm_ack", "ACKNOWLEDGMENTS"),
    ("fm_abstract", "ABSTRACT"),
]


def heading_of(pages, i, folio):
    """The text of page `i` with its printed page number removed.

    The PDF text layer emits the footer before the body, so a front-matter
    page reads "XXABSTRACT...". Stripping exactly the folio that page must
    carry lets a heading be recognised by what follows it, without the false
    matches that a loose substring search would produce - "LIST OF FIGURES"
    also occurs part-way down the contents page.
    """
    text = pages[i]
    return text[len(folio):] if text.startswith(folio) else text


def resolve_front(pages, body_start):
    """Roman page numbers for the front-matter rows of the contents. The cover
    is page i, so a page's number is its position in the document."""
    found = {}
    for key, anchor in FRONT_PAGES:
        for i in range(body_start):
            if heading_of(pages, i, roman(i + 1).upper()).startswith(anchor):
                found[key] = roman(i + 1)
                break
    return found


def _norm(text):
    """Collapse text to letters and digits, so that line breaks, tab stops and
    punctuation cannot affect a match."""
    return re.sub(r"[^A-Z0-9]", "", (text or "").upper())


def _anchor(entry):
    """The text that identifies an indexed item on the page it appears on.

    A chapter's contents line reads "1.  INTRODUCTION" while the page itself
    carries only the title, so such entries supply their own anchor."""
    if entry.get("anchor"):
        return _norm(entry["anchor"])
    if entry["kind"] == "toc":
        return _norm(entry["text"])
    label = "FIGURE" if entry["kind"] == "lof" else "TABLE"
    return _norm(f'{label} {entry["number"]} {entry["caption"]}')[:90]


def resolve_pages(pdf_path, index):
    """Locate every indexed item in the rendered PDF and return its printed
    page number. Body pages restart at 1 on the first page of Chapter 1, so
    the printed number is the offset from that page."""
    reader = PdfReader(pdf_path)
    pages = [_norm(page.extract_text()) for page in reader.pages]

    # The abstract is the last page of the front matter; Chapter 1 opens on
    # the next page, whose text begins with its title once the folio "1" is
    # removed.
    abstract = next(
        (i for i in range(len(pages))
         if heading_of(pages, i, roman(i + 1).upper()).startswith("ABSTRACT")),
        None)
    if abstract is None:
        raise RuntimeError("could not locate the ABSTRACT page")
    first_body = next(
        (i for i in range(abstract + 1, len(pages))
         if heading_of(pages, i, "1").startswith("INTRODUCTION")), None)
    if first_body is None:
        raise RuntimeError("could not locate the first page of Chapter 1")

    resolved, unresolved = {}, []
    for entry in index:
        anchor = _anchor(entry)
        if not anchor:
            unresolved.append(entry)
            continue
        # A chapter or appendix always opens a page, so it is located by the
        # page it starts. Matching anywhere on the page would otherwise catch
        # a cross-reference such as "Chapter 2, Literature Review" in the
        # chapter-organisation list of Section 1.9.
        opens = entry.get("opens_page")
        for i in range(first_body, len(pages)):
            folio = str(i - first_body + 1)
            found = (heading_of(pages, i, folio).startswith(anchor) if opens
                     else anchor in pages[i])
            if found:
                resolved[entry["key"]] = i - first_body + 1
                break
        else:
            unresolved.append(entry)
    front = resolve_front(pages, first_body)
    return resolved, unresolved, len(reader.pages), front


#: Clause openers that begin an explanatory tail. Everything from the marker
#: onwards is dropped, because a list entry needs to name the figure, not
#: describe it.
_TAIL_MARKERS = [
    " showing ", " covering ", " including ", " that converts ",
    ", showing", ", covering", ", including", ", with ", ", its ",
    ", as baselined", ", and the ", " — ", ": ",
]
_SHORT_LIMIT = 64
_MIN_HEAD = 12


def short_caption(caption):
    """A compact form of a figure or table caption, for the contents lists.

    The supervisor asked for short names in the List of Figures and the List
    of Tables. The full caption still appears beneath the figure or above the
    table; only the list entry is condensed. The caption is reduced to its
    first sentence, any explanatory tail clause is dropped, and what remains
    is trimmed on a word boundary. No ellipsis is added, so every entry reads
    as a complete name.
    """
    text = caption.strip().rstrip(".")
    text = re.sub(r"\s*\((?:n\s*=|abridged|Data Flow)[^)]*\)", "", text)
    text = text.split(". ")[0].strip()
    for marker in _TAIL_MARKERS:
        head = text.split(marker)[0].strip()
        if len(head) >= _MIN_HEAD:
            text = head
    if len(text) > _SHORT_LIMIT:
        text = text[:_SHORT_LIMIT].rsplit(" ", 1)[0]
    return text.rstrip(" ,;:-—")


def split_index(index, pages):
    toc, lof, lot = [], [], []
    for entry in index:
        page = pages.get(entry["key"])
        if page is None:
            continue
        if entry["kind"] == "toc":
            toc.append({"level": entry["level"], "text": entry["text"],
                        "caps": entry["caps"], "bold": entry["bold"],
                        "page": str(page)})
        elif entry["kind"] == "lof":
            lof.append({"number": entry["number"],
                        "caption": short_caption(entry["caption"]),
                        "page": str(page)})
        elif entry["kind"] == "lot":
            lot.append({"number": entry["number"],
                        "caption": short_caption(entry["caption"]),
                        "page": str(page)})
    return toc, lof, lot


def main():
    fast = "--fast" in sys.argv
    os.makedirs(OUT_DIR, exist_ok=True)

    print("pass 1: laying out the report")
    doc, index = build_document()
    doc.save(DRAFT)
    print(f"  {len(index)} indexed items -> {os.path.relpath(DRAFT, ROOT)}")

    if fast:
        shutil.copy(DRAFT, FINAL)
        print(f"  --fast: copied to {os.path.relpath(FINAL, ROOT)}")
        return

    # Body page numbers cannot move, because Chapter 1 restarts numbering in
    # its own section. The roman numbers of the front matter can move, because
    # adding rows to the contents changes how many pages the contents fills,
    # so the layout is re-derived until those numbers stop changing.
    toc = lof = lot = None
    front = {}
    source = DRAFT
    for attempt in range(1, 5):
        label = "pass 1b" if attempt == 1 else f"pass {attempt}b"
        print(f"{label}: rendering to read page numbers back")
        rendered = render_pdf(source, OUT_DIR)
        pages, unresolved, total, new_front = resolve_pages(rendered, index)
        os.path.exists(rendered) and os.remove(rendered)
        print(f"  {total} pages; resolved {len(pages)}/{len(index)} items; "
              f"front matter {len(new_front)}/{len(FRONT_PAGES)}")
        if unresolved:
            print(f"  {len(unresolved)} could not be located:")
            for entry in unresolved[:10]:
                name = entry.get("text") or (
                    f'{entry.get("number")} {entry.get("caption", "")}')
                print(f"    - {entry['kind']}: {name[:66]}")

        toc, lof, lot = split_index(index, pages)
        if new_front == front and attempt > 1:
            print("  front-matter numbering is stable")
            break
        front = new_front
        print(f"  rebuilding with contents {len(toc)}, figures {len(lof)}, "
              f"tables {len(lot)}")
        doc, index = build_document(toc, lof, lot, front)
        doc.save(FINAL)
        source = FINAL
    else:
        print("  warning: front-matter numbering did not settle")

    print("rendering the final PDF")
    render_pdf(FINAL, OUT_DIR, target=PDF)
    print(f"  -> {os.path.relpath(FINAL, ROOT)}")
    print(f"  -> {os.path.relpath(PDF, ROOT)}")


if __name__ == "__main__":
    main()
