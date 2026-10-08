#!/usr/bin/env python3
"""Structural and house-style checks for reader-facing guide files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDE_ROOT = ROOT / "guide"
INDEX = GUIDE_ROOT / "_index.md"
README = ROOT / "README.md"
CHAPTERS = ROOT / "book" / "chapters.txt"
BOOK_FRONT_MATTER = ROOT / "book" / "front-matter.md"
STATIC_IMAGES = GUIDE_ROOT / "images"

INDEX_NAV_RE = re.compile(r"^\d+\.\s+\[[^\]]+\]\(([^)]+\.md)\)", re.MULTILINE)
README_NAV_RE = re.compile(r"^\d+\.\s+\[[^\]]+\]\((guide/[^)]+\.md)\)", re.MULTILINE)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#]+\.md)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def guide_markdown_files() -> list[Path]:
    return sorted(GUIDE_ROOT.glob("*.md"))


READER_PATHS: list[Path] = [README, *guide_markdown_files()]
if BOOK_FRONT_MATTER.is_file():
    READER_PATHS.append(BOOK_FRONT_MATTER)


def fail(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def nav_targets(text: str, pattern: re.Pattern[str]) -> list[str]:
    return pattern.findall(text)


def normalise_doc_path(href: str) -> str:
    href = href.strip().replace("\\", "/")
    if href.startswith("guide/"):
        return href
    return f"guide/{href}"


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
            "README.md numbered list does not match guide/_index.md:\n"
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
            "book/chapters.txt does not match guide/_index.md reading order:\n"
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
    if href.startswith("http://") or href.startswith("https://"):
        return path
    if path == BOOK_FRONT_MATTER:
        if href.startswith("guide/"):
            return (ROOT / href).resolve()
        name = Path(href).name
        for chapter in guide_markdown_files():
            if chapter.name == name:
                return chapter.resolve()
        return (GUIDE_ROOT / href).resolve()
    if path == README and href.startswith("guide/"):
        return (ROOT / href).resolve()
    if href.startswith("guide/"):
        return (ROOT / href).resolve()
    return (path.parent / href).resolve()


def is_under_guide(path: Path) -> bool:
    try:
        path.resolve().relative_to(GUIDE_ROOT.resolve())
        return True
    except ValueError:
        return False


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
            if is_under_guide(path) and allowed_chapters:
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
    if href.startswith("http://") or href.startswith("https://"):
        return path
    if href.startswith("images/"):
        return (STATIC_IMAGES / href.removeprefix("images/")).resolve()
    if path == BOOK_FRONT_MATTER and href.startswith("images/"):
        return (STATIC_IMAGES / href.removeprefix("images/")).resolve()
    if path == README:
        if href.startswith("guide/images/"):
            return (ROOT / href).resolve()
    return (path.parent / href).resolve()


def check_images() -> None:
    for path in guide_markdown_files():
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
