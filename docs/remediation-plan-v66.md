# Remediation Plan v66 — the v59-era pair's fresh standing sweep (the
# calculator dialog + login view re-run at 1280) + the axe-core 5.x wrapper
# watch (an upstream 4.14.0 appears) + the calculator dialog's HEIGHT-family
# computed census pin

Date: 2026-10-16 · Scope: the session-159/160 v66 queue — "the re-run
cadence rotates to the v59-era pair (the calculator + login views at 1280 —
the oldest remaining after v64/v65 covered the v57/v58 pairs)" and "the
axe-core 5.x wrapper watch (unchanged next re-check point)" — plus the 60th
standing checks. All READ-ONLY on the reference (the v46 rule). Measured
live on BOTH sites via the v66 family: `vlm-shots-v66.sh` +
`clone-vlmshots-v66.sh` + `vlm-compare-v66.mjs` + `login-shots-v66.sh` +
`clone-login-shots-v66.sh` (the pair), `arbit-v66.sh` + `arbit-v66b.sh`
(the DOM arbitration census, the row-HEIGHT family added),
`ref-standing-v60.sh` + `standing-checks-v60.sh` (the 60th round,
version-bumped from v59), and the npm/lockfile version audit (F1).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · 267 e2e ✓ (the --list count —
266 chromium + 1 setup; the chunk runs 99 + 85 + 85 = 266 chromium + 3
setups, zero failures — the `:3100`/`:3200` orphan checks clean before the
runs) · 35/35 smoke ✓ — the codebase matches the documented v65 state
exactly (the v65 pin verified present at items.spec.ts "the SAVINGS view's
PAGE-HEADER ROW computed census at 1280"). The dev DB at the exact seed
state (7 budget items / 3 assets / 2 liabilities — seeded fresh this
sandbox).

## The v66 sweep — what the measurement found

### The 60th standing checks — ALL GREEN

- **Reference side**: the four bugs ALL still live — the toast-blocker
  (`hitIsBurgerChild:false`, the burger's center hit intercepted by
  `DIV.fixed top-0 z-[100]`), the sheet-trap (the overlay remains after
  the nav click, `overlayCount:1`), the no-landmark (`navLandmark:false`),
  the 464px `/networth` overflow at 390. The data census UNCHANGED (the
  60th consecutive clean drift check: "1 items · $25,000" networth /
  "1 items · $5000.00" income / "4 items · $525.00" expenses). The SEO
  pair live.
- **Clone side**: R1 the burger hit-test TRUE + the sheet opens · R2 the
  sheet CLOSES + navigates (`sheetGone:true, overlayGone:true` on
  /income) · R3 the nav landmark present · R4 ZERO overflow at 390 on
  all five views (docSW 390 each) · the SEO pair live. **The mobile
  navigation menu VERIFIED WORKING — the 60th consecutive time.**

### F1 [AUDIT] — the axe-core 5.x wrapper watch: local NO DRIFT + an upstream 4.14.0 appears

The v65 F1's documented next re-check point ("a 5.x wrapper release or an
engine bump inside the wrapper's nested dep"): **neither has happened in
the local tree** — the lockfile resolves `@axe-core/playwright` to 4.13.0,
and the engine that actually executes the AxeBuilder scans — the wrapper's
NESTED `axe-core@4.13.0` (`node_modules/@axe-core/playwright/
node_modules/axe-core`) — is byte-identical to the v38/v62/v63/v64/v65
audits. The top-level `axe-core@4.14.0` in the tree still belongs to
`eslint-plugin-jsx-a11y@6.10.2` (via eslint-config-next) — a LINT-TIME
static-analysis consumer that never scans pages. **BUT the npm registry
now carries `@axe-core/playwright@4.14.0`** (dist-tags: latest 4.14.0 +
4.14.1-rc/next; its declared nested engine `axe-core ~4.14.0`) — a MINOR
bump inside the documented 4.x family, NOT the 5.x the watch guards
against. The pinned range `^4.13.0` would admit 4.14.0 on an
unconstrained fresh install, but the lockfile holds the tree — no drift.
Recorded as the candidate for a future DEDICATED upgrade iteration (bump
the pin deliberately + re-run the full a11y gate + re-audit the rule
coverage — never a side-effect lockfile drift). The a11y.spec.ts contract
remains valid as pinned; no re-scan required. The next re-check point:
unchanged (a 5.x wrapper release or an engine bump inside the wrapper's
nested dep).

### F2 [PAIR] — the v59-era pair's fresh sweep: the calculator dialog + the login view at 1280

The session-159/160 v66 queue's first item — a fresh VLM standing sweep
of the two surfaces the v59 pair first shot (the calculator dialog +
the login view at 1280×800; the v59-era shots predate the v61 dashboard
fix and the v62/v63 mobile twins; the v64/v65 passes covered the
v57/v58-era pairs). Shot both sides (`vlm-shots-v66.sh` +
`login-shots-v66.sh` + `clone-vlmshots-v66.sh` +
`clone-login-shots-v66.sh` — the clone's calculator half adds the
matching "Contents Insurance" $25 monthly-active line item through the
real UI then FULLY restores the fixture: delete + restore Rent's $1850 +
verify the "$2235.00" page total), compared via `vlm-compare-v66.mjs`,
every flag DOM-arbitrated via `arbit-v66.sh` + `arbit-v66b.sh` (the
computed census on both sides at 1280×800, the row-HEIGHT family added)
per the v43 rule.

**PAIR 1 (calculator) VERDICT DIFFERENT with 2 style flags, both
DOM-arbitrated to documented classes:**

1. "The clone's row is missing the hover-state action buttons" —
   DOM-arbitrated to the POINTER-POSITION class: the actions rest at
   **opacity 0 on BOTH sides** (btnCount 2 each; the v6 G9/G10 + v45 F2a
   pins) — the reference's screenshot caught the pair mid-reveal (the
   pointer had rested inside the dialog at shot time), a capture-timing
   artifact, not a chrome difference.
