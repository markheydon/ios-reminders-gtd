# Editorial notes (working)

Working notes while the guide is read on a real iPhone or iPad. This file is **not** part of the published guide (it is not linked from `README.md` or `guide/_index.md`). When reading is finished, turn confirmed items into GitHub issues and then archive or delete what has been actioned.

**Site (Oct 2026):** Findings **4**, **10**, and **54** (web footer) are implemented via Hugo Book (`website/` builds from `guide/`). Content findings **5–53** (except deferred **18**, rejected **25**) were implemented in the editorial content pass on branch `cursor/editorial-findings-pass-4e7f`. See [docs/README.md](docs/README.md).

**Illustrations:** still deferred until copy is stable (screenshot checklist below).

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
| **Proofread** | Callout added at start of setup §5. Where the reminder lives, and why it shows on those lists, is decided in finding 43: create and delete it on **Inbox**. It shows on each context smart list because it carries the tags, until it is deleted. |

### 2. Horizons note on the checklist before setup creates it

| Field | Detail |
| --- | --- |
| **Status** | fixed |
| **Where** | `docs/setup.md` (Weekly Review template); also `docs/weekly-review.md`, `docs/model.md`, `docs/projects.md`, `docs/examples.md` |
| **Problem** | The setup template includes **Look at the horizons note**, but no setup step says to create that Notes page (e.g. empty note titled “Horizons”). First weekly review can point at something that was never created in the afternoon path. |
| **Likely fix** | Short setup step (or bullet in section 7): create the note once, even if empty. |
| **Proofread** | Step added at start of setup §7. |

### 3. Packing-list subtasks

| Field | Detail |
| --- | --- |
| **Status** | fixed |
| **Where** | `docs/projects.md` - “How many current subtasks” (packing example) |
| **Problem** | The packing example reads as a **tagged** parent (“Pack for Thursday”) with **untagged** children, as if that were a special exception to “one context tag per action”. That misplaces **Pack for Thursday** (it belongs on **Projects** as a subtask of the relevant outcome, not as a freestanding tagged parent). Smart lists and project grouping may still show siblings (`docs/limits.md` already warns about extra visible subtasks). |
| **Likely fix** | Reframe the example: untagged project parent; **Pack for Thursday** as a current subtask with `#home` (or `#anywhere`). Socks, charger, and passport can be subtasks of that packing step if the reader wants a one-sitting checklist. Subtasks should get a context tag at clarify; leaving checklist lines untagged is the reader’s choice at clarify, not a guide-wide exception to the one-tag rule. Optional: one short sentence on smart-list grouping if untagged grandchildren still surprise someone (not re-tested on device in this chat). |
| **Proofread** | Decided 8 Oct 2026 (proofread chat). **Pack for Thursday** is a subtask under the relevant **Projects** outcome, tagged `#home` (most likely) or `#anywhere`. Project parents stay untagged. Subtasks should carry context tags; untagged packing lines are down to the reader at clarify, not a promoted carve-out. **Fixed** in `guide/projects.md` (editorial pass). |

---

## Your notes (during proofread)

**Findings review (Oct 2026):** Every guide page was read; `guide/setup.md` was followed on an iPad. Content findings **5–53** (except deferred **18**, rejected **25**) are implemented under `guide/` on branch `cursor/editorial-findings-pass-4e7f`. Findings **4**, **10**, and **54** are in the Hugo site. Rows below record what was decided; use them when opening GitHub issues for anything still `open`.

Decided in the sanity pass (8 Oct 2026). The rows below match the implemented guide unless a row is still `open`.

- A smart list can include only one list in the Lists filter (finding 40). **Anywhere**, **Home**, **Out**, and **Calls** smart lists filter on their tag only (tag gathers across lists). **Waiting** smart list is the exception: **tag** `` `waiting` `` **or** list **Waiting For** (finding 46).
- Setup should not offer All Selected versus Any Selected (finding 41). With one tag selected, the two modes match.
- The GTD names are **Next Actions**, **Projects**, and **Waiting For** (findings 16, 46, 49). **Waiting For** is the standard list for one-off waits. Actions that belong to an outcome, including waits, are subtasks on **Projects**. Smart lists are how a tag is gathered across those lists.
- **Tag setup** is created and deleted on **Inbox** (finding 43).
- A capture may be rough, including “Sam” or a bit of nonsense. It has to be enough to remember the thought at clarify (finding 27).
- A project keeps at least one next physical action you can do now, or a waiting item if something is blocking. More than one subtask is fine when each can be done now (finding 30).
- The README repeats guide prose only where the repo page needs it. The book should keep useful home-page material. The “if you only do three things” line is already in `book/front-matter.md` (findings 33 and 48).
- “Starting again after a break” does not belong on `guide/why.md`, and that page should not point at it (finding 47).

