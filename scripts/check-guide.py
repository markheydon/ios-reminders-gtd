#!/usr/bin/env python3
"""Structural and house-style checks for reader-facing guide files.

README numbered list matches book/chapters.txt (export order).
guide/_index.md Quick Start + Read the Full Guide must link each chapter once.
"""

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


def chapters_file_order() -> list[str]:
    if not CHAPTERS.is_file():
        fail(f"missing {CHAPTERS.relative_to(ROOT)}")
    lines: list[str] = []
    for line in CHAPTERS.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            lines.append(line.replace("\\", "/"))
    return lines


def check_readme_chapters_sync() -> None:
    readme_text = README.read_text(encoding="utf-8")
    readme_order = nav_targets(readme_text, README_NAV_RE)
    expected = chapters_file_order()
    if not readme_order:
        fail("no numbered navigation links found in README.md")
    if readme_order != expected:
        fail(
            "README.md numbered list does not match book/chapters.txt:\n"
            f"  readme:   {readme_order}\n"
            f"  chapters: {expected}"
        )


def check_index_covers_chapters() -> None:
    index_text = INDEX.read_text(encoding="utf-8")
    index_hrefs = [normalise_doc_path(p) for p in nav_targets(index_text, INDEX_NAV_RE)]
    if not index_hrefs:
        fail(f"no numbered navigation links found in {INDEX.relative_to(ROOT)}")
    expected = chapters_file_order()
    expected_names = {Path(p).name for p in expected}
    index_names = [Path(p).name for p in index_hrefs]
    if len(index_names) != len(set(index_names)):
        fail(
            f"duplicate chapter link in {INDEX.relative_to(ROOT)} navigation: {index_hrefs}"
        )
    if set(index_names) != expected_names:
        fail(
            "guide/_index.md Quick Start + Read the Full Guide must list each chapter once:\n"
            f"  index:    {sorted(index_names)}\n"
            f"  expected: {sorted(expected_names)}"
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
    check_readme_chapters_sync()
    check_index_covers_chapters()
    check_no_em_dash()
    check_md_links()
    check_images()
    print("check-guide: ok")


if __name__ == "__main__":
    main()
