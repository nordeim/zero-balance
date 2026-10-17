# Remediation Plan v78 — the re-run cycle's next-oldest candidate (the mobile 390 twins' second re-run — last re-shot v69) + the axe watch (NO DRIFT) + the breakdown card's mobile svg family + chart-absence + width census pin (PIN-ONLY)

The session's plan, validated against the codebase before execution. The formal narrative ships in `docs/session_186.md`; the repo worklog entry: Session 113.

## The v78 target selection (the ledger-verified queue)

The v77 plan's v78 queue suggested the mobile 390 twins (the networth + dashboard pair, last re-shot v69) — and this time the rotation ledger AGREES: by the cadence's own oldest-first rule (ordering by LAST RE-SHOT DATE), the remaining candidates are the mobile 390 twins (v69) < the v57-era items pair (last re-shot v70) < the v58–v61-era desktop pairs (re-shot v74–v77 this cycle). The v77 target-selection lesson applied: the queue suggestion was verified against the ledger before commitment — no correction needed this time. The pair also re-proves the v41 mobile-superset surfaces (the clone's fitting 1-col responsive summary card vs the reference's own 464px overflow) and the v62 subtitle-wrap class, nine iterations after their last mobile re-run.

## The v78 sweep — what the measurement found

### F0 [BASELINE] — fully GREEN as-shipped (no code defect)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (`npm run build` — the v76 static-copy lesson holds; robots + sitemap prerendered; the standalone static + public copies verified present) · **280 e2e ✓** (99 + 102 + 81 chunks = 279 chromium + 3 setups — the exact documented v77 state) · 35/35 smoke ✓. The workspace survived the session boundary intact (no reset): `main @ 67e988b` (v77 shipped + the session_184/185 transcripts), node_modules + `.env` + `db/custom.db` + chromium-1243 all verified, no orphaned servers, the seedcheck confirming the exact seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 4.15, no 5.x); npm-latest `axe-core` = 4.14.0 (only a canary prerelease beyond). The lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0 — verified in the lockfile's packages tree; no nested engine dir under `node_modules/@axe-core/playwright/`). The engine-contract pin executed GREEN standalone (2 passed). Only a 5.x wrapper (or a nested-engine change) changes the calculus; the next re-check point unchanged.

### F2 [STANDING] — the 72nd standing checks: ALL GREEN

