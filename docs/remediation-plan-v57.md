# Remediation Plan v57 — The items-view desktop 1280 VLM standing pair +
# the item-card footer + badge-row census (PIN-ONLY — no production-code
# change; the seventh iteration since v46, the pin-only line's continuation
# after the v55 fix)

Date: 2026-10-13 · Scope: the session-134 v57 queue's own standing-check
suggestion — "a fresh VLM pair on the ITEMS view's desktop 1280 state (the
search-input glyph swap surface + the item-card grid at 1280)" — plus the
51st standing checks. Measured live on BOTH sites via the v57 family
(vlm-shots-v57.sh + clone-vlmshots-v57.sh + vlm-compare-v57.mjs — the
desktop 1280x800 pair; vlm-arbit-v57.sh + badge-census-ref-v57.sh +
badge-census-clone-v57.sh — the DOM arbitration + the footer/badge census;
ref-standing-v51.sh + standing-checks-v51.sh — the 51st standing checks).
All READ-ONLY on the reference (the v46 rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **255 e2e ✓ (115 + 141, two ordered chunks, both exit 0, zero
failures)** · 35/35 smoke ✓. The 51st standing checks all clean (mobile-nav
R1–R4 both sides — the reference's four bugs ALL live [toast-blocker,
sheet-trap, no-landmark, the 464 /networth overflow], the clone's mobile
menu VERIFIED WORKING, the data census intact ["1 items · $25,000"
networth / "1 items · $5000.00" income], the SEO pair live on both sites).
The trap-log scan CLEAN. The v56 pin verified (the hero-desk census in
dashboard.spec.ts).

## The v57 sweep — what the measurement found

- **THE DESKTOP 1280x800 VLM PAIR (the session-134 queue item): PAIR 1
  (the income view — the v55 search-glyph swap surface + the item-card
  grid) and PAIR 2 (the expenses view — the same grid family + the
  payment-method filter row) each flagged only DATA-CLASS items:**
  1. the user avatar ("U" vs "D") — the logged-in user's initial, the
     documented user-identity data class;
  2. the header subtitle + the card counts + the item names/amounts/dates
     — the seed-data class (the reference's own 1-item seed vs the
     clone's dev seed: "1 items · $5000.00" vs "2 items · $5550.00");
  3. the expense-card footer's payment chips — **DATA-CONDITIONAL, not
     style: the footer row's chrome is byte-identical on both sites**
     (flex justify-between 12px rgb(107,114,128) h 16; each span flex
     gap 4px with the 12×12 gray icon) — the reference's own income
     card renders the SAME two-child structure (the date + "Bank
     Account") while its expense items carry no payment methods (footer
     1 child); the clone's items carry them (2 children);
  4. the badge wrap — **DATA-CONDITIONAL: the badge row's chrome is
     byte-identical** (flex wrap, 8px gap, 12px mb; every badge flex
     center / 6px radius / 2px 10px pad / 12px/600 / h 22 / 12×12 icons)
     — the clone's Recurring superset badge (the 4th badge) wraps the
     row to h 52 (22 + 8 + 22), the reference's 3-badge rows stay h 22;
  5. the classification badge colors (need red / want blue) — the
     documented data class, already locked by badge-colors.spec.ts.
  **The pair CLEAN per the v43 rule** (every flag DOM-arbitrated:
  vlm-arbit-v57.sh + the badge-census pair).
- **THE GRID CENSUS (both sites, byte-identical): the 960px 3-column
  grid (each column ~=309.33px) with the 16px gap; the card chrome
  (309 / 20px pad / 12px radius / 1px solid rgb(229,231,227) / white) —
  the v45 F1a pin's own values, unchanged.**
- **NO production gap found — v57 is PIN-ONLY** (the v53/v54/v56 class).
  The gap in the pin COVERAGE: the item-card's FOOTER structure (the
  two-children conditional render — the date + payment-method spans)
  and the BADGE-ROW chrome (the geometry, not just the color maps the
  badge-colors spec locks) are unpinned at desktop 1280; the /expenses
  grid census is unpinned (the v45 pin covered /income only). The v57
  deliverable pins them.

## Findings

### F1. [PIN] the items-card footer + badge-row census at 1280 (the v57 pin)

Two new tests in `tests/e2e/items.spec.ts` — the describe
"items card footer + badge census at 1280 (v57 — plan F1)":

