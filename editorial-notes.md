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

**Next session: review the findings.** Every guide page has been read. `docs/setup.md` was followed on an iPad. The published guide has not been edited from this pass. Findings 4–53 are below. Finding 25 is rejected. Start with the open rows and decide what to change, what to leave, and which GitHub issues to open.

Still open before or during that review:

- Confirm When Messaging on `docs/do-the-work.md` (circled **i** and a contact).
- Packing-list case on `docs/projects.md` (item 3). Device result is still blank.
- Finding 45: context smart lists versus tapping a tag. Tied to finding 40 (one list tick on iPad).
- Finding 46: Waiting smart list matches **any** of tag `waiting` or list **Waiting**. Agreed in principle. Not tried on device yet.
- Tickler, Routines, and Columns-on-other-lists are drafted at the bottom as later additions. Do not write them in this review.

Read in whatever order you find the pages, and say what you noticed in chat. Notes get written here. The published guide stays as it is until a later pass decides what to change.

A page stays unticked while you are still in it. A tick means that page is finished. It is not a verdict. Findings stay `open` until the end review.

### Pages

Phone in hand. One sitting per page is enough, especially setup.

- [x] `docs/setup.md` - content read (findings 23–25) and followed on iPad, 8 Oct 2026 (findings 34–48). Finding 25 withdrawn.
- [ ] `docs/do-the-work.md` - content read (findings 28–29). Still to confirm on device: When Messaging is behind the **i** info button, and choosing a contact works as written.
- [ ] `docs/projects.md` - content read (finding 30). Device result for the packing-list case (open item 3 above) still blank.
- [x] `docs/weekly-review.md` - content fine. No findings.
- [x] `docs/advanced.md` - finished. Findings 50–53. Happy with the rest. Location and the **i** button were not rechecked on this pass.
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
| `docs/setup.md` | Tags, dates, and other metadata are in the box around the reminder | On iPad that phrase does not match the screen. The control seen is the circled **i**, which appears when you select the reminder line. Long-press is the other guess. See finding 39. | open |
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
| 23 | `docs/setup.md` (opening) | “Budget about an hour” sounds wrong. Keep the light tone, and say the steps take about an hour to complete. Something like “The following setup steps will take about an hour to complete.” | open |
| 24 | `docs/setup.md` (§5) | “Drag these five into the GTD group, under the standard lists.” Say that these five are the smart lists just created (Anywhere, Home, Out, Calls, Waiting), not the standard lists from §2. | open |
| 25 | Guide-wide (list name) | Withdrawn after the iPad run. Keep the list name **Weekly Review**. A longer name fought the template step: recreating the list from the template is simpler when the name stays plain. See finding 42. | rejected |
| 26 | `docs/capture-and-clarify.md` (Capture) | Beside “until you have time to decide”, add a short side note that it is good practice to schedule time to clarify. Include a version of the GTD line on this. Substance to check before any quotation goes in the guide: clarifying is deciding, not doing the work, and an inbox only stays trustworthy if you empty it on a regular rhythm. The weekly review is the backstop. The page already says to open Inbox after meetings, at the end of the day, or when it starts to nag. | open |
| 27 | `docs/capture-and-clarify.md` (Capture and Clarify) | Say the two naming moments apart. A capture can be rough, even nonsense, as long as it will remind you what the thing was. A clarified action starts with a doing verb. The page already prefers a phrase over a bare “Sam”, and step 4 already rewrites a one-step title as a physical action (“Email the insurer the photos”). Ties to findings 17 and 20. | open |
| 28 | `docs/do-the-work.md` (flags) | Same point as finding 22. Flags can mean your current focus, not only “chosen for today”. Nothing clears them automatically: a flag stays until you complete the action or remove the flag. Keep the limit of a few at a time (up to three, and the “couple of screens” signal). The page already says you can leave flags if tomorrow should start there. | open |
| 29 | `docs/do-the-work.md` (wording) | The repeated “subtask” reads oddly. These are tasks. The guide uses *subtask* because that is the Reminders control for an action under a project. Decide at the end review whether the prose should say task or next action, and keep *subtask* only when it points at that control. | open |
| 30 | `docs/projects.md` (How many current subtasks) | Extend “Prefer one.” A project should always have its next action as well. Those actions are physical tasks you can do right now, not a brainstorm of every possible task. The page already says not to dump the whole plan in as subtasks, and that the notes hold the plan. `docs/do-the-work.md` and `docs/weekly-review.md` already treat a project with no current action as a fault. | open |
| 31 | `docs/examples.md` (voice) | Rewrite the third person as *you*. The opening “someone restarting after a quiet couple of months” and the later “They have twenty minutes…” read better as “You have 20 minutes…”. The figure `20` is the number rule in finding 15. | open |
| 32 | `README.md` (The short version) | Same problem as findings 6, 7, and 16. “A project is a reminder” skips that a project is an outcome. The short version is weighted toward projects. GTD’s day-to-day weight is next actions. Projects stay important. The balance is off. | open |
| 33 | `README.md` (role) | The README repeats the published guide: short version, reading order, and what you need. A repository README should be about the project (what it is, where it is published, how to contribute). The guide itself belongs on the site. Finding 5 (“repository”) is the same sentence on `docs/index.md`. | open |
| 34 | `docs/setup.md` (§2) | On iPad, editing lists is **Edit Lists** under the **…** menu. The guide says tap **Edit**. | open |
| 35 | `docs/setup.md` (opening) | The steps assume a blank Reminders app. Some readers will arrive with a lapsed GTD setup that did not come from this guide. Say so near the start. | open |
| 36 | `docs/setup.md` (§2) | If other accounts exist (Exchange showed on this iPad), creating a list can ask which account. It needs to be iCloud. A short note at the top of “create the lists” is enough. Do not explain providers. | open |
| 37 | `docs/setup.md` (§2 and §5) | The List Info sheet is unnamed colour dots and unnamed icons. The guide’s names (Red, Indigo, Tray, Folder, Arrow, and the rest) are not labels on that sheet, so a reader cannot tell which swatch or glyph to tap. Seen on iPad, 7 Oct 2026. | open |
| 38 | Guide-wide (Groceries) | Grocery mentions read as a list the reader forgot to create. A short “if you are using it” is enough. Raised on `docs/setup.md` §3 and §6. Also `docs/model.md` and `docs/limits.md`. | open |
| 39 | Guide-wide (metadata box) | “In the box around the reminder” does not match the iPad. What appears is the circled **i** when you select the reminder line. Long-press is the other possibility. The phrase is also in `docs/capture-and-clarify.md`, `docs/limits.md`, and `docs/advanced.md`. | open |
| 40 | `docs/setup.md` (§5) | On this iPad you cannot tick more than one list in a smart list’s Lists filter, so the step “tick **Projects** and **Next**” cannot be done. iPhone not checked. This is the filter the context lists rely on. | open |
| 41 | `docs/setup.md` (§5) | Do not offer both All Selected and Any Selected. Tell the reader to use **Any Selected**, so a context can gain extra tags later without another decision now. | open |
| 42 | `docs/setup.md` (§7), `docs/weekly-review.md` | A template does not appear to copy its reminders into a list that already exists. Deleting the list and creating it again from the template may be the path that works. `docs/setup.md` also says you can delete the list’s contents and add the template again, which is the doubtful path. `docs/weekly-review.md` already says create a new list from the template and delete the tired copy. | open |
| 43 | `docs/setup.md` (§4 and §9) | **Tag setup** is created in **Next** and deleted from **Next**, so the page agrees with itself. It should be created and deleted in **Inbox**: it is a throwaway, and Inbox is where throwaways belong. | open |
| 44 | `docs/setup.md` (§5) | §2 gives an order for the five standard lists only. After the smart lists exist, give the order of every list in the GTD group so the reader does not have to invent it. | open |
| 45 | `docs/setup.md` (model) | If the reader can open a tag directly, what are the context smart lists for? Torn. Do not change the model until this is discussed. Tied to finding 40: the list filter was the reason a smart list was more than a tag. | open |
| 46 | `docs/setup.md` (model) | **Next** holds only next physical actions you could do now. One-step waits go on a standard list **Waiting**, not on **Next**. Project waits stay under the project, tagged `waiting`. The view is a smart list (**Waiting** or **Waiting For**) set to match **any** filter: tag `waiting`, or list **Waiting**. That is an or, so it does not need two lists ticked (finding 40). Not tried on device yet. The standard list and the smart list need different names if both exist. Context lists (Anywhere, Home, Out, Calls) are unchanged. | open |
| 49 | Guide-wide (projects versus lists) | Footnote, not a redesign. In the book, the Projects list is an index of outcomes. A current action is parked on a context Next Actions list, or on Waiting For if it is blocked on someone else. It is not stored under the project. Project support holds the plan and later steps, not the current action. This guide keeps the current action as a subtask on the project and gathers it with a smart list, which is a Reminders compromise. Official note that software may link a project to its action: [The GTD Approach to Linking Next Actions and Projects](https://gettingthingsdone.com/2020/06/the-gtd-approach-to-linking-next-actions-and-projects/). The footnote should say the strict split, and that later steps in the project notes are the part Allen did want kept with the project. | open |
| 50 | `docs/advanced.md` (opening) | “Set the basic system up first” should link to [setup](docs/setup.md) so the reader can get there in one tap. | open |
| 51 | `docs/advanced.md` (opening) | Expand “Every extra tag is a decision you must make during clarify, so each one has to earn that cost.” Say what the cost is: more tags mean more admin, more time babysitting the system instead of doing the work, and a system you are more likely to abandon. | open |
| 52 | `docs/advanced.md` (Time and energy) | The optional smart lists for `quick`, `focus`, and `low` say “lists Projects and Next”. On iPad a smart list cannot tick more than one list (finding 40), so that filter cannot be written as both lists. | open |
| 53 | `docs/advanced.md` (Columns) | Columns for energy on **Next** (Deep Focus and similar) is the wrong tool. Keep that simple: tags, as this page already suggests, not columns. Columns on lists other than Projects may be worth a later look if a low-admin use appears. No such use is clear yet. Do not add it in this pass. | open |
| 47 | `docs/setup.md`, `docs/why.md` | Move “Starting again after a break” into setup, or put a short version there. Readers are either new, or they already have a system and may only ever read the setup page. | open |
| 48 | Book export | `book/chapters.txt` does not include `docs/index.md`, so the short version and “if you only do three things” are missing from the PDF and EPUB. The file is the site home, which is why it is not a chapter. Decide whether that content moves into an early chapter so the book still has it. Ties to finding 9. | open |

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
| Consider Columns on lists other than Projects | Finding 53. Only if a low-admin use shows up. Not in this pass. | later |
