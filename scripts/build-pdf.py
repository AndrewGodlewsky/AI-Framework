#!/usr/bin/env python3
"""Cut the PDF versions of The AI Usage Spectrum from the committed HTML set.

    python scripts/build-pdf.py            # writes pdf/ai-usage-spectrum-YYYY-MM.pdf + one PDF per page
    python scripts/build-pdf.py --keep     # also keep the compiled HTML next to the PDFs, for inspection

What it does, in order:

1. Compiles the seven pages (hub, five archetypes in spectrum order, glossary) into one HTML
   document under a cover page, prefixing every id and internal link so anchors stay unique
   and cross-document links become in-document jumps.
2. Prints that compilation, and each page on its own, with headless Chrome — the @media print
   pass in style.css governs; Chrome keeps internal links live and writes a heading outline.
3. Stamps a running footer (document name, "Page N of M") on every page with pypdf.

Requirements: Google Chrome (or Chromium / Edge) on this machine, Python 3.10+, `pip install pypdf`.
Set CHROME=/path/to/chrome to override discovery. Nothing else; no network.

Page geometry lives in style.css (`@page { size: A4; ... }`). The fonts embedded are whatever the
build machine resolves the stylesheet's system stacks to — the stacks are system-only by design.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:  # pragma: no cover
    sys.exit("pypdf is required: pip install pypdf")

ROOT = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/AndrewGodlewsky/AI-Framework"

# Reading order for the compiled document: (file stem, footer/contents name, one-line reach).
DOCS = [
    ("index", "The spectrum", "the five archetypes at a glance"),
    ("autocomplete", "Autocomplete", "the open file; a human accepts every edit"),
    ("workspace", "Workspace", "the working tree, locally; nothing leaves without a human"),
    ("contributor", "Contributor", "the shared repository; a human merges every change"),
    ("committer", "Committer", "trunk, unread; a human still gates release"),
    ("operator", "Operator", "running production; the path is pre-authorised"),
    ("glossary", "Glossary", "the ruling vocabulary these documents are written in"),
]
SET_TITLE = "The AI Usage Spectrum"


# --------------------------------------------------------------------------- chrome

def find_chrome() -> str:
    env = os.environ.get("CHROME")
    if env and Path(env).exists():
        return env
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("No Chrome/Chromium/Edge found. Set CHROME=/path/to/chrome.")


def print_pdf(chrome: str, src: Path, out: Path, profile: Path) -> None:
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        f"--user-data-dir={profile}",
        "--no-pdf-header-footer",
        "--generate-pdf-document-outline",
        "--virtual-time-budget=1500",
        f"--print-to-pdf={out}",
        src.resolve().as_uri(),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if not out.exists() or out.stat().st_size == 0:
        sys.exit(f"Chrome produced no PDF for {src.name}:\n{res.stderr[-2000:]}")


# --------------------------------------------------------------------------- html compile

def read_page(stem: str) -> tuple[str, str]:
    """Return (inner HTML of <div class="page">, h1 text)."""
    text = (ROOT / f"{stem}.html").read_text(encoding="utf-8")
    start = text.index('<div class="page">')
    i = start + len('<div class="page">')
    depth = 1
    for m in re.finditer(r"<div\b|</div>", text[i:]):
        depth += 1 if m.group(0).startswith("<div") else -1
        if depth == 0:
            inner = text[i : i + m.start()]
            break
    else:
        sys.exit(f"{stem}.html: unbalanced <div class=\"page\">")
    h1 = re.search(r"<h1>(.*?)</h1>", inner, re.S)
    return inner, html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else stem


def localise(inner: str, stem: str, compiled: bool) -> str:
    """Rewrite ids and links so the fragment can live inside the compiled document."""
    stems = {d[0] for d in DOCS}

    # ADR and other repo-relative document links point at GitHub in a PDF.
    inner = re.sub(r'href="(docs/[^"]+)"', lambda m: f'href="{REPO_URL}/blob/main/{m.group(1)}"', inner)

    if compiled:
        inner = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{stem}-{m.group(1)}"', inner)
        inner = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{stem}-{m.group(1)}"', inner)

        def page_link(m: re.Match) -> str:
            target, frag = m.group(1), m.group(2)
            if target not in stems:
                return m.group(0)
            return f'href="#{target}-{frag}"' if frag else f'href="#doc-{target}"'

        inner = re.sub(r'href="([a-z]+)\.html(?:#([^"]+))?"', page_link, inner)

    # The hub's cards expand in place on screen; on paper they are simply open.
    inner = inner.replace("<details class=\"arch-card\"", "<details open class=\"arch-card\"")
    if stem == "index":
        old = ("Click an archetype to\n    see what it is made of; each links to a full, cited document.")
        new = ("Each archetype's summary card follows; each links to its full, cited document.")
        if old not in inner:
            sys.exit("index.html: the hub standfirst has changed; update the print rewrite in build-pdf.py")
        inner = inner.replace(old, new)
    return inner


def cover(build_date: dt.date) -> str:
    items = "\n".join(
        f'      <li><a href="#doc-{stem}">{name}</a><span>{reach}</span></li>'
        for stem, name, reach in DOCS
    )
    when = build_date.strftime("%-d %B %Y") if os.name != "nt" else build_date.strftime("%#d %B %Y")
    return f"""