Still open before or during that review:

- Tickler, Routines, and Columns-on-other-lists are drafted at the bottom as later additions. Do not write them in this review.

### Illustrations (planned)

**Scope:** Screenshots for **the whole guide** (`guide/*.md`), not only `examples.md`. After copy is stable on `main`, the author captures **generic iPhone screenshots**; a later agent pass places them beside the relevant sections. **Do not shoot until** list names, setup steps, and tap-path wording match the edited text (findings 16, 39, 46, etc.).

**Guide-wide shot checklist** (draft - trim or add when each page is edited; one UI idea per row is enough):

| Page | Sections / intent | Screenshot ideas |
| --- | --- | --- |
| `setup.md` | GTD group, lists, tags, smart lists | Lists screen with **GTD** group; create list / smart list; **Edit Filters** (tag-only row + **Waiting** OR row); Tag setup quick controls; weekly review template |
| `model.md` | Map of the system | **Projects** with parent + tagged next action; context smart list with project grouped underneath; built-ins **Today** / **Flagged** visible |
| `capture-and-clarify.md` | Capture vs clarify | **Inbox** untagged; rough capture in editor; clarify outcome (project vs **Next Actions**); optional clarify-flow moments |
| `do-the-work.md` | Day shape | **Today** / **Flagged**; one context smart list; **i** → **Places & People** → When Messaging + contact |
| `projects.md` | Project shape, waiting, someday | Tax-style project; `waiting` subtask; **Someday**; columns view optional |
| `weekly-review.md` | Review ritual | **Weekly Review** list from template; empty **Inbox** step |
| `advanced.md` | Optional tags | Extra tag on a reminder; location quick control (not **i**) |
| `limits.md` | Only if prose needs UI proof | e.g. subtasks grouped under project on a smart list — otherwise skip |
| `why.md` | Usually none | Diagrams already SVG; screenshots unlikely |
| `index.md` | Optional | Same system-map SVG; maybe one hero “lists overview” if home page gains a figure |

**`examples.md` storyboard** (same Reminders data as the worked week; nice for a coherent screenshot set across several pages):

Use these titles when building the example world (list names per findings 16 / 14):

| Shot | What to show | Reminder / list content (from the guide) |
| --- | --- | --- |
| 1 | Raw **Inbox** dump | `tax return`, `tap still dripping`, `call dentist`, `maybe learn to bake bread`, `Priya owes the damp photos`, `parking fine on the kitchen table`, `email accountant the questions`, `idea: repaint the spare room` |
| 2 | After clarify — **Projects** (sections) | Money: parent **Tax return filed** + subtask “Email accountant the questions” `#anywhere`; Home: **Kitchen tap fixed** + “Priya: photos of the damp patch” `#waiting` (When Messaging → Priya) |
| 3 | One-off actions | **Next Actions**: “Call dentist and book a checkup” `#call`; “Pay the parking fine” `#home` |
| 4 | **Someday** | “maybe learn to bake bread”, “idea: repaint the spare room” (untagged) |
| 5 | Smart lists after Monday evening | **Anywhere** (tax email under project); **Calls** (dentist); **Home** (parking fine); **Waiting** (Priya / tap) |
| 6 | Tuesday | **Anywhere**: doing or just completed “Email accountant the questions”; then project with new “Gather the interest statements” `#anywhere` |
| 7 | Wednesday | **Kitchen tap fixed**: waiting item done; subtask “Book the plumber from the shortlist” `#anywhere` (optional: Messages with When Messaging surfacing) |
| 8 | Thursday morning | **Home**: “Pay the parking fine”; then **Flagged**: “Gather the interest statements” |
| 9 | After Thursday tax step | Tax project: “Call the accountant with the questions list” `#call` added |
| 10 | Friday review | **Weekly Review** checklist; **Inbox** with `buy a washer for the tap`, `look at spare room paint`; **Calls** with dentist still open |
| 11 | Friday close | Booking dentist from **Calls** (optional completion tick) |

