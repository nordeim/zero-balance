# Remediation Plan v18 — Session-35 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v17 baseline
(`eec5427` / code `786f961`) re-verified green (lint · typecheck · 96/96
unit · build · 129/129 e2e — one load flake in the first full run,
clean on the re-run · 30/30 smoke). Probes: one-shot `agent-browser eval`
scripts, sessions `ref20`/`clone20` desktop 1280×800 + `ref20m`/`clone20m`
390×844, the standalone parity server on :3200 booted per command through
`scripts/with-server.sh`.

This pass swept the surface class the session-34 log flagged as the next
tier — **the net-worth asset/liability error tier** (the last dialog family
the error-state audit had not measured: asset/liability SAVE and DELETE
failures) — plus the standing task-focus re-verification (mobile
navigation R1–R4 + reference data-drift check).

The audit measured, for the first time, what each site does when a
NET-WORTH mutation fails:

- **The reference is SILENT on both measured paths** (its entity API
  aborted via `agent-browser network route --abort`):
  1. Asset DELETE failure — its asset-card menu Delete fires immediately
     (NO confirmation — the same family as its budget-item cards) and the
     failed delete leaves the card in place with zero feedback: no toast,
     no error text, no menu residue. The DELETE XHR fired and failed
     (verified in the network log).
  2. Asset SAVE failure — the Edit Asset dialog STAYS OPEN (its dialogs
     are plain `fixed` divs — no `[role=dialog]`, consistent with the
     documented no-Escape/no-overlay-click family) with NO toast, NO
     error text, and no optimistic update.
- **The clone's net-worth SAVE-failure superset is in place and verified
  live**: the failed asset Save keeps the dialog open AND fires "Could
  not save the asset / Network error — check your connection and try
  again" (verified live this pass; the liability dialog's catch is the
  same code family — "Could not save the liability").
- **The clone's net-worth DELETE failure is SWALLOWED** — the exact v17
  G1 pattern repeating in a new file: `net-worth-view.tsx`'s inline
  confirm bars call `void deleteAsset(asset.id)` and
  `void deleteLiability(liability.id)` with no catch. (The same grep
  later found the pattern's third site — `item-card.tsx`'s
  `void deleteItem(item.id)` — documented in the fix section below.) Verified live on
  BOTH paths: the card stays (parity by construction — the store's
  `deleteAsset`/`deleteLiability` only mutate state AFTER the awaited API
  resolves), the confirm bar stays up, but NO toast fires — the silence
  is an accident of the `void` operator, not a decision.
