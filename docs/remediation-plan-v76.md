# Remediation Plan v76 — the re-run cycle's next-oldest candidate (the v60-era networth + drill-down pair's second re-run — last re-shot v67) + the axe watch (NO DRIFT) + the stat-card trend-icon glyph + donut label chrome pin (PIN-ONLY)

The session's plan, validated against the codebase before execution. The formal narrative ships in `docs/session_182.md`; the repo worklog entry: Session 110.

## The v76 sweep — what the measurement found

### F0 [BASELINE] — the environment lesson (no code defect)

The baseline chain's first pass hit a 20-test 5.9-minute wall with the boot-failure spec failing at the
`aside, nav` toBeVisible assertion — the page stuck at `aria-label="Loading"` forever. The root cause:
**`npx next build` alone does not produce a servable standalone** — `package.json`'s `build` script is
`next build && cp -r .next/static .next/standalone/.next/ && cp -r public .next/standalone/`, and the
bare `next build` leaves `.next/standalone/.next/static` MISSING: the server renders the HTML shell but
404s every `/_next/static/chunks/*.js|css` — the client never hydrates, boot() never runs, and every
hydration-dependent assertion burns its 10s expect timeout (the "slow suite" was the 404 loop, not
slowness). After the copy steps the chain is FULLY GREEN as-shipped: lint ✓ · typecheck ✓ · 108/108
unit ✓ · build ✓ (robots + sitemap prerendered) · **278 e2e ✓** (98 + 60 + 122 chunks = 277 chromium
+ 3 setups — the exact documented v75 state) · 35/35 smoke ✓. LESSON: the F0 build step must run
`npm run build` (the full script), never a bare `npx next build`.

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no
stable 4.14.1, no 4.15, no 5.x); npm-latest `axe-core` = 4.14.0 (only a canary prerelease beyond). The
lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0 — verified via
the lockfile's packages tree; no nested engine dir under `node_modules/@axe-core/playwright/`). The
engine-contract pin executed GREEN standalone (2 passed). Only a 5.x wrapper (or a nested-engine
change) changes the calculus; the next re-check point unchanged.

### F2 [STANDING] — the 70th standing checks: ALL GREEN

