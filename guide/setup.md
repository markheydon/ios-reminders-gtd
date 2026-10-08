---
title: "Set it up on your iPhone or iPad"
weight: 12
permalink: /setup/
---

The following setup steps take about an hour to complete. They are written for **Reminders on iOS 27** or **iPadOS 27**. Use them for a fresh install, for an old GTD setup that no longer matches your life, or when you are starting again after a break. Tags, dates, and the rest of the metadata sit on the **quick controls** when you open a reminder to edit, and in the **sectioned table** of reminder details below them. Apple Intelligence can fill in a date, time, or place from a sentence you type on a supported device (for example iPhone 15 Pro or later, or an iPad with Apple Intelligence). The lists and habits in this guide do not depend on that fill-in.

If you are restarting after time away, you do not need a new app. Give yourself one sitting: run these steps if the lists are missing or wrong, dump everything on your mind into **Inbox** (speak to Siri if typing feels heavy), clarify with [capture and clarify](capture-and-clarify.md) until **Inbox** is empty, do one light [weekly review](weekly-review.md), then do one action from the context you are actually in.

## 1. Turn on iCloud Reminders

1. Open **Settings**.
2. Tap your name, then **iCloud**.
3. Turn on **Reminders**. On newer iOS or iPadOS versions it sits under **Apps** or **Show All** inside iCloud.

Tags, smart lists, and subtasks in this guide all depend on iCloud lists.

## 2. Make the GTD group and the standard lists

If Reminders asks which account to use, choose **iCloud**. Other accounts can appear; this guide assumes your GTD lists live in iCloud.

1. Open **Reminders**.
2. On the lists screen, open the **…** menu, then tap **Edit Lists**.
3. Tap **Add Group**. Name it `GTD`. Tap Create, then Done.
4. Tap **Add List** and create these standard lists (leave List Type as Standard). Put each one in the **GTD** group if the system asks; otherwise drag them into the group after you finish editing.

| List | Suggested colour | Suggested symbol |
| --- | --- | --- |
| Inbox | First swatch on the top row of the colour grid (warm red) | Tray |
| Projects | Indigo swatch on the middle rows | Folder |
| Next Actions | Teal swatch beside the blues | Arrow |
| Waiting For | Grey swatch on the bottom row | Clock |
| Someday | Brown swatch on the earth-tone row | Moon |
| Weekly Review | Neutral grey | Checklist, or the tick mark |

Drag them into the **GTD** group if they landed outside it: **Edit Lists**, hold the list handle, move it under **GTD**, tap Done.

Order inside the group for now, top to bottom: **Inbox**, **Projects**, **Next Actions**, **Waiting For**, **Someday**, **Weekly Review**. You will add the five context smart lists underneath in step 5.

## 3. Add areas to Projects

1. Open **Projects**.
2. Tap the more button (the circle with three dots), then **New Section**.
3. Create: Work, Home, Money, Health, People.
4. Rename or delete until the names match your life. Four to seven sections is the useful range.

These sections are areas of responsibility. They stay on this list only.

Leave **Auto-Categorize** off for **Projects**, **Next Actions**, **Inbox**, **Waiting For**, **Someday**, and **Weekly Review**. That control can sort a list into sections for you. On **Projects**, your sections are areas you chose. Automatic sections would file projects into groups you did not name. If you use Apple’s **Groceries** list for shopping, that is the place to let Apple sort.

## 4. Create the tags once

Smart list filters offer tags you have already used. Make them exist:

1. Open **Inbox**.
2. Tap **New Reminder** and title it `Tag setup`.
3. With that reminder open for editing, tap **Tag** on the **quick controls** (Date, Time, Urgent, Repeat, Location, Tag, Flag, and Camera). You can also type a space and `#`. Add: `anywhere` `home` `out` `call` `waiting`.
4. Tap Done.

Leave this reminder on **Inbox** until the smart lists exist. You will delete it at the end.

## 5. Create the context smart lists

**Tag setup** carries all five tags on purpose so the filters can see them. Until you delete it in step 9, that reminder will appear on **each** of the five smart lists in the tables below (including **Waiting**). That is expected while you are building the lists, not a misconfiguration.

### How the filters work

- **Anywhere**, **Home**, **Out**, and **Calls** gather reminders that carry the matching tag, wherever those reminders live among your lists. The smart list filter uses **only that tag**. You do not tick **Projects**, **Next Actions**, or any other list in **Lists** for these four.
- **Waiting** is different. It must show project subtasks tagged `waiting` **and** one-off waits on the **Waiting For** list. Its filter uses **tag** `waiting` **or** **list** **Waiting For** (see the **Waiting** row below).

Repeat the steps for each row in the first table. Then build **Waiting** using the second set of steps.

**Anywhere, Home, Out, and Calls**

