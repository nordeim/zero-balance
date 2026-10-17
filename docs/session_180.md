# Session 180 — Parity iteration v75: the re-run cycle's next-oldest candidate (the v59-era login + calculator pair's second re-run) + the login card's geometry + typography pin (PIN-ONLY)

The v75 cycle — the session-179 queue's first item. With the v74 savings re-run shipped, the re-run cadence rotates to the next-oldest candidate: the v59-era pair (the login view + the calculator dialog at desktop 1280), last re-shot v66. Plus the axe-core watch at its re-check point and the 69th standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 278.** The plan: `docs/remediation-plan-v75.md`.

## The environment (preserved — no reset this session)

The workspace survived the session boundary intact: the repo at `main @ d6c278a` (v74 shipped + the session_179 transcript), `git pull` fast-forwarding nothing new beyond it, `node_modules` + `.env` + `db/` + the chromium-1243 cache all verified in place, and the seedcheck confirming the exact documented seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

## F0 — the baseline chain FULLY GREEN as-shipped (no F0 finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots.txt + sitemap.xml prerendered) · **277 e2e ✓** (84 + 74 + 122 chunks = 276 chromium + 3 setups — the exact documented v74 state) · 35/35 smoke ✓.

## F1 — the axe-core watch at its re-check point: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 5.x); npm-latest `axe-core` = 4.14.0 (only a canary beyond). The lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0 — verified via the lockfile's packages tree; no nested engine dir). The engine-contract pin GREEN standalone (2 passed). Only a 5.x wrapper (or a nested-engine change) changes the calculus.

## F2 — the 69th standing checks: ALL GREEN