**Consistency check (8 Oct 2026):** Tuesday–Friday actions follow the Monday clarify table and the Monday-evening summary (line 29). Tax arc: email → gather statements → call accountant. Tap arc: Priya wait → book plumber; Friday adds washer `#out`. Parking fine cleared Thursday Home. Friday **Inbox** lines are **new** mid-week captures, not Monday leftovers. No story break found; re-check after finding 16 renames and finding 27 capture-example edits.

Read in whatever order you find the pages, and say what you noticed in chat. Notes get written here. Confirmed fixes land in `guide/` on the editorial branch, then merge to `main`.

A page stays unticked while you are still in it. A tick means that page is finished. It is not a verdict. Findings stay `open` until the end review.

### Pages

Phone in hand. One sitting per page is enough, especially setup.

- [x] `guide/setup.md` - content read (findings 23–25) and followed on iPad, 8 Oct 2026 (findings 34–48). Finding 25 withdrawn.
- [x] `guide/do-the-work.md` - content read (findings 28–29). When Messaging on **i** confirmed 8 Oct 2026 (Places & People; contact picker). Messages surfacing out of scope for the guide.
- [x] `guide/projects.md` - content read (finding 30). Packing-list model decided (item 3); fixed in `guide/projects.md`.
- [x] `guide/weekly-review.md` - content fine. No findings.
- [x] `guide/advanced.md` - finished. Findings 50–53. **i** sheet and quick-controls-in-edit flow confirmed 8 Oct 2026 (finding 39).
- [x] `guide/limits.md` - content fine. No findings.

Quieter pass. Voice, links, and names staying consistent. No tap-by-tap unless a sentence sends you to a control.

- [x] `guide/_index.md` - finished. Findings 4–9.
- [x] `guide/why.md` - finished. Findings 10–15.
- [x] `guide/model.md` - finished. Findings 16–22. Title duplicate is finding 10, not logged again.
- [x] `guide/capture-and-clarify.md` - finished. Findings 26–27.
- [x] `guide/examples.md` - finished. Finding 31.
- [x] `README.md` - finished. Findings 32–33. The numbered guide list matches `book/chapters.txt`.

### Findings

#### Tap paths and control names

Reminders on iPhone and iPad match for this guide. Three ideas, not one vague “box”:

- **List view.** Quick controls do **not** show until you are in a **single reminder** entry or edit flow.
- **Quick controls.** When you open one reminder for entry/editing, Date, Time, Urgent, Repeat, Location, Tag, Flag, and Camera appear there (setup §4). Tag setup uses this path. `docs/advanced.md` should send readers to **Location** here, not to the **i** button.
- **Details table.** The same flow also uses the usual **settings-style table**: rows in **sections** for the rest of the metadata. Replace “box around the reminder” and “metadata box” with language that points at **quick controls** and/or **rows in that sectioned table**, as the sentence needs.
- **i info button.** `docs/do-the-work.md`: edit the reminder, tap **i**, turn on When Messaging under **Places & People**, choose the contact. `docs/advanced.md`: When Messaging, notes, and priority on that **i** screen. Do not fold every metadata step into **i**.

| Page | What the guide says | What you see | Status |
| --- | --- | --- | --- |
| `docs/setup.md` | Tags, dates, and other metadata are in the box around the reminder | Confirmed 8 Oct 2026. Open a single reminder to edit; **quick controls** appear (not on the list when you are not in that entry). Full details use the **sectioned table**. Same on iPhone and iPad. Rewrite “box” / “metadata box” per finding 39; keep §4’s control list, fix the lead-in sentence. | confirmed |
| `docs/do-the-work.md`, `docs/advanced.md` | When Messaging is behind the **i** info button (advanced also puts notes and priority there) | Confirmed on iPad, 8 Oct 2026. **When Messaging** is on the **i** sheet under **Places & People**; enable it, then choose a contact. Notes and priority are on the same **i** screen. Surfacing in Messages works in practice; how it works is out of scope for the guide. Optional copy tweak when editing: name **Places & People** so readers find the switch. | rejected |

#### Other findings

