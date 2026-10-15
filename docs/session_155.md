# Session 155 — v64: the OLDEST desktop pair's fresh standing sweep (the
# v57-era items pair re-run) + the axe-core 5.x wrapper watch (NO DRIFT) +
# the income filter-card computed census pin

The continuation of the audit → fix → alignment → deliver workflow on
the `zero-balance` repo, executing the session-153 v64 queue. The
workspace had been reset (a fresh sandbox) — the repo re-cloned from
`https://github.com/nordeim/zero-balance.git` at `1ba981c` (the
session-154 transcript doc on top of `55e5a5b`, the v63 ship).

## Refresh & validation

The five core docs (AGENTS/CLAUDE/README/PAD/SKILL) and the latest
session records (session_153 / remediation-plan-v63 / worklog /
session_154) reviewed; the codebase validated against the documented
v63 state. The environment rebuilt from scratch: `npm install` (+ the
prisma engines rebuild), `.env` restored
(`DATABASE_URL="file:../db/custom.db"`), `npm run db:push` + `db:seed`
(7 budget items / 3 assets / 2 liabilities), and the Playwright
browsers installed (the fresh-sandbox caveat). **Baseline chain GREEN:
lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap
prerendered) · 265 e2e ✓ (91 + 94 + 82 chunk runs = 264 chromium + 1
setup, zero failures — the `:3100` orphan check clean before the runs)
· 35/35 smoke ✓** — the codebase matches the documented v63 state
exactly (the v63 pin verified present at networth.spec.ts:868).

## The 58th standing checks

