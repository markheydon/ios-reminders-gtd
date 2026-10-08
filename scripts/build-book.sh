#!/usr/bin/env bash
# Build combined EPUB and PDF from docs/ chapters (see book/chapters.txt).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

BOOK_RELEASE="${BOOK_RELEASE:-0}"
if [[ "${1:-}" == "release" ]]; then
  BOOK_RELEASE=1
fi

if [[ "$BOOK_RELEASE" == "1" ]]; then
  BASENAME="reminders-gtd"
else
  BASENAME="reminders-gtd-draft"
fi

CHAPTERS_FILE="book/chapters.txt"
DIST_DIR="dist"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "error: required command not found: $1" >&2
    exit 1
  fi
}

require_cmd pandoc
require_cmd rsvg-convert
require_cmd python3
require_cmd xelatex

# Release workflow may override version via env (see book-release.yml).
METADATA_FILE="$TMP_DIR/metadata.yaml"
cp book/metadata.yaml "$METADATA_FILE"
if [[ -n "${BOOK_VERSION:-}" ]]; then
  python3 - "$BOOK_VERSION" "$METADATA_FILE" <<'PY'
import re, sys
version, path = sys.argv[1], sys.argv[2]
text = open(path, encoding="utf-8").read()
text = re.sub(r"^version:.*$", f"version: {version}", text, count=1, flags=re.M)
open(path, "w", encoding="utf-8").write(text)
PY
fi

while IFS= read -r chapter || [[ -n "$chapter" ]]; do
  chapter="${chapter%%#*}"
  chapter="${chapter// /}"
  [[ -z "$chapter" ]] && continue
  if [[ ! -f "$chapter" ]]; then
    echo "error: missing chapter file: $chapter" >&2
    exit 1
  fi
done < "$CHAPTERS_FILE"

PREPARED_DIR="$TMP_DIR/prepared"
mkdir -p "$PREPARED_DIR"

python3 - "$ROOT" "$CHAPTERS_FILE" "$PREPARED_DIR" <<'PY'
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
chapters_file = Path(sys.argv[2])
prepared_dir = Path(sys.argv[3])

def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text

prepared_dir.mkdir(parents=True, exist_ok=True)
paths = []
for line in chapters_file.read_text(encoding="utf-8").splitlines():
    line = line.split("#", 1)[0].strip()
    if not line:
        continue
    src = root / line
    rel_name = Path(line).name
    body = strip_front_matter(src.read_text(encoding="utf-8"))
    dest = prepared_dir / rel_name
    dest.write_text(body, encoding="utf-8")
    paths.append(dest)

manifest = prepared_dir / "chapters.manifest"
manifest.write_text("\n".join(str(p) for p in paths) + "\n", encoding="utf-8")
PY

mapfile -t CHAPTER_PATHS < "$PREPARED_DIR/chapters.manifest"

# PDF staging: rasterise SVG diagrams for LaTeX.
PDF_DOCS="$TMP_DIR/pdf-docs"
mkdir -p "$PDF_DOCS/images"
for chapter in "${CHAPTER_PATHS[@]}"; do
  cp "$chapter" "$PDF_DOCS/$(basename "$chapter")"
done
cp book/front-matter.md "$PDF_DOCS/front-matter.md"
PDF_FRONT_MATTER="$PDF_DOCS/front-matter.md"
for svg in docs/images/*.svg; do
  base="$(basename "$svg" .svg)"
  rsvg-convert -w 1200 "$svg" -o "$PDF_DOCS/images/${base}.png"
done

PDF_CHAPTER_PATHS=()
for chapter in "${CHAPTER_PATHS[@]}"; do
  PDF_CHAPTER_PATHS+=("$PDF_DOCS/$(basename "$chapter")")
done

python3 - "$PDF_DOCS" <<'PY'
import re
import sys
from pathlib import Path

pdf_docs = Path(sys.argv[1])
for md in pdf_docs.glob("*.md"):
    text = md.read_text(encoding="utf-8")
    text = re.sub(
        r"!\[([^\]]*)\]\(images/([^)]+\.)svg\)",
        r"![\1](images/\2png)",
        text,
    )
    md.write_text(text, encoding="utf-8")
PY

mkdir -p "$DIST_DIR"
EPUB_OUT="$DIST_DIR/${BASENAME}.epub"
PDF_OUT="$DIST_DIR/${BASENAME}.pdf"

PANDOC_COMMON=(
  -f markdown+smart
  --metadata-file="$METADATA_FILE"
  --toc
  --toc-depth=2
)

pandoc "${PANDOC_COMMON[@]}" \
  book/front-matter.md \
  "${CHAPTER_PATHS[@]}" \
  --resource-path=docs:book \
  --epub-cover-image=book/assets/cover.svg \
  -o "$EPUB_OUT"

pandoc "${PANDOC_COMMON[@]}" \
  "$PDF_FRONT_MATTER" \
  "${PDF_CHAPTER_PATHS[@]}" \
  --resource-path="$PDF_DOCS":book \
  --pdf-engine=xelatex \
  -H book/latex-header.tex \
  -o "$PDF_OUT"

echo "Wrote $EPUB_OUT"
echo "Wrote $PDF_OUT"
