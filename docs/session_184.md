# Session 184 — Parity iteration v77: the re-run cycle's next-oldest candidate (the v61-era dashboard pair's second re-run) + the axe watch (NO DRIFT) + the Budget Guidelines interior-text family + quick-action icon viewBox pin (PIN-ONLY)

**Date:** 2026-10-17 · **Plan:** `docs/remediation-plan-v77.md` · **Worklog:** Session 111 · **Commit:** the v77 parity iteration (PIN-ONLY — no production-code change; +1 e2e = 280)

## The session's target selection (the judgment call, documented)

The v76 plan's v77 queue suggested the mobile 390 twins (the networth + dashboard pair, last re-shot v69). The re-run ledger said otherwise: by the cadence's own oldest-first rule (the v74 "the re-run cycle's OLDEST candidate … the only pre-v70 pair not re-run since" convention — ordering by LAST RE-SHOT DATE), the **v61-era pair (the dashboard FULL-PAGE at desktop 1280x800 — the Budget Guidelines card + the quick-action row, last re-shot v68)** is the oldest remaining candidate (v68 < v69). The v76 suggestion skipped it. The correction: v77 re-runs the v61-era pair; the mobile 390 twins become the v78 candidate. The choice also re-proves the v61 STRETCH-fix surfaces sixteen iterations after their fix, and complements v76's drill-down EXPANDED re-run (the dashboard's other state).

## The environment (preserved — no reset)

The workspace survived the session boundary intact: `main @ 9d694b3` (v76 shipped + the session_183 transcript), node_modules + `.env` (DATABASE_URL="file:../db/custom.db", db/ at the repo root) + `db/custom.db` + chromium-1243 all verified, no orphaned servers, the seedcheck confirming the exact seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

## F0 — the baseline chain: FULLY GREEN as-shipped

lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (`npm run build` — the v76 F0 lesson applied: the standalone static + public copies verified present; robots + sitemap prerendered) · **279 e2e ✓** (98 + 64 + 119 chunks = 278 chromium + 3 setups — the exact documented v76 state) · 35/35 smoke ✓. No code defect, no environment lesson this session — the v76 lesson (never a bare `npx next build`) held by construction.

## F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 4.15, no 5.x); npm-latest `axe-core` = 4.14.0 (only a canary prerelease beyond). The lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0; no nested engine dir under `node_modules/@axe-core/playwright/`). The engine-contract pin GREEN standalone (2 passed).

## F2 — the 71st standing checks: ALL GREEN