2. "The clone carries an extra '• Will update category total' span" —
   DOM-arbitrated to the DATA-CONDITIONAL class: the span renders while
   `total !== item.amount`. The reference's OWN Rent is natively $25.00
   and its single line item sums to $25.00 → lineTotal === parentAmount
   → HIDDEN (measured `hasWillUpdateSpan:false`); the clone's modal
   snapshot carries the opened-at parent amount ($1850) against the
   recalculated $25.00 → SHOWN (measured `true`). The conditional itself
   is the pinned contract (calculator.spec.ts "0 !== 1850 → shown").
3. Plus the panel's computed box-shadow (not VLM-flagged this run but
   censused): the reference renders `rgba(0,0,0,0) 0px 0px 0px 0px,
   rgba(0,0,0,0) 0px 0px 0px 0px, rgba(0,0,0,0.25) 0px 25px 50px -12px`
   (two LEADING zero-alpha layers — the Tailwind v4 computed-form class)
   while the clone's `.zb-modal-panel` emits the VISIBLE layer alone —
   the documented accepted lead-divergence class (the v49 pin's own
   idiom).

**PAIR 2 (login) VERDICT: IDENTICAL** — the only distinction the
reference's "Edit with Base44" FAB (platform chrome, excluded from
comparisons by rule). The census is byte-for-byte: title "ZeroBudget",
h1 "Welcome to ZeroBudget", the same input placeholders
(you@example.com / ••••••••), the Sign in button 368×48, no `<a>` on
either side (the forgot/reset links live INSIDE the mode forms, not the
login card).

**The pair is CLEAN: every flag arbitrates to a documented class. No
production-code parity gap** (`git diff src/` empty at ship — the
pin-only line continues).

**The arbitration's own discovery — the never-pinned HEIGHT family.**
The v66 census added the row-height axes (never measured before v66):
the v45 F2a pin covers the row's width/pad/radius/border + the hover
reveal, the v53 pin the 390 reflow, the v59 pin the panel + totalCard
(w/bg/radius/pad/border — the totalCard's h measured for the first time
this iteration). The v66 census measured the family BYTE-IDENTICAL on
both sides (the reference's values, the clone's identical): the row
**720×102** (the deterministic arithmetic: the 32px top actions row +
the h4's 4px mb + the 28px amount block + the 32px p-4 padding + the
2px border), the name h4 block (16px/600/rgb(26,58,46)/h 24/mb 4px),
the badge pill row (flex/gap 8px/12px/h 20), the first pill (h 20/w 65/
pad 2px 8px/radius 9999px/12px/400), the amount P (20px/700/
rgb(224,122,59)/h 28), and the totalCard **h 90** (the 32px total row +
the 8px mb-2 + the 16px caption row + the 32px p-4 padding + the 2px
border — the height arithmetic of the v59-pinned chrome).

### F3 [PIN] — the calculator dialog's HEIGHT-family computed census at 1280

The F2 arbitration census measured a never-pinned family: the computed
HEIGHTS of the calculator dialog's interior — the v45 F2a pin covers the
row's width/pad/radius/border class strings + the v59 pin the panel and
the totalCard's w/bg/radius/pad/border, but NEVER the heights (the row
h 102, the name h4 block, the badge pill row, the amount P, the
totalCard h 90). The census, measured BYTE-IDENTICAL on both sides:

- **The row**: 720×102, pad 16px, radius 12px, border-top 1px solid
  rgb(229,231,227), bg white.
