# Remediation Plan v59 — The calculator-view desktop 1280 VLM standing pair +
# the calculator panel/total-card census (PIN-ONLY — no production-code
# change; the ninth iteration since v46, the pin-only line's continuation)

Date: 2026-10-15 · Scope: the session-139 v59 queue's first TWO items —
"the CALCULATOR view's desktop 1280 VLM pair (the panel + row surfaces —
the v45/v49 pins cover 1280/640 chrome, no VLM pair)" and "the LOGIN
view's desktop 1280 pair (the v55 glyph pin's own surface — no pair at
1280 yet)" — plus the 53rd standing checks. Measured live on BOTH sites
via the v59 family (vlm-shots-v59.sh + clone-vlmshots-v59.sh +
vlm-compare-v59.mjs — the calculator dialog's desktop 1280x800 pair;
login-shots-v59.sh + clone-login-shots-v59.sh — the login view's 1280
pair; calc-census-ref-v59.sh + calc-census-clone-v59.sh — the DOM
arbitration + the panel/total-card/row census, both sides;
ref-standing-v53.sh + standing-checks-v53.sh — the 53rd standing
checks). All READ-ONLY on the reference (the v46 rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · **258 e2e ✓ (89 + 94 + 76,
three ordered chunks, zero failures)** · 35/35 smoke ✓. The 53rd
standing checks all clean (mobile-nav R1–R4 both sides — the reference's
four bugs ALL live [toast-blocker hitIsBurgerChild:false, the sheet-trap
overlayCount:1, the no-landmark navLandmark:false, the 464 /networth
overflow], the clone's mobile menu VERIFIED WORKING — the 53rd time,
the data census intact ["1 items · $25,000" networth / "1 items ·
$5000.00" income / NEW this session: "4 items · $525.00" expenses], the
SEO pair live on both sites).

## The v59 sweep — what the measurement found

- **THE CALCULATOR 1280x800 VLM PAIR (the session-139 queue item #1):
  flagged TWO items, every one DOM-arbitrated (the v43 rule):**
  1. the total card's "• Will update category total" span —
     **DATA-CONDITIONAL, not style: the span's visibility is the pinned
     contract (lineTotal !== parentAmount at dialog-open → shown;
     calculator.spec.ts "0 !== 1850 → shown")** — the reference's OWN
     Rent is $25.00 and its single "Contents Insurance" line item sums
     to $25.00 (25 === 25 → HIDDEN), while the clone's Rent was $1,850
     at dialog-open (25 !== 1850 → SHOWN; the clone-side pair state was
     built by adding the SAME line item through the real UI, then FULLY
     restored: delete + the $1850 edit-flow restore + the $2235.00 page
     total verified);
  2. the row's hover-action pair (edit + delete) — **POINTER-POSITION
     ARTIFACT, not chrome: at rest BOTH sites gate the pair at
     opacity 0** (the reference's census: actionsAtRest opacity 0 /
     2 buttons / btnW 32 — identical to the clone's, and to the v6
     G9/G10 + v45 F2a pins) — the reference's screenshot merely caught
     the actions mid-hover (its pointer rested inside the dialog after
     the click; the clone's shot parked the pointer at (5,5) per the
     parked-pointer lesson).
  **The census (both sides, byte-identical on every axis):** the panel
  w 768 / h 393 (the 1-row state) / x 256 / y 204 (the centering
  invariant: round((800−393)/2)) / radius 16px / maxW 768px / maxH
  680px (85vh of the 800 viewport — the v49 F3's 816px was the 960
  viewport's) / bg white / overflow hidden / the 2xl VISIBLE shadow
  layer rgba(0,0,0,0.25) 0px 25px 50px -12px (the reference's 2
  transparent leads = the accepted lead-divergence class); the total
  card 720×90 / bg rgb(255,247,245) / radius 12px / pad 16px / border
  1px solid rgb(252,221,213); the close 36×36; the header border-b
  1px solid rgb(229,231,227); the row 720 / pad 16 / radius 12 /
  border 1px solid rgb(229,231,227) / bg white / transition all 0.15s
  (the v45 F2a values, re-confirmed on both sides live).
  **The pair CLEAN per the v43 rule.**
- **THE LOGIN 1280x800 VLM PAIR (the session-139 queue item #2):
  IDENTICAL** — the VLM found zero layout/style differences (the card,
  logo, fonts, colors, inputs, the dark navy button, the OR divider);
  the only flag is the reference's "Edit with Base44" platform badge
  (the documented platform-chrome class). The clone's login census
  matches the reference's exactly: title "ZeroBudget" / h1 "Welcome to
  ZeroBudget" / email+password inputs (the same placeholders) / the
  Sign in button 368×48.
- **NO production gap found — v59 is PIN-ONLY** (the v53/v54/v56/v57/v58
  class). The gap in the pin COVERAGE: the calculator panel's full
  chrome + the total card at 1280 — the v49 F3 pin walked the panel
  chrome at 640 only, the v45 F2a pinned the panelW + row at 1280, and
  the total card is pinned at 390 only (v53 F2: 310 wide). The v59
  deliverable pins them at the pair viewport.

## Findings

### F1. [PIN] the calculator panel + total-card census at 1280 (the v59 pin)

One new test in `tests/e2e/calculator.spec.ts` — its own describe "the
calculator panel census at 1280 (v59 — plan F1)":

**F1** (the read-only open state, the v49-F3 pattern at the pair
viewport) on /expenses at 1280×800: hover Rent → Calculate → census:
(1) the panel: w 768 / radius 16px / maxW 768px / maxH 680px (the 85vh
cap) / bg rgb(255,255,255) / overflow hidden / the 2xl VISIBLE shadow
layer (toContain rgba(0,0,0,0.25) 0px 25px 50px -12px); (2) the
centering invariant: panel y === round((800 − h)/2) (the height is
data-dependent — never pinned); (3) the close 36×36; (4) the header
border-b 1px solid rgb(229,231,227); (5) the total card (the empty
state — the e2e seed's Rent carries NO line items): w 720 (768 − the
2×24 p-6) / bg rgb(255,247,245) / radius 12px / pad 16px / border
1px solid rgb(252,221,213) — the v53 F2's own chrome at the 1280
viewport; (6) the panel-width control (the v45 F2a value re-asserted:
768).

### S1. [MUTATION-SANITY] the pin bites

(a) the total card's `backgroundColor: "#fff7f5"` → `"#fff8f0"`
(src/components/budget/calculator-dialog.tsx:150) → the F1 totalCard bg
assertion FAILS (rgb(255,247,245) vs rgb(255,248,240));
(b) the panel's `maxWidth: "48rem"` → `"42rem"` (:103) → the F1 panel
maxW assertion FAILS (768px vs 672px; the panel w 768 → 672 too);
(c) the total card's `p-4` → `p-5` (:149) → the F1 totalCard pad
assertion FAILS ("16px" vs "20px").
All restored → GREEN. Each mutation preceded by `npm run build`, run
as a SEPARATE command (the v47–v58 execution lesson).

### P1. [PROBE-INFRA] the v59 probe family persisted

vlm-shots-v59.sh + clone-vlmshots-v59.sh + vlm-compare-v59.mjs (the
calculator pair), login-shots-v59.sh + clone-login-shots-v59.sh (the
login pair), calc-census-ref-v59.sh + calc-census-clone-v59.sh (the DOM
arbitration + the full 1280 census, both sides), ref-standing-v53.sh +
standing-checks-v53.sh (the 53rd standing checks), plus the probe
README's v59 section. The v59 probe lessons: (1) `agent-browser mouse
click` DOES NOT EXIST in 0.39.0 — the low-level pair is `mouse down` +
`mouse up` after a `mouse move` (the silent-redirect failure mode: a
failed subcommand swallowed by >/dev/null leaves the pointer wherever
it was — the card body — and the down/up click OPENS THE ITEM DETAILS
dialog instead: a false-failure signature); (2) the eval output is a
JSON-encoded STRING — `"443,550"` — and `cut -d,` on it yields `"443`
(a leading quote) which silently breaks `mouse move` — strip the quotes
first (`POS=${POS//\"/}`); (3) the reference's dialogs are PLAIN fixed
divs (no role=dialog — the documented class) — the reference-side
dialog census must find the panel by geometry (maxWidth 768px) or the
fixed-overlay filter, never by [role=dialog]; (4) the reference's
session EXPIRES between long eval gaps — re-login before any follow-up
census (the carried v58 lesson, re-confirmed twice this session); (5)
the reference's /expenses data census ("4 items · $525.00":
Miscellaneous $0 / Investments $300 / Netflix $200 / Rent $25 — the
reference's OWN data) is now documented for future calculator pairs.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v59 paragraph. D2: CLAUDE.md — the E2E count
258 → 259 + the v59 family entry. D3: README — the counts + the v59
row. D4: the SKILL doc — the Session 94 row + the state line. D5: the
PAD — a v1.1.16 revision block. D6: the probe README — the v59 section.
D7: session_141.md (the formal log) + the repo worklog Session 93 +
the ledger list. D8: the workspace worklog.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1's pin: the calculator panel + total-card census describe at 1280 → GREEN (pin-only, no RED phase — the surface is already correct; the pin is the deliverable) | test | `tests/e2e/calculator.spec.ts` |
| 2 | S1(a)–(c): the three pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`, run as a SEPARATE command) | verify | `src/components/budget/calculator-dialog.tsx` |
| 3 | The probe scripts persisted + the probe README's v59 section | docs | `scripts/parity-probes/` |
| 4 | The full chain re-run (108 unit · **259** e2e [+1: the v59 calculator pin] · 35 smoke + lint + typecheck + build) — all green | verify | — |
| 5 | The 16 screenshots regenerated (expect ALL byte-identical — the pin-only invariant; regenerate to confirm, keep whichever diff) | docs | `docs/screenshots/` |
| 6 | D1–D8 + the formal session log (session_141.md) + the repo worklog Session 93 + the SKILL doc Session 94 row | docs | repo root + `docs/` |
| 7 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/calculator-dialog.tsx:103` — the panel's
  `maxWidth: "48rem"` (768px); `:104` `maxHeight: "85vh"` (680px at the
  800 viewport); `:105` `overflow: "hidden"`; `:149-150` the total
  card's `mb-6 rounded-xl p-4` + `style={{ backgroundColor: "#fff7f5",
  border: "1px solid #fcddd5" }}` (the S1 mutation targets); `:205` the
  row's `group rounded-xl border bg-white p-4 transition-all
  hover:shadow-md` (the v45 F2a surface).
- The e2e contract: the v59 describe runs AUTHENTICATED via the setup
  project's storageState; the deterministic e2e seed (prisma/seed.ts)
  puts Rent ($1,850, Oct 4) on /expenses; the calculator's EMPTY state
  (no line items) is the pinned read-only open state (the v49 F3
  pattern — no fixture restore needed); the total card's empty-state
  census (720 wide at 1280) was measured live this session on the
  CLONE (the with-row state's total card is also 720 — the width is
  the panel constant minus p-6, data-independent).
- The existing pins are SAFE: the v45 F2a pin asserts the panelW 768 +
  the row census at 1280 (the v59 pin re-asserts panelW as its control
  — same value, no conflict); the v49 F3 pin walks the panel chrome at
  640 (viewport-scoped, no overlap); the v53 F2 pins the mobile 390
  census (viewport-scoped); the v6 G7-G11 + v21 pins walk the row
  actions (the v59 pin doesn't touch the row actions — the census
  control only); calculator-error.spec.ts's restoreRent contract
  untouched (the v59 pin is read-only — no line items, no recalcs).
- The chain gate: lint → typecheck → 108 unit → build → 258 e2e
  (**259** after: +1 — the v59 calculator pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser
  run; a rebuild swaps .next/standalone UNDER a running parity server —
  the with-server.sh boots fresh per command; the reference session
  EXPIRES between long eval gaps — re-login via the same eval before
  any follow-up census; the e2e-chunk file filter: pass FULL file
  paths (no regex alternation — the v58 lesson).
- DEFERRED queue (unchanged, all need reference WRITES — out of bounds
  under the v46 read-only rule): the reference-side verify-email panel
  census, the forgot-confirm state census, the calculator EMPTY-state
  reference census (the reference's Rent carries a line item — an
  empty state would need a reference delete), the line-items dialog
  glyphs. The reference's trending-down glyph stays data-conditional
  (its net is positive — the 53rd data census confirms "1 items ·
  $25,000" unchanged).
- The v60 queue (suggestions): the DASHBOARD's desktop 1280 VLM
  standing pair re-run (the v56 pair + the v57/v58 items-family pairs
  covered the hero at 1280 — the drill-down dialog surfaces have no
  VLM pair), the NETWORTH view's desktop 1280 VLM pair (the v52-era
  pins cover the 390/640 chrome, no 1280 pair), and the deferred
  reference-write censuses (unchanged).
