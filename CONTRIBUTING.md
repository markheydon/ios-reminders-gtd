# Contributing

This repository is a **written guide** for Getting Things Done in the iPhone and iPad **Reminders** app. It is not an application. Changes are prose, diagrams, and light Jekyll site config under `docs/`.

The published guide lives at [markheydon.me.uk/ios-reminders-gtd](https://markheydon.me.uk/ios-reminders-gtd/). Merging to `main` updates GitHub Pages from the `/docs` folder.

## Report a problem

Use **Report a problem** in [GitHub Issues](https://github.com/markheydon/ios-reminders-gtd/issues/new/choose).

Helpful details:

- Which page or section (link or file under `docs/`).
- What you expected the guide to say or what step to do.
- If it is about tap paths, smart lists, or on-screen labels: your **iOS or iPadOS version** and what you actually saw. Add the `needs-device-check` label if you open the issue manually.

For setup and Reminders UI behaviour, the maintainer will not merge fixes without a device check on **iOS 27** or **iPadOS 27** unless the change is clearly editorial only.

## Propose an edit

1. Fork (if you are not the maintainer), create a branch, and edit.
2. Follow house style in [AGENTS.md](AGENTS.md): UK English, spaced hyphens (not em dashes), curly quotes for example reminder titles, bold list names, lowercase context tags in backticks.
3. Open a pull request against `main`. Use the PR checklist in the template.

**Default:** branch → pull request → squash merge to `main` (good history and review trail).

**Exception:** a trivial one-line typo on `main` is acceptable for the maintainer when speed matters. AI agents should still use pull requests unless the user explicitly asks otherwise.

## Before you open a pull request

- [ ] Read [AGENTS.md](AGENTS.md).
- [ ] Run an editorial review on the diff (maintainer: `/review-changes` in Cursor; humans: read the changed sections and neighbours).
- [ ] Apply labels: one **change type** (`fix`, `content`, `copyedit`, `diagram`, `meta`, or `question`) and an **area** label when the change is localised (`area:setup`, `area:workflow`, `area:model`, `area:limits`). See [.github/labels.yml](.github/labels.yml).
- [ ] If you changed navigation or page titles: keep [README.md](README.md) numbered list aligned with [docs/index.md](docs/index.md).
- [ ] If you changed the model (lists, tags, workflows): update diagrams in [docs/images/](docs/images/) as well as prose.
- [ ] If you touched [docs/setup.md](docs/setup.md), smart-list tables, or Reminders UI strings: label `needs-device-check` and state verification in the PR (device and result, or “not verified yet - do not merge”).
- [ ] Skim [editorial-notes.md](editorial-notes.md) for known open questions; do not reopen settled `fixed` items without reason.

## Merge

- Prefer **squash merge** so each logical change is one commit on `main`.
- GitHub Pages updates from `/docs` on merge. **Guide check** (fast) runs on pull requests and `main`: navigation sync, `book/chapters.txt` order, broken internal links and images, and em-dash guardrails (`python3 scripts/check-guide.py`). **Book** export builds on the same content changes (verify on PR; draft artifacts on `main` only) and when a [release is published](https://github.com/markheydon/ios-reminders-gtd/releases) (stable attachments). Editorial review stays checklist-based for voice and device behaviour.

### Build the book locally

Install `pandoc`, `rsvg-convert`, and `texlive-xelatex` (plus `texlive-latex-extra` on Debian/Ubuntu), then from the repository root:

```bash
./scripts/build-book.sh
```

Outputs land in `dist/` (`reminders-gtd-draft.epub` and `.pdf`). For release filenames, run `./scripts/build-book.sh release`.

## Licence

By contributing, you agree that your contributions are licensed under the same [CC BY 4.0](LICENSE) licence as the guide, unless you and the maintainer agree otherwise in the issue or pull request.

## Labels

Canonical definitions live in [.github/labels.yml](.github/labels.yml). After editing that file, sync to GitHub:

```bash
./scripts/sync-github-labels.sh
```

Optional argument: `./scripts/sync-github-labels.sh owner/repo`.

## For AI agents

- Read [AGENTS.md](AGENTS.md) before editing reader-facing files.
- Use `/review-changes` on the branch diff before suggesting a pull request; the author may use `/challenge-review` to stress-test the review.
- Propose issue and PR labels from `.github/labels.yml` in the PR description.
- Do not commit or open pull requests unless the user asks.

## Code of conduct

This is a small, maintainer-led guide. A formal code of conduct may be added if outside contributors become common. Be constructive in issues and reviews.