**F1a** ("the income card's footer row + badge chrome") at
`setViewportSize({ 1280, 800 })` on /income (the Freelance card, the
date-DESC first): (1) the footer row: flex / items-center /
space-between / 12px / rgb(107, 114, 128) / h 16 / exactly 2 children —
the date span (flex gap 4px, 12px, gray, the 12×12 calendar icon at
gray) + the payment span (flex gap 4px, "PayPal", the 12×12
credit-card icon); (2) the badge row: flex / wrap / 8px gap / 12px mb /
h 22 / 3 badges (want, monthly, active — Freelance is not recurring);
(3) every badge: flex / center / 6px radius / 2px 10px pad / 12px /
600 / h 22; the first badge's icon 12×12; (4) the card chrome control
(the v45 F1a values: 309 / 20px / 12px).

**F1b** ("the expenses grid + the first card's footer + the wrapped
badge row") on /expenses (the Entertainment card, the date-DESC
first): (1) the grid: 960 wide / 16px gap / 3 children / the 3-column
template (each ~=309.33px); (2) the card chrome (309 / 20px / 12px);
(3) the footer: the same chrome + exactly 2 children, the payment span
matching /Bank Transfer|Credit Card/; (4) the wrapped badge row: flex /
wrap / 8px gap / h 52 (the measured two-line layout: 22 + 8 + 22) / 4
badges (want, monthly, Recurring, active — the clone's superset
Recurring badge is the wrap's driver; the reference's 3-badge rows
stay h 22 — the wrap is the data class, the row chrome is identical).

### F2. [VLM-PAIR] the items-view desktop 1280 standing pair — DONE, CLEAN

The session-134 v57 queue's own suggestion, executed: PAIR 1 (the
income view) + PAIR 2 (the expenses view). Every flag DOM-arbitrated
to the documented classes (the avatar, the seed data, the
payment-method conditional footer, the badge wrap, the classification
colors). The pair scripts + the arbitration + the census persisted
(P1).

### S1. [MUTATION-SANITY] the pin bites

(a) the footer's `text-xs` → `text-sm` (12px → 14px,
src/components/budget/item-card.tsx:189) → the F1a footer fs assertion
FAILS ("12px" vs "14px"; the footer h 16 → 20);
(b) the badge row's `gap-2` → `gap-4` (8px → 16px, :160) → the F1a
badgeRow gap assertion FAILS ("8px" vs "16px");
(c) the first badge's `px-2.5` → `px-2` (2px 10px → 2px 8px, :163) →
the F1a badge pad assertion FAILS ("2px 10px" vs "2px 8px") — the
line-scoped mutation hits only the classification badge; the loop over
badges catches it.
All restored → GREEN (2/2 + the setup). Each mutation with the
standalone REBUILD as a SEPARATE command (the v47–v54 execution
lesson).

### F3. [TEST-INFRA] the not-found G7 flake fix (the only non-pin change)

The full-chain re-run surfaced a genuine (not load-induced) flake:
not-found.spec.ts's "Go Home navigates to the dashboard" — three
chunk-run failures in one session, and the root-cause probe
(`--repeat-each=8` in isolation) reproduced it at ~1-in-8 on an IDLE
machine. The cause: the file's logged-out opt-out (line 15,
`test.use({ storageState: { cookies: [], origins: [] } })`) applied to
a test that asserts an AUTHENTICATED surface — logged-out, the
"Budget Dashboard" heading only exists in the ~50-180ms window between
the page boot and the RequireSession /login redirect, a race
toBeVisible's polling sometimes loses (the trace: /api/auth/me at
.137, the /login?from_url client-nav at .187 — the heading lives
inside that gap). The fix (test-only, no production code): the test
moves into its own describe carrying a describe-scoped storageState
override (`tests/e2e/.auth/user.json` — the same AUTH_STATE the
chromium project uses; describe-scope beats file-scope), the header
comment documents the exception. Verified: `--repeat-each=10` → 21/21
passed (the pre-fix rate ~1-in-8), the full spec 7/7, the whole chunk
2 green (143 passed).

### P1. [PROBE-INFRA] the v57 probe family persisted

