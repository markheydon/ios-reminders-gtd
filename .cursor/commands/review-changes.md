---
name: review-changes
description: PR-style editorial review of your current guide edits (diff-focused)
---

Review **only the current changes** in this repository as though they were submitted in a pull request.

## Scope

1. Inspect what changed: `git status`, then choose the diff scope (see **Scope modes** below).
2. Read each touched file in full where context matters (neighbouring sections, cross-links, tables, diagram references).
3. Do **not** re-audit the entire guide. For a publication-ready review of the whole repo, use the **full-repo-review** skill instead.

### Scope modes

- **Default:** Include the branch diff against `main` (or the base branch the user names) with `git diff main...HEAD`, **and** the working tree (`git diff` for unstaged, `git diff --cached` for staged) so nothing in the PR is missed.
- **Staged only:** When the user asks for staged-only review, use `git diff --cached` only. Do not report on unstaged changes or files outside that diff.

## House style

Follow [AGENTS.md](../../AGENTS.md): UK English, spaced hyphens (not em dashes), curly quotes for example titles, bold list names, lowercase context tags in backticks, iPhone-first scope.

Read [`.agents/skills/full-repo-review/references/REFERENCE.md`](../../.agents/skills/full-repo-review/references/REFERENCE.md) when judging naming, tags, platform scope, or GTD trade-offs.

## Focus on

- Regressions introduced by the changes
- GTD workflow impacts
- Documentation quality
- Clarity of explanations
- Consistency with the rest of the repository (including README ↔ `docs/index.md` if navigation or titles changed)
- If the diff touches `docs/setup.md` or smart-list tables, cross-check against REFERENCE and unchanged pages
- Proofreading issues
- User confusion risks
- If a finding might be a known open question, check [editorial-notes.md](../../editorial-notes.md) before flagging it as a regression

## Output

Provide these sections with headings **exactly** as numbered:

1. **Summary**
2. **Critical Issues**
3. **Major Issues**
4. **Minor Issues**
5. **Suggested Wording Improvements**
6. **Positive Changes**
7. **Merge Recommendation** (approve, approve with nits, or request changes — one sentence why)

Be specific: quote the **exact passages** that need attention and cite the file path. Group duplicate issues under one finding when the same problem appears in multiple places.

Do not edit files unless asked; report only.

**Follow-up:** To stress-test this review, run `/challenge-review` in the same chat.
