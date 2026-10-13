# Remediation Plan v58 — The savings-view desktop 1280 VLM standing pair +
# the savings goal-card's footer + badge-row census (PIN-ONLY — no
# production-code change; the eighth iteration since v46, the pin-only
# line's continuation)

Date: 2026-10-13 · Scope: the session-137 v58 queue's own first
suggestion — "the SAVINGS view's desktop 1280 VLM pair (the items
family's remaining view — income + expenses are now covered by the v57
pair; the savings goal-card's 1280 state is unpinned at the pair
viewport, its internals pinned at 390 only [v54 F1])" — plus the 52nd
standing checks. Measured live on BOTH sites via the v58 family
(vlm-shots-v58.sh + clone-vlmshots-v58.sh + vlm-compare-v58.mjs — the
savings view's desktop 1280x800 pair; savings-census-ref-v58.sh +
savings-census-clone-v58.sh — the DOM arbitration + the
grid/card/footer/badge census, both sides;
ref-standing-v52.sh + standing-checks-v52.sh — the 52nd standing
checks). All READ-ONLY on the reference (the v46 rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **257 e2e ✓ (104 + 138 + 14, three ordered chunks this
session — the chunk-regex lesson below, zero failures)** · 35/35 smoke
✓. The 52nd standing checks all clean (mobile-nav R1–R4 both sides —
the reference's four bugs ALL live [toast-blocker
hitIsBurgerChild:false, the sheet-trap overlayCount:1, the no-landmark
navLandmark:false, the 464 /networth overflow], the clone's mobile
menu VERIFIED WORKING, the data census intact ["1 items · $25,000"
networth / "1 items · $5000.00" income], the SEO pair live on both
sites).

## The v58 sweep — what the measurement found

