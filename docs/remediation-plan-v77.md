# Remediation Plan v77 — the re-run cycle's next-oldest candidate (the v61-era dashboard pair's second re-run — last re-shot v68) + the axe watch (NO DRIFT) + the guidelines interior-text family + quick-action icon viewBox pin (PIN-ONLY)

The session's plan, validated against the codebase before execution. The formal narrative ships in `docs/session_184.md`; the repo worklog entry: Session 111.

## The v77 target selection (the session's judgment call, documented)

The v76 plan's v77 queue suggested the mobile 390 twins (the networth + dashboard pair, last re-shot v69). The re-run ledger says otherwise: by the cadence's own oldest-first rule (the v74 "the re-run cycle's OLDEST candidate … the only pre-v70 pair not re-run since" convention — ordering by LAST RE-SHOT DATE), the **v61-era pair (the dashboard FULL-PAGE at desktop 1280x800 — the Budget Guidelines card + the quick-action row, last re-shot v68)** is the oldest remaining candidate (v68 < v69). The v76 suggestion skipped it. The correction: v77 re-runs the v61-era pair; the mobile 390 twins (last re-shot v69) become the v78 candidate. The choice also re-proves the v61 STRETCH-fix surfaces (the guidelines card's natural-height contract) sixteen iterations after their fix, and complements v76's drill-down EXPANDED re-run (the dashboard's other state).

## The v77 sweep — what the measurement found

### F0 [BASELINE] — fully GREEN as-shipped (no code defect)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (`npm run build` — the F0 static-copy lesson holds; robots + sitemap prerendered; the standalone static + public copies verified present) · **279 e2e ✓** (98 + 64 + 119 chunks = 278 chromium + 3 setups — the exact documented v76 state) · 35/35 smoke ✓. The workspace survived the session boundary intact (no reset): `main @ 9d694b3` (v76 shipped + the session_183 transcript), node_modules + `.env` + `db/custom.db` + chromium-1243 all verified, no orphaned servers, the seedcheck confirming the exact seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 4.15, no 5.x); npm-latest `axe-core` = 4.14.0 (only a canary prerelease beyond). The lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0 — verified in the lockfile's packages tree; no nested engine dir under `node_modules/@axe-core/playwright/`). The engine-contract pin executed GREEN standalone (2 passed). Only a 5.x wrapper (or a nested-engine change) changes the calculus; the next re-check point unchanged.

### F2 [STANDING] — the 71st standing checks: ALL GREEN

ref-standing-v71.sh + standing-checks-v71.sh (version-bumped from v70 — version-bump-only diffs verified against the v69→v70 convention). Reference side: the four bugs ALL still live (the toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 71st consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED WORKING (the 71st consecutive time: `hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

### F3 [PAIR] — the v61-era pair's second re-run (the dashboard FULL-PAGE at desktop 1280x800 — the Budget Guidelines card + the quick-action row below the fold, last re-shot v68): VERDICT IDENTICAL, ZERO style flags — NO NEW GAP

vlm-shots-v77.sh + clone-vlmshots-v77.sh + vlm-compare-v77.mjs (login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference — the v46 rule holds). The VLM verdict **IDENTICAL** — the LAYOUT/STYLE section explicitly zero: the Budget Guidelines card (geometry, border, header typography, row tints, row padding, label/percent/description typography and colors) and the Quick Action cards (geometry, radius, padding, border, icon tile size/radius/tint, icon graphic size, label typography, plus icon size/opacity/placement) all visually identical. The reported deltas all DATA (the expected seed classes: the allocation pct, the balance/income/savings/expenses figures, the stat cards, the donut proportions) + the v56 root-URL active-nav class + the avatar-letter user-identity class — every one a documented class, matching the v68 re-run's own IDENTICAL verdict (zero drift since v68 on the VLM layer).

The both-sides DOM census (arbit-v77.sh — the v75 convention: the IDENTICAL verdict's census, the v61 qa-census axes re-measured on BOTH sides at 1280):

- **PART G (the guidelines card) — byte-identical on every axis, ZERO drift since v61:** the card 468×348/radius 12px/border rgb(229,231,227) 1px/white (the h 348 = the v61 STRETCH-fix natural height — the contract holds 16 iterations later); the header pad 24px/fs 16px/fw 600/color rgb(26,58,46)/**lh 16px/tracking -0.4px**; the body pad "0px 24px 24px"/block; tileCount 3; the three tiles each 418×78/radius 8px/pad 16px with the three tint+border pairs (Needs #fff7f5/#fcddd5, Wants #f0f7fb/#d4e9f5, Savings #f5f9f0/#dfecd0) + the label fs 16px/fw 500/type colors + the pct fs 14px/fw 400/type colors + the desc fs 12px/color rgb(107,114,128)/lh 16px. The card shadow's transparent lead layers (ref 2 vs clone 4) the **v66 computed-form class** — the VISIBLE layers byte-identical.
- **PART Q (the quick-action row) — byte-identical on every axis:** the grid display grid/template "304px 304px 304px"/gap 24px/w 960; the three cards each 304×90/radius 16px/pad 24px/white/border/shadow none/textAlign left/transition 0.2s; the tiles 40×40/radius 12px with the three type tints; the icons 20×20 with the three type colors + viewBox "0 0 24 24"; the plus 16×16/opacity 0.5/type colors. The label's fw/color delta (ref 500/rgb(26,58,46) vs clone 400/rgb(10,10,10)) is the **v61 label lesson re-learned** — the census's bare textContent finder catches the clone's row WRAPPER span while the reference's first match is the leaf; the v61 F3 pin's LEAF-span finder measures the leaf chrome byte-identical (fw 500/rgb(26,58,46)) and passed in the F0 baseline. The grid mt (ref 0px vs clone 32px) the **margin-structure class** — the rendered cross-row gap byte-identical (PART X: gap 340, cardBottom 1122, gridTop 1462 on BOTH sides — the internal margin distribution differs, the rendered geometry does not; the v72 structural-class family).
- **PART X (the cross-row gap) — byte-identical:** gap 340/cardBottom 1122/gridTop 1462 both sides.
- The seedcheck after the census: the exact seed state.

**NO NEW GAP — the v77 iteration is PIN-ONLY.**

### F4 [PIN] — the guidelines card's interior-TEXT family + the quick-action icons' viewBox census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 280)

The never-pinned axes (the existing pins: the v61 F2 pin covers the guidelines card's box chrome + the FIRST tile only — the header's lh/tracking, the tiles 2/3 (Wants/Savings) chrome, and ALL three tiles' label/pct/desc TEXT chrome never pinned at 1280; the v51 F4 pin covers the tiles' text family at 390 ONLY (the mobile h 94/94/78 two-line-desc arithmetic); the v61 F3 pin covers the quick-action cards/tiles/label/plus chrome — the icons' viewBox never pinned, the v76 pin's glyph family covering the breakdown section icon only):

- the HEADER's full typography: fs 16px / fw 600 / color rgb(26,58,46) / **lh 16px** (leading-none) / **tracking -0.4px** (tracking-tight) — the lh + tracking never pinned;
- the three TILES' full census at 1280 (the v51 F4 family's desktop twin): each 418×78 (the one-line-desc arithmetic at the 418px width — the mobile twin's 94/94/78 contrast)/radius 8px/pad 16px/the three tint+border pairs + the label {fs 16px, fw 500, the type color} + the pct {fs 14px, fw 400, the type color} + the desc {fs 12px, color rgb(107,114,128), lh 16px};
- the QUICK-ACTION ICONS' viewBox "0 0 24 24" (the three type icons — the v76 glyph-pin family's quick-action extension; the w/h/color already pinned by v61 F3).

The pin asserts the arbitration's own measured values, byte-identical on both sides' dashboards at 1280x800.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → build (`npm run build`) → **280 e2e** in chunks (+1) → 35 smoke; the 16 standing screenshots regenerated + byte-compared (the same-DB discipline; the seedcheck under `env -u DATABASE_URL`). EXPECTED: any DATE-class diff pixel-arbitrated per the v66/v75 discipline, never a VLM verdict.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the guidelines card's interior-TEXT family + the quick-action icons' viewBox census at 1280 (the header fs/fw/color/lh/tracking + the three tiles' box + label/pct/desc chrome + the icons' viewBox — the arbitration's own measured values) | tests/e2e/dashboard.spec.ts |
| 2 | sanity | the pin-sanity mutation: the tile label's `font-medium` → `font-normal` (dashboard-view.tsx:852, the GUIDELINE_ROWS label span) → the pin FAILS at exactly the three tiles' label.fw axes (fw 500→400); restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/dashboard-view.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 280 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v77 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (279→280 + the v77 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v77 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 112 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.34 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v77 section (the new probes + the target-selection note + the wrapper-vs-leaf lesson re-confirmation) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_184.md + the repo worklog Session 111 entry | docs/session_184.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v77.sh census's own measured values, byte-identical on both sides' dashboards at 1280x800: the header `{pad: "24px", fs: "16px", fw: "600", color: "rgb(26, 58, 46)", lineHeight: "16px", tracking: "-0.4px"}`; the tiles `[{w: 418, h: 78, radius: "8px", pad: "16px", bg: "rgb(255, 247, 245)", border: "rgb(252, 221, 213)", label: {text: "Needs", fs: "16px", fw: "500", color: "rgb(224, 122, 59)"}, pct: {text: "~50%", fs: "14px", fw: "400", color: "rgb(224, 122, 59)"}, desc: {fs: "12px", color: "rgb(107, 114, 128)", lh: "16px"}}, {…Wants rgb(59, 126, 161)…}, {…Savings rgb(143, 188, 63)…}]`; the quick-action icons' `viewBox: "0 0 24 24"` (all three).
- The source confirms the values: the header's `font-semibold leading-none tracking-tight` + the forestDark style (dashboard-view.tsx:837); the tile label's `font-medium` + the type-color style (:852); the pct's `text-sm` (:855); the desc's `text-xs` + the gray style (:860); the GUIDELINE_ROWS trio's tints/borders/colors (src/lib/constants.ts:203); the quick-action icons' legacy factory viewBox (src/components/ui/legacy-icons.tsx).
- The pin-sanity target: the tile label's `font-medium` → `font-normal` flips ONLY the label fw (500→400) on all three tiles — the family's own headline axis; every other pinned axis (fs/color/pct/desc/header/viewBox) untouched. The v76 finder-description lesson applied: the pin's tile finder is the v61 census's own chrome-based finder (radius 8px + the 40–200px height + a span/p child + a tinted bg), and the label leaf is the tile's FIRST span (the pct the LAST) — no wrapper ambiguity in the guidelines tiles (the v61 label lesson's quick-action-only trap re-confirmed by the census delta).
- The existing pins are SAFE: the v61 F2 pin asserts the card + firstTile box + the STRETCH contract (disjoint from the text axes); the v51 F4 pin asserts the tiles' text family at 390 (a different viewport — the h 94/94/78 mobile arithmetic, never contradicted); the v61 F3 pin asserts the quick-action chrome + the leaf-label (the viewBox an additive axis); the v76 pin covers the breakdown section icon + donut labels (disjoint surfaces).
- The blast radius: ZERO production-code change (the VLM verdict IDENTICAL + every census delta a documented class — the pin-only line holds); the pin-sanity mutation touches `src/components/budget/dashboard-view.tsx:852` (the `font-medium` class) REVERTED before ship (`git diff src/` = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` → 279 e2e (**280** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser run; the with-server boots fresh per command; the reference session EXPIRES between long eval gaps — the login-retry loop handles it; the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` + kill before every full-chain run (the v53 orphaned-webServer lesson); one-shot Prisma scripts need `env -u DATABASE_URL`; no dollar sequences in census JS inside double-quoted bash strings (the v64 rule); no attribute-value selectors in single-quoted eval strings (the v60/v67 rule); the QUOTED heredoc with the env-injected census (the v73 lesson); the mutations need the standalone REBUILD as a SEPARATE command (the v53 lesson); the clean-check gate re-runs AFTER every new file lands (the v69 lesson); the build step is `npm run build` (the v76 F0 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of bounds under the v46 read-only rule): the reference-side verify-email panel census, the forgot-confirm state census, the calculator EMPTY-state reference census, the line-items dialog glyphs.
- The v78 queue (suggestions): (1) the re-run cadence rotates to the next-oldest candidate after this pair (the mobile 390 twins — the networth + dashboard pair, last re-shot v69 — the v76 plan's own suggestion, now next in line), (2) the axe-core watch at its next re-check point (only a 5.x wrapper changes the calculus), (3) the deferred reference-write censuses (unchanged).