1. From the lists screen, tap **Add List**.
2. Type the smart list name.
3. Tap **List Type** and choose **Smart List**. On some versions the control says **Make into Smart List**.
4. Tap **Edit Filters**.
5. Set the match rule to **All** (every filter must match).
6. Under **Tags**, choose only the tag in the table. With a single tag selected, you do not need to worry about All Selected versus Any Selected.
7. Leave **Lists** empty. Do not tick **Projects**, **Next Actions**, or any other list. A smart list can include only one list in the **Lists** filter, and these four lists are tag-only.
8. Pick the colour and symbol. Tap Done.

| Smart list | Tag | Colour | Symbol |
| --- | --- | --- | --- |
| Anywhere | `anywhere` | Blue swatch on the cool-colour row | Circle, or a person |
| Home | `home` | Green swatch on the middle row | House |
| Out | `out` | Orange swatch beside the reds | Location pin |
| Calls | `call` | Purple swatch on the violet row | Phone |

**Waiting**

1. Add a smart list named **Waiting** (display name **Waiting**, not “Waiting For”).
2. Tap **Edit Filters**.
3. Set the match rule to **Any** (any filter can match).
4. Add a **Tags** filter for `waiting`.
5. Add a **Lists** filter and tick **Waiting For** only. Do not tick **Projects** or **Next Actions** here.
6. Pick grey and a clock symbol if you like. Tap Done.

Drag all **five** smart lists into the **GTD** group, **below** the standard lists from step 2.

When everything is in place, the **GTD** group order from top to bottom should be:

1. **Inbox**
2. **Projects**
3. **Next Actions**
4. **Waiting For**
5. **Anywhere**, **Home**, **Out**, **Calls**, **Waiting** (the five smart lists)
6. **Someday**
7. **Weekly Review**

**Today**, **Scheduled**, and **Flagged** usually stay above your own groups; step 6 covers those.

If a tag does not appear in **Edit Filters**, open **Tag setup** on **Inbox**, confirm the tag was saved, then try again.

## 6. Keep three of Apple’s own lists

On the lists screen, tap the more button, then choose which default smart lists are visible. Turn on:

- **Today**
- **Scheduled**
- **Flagged**

All, Completed, and Assigned to Me can stay off until you want them. Leave **Groceries** on if you already use it for shopping. Siri Suggestions can stay off until you have decided you want Apple proposing extra reminders; if you turn it on, treat its output as **Inbox** material and clarify it.

**Today**, **Scheduled**, and **Flagged** usually stay above your own groups. That is a good place for them. Your day starts there, then moves to a context list.

## 7. Save the weekly review as a template

1. Open **Notes** and create a note titled **Horizons** (empty is fine). The [weekly review](weekly-review.md) and [projects](projects.md) pages explain what belongs there over time.
2. Open **Weekly Review**.
3. Add these reminders, with no dates and no tags:

   - Empty Inbox
   - Check Today and Scheduled
   - Check Waiting
   - Open each active project and confirm it has a next action
   - Scan **Next Actions** for anything that is really a project
   - Review Someday
   - Look at the horizons note
   - Clear stale flags

4. Tap the more button, then **Save as Template**. Name it `Weekly Review`.

Keep the list as well as the template. Templates do not merge into a list that already has reminders on it. Each week, either path is fine:

1. Delete the **Weekly Review** list and create it again from the template, or
2. Show completed items, **uncheck** each checklist line on the existing list, and work through them again.

The [weekly review](weekly-review.md) page explains the rhythm.

## 8. Make capture easy

Do whichever of these you will actually use:

- Add the Reminders **widget** to the Home Screen or Lock Screen (Lock Screen widgets are iPhone-only), pointed at **Inbox** if the widget lets you choose a list.
- Tell Siri “Remind me to …” during setup once, and check the reminder landed in a list you can see. If Siri files new reminders into a default list other than **Inbox**, change the default: open Reminders, tap the more button on the lists screen, look for the default list setting, and choose **Inbox**. The exact label varies slightly by iOS or iPadOS version; it is the list Siri uses when you do not name one.
- In an app you read often, such as Mail or Safari, try the share button and then Reminders, and send one item to **Inbox**.
- Add Reminders to Control Centre, or assign it to the Action button on iPhone, if you want capture without hunting for the app icon. An extra-large Reminders widget is available if you want **Inbox** to fill a Home Screen page.

## 9. Delete the sample and do a first dump

1. Delete **Tag setup** from **Inbox**.
2. Stop only after **Inbox** contains the things already on your mind. Speak them to Siri if that is faster.
3. Clarify them with [capture and clarify](capture-and-clarify.md).

## You are done when

- The **GTD** group contains **Inbox**, **Projects**, **Next Actions**, **Waiting For**, **Someday**, **Weekly Review**, and the five smart lists, in the order above.
- **Projects** has your area sections.
- **Anywhere**, **Home**, **Out**, and **Calls** filter on their tag only. **Waiting** matches tag `waiting` or list **Waiting For**.
- **Tag setup** is gone.
- New captures have a path into **Inbox**.
