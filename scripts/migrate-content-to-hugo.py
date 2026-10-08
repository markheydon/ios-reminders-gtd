#!/usr/bin/env python3
"""Legacy: migrate docs/*.md into nested website/content (superseded by guide/ layout)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DOCS = ROOT / "docs"
DEST_CONTENT = ROOT / "website" / "content"

# Reading order and Hugo sidebar sections (editorial finding 4).
CHAPTERS: list[tuple[str, str, int, str]] = [
    # (basename, section folder, weight, title from first # line)
    ("why.md", "start", 10, "Why this is worth doing"),
    ("model.md", "start", 20, "The model"),
    ("setup.md", "start", 30, "Set it up on your iPhone or iPad"),
    ("capture-and-clarify.md", "daily", 10, "Capture and clarify"),
    ("do-the-work.md", "daily", 20, "Do the work"),
    ("projects.md", "daily", 30, "Projects, waiting, and someday"),
    ("weekly-review.md", "maintain", 10, "The weekly review"),
    ("examples.md", "maintain", 20, "A worked week"),
    ("advanced.md", "more", 10, "Optional extras"),
    ("limits.md", "more", 20, "What Reminders will not do"),
]

SECTION_META = {
    "start": ("Start", 10),
    "daily": ("Daily", 20),
    "maintain": ("Maintain", 30),
    "more": ("More", 40),
}

BASENAME_TO_REL: dict[str, str] = {
    name: f"docs/{section}/{name}" for name, section, _, _ in CHAPTERS
}


def strip_jekyll_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


def strip_leading_h1(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return "\n".join(lines) + "\n"


def rewrite_md_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label, href = match.group(1), match.group(2)
        if href.startswith("http"):
            return match.group(0)
        base = Path(href).name
        if base in BASENAME_TO_REL:
            return f"[{label}]({BASENAME_TO_REL[base]})"
        return match.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)#]+\.md)\)", repl, text)


def main() -> None:
    DEST_CONTENT.mkdir(parents=True, exist_ok=True)
    (DEST_CONTENT / "docs").mkdir(exist_ok=True)

    for section, (title, weight) in SECTION_META.items():
        section_dir = DEST_CONTENT / "docs" / section
        section_dir.mkdir(parents=True, exist_ok=True)
        index = section_dir / "_index.md"
        index.write_text(
            f"---\nbookCollapseSection: true\nweight: {weight}\ntitle: {title}\n---\n",
            encoding="utf-8",
        )

    for basename, section, weight, title in CHAPTERS:
        src = SRC_DOCS / basename
        body = strip_jekyll_front_matter(src.read_text(encoding="utf-8"))
        body = strip_leading_h1(body)
        body = rewrite_md_links(body)
        slug = basename.removesuffix(".md")
        front = (
            f"---\n"
            f"title: \"{title}\"\n"
            f"weight: {weight}\n"
            f"---\n\n"
        )
        dest = DEST_CONTENT / "docs" / section / basename
        dest.write_text(front + body, encoding="utf-8")

    # Home page
    index_src = SRC_DOCS / "index.md"
    body = strip_jekyll_front_matter(index_src.read_text(encoding="utf-8"))
    body = strip_leading_h1(body)
    body = rewrite_md_links(body)
    home = (
        "---\n"
        "title: Reminders GTD\n"
        "type: docs\n"
        "---\n\n"
        + body
    )
    (DEST_CONTENT / "_index.md").write_text(home, encoding="utf-8")

    print("Migrated chapters to", DEST_CONTENT)


if __name__ == "__main__":
    main()
