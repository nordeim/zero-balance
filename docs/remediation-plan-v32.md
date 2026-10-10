# Remediation Plan v32 — Session-63 Parity Iteration

Date: 2026-10-10 · Scope: fresh two-site re-audit after the v31 baseline
(`157fecd` + the session-log commit `0c91904` on `main`; this session's
re-run of the whole chain green on the FIRST full run: lint ✓ ·
typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) ·
**164/164 e2e ✓** · 35/35 smoke ✓). The workspace had been RESET — the repo
re-cloned, the environment rebuilt (node_modules, `.env` with
`DATABASE_URL="file:../db/custom.db"`, `db/` re-pushed + re-seeded,
scandihaven re-cloned). Probes: the standing disciplines — one-shot
`agent-browser eval` (base64 via run-probe.sh for `$`-bearing probes),
the :3200 parity server inside ONE `with-server.sh` invocation, REAL key
presses for every focus-chrome claim (the v25 lesson: programmatic
`focus()` alone never proves a `:focus-visible` family — it DOES match
when the recent interaction was a keyboard press, which is why every
ring claim here is backed by a REAL Tab/Enter press), parked-pointer
settles, full computed strings, and full-settle re-reads.

## The sweep — method and results

The pass swept the three session-63 suggested surfaces — the **net-worth
card action dropdown menus' keyboard contract** (Radix Menu's
arrow/Home/End/typeahead/Escape), the **calculator line-item row
actions' Tab order**, and the **breakdown accordion's arrow semantics** —
plus the standing re-verification set (mobile-nav R1–R4 on BOTH sites,
data drift, the SEO pair, two VLM pairs) and the code audit (`npm audit`
= the same 5 dev-only ESLint `braces`/eslint-config-next advisories —
accepted, unchanged, dev-only; the secret-pattern scan matching only the
documented files; `.env.example` verified current).