ref-standing-v72.sh + standing-checks-v72.sh (version-bumped from v71 — version-bump-only diffs verified). Reference side: the four bugs ALL still live (the toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 72nd consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED WORKING (the 72nd consecutive time: `hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

### F3 [PAIR] — the mobile 390 twins' second re-run (the networth + dashboard full-page pair at 390x844, last re-shot v69): every flag DOM-arbitrated to a documented class — NO NEW GAP

vlm-shots-v78.sh + clone-vlmshots-v78.sh + vlm-compare-v78.mjs (login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference — the v46 rule holds). Both verdicts DIFFERENT, every flag a documented class:

- **PAIR 1 (NETWORTH at 390)**: the stat tiles side-by-side (ref) vs stacked (clone) — the v41 mobile-superset class; the asset groups/card contents — the seed-data class; the "Edit with Base44" overlay — the platform-chrome class; the avatar area — the user-identity class. Matching the v69 re-run's own flag set exactly (the v63-era classes re-confirmed).
- **PAIR 2 (DASHBOARD at 390)**: the subtitle wrap point — the v62 width-delta class (the reference's own 395px docSW overflow shifts its wrap by one word; the chrome byte-identical); the progress-bar length — the pct data class (the savings-percentage arithmetic under different seeds); the black tooltip over the breakdown rows — the Base44 platform chrome; the donut proportions/labels — the seed-data class.

The both-sides DOM census (arbit-v78.sh — the v75 convention: the census runs regardless of the verdict; the v69 census axes re-measured on BOTH sides at 390):

- **NETWORTH**: the medallion 64×64 + the trend icon 32×32 + the tiles h 84 + the grid gap 16px — BYTE-IDENTICAL on both sides; the deltas all the v41 mobile-superset class (the reference's card 432 wide / docSW 464 / fixed 2-col tiles 176×84 / medallion clipping at right 416 vs the clone's card 358 / docSW 390 / 1-col tiles 294×84 / medallion fitting at right 342 — the clone's responsive superset fix, zero drift since the v69/v63 censuses).
- **DASHBOARD**: the subtitle chrome BYTE-IDENTICAL (fs 16px / fw 400 / rgb(107,114,128) / lh 24px, the P h 48, the block h 92, 2 lines) — the wrap-point delta (ref "...expenses to / achieve net zero" vs clone "...and expenses / to achieve net zero") the v62 width-delta class (the reference's own 363px content column vs the clone's 358px, its docSW 395 overflow); the breakdown card's HEIGHT + SVG families byte-identical (h 324, svgCount 7, the first-four svgs [16×16, 14×14, 16×16, 14×14], rechartsWrappers 0, pieSectors 0 on BOTH sides — no donut in the breakdown card anywhere, the v69 disproof class); the 5px width family delta (card 363 vs 358, H3 313 vs 308, DIV 313×238 vs 308×238) the reference's own docSW-395 overflow class — the heights byte-identical.

**NO NEW GAP — the v78 iteration is PIN-ONLY.**

### F4 [PIN] — the Net Zero Breakdown card's mobile svg family + chart-absence + width census at 390 (PIN-ONLY for src/ — no production-code change; +1 e2e = 281)

The never-pinned axes (the existing pins cover around them: the v44 F2a pin asserts the card's HEIGHTS at 390 — 324/441/495 + the section/indent/cat geometry — never the WIDTH, the svg family, or the chart-absence; the v76 pin asserts the section icon chip at 1280 only; the v62 pin the subtitle block; the v49/v50/v51 families the donut legend / hero / stats / guidelines / quick-actions — never the breakdown card's mobile svg census):

- the CARD's mobile box: w 358 × h 324 (the w never pinned at 390 — the 390 − 2×16 page-padding arithmetic) + the docSW 390 guard;
- the SVG FAMILY: svgCount 7 + the full size census [16,14,16,14,16,14,16] (the three section icons 16×16 h-4 w-4 + the three collapsed chevrons 14×14 h-3.5 w-3.5 + the net-balance icon 16×16 — never pinned at any viewport);
- the CHART-ABSENCE contract: rechartsWrappers 0 + pieSectors 0 inside the breakdown card (the v69 donut-invention lesson's regression guard — the VLM claimed a "faint circle behind the text" donut that exists on NEITHER side; the census is the authority);
- the CHILDREN's width family: the H3 308×20 + the content DIV 308×238 (the 358 − 2×1 border − 2×24 p-6 arithmetic — never pinned).

The pin asserts the arbitration's own measured values, byte-identical on both sides' dashboards at 390x844.

**The pin-sanity mutation**: the collapsed section chevron's `h-3.5 w-3.5` → `h-4 w-4` (dashboard-view.tsx:339, the ChevronDownIcon branch) — flips exactly the three chevrons in the svg size family ([16,14,16,14,16,14,16] → [16,16,16,16,16,16,16]); the section row h stays 48 (the 32px h-8 w-8 chip governs the flex row), the card h stays 324, the v44 F2a height pins and the v76 1280 section-icon pin untouched (the category-level chevrons are h-3 w-3, a different class, unrendered when collapsed).

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → build (`npm run build`) → **281 e2e** in chunks (+1) → 35 smoke; the 16 standing screenshots regenerated + byte-compared (the same-DB discipline; the seedcheck under `env -u DATABASE_URL`). EXPECTED: any DATE-class diff pixel-arbitrated per the v66/v75 discipline, never a VLM verdict.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the breakdown card's mobile svg family + chart-absence + width census at 390 (the card w/h + docSW guard, the svgCount + the [16,14,16,14,16,14,16] size family, the rechartsWrappers/pieSectors 0 contract, the H3/DIV width family — the arbitration's own measured values) | tests/e2e/dashboard.spec.ts |
| 2 | sanity | the pin-sanity mutation: the collapsed section chevron's `h-3.5 w-3.5` → `h-4 w-4` (dashboard-view.tsx:339, the ChevronDownIcon branch) → the pin FAILS at exactly the svg-family axis (the three 14s → 16s); restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/dashboard-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 281 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v78 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (280→281 + the v78 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v78 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 113 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.35 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v78 section (the new probes + the ledger-verified queue note) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_186.md + the repo worklog Session 113 entry | docs/session_186.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v78.sh census's own measured values, byte-identical on both sides' dashboards at 390x844: the card `{w: 358, h: 324}`; the svgs `[16×16, 14×14, 16×16, 14×14, 16×16, 14×14, 16×16]` (svgCount 7); `rechartsWrappers: 0, pieSectors: 0`; the children `[{H3, 308, 20}, {DIV, 308, 238}]`; the docSW guard 390.
- The source confirms the values: the card's `rounded-2xl p-6` + border (dashboard-view.tsx:495); the H3's `mb-4 text-sm font-medium` (:496-497); the content DIV's `space-y-3` (:499); the section icon's `h-4 w-4` (:317); the collapsed chevron's `h-3.5 w-3.5` (:339); the net icon's `h-4 w-4` (:535); the page's `p-4` mobile padding (the 390 − 32 = 358 card arithmetic).
- The pin-sanity target: the ChevronDownIcon's `h-3.5 w-3.5` → `h-4 w-4` flips ONLY the three collapsed section chevrons (14→16) — the family's own headline axis; the category-level chevrons are `h-3 w-3` (a different class, unrendered when collapsed); no other pinned axis (card h 324 / section h 48 / the v44 heights / the v76 1280 chip / the v62 subtitle) is touched. The v76 finder-description lesson applied: the pin's card finder is the exact H3-text walk-up the arbitration itself used (the 'Net Zero Breakdown' leaf → 6-parent radius/white walk), and the census dumps the matched card's tag/size — no wrapper ambiguity.
- The existing pins are SAFE: the v44 F2a pin asserts the card's heights + section/indent/cat geometry (disjoint from the width/svg/chart-absence axes); the v76 pin asserts the section icon chip + donut labels at 1280 (a different viewport + different axes — the chevron never asserted); the v62 pin the subtitle block (disjoint surface); the v43/v44 glyph-swap pins assert the chevron's GLYPH identity (down-collapsed/up-expanded) + visibility, never its size; the breakdown.spec.ts chevron test asserts visibility only.
- The blast radius: ZERO production-code change (every census delta a documented class — the pin-only line holds); the pin-sanity mutation touches `src/components/budget/dashboard-view.tsx:339` (the ChevronDownIcon's className) REVERTED before ship (`git diff src/` = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` → 280 e2e (**281** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser run; the with-server boots fresh per command; the reference session EXPIRES between long eval gaps — the login-retry loop handles it; the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` + kill before every full-chain run (the v53 orphaned-webServer lesson); one-shot Prisma scripts need `env -u DATABASE_URL`; no dollar sequences in census JS inside double-quoted bash strings (the v64 rule); no attribute-value selectors in single-quoted eval strings (the v60/v67 rule); the QUOTED heredoc with the env-injected census (the v73 lesson); the mutations need the standalone REBUILD as a SEPARATE command (the v53 lesson); the clean-check gate re-runs AFTER every new file lands (the v69 lesson); the build step is `npm run build` (the v76 F0 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of bounds under the v46 read-only rule): the reference-side verify-email panel census, the forgot-confirm state census, the calculator EMPTY-state reference census, the line-items dialog glyphs.
- The v79 queue (suggestions): (1) the re-run cadence rotates to the next-oldest candidate after this pair (the v57-era items pair [income + expenses at desktop 1280], last re-shot v70 — now the oldest remaining [v70 < v74–v78]), (2) the axe-core watch at its next re-check point (only a 5.x wrapper changes the calculus), (3) the deferred reference-write censuses (unchanged).
