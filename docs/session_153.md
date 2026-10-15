# Session 153 — v63: the /networth mobile 390 full-page pair (the standing-pair matrix COMPLETED) + the stat-tile family pin + the axe-core version-drift re-check

The continuation of the audit → fix → alignment → deliver workflow on
the `zero-balance` repo, executing the session-149/151 v63 queue. The
workspace carried over from the previous session (the repo intact at
`1f4be36`; `git pull` fast-forwarded to `acf51d4` — the session-152
transcript doc).

## Refresh & validation

The five core docs (AGENTS/CLAUDE/README/PAD/SKILL) and the latest
session records (session_151 / remediation-plan-v62 / worklog /
session_152) reviewed; the codebase validated against the documented
v62 state. **Baseline chain GREEN: lint ✓ · typecheck ✓ · 108/108
unit ✓ · build ✓ (robots + sitemap prerendered) · 264 e2e ✓ (97 + 91 +
78 chunk runs = 263 chromium + 1 setup, zero failures — the
`:3100` orphan check clean before the runs) · 35/35 smoke ✓** — the
codebase matches the documented v62 state exactly (the v62 pin verified
at dashboard.spec.ts's "mobile header-subtitle block census at 390").

## The 57th standing checks

`ref-standing-v57.sh` + `standing-checks-v57.sh` (version bumps of the
v56 scripts). Reference: the four bugs ALL still live (the
toast-blocker `hitIsBurgerChild:false` via the `DIV.fixed top-0
z-[100]` intercept; the overlay trap `overlayCount:1` after the nav
click; `navLandmark:false`; the 464px `/networth` overflow at 390);
the data census UNCHANGED (the 57th consecutive clean drift check:
"1 items · $25,000" / "1 items · $5000.00" / "4 items · $525.00"); the
SEO pair live. Clone: R1 the burger hit-test true + the sheet opens;
R2 the sheet closes + navigates; R3 the landmark; R4 zero overflow at
390 on all five views; the SEO pair live. **The mobile navigation menu
VERIFIED WORKING — the 57th consecutive time.**

## The v63 sweep

**F1 — the axe-core version-drift re-check: NO DRIFT.** The queue's
watch item ("the 4.13 family set held this round; a major bump could
shift rule coverage"): the pinned `@axe-core/playwright@^4.13.0`
resolves to 4.13.0 — still npm-latest — and the engine that actually
executes the AxeBuilder scans is the wrapper's NESTED
`axe-core@4.13.0`, byte-identical to the v38/v62 audits. The top-level
`axe-core@4.14.0` in the tree belongs to `eslint-plugin-jsx-a11y`
(`^4.10.0`) — a lint-time static-analysis consumer that never scans
pages (documented to preempt the next "why is 4.14 in the lockfile"
question). The a11y.spec.ts contract remains valid as pinned; no
re-scan required. The next re-check point: a 5.x wrapper release or an
engine bump inside the wrapper's nested dep.

**F2 — the /networth 390 full-page VLM pair: the matrix COMPLETED.**
The standing-pair program's last un-paired viewport × view combination
(`vlm-shots-v63.sh` + `clone-vlmshots-v63.sh` +
`vlm-compare-v63.mjs`); with it, {dashboard, items (income/expenses),
savings, calculator, networth} × {1280 desktop, 390 mobile} are ALL
paired. VERDICT DIFFERENT with THREE flags, ALL DOM-arbitrated via
`arbit-v63.sh` to documented classes:
1. "Stat tiles side-by-side (ref) vs stacked (clone)" — the v41
   mobile-superset class re-measured live: the reference's card
   432-wide inside its own 464 docSW overflow renders its fixed 2-col
   grid (cols "175.828px 175.844px", tiles 176×84); the clone's
   358-fit card stacks 1-col (cols "294px", tiles 294×84) — the v4
   data-fit superset (v29's live 2-col DOM experiment).
2. "The clone's summary card is taller" — the direct arithmetic of
   (1): the reference's h 333 + the second 84px tile row + the 16px
   gap = the clone's 421.
3. "The trend-icon circle appears larger/more prominent in the clone"
   — a PERCEPTION ARTIFACT of the v54 clipping class: the medallion
   BYTE-IDENTICAL 64×64 and the icon BYTE-IDENTICAL 32×32 on both
   sides, but the reference's medallion sits at right 416 in its
   464-overflowing page — 26px PAST the 390 viewport edge
   (`clipsViewport:true`, partially rendered, visually smaller) —
   while the clone's sits fully in-bounds at right 342.

The data differences the expected classes (the reference's 1 asset vs
the clone's 3+2 seed; "∞:1" vs "0.21:1" — the pinned formatRatio
contract; the Base44 tooltip — platform chrome). **The pair is CLEAN;
no production-code parity gap** (`git diff src/` empty at ship).

## The remediation plan v63 + the TDD execution

`docs/remediation-plan-v63.md` (the 63rd plan; the ToDo table's 13
rows). The pin: **the networth summary card's stat-tile family census
at 390** (the arbitration measured a never-pinned family — the v41 F3
pin covers the card w/pad/radius/bg/shadow, the 24px figure, the
gridCols and the chip bounds, but NOT the tile geometry, the tile
chrome, the grid gap, the card-height arithmetic, or the medallion's
inner icon):
- GREEN first run (PIN-ONLY — the surface is already correct): the
  stat grid {cols "294px", gap "16px", w 294, 2 children} · the tiles
  {294×84 each; bg rgba(255,255,255,0.1), backdrop blur(10px), radius
  12px, pad 16px} · the card HEIGHT 421 (the 1-col stacking
  arithmetic) · the medallion's inner icon 32×32.
- THREE pin-sanity mutations verified to FAIL then restored (each with
  the standalone REBUILD as a SEPARATE command): the stat grid
  gap-4→gap-2 (gap 16→8 + card h 421→413) · the tile p-4→p-2 (tile h
  84→68 + pad 16→8) · the medallion svg h-8 w-8→h-6 w-6 (icon 32→24).
  The restore verified with `git status src/` clean + the full
  networth spec 24 passed.

## The screenshots

The 16 regenerated — **all BYTE-IDENTICAL** (no re-seed this session;
the seed dates still anchor to the same day as the v62 capture, so
even the SEED-DATE class is absent).

## The chain + the ship

**Full chain GREEN: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ ·
265 e2e ✓ · 35/35 smoke ✓.** The docs aligned D1–D8 (the AGENTS v63
paragraph; CLAUDE 264→265 + the stat-tile pin reference; the README
state lines + the v63 table row; the SKILL Session 98 row + the five
count lines; the PAD v1.1.20 revision block; the probe README's v63
section; this session log + the repo worklog Session 97; the workspace
worklog). The v63 probe family persisted: `vlm-shots-v63.sh`,
`clone-vlmshots-v63.sh`, `vlm-compare-v63.mjs`, `arbit-v63.sh`,
`ref-standing-v57.sh`, `standing-checks-v57.sh`.

## The v64 queue (suggestions)

1. The re-run cadence on the OLDEST desktop pairs (v57's items pair
   and v58's savings pair predate the v61 dashboard fix and the
   v62/v63 mobile twins — a fresh standing sweep of one of them).
2. The axe-core 5.x wrapper watch (F1's documented next re-check
   point).
3. The deferred reference-write censuses (unchanged — all need
   reference WRITES, out of bounds under the v46 read-only rule): the
   verify-email panel census, the forgot-confirm state census, the
   calculator EMPTY-state census, the line-items dialog glyphs.
