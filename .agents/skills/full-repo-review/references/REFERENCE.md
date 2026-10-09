# Full repo review - reference

## Reader-facing files

| Path | Role |
| --- | --- |
| `README.md` | GitHub entry; keep list aligned with `book/chapters.txt` |
| `guide/_index.md` | Site home and reading order (Quick Start + Read the Full Guide) |
| `guide/why.md` | Motivation |
| `guide/model.md` | Lists, tags, dates, mental model |
| `guide/setup.md` | Tap-by-tap afternoon setup |
| `guide/capture-and-clarify.md` | Inbox and clarify flow |
| `guide/do-the-work.md` | Daily execution from smart lists |
| `guide/projects.md` | Project reminders and subtasks |
| `guide/weekly-review.md` | Weekly review habit |
| `guide/examples.md` | Worked examples |
| `guide/advanced.md` | Optional tags and extras |
| `guide/limits.md` | Mac/web and edge cases |
| `guide/images/*.svg` | Diagrams linked from prose |

Published via Hugo Book (`website/`). Not published: `editorial-notes.md`, `docs/` (contributor notes), `AGENTS.md`, and agent tooling under `.agents/` or `.cursor/` (for example this skill and `/review-changes`).

## Naming conventions (consistency audit)

| Kind | Convention |
| --- | --- |
| Lists | Bold: **Inbox**, **Projects**, **Next Actions**, **Waiting For**, **Someday**, etc. |
| Context tags | Backticks, lowercase: `anywhere`, `home`, `out`, `call` |
| Waiting | Tag `waiting`; smart list **Waiting** (display name **Waiting**, not “Waiting For”) |
| Smart lists | Match tables in `guide/_index.md` and `guide/setup.md` |
| Platform | iPhone/iPad first; iOS 27 / iPadOS 27 minimum |
| Product strings | US spelling only for official names (e.g. Auto-Categorize) |

## GTD mapping (intentional deviations to judge)

- **Project** = parent reminder in **Projects**; **next actions** = tagged subtasks (not a separate “Next Actions” list per project).
- **Four contexts** only on the main path; more in `guide/advanced.md`.
- **`anywhere`** instead of `@computer`.
- **`waiting`** as a tag swap, not a separate GTD “@waiting” context list.

## Proofreading targets

- UK English in reader-facing text
- No em dashes; use ` - ` (spaced hyphen)
- Curly quotes `“` `”` for example titles and short quotes
- “Getting Things Done” / David Allen attribution where relevant
