---
name: full-repo-review
description: Performs a rigorous, publication-ready review of the Reminders GTD guide repository covering GTD methodology, documentation quality, proofreading, UX, consistency, and workflow simulation. Use when the user asks for a full repo review, comprehensive editorial review, pre-publish audit, or GTD/Reminders guide QA. For reviewing only the current diff (PR-style), use `/review-changes`. To rebut a review in the same chat, use `/challenge-review`.
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
6. Do not edit files unless the user asks; output a report only.

## Citation format

Every substantive finding must cite the repository:

- Markdown: `` `path/to/file.md` `` plus a short quoted excerpt or line reference when helpful.
- Prefer citing the exact phrase that is wrong or confusing.
- Group multiple hits of the same issue under one finding with several citations.

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

## Review mandate

Act as a senior technical editor, GTD practitioner, QA tester, and first-time user.

Review this repository as if it were going to be published publicly for people who want to implement Getting Things Done (GTD) using Apple Reminders.

Perform a comprehensive review covering the following areas:

## 1. GTD Methodology Review

Evaluate whether the guidance accurately reflects GTD principles.

Identify:
- Places where GTD concepts are misrepresented
- Steps that are unclear or incomplete
- Advice that could create friction in a real-world GTD workflow
- Areas where the workflow differs from standard GTD
- Assumptions that may confuse users already familiar with GTD

For any deviations from traditional GTD, explain whether they appear intentional and whether the trade-off is reasonable.

## 2. Documentation Quality

Review the documentation for:

- Clarity
- Readability
- Logical structure
- Consistency
- Missing information
- Unnecessary complexity
- Repetition

Identify sections that:
- Need rewriting
- Need additional explanation
- Could be shortened
- Could benefit from examples

## 3. Proofreading

Identify:

- Grammar mistakes
- Spelling mistakes
- punctuation issues
- awkward phrasing
- inconsistent terminology
- inconsistent capitalisation

Provide suggested replacements.

## 4. User Experience Review

Assume you are a new user starting from scratch.

Identify:
- Points where you become confused
- Missing setup instructions
- Unclear prerequisites
- Ambiguous decisions
- Areas where screenshots, diagrams, or examples would help

Rate onboarding quality from 1-10 and explain why.

## 5. Consistency Audit

Check for consistency across the repository:

- Names of lists
- Tags
- Areas
- Projects
- Contexts
- Review processes
- Apple Reminders terminology
- GTD terminology

Report all inconsistencies.

## 6. Test the Workflow

Mentally simulate the workflow for the following scenarios:

- Capturing a new task
- Creating a project
- Deferring work
- Reviewing next actions
- Weekly review
- Someday/Maybe management
- Waiting For items
- Completed projects

For each scenario:
- Describe what a user would do
- Note any confusion or ambiguity
- Suggest improvements

## 7. Repository Improvement Opportunities

Suggest improvements that would make the guide:

- Easier to adopt
- Easier to maintain
- More beginner-friendly
- More GTD-compliant
- More opinionated where beneficial

Prioritise findings as:

Critical
Major
Minor
Nice-to-have

Output the review as a structured report with specific examples and citations from the repository.
Be critical and rigorous. Assume the author wants honest feedback rather than encouragement.

## Workflow scenarios checklist

When completing section 6, trace these pages at minimum:

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

## Additional resources

- Repo inventory and naming reference: [references/REFERENCE.md](references/REFERENCE.md)
