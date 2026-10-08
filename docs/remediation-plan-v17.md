# Remediation Plan v17 — Session-33 Parity Iteration

Date: 2026-10-08 · Scope: fresh two-site re-audit after the v16 baseline
(`7c45de1` / code `13b0088`) re-verified green (lint · typecheck · 96/96
unit · build · 126/126 e2e — first full run, no flakes · 30/30 smoke).
Probes: one-shot `agent-browser eval` scripts, sessions `ref18`/`clone18`
desktop 1280×800 + `ref18m`/`clone18m` 390×844, the standalone parity
server on :3200 booted per command through `scripts/with-server.sh`.

This pass swept the surface class the session-32 log flagged as the next
tier — **the calculator's line-item error paths** (the parent-recalc
response `{ lineItem, parentAmount }` family) — plus the standing
task-focus re-verification (mobile navigation R1–R4 + reference
data-drift check).

The audit measured, for the first time, what each site does when a
LINE-ITEM mutation or load fails:

- **The reference is SILENT on all three paths** (its entity API aborted
  via `agent-browser network route --abort`):
  1. Line-item CREATE failure — the Add Line Item sub-dialog stays open,
     NO toast, NO error text, and NO optimistic update (the calculator
     still reads "Total Calculated $25.00 / Based on 1 item" after the
     failed save).
  2. Line-item DELETE failure — its calculator deletes with NO
     confirmation (documented v6 behavior), and the failed delete leaves
     the row in place with zero feedback.
  3. Calculator LOAD failure (opening the calculator with the API dead) —
     it renders the SILENT EMPTY-STATE: "Total Calculated $0.00 / Based
     on 0 items / • Will update category total / No line items yet.
     Start by adding individual items that make up this category. / Add
     First Item". A dead API is visually indistinguishable from an empty
     category — the same data-integrity illusion as the v16 boot case.
- **The clone's mutation-failure superset is in place and verified live**:
  the create failure keeps the sub-dialog open AND fires "Could not save
  the line item / Network error — check your connection and try again";
  the delete failure keeps the row (no optimistic delete) AND fires
  "Could not remove the line item / Network error — …". Both verified
  live this pass on the :3200 parity server.
- **The clone's calculator LOAD failure renders byte-identical parity**
  (the empty-state, $0.00, 0 items — `lineItemsMap[item.id] ?? []` falls
  back to the empty array) — but the failure is swallowed as an
  UNHANDLED promise rejection: `calculator-dialog.tsx`'s effect calls
  `void loadLineItems(item.id)` with no catch. Two problems: (a) the
  unhandled rejection is a code-quality wart (console noise, fragile
  under stricter environments), and (b) the honest-error superset that
  v16 established for the boot data-failure is NOT applied to the
  calculator's own load — the silence is the reference's illusion, not a
  deliberate clone decision.
- **Zero e2e coverage of the calculator's error tier**: the calculator
  spec covers the happy paths (add → recalc, delete → recalc, chrome,
  placeholders) but nothing pins the catch blocks — a regression that
  drops the error toasts or breaks the dialog-stays-open behavior would
  ship silently.

The mobile-navigation stack (the task focus) was re-verified end-to-end
first (R1/R2/R3/R4 all still live on the reference; all six clone
superset fixes intact — the Tailwind v4 pins hold), and the reference
data-drift check ran clean (unchanged since session 19: allocation
30.5%, income `$5000.00`/1 item, savings `$1000.00`/1 item, expenses
`$525.00`/4 items, Net Balance `+$3475.00` — eleventh consecutive clean
check). The calculator's row-action geometry was re-measured (32×32
buttons, 16×16 icons — both sides, the v6 pin holds). The code audit
re-ran clean: `npm audit` = 5 high, all the dev-only ESLint `braces`
chain (GHSA-vfj7-8cjw-p6xm, no patched release — accepted, documented);
secret-pattern scan clean.

The audit found **1 clone-side finding group**; no new reference bugs
(the reference's silent failures ARE the parity target's behavior — the
clone keeps the surfaces and adds honest feedback, the established
superset class).

---

## Findings ledger