| # | Page / area | Issue | Status |
| --- | --- | --- | --- |
| 4 | Site header (all pages) | The top navigation lists every page in one row and looks overcrowded. This is the theme menu, separate from the “Read it in this order” list on the home page. **Confirmed 8 Oct 2026:** Replace flat nav with **four groups** (dropdown or equivalent on narrow screens): **Start** — why, model, setup; **Daily** — capture-and-clarify, do-the-work, projects; **Maintain** — weekly-review, examples; **More** — advanced, limits. Same structure on phone and desktop; layout must **respond** sensibly at different widths. Author is not tied to **Minima**; switching themes is fine if a better fit solves nav without fighting the guide. Implement after copy pass (may pair with screenshots / theme work). | fixed |
| 5 | `docs/index.md` (opening) | “This repository is an independent guide” uses *repository*, which is too technical for a reader who is not used to git. **Confirmed 8 Oct 2026:** Use **“This guide is independent…”** (not an Apple or David Allen product). README may still say repository where GitHub readers expect it (finding 33). | fixed |
| 6 | `docs/index.md` (The short version) | “A project is a reminder” is easy to misread. **Confirmed 8 Oct 2026:** Outcome-first rewrite (option 1): a **project** is an **outcome** you are committed to; in Reminders it is a reminder on **Projects**; actions you can take now are **subtasks**, each with one context tag; smart lists gather by tag. One-off actions on **Next Actions** stay finding 7. | fixed |
| 7 | `docs/index.md` (The short version) | Subtasks are the next actions, but the short version only describes them under a project. **Confirmed 8 Oct 2026:** Add **two sentences** after the project/subtask block — one for one-off **do now** actions on **Next Actions**, one for one-off waits on **Waiting For** (each still one context tag or `waiting`, same smart-list idea). Align README short version when edited (finding 32). | fixed |
| 8 | `docs/index.md` (context table) | The four contexts are the opinionated default. **Confirmed 8 Oct 2026:** One asterisk-style line **directly under the table** (tone B): these four are the default in this guide; swap names only if you will still clarify to **one tag per action**. Afterthought only, not a second taxonomy. | fixed |
| 9 | `docs/index.md` (Read it in this order) | Replace the single reading list with two sections. **Confirmed 8 Oct 2026:** Section titles **Quick Start** and **Read the Full Guide**. **Quick Start:** `setup.md` → `capture-and-clarify.md` → `do-the-work.md`, then **If you only do three things…** (only under Quick Start). **Read the Full Guide** (no duplicates; option A): 1. why, 2. model, 3. projects, 4. weekly-review, 5. examples, 6. advanced, 7. limits. Drop “including how to start again after a break” from the why blurb when lists are rebuilt (finding 47). README numbered list must match the **combined** reading path or whatever `check-guide.py` expects after edit (finding 33). Book: `book/front-matter.md` already holds “three things”; finding 48. | fixed |
| 10 | Site-wide (page title) | The title is drawn twice at the top of a rendered page. Seen on `docs/why.md` and again on `docs/model.md`. The theme prints a title and the markdown also has the same heading. Do not log this again per page. **Confirmed 8 Oct 2026:** **Defer** until theme work (finding 4); fix duplicate titles in the same pass as a new/responsive theme rather than a Minima-only CSS hack. | fixed |
| 11 | Guide-wide (“Getting Things Done”) | Hyperlink every reader-facing **Getting Things Done** (the method name) to [gettingthingsdone.com](https://gettingthingsdone.com/), same as `docs/index.md` and `README.md`. In `docs/` today that is mainly `why.md` opening plus the home page; add links when the phrase appears elsewhere. Do **not** link the **GTD** acronym or list group name. **Confirmed 8 Oct 2026.** `book/front-matter.md`: link the phrase once there if it fits; book disclaimer stays in front matter only (finding 54). | fixed |
| 12 | `docs/why.md` (opening) | Keep “stop rehearsing them”, and add a plainer phrase beside it. **Confirmed 8 Oct 2026:** **Parenthetical** (option 2), not an em dash or spaced hyphen aside. Example shape: “stop rehearsing them (running the same worries on a loop in your head)”. Tweak wording in the edit pass if needed; keep it one short parenthesis. | fixed |
| 13 | `docs/why.md` (second paragraph) | “Reminders can be that system…” should reuse *trusted system*, which is fundamental to GTD. **Confirmed 8 Oct 2026:** Use David Allen’s **trusted system** wording — e.g. “Reminders can be that **trusted system** on an iPhone or iPad…”. Keep the tie to the first paragraph’s trust idea. | fixed |
| 14 | Guide-wide (names and emphasis) | **Confirmed 8 Oct 2026.** One **consistency sweep** across `docs/*.md` (and README where it mirrors the guide), **in the same pass as finding 16** (list renames). Author’s priority: **consistent policy matters more than which policy** — apply throughout. **Policy:** (A) Bold standard list names when meaning that list: **Inbox**, **Projects**, **Next Actions**, **Waiting For**, **Someday**, **Weekly Review**, **Groceries** when relevant. (B) Bold smart list names (**Anywhere**, **Home**, **Out**, **Calls**, **Waiting**). (C) Bold built-in views when named (**Today**, **Flagged**, **Completed**, etc.). (D) Context tags always in backticks, lowercase — never bold. (E) Setup tables: plain list names in cells; bold in prose. “Empty **Inbox**” / “**Inbox** at zero”: bold the list name. Generic outcomes: lowercase *projects* / rephrase; **Projects** when meaning the list (`do-the-work.md` style). | fixed |
| 15 | Guide-wide (numbers) | **Confirmed 8 Oct 2026:** UK editorial rule (option 1) — **one to nine** as words; **10 and above** as figures. Examples to fix in pass: “day 10”, “about 10 minutes”, “20 to 40 minutes”, “You have 20 minutes” (`examples.md` / finding 31). Keep figures in setup **numbered steps**, list order, and product versions (**iOS 27**). `advanced.md` “15 minutes” already correct. “Four to seven sections” stays words. Apply in the same editing pass as findings 14 and 16 where practical. | fixed |
| 16 | Guide-wide (list name) | **Confirmed 8 Oct 2026.** Rename **Next** → **Next Actions** and name the standard wait list **Waiting For** (exact list titles in setup). Smart list display name stays **Waiting** (not “Waiting For”). **Waiting** smart list filter (finding 46): `` `waiting` `` **or** list **Waiting For** — not tag-only. Guide-wide rename in prose, setup, diagrams, README, book; same pass as finding 14. | fixed |
| 17 | `docs/model.md` (Projects and subtasks) | **Confirmed 8 Oct 2026.** Add a **callout block** (not a footnote) near the tax example: **one or two sentences** max. Substance: project title names the **outcome** as if done; each subtask is a **physical next action** you could do now, usually starting with a verb. Do not expand into a method chapter. Ties to findings 19–20. | fixed |
| 18 | Guide-wide (horizons note) | “Goals, vision, and purpose sit in **one Notes note**” / **horizons note** / setup checklist step / weekly-review step — author has concerns about the whole pattern. **Deferred 8 Oct 2026:** no copy change in this editorial pass. Open a **future GitHub issue** to decide what horizons material belongs in the guide (title, Notes page, review step, model paragraph). Seek input from a planned **second human read-through** before redesign. Until then, leave published text and setup §7 step as they are. | open |
| 19 | `docs/model.md` (Projects and subtasks) | **Confirmed 8 Oct 2026:** Prefer GTD *outcome* over *result*. Change “A project is any **result**…” to “any **outcome**…”. In the same pass, fix any nearby reader-facing *result* on this page that means the same thing (e.g. Next list table “successful result” when finding 16 renames that row). Do not hunt *result* where it is ordinary English, not GTD. | fixed |
| 20 | `docs/model.md` (Projects and subtasks) | **Confirmed 8 Oct 2026:** Strengthen the subtasks bullet — use **next physical action(s)** explicitly instead of only “actions you could do now”. Complements finding 17 callout; ties to findings 27 and 30. | fixed |
| 21 | Guide-wide (bullets) | **Confirmed 8 Oct 2026:** **Sentence** bullets end with a full stop across `docs/*.md` (README where it mirrors guide bullets). **Fragments** (labels, single words, comma-only lists) stay without a stop. Tables and numbered setup steps unchanged except where a sentence bullet was missing a stop. Fold into the main copy-editing pass with findings 14–16. | fixed |
| 22 | `docs/model.md` (built-in lists) | **Confirmed 8 Oct 2026:** **Current focus (a few at a time)**; flag **stays** until finished or cleared. Avoid bare “today” wording that sounds like the built-in **Today** list — Reminders already has **Today** as a separate view. OK to say **current focus for today** when you mean “what I care about this calendar day”, but distinguish **Flagged** / flags from opening the **Today** list. Same on `docs/do-the-work.md` (finding 28). | fixed |
| 23 | `docs/setup.md` (opening) | **Confirmed 8 Oct 2026:** Replace “Budget about an hour” with steps-take-about-an-hour wording (e.g. “The following setup steps take about an hour to complete.”). Keep “an hour” as words; align with `docs/index.md` “What you need”. | fixed |
| 24 | `docs/setup.md` (§5) | **Confirmed 8 Oct 2026:** Replace vague “these five” line with explicit wording: drag the **five smart lists** into the **GTD** group **below** the standard lists from step 2 (Anywhere, Home, Out, Calls, Waiting). | fixed |
| 25 | Guide-wide (list name) | Withdrawn after the iPad run. Keep the list name **Weekly Review**. A longer name fought the template step: recreating the list from the template is simpler when the name stays plain. See finding 42. | rejected |
| 26 | `docs/capture-and-clarify.md` (Capture) | **Confirmed 8 Oct 2026.** **Callout** in Capture (near “until you have time to decide”): good practice to **set aside time to clarify** (soft habit wording — no Calendar app lecture). **Paraphrase** GTD substance only, no attributed quote: clarifying is deciding not doing; trustworthy **Inbox** needs a regular emptying rhythm; weekly review is backstop. Complements existing “after meetings / end of day / when it nags”. | fixed |
| 27 | `docs/capture-and-clarify.md` (Capture and Clarify) | **Confirmed 8 Oct 2026.** Capture may be rough if you will recognise it at clarify; “thing” and “fix it” are **failed** captures (no hook). **Good rough capture:** “Sam — kitchen quote?”. **Clarified title** (step 4 / clarify): keep “Ask Sam whether the quote includes fitting” with tag as appropriate. “Ask Sam…” is not the capture example — too clarified for Capture. Ties to findings 17 and 20. | fixed |
| 28 | `docs/do-the-work.md` (flags) | Same as finding 22 — **confirmed** there. Current focus for today is fine when distinct from the **Today** list; flag persists; up to three; “couple of screens”; may leave flags for tomorrow. | fixed |
| 29 | Guide-wide (wording) | **Confirmed 8 Oct 2026.** Prose: **next action** for the work. Reserve **subtask** only when naming the Reminders control (add subtask, tick subtask, etc.). Apply **guide-wide** with finding 14 sweep. `docs/do-the-work.md` was the prompt. | fixed |
| 30 | `docs/projects.md` (How many current next actions) | **Confirmed 8 Oct 2026.** Rename section **“How many current next actions”** (option A). Body: sanity-pass paint logic (≥1 next physical action or `waiting`; several only when each doable now; later steps in notes). Integrate item 3 packing reframe in same edit. Align with finding 29 wording. | fixed |
| 31 | `docs/examples.md` (voice) | **Confirmed 8 Oct 2026.** Frame the worked week as **you** (the reader using the system). Full second-person rewrite; opening e.g. ordinary week **for you** after a quiet couple of months. Keep the Monday clarify **table** examples as-is (author likes them). “You have **20** minutes…” (finding 15). Story consistency Tue–Fri checked — see Illustrations storyboard; no break found. | fixed |
| 32 | `README.md` (The short version) | **Confirmed 8 Oct 2026:** Keep **consistent** with `docs/index.md` **The short version** when both are edited — findings 6, 7, 8, 16, 29 (outcome-first, Next Actions / Waiting For sentences, context-table asterisk, next-action prose). Diagram and table stay on README for GitHub readers; wording matches the site block, not a separate summary. | fixed |
| 33 | `README.md` (role) | **Confirmed 8 Oct 2026:** **1A** — keep full opening on README for GitHub visitors. **Duplicate** “What you need” on README. **Keep** “if you only do three things” on README (wording aligned with finding 29 / site Quick Start). **One numbered reading list** on README matching `docs/index.md` for `check-guide.py` even when the site uses Quick Start + Read the Full Guide (finding 9). Short version stays in sync (finding 32). “Repository” on README is fine; site uses “this guide” (finding 5). | fixed |
| 34 | `docs/setup.md` (§2) | **Confirmed 8 Oct 2026:** On iPad (and guide assumes iPhone matches), use **Edit Lists** under the **…** menu, not tap **Edit**. Update §2 and any other list-edit steps. | fixed |
| 35 | `docs/setup.md` (opening) | **Confirmed 8 Oct 2026 (with finding 47):** Setup opening covers **fresh install and lapsed / foreign GTD setup** in one intro. | fixed |
| 36 | `docs/setup.md` (§2) | **Confirmed 8 Oct 2026:** Short note at top of create-the-lists: choose **iCloud** if asked (other accounts can appear). No provider essay. | fixed |
| 37 | `docs/setup.md` (§2 and §5) | **Confirmed 8 Oct 2026:** **Update the tables** so colour and symbol columns describe what the reader **actually sees** in the iOS 27 List Info sheet (unnamed swatches and glyphs), not abstract names like “Red” / “Tray” when those strings are not on screen. **Change suggested values** to match what is available in the picker (may differ from today’s table). Prefer descriptions that work without screenshots first (e.g. position on the grid, distinct visual: “teal arrow”, “indigo folder”) and reinforce with setup screenshots when shot (Illustrations). **Needs device pass:** author to verify each list/smart-list row on iPhone when editing or capturing shots; iPad 7 Oct noted unnamed dots. | fixed |
| 38 | Guide-wide (Groceries) | **Confirmed 8 Oct 2026:** Where **Groceries** is mentioned (`setup` §3/§6, `model.md`, `limits.md`), frame as **if you use Groceries** (optional Apple/shopping list), not something the reader was supposed to create in §2. | fixed |
| 39 | Guide-wide (metadata box) | “In the box around the reminder” and “metadata box” do not match the UI. **Confirmed 8 Oct 2026:** iPhone and iPad match. Quick controls (Date, Time, Urgent, Repeat, Location, Tag, Flag, Camera) appear only when you are in a **single reminder** entry/edit flow, not on the list otherwise. The same flow includes a **settings-style table** (rows in sections) for reminder details. **Rewrite:** drop “box” / “metadata box”. Setup §4: open the new **Tag setup** reminder for editing, tap **Tag** on the **quick controls** (and `#` in the title if needed). Capture/limits: check date, time, and place on the quick controls or table rows before Done (Apple Intelligence). Advanced: **Location** via quick controls when editing; When Messaging via **i** / **Places & People**. Optional: name **Places & People** where When Messaging is introduced. Screenshots after copy is settled (see Illustrations above). Files: `docs/setup.md`, `docs/capture-and-clarify.md`, `docs/limits.md`, `docs/advanced.md`. | fixed |
| 40 | `docs/setup.md` (§5) | **Confirmed 8 Oct 2026:** Smart list **Lists** filter: one list max — remove tick Projects + Next. **Anywhere**, **Home**, **Out**, **Calls**: **tag only** (gathers across lists). iPad-confirmed; iPhone assumed same. Finding 52 same rule. | fixed |
| 41 | `docs/setup.md` (§5) | **Confirmed 8 Oct 2026:** Single-tag smart lists: **one path** only; drop All Selected vs Any Selected choice (except **Waiting** row uses Any + tag or list per finding 46). | fixed |
| 42 | `docs/setup.md` (§7), `docs/weekly-review.md` | **Confirmed 8 Oct 2026:** Template on an **existing** **Weekly Review** list — offer **two OK paths**: (1) delete the list and create again from the template; (2) **uncheck** each checklist item on the existing list (do not rely on “clear contents and re-add template” as the main path). Align `setup.md` and `weekly-review.md`; say templates do not merge into a populated list. | fixed |
| 43 | `docs/setup.md` (§4 and §9) | **Confirmed 8 Oct 2026:** **Tag setup** on **Inbox**, all five tags, delete after smart lists built. §5 callout: noise on all five smart lists until delete. Do not say it lives on **Next** / **Next Actions**. | fixed |
| 44 | `docs/setup.md` (§5) | **Confirmed 8 Oct 2026.** Full **GTD** group order (top to bottom): 1. **Inbox**, 2. **Projects**, 3. **Next Actions**, 4. **Waiting For**, 5. context smart lists (**Anywhere**, **Home**, **Out**, **Calls**, **Waiting**), 6. **Someday**, 7. **Weekly Review**. Document after §5; reconcile with §2 partial order. Today / Scheduled / Flagged placement stays as §6 (outside or above group per Apple defaults). | fixed |
| 45 | `docs/setup.md` (model) | **Confirmed 8 Oct 2026:** Document smart-list model in setup (and fix `model.md` smart-list section to match): tag-only context lists; **Waiting** OR rule (finding 46). | fixed |
| 46 | `docs/setup.md` (model) | **Confirmed 8 Oct 2026 (updated).** **Next Actions** — one-off next actions. **Waiting For** — standard list for one-off waits (also tag `` `waiting` ``). Project waits stay subtasks on **Projects**, tagged `` `waiting` ``. **Waiting** smart list (display name **Waiting**): include reminders where **tag** is `` `waiting` `` **or** **list** is **Waiting For**. Setup §5 must document tap path (likely **Any Selected** plus tag + Lists = **Waiting For** only for that row); device-check when writing steps. **Anywhere**, **Home**, **Out**, **Calls** remain tag-only; do not tick multiple lists (finding 40). | fixed |
| 47 | `docs/setup.md`, `docs/why.md` | **Confirmed 8 Oct 2026 (with finding 35):** Move **Starting again after a break** to setup only; remove from `why.md`. Drop home/README nav blurb pointing at it on why. Combined setup opening for blank app + lapsed setup + restart path. | fixed |
| 48 | Book export | **Confirmed 8 Oct 2026:** Keep home-style material in `book/front-matter.md` (diagram, three things, short version / context table as needed). Chapters stay `why.md` onward in `chapters.txt`. No extra chapter for index-only content unless a later edit adds it. | fixed |
| 49 | Guide-wide (projects versus lists) | **Confirmed 8 Oct 2026:** Short **footnote** (not redesign): pure GTD lists vs Reminders subtask compromise; link [GTD linking actions and projects](https://gettingthingsdone.com/2020/06/the-gtd-approach-to-linking-next-actions-and-projects/). Best home: `model.md` or setup model — pick at edit time. | fixed |
| 50 | `docs/advanced.md` (opening) | **Confirmed 8 Oct 2026:** Link “set the basic system up first” to `setup.md`. | fixed |
| 51 | `docs/advanced.md` (opening) | **Confirmed 8 Oct 2026:** Expand tag **cost** (admin, babysitting, abandonment risk) in opening paragraph. | fixed |
| 52 | `docs/advanced.md` (Time and energy) | **Confirmed 8 Oct 2026:** Optional `quick` / `focus` / `low` smart lists are **tag-only**; remove “lists Projects and Next”. | fixed |
| 53 | `docs/advanced.md` (Columns) | **Confirmed 8 Oct 2026:** No columns-on-**Next Actions** prose in this pass; tags stay the answer. Later issue if needed (draft table at bottom). | fixed |
| 54 | Site vs book (GTD attribution) | **Confirmed 8 Oct 2026.** Intent: David Allen is the author of GTD; this guide is an independent Reminders implementation, not passing the method off as the author’s own. **Book:** attribution in `book/front-matter.md` only (no per-chapter footer); align wording with footer if useful. **Web:** **site footer on every page** (theme pass, finding 4). Approved text: “[Getting Things Done](https://gettingthingsdone.com/) is David Allen’s work. This guide describes one way to practise it in Apple Reminders; it is independent and is not an Apple or David Allen Company product.” Plus **CC BY 4.0** link in the footer. **Home (`docs/index.md`):** remove the David Allen / independence paragraph from the body (option A); footer carries it. Finding 5 “This guide is independent…” may still apply elsewhere on home if needed for Apple-only nuance — check when editing so nothing essential is lost. | fixed |

---

## After the full read

- [x] All items above have a final status (`confirmed` / `rejected` / `fixed` / deferred). Only finding **18** (horizons) stays `open` for a future issue; no guide edits this pass.
- [x] Conditional item 3 resolved and rewritten in `guide/projects.md`.
- [x] Agreed list of GitHub issues (title + one-line scope). Horizons (finding 18) filed on GitHub; Tickler/Routines/Columns remain `later` in the table below.
- [x] This file updated after the content pass (findings 5–53 marked `fixed` in the table where implemented).

### Issues to create (draft - fill in after review)

| Issue title | Source note # | Priority |
| --- | --- | --- |
| Add a Tickler list for items that should come back on a date | Future addition. Not in the guide (checked `docs/advanced.md`). Do not write it during this proofread. | later |
| Add Routines for regular repeating work | Future addition. Not in the guide. Do not write it during this proofread. | later |
| Consider Columns on lists other than Projects | Finding 53. Only if a low-admin use shows up. Not in this pass. | later |
| Revisit horizons note (Notes page, review step, model copy) | Finding 18. Deferred; input from second human read-through before deciding. | later |