ref-standing-v69.sh + standing-checks-v69.sh (version-bumped from v68 — version-bump-only diffs verified against the v67→v68 convention, the ordinal included). Reference side: the four bugs ALL still live (the toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 69th consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED WORKING (the 69th consecutive time: `hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

## F3 — the re-run pair: the login view + the calculator dialog at desktop 1280x800 — NO NEW GAP, every flag DOM-arbitrated

vlm-shots-v75.sh + clone-vlmshots-v75.sh + login-shots-v75.sh + clone-login-shots-v75.sh (login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference — the v46 rule holds; the clone's calculator twin riding the v66 fixture discipline: the "Contents Insurance" $25 line item added through the real UI then FULLY restored — the Delete cleanup + Rent's $1850 re-edit + the "3 items · $2235.00" page-total verification). The VLM verdicts:

- **PAIR 1 (the LOGIN view — the logged-out surface): VERDICT IDENTICAL, zero style flags** (the only observable delta the Base44 "Edit with" FAB — the platform-chrome class). The both-sides census (the shared LOGIN_CENSUS_JS via arbit-v75.sh, the reference side re-run through login-census-ref-v75.sh after the cold-session race): **byte-identical on every axis** — the card 448 / radius 16px / bg rgba(255,255,255,0.95) / border 0; the h1 "Welcome to ZeroBudget" 30px/700/lh 36px/rgb(15,23,42); the subtitle "Sign in to continue" 16px/rgb(100,116,139); the logo img 96×96/alt "ZeroBudget logo"; the email + password inputs h 48/radius 12px/border 1px rgb(226,232,240)/fs 14px/the exact placeholder pair; the Sign in button 368×48/radius 12px/bg rgb(15,23,42)/color white/14px/500; the links [] BOTH sides (the mode switchers are buttons, not anchors — a DOM-shape note); the Google + OR-divider blocks BOTH present; the docSW 1280. The card shadow's VISIBLE layer byte-identical (`rgba(0, 0, 0, 0.25) 0px 25px 50px -12px`); the lead-layer count differs (the reference's 2 transparent leads vs the clone's 4 — the v66 documented computed-form class; zero-alpha layers render nothing).
- **PAIR 2 (the CALCULATOR dialog): DIFFERENT with three flags, every one DOM-arbitrated via arbit-v75.sh (the both-sides CALC_CENSUS_JS census — the amount leaf found via `String.fromCharCode(36)`, the v64 dollar rule) to a documented class**:
  - the "extra will-update line" = the **v66 DATA-CONDITIONAL class** re-verified live (`hasWillUpdateSpan` false on the reference — its Rent natively $25.00 === its line-item total $25.00 → hidden; true on the clone — its dialog opened at $1850 while the recalculated total is $25.00 → shown; the span's chrome pinned at v73);
  - the "row hover state" = the **v66 pointer-position class** re-verified live (`actionsAtRest {opacity: "0", btnCount: 2}` on BOTH sides — the actions rest at opacity 0; the reference's screenshot caught them mid-reveal because the shot precedes the pointer park, the clone's follows it);
  - the "amount alignment" = the **pointer-position corollary** (the amount's own chrome byte-identical — 20px/700/rgb(224,122,59)/h 28; the horizontal delta is the hover-revealed action pair's footprint).
  - The full census otherwise **byte-identical**: the panel 768×393/radius 16px/maxW 768px/bg white; the scrim rgba(26,58,46,0.5)/blur(8px)/1280×800; the title 18px/700/rgb(26,58,46)/lh 28px; the desc 14px/rgb(107,114,128)/lh 20px; the close 36×36/radius 6px/transparent (the clone's Radix close; the reference's carries the v73-measured same-family chrome — its empty-text button missed the finder, a census note, not a gap); the totalCard 720×90/pad 16px/radius 12px/border 1px solid rgb(252,221,213); the nameH4 16px/600/rgb(26,58,46)/h 24/mb 4px; the row 720×102/pad 16px/radius 12px/borderTop 1px solid rgb(229,231,227)/bg white; the pillRow flex/gap 8px/12px/h 20; the pill1 20×65/pad 2px 8px/radius 9999px/12px/400; the addBtn 110×32/radius 6px/12px/500/white; the docSW 1280. The panel shadow: the reference's 3-layer form (2 transparent leads) vs the clone's single-layer — the v66 documented computed-form class (the visible layer byte-identical).
- The seedcheck after the fixture cycle: the exact seed state.

**NO NEW GAP — the v75 iteration is PIN-ONLY.**

## F4 — the pin: the login card's geometry + typography census at 1280 (+1 e2e = 278)

The never-pinned axes (the coverage map: the v7 G2/G3 pins lock the login surface's COLORS — the slate family, the card bg, the bar/page gradients, the submit bg/color/h, the email border/bg; the v9 pins the per-state control heights + 14px text; the v13 pin the focus rings; the v24 pins the label gaps + mobile families; the v55 glyph pin the login icons — the card's WIDTH + RADIUS, the h1's TYPOGRAPHY family (fs/fw/lh — only its color was pinned), the subtitle's fs, the Sign in button's FULL chrome (w/radius/fs/fw), the logo's geometry, and the input radius/fs family at desktop were never pinned). The pin (tests/e2e/login-parity.spec.ts, a new describe at the tail, the logged-out storageState opt-out, fixture-free):

- the CARD geometry: w 448 (the max-w-md wrapper) / radius 16px (rounded-2xl) / bg rgba(255,255,255,0.95) (re-asserted alongside);
- the h1 typography: fs 30px / fw 700 / lh 36px / color rgb(15,23,42) (the sm:text-3xl state);
- the subtitle: fs 16px / color rgb(100,116,139);
- the email + password inputs: h 48 / radius 12px / fs 14px / border 1px rgb(226,232,240);
- the Sign in button: w 368 / h 48 / radius 12px / fs 14px / fw 500 / bg rgb(15,23,42) / color white;
- the logo img: 96×96 / alt "ZeroBudget logo";
- the docSW 1280 no-overflow guard.

The pin **GREEN on first run**. The pin-sanity mutation (the h1's `sm:text-3xl` → `sm:text-2xl` in `src/components/budget/login-card.tsx`): the standalone REBUILD as a SEPARATE command → the pin **FAILS at exactly the h1 axis** (fs 30px→24px, every other axis green) → restored → rebuilt → GREEN. `git diff src/` = 0 lines — **PIN-ONLY holds.**

## F5 — the full chain re-run + the screenshots

lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ (robots + sitemap) · **278 e2e ✓** (84 + 74 + 122 chunks = 277 chromium + 3 setups) · 35/35 smoke ✓. The 16 standing screenshots regenerated + byte-compared: **15/15 byte-identical + 07-add-item-modal the documented dialog-default DATE class** (the calendar rolled 2026-10-16 → 2026-10-17; pixel-arbitrated via pixel-diff-v75.py — the 16×22 px region at (1552,931)-(1568,953), the exact v66 bbox, everything else in the 2880×1800 frame byte-stable; the new shot re-baselined). The seedcheck (under `env -u DATABASE_URL`): the exact seed state.

## The docs alignment

D1 AGENTS.md (the v75 paragraph), D2 CLAUDE.md (278 + the v75 pin clause), D3 README.md (the counts + the v75 plan-table row), D4 zero-balance_SKILL.md (Session 110 audit row + the state lines), D5 the PAD's v1.1.32 revision block, D6 the probe README's v75 section (the probes + the three lessons), D7 this narrative + the worklog's Session 109 entry. The lint gate re-runs after every new file (the v69 lesson).

## The probe lessons

1. **The cold-session login census races its page load**: the arbitration's first reference-side login read returned `"form": "not found"` — the fresh context's first navigation hadn't painted the form at census time. The load-RETRIED census (login-census-ref-v75.sh — loop the open + census until the form lands) is the reliable pattern for a cold-context surface; never accept a "not found" as a verdict.
2. **The login card's shadow arbitrates through the VISIBLE layer**: the reference's computed string carries 2 transparent lead layers, the clone's 4 (different engines, different lead counts) — the rendered chrome (the one non-transparent layer) is byte-identical. The v66 computed-form class generalizes: compare the full string, classify on the visible layer.
3. **The DATE-class screenshot diff recurs every calendar rollover**: expect exactly one small-region diff per overnight regeneration and arbitrate it programmatically (the PIL bbox + the region size — the exact v66 bbox recurs), never with a VLM verdict.

## The ship

The changeset reviewed clean (`src/` untouched — PIN-ONLY; no key material; the `.env.example` re-verified against the codebase — unchanged, still matching). The commit + the SSH-wrapper push per `docs/how-to-git-push-using-ssh-wrapper_SKILL.md` (the explicit `--remote` dry-run first, the operator key materialized 0600 and shredded after). **v75 complete: `main` remote-verified via the wrapper.**

## Suggested next (the v76 queue)

(1) The re-run cadence rotates to the next-oldest candidate after this pair — the v60-era networth + drill-down pair (last re-shot v67) or the mobile 390 twins (last re-shot v69); the full re-run ledger is in the probe README. (2) The axe-core watch at its next re-check point (only a 5.x wrapper changes the calculus). (3) The deferred reference-write censuses (unchanged, blocked by the v46 read-only rule). The full queue: `docs/remediation-plan-v75.md`.
