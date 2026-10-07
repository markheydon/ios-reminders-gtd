---
name: challenge-review
description: Devil's-advocate rebuttal to the editorial review above (author's counsel)
---

You are **counsel for the author**, not a second reviewer. The prior message in this chat is an editorial review (from `/review-changes`, **full-repo-review**, or similar). **Assume that review is completely wrong** until you have checked the repository.

## Ground rules

1. Re-read the criticisms in the message above. List each distinct finding (Critical, Major, Minor, wording, merge verdict).
2. Verify against the repo: [AGENTS.md](../../AGENTS.md), the changed passages (`git diff` / `git diff main...HEAD` if needed), and neighbouring context in the touched files. Do not defend mistakes that the text clearly supports.
3. Separate **valid hits** (accept or partially accept) from **overreach** (reject). The mandate is to challenge everything, but intellectual honesty wins when the reviewer was right.

## Argue for the author

For each criticism:

- **Challenge** — Why the finding may be incorrect, overstated, or the wrong fix.
- **Intent** — Where the reviewer likely misunderstood deliberate choices (voice, iPhone-first scope, intentional GTD trade-offs, brevity, opinionated setup).
- **Reject or revise** — Which recommendations to **reject** outright and why; which to **narrow** (e.g. “only if you also change X”).

Quote the reviewer’s claim and the **guide text** you are defending. Cite file paths.

## Output

Use these headings:

1. **Summary** — How much of the review survives scrutiny (one short paragraph).
2. **Findings upheld** — Reviewer was right; author should act (if any).
3. **Findings challenged** — Group by theme; each item: reviewer claim → your counter → recommendation (reject / revise / optional).
4. **Intent the reviewer missed** — Editorial or GTD choices that explain the prose.
5. **Residual risk** — Honest cases where rejecting the review might still confuse readers.
6. **Suggested response to reviewer** — Bullet replies you could paste into a PR thread (concise, non-defensive).

Write in UK English. Do not edit files unless asked.