vlm-shots-v57.sh + clone-vlmshots-v57.sh + vlm-compare-v57.mjs (the
desktop 1280 pair), vlm-arbit-v57.sh + badge-census-ref-v57.sh +
badge-census-clone-v57.sh (the DOM arbitration + the footer/badge
census, both sides), ref-standing-v51.sh + standing-checks-v51.sh (the
51st standing checks), plus the probe README's v57 section. The v57
probe lessons: (1) the combined arbitration probe's badge-row finder
must walk the card's DIRECT children (the row is a direct child,
class flex flex-wrap gap-2 mb-3 — a nested querySelectorAll filter
misses it); (2) the clone-side with-server heredoc must be QUOTED
(<<'EOF') when it carries a $-expanded census variable — the unquoted
heredoc re-parses the JS's double quotes through the inner bash and
strips them (the badge-census-clone-v57.sh lesson; the debug variant
carries the fix); (3) the reference's expenses items carry NO payment
methods — its expense-card footers render one child (the date alone)
while its income card carries two (the date + "Bank Account") — the
conditional render is the parity contract, not a drift.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v57 paragraph. D2: CLAUDE.md — the E2E count
255 → 257 + the v57 family entry. D3: README — the counts + the v57
row. D4: the SKILL doc — the Session 92 row + the state line. D5: the
PAD — a v1.1.14 revision block. D6: the probe README — the v57
section. D7: session_137.md (the formal log) + the repo worklog
Session 91 + the ledger list. D8: the workspace worklog.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1's pin: the two-test footer + badge census describe → GREEN (pin-only, no RED phase — the surface is already correct; the pin is the deliverable) | test | `tests/e2e/items.spec.ts` |
| 2 | S1(a)–(c): the three pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`, run as a SEPARATE command) | verify | `src/components/budget/item-card.tsx` |
| 2b | F3: the not-found G7 flake fix — the Go Home test's describe-scoped storageState override (test-only; `--repeat-each=10` → 21/21, the pre-fix rate ~1-in-8) | test | `tests/e2e/not-found.spec.ts` |
| 3 | The probe scripts persisted + the probe README's v57 section | docs | `scripts/parity-probes/` |
| 4 | The full chain re-run (108 unit · **257** e2e [+2: the v57 footer + badge pins] · 35 smoke + lint + typecheck + build) — all green, two ordered chunks | verify | — |
| 5 | The 16 screenshots regenerated (expect ALL byte-identical — the pin-only invariant; regenerate to confirm, keep whichever diff) | docs | `docs/screenshots/` |
| 6 | D1–D8 + the formal session log (session_137.md) + the repo worklog Session 91 + the SKILL doc Session 92 row | docs | repo root + `docs/` |
| 7 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/item-card.tsx:160` — the badge row's
  `mb-3 flex flex-wrap gap-2`; `:163` the classification badge's
  `px-2.5 py-0.5` (the line-scoped mutation target); `:189-199` the
  footer `flex items-center justify-between text-xs` + the two
  conditional spans (the date + `item.paymentMethod ? ... : null`);
  `:121` the 8×8 category dot; `:155-157` the 24px amount.
- The e2e contract: the v57 describe runs AUTHENTICATED via the setup
  project's storageState; the deterministic e2e seed (prisma/seed.ts —
  the SAME seed the :3200 parity server runs) puts Freelance (want,
  PayPal, non-recurring, Oct 8) first on /income and Entertainment
  (want, Credit Card, recurring, Oct 11) first on /expenses — both by
  the date-DESC order; the pin's texts/badge counts follow. The footer
  height 16 / the badge h 22 / the wrapped row h 52 (22 + 8 + 22) are
  deterministic arithmetic.
- The existing pins are SAFE: the v45 F1a 1280 grid census pins the
  /income grid + card chrome + title row + kebab + hover (the v57 F1a
  re-asserts the card chrome as its control — same values, no
  conflict); the v52 F2/F3 mobile censuses pin the footer + date span
  at 390 (the v57 pins the same chrome at 1280 — viewport-scoped, no
  conflict); the v54 F1 savings internals census pins the chip family
  at 390 on the SAVINGS goal card (the v57 pins the item-card badge
  family at 1280 — different view, no overlap); badge-colors.spec.ts
  locks the classification color maps (the v57 locks the GEOMETRY —
  the documented split).
- The chain gate: lint → typecheck → 108 unit → build → 255 e2e
  (**257** after: +2 — the v57 footer + badge pins) → 35 smoke. The
  chain re-run surfaced the not-found G7 flake (F3) — fixed test-only,
  then the full chain green: 115 + 143 (two ordered chunks) + 108 unit
  + 35 smoke + lint + typecheck + build.
- Execution notes: `pkill -f agent-browser` + the stale-session sweep
  before every agent-browser run; a rebuild swaps .next/standalone
  UNDER a running parity server — the with-server.sh boots fresh per
  command; the reference session EXPIRES between long eval gaps —
  re-login via the same eval before any follow-up census; the
  clone-side heredoc quoting lesson (P1.2).
- DEFERRED queue (unchanged, all need reference WRITES — out of bounds
  under the v46 read-only rule): the reference-side verify-email panel
  census, the forgot-confirm state census, the calculator EMPTY-state
  census, the line-items dialog glyphs. The reference's trending-down
  glyph stays data-conditional (its net is positive — the 51st data
  census confirms "1 items · $25,000" unchanged, no flip to measure).
- The v58 queue (suggestions): the SAVINGS view's desktop 1280 VLM
  pair (the items family's remaining view — income + expenses are now
  covered), the calculator view's desktop 1280 pair (the panel + row
  surfaces), and the deferred reference-write censuses (unchanged).