<section class="cover">
  <p class="cover-kicker">A reference set, compiled {when}</p>
  <h1>{SET_TITLE}</h1>
  <p class="cover-sub">Five archetypes for how a professional development team works with AI,
  ordered by what the agent's output can reach with no human action in between. The documents
  describe rather than recommend: each archetype ends with the posture that fits it, and none is
  the goal state.</p>
  <ol class="cover-contents">
{items}
  </ol>
  <p class="cover-meta">Compiled from the HTML set committed at {REPO_URL}. Every claim carries a
  citation chip with its source, date and evidence tier; each document states when its sources
  were last verified. Vocabulary as of 2026-08-31; taxonomy ADR-0004.</p>
</section>
"""


def compile_set(build_date: dt.date) -> str:
    parts = [
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n",
        f"<title>{SET_TITLE}</title>\n<link rel=\"stylesheet\" href=\"style.css\">\n</head>\n",
        "<body class=\"compiled\">\n",
        cover(build_date),
    ]
    for stem, _name, _reach in DOCS:
        inner, _h1 = read_page(stem)
        parts.append(f'\n<article class="doc" id="doc-{stem}">\n<div class="page">{localise(inner, stem, True)}</div>\n</article>\n')
    parts.append("</body>\n</html>\n")
    return "".join(parts)


def single_page(stem: str) -> str:
    text = (ROOT / f"{stem}.html").read_text(encoding="utf-8")
    inner, _ = read_page(stem)
    return text.replace(inner, localise(inner, stem, False))


# --------------------------------------------------------------------------- footer stamp

# Helvetica advance widths (per 1000 em) for the characters the footer uses.
_W = {" ": 278, "P": 667, "a": 556, "g": 556, "e": 556, "o": 556, "f": 278}
_W.update({d: 556 for d in "0123456789"})


def _overlay(width: float, height: float, left: str, right: str) -> PdfReader:
    """A one-page PDF carrying the footer text, built by hand so no extra library is needed."""
    size = 8.0
    y = 11 * 72 / 25.4            # 11 mm up from the sheet edge
    x_left = 16 * 72 / 25.4       # the page's side margin
    right_w = sum(_W.get(c, 556) for c in right) / 1000 * size
    x_right = width - x_left - right_w

    def lit(s: str) -> bytes:
        b = s.encode("cp1252", "replace")
        return b.replace(b"\\", b"\\\\").replace(b"(", b"\\(").replace(b")", b"\\)")

    content = (
        b"BT /F1 %.1f Tf 0.45 g %.2f %.2f Td (" % (size, x_left, y) + lit(left) + b") Tj ET\n"
        b"BT /F1 %.1f Tf 0.45 g %.2f %.2f Td (" % (size, x_right, y) + lit(right) + b") Tj ET\n"
    )
    objs = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %.2f %.2f] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>" % (width, height),
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
        b"<< /Length %d >>\nstream\n" % len(content) + content + b"endstream",
    ]
    out = io.BytesIO()
    out.write(b"%PDF-1.4\n")
    offsets = []
    for n, body in enumerate(objs, start=1):
        offsets.append(out.tell())
        out.write(b"%d 0 obj\n" % n + body + b"\nendobj\n")
    xref = out.tell()
    out.write(b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1))
    for off in offsets:
        out.write(b"%010d 00000 n \n" % off)
    out.write(b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objs) + 1, xref))
    out.seek(0)
    return PdfReader(out)


def doc_ranges(reader: PdfReader, h1_to_name: dict[str, str]) -> list[tuple[int, str]]:
    """(first page index, footer name) for each document, from Chrome's heading outline."""
    starts = []
    for item in reader.outline:
        if isinstance(item, list):
            continue
        title = str(item.title).strip()
        if title in h1_to_name:
            starts.append((reader.get_destination_page_number(item), h1_to_name[title]))
    return sorted(starts)


