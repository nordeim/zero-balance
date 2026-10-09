# Remediation Plan v22 — Session-43 Parity Iteration

Date: 2026-10-09 · Scope: fresh two-site re-audit after the v21 baseline
(`34f0911` on `main`, all green per the prior session's records — cloned
clean into a reset sandbox: `.env` with `DATABASE_URL="file:../db/custom.db"`
re-created, `db/` at the repo root re-pushed + re-seeded, node_modules
installed, Vitest/Playwright configs verified intact). Baseline chain
re-run BEFORE any work: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ ·
**141/142 e2e — ONE FAILURE** (the finding below, deterministic on re-run)
· smoke pending the post-fix full chain. Probes: one-shot `agent-browser
eval` scripts (sessions `ref24`/`clone24`, desktop 1280×800 + 390×844
resized per check), the standalone parity server on :3200 booted per
command through `scripts/with-server.sh` (local copy:
`scripts/parity-probes/with-server.sh`), and the VLM visual sweep
(`z-ai vision` pairs, the v19–v21 methodology — every flag DOM-verified
before it becomes a finding).

## The sweep — method and results

The pass swept the session-42 log's three suggested surface classes — the
line-item-populated CALCULATOR at MOBILE viewport (v21 compared it at
desktop only), the line-item EDIT SUB-DIALOG (the nested dialog's
populated state, never measured), and a KEYBOARD-NAVIGATION sweep on the
app views (Tab order + focus chrome) — plus the standing task-focus
re-verification (mobile navigation R1–R4 + reference data-drift check),
the standing SEO check (robots/sitemap live on both sites), and the code
audit (`skills/code-review-and-audit` native-CLI fallback: lint/tsc/tests
green; `npm audit` = the same 5 dev-only ESLint `braces` advisories, no
patched release — accepted, unchanged; secret-pattern scan clean — no key
material anywhere outside the documented redacted wrapper placeholder;
scandihaven current at `d4789c3`, patterns already reflected).

- **Mobile navigation (task focus) R1–R4 re-confirmed, all four live:**
  R1 (the reference's TWO `fixed top-0 z-[100]` toast containers still
  intercept the burger's center hit at (38,30), `pe:auto`, 390×32 each;
  the clone's hit is DIRECT on the svg, viewport `pe:none`; burger 28×28
  at (24,16) both), R2 (the reference's sheet still traps after nav —
  `sheetStillOpen: true`; the clone's closes; sheet 288px + Income link
  (20,185) 247×32 identical), R3 (nothing active on `/` on the reference
  — all five rail links `rgb(63,63,70)`/400, no `<nav>` landmark; the
  clone highlights Dashboard), R4 (the reference overflows 395px on
  `/`+`/dashboard`, 464px on `/networth`; the clone fits 390 on all six
  routes). The Tailwind v4 pins hold — the clone's mobile menu works as
  expected.
- **Data drift clean (sixteenth consecutive check)**: reference unchanged
  since session 19 (allocation 30.5%, income `$5000.00`/1 item, savings
  `$1000.00`/1, expenses `$525.00`/4 items, Balance `$3475.00`).
- **SEO check (the brief's standing ask) PASSES**: the clone now serves
  `/robots.txt` (allow-all + sitemap link) and `/sitemap.xml` (five URLs,
  weekly, priorities 1/0.8) — verified live on :3200 against the
  reference's files; head metadata parity re-verified on `/login` (title,
  description, OG/Twitter cards, canonical — origin-keyed fields correctly
  differ, `NEXT_PUBLIC_SITE_URL`).
- **Mobile calculator pair (VLM + DOM)**: the first pair flagged three
  diffs — the toast (the documented success-toast superset), the
  "Will update category total" hint (data-driven: the reference's Rent
  parent `$25.00` equals its line-item sum so its identical conditional
  hides the hint; the clone's seeded `$1850` Rent does not — both
  conditionals match), and the row actions "missing" on the clone —
  DOM-verified a SCREENSHOT-PROCEDURE ARTIFACT: the reference's shot
  caught its row under the parked mouse (a real click had left the
  pointer inside the row, `.group:hover` matched, opacity 1), while the
  clone's shot was taken with the pointer at the Save button. Re-measured
  with the pointer parked away on BOTH sides: identical container classes
  (`flex items-center gap-1 opacity-0 group-hover:opacity-100
  transition-opacity`), opacity "0" at rest, opacity "1" under a real row
  hover, 32×32 buttons, 16px icons, `rgb(10,10,10)`/`rgb(220,38,38)`
  colors. Re-taken pair: only the X-close claim remains — DOM-refuted for
  the FOURTH consecutive pass (identical 29×36 at mobile, 0px border,
  transparent bg, radius 6, 16px svg `#0a0a0a` both sides). **Chrome
  parity holds.**
