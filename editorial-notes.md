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

Add rows or sections as you go. Include page, what you saw on the phone, and whether it is setup/tap-path wrong vs model wrong.

### Tap paths and control names

Setup uses the **metadata box**; When Messaging is documented via the **i** info button in `do-the-work.md` and `advanced.md`. Note any label mismatches on device here.

| Page | What the guide says | What you see | Status |
| --- | --- | --- | --- |
| | | | open |

### Other findings

| # | Page / area | Issue | Status |
| --- | --- | --- | --- |
| | | | |

---

## After the full read

- [ ] All items above have a final status (`confirmed` / `rejected` / `fixed`).
- [ ] Conditional item 3 resolved on device.
- [ ] Agreed list of GitHub issues (title + one-line scope).
- [ ] This file updated or removed once issues exist.

### Issues to create (draft - fill in after review)

| Issue title | Source note # | Priority |
| --- | --- | --- |
| | | |