`ref-standing-v58.sh` + `standing-checks-v58.sh` (version bumps of the
v57 scripts). Reference: the four bugs ALL still live (the toast-blocker
`hitIsBurgerChild:false` via the `DIV.fixed top-0 z-[100]` intercept;
the overlay trap `overlayCount:1` after the nav click;
`navLandmark:false`; the 464px `/networth` overflow at 390); the data
census UNCHANGED (the 58th consecutive clean drift check: "1 items ·
$25,000" / "1 items · $5000.00" / "4 items · $525.00"); the SEO pair
live. Clone: R1 the burger hit-test true + the sheet opens; R2 the
sheet closes + navigates; R3 the landmark; R4 zero overflow at 390 on
all five views; the SEO pair live. **The mobile navigation menu
VERIFIED WORKING — the 58th consecutive time.**

## The v64 sweep

**F1 — the axe-core 5.x wrapper watch: NO DRIFT.** The v63 F1's
documented next re-check point ("a 5.x wrapper release or an engine
bump inside the wrapper's nested dep"): neither has happened. The
npm-latest `@axe-core/playwright` is STILL 4.13.0 (no 5.x release
exists), the lockfile resolves the wrapper to 4.13.0, and the engine
that actually executes the AxeBuilder scans — the wrapper's NESTED
`axe-core@4.13.0` — is byte-identical to the v38/v62/v63 audits. The
top-level `axe-core@4.14.0` still belongs to `eslint-plugin-jsx-a11y`
(via eslint-config-next) — lint-time only. The a11y.spec.ts contract
remains valid as pinned; no re-scan required. The next re-check point:
unchanged.

**F2 — the OLDEST desktop pair's fresh sweep: the v57-era items pair
re-run.** The queue's first item — a fresh VLM standing sweep of the
OLDEST desktop pair (the v57 shots of the income + expenses views at
1280×800 predate the v61 dashboard fix and the v62/v63 mobile twins).
Shot FULL-PAGE both sides (`vlm-shots-v64.sh` +
`clone-vlmshots-v64.sh`), compared via `vlm-compare-v64.mjs`, every
flag DOM-arbitrated via `arbit-v64.sh` per the v43 rule.

- **PAIR 1 (income): VERDICT DIFFERENT** — the avatar (the
  user-identity class), the Base44 FAB (the platform-chrome class — the
  VLM contradicted itself between the two pairs, attributing the FAB to
  the clone in pair 2; either way platform chrome, excluded by rule),
  and the seed data (the reference's 1 income item vs the clone's
  2-item seed). All documented classes.
- **PAIR 2 (expenses): VERDICT DIFFERENT with THREE style flags, ALL
  arbitrated to documented classes:**
  1. The card footer content — the v57 DATA-CONDITIONAL class
     re-measured live: the footer chrome BYTE-IDENTICAL (flex
     justify-between 12px rgb(107,114,128) h 16; every child span flex
     gap 4px with the 12×12 gray icon); the reference's expense items
     carry no paymentMethod values so their footers render ONE child
     (the date alone), while the clone's render the SAME two-child
     structure the reference's OWN income card renders (measured live:
     "Oct 7, 2026" + "Bank Account").
  2. The badge arrangement — the v57 wrap data class re-measured: the
     badge chrome BYTE-IDENTICAL (flex/6px radius/2px 10px pad/12px-600/
     h 22; the row flex wrap 8px gap mb 12px); the clone's Recurring
     superset badge wraps the row to h 52 = 22+8+22.
  3. The grid population — the seed-count data class: the grid axes
     BYTE-IDENTICAL (w 960, gap 16px, the template "309.328px
     309.328px 309.344px" — the SAME fractional last track on both
     sides); the reference's 4 cards vs the clone's seed's 3.
  4. Plus the card heights (200 vs 230) — the badge-wrap arithmetic
     data class (the wrapped 52px badge row adds exactly the 30px; the
     card HEIGHT is documented as a data class, never pinned).

**The pair is CLEAN: every flag arbitrates to a documented class. No
production-code parity gap** (`git diff src/` empty at ship — the
pin-only line continues).

## The remediation plan v64 + the TDD execution

`docs/remediation-plan-v64.md` (the 64th plan; the ToDo table's 13
rows). The pin: **the INCOME view's filter-card COMPUTED census at
1280** — the never-census'd sibling of the v38 S2 savings pin (v37/v38
measured the /expenses triggers + the /savings instance; the v52 F2 pin
covered this card's MOBILE 390 state; the early-era income test pins
CLASS STRINGS only — the never-census'd-sibling lesson):

- GREEN first run (PIN-ONLY — the surface is already correct): the
  card 960×86 (pad 24px, radius 16px, white, border rgb(229,231,227),
  mb 24px — the 24+36+24+2 height arithmetic) · the search 447×36 (the
  2-col span 215.5+16+215.5; the asymmetric 40px left pad — the
  search icon's room, pl-10; radius 6px, border rgb(229,229,229)) ·
  the inner grid 4 tracks "215.5px"/16px gap/3 children · the two
  comboboxes 216×36 at 14px ("All Categories"/"All Frequencies").
- THREE pin-sanity mutations verified to FAIL then restored (each with
  the standalone REBUILD as a SEPARATE command): the card `p-6`→`p-4`
  (pad 24→16 + card h 86→70) · the search wrapper `md:col-span-2`
  removed (search w 447→215.5 — the span arithmetic) · the grid
  `gap-4`→`gap-2` (gap 16→8 + the tracks recompute 215.5→221.5). The
  restore verified with `git status src/` clean + the full items spec
  29 passed (+1).

## The screenshots

The 16 regenerated — **all BYTE-IDENTICAL** (the fresh sandbox's
re-seed anchored to the same day as the v63 capture, so even the
SEED-DATE class is absent; no production change).

## The chain + the ship

**Full chain GREEN: lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ ·
266 e2e ✓ · 35/35 smoke ✓.** The docs aligned D1–D8 (the AGENTS v64
paragraph; CLAUDE 265→266 + the filter-card pin reference; the README
state lines + the v64 table row; the SKILL Session 99 row + the three
count lines; the PAD v1.1.21 revision block; the probe README's v64
section; this session log + the repo worklog Session 98; the workspace
worklog). The v64 probe family persisted: `vlm-shots-v64.sh`,
`clone-vlmshots-v64.sh`, `vlm-compare-v64.mjs`, `arbit-v64.sh`,
`ref-standing-v58.sh`, `standing-checks-v58.sh`.

## The v65 queue (suggestions)

1. The v58-era savings pair's fresh sweep — the queue's other OLDEST
   candidate (the v64 pass covered the v57-era items pair).
2. The axe-core 5.x wrapper watch (unchanged next re-check point).
3. The deferred reference-write censuses (unchanged — all need
   reference WRITES, out of bounds under the v46 read-only rule): the
   verify-email panel census, the forgot-confirm state census, the
   calculator EMPTY-state census, the line-items dialog glyphs.
