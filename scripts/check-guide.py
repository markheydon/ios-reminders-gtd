#!/usr/bin/env python3
"""Structural and house-style checks for reader-facing guide files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
INDEX = DOCS / "index.md"
README = ROOT / "README.md"
CHAPTERS = ROOT / "book" / "chapters.txt"

INDEX_NAV_RE = re.compile(r"^\d+\.\s+\[[^\]]+\]\(([^)]+\.md)\)", re.MULTILINE)
README_NAV_RE = re.compile(r"^\d+\.\s+\[[^\]]+\]\((docs/[^)]+\.md)\)", re.MULTILINE)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#]+\.md)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")

READER_PATHS: list[Path] = [README, *sorted(DOCS.glob("*.md"))]


def fail(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def nav_targets(text: str, pattern: re.Pattern[str]) -> list[str]:
    return pattern.findall(text)


def normalise_doc_path(href: str) -> str:
    href = href.strip()
    if href.startswith("docs/"):
        return href
    return f"docs/{href}"


def check_nav_sync() -> None:
    index_text = INDEX.read_text(encoding="utf-8")
    readme_text = README.read_text(encoding="utf-8")
    index_order = [normalise_doc_path(p) for p in nav_targets(index_text, INDEX_NAV_RE)]
    readme_order = nav_targets(readme_text, README_NAV_RE)
    if not index_order:
        fail(f"no numbered navigation links found in {INDEX.relative_to(ROOT)}")
    if index_order != readme_order:
        fail(
            "README.md numbered list does not match docs/index.md:\n"
            f"  index:  {index_order}\n"
            f"  readme: {readme_order}"
        )


def check_chapters_sync() -> None:
    if not CHAPTERS.is_file():
        return
    index_text = INDEX.read_text(encoding="utf-8")
    expected = [normalise_doc_path(p) for p in nav_targets(index_text, INDEX_NAV_RE)]
    lines = []
    for line in CHAPTERS.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            lines.append(line.replace("\\", "/"))
    if lines != expected:
        fail(
            "book/chapters.txt does not match docs/index.md reading order:\n"
            f"  index:    {expected}\n"
            f"  chapters: {lines}"
        )


def check_no_em_dash() -> None:
    for path in READER_PATHS:
        text = path.read_text(encoding="utf-8")
        if "\u2014" in text:
            fail(f"em dash found in {path.relative_to(ROOT)} (use spaced hyphen instead)")


def check_md_links() -> None:
    for path in READER_PATHS:
        text = path.read_text(encoding="utf-8")
        base = path.parent
        for href in MD_LINK_RE.findall(text):
            href = href.strip()
            if href.startswith("http://") or href.startswith("https://"):
                continue
            target = (base / href).resolve()
            if not target.is_file():
                fail(f"broken markdown link in {path.relative_to(ROOT)}: {href}")


def check_images() -> None:
    for path in sorted(DOCS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for href in IMAGE_RE.findall(text):
            href = href.strip()
            if href.startswith("http://") or href.startswith("https://"):
                continue
            target = (path.parent / href).resolve()
            if not target.is_file():
                fail(f"broken image in {path.relative_to(ROOT)}: {href}")
    readme_text = README.read_text(encoding="utf-8")
    for href in IMAGE_RE.findall(readme_text):
        href = href.strip()
        if href.startswith("http://") or href.startswith("https://"):
            continue
        target = (ROOT / href).resolve()
        if not target.is_file():
            fail(f"broken image in README.md: {href}")


def main() -> None:
    check_nav_sync()
    check_chapters_sync()
    check_no_em_dash()
    check_md_links()
    check_images()
    print("check-guide: ok")


if __name__ == "__main__":
    main()