### G1. [MED] the calculator's line-item load failure is swallowed (unhandled rejection, no honest toast) — and the whole error tier is unpinned by tests

Measured live on the reference (abort `**/entities/**`, open the Rent
calculator): the SILENT EMPTY-STATE renders — "Total Calculated $0.00 /
Based on 0 items / No line items yet. Start by adding individual items
that make up this category. / Add First Item" (no error surface at all).

Measured live on the clone (abort `**/api/line-items**`, open the Rent
calculator): the SAME empty-state renders byte-identically (parity by
construction — `lineItemsMap[item.id] ?? []`), but `void
loadLineItems(item.id)` in `calculator-dialog.tsx`'s mount effect
rejects with nobody listening: an unhandled promise rejection with NO
toast. The clone's silence here is not a decision — it is an accident
of the `void` operator.

Drift on two axes:

1. **Code hygiene**: an unhandled rejection on a network failure (the
   exact class the v16 boot fix taught us to catch).
2. **Honest error (superset)**: the reference's empty-state under a dead
   API is the same data-integrity illusion as the v16 boot case — a
   transient network failure renders as "No line items yet". The clone's
   established superset class (honest error toasts on mutation failures,
   the boot data-failure toast) extends naturally: surface a load-failure
   toast. The empty-state surfaces themselves stay exactly as-is (parity
   with the reference's rendering).

Additionally (same finding group, test tier): the mutation-failure
superset — verified live and working this pass — has ZERO e2e coverage:
`tests/e2e/calculator.spec.ts` pins only the happy paths. A regression
in `line-item-dialog.tsx`'s or `calculator-dialog.tsx`'s catch blocks
would ship silently.

Fix (2 parts):

- `calculator-dialog.tsx`: the mount effect catches the load failure and
  fires the honest error toast — title "Could not load the line items",
  description `messageOf(error)` (the api client already yields "Network
  error — check your connection and try again" for aborted routes — the
  same string the dialogs' catch blocks toast), `variant: "error"`. The
  rendering is unchanged (the `?? []` fallback keeps the reference's
  empty-state surfaces). The toast fires per dialog-open (a fresh user
  action each time — the per-action semantics of the dialogs' own catch
  toasts, NOT a one-shot flag; only v16's boot case needed one-shot
  because its effect can re-fire without a user action).
- NEW `tests/e2e/calculator-error.spec.ts` (3 specs, route-abort
  pattern): the load-failure empty-state + toast (pins the fix), the
  create-failure dialog-stays-open + toast (pins the existing superset),
  the delete-failure row-stays + toast (pins the existing superset, with
  a seeded line item restored by the spec's own scope).

Fix files: `src/components/budget/calculator-dialog.tsx`,
`tests/e2e/calculator-error.spec.ts` (new).

### Observations (documented, no action)

- **The reference's line-item create failure is a silent no-op** — the
  sub-dialog stays open with no toast/banner/error text and no
  optimistic update (the list + total unchanged). The clone's
  dialog-open + error-toast superset verified live ("Could not save the
  line item / Network error — check your connection and try again").
- **The reference's line-item delete failure is a silent no-op** — no
  confirmation (its calculator deletes immediately), the row stays, no
  feedback. The clone's confirm + row-stays + error-toast superset
  verified live ("Could not remove the line item / Network error — …").
- **The reference's line-item EDIT failure is the same class by
  construction** — its edit flows through the same Save→PUT path as
  create (both measured silent); the clone's edit shares the create
  catch block (one `onSubmit` covers both). Not separately measured on
  the reference; the clone's shared-catch behavior is pinned by the
  create spec.
- **The reference's calculator load renders the parent's amount as the
  LINE-ITEMS sum, not the parent figure**: with the API dead, the
  calculator shows $0.00 while the card behind shows $25.00 — the total
  is computed from the fetched line items. The clone matches (its total
  is `sumAmounts(lineItems)`, same source) — parity by construction.
- **The calculator row-action geometry holds**: 32×32 buttons with
  16×16 icons on both sites (the v6 pin re-measured this pass; the ref's
  svg class string reads `w-3.5 h-3.5` but its rendered box is 16×16 —
  the button's flex layout sizes it; the clone's own pin stands).
- **`/login` under a dead API renders the card on both sites** (v15
  observation; no data fetch — unchanged).

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): R1 re-confirmed live
(the ref's TWO toast containers — both `fixed top-0 z-[100]` 390×32
`pe:auto` — intercept the burger's center hit at (38,30); the clone's
hit is DIRECT on the svg; burger 28×28 at (24,16) both). R2 re-confirmed
(tapping Income in the ref's sheet navigated to `/income` with
`sheetStillOpen: true` + overlay count 1; the clone's sheet CLOSED + 390
fit + `/income`). R3 re-confirmed (no ref link active on `/` — all five
rail links `rgb(63,63,70)`/400, no `<nav>` landmark either; the clone
highlights Dashboard — white + gradient + 500). R4 re-confirmed (ref
scrollWidth 395 on `/`+`/dashboard`, 464 on `/networth` full-page load;
clone 390 on ALL six routes). Sheet link geometry identical (Income at
(20,185), 247×32, both).

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1: the calculator load-failure honest toast (superset) + the reference's empty-state parity under a dead API | `tests/e2e/calculator-error.spec.ts` NEW "calculator load failure renders the reference empty-state + the error toast (v17)" — abort `**/api/line-items**` BEFORE opening the calculator (goto `/expenses`, click Rent's Calculate), assert: the calculator opens, "Total Calculated" reads `$0.00`, "Based on 0 items", the empty state ("No line items yet" + "Add First Item") renders, AND the toast fires (title "Could not load the line items", exact:true per the v16 live-region lesson); `unrouteAll({ behavior: "ignoreErrors" })` before spec end | `calculator-dialog.tsx` |
| 2 | G1 pin: line-item CREATE failure keeps the dialog open + toasts the error (the existing superset, unpinned until now) | same spec, NEW "line-item create failure keeps the dialog open + error toast (v17 pin)" — abort `**/api/line-items**` (POST), open the calculator, Add Item, fill name + amount, Save Item, assert: the "Add Line Item" dialog is STILL open, the error toast fires ("Could not save the line item", exact:true); unroute before end | — (pins current behavior) |
| 3 | G1 pin: line-item DELETE failure keeps the row + toasts the error (existing superset, unpinned) | same spec, NEW "line-item delete failure keeps the row + error toast (v17 pin)" — create a line item via the LIVE API first (fetch inside the spec with the page's session), then abort `**/api/line-items**`, click the row's Delete + confirm, assert: the row heading is STILL present, the error toast fires ("Could not remove the line item", exact:true); unroute, then restore the fixture (delete the line item + PATCH the parent back to the seed amount) inside the spec's own scope | — (pins current behavior) |
| 4 | Docs: session log (`docs/session_34.md` — the session_33.md slot holds the incoming session-31 conversation summary), worklog, README/AGENTS/CLAUDE/SKILL alignment (the v17 pin paragraph + the calculator error tier), probe README v17 rows | — | docs |
| 5 | Regression: full chain + live parity re-check (route-aborted calculator open reproduces the empty-state + the toast; a clean reload restores the line items) + screenshot refresh (no visible change expected — the fix is behavior-only; the empty-state branch never renders in the content-waiting shots) | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight — rail AND sheet, no mobile overflow, Escape close, delete
  confirmations) and the v9–v16 pins (donut geometry + tooltip, tab
  icons + header chip, banner chrome, titles, placeholders, focus rings,
  the full-page loading state + its data-flight timing, the boot
  data-failure stay-in-app + one-shot toast + the 401-probe redirect)
- The calculator's HAPPY paths: add → parent recalculates immediately,
  delete → recalculates back (the existing calculator specs re-run
  green); the chrome/placeholder pins
- The v16 boot semantics: `bootError`/`clearBootError` untouched; the
  load-failure toast here is PER-OPEN (a user action), not one-shot
- The mutation-failure superset toasts' exact text ("Could not save the
  line item" / "Could not remove the line item") — the new specs PIN
  them, not change them
- e2e fixture discipline: the delete spec creates its line item via the
  API and restores it inside its own scope (delete + PATCH the parent
  back); the aborted handlers are unhooked by the specs' own scope