- **THE DESKTOP 1280x800 VLM PAIR (the session-137 queue item): the
  SAVINGS view pair flagged only DATA-CLASS items, every one
  DOM-arbitrated (the v43 rule):**
  1. the header stats + the card counts/names/amounts/dates — the
     seed-data class (the reference's own 1-item seed ["1 items ·
     $1000.00", "Emergency Fund" $1000, "Home Savings"] vs the
     clone's dev seed ["2 items · $1250.00", Investments $450 +
     Emergency Fund $800, "Index Funds"/"Safety Net"]);
  2. the savings card's FOOTER content — **DATA-CONDITIONAL, not
     style: the footer row's chrome is byte-identical on both sites**
     (flex justify-between 12px rgb(107,114,128) h 16; each span flex
     gap 4px, 12px, gray, the 12×12 gray icon) — the reference's own
     savings item carries NO paymentMethod so its footer renders ONE
     child (the date alone, "Oct 7, 2026" + the 12×12 calendar icon);
     the clone's savings items carry paymentMethods so the footer
     renders the SAME two-child structure the reference's own income
     card renders (the date + the "Brokerage" chip with the 12×12
     credit-card icon) — the v57 conditional-footer contract, now
     measured on the third view;
  3. the badge family — **DATA-CONDITIONAL: the badge-row chrome is
     byte-identical** (flex wrap, 8px gap, 12px mb; every badge flex
     center / 6px radius / 2px 10px pad / 12px/600 / h 22 / the
     iconed badges' 12×12 icons) — the reference's savings item is
     classified "need" (the red family: bg rgb(254,242,242) + 1px
     solid rgb(254,202,202) — the badge-colors.spec.ts need map) while
     the clone's are "savings" (the green family: bg rgb(240,253,244)
     + 1px solid rgb(187,247,208) — the badge-colors.spec.ts savings
     map): the CLASSIFICATION VALUE is the data class, the COLOR MAPS
     are locked by badge-colors.spec.ts; the monthly (rgb(250,245,255)
     purple-50) + active (rgb(248,250,252) slate-50) badges are
     byte-identical both sides; the clone's Recurring superset badge
     (the 4th, green + the 12×12 repeat icon) wraps the row to h 52
     (22 + 8 + 22) — the reference's 3-badge row stays h 22 (the
     documented wrap class, the v57 arithmetic);
  4. the grid — **byte-identical chrome** (960 wide, 16px gap, the
     3-column template each ≈309.33px; the reference's own 1 savings
     card vs the clone's 2 — the seed class; the card chrome
     309 / 20px pad / 12px radius / 1px solid rgb(229,231,227) /
     white — the v45 F1a pin's own values).
  **The pair CLEAN per the v43 rule.**
- **NO production gap found — v58 is PIN-ONLY** (the v53/v54/v56/v57
  class). The gap in the pin COVERAGE: the savings view's 1280 state —
  the /savings grid census + the savings goal-card's two-children
  conditional footer + the wrapped 4-badge row are unpinned at 1280
  (the v45 pin covered /income only; the v57 pins covered /income +
  /expenses; the savings internals are pinned at 390 only [v54 F1]).
  The v58 deliverable pins them.

## Findings

### F1. [PIN] the savings goal-card's footer + badge census at 1280 (the v58 pin)

One new test in `tests/e2e/items.spec.ts` — appended to the v57
describe's file as its own describe "the savings goal-card census at
1280 (v58 — plan F1)":

**F1** ("the savings grid + the goal card's footer + the wrapped badge
row") on /savings (the Investments card, the date-DESC first): (1) the
grid: 960 wide / 16px gap / 2 children (the e2e seed's Investments +
Emergency Fund) / the 3-column template (each ≈309.33px); (2) the card
chrome (the v45 control: 309 / 20px / 12px); (3) the footer: the
byte-identical chrome (flex / space-between / 12px /
rgb(107,114,128) / h 16) + exactly 2 children — the date span (flex
gap 4px, 12px, gray, the 12×12 calendar icon) + the payment span
("Brokerage", flex gap 4px, the 12×12 credit-card icon); (4) the
wrapped badge row: flex / wrap / 8px gap / 12px mb / h 52 (the
measured two-line layout: 22 + 8 + 22) / 4 badges [savings, monthly,
Recurring, active]; (5) every badge: flex / center / 6px radius / 2px
10px pad / 12px / 600 / h 22; the classification badge's icon 12×12.

### S1. [MUTATION-SANITY] the pin bites

(a) the footer's `text-xs` → `text-sm` (12px → 14px,
src/components/budget/item-card.tsx:189) → the F1 footer fs assertion
FAILS ("12px" vs "14px"; the footer h 16 → 20);
(b) the badge row's `gap-2` → `gap-4` (8px → 16px, :160) → the F1
badgeRow gap assertion FAILS ("8px" vs "16px");
(c) the classification badge's `py-0.5` → `py-1` (2px 10px → 4px 10px,
:163) → the F1 badge pad assertion FAILS ("2px 10px" vs "4px 10px"),
the badge h 22 → 26, AND the wrapped row's h 52 → 60 — the fresh axis
that proves the wrap ARITHMETIC (22 + 8 + 22), not just the row
geometry (the v57 S1(c) mutated the same line's HORIZONTAL pad; this
one mutates the VERTICAL pad that drives the two-line height).
All restored → GREEN. Each mutation with the standalone REBUILD as a
SEPARATE command (the v47–v54 execution lesson).

### P1. [PROBE-INFRA] the v58 probe family persisted

