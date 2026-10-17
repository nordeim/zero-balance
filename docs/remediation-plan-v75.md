# Remediation Plan v75 — the re-run cycle's next-oldest candidate (the v59-era login + calculator pair's second re-run — last re-shot v66) + the axe watch (NO DRIFT) + the login card's geometry + typography pin (PIN-ONLY)

The session's plan, validated against the codebase before execution. The formal narrative ships in `docs/session_180.md`; the repo worklog entry: Session 109.

## The v75 sweep — what the measurement found

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 4.15, no 5.x); npm-latest `axe-core` = 4.14.0 (only a canary prerelease beyond). The lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0 — verified via the lockfile's packages tree; no nested engine dir under `node_modules/@axe-core/playwright/`). The engine-contract pin executed GREEN standalone (2 passed). Only a 5.x wrapper (or a nested-engine change) changes the calculus; the next re-check point unchanged.

### F2 [STANDING] — the 69th standing checks: ALL GREEN

ref-standing-v69.sh + standing-checks-v69.sh (version-bumped from v68 — version-bump-only diffs verified against the v67→v68 convention, the ordinal included). Reference side: the four bugs ALL still live (the toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 69th consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED WORKING (the 69th consecutive time: `hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

### F3 [PAIR] — the re-run cadence's next-oldest candidate: the v59-era pair's fresh sweep (the login view + the calculator dialog at desktop 1280x800, last re-shot v66) — NO NEW GAP, every flag DOM-arbitrated

vlm-shots-v75.sh + clone-vlmshots-v75.sh + login-shots-v75.sh + clone-login-shots-v75.sh + vlm-compare-v75.mjs (login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference — the v46 rule holds; the clone's calculator twin rides the v66 fixture discipline: the "Contents Insurance" $25 line item added through the real UI then FULLY restored — the Delete cleanup + Rent's $1850 re-edit + the "3 items · $2235.00" page-total verification).

- **PAIR 1 (the LOGIN view at desktop 1280x800 — the logged-out surface)** — **VERDICT IDENTICAL, zero style flags** (the only observable delta the Base44 "Edit with" FAB — the platform-chrome class). The both-sides census (LOGIN_CENSUS_JS via arbit-v75.sh + the login-census-ref-v75.sh follow-up): the card w 448 / radius 16px / bg rgba(255,255,255,0.95) / border 0; the h1 "Welcome to ZeroBudget" 30px/700/lh 36px/rgb(15,23,42); the subtitle "Sign in to continue" 16px/rgb(100,116,139); the logo img 96x96/alt "ZeroBudget logo"; the email + password inputs h 48/radius 12px/border 1px rgb(226,232,240)/fs 14px/the exact placeholder pair; the Sign in button 368x48/radius 12px/bg rgb(15,23,42)/color white/14px/500; the links [] BOTH sides (the mode switchers are buttons, not anchors — a DOM-shape note); the Google + OR-divider blocks BOTH present; the docSW 1280. The card shadow's VISIBLE layer byte-identical (`rgba(0, 0, 0, 0.25) 0px 25px 50px -12px`); the lead-layer count differs (the reference's 2 transparent leads vs the clone's 4 — the v66 documented computed-form class; zero-alpha layers render nothing).
- **PAIR 2 (the CALCULATOR dialog at desktop 1280x800)** — the VLM verdict DIFFERENT with three flags, every one DOM-arbitrated via arbit-v75.sh (the both-sides CALC_CENSUS_JS census):
  - **The "extra will-update line" flag = the v66 DATA-CONDITIONAL class re-verified live**: `hasWillUpdateSpan` false (the reference — its Rent natively $25.00 === its line-item total $25.00 → hidden) vs true (the clone — its dialog opened at $1850 while the recalculated total is $25.00 → shown). The span's chrome was pinned at v73 (12px/400/rgb(234,88,12)) and byte-verified at v66/v73.
  - **The "row hover state" flag = the v66 pointer-position class re-verified live**: `actionsAtRest` `{opacity: "0", btnCount: 2}` on BOTH sides — the actions rest at opacity 0; the reference's screenshot caught them mid-reveal because the shot precedes the pointer park (the documented screenshot-timing class), while the clone's shot follows the park.
  - **The "amount alignment" flag = the pointer-position class's corollary**: the amount's own chrome byte-identical (20px/700/rgb(224,122,59)/h 28) — the horizontal position delta is the hover-revealed action pair's footprint, not the amount's chrome.
  - **The full census byte-identical on every other axis**: the panel 768x393/radius 16px/maxW 768px/bg white; the scrim rgba(26,58,46,0.5)/blur(8px)/1280x800; the title 18px/700/rgb(26,58,46)/lh 28px; the desc 14px/rgb(107,114,128)/lh 20px; the close 36x36/radius 6px/transparent/no border (the clone; the reference's close carries the v73-measured same-family chrome); the totalCard 720x90/pad 16px/radius 12px/border 1px solid rgb(252,221,213); the nameH4 16px/600/rgb(26,58,46)/h 24/mb 4px; the row 720x102/pad 16px/radius 12px/borderTop 1px solid rgb(229,231,227)/bg white; the pillRow flex/gap 8px/12px/h 20; the pill1 20x65/pad 2px 8px/radius 9999px/12px/400; the addBtn 110x32/radius 6px/12px/500/white; the docSW 1280. The panel shadow: the reference's 3-layer form (2 transparent leads) vs the clone's single-layer — the v66 documented computed-form class (the visible layer byte-identical).
- The seedcheck after the fixture cycle: the exact seed state (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities).

**NO NEW GAP — the v75 iteration is PIN-ONLY.**

### F4 [PIN] — the login card's geometry + typography census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 278)

The never-pinned axes (the existing pins: the v7 G2/G3 pins lock the COLORS — the h1/subtitle/label slate values, the card bg, the bar + page gradients, the submit bg/color/h, the email border/bg, the logo-ring halo; the v9 pins lock the per-state control heights + 14px text; the v13 pin the focus rings; the v24 pins the label gaps + mobile families — the card's WIDTH + RADIUS, the h1's TYPOGRAPHY family (fs/fw/lh), the subtitle's fs, the Sign in button's FULL chrome (w/radius/fs/fw), the logo's geometry, and the input radius/fs family at desktop were never pinned):

- the CARD geometry: w 448 (the max-w-md wrapper) / radius 16px (rounded-2xl) / bg rgba(255,255,255,0.95) (re-asserted alongside);
- the h1 typography: fs 30px / fw 700 / lh 36px / color rgb(15,23,42) (the sm:text-3xl state);
- the subtitle: fs 16px / color rgb(100,116,139);
- the email + password inputs: h 48 / radius 12px / fs 14px / border 1px rgb(226,232,240);
- the Sign in button: w 368 / h 48 / radius 12px / fs 14px / fw 500 / bg rgb(15,23,42) / color white;
- the logo img: 96x96 / alt "ZeroBudget logo";
- the docSW 1280 no-overflow guard.

The pin rides no fixture (the logged-out storageState opt-out — the login-parity spec's own convention) and asserts the arbitration's own measured values, byte-identical on both sides' login cards at 1280x800.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → build → **278 e2e** in chunks (+1) → 35 smoke; the 16 standing screenshots regenerated + byte-compared (the same-DB discipline; the seedcheck under `env -u DATABASE_URL`). EXPECTED: the 07-add-item-modal shot carries the documented dialog-default DATE class (the calendar rolled 2026-10-16 → 2026-10-17 — the v66 lesson: exactly one 16-pixel-region diff per overnight regeneration, pixel-arbitrated, never a regression).

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the login card's geometry + typography census at 1280 (the card w/radius, the h1 family, the subtitle fs, the input pair's h/radius/fs/border, the signIn full chrome, the logo geometry, the docSW guard — the arbitration's own measured values) | tests/e2e/login-parity.spec.ts |
| 2 | sanity | the pin-sanity mutation: the h1's `sm:text-3xl` → `sm:text-2xl` → the pin FAILS at exactly the h1 axis; restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/login-card.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → build → 278 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (the 07 DATE class pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v75 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (277→278 + the v75 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v75 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 110 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.32 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v75 section (the new probes + the v75 lesson: the cold-session login census races its page load — the load-RETRIED census, never a single-shot read) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_180.md + the repo worklog Session 109 entry | docs/session_180.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v75.sh + login-census-ref-v75.sh censuses' own measured values, byte-identical on both sides' login views at 1280x800: the card (448/16px/rgba(255,255,255,0.95)), the h1 (30px/700/lh 36px/rgb(15,23,42)), the subtitle (16px/rgb(100,116,139)), the inputs (48/12px/14px/1px rgb(226,232,240)), the signIn (368x48/12px/14px/500/rgb(15,23,42)), the logo (96x96, alt "ZeroBudget logo"), the docSW 1280.
- The source confirms the values: `w-full max-w-md` (448) + `rounded-2xl` (16px) + the inline `backgroundColor: "rgba(255, 255, 255, 0.95)"` (login-card.tsx:558-561); the h1's `text-2xl ... sm:text-3xl` (30px/lh 36px at ≥640 — login-card.tsx:575); the content width 448 − 2×40 (md:px-10) = 368 (the signIn's w).
- The existing pins are SAFE: the v7 G2/G3 pins assert the SAME surfaces' COLORS (disjoint from the geometry/typography axes — no assertion collision); the v9 pins assert control heights + text (the signIn h 48 + 14px re-asserted consistently); the v13 focus-ring and v24 label-gap pins ride different axes; the login-parity spec's `test.use({ storageState: { cookies: [], origins: [] } })` opt-out is inherited by the new describe.
- The blast radius: ZERO production-code change (every flag arbitrated to a documented class — the pin-only line holds); the pin-sanity mutation touches `src/components/budget/login-card.tsx` (the h1's `sm:text-3xl` class) REVERTED before ship (`git diff src/` = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → build → 277 e2e (**278** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser run; the with-server boots fresh per command; the reference session EXPIRES between long eval gaps — the login-retry loop handles it; the cold-session login census needs the load-RETRIED finder (the v75 lesson — a single-shot read raced the page load and returned "form not found"); the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` + kill before every full-chain run (the v53 orphaned-webServer lesson); one-shot Prisma scripts need `env -u DATABASE_URL` (the sandbox's inherited parent-workspace URL is the documented pollution); no dollar sequences in census JS inside double-quoted bash strings (the v64 rule — the amount leaf is found via `String.fromCharCode(36)`); no attribute-value selectors in single-quoted eval strings (the v60/v67 rule); the QUOTED heredoc with the env-injected census (the v73 lesson); the mutations need the standalone REBUILD as a SEPARATE command (the v53 lesson); the clean-check gate re-runs AFTER every new file lands (the v69 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of bounds under the v46 read-only rule): the reference-side verify-email panel census, the forgot-confirm state census, the calculator EMPTY-state reference census, the line-items dialog glyphs.
- The v76 queue (suggestions): (1) the re-run cadence rotates to the next-oldest candidate after this pair (the v60-era networth + drill-down pair, last re-shot v67 — or the mobile 390 twins, last re-shot v69; the full re-run ledger is in the probe README), (2) the axe-core watch at its next re-check point (only a 5.x wrapper changes the calculus), (3) the deferred reference-write censuses (unchanged).