- **Mobile navigation (the task focus) R1–R4 all re-verified live on BOTH
  sites — the 26th consecutive check.** R1: the reference's two `fixed
  top-0 z-[100]` toast containers still intercept the burger's center hit
  (hit `DIV.fixed.top-0.z-[100]`, scrollWidth 395), while the clone's burger
  hit is DIRECT on the svg with 390 fit. R2: the reference's sheet still
  traps after nav (measured on `/income` after the nav click with a robust
  fixed-panel detector — sheet open, body locked, 3 dark overlays; the
  v31 probe's white-bg detector missed the sheet this session, a probe
  lesson); the clone's closes (superset fix #2). R3: the reference marks
  nothing active on `/` (no `<nav>` landmark, no visible links at mobile);
  the clone highlights Dashboard + has the landmark. R4: the reference
  overflows 395 on `/`+`/dashboard` and 464 on `/networth`; the clone fits
  390 on all six routes. **The Tailwind v4 pins hold — the clone's mobile
  menu works as expected.**
- **Data drift clean (26th)**: allocation 30.5%, Balance `$3475.00`,
  income `$5000.00`/1 (Salary), savings `$1000.00`/1 (Emergency Fund),
  expenses `$525.00`/4 — verified BEFORE and AFTER the calculator probe
  cycles (the reference's Miscellaneous parent returned to `$0.00` after
  the add/delete restore; the census never moved).
- **SEO pair ✓** (live, both sites): robots.txt (allow-all + sitemap
  link) + sitemap.xml (5 URLs, weekly, 1.0/0.8) + the full head-metadata
  census — description / og:title / og:description / og:type /
  twitter:card / twitter:title / twitter:description /
  apple-mobile-web-app-title / title byte-identical; canonical + og:image
  keyed off `NEXT_PUBLIC_SITE_URL` (the env contract); charset + viewport
  present on both. Known non-pinned deltas: Next renders `User-Agent`
  (capital A) and serializes priority `1` (the reference's `1.0`) — both
  valid per the robots/sitemap protocols, documented; the clone's routes
  are lowercase (self-consistent, deliberate). The reference's
  `/manifest.json` endpoint 302s empty (broken); the clone's
  `manifest.webmanifest` serves the full v7-pinned document — a superset.
- **The net-worth dropdown menus' keyboard contract (suggestion #1) — NO
  finding, byte-identical on both sites at every axis**: click-open →
  focus on the menu CONTAINER (`role=menu`, tabindex −1, items all −1, no
  highlight); Enter-open (keyboard) → first item (Edit) focused +
  `data-highlighted`; ArrowDown → Edit (tabindex 0) → Delete; ArrowUp
  reverse; **no wrap at either end (clamped)**; Home/End work; **NO
  typeahead** (typing `d` from Edit stays on Edit on both); Escape →
  menu closed + focus returned to the trigger (the reference's trigger is
  unnamed, the clone's carries `aria-label="Actions for …"` — the
  documented v29 naming superset). Two items on both sites (Edit/Delete).
- **The calculator line-item row actions' Tab order (suggestion #2) — the
  populated-dialog census and Tab walk are byte-identical; ONE ring-family
  drift (G1 below)**: both sites' populated calculator renders exactly
  FOUR focusable stops in the same order — X (36px) → Add Item (110px) →
  the row's Edit action (32px) → the row's Delete action (32px), all
  `tabindex=0`, the row actions `opacity 1` inside their `opacity-0`
  hover-reveal container (focusable-while-invisible on BOTH — the reveal
  is hover-only, never focus). A REAL Tab walk reproduces the same
  sequence on both; after the last stop the reference EXITS to the page
  (no trap — its dialogs are plain divs) while the clone WRAPS to the X
  (the documented Radix-trap superset, the dialogs-wide family). The
  focused row action keeps `contOp:0` on both sites. **The drift: the
  reference's row-action buttons carry the shadcn focus family
  (`focus-visible:outline-none focus-visible:ring-1
  focus-visible:ring-ring`) — measured via REAL Tab, the focused Edit
  renders `outline: solid 2px rgba(0,0,0,0)` (invisible) +
  `box-shadow: rgb(255,255,255) 0 0 0 0, rgb(10,10,10) 0 0 0 1px,
  rgba(0,0,0,0) 0 0 0 0` (the 1px #0a0a0a ring with the white lead
  layer), at rest `box-shadow: none` — while the clone's raw
  `inline-flex h-8 w-8 … transition-colors hover:bg-accent` buttons
  render the browser-default `outline: auto 1px lab(…)` and
  `box-shadow: none` when keyboard-focused.**
- **The breakdown accordion's arrow semantics (suggestion #3) — NO
  functional finding**: the section rows are full `<button>`s on both
  sites (tabindex 0, same token set `w-full flex items-center
  justify-between cursor-pointer hover:bg-gray-50 p-2 -mx-2 rounded-lg
  transition-colors` — class ORDER differs, computed chrome identical:
  radius 8px, transparent bg, 0.15s color/bg transition); arrows and
  Home/End are INERT on both (focus never moves); Enter EXPANDS on both
  (focus stays on the row); Escape does NOT collapse on either (a shared
  reference quirk the clone deliberately matches). One DOM delta kept
  and now DOCUMENTED as a superset (S1 below): the clone's section AND
  category rows carry `aria-expanded` (accurate state reporting); the
  reference's carry none.
- **The reference's row delete is IMMEDIATE** (no confirm — measured:
  click Delete → item gone, "Based on 0 items", no confirm text, no red
  buttons). The clone's inline "Delete this line item?" confirm is the
  documented "unconfirmed deletes fixed" superset (CLAUDE.md's superset
  list) — its confirm buttons have no reference counterpart and need no
  parity work.
- **The VLM pairwise (two fresh pairs)**: the dashboard — DIFFERENT
  flag, DOM-explained (the clone's Dashboard-active rail = superset #3);
  the calculator — DIFFERENT flag, DOM-explained (the clone's X renders
  its v27-pinned 1px ring on open because Radix focuses it — the
  documented v29 superset).
- Probe-methodology notes: (a) the v31 R2 probe's white-bg sheet
  detector can miss the reference's sheet (this session it read
  `sheetOpened:false` while a robust fixed-panel + body-lock + overlay
  census proved it open — prefer structure/lock detection over
  background-color matching); (b) form fill finders must anchor on
  LABEL text or DOM order, never `placeholder*=name` (the reference's
  Provider field placeholder "Insurance Company Name" swallowed a
  "Test Item" fill meant for Item Name); (c) a calculator probe cycle
  that adds + deletes a line item RECALCULATES the parent amount to the
  line-item sum (zero, after the delete) — the dev `db/custom.db` needs
  the amount restored afterward (the seed's natural-key upsert does NOT
  restore it; the reference's Miscellaneous was `$0.00` by coincidence
  and needed nothing); (d) programmatic `focus()` DOES match
  `:focus-visible` when the recent interaction was a keyboard press —
  every ring claim in this plan is still backed by a REAL key press.

## Findings

### G1. [MED] The calculator's line-item row actions lack the reference's focus-visible ring family

The only production-code drift this session. The reference's calculator
row-action buttons (the 32px Edit and Delete icon buttons on each
line-item row) carry the shadcn Button focus family — measured on the
live reference (REAL Tab walk):

- class: `inline-flex items-center justify-center gap-2 whitespace-nowrap
  rounded-md text-sm font-medium transition-colors
  focus-visible:outline-none focus-visible:ring-1
  focus-visible:ring-ring disabled:pointer-events-none
  disabled:opacity-50 [&_svg]:pointer-…` (the full shadcn base)
- at rest: `box-shadow: none`, `outline: none 3px` (style none)
- keyboard-focused (REAL Tab): `outline: solid 2px rgba(0,0,0,0)`
  (transparent — the v3 `outline-none` form), `box-shadow:
  rgb(255,255,255) 0 0 0 0, rgb(10,10,10) 0 0 0 1px, rgba(0,0,0,0) 0 0
  0 0` — the 1px `#0a0a0a` ring (`--color-ring: #0a0a0a`) with the
  white 0-width lead layer, the exact family the clone already pins on
  the shadcn Button base (`src/components/ui/button.tsx`) and on the
  item-card raw actions (`src/components/budget/item-card.tsx:98,107`).