vlm-shots-v58.sh + clone-vlmshots-v58.sh + vlm-compare-v58.mjs (the
savings view's desktop 1280 pair), savings-census-ref-v58.sh +
savings-census-clone-v58.sh (the DOM arbitration + the full census,
both sides — the clone script carries the P1.2 quoted-heredoc fix by
construction), ref-standing-v52.sh + standing-checks-v52.sh (the 52nd
standing checks), plus the probe README's v58 section. The v58 probe
lessons: (1) the savings census's badge-row finder walks the card's
DIRECT children (the v57 P1.1 lesson, carried); (2) a comment
apostrophe inside a single-quoted shell census variable terminates
the quote (the savings-census-ref-v58.sh first-run syntax error —
bash -n before every run); (3) the reference's savings item is
classified NEED (red) — its own data choice, the classification VALUE
is the data class, the color map stays locked by badge-colors.spec.ts.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v58 paragraph. D2: CLAUDE.md — the E2E count
257 → 258 + the v58 family entry. D3: README — the counts + the v58
row. D4: the SKILL doc — the Session 93 row + the state line. D5: the
PAD — a v1.1.15 revision block. D6: the probe README — the v58
section. D7: session_139.md (the formal log) + the repo worklog
Session 92 + the ledger list. D8: the workspace worklog.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1's pin: the savings goal-card census describe → GREEN (pin-only, no RED phase — the surface is already correct; the pin is the deliverable) | test | `tests/e2e/items.spec.ts` |
| 2 | S1(a)–(c): the three pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`, run as a SEPARATE command) | verify | `src/components/budget/item-card.tsx` |
| 3 | The probe scripts persisted + the probe README's v58 section | docs | `scripts/parity-probes/` |
| 4 | The full chain re-run (108 unit · **258** e2e [+1: the v58 savings pin] · 35 smoke + lint + typecheck + build) — all green | verify | — |
| 5 | The 16 screenshots regenerated (expect ALL byte-identical — the pin-only invariant; regenerate to confirm, keep whichever diff) | docs | `docs/screenshots/` |
| 6 | D1–D8 + the formal session log (session_139.md) + the repo worklog Session 92 + the SKILL doc Session 93 row | docs | repo root + `docs/` |
| 7 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/item-card.tsx:160` — the badge row's
  `mb-3 flex flex-wrap gap-2`; `:163` the classification badge's
  `px-2.5 py-0.5` (the S1(c) line-scoped mutation target — the
  vertical pad); `:189-199` the footer `flex items-center justify-
  between text-xs` + the two conditional spans (the date + the
  `item.paymentMethod ? ... : null` — the Investments card's
  "Brokerage").
- The e2e contract: the v58 describe runs AUTHENTICATED via the setup
  project's storageState; the deterministic e2e seed (prisma/seed.ts
  — the SAME seed the :3200 parity server runs) puts Investments
  (savings classification, Brokerage payment, monthly, recurring,
  active, Oct 6 — the date-DESC order) first on /savings, then
  Emergency Fund (Oct 5) — the census measured exactly this order
  live. The wrapped row h 52 (22 + 8 + 22) is deterministic
  arithmetic.
- The existing pins are SAFE: the v45 F1a 1280 grid census pins the
  /income grid + card chrome + title row + kebab + hover (the v58 pin
  re-asserts the card chrome as its control — same values, no
  conflict); the v57 F1a/F1b pins lock the income + expenses footers
  and badge rows at 1280 (the v58 pin locks the SAVINGS view's — the
  remaining view, no overlap); the v52 F2/F3 mobile censuses pin the
  footer + date span at 390; the v54 F1 savings internals census pins
  the chip family at 390 on the SAVINGS goal card (the v58 pins the
  item-card footer + badge family at 1280 — viewport-scoped, no
  conflict); badge-colors.spec.ts locks the classification color maps
  (the v58 locks the GEOMETRY — the documented split).
- The chain gate: lint → typecheck → 108 unit → build → 257 e2e
  (**258** after: +1 — the v58 savings pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` + the stale-session sweep
  before every agent-browser run; a rebuild swaps .next/standalone
  UNDER a running parity server — the with-server.sh boots fresh per
  command; the reference session EXPIRES between long eval gaps —
  re-login via the same eval before any follow-up census; the
  e2e-chunk regex lesson: the file filter's alternation must match
  the FULL filename (an `auth\.spec` + `\.spec\.ts` double-match
  silently drops auth.spec.ts / calculator-error.spec.ts /
  networth-error.spec.ts — the alternation needs the stem only, with
  the shared `\.spec\.ts` suffix outside the group).
- DEFERRED queue (unchanged, all need reference WRITES — out of bounds
  under the v46 read-only rule): the reference-side verify-email panel
  census, the forgot-confirm state census, the calculator EMPTY-state
  census, the line-items dialog glyphs. The reference's trending-down
  glyph stays data-conditional (its net is positive — the 52nd data
  census confirms "1 items · $25,000" unchanged, no flip to measure).
- The v59 queue (suggestions): the CALCULATOR view's desktop 1280 VLM
  pair (the panel + row surfaces — the v45/v49 pins cover 1280/640
  chrome, no VLM pair), the login view's desktop 1280 pair (the v55
  glyph pin's own surface — no pair at 1280 yet), and the deferred
  reference-write censuses (unchanged).
