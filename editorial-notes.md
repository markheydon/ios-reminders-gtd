# Editorial notes (working)

Working notes while the guide is read on a real iPhone or iPad. This file is **not** part of the published guide (it is not linked from `README.md` or `docs/index.md`). When reading is finished, turn confirmed items into GitHub issues and then archive or delete what has been actioned.

**Status key:** `open` · `confirmed` · `rejected` (not a real problem) · `fixed` (no issue needed)

---

## From initial scan (before full read)

### 1. Tag setup clutters every context smart list during setup

| Field | Detail |
| --- | --- |
| **Status** | fixed |
| **Where** | `docs/setup.md` - steps 4–9 (Tag setup reminder) |
| **Problem** | Step 4 puts all five tags (`anywhere`, `home`, `out`, `call`, `waiting`) on one **Tag setup** reminder. The guide elsewhere assumes one tag per live action (`waiting` replaces a context tag). With multiple tags on one reminder, **Tag setup** is likely to appear on **every** context smart list while the reader is checking filters in steps 5–8. Nothing warns that this is temporary noise, which can look like a misconfiguration. |
| **Likely fix** | Bootstrap tags another way (e.g. five one-tag throwaways, deleted in step 9), or add an explicit callout before validating smart lists: expect **Tag setup** on all five lists until step 9. |
| **Proofread** | Callout added at start of setup §5. |

### 2. Horizons note on the checklist before setup creates it

| Field | Detail |
| --- | --- |
| **Status** | fixed |
| **Where** | `docs/setup.md` (Weekly Review template); also `docs/weekly-review.md`, `docs/model.md`, `docs/projects.md`, `docs/examples.md` |
| **Problem** | The setup template includes **Look at the horizons note**, but no setup step says to create that Notes page (e.g. empty note titled “Horizons”). First weekly review can point at something that was never created in the afternoon path. |
| **Likely fix** | Short setup step (or bullet in section 7): create the note once, even if empty. |
| **Proofread** | Step added at start of setup §7. |

### 3. Packing-list subtasks (conditional - confirm on device)

| Field | Detail |
| --- | --- |
| **Status** | open - needs device check |
| **Where** | `docs/projects.md` - “How many current subtasks” (packing example) |
| **Problem** | A tagged parent (“Pack for Thursday”) with **untagged** child items (socks, charger, passport) is an exception to “one context tag per action”. Smart lists and project grouping may still show siblings (`docs/limits.md` already warns about extra visible subtasks). Behaviour must match what you promise. |
| **If confirmed broken** | Narrow the exception, or document actual Reminders behaviour on iOS 27. |
| **If confirmed OK** | Set status to `rejected` and optionally add one sentence so readers are not surprised. |
| **Proofread** | Device result: |
| | |

---

## Your notes (during proofread)

**Paused 7 Oct 2026.** Prose pass is done except `docs/advanced.md`, which waits until after a real run of `docs/setup.md`. Findings 4–33 stay `open`. The published guide has not been edited from this pass.

Still to do:

- Device pass, possibly this evening: follow `docs/setup.md` on the phone. Also confirm When Messaging on `docs/do-the-work.md`, and the packing-list case (item 3) on `docs/projects.md`.
- Then read `docs/advanced.md`.
- End review of the open findings, then GitHub issues. Tickler and Routines are drafted below as later additions, not created yet.

Read in whatever order you find the pages, and say what you noticed in chat. Notes get written here. The published guide stays as it is until a later pass decides what to change.

A page stays unticked while you are still in it. A tick means that page is finished. It is not a verdict. Findings stay `open` until the end review.

### Pages

Phone in hand. One sitting per page is enough, especially setup.

- [ ] `docs/setup.md` - content read (findings 23–25). Device pass still to do after the proofread: follow the afternoon once, and check button names, list names, the tag-setup callout at the start of §5, and the horizons note in §7.
- [ ] `docs/do-the-work.md` - content read (findings 28–29). Still to confirm on device: When Messaging is behind the **i** info button, and choosing a contact works as written.
- [ ] `docs/projects.md` - content read (finding 30). Device result for the packing-list case (open item 3 above) still blank.
- [x] `docs/weekly-review.md` - content fine. No findings.
- [ ] `docs/advanced.md` - not read. Dogfood after the setup run-through. Tickler and routines are future issues, not part of this proofread.
- [x] `docs/limits.md` - content fine. No findings.

Quieter pass. Voice, links, and names staying consistent. No tap-by-tap unless a sentence sends you to a control.

- [x] `docs/index.md` - finished. Findings 4–9.
- [x] `docs/why.md` - finished. Findings 10–15.
- [x] `docs/model.md` - finished. Findings 16–22. Title duplicate is finding 10, not logged again.
- [x] `docs/capture-and-clarify.md` - finished. Findings 26–27.
- [x] `docs/examples.md` - finished. Finding 31.
- [x] `README.md` - finished. Findings 32–33. The numbered guide list matches `docs/index.md`.