- **Keyboard sweeps (dashboard `/` + income view, both sites)**: Tab order
  IDENTICAL (the five rail links → Add button → search input → filter
  select); the nav links render the blue 2px `#3b82f6` sidebar-ring on
  BOTH sites under Tab; the interactive elements (Add button, selects)
  render the shadcn 1px `#0a0a0a` ring + ambient shadow on both (the
  clone's computed strings carry extra TRANSPARENT lead layers — v4's
  ring implementation, invisible); the stat buttons keep the
  browser-default outline on both. **No findings** — but the pass
  reinforced the v11 truncation lesson AGAIN: two first-read "missing
  ring" scares were 60-char truncations of multi-layer strings (the
  visible layer trails the leads).
- **Register verify-email e2e failure (the baseline's one red)**: see G1.

### G1. [MED] verify-email spec: a parked-pointer race reads the Verify button mid-hover-transition

The baseline chain's only failure: `tests/e2e/verify-email.spec.ts:47`
"the register flow lands on the verify state with the reference chrome"
— the 44px primary-button assertion reads `rgb(19, 27, 46)` where
`rgb(15, 23, 42)` (#0f172a) is expected. Root cause (probed with the
pointer parked vs away on the :3100 build): Playwright's mouse stays at
the "Create account" click position; when the card swaps to the verify
state, the "Verify email" button lands under the parked pointer;
`:hover` applies and the `transition-all duration-200` from
`bg-[#0f172a]` toward `hover:bg-[#1e293b]` is IN FLIGHT when the
evaluate lands (`rgb(19,27,46)` ≈ 27% through; settled = `rgb(30,41,59)`).
The APP is correct: resting `#0f172a` (measured pointer-away), hover
`#1e293b` (the v13-pinned sign-up-family hover, by design). The prior
session's green first run was timing luck — the evaluate raced ahead of
the hover application. This is the repo's own documented transition
discipline (AGENTS.md: "transitions need a ~300ms settle before reading
computed styles"; the v13 "350ms transition settle" lesson) applied to a
NEW surface: a state-swap that re-renders a button UNDER the parked
pointer.

**Fix (spec-only, TDD-flavored — the RED is the failing run above):**
- In `registerFreshAccount` (after the verify-state heading assert): park
  the pointer far away (`page.mouse.move(5, 5)`) and settle ~350ms —
  deterministic for every test in the file (tests 2–4 then move the
  pointer themselves via their interactions).
- No app change. No other spec shares the pattern (login-parity `goto`s
  directly — its mouse never parks on a swapped-in button; grep-verified).

### G2. [MED] Line-item sub-dialog: the reference's 85vh panel cap + space-y-5 form gap (the wrong dialog family)

Measured live on the reference at BOTH viewports (the nested dialog's
populated Edit state, never measured before — the session-42 log's
suggestion):

- **Desktop 1280×800**: panel 672×680, classes `bg-white rounded-2xl
  shadow-2xl max-w-2xl w-full max-h-[85vh] overflow-y-auto`, form
  `p-6 space-y-5` (content 69px header + 1002px form, scrolls inside).
- **Mobile 390×844**: panel 358×717 (= 85vh), inputs 7 × 310×36, buttons
  X 36×36 / Monthly 310×36 / Active 310×36 / Cancel 150×36 / Save Item
  148×36.

The clone renders the line-item dialog on the GENERIC `.zb-modal-panel`
family (max-height 90vh, form `space-y-6 p-6`): desktop 672×**720**,
mobile 358×**760**, form 1010px (gaps 24px vs the reference's 20px —
inputs/buttons/widths all identical). The reference's calculator dialog
is a different family (`max-w-3xl max-h-[85vh] overflow-hidden flex
flex-col` — the clone's `calculator-dialog.tsx` already matches via its
inline style), and its budget-item dialog is `max-w-2xl max-h-[90vh]
overflow-y-auto` + `space-y-6` (the clone's `budget-item-dialog.tsx`
matches via the bare `zb-modal-panel`). The line-item dialog is the
reference's THIRD family — `max-w-2xl` + **85vh** + `overflow-y-auto` +
form **`space-y-5`** — and the clone drifted it onto the budget-item
family. Height delta: 40px (desktop) / 43px (mobile); form-row gap delta
4px × 2 rows.

**Fix:**
- `src/components/budget/line-item-dialog.tsx`: the `<DialogContent>`
  gains an inline `maxHeight: "85vh"` (the calculator's precedent — inline
  style overrides the zb-modal-panel default; max-width 42rem and
  overflow-y-auto already match), with a comment naming the measured
  family.
- Same file: the form class `space-y-6 p-6` → `p-6 space-y-5`.
- **Pinned by** a new e2e test in `tests/e2e/dialog-buttons.spec.ts` (the
  dialog-chrome home): open the seeded Rent calculator → open the Edit
  Line Item sub-dialog → assert the panel's computed `max-height`
  ≈ 85vh (680px at 800 viewport) and the form's measured row gap 20px
  (the field-grid bottom → Notes top distance). RED at the current
  90vh/24px state.

## Validation of this plan against the codebase

- G1: the spec's `registerFreshAccount` ends with the heading assert
  (line 34) — the chrome read at line 58 follows immediately; no
  `mouse.move` or settle exists anywhere in the file (grep-verified).
  The app-side classes are `bg-[#0f172a] hover:bg-[#1e293b]` +
  `transition-all duration-200` (login-card.tsx:607 — the v13-pinned
  sign-up family, correct). The probe evidence: rest `rgb(15,23,42)`,
  parked-settled `rgb(30,41,59)`, mid-transition `rgb(19,27,46)`.
- G2: `line-item-dialog.tsx:117-120` renders bare `<DialogContent>` (the
  zb-modal-panel: `max-height: 90vh` per globals.css:267) + form
  `space-y-6 p-6` (line 120); `calculator-dialog.tsx:100-110` holds the
  inline `maxHeight: "85vh"` precedent; `budget-item-dialog.tsx:151-156`
  holds the matching budget family (bare DialogContent + space-y-6 —
  correct as-is). No existing spec pins the sub-dialog's panel cap or
  form gap (grep across tests/e2e — the dialog-buttons spec pins X-close
  69px header, labels, tiles; nothing about maxHeight/row gaps).

## Execution order (TDD)

1. **G1**: the RED already exists (the baseline failure) → patch
   `registerFreshAccount` (pointer park + settle) → re-run
   `verify-email.spec.ts` (4/4 GREEN).
2. **G2**: write the new sub-dialog-family e2e test (RED at 90vh/24px)
   → the inline `maxHeight` + `space-y-5` form fix (GREEN) → re-run the
   dialog-buttons spec.
3. Full clean-check chain: `npm run lint && npm run typecheck && npm test
   && npm run build && npm run test:e2e` + `bash scripts/smoke-test.sh`.
4. Live parity re-verification of G2 on :3200 vs the reference (panel cap
   + form gap at both viewports); regenerate the docs screenshots (the
   calculator-family shots if the sub-dialog appears); align
   README/CLAUDE/AGENTS/SKILL/session log/worklog.

## Risk notes

- G1's pointer park must come AFTER the verify-state renders (parking
  before the swap would leave the pointer wherever the flow put it) —
  the park lands inside `registerFreshAccount` right after the heading
  assert, where the state is guaranteed rendered.
- G2's inline `maxHeight` must not fight the zb-modal-panel's
  `overflow-y: auto` (it doesn't — the property is orthogonal; the
  calculator's `overflow: hidden` + flex column is a different family
  and stays untouched).
- The e2e rate-limit budget is unchanged (no new logins; the new G2 test
  rides the auth setup's storageState).