- **Zero e2e coverage of the net-worth error tier**: the networth spec's
  22 tests cover happy paths only — a regression that drops the save
  toasts or breaks the card-stays behavior would ship silently. The
  budget-item tier got its pins in v16 (mutation catch verified live),
  the calculator's in v17; the net-worth tier is the last unpinned
  dialog family (the session-34 log's own suggestion).

The mobile-navigation stack (the task focus) was re-verified end-to-end
first (R1/R2/R3/R4 all still live on the reference; all six clone
superset fixes intact — the Tailwind v4 pins hold), and the reference
data-drift check ran clean (unchanged since session 19: allocation
30.5%, income `$5000.00`/1 item, savings `$1000.00`/1 item, expenses
`$525.00`/4 items, Balance `$3475.00` — twelfth consecutive clean check;
the reference's net worth holds 1 asset "Savings Account" `$25,000.00`
and 0 liabilities). The code audit re-ran clean: `npm audit` = 5 high,
all the dev-only ESLint `braces` chain (GHSA-vfj7-8cjw-p6xm, no patched
release — accepted, documented); secret-pattern scan clean. One process
note: the first full e2e run of the session failed ONE spec
(`login-parity.spec.ts` register duplicate-email) which passed in
isolation and in the complete re-run — root-caused during this session
as the spec's own announcer race (G2 below, fixed), not a product
flake.

A post-fix grep sweep (the "no remaining void sites" verification)
surfaced a THIRD site of the same G1 family — `item-card.tsx`'s inline
confirm bar (`void deleteItem(item.id)`, line 204) — missed by the v16
audit because the budget-item DIALOG's delete was always caught
("Could not delete the item") while the card menu's own inline confirm
is a separate code path; it joined the fix + gained its own pin spec
(the fifth of the pass).

The audit found **2 clone-side finding groups** (G1 spanning three
files, G2 the spec flake); no new reference bugs
(the reference's silent failures ARE the parity target's behavior — the
clone keeps the surfaces and adds honest feedback, the established
superset class).

---

## Findings ledger

### G1. [MED] the net-worth delete failures are swallowed (unhandled rejections, no honest toast) — and the whole net-worth error tier is unpinned by tests

Measured live on the reference (abort `**/entities/**`, click the asset
card's Delete): the DELETE fires immediately (no confirmation), the card
stays, and NOTHING else happens — no toast, no error text. Measured live
on the clone (abort `**/api/assets/**`, menu → Delete → the inline
confirm's Delete): the card stays (correct parity — the store deletes
from state only after the API resolves) and the confirm bar stays up —
but NO toast: `net-worth-view.tsx` lines 129/219 call
`void deleteAsset(asset.id)` / `void deleteLiability(liability.id)` and
the rejection lands on nobody. The same class as v17's G1 (the
calculator's `void loadLineItems`), in the last file the audit had not
swept.

Drift on two axes:

1. **Code hygiene**: unhandled promise rejections on network failures
   (the exact class the v16/v17 fixes taught us to catch — the
   reference-tier audit has now found the pattern in every entity
   family).
2. **Honest error (superset)**: the reference's silent card-stay under a
   dead API is the same data-integrity illusion as every prior tier — a
   transient network failure renders as "nothing happened". The clone's
   established superset class (honest error toasts on mutation failures
   — budget items since v16, line items since v17) extends naturally:
   surface a delete-failure toast. The surfaces themselves stay exactly
   as-is (card stays, confirm bar stays — parity with the reference's
   rendering).

Additionally (same finding group, test tier): the SAVE-failure superset
— verified live and working this pass ("Could not save the asset") — has
ZERO e2e coverage: `tests/e2e/networth.spec.ts` pins only the happy
paths. A regression in `asset-dialog.tsx`'s or `liability-dialog.tsx`'s
catch blocks would ship silently.

Fix (3 parts):

- `net-worth-view.tsx`: both confirm-bar Delete buttons catch the
  rejection and fire the honest error toast — title "Could not delete
  the asset" / "Could not delete the liability" (the budget-item
  delete's established wording — "Could not delete the item"),
  description `messageOf(error)` (the api client already yields
  "Network error — check your connection and try again" for aborted
  routes), `variant: "error"`. The rendering is unchanged (the card
  stays, the confirm bar stays). Per-click semantics (a fresh user
  action each time — the same per-action semantics as every dialog
  catch; no one-shot flag).
- `item-card.tsx` (the third site, found by the post-fix grep sweep):
  the budget-item card's inline confirm bar gets the identical
  caught-rejection treatment — toast title "Could not delete the item"
  (the dialog-delete's established text, now shared by the card path).
  The reference's failed card delete is the same measured silent
  family; the clone keeps the card + confirm bar surfaces.
- NEW `tests/e2e/networth-error.spec.ts` (4 specs, route-abort pattern):
  the asset save-failure dialog-stays-open + toast (pins the existing
  superset), the asset delete-failure card-stays + toast (pins the fix),
  the liability delete-failure card-stays + toast (pins the fix on the
  second path), and the liability save-failure toast (pins the second
  dialog catch). PLUS a fifth spec in `tests/e2e/items.spec.ts`: the
  budget-item card delete-failure card-stays + confirm-bar-stays +
  toast (pins the third site).

Fix files: `src/components/budget/net-worth-view.tsx`,
`src/components/budget/item-card.tsx`,
`tests/e2e/networth-error.spec.ts` (new), `tests/e2e/items.spec.ts`
(one new describe).

### G2. [LOW] the register duplicate-email spec raced Next.js's route announcer (one-shot banner read flaked under full-suite load)

Observed this session: the spec failed in 2 of 4 full-suite runs (the
first baseline run + the post-G1-fix run) — never in file isolation.
The failure signature: the `waitForSelector("[role='alert']")` PASSED,
then the immediately-following one-shot `page.evaluate` read `null` —
no `[role=alert]` existed at read time.

Root cause (isolated by hardening the assertion and re-running in file
isolation — the strict-mode violation exposed it):
**Next.js App Router's route announcer also renders
`role="alert"`** (`<div role="alert" aria-live="assertive"
id="__next-route-announcer__">`, mounted dynamically at hydration with
EMPTY text, sometimes unmounting again). The old
`waitForSelector("[role='alert']")` matched the ANNOUNCER — a no-op
wait that passed before the 409 banner ever rendered — and then the
evaluate raced the actual 409's arrival: under full-suite load (one
worker, Chromium + the standalone server, late-alphabetical file) the
response latency is high enough that the evaluate ran in the gap after
the announcer unmounted and before the banner rendered → null. In file
isolation the 409 lands fast enough that the evaluate sees the banner
(or the announcer still up). The PRODUCT is not at fault — the banner
itself is stable once the 409 lands; the spec simply waited on the
wrong element.

Fix: assert via a RETRYING, TEXT-FILTERED locator —
`expect(page.getByRole("alert").filter({ hasText: "A user with this
email already exists" })).toBeVisible()` — the filter scopes the
locator to the banner (the empty announcer never matches the text) and
toBeVisible polls through any mount/unmount churn. The sibling v12
banner-chrome test is NOT affected (verified): it waits on the banner's
TEXT first (a retrying locator), and the banner precedes the
body-appended announcer in document order, so its `querySelector`
always reads the banner — 15+ sessions of green runs confirm.

Fix files: `tests/e2e/login-parity.spec.ts`.

### Observations (documented, no action)

- **The reference's asset-card Delete fires with NO confirmation** — the
  menu item click IS the delete attempt (consistent with its budget-item
  cards and calculator rows — the documented superset-fix-#6 family).
  The clone's inline confirm bar stays the superset; under a dead API
  the confirm bar REMAINS up after the failed delete (both sides render
  the card; the clone's bar is the only difference — the superset).
- **The reference's net-worth dialogs are plain `fixed` divs** (no
  `[role=dialog]`, no data-state) — the h2 "Edit Asset" + its form stay
  visible after the failed Save. The clone's Radix dialogs are the a11y
  superset (focus trap, Escape, overlay-click) — same class as every
  documented dialog divergence.
- **The reference's SAVE failure leaves the dialog open with NO
  feedback** — the same silent no-op as its budget-item and line-item
  dialogs (v16/v17 measurements). The clone's dialog-open + error-toast
  superset verified live this pass on the asset path.
- **The reference's net worth holds 1 asset and 0 liabilities** ("bank
  account / Savings Account / $25,000.00"; the Liabilities tab renders
  "No liabilities yet") — the clone's seed is a superset (3 assets, 2
  liabilities) by design; the empty-state parity is pinned by the
  existing empty-states spec.
- **The reference's tab panels need real pointer clicks** — programmatic
  `.click()` on its Radix tabs left the selection unchanged (React state
  quirk; the same class as the session-33 mobile-login lesson). The
  audit used snapshot refs (real events) for both tabs.

### Verified matching this pass (no action)

Mobile navigation (task focus, both sites 390×844): R1 re-confirmed live
(the ref's TWO toast containers — both `fixed top-0 z-[100]` 390×32
`pe:auto` — intercept the burger's center hit at (38,30); the clone's
hit is DIRECT on the svg; burger 28×28 at (24,16) both). R2 re-confirmed
(tapping Income in the ref's sheet navigated to `/income` with
`sheetStillOpen: true` + overlay count 1; the clone's sheet CLOSED + 390
fit + `/income`). R3 re-confirmed (no ref link active on `/` — all five
rail links `rgb(63,63,70)`/400 and no `<nav>` landmark; the clone
highlights Dashboard — white + gradient + 500 + landmark). R4
re-confirmed (ref scrollWidth 395 on `/` + `/dashboard`, 464 on
`/networth` full-page load; clone 390 on ALL six routes). Sheet link
geometry identical (Income at (20,185), 247×32, both).

---

## ToDo (TDD — specs first)

| # | Task | Test changes | Files |
|---|------|--------------|-------|
| 1 | G1: the net-worth delete-failure honest toasts (superset) + the reference's card-stays parity under a dead API | `tests/e2e/networth-error.spec.ts` NEW "asset delete failure keeps the card + error toast (v18)" — abort `**/api/assets/**` (DELETE), goto `/networth`, open the Share Portfolio card menu → Delete → the confirm bar's Delete, assert: the card heading is STILL present, the confirm bar is STILL up, AND the toast fires (title "Could not delete the asset", exact:true per the v16 live-region lesson); `unrouteAll({ behavior: "ignoreErrors" })` before spec end | `net-worth-view.tsx` |
| 2 | G1: the liability delete-failure twin (the second `void` site) | same spec, NEW "liability delete failure keeps the card + error toast (v18)" — abort `**/api/liabilities/**`, switch to the Liabilities tab, Credit Card menu → Delete → confirm, assert: the card stays, the toast fires ("Could not delete the liability", exact:true); unroute before end | `net-worth-view.tsx` |
| 3 | G1 pin: asset SAVE failure keeps the dialog open + toasts the error (the existing superset, unpinned until now) | same spec, NEW "asset save failure keeps the dialog open + error toast (v18 pin)" — abort `**/api/assets/**` (PATCH), open the Edit Asset dialog, click Save Asset, assert: the dialog heading is still visible, the toast fires ("Could not save the asset", exact:true); unroute before end | — (pins current behavior) |
| 4 | G1 pin: liability SAVE failure toasts the error (the second dialog catch, unpinned) | same spec, NEW "liability save failure keeps the dialog open + error toast (v18 pin)" — abort `**/api/liabilities/**`, open the Edit Liability dialog (Credit Card), click Save, assert: dialog still open, the toast fires ("Could not save the liability", exact:true); unroute before end | — (pins current behavior) |
| 5 | G2: harden the register duplicate-email spec against the Next.js route-announcer race (the spec waited on the wrong `role="alert"`) | same test, the assertion becomes `await expect(page.getByRole("alert").filter({ hasText: "A user with this email already exists" })).toBeVisible()` (the text filter scopes past the empty `__next-route-announcer__`; the retrying locator polls through the mount churn; the waitForSelector + one-shot evaluate pattern removed) | `tests/e2e/login-parity.spec.ts` |
| 6 | Docs: session log (`docs/session_36.md` — the session_35.md slot holds the incoming session-33 conversation summary), worklog, README/AGENTS/CLAUDE/SKILL alignment (the v18 pin paragraph + the net-worth error tier), probe README v18 rows | — | docs |
| 7 | Regression: full chain + live parity re-check (route-aborted net-worth delete reproduces the card-stays + the toast; a live-API delete round-trip still works) + screenshot refresh (no visible change expected — the fix is behavior-only; the failure branch never renders in the content-waiting shots) | — | — |

## Regression pin map (must NOT change)

- All six superset fixes (hamburger hit, sheet close-on-nav, root-URL nav
  highlight — rail AND sheet, no mobile overflow, Escape close, delete
  confirmations) and the v9–v17 pins (donut geometry + tooltip, tab
  icons + header chip, banner chrome, titles, placeholders, focus rings,
  the full-page loading state + its data-flight timing, the boot
  data-failure stay-in-app + one-shot toast + the 401-probe redirect,
  the calculator error tier)
- The net-worth HAPPY paths: the existing networth specs re-run green
  (create/edit/delete round-trips, tabs, summary, type groups, the
  header chip, the tab icons); the inline confirm-bar UI itself is
  superset-fix-#6 chrome — unchanged
- The v16 boot semantics: `bootError`/`clearBootError` untouched; the
  delete-failure toasts here are PER-CLICK (user actions), not one-shot
- The mutation-failure superset toasts' exact text ("Could not save the
  asset" / "Could not save the liability" — the new specs PIN them, not
  change them); the new delete toasts follow the budget-item delete's
  "Could not delete the {noun}" convention
- e2e fixture discipline: every spec that creates a row via the API
  restores it inside its own scope; the aborted handlers are unhooked by
  the specs' own scope (`unrouteAll({ behavior: "ignoreErrors" })`)
