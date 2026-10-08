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
BOOK_FRONT_MATTER = ROOT / "book" / "front-matter.md"

INDEX_NAV_RE = re.compile(r"^\d+\.\s+\[[^\]]+\]\(([^)]+\.md)\)", re.MULTILINE)
README_NAV_RE = re.compile(r"^\d+\.\s+\[[^\]]+\]\((docs/[^)]+\.md)\)", re.MULTILINE)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#]+\.md)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")

READER_PATHS: list[Path] = [README, *sorted(DOCS.glob("*.md"))]
if BOOK_FRONT_MATTER.is_file():
    READER_PATHS.append(BOOK_FRONT_MATTER)


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


def chapter_basenames() -> set[str]:
    if not CHAPTERS.is_file():
        return set()
    names: set[str] = set()
    for line in CHAPTERS.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            names.add(Path(line).name)
    return names


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
        fail(f"missing {CHAPTERS.relative_to(ROOT)}")
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


def resolve_md_link(path: Path, href: str) -> Path:
    href = href.strip()
    if path == BOOK_FRONT_MATTER and not href.startswith("docs/"):
        return (DOCS / Path(href).name).resolve()
    if path == README and href.startswith("docs/"):
        return (ROOT / href).resolve()
    return (path.parent / href).resolve()


def check_md_links() -> None:
    allowed_chapters = chapter_basenames()
    for path in READER_PATHS:
        text = path.read_text(encoding="utf-8")
        for href in MD_LINK_RE.findall(text):
            href = href.strip()
            if href.startswith("http://") or href.startswith("https://"):
                continue
            target = resolve_md_link(path, href)
            if not target.is_file():
                fail(f"broken markdown link in {path.relative_to(ROOT)}: {href}")
            if path.parent == DOCS and allowed_chapters:
                name = Path(href).name
                if name not in allowed_chapters:
                    fail(
                        f"markdown link in {path.relative_to(ROOT)} targets {href}, "
                        "which is not listed in book/chapters.txt (offline export would omit it)"
                    )
            if path == BOOK_FRONT_MATTER and allowed_chapters:
                name = Path(href).name
                if name not in allowed_chapters:
                    fail(
                        f"markdown link in {BOOK_FRONT_MATTER.relative_to(ROOT)} targets {href}, "
                        "which is not listed in book/chapters.txt (offline export would omit it)"
                    )


def resolve_image_path(path: Path, href: str) -> Path:
    href = href.strip()
    if path == BOOK_FRONT_MATTER and href.startswith("images/"):
        return (DOCS / href).resolve()
    if path == README:
        return (ROOT / href).resolve()
    return (path.parent / href).resolve()


def check_images() -> None:
    for path in sorted(DOCS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for href in IMAGE_RE.findall(text):
            href = href.strip()
            if href.startswith("http://") or href.startswith("https://"):
                continue
            target = resolve_image_path(path, href)
            if not target.is_file():
                fail(f"broken image in {path.relative_to(ROOT)}: {href}")
    readme_text = README.read_text(encoding="utf-8")
    for href in IMAGE_RE.findall(readme_text):
        href = href.strip()
        if href.startswith("http://") or href.startswith("https://"):
            continue
        target = resolve_image_path(README, href)
        if not target.is_file():
            fail(f"broken image in README.md: {href}")
    if BOOK_FRONT_MATTER.is_file():
        text = BOOK_FRONT_MATTER.read_text(encoding="utf-8")
        for href in IMAGE_RE.findall(text):
            href = href.strip()
            if href.startswith("http://") or href.startswith("https://"):
                continue
            target = resolve_image_path(BOOK_FRONT_MATTER, href)
            if not target.is_file():
                fail(f"broken image in {BOOK_FRONT_MATTER.relative_to(ROOT)}: {href}")


def main() -> None:
    check_nav_sync()
    check_chapters_sync()
    check_no_em_dash()
    check_md_links()
    check_images()
    print("check-guide: ok")


if __name__ == "__main__":
    main()
