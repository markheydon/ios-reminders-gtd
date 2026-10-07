# Full repo review — reference

## Reader-facing files

| Path | Role |
| --- | --- |
| `README.md` | GitHub entry; keep list aligned with `docs/index.md` |
| `docs/index.md` | Site home and reading order |
| `docs/why.md` | Motivation and restart |
| `docs/model.md` | Lists, tags, dates, mental model |
| `docs/setup.md` | Tap-by-tap afternoon setup |
| `docs/capture-and-clarify.md` | Inbox and clarify flow |
| `docs/do-the-work.md` | Daily execution from smart lists |
| `docs/projects.md` | Project reminders and subtasks |
| `docs/weekly-review.md` | Weekly review habit |
| `docs/examples.md` | Worked examples |
| `docs/advanced.md` | Optional tags and extras |
| `docs/limits.md` | Mac/web and edge cases |
| `docs/images/*.svg` | Diagrams linked from prose |

Not published: `editorial-notes.md`, `AGENTS.md`, and agent tooling under `.agents/` or `.cursor/` (for example this skill and `/review-changes`).

## Naming conventions (consistency audit)

| Kind | Convention |
| --- | --- |
| Lists | Bold: **Inbox**, **Projects**, **Next**, **Someday**, etc. |
| Context tags | Backticks, lowercase: `anywhere`, `home`, `out`, `call` |
| Waiting | Tag `waiting`; smart list “Waiting” (verify exact UI label in prose) |
| Smart lists | Match tables in `docs/index.md` and `docs/setup.md` |
| Platform | iPhone/iPad first; iOS 27 / iPadOS 27 minimum |
| Product strings | US spelling only for official names (e.g. Auto-Categorize) |

## GTD mapping (intentional deviations to judge)

- **Project** = parent reminder in **Projects**; **next actions** = tagged subtasks (not a separate “Next Actions” list per project).
- **Four contexts** only on the main path; more in `docs/advanced.md`.
- **`anywhere`** instead of `@computer`.
- **`waiting`** as a tag swap, not a separate GTD “@waiting” context list.

## Proofreading targets

- UK English in reader-facing text
- No em dashes; use ` - ` (spaced hyphen)
- Curly quotes `“` `”` for example titles and short quotes
- “Getting Things Done” / David Allen attribution where relevant
