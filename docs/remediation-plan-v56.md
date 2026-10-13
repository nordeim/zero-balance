# Remediation Plan v56 — The 1280 desktop VLM standing pair + the
# glyph-swap HOLD re-audit (PIN-ONLY — no production-code change; the
# sixth iteration since v46, the v53/v54/v55 line's return to pin-only
# after THE FIX)

Date: 2026-10-13 · Scope: the session-131 v56 queue's own standing-check
suggestion — "a fresh VLM pair on the v55 F1 surface's desktop 1280
state (the donut legend + the stat rows post-swap)" — extended with the
full glyph re-audit (does the v55 swap still hold? any NEW drift?) and
the 50th standing checks. Measured live on BOTH sites via the v56
family (glyph-audit-v56.sh — the re-audit with the polyline/rect-rx
capture fix; vlm-shots-v56.sh + clone-vlmshots-v56.sh +
vlm-compare-v56.mjs — the desktop 1280x800 pair; vlm-arbit-v56.sh +
clone-arbit-v56.sh — the DOM arbitration; hero-desk-v56.sh — the hero
census; standing-checks-v50.sh + ref-standing-v50.sh — the 50th
standing checks. All READ-ONLY on the reference, the v46 rule).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ · **254 e2e ✓ (104 + 151, two ordered chunks, both exit 0, zero
failures — one not-found navigation flake under full-suite load,
green on the isolated re-run and the full-chunk re-run)** · 35/35 smoke
✓. The 50th standing checks all clean (mobile-nav R1–R4 both sides —
the reference's four bugs ALL live [toast-blocker, sheet-trap,
no-landmark, the 464 /networth overflow], the clone's mobile menu
VERIFIED WORKING, the data census intact ["1 items · $25,000" networth
/ "1 items · $5000.00" income], the SEO pair live on both sites). The
trap-log scan CLEAN (both `-mb-2` back buttons inside their converted
`zb-auth-mode` containers; the oklab mentions are the mitigation
comments). The v55 diff verified (the legacy-icons module + the eight
import swaps + the glyph-parity spec).

## The v56 sweep — what the measurement found

- **THE GLYPH RE-AUDIT (the v55 swap HOLDS): the full per-view lucide
  glyph dictionary re-censused on BOTH sites — 24 shared glyph names,
  0 DIFFS among the shared set, 1 one-side-only (repeat — the clone's
  Recurring superset badge, the documented class).** The four
  previously-drifted glyphs (piggy-bank, trending-up, search, mail) all
  render the reference's OLD geometry on both sites now — the v55
  legacy-icons swap holds byte-identical. NO new drift found. (The
  re-audit script fixes the v55 census's polyline/rect capture —
  polylines read `points`, rects carry their rx — the v55 lesson
  applied.)
- **THE DESKTOP 1280x800 VLM PAIR (the session-131 queue item): PAIR 1
  (the dashboard — the v55 F1 surfaces post-swap: the stat rows, the
  donut, the legend) flagged 4; PAIR 2 (the networth view — the
  trending-up hero/summary swap surfaces) VERDICT IDENTICAL, zero
  visual/style flags.** The PAIR 1 flags, every one DOM-arbitrated
  (vlm-arbit-v56.sh + clone-arbit-v56.sh, the v43 rule):
  1. the nav "Dashboard" highlight — the reference shows NO highlight
     at `/` (computed: transparent, none, zinc-700, 400) while the
     clone highlights (the 135deg forest→lime gradient, white, 500) —
     **the documented root-URL active-nav gap, a reference bug the
     clone deliberately fixes (the superset class)**. The non-root
     control: at `/networth` BOTH sites render the byte-identical
     active style (linear-gradient(135deg, rgb(45, 90, 74),
     rgb(143, 188, 63)), white, 500) — the clone's rail matches the
     reference's rail wherever the reference works.
  2. the hero progress bar length — **data-driven, not style**: the
     track is byte-identical on both sites (w 568, h 12,
     rgba(255, 255, 255, 0.1), radius 9999px); the fill's width is
     `pct%` of the track (the reference 173 = 30.5% × 568; the clone
     357 = 62.8% × 568 — each site's own allocation data).
  3. the user avatar ("U" vs "D") — the logged-in user's initial, the
     documented user-identity data class.
  4. the "Edit with Base44" FAB — the reference's platform chrome, the
     documented class.
  **The pair CLEAN per the v43 rule.**
- **THE HERO DESKTOP CENSUS (the v56 pin's measurement source —
  hero-desk-v56.sh, byte-identical on both sites at 1280x800):** the
  hero grid `304px 304px 304px` cols with the 24px gap and its two
  children (the 632×364 goal-card panel + the 304×364 breakdown card,
  both at y 136); the goal card 632×316, radius 16px, pad 32px, the
  135deg forest gradient, the shadow `rgba(26, 58, 46, 0.3) 0px 20px
  60px 0px`; the track 568×12 (bg/radius above); the fill's 90deg
  orange status gradient + radius 9999px; the stat tiles 48×48 with
  their 24×24 svgs (the glyph-swap chrome).
- **NO production gap found — v56 is PIN-ONLY** (the v53/v54 class):
  the glyph parity holds, the desktop pair is clean, the mobile
  standing checks pass (50th). The gap in the pin COVERAGE: the hero
  card's DESKTOP 1280 state is unpinned (the v50 F3 hero census covers
  mobile 390 only; the glyph census covers the shape data at the
  default 1280x720 but no hero chrome geometry at the exact 1280x800
  pair viewport). The v56 deliverable pins it.