ref-standing-v70.sh + standing-checks-v70.sh (version-bumped from v69 — version-bump-only diffs
verified against the v68→v69 convention). Reference side: the four bugs ALL still live (the
toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark
`navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 70th
consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items
· $525.00" expenses) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu
VERIFIED WORKING (the 70th consecutive time: `hitIsBurgerChild:true`, the sheet opens, closes on nav,
the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

### F3 [PAIR] — the re-run cadence's next-oldest candidate: the v60-era pair's fresh sweep (the networth view + the dashboard drill-down EXPANDED at desktop 1280x800, last re-shot v67) — NO NEW GAP, every flag DOM-arbitrated

vlm-shots-v76.sh + clone-vlmshots-v76.sh + vlm-compare-v76.mjs + arbit-v76.sh (login on the first
attempt both sides; the parked pointer at (5,5); read-only on the reference — the v46 rule holds; the
view-state expansion clicks only).

- **PAIR 1 (the NETWORTH view at desktop 1280x800 — full page)** — the VLM verdict DIFFERENT with two
  style flags, both documented classes: the Base44 "Edit with" FAB (the platform-chrome class) + the
  avatar letter "U" vs "D" (the user-identity class — the VLM misread the clone's letter as "P"; the
  census is the truth). The data deltas (the figures, the groups, the ratio "∞:1" vs "0.21:1", the
  labelBlock width 304 vs 357 — the figure text length drives the min-w-0 block) all the seed-data
  classes. The PART B census (arbit-v76.sh) — the summary card's full HEIGHT family — **byte-identical
  on every axis**: the card 960×333/pad 32px/radius 16px/the 135deg forest→lime gradient/the
  `rgba(26,58,46,0.3) 0px 20px 60px` shadow; the headRow 76/mb 32px/flex/center; the label
  14px/rgba(255,255,255,0.8)/mb 8px/h 20; the figure 48px/700/white/lh 48/h 48; the medallion
  64×64/rgba(255,255,255,0.2)/icon 32×32; the statGrid `440px 440px`/rows 84px/gap 16px/896; the
  statTile 440×84/pad 16px/radius 12px/rgba(255,255,255,0.1)/blur(10px)/label 12px/h 16/mb
  4/amount 24px/700/h 32; the ratioFooter mt 24px/pt 24px/border-t 1px rgba(255,255,255,0.2)/h
  53/label 14px/value 18px/700 — the v67 F3 pin's own axes re-measured with ZERO drift.
- **PAIR 2 (the DASHBOARD drill-down EXPANDED at desktop 1280x800)** — the VLM verdict DIFFERENT with
  six flags, every one DOM-arbitrated via arbit-v76.sh (the PART A census) to a documented class:
  - **The "Dashboard nav highlighted in the clone" flag = the v56 root-URL active-nav class
    re-verified live**: the census's navHighlight bg is TRANSPARENT on BOTH sides — the observable
    delta is the clone's white/500 text vs the reference's zinc-600/400 (the reference does not mark
    Dashboard active at the root URL; the clone does — the documented class, unchanged since v56).
  - **The "progress bar longer in the clone" flag = the pct × 568 data class re-verified live**: the
    track chrome byte-identical (trackW 568/trackH 12/trackBg rgba(255,255,255,0.1)/the same 90deg
    gradient fill family) — the fillW 173 (ref, 30.5%) vs 357 (clone, 62.8%) is the savings-percentage
    data arithmetic.
  - **The "clone has percentage labels the reference lacks" flag = the v60 perception class
    re-verified live**: the donut label chrome BYTE-IDENTICAL (count 4/labelFs 16px/labelFill
    rgb(0,0,0)/sectors 3/labelLineCount 0 on BOTH sides) — the reference's first label element carries
    the three texts concatenated ("92.3%4.6%3.1%") while the clone's are distributed — a recharts
    label-grouping DOM artifact, the rendered chrome identical; the VALUES are the data class.
  - **The "extra category/sub-item rows" + "2 categories footer" + stat-count flags = the seed-data
    classes** (the reference's own 1-income-item data vs the clone's 7-item dev seed).
  - **The "black tooltip over Total Expense" flag = the Base44 platform chrome** (the FAB's tooltip,
    caught over the stat card).
  - The stat cards' footer TREND ICONS byte-identical (the v67 axes: 16×16/rgb(143,188,63)/the
    twin-polyline glyphSig/the 0 0 24 24 viewBox) and the hero trend glyph row byte-identical (7
    glyphs, the same colors + path signatures) — no drift since v67.
- The seedcheck after the pair: the exact seed state (7 items / rent 1850 / expenses 2235 / 0 line
  items / 3 assets / 2 liabilities).

**NO NEW GAP — the v76 iteration is PIN-ONLY.**

### F4 [PIN] — the breakdown section-icon chip glyph + the donut label chrome census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 279)

The never-pinned axes (the existing pins: the v43 F2/v44 F1-F4 censuses pin the section rows' geometry + the chevron glyph swap; the v60 F2 pin the expanded sub/item rows; the v55 glyph census pins the stat-tile SHAPE row; the v9 G1b contract + the early dashboard test pin the labelLineCount 0 + the sector fill order — NEVER the section icon's own glyph signature/color/viewBox, and never the donut label elements' own count/fs/fill):

- the BREAKDOWN CARD's income-SECTION ICON CHIP: the 16×16 legacy TrendingUpIcon glyph (the twin-polyline glyphSig `<polyline
  points="22 7 13.5 15.5 8.5 10.5 2 17"></polyline><polyline points="16 7 22 7 22 13"></polyline>`) /
  the color rgb(143,188,63) (the income section's limeGreen — the config at dashboard-view.tsx:479) / the `0 0 24 24`
  viewBox, inside its h-8 w-8 rounded-lg chip (32×32 / radius 8px / the tinted rgba(143,188,63,0.125) bg —
  the chip census riding alongside);
- the DONUT LABEL chrome: the label count 4 / the labelFs 16px / the labelFill rgb(0,0,0) / the
  sectors 3 / the labelLineCount 0 (re-asserted alongside the v9 G1b contract);
- the census rides the plain dashboard state at 1280×800 (the breakdown card + the donut render
  without the drill-down expansion).

The pin's precise finder targets the section BUTTON (the aria-expanded toggle carrying "Total
Income") — the exact element the arbitration census's statCards[0] finder resolved to on BOTH sides
(the finder-description lesson: the v67/v76 arbitration's "stat-card footer trend icon" label was a
MISNOMER — its width-200-500 "Total Income" finder matches the breakdown section row FIRST in the
DOM, and THAT icon's chrome is what measured byte-identical; the pin pins the same surface with an
honest name + the exact-value assertions).

The pin asserts the arbitration's own measured values, byte-identical on both sides' dashboards at
1280×800.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → build (`npm run build` — the F0 lesson) → **279 e2e** in chunks (+1) →
35 smoke; the 16 standing screenshots regenerated + byte-compared (the same-DB discipline; the
seedcheck under `env -u DATABASE_URL`). EXPECTED: the 07-add-item-modal shot carries the documented
dialog-default DATE class (the calendar already rolled 2026-10-16 → 2026-10-17 at v75 — same-day
regeneration should be byte-stable; any overnight rollover pixel-arbitrated per the v66/v75
discipline, never a VLM verdict).

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the breakdown section-icon chip glyph + donut label chrome census at 1280 (the section icon 16×16/color/glyphSig/viewBox + the chip 32×32/8px/tinted bg + the label count/fs/fill/sectors/labelLineCount — the arbitration's own measured values, the finder-description corrected to the actual surface) | tests/e2e/dashboard.spec.ts |
| 2 | sanity | the pin-sanity mutation: the section icon's `h-4 w-4` → `h-5 w-5` (dashboard-view.tsx:316, the BreakdownSection Icon) → the pin FAILS at exactly the sectionIcons axis (the empty array at 20×20); restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/dashboard-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 279 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v76 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (278→279 + the v76 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v76 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 111 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.33 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v76 section (the new probes + the F0 lesson: `npm run build`, never a bare `npx next build` — the standalone static copy is part of the build contract) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_182.md + the repo worklog Session 110 entry | docs/session_182.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v76.sh PART A census's own measured values, byte-identical
  on both sides' dashboards at 1280×800: the sectionIcons `[{w: 16, h: 16, color: "rgb(143, 188, 63)",
  viewBox: "0 0 24 24", glyphSig: '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"></polyline><polyline
  points="16 7 22 7 22 13"></polyline>'}]`; the iconChip `{w: 32, h: 32, radius: "8px", bg:
  "rgba(143, 188, 63, 0.125)"}` (the chip census — the source's h-8 w-8 rounded-lg + the
  hexToRgba(limeGreen, 0.125)); the donutLabels `{count: 4, labelLineCount: 0, labelFs: "16px",
  labelFill: "rgb(0, 0, 0)", sectors: 3}`.
- The pin-sanity execution NOTE (the honest record): the FIRST mutation attempt targeted the
  hero-stat-tile trend icon (dashboard-view.tsx:619) and the pin STAYED GREEN — exposing the
  finder-description mismatch (the arbitration's "stat-card" finder resolves to the breakdown
  section row, whose icon lives at :316); the pin was rewritten with the precise section-button
  finder + the honest surface name, and the corrected mutation (the :316 section icon h-4 w-4 →
  h-5 w-5) verified to FAIL at exactly the sectionIcons axis (the empty array at 20×20) before the
  restore.
- The source confirms the values: the trend icon's `h-4 w-4` sizing + the `style={{ color }}`
  (dashboard-view.tsx:619, the color from the stat config's `color: COLORS.limeGreen` at :479); the
  legacy TrendingUpIcon's twin-polyline path + the `0 0 24 24` viewBox
  (src/components/ui/legacy-icons.tsx); the donut's `labelLine={false}` + the percent formatter
  (dashboard-view.tsx:737-738); the label fs/fill inherit the document defaults (16px/black —
  byte-identical on both sides).
- The existing pins are SAFE: the v51 F5 census pins the stat-card family at 390 including
  `trend: {w: 16}` (a different viewport, a disjoint axis set — the glyph/color/viewBox/count never
  asserted there); the v9 G1b labelLineCount 0 pin lives in the plain-dashboard test (re-asserted
  consistently by the new pin, not contradicted); the v56 F1 hero pin covers the track/fill/tiles —
  disjoint surfaces.
- The blast radius: ZERO production-code change (every flag arbitrated to a documented class — the
  pin-only line holds); the pin-sanity mutation touches
  `src/components/budget/dashboard-view.tsx:619` (the `h-4 w-4` class) REVERTED before ship
  (`git diff src/` = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` → 278 e2e (**279** after: +1 — the F4
  pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser run; the with-server boots
  fresh per command; the reference session EXPIRES between long eval gaps — the login-retry loop
  handles it; the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` + kill before every
  full-chain run (the v53 orphaned-webServer lesson); one-shot Prisma scripts need `env -u
  DATABASE_URL`; no dollar sequences in census JS inside double-quoted bash strings (the v64 rule);
  no attribute-value selectors in single-quoted eval strings (the v60/v67 rule); the QUOTED heredoc
  with the env-injected census (the v73 lesson); the mutations need the standalone REBUILD as a
  SEPARATE command (the v53 lesson); the clean-check gate re-runs AFTER every new file lands (the
  v69 lesson); **the build step is `npm run build` (the static+public copy into
  .next/standalone is part of the build contract — the F0 lesson)**.
- The deferred queue (unchanged, all need reference WRITES — out of bounds under the v46 read-only
  rule): the reference-side verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census, the line-items dialog glyphs.
- The v77 queue (suggestions): (1) the re-run cadence rotates to the next-oldest candidate after this
  pair (the mobile 390 twins — the networth + dashboard pair, last re-shot v69 — the full re-run
  ledger is in the probe README), (2) the axe-core watch at its next re-check point (only a 5.x
  wrapper changes the calculus), (3) the deferred reference-write censuses (unchanged).