The clone's row actions (`src/components/budget/calculator-dialog.tsx`,
the `h-8 w-8` Edit/Delete buttons) are raw buttons WITHOUT the family:
keyboard focus renders the browser-default `outline: auto 1px lab(…)`
— an unpinned ring, the same drift class the v25/v27 sessions fixed on
the auth submits and the dialog action buttons (never copy one family's
color onto another; here the family is the standard `ring-ring`
near-black, measured).

**Fix (TDD):** add `focus-visible:outline-none focus-visible:ring-1
focus-visible:ring-ring` to both row-action buttons' className strings.
No geometry/color change at rest (the family is focus-only). The e2e pin
(REP below) uses the established `focus({ focusVisible: true })` probe
(the dialog-buttons spec's v11 pattern) PLUS a REAL-Tab verification.

### S1. [SUPSET, document + pin] The breakdown rows' aria-expanded (accurate state reporting the reference lacks)

The clone's Net Zero Breakdown section rows (`dashboard-view.tsx:245`)
and category rows (`:281`) render `aria-expanded={expanded}` /
`aria-expanded={catOpen}`; the reference's rows have NO attribute. The
value is accurate on the clone (measured: `"false"` at rest, `"true"`
after Enter-expand). This is an a11y superset in the same family as the
kept `aria-label` supersets (the reference's row actions and card
triggers are unnamed; the clone's are labeled) — invisible, correct,
and it does not create spurious semantics (unlike the recharts-3
a11y-layer attributes the v31 G1 fix removed). It was added in the v2
era (`8b82e4c`) without a reference measurement or documentation — this
session measures it, KEEPS it as a deliberate superset, and PINS it so
a future parity sweep doesn't "fix" it away.

**No production change.** New e2e assertions in `breakdown.spec.ts`
(the section row reads `aria-expanded="false"` at rest and `"true"`
when expanded) + this documentation.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | G1 RED: the calculator row-action focus-family e2e test (fails on the drifted build) | test | `tests/e2e/calculator.spec.ts` |
| 2 | G1 GREEN: add the `focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring` family to the two row-action buttons | fix | `src/components/budget/calculator-dialog.tsx` |
| 3 | G1 pin-sanity: remove the family → the test fails → restore | verify | same |
| 4 | S1 pin: the breakdown rows' `aria-expanded` superset assertions (rest + expanded) | test | `tests/e2e/breakdown.spec.ts` |
| 5 | S1 pin-sanity: remove the attribute → the pin fails → restore | verify | `src/components/budget/dashboard-view.tsx` |
| 6 | Live re-verification on the :3200 parity server (the focused row action's ring; the standing mobile-nav R1–R4 spot check) | verify | — |
| 7 | The 16 screenshots regenerated | docs | `docs/screenshots/` |
| 8 | The v32 probes persisted + the probe README updated | docs | `scripts/parity-probes/` |
| 9 | Docs aligned (README, CLAUDE, AGENTS, SKILL, session_66, the narrative, worklog) | docs | repo root + `docs/` |
| 10 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `calculator-dialog.tsx` rows: the two `h-8 w-8` buttons at the
  `opacity-0 group-hover:opacity-100` container — confirmed the family
  is absent today (grep: no `focus-visible` in the file); the item-card
  precedent (`item-card.tsx:98,107`) uses exactly the family string this
  plan adds; `--color-ring: #0a0a0a` is the token the reference's
  measured `rgb(10,10,10)` ring resolves to.
- `calculator.spec.ts` already has the row lifecycle ("add a line item →
  parent recalculates" at :112 creates "Contents Insurance" $25 on Rent,
  and the row-chrome test at :188 asserts the rest chrome) — the new
  test rides the same fixture (create the row, park the pointer, probe
  the focused Edit/Delete chrome, then the existing delete-restore
  pattern cleans up). NO existing assertion touches the row actions'
  focus state (grep: `focus` in calculator.spec.ts matches only the
  input-focus helpers) — no collision.
- `breakdown.spec.ts` has five tests; none read `aria-expanded` (grep
  clean) — the S1 pin is additive.
- The e2e DB contract: the calculator spec's tests create + delete
  their own fixtures and restore the parent amount (the "deleting a line
  item recalculates the parent back" test at :158) — the new test
  follows the same discipline.
- The chain gate: lint → typecheck → 108 unit → build → 164 e2e (165
  after the G1 test; the S1 assertions extend an existing test — or add
  one, 166) → 35 smoke.