## Findings

### F1. [PIN] the hero-card desktop 1280 census (the v56 pin)

One new describe in `tests/e2e/dashboard.spec.ts` —
"hero desktop 1280 census (v56 — plan F1)" — pinning the
hero-desk-v56.sh measurement at `setViewportSize({ 1280, 800 })`:
(1) the hero grid: the `304px 304px 304px` column template, the 24px
gap, exactly 2 children with the [632×364, 304×364] sizes at y 136;
(2) the goal card: 632×316, radius 16px, pad 32px, the
`linear-gradient(135deg, rgb(26, 58, 46)` bg + the
`rgba(26, 58, 46, 0.3) 0px 20px 60px 0px` shadow;
(3) the progress track: 568×12, `rgba(255, 255, 255, 0.1)`, radius
9999px;
(4) the fill: the `linear-gradient(90deg, rgb(224, 122, 59)` family +
radius 9999px + the DATA-INTEGRITY arithmetic (the fill's width ≈
pct/100 × 568 within ±2px — the reference's own 173 = 30.5% × 568
measured);
(5) the pct label (the `/^[0-9.]+%$/` figure);
(6) the three stat-row icon tiles: 48×48 with 24×24 svgs (the
glyph-swap chrome — the shapes already pinned by the v55 glyph spec).

### F2. [VLM-PAIR] the desktop 1280 standing pair — DONE, CLEAN

The session-131 v56 queue's own suggestion, executed: PAIR 1 (the
dashboard) + PAIR 2 (the networth). PAIR 2 IDENTICAL; PAIR 1's four
flags all DOM-arbitrated to the documented classes (the root-URL
active-nav gap superset fix, the data-driven fill, the avatar, the
Base44 FAB). The pair scripts + the arbitration persisted (P1).

### S1. [MUTATION-SANITY] the pin bites

(a) the track's `h-3` → `h-2` (12px → 8px,
src/components/budget/dashboard-view.tsx:116) → the F1 track-height
assertion FAILS;
(b) the goal card's `p-8` → `p-6` (32px → 24px, :82) → the F1
pad assertion FAILS;
(c) the hero grid's `gap-6` → `gap-4` (24px → 16px, :947) → the F1
gap assertion FAILS.
All restored → GREEN. Each mutation with the standalone REBUILD as a
SEPARATE command (the v47–v54 execution lesson).

### P1. [PROBE-INFRA] the v56 probe family persisted

