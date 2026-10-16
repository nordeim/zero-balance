# Remediation Plan v68 — the DEDICATED axe-core wrapper upgrade iteration
# (the deliberate 4.14.0 pin bump + the lockfile regeneration + the
# nested-engine verify + the full a11y gate re-run + the rule-coverage
# re-audit) + the v61-era pair's fresh standing sweep (the dashboard
# full-page 1280 re-run) + the a11y gate's ENGINE-CONTRACT pin

Date: 2026-10-16 · Scope: the session-163/164 v68 queue — item #1 "the
DEDICATED axe-core wrapper upgrade iteration (bump the pin
`^4.13.0`→`^4.14.0` deliberately + regenerate the lockfile entry + verify
the nested engine resolves axe-core@4.14.x + re-run the full a11y gate +
RE-AUDIT the rule coverage — diff the activated rule sets axe-core 4.13.0
vs 4.14.0, arbitrate any new violations: a real markup issue → fix + pin;
a rule-behavior change → pin accordingly; the upgrade is NEVER a
side-effect lockfile drift)" and item #2 "the re-run cadence rotates to
the v61-era pair (the dashboard full-page 1280 — the quick-action row +
the Budget Guidelines card, the oldest remaining after v64/v65/v66/v67
covered the v57/v58/v59/v60 pairs)" — plus the 62nd standing checks.
Measured live via the v68 family: `axe-rule-census-v68.mjs` (the
rule-coverage census, both engines) + `vlm-shots-v68.sh` +
`clone-vlmshots-v68.sh` + `vlm-compare-v68.mjs` (the pair) +
`ref-standing-v62.sh` + `standing-checks-v62.sh` (the 62nd round,
version-bumped from v61).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · 269 e2e ✓ (the --list count —
268 chromium + 1 setup; the chunk runs 97 + 97 + 77 = 268 chromium + 3
setups, zero failures — the exact documented v67 state) · 35/35 smoke ✓
— the codebase matches the documented v67 state exactly (the v67 pin
verified present at networth.spec.ts:1738 "net worth summary card HEIGHT
census at 1280"). The dev DB re-seeded at the exact seed state (7 budget
items / 3 assets / 2 liabilities).

## The v68 sweep — what the measurement found

### The 62nd standing checks — ALL GREEN