- **The name h4**: fontSize 16px, weight 600, color rgb(26,58,46)
  (forestDark), h 24, mb 4px.
- **The badge pill row**: flex, gap 8px, fontSize 12px, h 20.
- **The first pill**: h 20, w 65 (the "monthly" default), pad 2px 8px,
  radius 9999px, 12px/400.
- **The amount P**: fontSize 20px, weight 700, color rgb(224,122,59)
  (orangeDark), h 28.
- **The totalCard**: 720×90 (the v59-pinned chrome's height axis).

The F3 pin adds the census to `tests/e2e/calculator.spec.ts` (PIN-ONLY —
the surface is already correct; GREEN first run expected), a new
describe after the v59 panel-census block, at the pair viewport
(1280×800), riding the established add-then-restoreRent fixture flow
(the v45 F2a idiom — the height family needs a live row; the e2e seed's
Rent carries none).

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F3 pin: the calculator dialog's height-family computed census at 1280 (GREEN first) | tests/e2e/calculator.spec.ts |
| 2 | sanity | S1 mutation A: the row's `p-4`→`p-2` must FAIL the pin (pad 16→8 + row h 102→70); standalone rebuild; restore | src/components/budget/calculator-dialog.tsx |
| 3 | sanity | S2 mutation B: the h4's `mb-1`→`mb-2` must FAIL the pin (mb 4→8 — the nameH4 axis; the row h stays 102: the 32px actions row still governs the top block); standalone rebuild; restore | src/components/budget/calculator-dialog.tsx |
| 4 | sanity | S3 mutation C: the totalCard's `p-4`→`p-2` must FAIL the pin (pad 16→8 + totalCard h 90→58); standalone rebuild; restore | src/components/budget/calculator-dialog.tsx |
| 5 | verify | the 16 screenshots regenerated + byte-compared (expect NO change — no production-code change) | docs/screenshots/ |
| 6 | docs | D1: AGENTS.md v66 paragraph | AGENTS.md |
| 7 | docs | D2: CLAUDE.md count/state bump | CLAUDE.md |
| 8 | docs | D3: README state + the v66 row | README.md |
| 9 | docs | D4: SKILL doc Session 101 row + the state line | zero-balance_SKILL.md |
| 10 | docs | D5: PAD revision block v1.1.23 | Project_Architecture_Document.md |
| 11 | docs | D6: the probe README's v66 section | scripts/parity-probes/README.md |
| 12 | docs | D7: session_161.md + the repo worklog Session 100 entry | docs/session_161.md + worklog.md |
| 13 | ship | the full chain re-run (lint → typecheck → 108 unit → build → 268 e2e → 35 smoke) + commit + SSH-wrapper push | — |

## Pre-execution validation (done before the plan's execution)

- The F3 pin's finders: modeled on the v66 arbitration's own census
  (arbit-v66.sh / arbit-v66b.sh) — the panel by its "Rent Calculator"
  text, the h4 by its exact "Contents Insurance" leaf text, the row by
  the walk-UP from the h4 to the bordered white card, the pills by
  their 9999px radius inside the row (the first pill = the frequency
  "monthly" default), the amount P by the `$`-prefixed largest-font
  leaf, the totalCard by its rgb(255,247,245) bg. All axes
  scroll-independent (the dialog sits centered at 1280×800).
- The mutation targets: the row's `p-4` at calculator-dialog.tsx:205
  (the row-height + pad axes), the h4's `mb-1` at :210 (the nameH4 mb
  axis), the totalCard's `p-4` at :149 (the totalCard height + pad
  axes). Each mutation needs the STANDALONE REBUILD as a SEPARATE
  command (the v53 lesson) before the pin run can bite.
- The chain gate: lint → typecheck → 108 unit → build → 267 e2e
  (**268** after: +1 — the F3 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser
  run; the with-server boots fresh per command; the reference session
  EXPIRES between long eval gaps — re-login (the fresh-login /expenses
  fetch can exceed the wait window — the Rent finder RETRIES before the
  hover); the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` +
  kill before every full-chain run (the v53 orphaned-webServer lesson);
  the census JS inside the heredoc avoids every dollar sequence where
  possible (the String.fromCharCode(36) finder — the v64/v65 rule).
- The deferred queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side verify-email
  panel census, the forgot-confirm state census, the calculator
  EMPTY-state reference census, the line-items dialog glyphs.
- The v67 queue (suggestions): (1) the re-run cadence rotates to the
  v60-era pair (the networth-view desktop 1280 standing pair — the
  oldest remaining after v64/v65/v66 covered the v57/v58/v59 pairs),
  (2) the axe-core wrapper upgrade decision (the upstream 4.14.0 — a
  dedicated upgrade iteration, never a drift), (3) the deferred
  reference-write censuses (unchanged).