def tidy_outline(writer: PdfWriter) -> None:
    """Chrome's heading outline copies the <h2> text verbatim: the section number runs into the
    title ("03What a human still gates") and some titles come through doubled. Make them read."""
    from pypdf.generic import NameObject, TextStringObject

    def fix(title: str) -> str:
        t = title.strip()
        half = len(t) // 2
        if len(t) % 2 == 0 and t[:half] == t[half:]:
            t = t[:half]
        m = re.match(r"^(\d\d)(?=\S)", t)
        if m:
            t = f"{m.group(1)} {t[2:]}"
            half = (len(t) - 3) // 2
            body = t[3:]
            if len(body) % 2 == 0 and body[:half] == body[half:]:
                t = t[:3] + body[:half]
        return t.lstrip("\u2014 ").strip()

    outlines = writer._root_object.get("/Outlines")
    if outlines is None:
        return

    def walk(node) -> None:
        item = node.get_object().get("/First")
        while item is not None:
            obj = item.get_object()
            if "/Title" in obj:
                obj[NameObject("/Title")] = TextStringObject(fix(str(obj["/Title"])))
            walk(obj)
            item = obj.get("/Next")

    walk(outlines)


def stamp(src: Path, dst: Path, names: list[tuple[int, str]], skip_first: bool) -> int:
    reader = PdfReader(src)
    writer = PdfWriter(clone_from=reader)
    total = len(writer.pages)
    for i, page in enumerate(writer.pages):
        if skip_first and i == 0:
            continue
        name = SET_TITLE
        for start, label in names:
            if i >= start:
                name = f"{SET_TITLE} \u2014 {label}" if label else SET_TITLE
        box = page.mediabox
        page.merge_page(_overlay(float(box.width), float(box.height), name, f"Page {i + 1} of {total}").pages[0])
    tidy_outline(writer)
    # Chrome writes one font subset per page; fold the duplicates and deflate the streams.
    for page in writer.pages:
        page.compress_content_streams()
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open("wb") as fh:
        writer.write(fh)
    return total


# --------------------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--outdir", default=str(ROOT / "pdf"))
    ap.add_argument("--date", help="YYYY-MM-DD to stamp instead of today")
    ap.add_argument("--keep", action="store_true", help="keep the compiled HTML next to the PDFs")
    args = ap.parse_args()

    build_date = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    tag = build_date.strftime("%Y-%m")
    outdir = Path(args.outdir)
    chrome = find_chrome()

    with tempfile.TemporaryDirectory(prefix="spectrum-pdf-") as tmp:
        build = Path(tmp)
        shutil.copy(ROOT / "style.css", build / "style.css")
        profile = build / "profile"

        # the compiled set
        compiled_html = build / "ai-usage-spectrum.html"
        compiled_html.write_text(compile_set(build_date), encoding="utf-8")
        raw = build / "ai-usage-spectrum.raw.pdf"
        print_pdf(chrome, compiled_html, raw, profile)
        h1_to_name = {read_page(stem)[1]: name for stem, name, _ in DOCS}
        h1_to_name[SET_TITLE] = ""  # the cover's own heading
        names = doc_ranges(PdfReader(raw), h1_to_name)
        dst = outdir / f"ai-usage-spectrum-{tag}.pdf"
        n = stamp(raw, dst, names, skip_first=True)
        print(f"{dst.relative_to(ROOT) if dst.is_relative_to(ROOT) else dst}  {n} pages  ({dst.stat().st_size // 1024} KB)")
        if args.keep:
            shutil.copy(compiled_html, outdir / f"ai-usage-spectrum-{tag}.html")

        # each page on its own
        for stem, name, _ in DOCS:
            src = build / f"{stem}.html"
            src.write_text(single_page(stem), encoding="utf-8")
            raw = build / f"{stem}.raw.pdf"
            print_pdf(chrome, src, raw, profile)
            dst = outdir / f"{stem}-{tag}.pdf"
            n = stamp(raw, dst, [(0, name)], skip_first=False)
            print(f"{dst.relative_to(ROOT) if dst.is_relative_to(ROOT) else dst}  {n} pages  ({dst.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