ref-standing-v71.sh + standing-checks-v71.sh (version-bumped from v70 — version-bump-only diffs verified against the convention). Reference side: the four bugs ALL still live (the toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 71st consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED WORKING (the 71st consecutive time: `hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

## F3 — the re-run pair: the v61-era dashboard FULL-PAGE at 1280 — VERDICT IDENTICAL, ZERO style flags — NO NEW GAP

vlm-shots-v77.sh + clone-vlmshots-v77.sh + vlm-compare-v77.mjs (login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference — the v46 rule holds). The VLM verdict **IDENTICAL** — the LAYOUT/STYLE section explicitly empty: the Budget Guidelines card (geometry, border, header typography, row tints, row padding, label/percent/description typography and colors) and the Quick Action cards (geometry, radius, padding, border, icon tile size/radius/tint, icon graphic size, label typography, plus icon size/opacity/placement) all visually identical. The reported deltas all DATA (the seed classes: the allocation pct, the balance/income/savings/expenses figures, the stat cards, the donut proportions) + the v56 root-URL active-nav class + the avatar-letter user-identity class — matching the v68 re-run's own IDENTICAL verdict (zero VLM-layer drift since v68).

The both-sides DOM census (arbit-v77.sh — the v75 convention: the IDENTICAL verdict's both-sides census, the v61 qa-census axes re-measured on BOTH sides at 1280):

- **PART G (the guidelines card) — byte-identical on every axis, ZERO drift since v61:** the card 468×348/radius 12px/border rgb(229,231,227) 1px/white (the h 348 = the v61 STRETCH-fix natural height — the contract holds 16 iterations later); the header pad 24px/fs 16px/fw 600/color rgb(26,58,46)/lh 16px/tracking -0.4px; the body pad "0px 24px 24px"/block; tileCount 3; the three tiles each 418×78/radius 8px/pad 16px with the three tint+border pairs (Needs #fff7f5/#fcddd5, Wants #f0f7fb/#d4e9f5, Savings #f5f9f0/#dfecd0) + the label fs 16px/fw 500/type colors + the pct fs 14px/fw 400/type colors + the desc fs 12px/color rgb(107,114,128)/lh 16px. The card shadow's transparent lead layers (ref 2 vs clone 4) the **v66 computed-form class** — the VISIBLE layers byte-identical.
- **PART Q (the quick-action row) — byte-identical on every axis:** the grid display grid/template "304px 304px 304px"/gap 24px/w 960; the three cards each 304×90/radius 16px/pad 24px/white/border/shadow none/textAlign left/transition 0.2s; the tiles 40×40/radius 12px with the three type tints; the icons 20×20 with the three type colors + viewBox "0 0 24 24"; the plus 16×16/opacity 0.5/type colors. The label's fw/color delta (ref 500/rgb(26,58,46) vs clone 400/rgb(10,10,10)) is the **v61 label lesson re-learned** — the census's bare textContent finder catches the clone's row WRAPPER span while the reference's first match is the leaf; the v61 F3 pin's LEAF-span finder measures the leaf chrome byte-identical (and passed in the F0 baseline). The grid mt (ref 0px vs clone 32px) the **margin-structure class** — the rendered cross-row gap byte-identical (PART X: gap 340, cardBottom 1122, gridTop 1462 on BOTH sides).
- **PART X (the cross-row gap) — byte-identical:** gap 340/cardBottom 1122/gridTop 1462 both sides.
- The seedcheck after the census: the exact seed state.

**NO NEW GAP — the v77 iteration is PIN-ONLY.**

## F4 — the pin: the Budget Guidelines interior-text family + the quick-action icons' viewBox census at 1280 (PIN-ONLY; +1 e2e = 280)

The never-pinned axes (the v61 F2 pin covers the card's box chrome + the FIRST tile + the STRETCH contract; the v51 F4 pin covers the tiles' text family at 390 ONLY; the v61 F3 pin covers the quick-action chrome but never the icons' viewBox):

- the HEADER's full typography: fs 16px / fw 600 / color rgb(26,58,46) / **lh 16px** (leading-none) / **tracking -0.4px** (tracking-tight) — the lh + tracking never pinned;
- the three TILES' full census at 1280 (the v51 F4 family's desktop twin): each 418×78 (the one-line-desc arithmetic at the 418px width — the mobile twin's 94/94/78 contrast)/radius 8px/pad 16px/the three tint+border pairs + the label {fs 16px, fw 500, the type color} + the pct {fs 14px, fw 400, the type color} + the desc {fs 12px, color rgb(107,114,128), lh 16px};
- the QUICK-ACTION ICONS' viewBox "0 0 24 24" (the three type icons — the v76 glyph-pin family's quick-action extension; the w/h/color already pinned by v61 F3).

The pin asserts the arbitration's own measured values, byte-identical on both sides' dashboards at 1280×800. **GREEN on first run.** The pin-sanity mutation (the tile label's `font-medium` → `font-normal` at dashboard-view.tsx:848) verified to **FAIL at exactly the three tiles' label.fw axes** (fw 500→400 — the deep-equality diagnostic showing the label object's fw line), then restored (the standalone REBUILD as a SEPARATE command; `git diff src/` = 0 lines). The v76 finder-description lesson applied: the pin's tile finder is the v61 census's own chrome-based finder, and the label leaf is the tile's FIRST span (the pct the LAST) — no wrapper ambiguity in the guidelines tiles.

## F5 — the full chain re-run + the screenshots: ALL GREEN

lint → typecheck → 108 unit → `npm run build` → **280 e2e** (99 + 64 + 119 chunks = 279 chromium + 3 setups — +1 the v77 pin) → 35/35 smoke. The screenshots **16/16 BYTE-IDENTICAL** — the eighth consecutive fully-identical set (the same-day regeneration, no calendar rollover since the v75 re-baseline). The seedcheck under `env -u DATABASE_URL` after the captures: the exact seed state.

## The docs alignment (D1–D7)

D1 AGENTS.md (the v77 paragraph), D2 CLAUDE.md (the 280 state + the v77 pin clause), D3 README.md (the counts + the v77 plan-table row), D4 zero-balance_SKILL.md (the Session 112 audit row + the three state lines), D5 the PAD's v1.1.34 revision block, D6 the probe README's v77 section (the probes + the target-selection note + the lessons), D7 this narrative + the worklog Session 111 entry.

## The probe lessons

1. **THE TARGET-SELECTION LESSON:** verify a queue suggestion against the rotation ledger before executing it — the v76 plan's v77 queue named the mobile 390 twins (last re-shot v69) while the ledger's own oldest-first rule pointed at the v61-era pair (last re-shot v68). A queue suggestion is a hint, not a commitment; the ledger is the truth.
2. **THE v61 WRAPPER-VS-LEAF LABEL LESSON re-confirmed live:** the quick-action label's WRAPPER span still reads fw 400/rgb(10,10,10) under a bare textContent finder while the reference's first match is the leaf (fw 500/rgb(26,58,46)) — the DOM shapes differ, the leaf chrome does not. Keep pinning the LEAF (the exact text + zero element children), and expect the wrapper delta to reappear in any census that forgets the finder discipline.
