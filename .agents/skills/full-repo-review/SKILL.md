---
name: full-repo-review
description: Performs a rigorous, publication-ready review of the Reminders GTD guide repository covering GTD methodology, documentation quality, proofreading, UX, consistency, and workflow simulation. Use when the user asks for a full repo review, comprehensive editorial review, pre-publish audit, or GTD/Reminders guide QA. For reviewing only the current diff (PR-style), use `/review-changes`. To rebut a review in the same chat, use `/challenge-review`.
disable-model-invocation: true
---

# Full repository review

**Not for incremental edits.** If the user wants feedback on staged or branch changes only, stop and suggest `/review-changes` unless they explicitly want a whole-repo audit.

## Before you write

1. Read [AGENTS.md](../../../AGENTS.md) and treat it as the author’s house style (UK English, spaced hyphens not em dashes, curly quotes, naming conventions).
2. Read [references/REFERENCE.md](references/REFERENCE.md) for the reader-facing file inventory, naming conventions, and intentional GTD deviations (use it heavily for sections 5 and 6).
3. Read every reader-facing page in scope:
   - [README.md](../../../README.md)
   - All `docs/*.md` in the order in [docs/index.md](../../../docs/index.md) (“Read it in this order”)
   - Skim `docs/images/*.svg` labels if diagrams are cited in prose
4. Optionally read [editorial-notes.md](../../../editorial-notes.md) for known open questions; do not treat it as published canon. Flag overlap with fixed items only if the guide still contradicts them.
5. Cross-check **README.md** numbered guide list against **docs/index.md** navigation and titles.
6. Where pages link to each other, spot-check internal `docs/*.md` links and Jekyll `baseurl` (`/reminders-gtd`) on changed or fragile paths.
7. Do not edit files unless the user asks; output a report only.

## Citation format

Every substantive finding must cite the repository:

- Markdown: `` `path/to/file.md` `` plus a short quoted excerpt or line reference when helpful.
- Prefer citing the exact phrase that is wrong or confusing.
- Group multiple hits of the same issue under one finding with several citations.

## Persona and tone

Act as a senior technical editor, GTD practitioner, QA tester, and first-time user. Review as if the guide were about to be published for people implementing Getting Things Done in Apple Reminders. Be critical and rigorous; assume the author wants honest feedback rather than encouragement.

## Report structure

Use the seven sections below (headings **exactly** as numbered). Within each section, list findings with:

| Field | Content |
| --- | --- |
| **Priority** | Critical · Major · Minor · Nice-to-have |
| **Location** | File(s) and section heading if present |
| **Finding** | What is wrong or risky |
| **Evidence** | Quote or paraphrase with citation |
| **Recommendation** | Concrete fix (rewrite, add step, diagram, align term, etc.) |

End section **4. User Experience Review** with **Onboarding score: N/10** and a short justification.

End the report with a **Summary** table: counts by priority and top three actions.

### 1. GTD Methodology Review

Evaluate whether the guidance accurately reflects GTD principles. Look for:

- Misrepresented GTD concepts
- Unclear or incomplete steps
- Advice that could create friction in a real-world GTD workflow
- Workflow differences from standard GTD
- Assumptions that may confuse users already familiar with GTD

For deviations from traditional GTD, say whether they appear intentional (see [references/REFERENCE.md](references/REFERENCE.md)) and whether the trade-off is reasonable.

### 2. Documentation Quality

Review clarity, readability, logical structure, consistency, missing information, unnecessary complexity, and repetition. Flag sections that need rewriting, more explanation, shortening, or examples.

### 3. Proofreading

Identify grammar, spelling, punctuation, awkward phrasing, inconsistent terminology, and inconsistent capitalisation. Provide suggested replacements.

### 4. User Experience Review

Assume a new user starting from scratch. Identify confusion points, missing setup instructions, unclear prerequisites, ambiguous decisions, and places where screenshots, diagrams, or examples would help.

### 5. Consistency Audit

Check consistency across the repository for list names, tags, areas, projects, contexts, review processes, Apple Reminders terminology, and GTD terminology. Use [references/REFERENCE.md](references/REFERENCE.md) as the rubric.

### 6. Test the Workflow

Mentally simulate these scenarios. For each: what the user would do, confusion or ambiguity, and suggested improvements. Trace at minimum:

| Scenario | Primary pages |
| --- | --- |
| Capture | `docs/capture-and-clarify.md`, `docs/setup.md` (Inbox) |
| Project | `docs/projects.md`, `docs/model.md`, `docs/examples.md` |
| Defer / dates | `docs/model.md`, `docs/capture-and-clarify.md`, `docs/images/date-meanings.svg` |
| Next actions | `docs/do-the-work.md`, smart list tables in `docs/index.md` |
| Weekly review | `docs/weekly-review.md`, `docs/setup.md` (template) |
| Someday/Maybe | `docs/model.md`, `docs/advanced.md` |
| Waiting For | context/`waiting` guidance across `docs/index.md`, `docs/do-the-work.md` |
| Completed projects | `docs/projects.md`, `docs/weekly-review.md` |

### 7. Repository Improvement Opportunities

Suggest changes that make the guide easier to adopt, easier to maintain, more beginner-friendly, more GTD-compliant, or more opinionated where beneficial.

## Additional resources

- Repo inventory and naming reference: [references/REFERENCE.md](references/REFERENCE.md)