### Findings

#### Tap paths and control names

The guide uses two different places in Reminders. Compare both with the phone and fill **What you see**.

- **Metadata box.** `docs/setup.md` says tags, dates, and the rest of the metadata sit in the box around the reminder you are editing. `docs/capture-and-clarify.md` and `docs/limits.md` use the same phrase.
- **i info button.** When Messaging is not described as sitting in that box. `docs/do-the-work.md` says: edit the reminder, tap the **i** info button, turn on When Messaging, and choose the contact. `docs/advanced.md` says When Messaging, notes, and priority are behind that same button.

| Page | What the guide says | What you see | Status |
| --- | --- | --- | --- |
| `docs/setup.md` | Tags, dates, and other metadata are in the box around the reminder | | open |
| `docs/do-the-work.md`, `docs/advanced.md` | When Messaging is behind the **i** info button (advanced also puts notes and priority there) | | open |

#### Other findings

| # | Page / area | Issue | Status |
| --- | --- | --- | --- |
| 4 | Site header (all pages) | The top navigation lists every page in one row and looks overcrowded. A logically grouped dropdown would be easier. This is the theme menu, separate from the “Read it in this order” list on the home page. | open |
| 5 | `docs/index.md` (opening) | “This repository is an independent guide” uses *repository*, which is too technical for a reader who is not used to git. Replace that word. | open |
| 6 | `docs/index.md` (The short version) | “A project is a reminder” is easy to misread. In GTD a project is an outcome. The sentence is trying to say the **Projects** list holds reminders, and it never says the project is the outcome. | open |
| 7 | `docs/index.md` (The short version) | Subtasks are the next actions, but the short version only describes them under a project. Next actions that are not part of a project are not mentioned. | open |
| 8 | `docs/index.md` (context table) | The four contexts are the opinionated default. A short note under the table (asterisk style) would be enough to say a reader can use their own context names. Keep it as an afterthought, not part of the main explanation. | open |
| 9 | `docs/index.md` (Read it in this order) | Replace the single reading list with two: a Quick Start for people who want to be told what to do now, and a longer list for reading later (a quiet afternoon). The line under the list already points this way: “If you only do three things: create the lists in the setup guide, put current actions as tagged subtasks under projects, and open the matching smart list when you have time.” | open |
| 10 | Site-wide (page title) | The title is drawn twice at the top of a rendered page. Seen on `docs/why.md` and again on `docs/model.md`. The theme prints a title and the markdown also has the same heading. Do not log this again per page. | open |
| 11 | `docs/why.md` (opening) | Hyperlink the first “Getting Things Done” the same way `docs/index.md` links it to gettingthingsdone.com. | open |
| 12 | `docs/why.md` (opening) | Keep “stop rehearsing them”, and add a plainer phrase beside it. Rehearsing is clear if you already know GTD. Also true: people overthink those commitments, or they only store them in their heads. | open |
| 13 | `docs/why.md` (second paragraph) | “Reminders can be that system…” should reuse *trusted system*, which is fundamental to GTD. Something like “Reminders can be that trusted system…”. | open |
| 14 | `docs/why.md` (second paragraph) | **Inbox** should be bold, as it is on `docs/index.md`. | open |
| 15 | Guide-wide (numbers) | Prefer words for numbers under 10, and figures from 10 up (`20`, `40`). Flagged on `docs/why.md`: “twenty to forty minutes”. Same pattern elsewhere: “day ten” in `docs/why.md`, “about ten minutes” in `docs/weekly-review.md`, “twenty minutes” in `docs/examples.md`. Apply one rule across the guide when this is decided. The usual UK form of this rule writes one to nine as words and 10 upward as figures, so “ten” would be `10` as well. | open |
| 16 | Guide-wide (list name) | Rename the **Next** list to **Next Actions**. That name is a fundamental GTD term in the books and the other literature. Raised on `docs/model.md`. The list is named **Next** throughout the guide, so this is wider than one page. Related to finding 7 (single actions exist, but the home page never names them). | open |
| 17 | `docs/model.md` (Projects and subtasks) | The examples need a side note or footnote on why they are worded this way, for someone using the page as a quick glance rather than a GTD lesson. The project (the outcome) is written in the past / done form (“Tax return filed”). A clarified next action starts with a verb. Keep it short. Do not turn the page into a full method chapter. | open |
| 18 | `docs/model.md` (Lists) | “Goals, vision, and purpose sit in **one Notes note**” is unclear. Say more plainly what that single note is. | open |
| 19 | `docs/model.md` (Projects and subtasks) | “A project is any result that needs more than one step…” uses *result*. The GTD description the reader expects is *outcome*. The list table on this page already says “Outcomes you are committed to”. Might be a nitpick; decide at the end review. | open |
| 20 | `docs/model.md` (Projects and subtasks) | “Next physical action” should be a bigger point. The subtasks bullet only says “the actions you could do now”, which is softer than a physical, visible action. Ties to finding 17 (a clarified action starts with a verb). | open |
| 21 | Guide-wide (bullets) | Sentences in bullet lists should end with a full stop. Preference raised while reading `docs/model.md`. Apply across the guide when this is decided. | open |
| 22 | `docs/model.md` (built-in lists) | Keep “**Flagged** - the few actions you have chosen for today”, and add that they are your current focus. A reader should not think that flagging an action, then not finishing it today, makes the flag disappear tomorrow. It does not. | open |
| 23 | `docs/setup.md` (opening) | “Budget about an hour” sounds wrong. Keep the light tone, and say the steps take about an hour to complete. Something like “The following setup steps will take about an hour to complete.” Content note only. The afternoon has not been run on a phone yet. | open |
| 24 | `docs/setup.md` (§5) | “Drag these five into the GTD group, under the standard lists.” Say that these five are the smart lists just created (Anywhere, Home, Out, Calls, Waiting), not the standard lists from §2. | open |
| 25 | Guide-wide (list name) | The **Weekly Review** list should be clearer that it is not a day-to-day list. A name like **Weekly Review Checklist** would do that. Raised on `docs/setup.md`. The list is named **Weekly Review** throughout the guide (`docs/model.md` already calls it a standing checklist and “a tool, not a place you store work”). | open |
| 26 | `docs/capture-and-clarify.md` (Capture) | Beside “until you have time to decide”, add a short side note that it is good practice to schedule time to clarify. Include a version of the GTD line on this. Substance to check before any quotation goes in the guide: clarifying is deciding, not doing the work, and an inbox only stays trustworthy if you empty it on a regular rhythm. The weekly review is the backstop. The page already says to open Inbox after meetings, at the end of the day, or when it starts to nag. | open |
| 27 | `docs/capture-and-clarify.md` (Capture and Clarify) | Say the two naming moments apart. A capture can be rough, even nonsense, as long as it will remind you what the thing was. A clarified action starts with a doing verb. The page already prefers a phrase over a bare “Sam”, and step 4 already rewrites a one-step title as a physical action (“Email the insurer the photos”). Ties to findings 17 and 20. | open |
| 28 | `docs/do-the-work.md` (flags) | Same point as finding 22. Flags can mean your current focus, not only “chosen for today”. Nothing clears them automatically: a flag stays until you complete the action or remove the flag. Keep the limit of a few at a time (up to three, and the “couple of screens” signal). The page already says you can leave flags if tomorrow should start there. | open |
| 29 | `docs/do-the-work.md` (wording) | The repeated “subtask” reads oddly. These are tasks. The guide uses *subtask* because that is the Reminders control for an action under a project. Decide at the end review whether the prose should say task or next action, and keep *subtask* only when it points at that control. | open |
| 30 | `docs/projects.md` (How many current subtasks) | Extend “Prefer one.” A project should always have its next action as well. Those actions are physical tasks you can do right now, not a brainstorm of every possible task. The page already says not to dump the whole plan in as subtasks, and that the notes hold the plan. `docs/do-the-work.md` and `docs/weekly-review.md` already treat a project with no current action as a fault. | open |
| 31 | `docs/examples.md` (voice) | Rewrite the third person as *you*. The opening “someone restarting after a quiet couple of months” and the later “They have twenty minutes…” read better as “You have 20 minutes…”. The figure `20` is the number rule in finding 15. | open |
| 32 | `README.md` (The short version) | Same problem as findings 6, 7, and 16. “A project is a reminder” skips that a project is an outcome. The short version is weighted toward projects. GTD’s day-to-day weight is next actions. Projects stay important. The balance is off. | open |
| 33 | `README.md` (role) | The README repeats the published guide: short version, reading order, and what you need. A repository README should be about the project (what it is, where it is published, how to contribute). The guide itself belongs on the site. Finding 5 (“repository”) is the same sentence on `docs/index.md`. | open |

---

## After the full read

- [ ] All items above have a final status (`confirmed` / `rejected` / `fixed`).
- [ ] Conditional item 3 resolved on device.
- [ ] Agreed list of GitHub issues (title + one-line scope). When creating them, use labels from [.github/labels.yml](.github/labels.yml): typically `fix` plus `area:*`, and `needs-device-check` for setup or on-device behaviour.
- [ ] This file updated or removed once issues exist.

### Issues to create (draft - fill in after review)

| Issue title | Source note # | Priority |
| --- | --- | --- |
| Add a Tickler list for items that should come back on a date | Future addition. Not in the guide (checked `docs/advanced.md`). Do not write it during this proofread. | later |
| Add Routines for regular repeating work | Future addition. Not in the guide. Do not write it during this proofread. | later |