- **Reference side**: the four bugs ALL still live — the toast-blocker
  (`hitIsBurgerChild:false`, the burger's center hit intercepted by
  `DIV.fixed top-0 z-[100]`), the sheet-trap (the overlay remains after
  the nav click, `overlayCount:1`), the no-landmark
  (`navLandmark:false`), the 464px `/networth` overflow at 390. The
  data census UNCHANGED (the 62nd consecutive clean drift check: "1
  items · $25,000" networth / "1 items · $5000.00" income / "4 items ·
  $525.00" expenses). The SEO pair live.
- **Clone side**: R1 the burger hit-test TRUE + the sheet opens · R2 the
  sheet CLOSES + navigates (`sheetGone:true, overlayGone:true` on
  /income) · R3 the nav landmark present · R4 ZERO overflow at 390 on
  all five views (docSW 390 each) · the SEO pair live. **The mobile
  navigation menu VERIFIED WORKING — the 62nd consecutive time.**

### F1 [UPGRADE] — the DEDICATED axe-core wrapper upgrade: 4.13.0 → 4.14.0

The v67 plan's own decision, executed mechanically this iteration. The
complete chain, measured live:

1. **The registry state (the watch, final reading)**: npm-latest
   `@axe-core/playwright` = **4.14.0** (dist-tags: latest 4.14.0 +
   4.14.1-rc/next prereleases); its declared nested engine
   `axe-core ~4.14.0`. **No 5.x wrapper exists** — the guarded major
   never materialized; the upgrade stays inside the documented 4.x
   family.
2. **The pre-upgrade tree state (the v67 state re-confirmed)**: the
   lockfile resolved the wrapper to 4.13.0 with the NESTED engine
   `axe-core@4.13.0` at
   `node_modules/@axe-core/playwright/node_modules/axe-core`; the
   top-level `axe-core@4.14.0` was eslint-plugin-jsx-a11y's
   (lint-time only).
3. **The RULE-COVERAGE RE-AUDIT (the queue's re-audit step)**: the
   activated rule set enumerated from BOTH engines
   (`axe-rule-census-v68.mjs` — the axe.js bundle requires cleanly
   under Node, attaching `axe` to module.exports; `axe.getRules()`
   returns rule metadata keyed `ruleId` with the tag lists): at the
   gate's TAGS (wcag2a/wcag2aa/wcag21a/wcag21aa), **axe-core 4.13.0
   activates 69 of 105 rules and axe-core 4.14.0 activates 69 of 105 —
   the sets BYTE-IDENTICAL: ZERO rules added, ZERO removed.** The
   upgrade changes the engine version, NOT the activated coverage —
   there is no new rule to arbitrate and no markup issue to fix.
4. **The deliberate pin bump**: `package.json` devDependency
   `@axe-core/playwright` `^4.13.0` → `^4.14.0` (one line, the ONLY
   manifest change).
5. **The lockfile regeneration**: `npm install` — the wrapper entry
   4.13.0 → 4.14.0 and the NESTED engine entry DISSOLVES (npm dedupe:
   the top-level `axe-core@4.14.0` — eslint-plugin-jsx-a11y's, whose
   `^4.10.0` admits 4.14.0 — now satisfies the wrapper's `~4.14.0`
   too, so the tree carries ONE axe-core instead of two). The
   lockfile diff: 23 lines changed, net −7 (the wrapper entry + the
   nested-engine entry removed).
6. **The ENGINE verify (the runtime ground truth)**: the wrapper's own
   `require.resolve('axe-core')` (from `@axe-core/playwright`'s
   context) resolves to `<repo>/node_modules/axe-core/axe.js` —
   **version 4.14.0** — and NO nested directory remains under
   `node_modules/@axe-core/playwright/`. The engine that executes the
   AxeBuilder scans is axe-core@4.14.0 ✓ (the upgrade target
   achieved). The tree's axe packages: exactly two —
   `node_modules/@axe-core/playwright` + `node_modules/axe-core` (was
   three with the nested engine).
7. **The full a11y gate re-run under 4.14.0**:
   `npx playwright test tests/e2e/a11y.spec.ts` — **22 passed (21
   chromium + 1 setup)**. The v38 contract holds under the new engine:
   GATE 1 (structural) — no violation other than color-contrast on any
   surface; GATE 2 (provenance) — every flagged color in the
   reference's own 7-color palette; the login page zero-violation
   clean (desktop + mobile); the mobile sheet-open structure intact.
   **No rule-behavior regression exists on any scanned surface** —
   with the activated rule sets byte-identical AND the violations
   profile unchanged, the upgrade is verified clean.

### F2 [PAIR] — the v61-era pair's fresh sweep: the dashboard full-page at 1280

The session-163/164 v68 queue's second item — a fresh VLM standing sweep
of the surface the v61 pair first shot (the v61-era shots predate the
v62/v63 mobile twins, the v64–v67 pins, and the v67 height-family
arbitration; the v64/v65/v66/v67 passes covered the v57/v58/v59/v60-era
pairs). Both sides captured via `vlm-shots-v68.sh` +
`clone-vlmshots-v68.sh` (login on the first attempt both sides, the
parked pointer at (5,5) so no hover-revealed chrome is caught
mid-flight), compared via `vlm-compare-v68.mjs`.

**THE PAIR: VERDICT IDENTICAL** — the VLM found ZERO layout/style
differences: "The geometry, borders, padding, typography, icon
sizing/tinting, and color palette for the Budget Guidelines card and the
Quick Actions row are visually identical between the two images." Every
difference it listed was the expected DATA class (the allocation pct
30.5% vs 62.8%, the balance $3475.00 vs $2065.00, the income/savings/
expenses figures, the stat amounts + counts, the donut percentages +
drill-down rows — each site's own seed). No platform-chrome flag this
run (the "Edit with Base44" FAB excluded by rule regardless).

The re-run re-proves the v61-era surfaces live after the v61 STRETCH fix
(the original v61 pair's own discovery — the guidelines card stretching
to the full 656px row height — fixed in v61 itself, the first
production-code change since v55) and after v62–v67's pins: **the pair
is CLEAN with zero flags to arbitrate.**

### F3 [PIN] — the a11y gate's ENGINE-CONTRACT pin

The upgrade's own invariant, pinned: **the engine the AxeBuilder
executes under is axe-core 4.14.x — the deliberately-pinned toolchain
state, never a silent drift.** The AxeResults object carries
`testEngine: { name, version }` — the identity of the engine that
actually executed the scan — so the pin asserts a real scan's
`testEngine.name === "axe-core"` and `testEngine.version` matches
`/^4\.14\./`. The scan surface: the login page (the zero-violation
surface, no auth needed, the fastest scan in the gate). Any future
engine change without a conscious re-verification (a lockfile drift, a
dedupe flip, a wrapper downgrade, a 4.15/5.x bump) FAILS the suite —
the "never a drift" discipline becomes executable. The pin also
asserts the activated-coverage count via the page-side rule registry?
— NO: the AxeResults do not enumerate the activated rules, and the
coverage is a property of the engine version (the F1 census pinned it
in this plan: 69 activated rules, byte-identical 4.13.0 → 4.14.0) —
pinning the version pins the coverage.

The pin adds ONE test to `tests/e2e/a11y.spec.ts` (a new describe after
the v41 F4 block — the file tail), +1 → **270 e2e**. TOOLCHAIN-ONLY —
no production-code change (the pin-only line continues; the upgrade
touches package.json + package-lock.json, never src/).

### F4 [VERIFY] — the screenshots: 10/16 byte-identical + 6 the DATE class

The workspace was FRESH-CLONED this session (db/ is gitignored — the
committed set's database does not travel), so the dev DB was re-seeded
before the capture. The seed anchors every item date to its seed-time
(`isoDate(offsetDays)` in prisma/seed.ts: -2/-3/-5/-7/-8/-9/-10), and
the committed set's DB was seeded 2026-10-15 (the v66 ship's seed, its
dates re-used byte-identically by v67's capture on the surviving
workspace) — the v68 re-seed (2026-10-16) shifts every rendered date
one day later. The programmatic PIL diff (the v66 method — stronger
than a VLM verdict for single-region changes) localized every changed
region to date digits:

- **03-income**: 2 regions — the salary card's date "Oct 10" → "Oct
  11" (isoDate(-5)) at (716,800) + the second card's date at
  (1458,860).
- **04-expenses**: 1 band — "13, 2026" → "14, 2026" (the Rent card's
  isoDate(-2)) at y 860-878.
- **05-savings**: 1 band — the goal-card date digits at y 860-878.
- **06-networth**: 1 region (11×19 px) — the liability's date digits
  at (834,1658).
- **08-calculator**: max channel diff 2 (sub-perceptual raster noise,
  0.046% of pixels) at the dialog's date-input region — the same
  DATE family, no content change.
- **16-item-details**: 1 region — the details sheet's date digits at
  (1180,1009).

Every other pixel in all 16 frames byte-stable; the other 10
screenshots byte-identical (the login/404/forgot/login-error frames
carry no seed dates). `git diff src/` = 0 lines — the class is the
workspace's re-seed, not production code. The NEW set is committed
(the honest capture of the current seed state — the v66 precedent).

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F3 pin: the a11y gate's engine-contract — a real scan executes under axe-core 4.14.x (GREEN first) | tests/e2e/a11y.spec.ts |
| 2 | sanity | S1 mutation: downgrade the wrapper to 4.13.0 (`npm install @axe-core/playwright@4.13.0` — the TOOLCHAIN mutation, the pin's guarded "source") must FAIL the pin (testEngine.version "4.13.0"); restore (git checkout the manifest + lockfile, npm install) | package.json + package-lock.json |
| 3 | verify | the a11y gate full re-run under the restored 4.14.0 (22 passed) + the full chain re-run (lint → typecheck → 108 unit → build → 270 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (10/16 byte-identical + 6 the DATE class — the fresh workspace's re-seed re-anchored the seed's relative dates one day later; every changed region pixel-arbitrated to date digits, documented below) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v68 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (the toolchain + the E2E count 269→270) | CLAUDE.md |
| 7 | docs | D3: README state + the v68 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 103 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.25 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v68 section (the axe-rule-census probe + the 5 v68 lessons) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_165.md + the repo worklog Session 102 entry | docs/session_165.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push | — |

## Pre-execution validation (done before the plan's execution)

- The F3 pin's mechanism verified live: the AxeResults `testEngine`
  field is part of axe-core's public result contract (axe.d.ts:
  `testEngine: { name: string; version: string }`), populated by every
  `analyze()` — the wrapper does not strip it.
- The pin's scan surface: the login page describe opts OUT of the
  shared storageState (`test.use({ storageState: { cookies: [],
  origins: [] } })` — the established idiom); the pin needs no auth, no
  fixture flow, no fixture restore (READ-ONLY).
- The S1 mutation mechanics: `npm install @axe-core/playwright@4.13.0`
  mutates the resolved tree (the wrapper entry regresses to 4.13.0 and
  the nested engine re-materializes at 4.13.0); NO rebuild is needed —
  axe-core is a TEST dependency loaded by the runner in Node, never
  part of the standalone build the webServer serves; the pin run then
  reports testEngine.version "4.13.0" and FAILS the /^4\.14\./
  assertion. The restore: `git checkout -- package.json
  package-lock.json && npm install` (back to the committed 4.14.0
  state), then the a11y gate re-run GREEN.
- The existing pins are SAFE: the v38 gate contract (the 21 a11y
  tests), the v39/v41 mobile extensions, the v44 hero/stat pins, the
  v45 F3 hover-shadow pin, the v51 F4 mobile guidelines census, and
  the v61 quick-action + guidelines-stretch pins are all re-asserted
  or untouched — the v68 pin asserts the TOOLCHAIN family they never
  covered. The upgrade itself (F1 steps 1–7) is already executed and
  verified against the full a11y gate.
- The chain gate: lint → typecheck → 108 unit → build → 269 e2e
  (**270** after: +1 — the F3 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server boots fresh per command; the
  reference session EXPIRES between long eval gaps — re-login (the
  v61-family login-retry loop already handles it); the e2e chunks pass
  FULL file paths; `ss -tlnp | grep :3100` + kill before every
  full-chain run (the v53 orphaned-webServer lesson); a
  single-quote-selector rule bites BOTH ways inside heredocs (the
  v60/v67 lesson — double-quoted attribute-value selectors only).
- The probe-engineering lesson of the census: the axe.js bundle is a
  UMD-ish IIFE — under `require()` it attaches `axe` to module.exports
  (a vm sandbox with window/document stubs FAILS silently — the global
  never attaches; the honest load is the plain require);
  `axe.getRules()` returns metadata keyed `ruleId` (NOT `id` — the v68
  census's first draft crashed on `.id.localeCompare` of undefined)
  with a `tags` array + an `enabled` field per rule.
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog
  glyphs.
- The v69 queue (suggestions): (1) the re-run cadence rotates to the
  v62-era pair (the networth mobile 390 full-page twin — the OLDEST
  remaining after v63's own pass and v64/v65/v66/v67/v68 covered the
  v57/v58/v59/v60/v61 pairs), (2) the axe-core watch continues at its
  next re-check point (a 5.x wrapper release or a nested-engine bump
  — the 4.14.0 upgrade closes the 4.x story; only a 5.x now changes
  the calculus), (3) the deferred reference-write censuses (unchanged).