glyph-audit-v56.sh (the glyph re-audit — with the polyline/rect-rx
capture fix), vlm-shots-v56.sh + clone-vlmshots-v56.sh +
vlm-compare-v56.mjs (the desktop 1280 pair), vlm-arbit-v56.sh +
clone-arbit-v56.sh (the DOM arbitration), hero-desk-v56.sh (the hero
census, both sides), standing-checks-v50.sh + ref-standing-v50.sh (the
50th standing checks), plus the probe README's v56 section. The v56
probe lessons: (1) the v55 census's polyline capture read `points` as
empty via x1/y1 — the shape dump must branch per tag (the fix applied
to glyph-audit-v56.sh); (2) the reference has NO `<nav>` landmark (its
own documented bug) — nav probes must scan ALL anchors, not
nav-scoped selectors; (3) the combined clone-shot script can exceed
the 240s Bash timeout when the agent-browser daemon was reset between
steps — split the shots into per-view invocations (login+shot, then
shot) when the timeout bites.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v56 paragraph. D2: CLAUDE.md — the v56 entry. D3:
README — the v56 row. D4: the SKILL doc — the Session 91 row + the
state line. D5: the PAD — a v1.1.13 revision block. D6: the probe
README — the v56 section. D7: session_134.md (the formal log) +
session_135.md (the raw transcript) + the repo worklog Session 90 +
the ledger list. D8: the workspace worklog
(/home/z/my-project/worklog.md).

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1's pin: the hero desktop 1280 census describe → GREEN (pin-only, no RED phase — the surface is already correct; the pin is the deliverable) | test | `tests/e2e/dashboard.spec.ts` |
| 2 | S1(a)–(c): the three pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`, run as a SEPARATE command) | verify | `src/components/budget/dashboard-view.tsx` |
| 3 | The probe scripts persisted + the probe README's v56 section | docs | `scripts/parity-probes/` |
| 4 | The full chain re-run (108 unit · **255** e2e [+1: the v56 hero-desk pin] · 35 smoke + lint + typecheck + build) — all green, two ordered chunks | verify | — |
| 5 | The 16 screenshots regenerated (expect ALL byte-identical — the pin-only invariant; regenerate to confirm, keep whichever diff) | docs | `docs/screenshots/` |
| 6 | D1–D8 + the formal session log (session_134.md) + the raw transcript (session_135.md) + the repo worklog Session 90 + the SKILL doc Session 91 row | docs | repo root + `docs/` |
| 7 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/dashboard-view.tsx:82` — the goal card's
  `rounded-2xl p-8` (16px / 32px — the census's radius/pad); `:116`
  the track's `h-3 overflow-hidden rounded-[9999px]` + the inline
  `rgba(255, 255, 255, 0.1)`; `:118-121` the fill's
  `h-full rounded-[9999px]` + the inline `width: ${pct}%` and the
  90deg status gradient; `:947-953` the hero grid
  `grid grid-cols-1 gap-6 lg:grid-cols-3` with the `lg:col-span-2`
  goal panel + the breakdown card; `:956-960` the StatCard row (the
  48px tiles — the `h-12 w-12` icon circle pattern at :99-103 for the
  hero's own target icon, the StatCard tile in the StatCard component).
- The e2e contract: the v56 describe runs AUTHENTICATED via the setup
  project's storageState (the deterministic e2e seed — the dashboard
  settle text `+$2065.00`, the same pattern the glyph-parity spec
  uses); `setViewportSize({ 1280, 800 })` per test (the v42-F2
  breakdown-band census's own 1280×800 pattern at dashboard.spec.ts:511).
  The seed's allocation arithmetic: income 555000 − savings 125000 −
  expenses 223500 = 206500 → pct = expenses / (income − savings) =
  2235/4300 = 52.0%? NO — the measured pct is 62.8% (the allocation
  = expenses / income = 2235/3555? no — 2235/5550 = 40.3%). The
  allocation-percent formula is `totals.allocationPercent` — the pin
  does NOT hardcode the pct value (data-dependent, the seed's own
  arithmetic — the fill's width arithmetic uses the RENDERED pct text,
  so the pin holds regardless of the seed's data); it pins the
  TRACK/FAMILY geometry (byte-identical on both sites) + the
  fillWidth ≈ pct × trackWidth arithmetic.
- The existing pins are SAFE: the v50 F3 hero mobile census (390) is
  viewport-scoped; the v42 F2 breakdown-band census (1280×800) pins
  the breakdown card's bands (the second grid child — its y 136
  position is already implied by the v42 pin's own y measurements);
  the glyph-parity spec's dashboard census (default 1280×720) pins the
  shape data, not the hero chrome. No overlap conflicts.
- The chain gate: lint → typecheck → 108 unit → build → 254 e2e
  (**255** after: +1 — the v56 hero-desk pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` + the stale-session sweep
  before every agent-browser run (the v50/v51 lesson — applied twice
  this session when the daemon hung); a rebuild swaps .next/standalone
  UNDER a running parity server — reboot the :3200 server after every
  build (with-server.sh boots fresh per command); the reference
  session EXPIRES between long eval gaps — re-login via the same eval
  before any follow-up census; split long clone-side shot scripts into
  per-view invocations when the 240s timeout bites (the v56 lesson).
- DEFERRED queue (unchanged, all need reference WRITES — out of bounds
  under the v46 read-only rule): the reference-side verify-email panel
  census, the forgot-confirm state census, the calculator EMPTY-state
  census, the line-items dialog glyphs. The reference's trending-down
  glyph stays data-conditional (its net is positive — the 50th data
  census confirms "1 items · $25,000" unchanged, no flip to measure).
