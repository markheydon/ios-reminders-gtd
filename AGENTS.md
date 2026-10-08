# Agent notes

This repository is a written guide (not an app): Getting Things Done in the iPhone and iPad **Reminders** app on **iOS 27** and **iPadOS 27** (minimum for readers). Human readers matter more than tooling polish; keep edits small and in voice with the existing pages.

## Repository layout

- **`guide/`** - Reader-facing markdown and [`guide/images/`](guide/images/) (canonical source). Edit here for prose and diagrams.
- **`website/`** - Hugo shell (Hugo Book via Go modules in [`website/go.mod`](website/go.mod)). Builds the public site from `guide/`; published via GitHub Actions on merge to `main`. `baseURL` is `/ios-reminders-gtd` on [markheydon.me.uk](https://markheydon.me.uk/ios-reminders-gtd/). Do not add a custom domain on this repo (it would clash with the profile site).
- **`docs/`** - Contributor notes (not published chapters). Start with [`docs/README.md`](docs/README.md).
- **`README.md`** - Entry point on GitHub; its numbered guide list should stay aligned with [`guide/_index.md`](guide/_index.md) when you change navigation or titles.
- **`book/`** - Export-only metadata and front matter for PDF/EPUB builds (`scripts/build-book.sh`). Keep [`book/chapters.txt`](book/chapters.txt) in the same order as the numbered list on the home page. CI enforces that order and README ↔ index navigation via `scripts/check-guide.py`.

## Language and punctuation

- **UK English** in all reader-facing prose: *recognise*, *behaviour*, *colour* (including setup tables), and similar. Keep US spellings only where they are the official product name (e.g. Reminders **Auto-Categorize**).
- **No em dashes** (`—`). Use a spaced hyphen instead: ` - ` (e.g. `**Today** - dated items…`, `[setup](setup.md) - the tap-by-tap afternoon`).
- **Quotation marks** for example reminder titles and short quoted phrases: use curly quotes `“` and `”` as in the existing docs, not straight `"`.

## Voice and content

- Address the reader as **you**. Calm, practical, slightly opinionated; avoid hype and filler.
- **iPhone-first.** Mac and web are mentioned only where behaviour differs (`guide/limits.md` is the honest edge cases page).
- **GTD attribution:** David Allen’s method is the foundation; this is an independent guide, not an Apple or David Allen product.
- **Naming:** List names in bold (**Inbox**, **Projects**, **Next**, …). Context tags in backticks, lowercase (`anywhere`, `home`, `out`, `call`). Smart list names match the guide tables.
- **Scope:** The main path uses four contexts; optional tags and extras live in `guide/advanced.md`. Do not expand the core taxonomy without a deliberate editorial reason.

## Editorial review (agents)

- **Diff / PR-style:** `/review-changes` (`.cursor/commands/review-changes.md`)
- **Challenge a review:** `/challenge-review` in the same chat
- **Full publication audit:** `full-repo-review` skill under `.agents/skills/full-repo-review/`

## Issues and pull requests

- Human workflow and checklists: [CONTRIBUTING.md](CONTRIBUTING.md) and [.github/pull_request_template.md](.github/pull_request_template.md).
- Label names and meanings: [.github/labels.yml](.github/labels.yml). Apply one change-type label and an `area:*` label when the edit is localised; use `needs-device-check` for setup and Reminders UI changes.
- Do not open issues or pull requests unless the user asks.

## When editing

- Match the tone and structure of neighbouring sections before adding new ones.
- Prefer updating diagrams in `docs/images/` when the model changes, not only the text.
- Do not commit unless the user asks. Do not put secrets in the repo.
