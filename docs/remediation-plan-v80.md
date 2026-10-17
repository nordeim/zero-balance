# Remediation Plan v80 — the re-run cycle's next-oldest candidate (the v58-era savings pair's third re-run — last re-shot v74) + the axe watch (NO DRIFT) + the savings goal-card's card-height twins + title-row geometry + border/bg pin (PIN-ONLY)

The session's plan, validated against the codebase before execution. The formal narrative ships in `docs/session_190.md`; the repo worklog entry: Session 115.

## The v80 target selection (the ledger-verified queue)

The v79 plan's v80 queue suggested the v58-era savings pair (the savings view at desktop 1280, last re-shot v74) — and the rotation ledger AGREES: by the cadence's own oldest-first rule (ordering by LAST RE-SHOT DATE), the remaining candidates are the savings pair (v74) < the login + calculator pair (v75) < the networth + drill-down pair (v76) < the dashboard pair (v77) < the mobile 390 twins (v78) < the items pair (v79). The v77 target-selection lesson applied: the queue suggestion verified against the ledger before commitment — no correction needed (the third consecutive agreement). This is the pair's THIRD re-run (v58 → v65 → v74 → v80); the pair re-proves the v58 DATA-CONDITIONAL footer chips and the v54 badge internals six iterations after their last measurement, and the v70b wrap/stretch arithmetic on the savings view's own two-card row.

## The v80 sweep — what the measurement found

### F0 [BASELINE] — fully GREEN as-shipped (no code defect)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (`npm run build` — the v76 static-copy lesson holds; robots + sitemap prerendered; the standalone static + public copies verified present) · **282 e2e ✓** (101 + 122 + 61 chunk executions = 282 unique tests in 24 files [281 chromium + 1 setup, the setup re-run per chunk as the project dependency] — the exact documented v79 state) · 35/35 smoke ✓. The workspace was RESET before this session (the fresh clone): node_modules reinstalled, chromium-1243 reinstalled, `.env` rewritten (DATABASE_URL="file:../db/custom.db", db/ at the repo root), `db:push` + `db:seed` re-run, the seedcheck confirming the exact seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 4.15, no 5.x); npm-latest `axe-core` = 4.14.0 (only a canary prerelease beyond). The lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0 — no nested engine dir under `node_modules/@axe-core/playwright/`). The engine-contract pin executed GREEN standalone (2 passed). Only a 5.x wrapper (or a nested-engine change) changes the calculus; the next re-check point unchanged.

### F2 [STANDING] — the 74th standing checks: ALL GREEN

ref-standing-v74.sh + standing-checks-v74.sh (version-bumped from v73 — version-bump-only diffs verified). Reference side: the four bugs ALL still live (the toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 74th consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED WORKING (the 74th consecutive time: `hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

### F3 [PAIR] — the v58-era savings pair's third re-run (the savings view at desktop 1280x800, full-page, last re-shot v74): every flag DOM-arbitrated to a documented class — NO NEW GAP

vlm-shots-v80.sh + clone-vlmshots-v80.sh + vlm-compare-v80.mjs (login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference — the v46 rule holds). The verdict DIFFERENT with every flag a documented class (matching the v74 re-run's own flag set exactly):

- The card grid layout (the reference's single card vs the clone's two) — the seed-count data class.
- The card footer's account-type chips ("Brokerage"/"Bank Account" + icon on the clone; the date alone on the reference) — the v58 DATA-CONDITIONAL class (the reference's own savings item carries NO paymentMethod; the same two-child structure its own income card renders).
- The badge family ("need" red vs "savings" green; the clone's extra "Recurring") — the classification-VALUE + Recurring superset data classes.
- The subtitle figures ("1 items · $1000.00" vs "2 items · $1250.00") — the seed-data class.
- The avatar letter ("U" vs "D") — the user-identity class.

The both-sides DOM census (arbit-v80.sh — the v75 convention: the census runs regardless of the verdict; the v74 census axes re-measured PLUS the v80 titleRow geometry):

- **The HEADER BYTE-IDENTICAL** (the h1 "ZeroBalance" 20px/700/rgb(26,58,46)).
- **The GRID + CARD chrome BYTE-IDENTICAL** (grid w 960 / gap 16px / the 3-col ~309px template; card w 309 / pad 20px / radius 12px / border 1px solid rgb(229,231,227) / bg rgb(255,255,255)); the childCount (1 vs 2) the seed-count class; the card h (ref 200 vs clone 230) the v70b-decomposed class (the Recurring superset badge's wrap h 52 [22+8+22] → +30px, and the 1-row grid STRETCHES the shorter sibling to the taller card's natural height — the clone's live heights measured [230, 230], alignItems "normal" [the grid default = stretch]).
- **The TITLE ROW BYTE-IDENTICAL — the v80 never-census'd axis** (display flex / gap 8px / alignItems center / row h 24 / the dot 8×8 / radius 9999px / dotBg rgb(59,126,161) — the savings blue on BOTH sides; the 1280 state of the v51/v54 390-only family).
- **The INTERIOR TEXT BYTE-IDENTICAL** (the h4 16px/600/lh 24px/rgb(26,58,46); the amount 24px/700/lh 32px/rgb(59,126,161) — the savings blue accent).
- **The FOOTER + BADGE chrome BYTE-IDENTICAL** (flex/space-between/12px/rgb(107,114,128)/h 16 with the 12×12 icons; the badge row flex/wrap/8px/mb 12px; every badge radius 6px/pad 2px 10px/fs 12px/fw 600/h 22); the footer childCount (1 vs 2) the v58 DATA-CONDITIONAL class; the badgeRow h (22 vs 52) + the badge texts/colors the v57 wrap + classification-VALUE data classes.
- **The docSW 1280 guard on both sides.**

**NO NEW GAP — the v80 iteration is PIN-ONLY.**

### F4 [PIN] — the savings goal-card's double-wrap heights + title-row geometry + border/bg census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 283)

The never-pinned axes (the existing pins cover around them: the v58 pin asserts the savings grid + the FIRST card's w/pad/radius + the footer + the badge chrome but never the card HEIGHT; the v45 F1a pin holds the INCOME card's border/bg/titleRow (the lime-dot twin) — the savings view's own border/bg + blue-dot titleRow state at 1280 never pinned [the v51/v54 pins hold the 390 family only]; the v74 pin holds the h4/amount/hidden-h1 — no heights):

- **The savings view's CARD HEIGHTS [230, 230] at 1280 — the DOUBLE-WRAP twins** (the v80 live-grid probe's own measured values, childCount 2 / heights [230, 230] / alignItems "normal"): BOTH savings cards are wrap-governed naturals (each carries 4 badges wrapping its row to 52px — the v70b arithmetic's savings-view guard: a broken wrap on EITHER card flips the pin). **The v80 probe CORRECTED the v70b attribution**: the stretch axis lives on the INCOME view (the Salary card, natural 200 with its 3 badges, STRETCHED to the Freelance card's natural wrap 230 — the v79 pin's income heights[0] has pinned the STRETCH twin all along, its comment's wrap/stretch attribution inverted between the two siblings; the probe's items-start experiment measured the income view's naturals at [200, 230] — proving Salary is the stretched one) while the savings view's two cards are BOTH natural wrap twins. The v80 pin asserts the savings view's own [230, 230] — the view's height arithmetic pinned for the first time.
- **The TITLE ROW's geometry at 1280** (the 1280 state of the v51/v54 390-only family, measured byte-identical on both sides by the v80 census): display flex / gap 8px / alignItems center / row h 24 / the dot 8×8 / radius 9999px / dotBg rgb(59,126,161) — the savings blue (the v45 F1a pin's income lime-dot twin completed to the savings type).
- **The CARD's border + bg at 1280** (the v45 F1a pin's income-card family's savings twin): border "1px solid rgb(229, 231, 227)" / bg "rgb(255, 255, 255)".
- The docSW 1280 guard.

The pin asserts the arbitration's own measured values, byte-identical on both sides' savings views at 1280x800.

**The pin-sanity mutation**: the titleRow's `lg:items-start` (item-card.tsx:119 — `mb-1 flex items-center gap-2` + ` lg:items-start`) — flips EXACTLY the titleRow.alignItems axis at 1280 ("center" → "flex-start") and nothing else (the mutation is viewport-scoped: at 390 the lg: variant is inert — the v54 hdrRow pin [alignItems "center" at 390] stays GREEN; the v45 F1a pin asserts the income titleRow's gap/dotW/dotBg/font/weight — NO alignItems — GREEN; the row's height is content-governed (max of the dot 8 and the h4 box 24), alignment-independent — the v79 income heights[0] 230 and the v58 badgeRow h 52 stay GREEN; the v74 h4/amount pins untouched; the v51 F3 dot radius/bg at 390 untouched — cascade-free by construction, the shared-component per-view-completion reality dodged via the responsive variant) — then restored (the standalone REBUILD as a SEPARATE command).

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → build (`npm run build`) → **283 e2e** in chunks (+1) → 35 smoke; the 16 standing screenshots regenerated + byte-compared (the same-DB discipline; the seedcheck under `env -u DATABASE_URL`). EXPECTED: any DATE-class diff pixel-arbitrated per the v66/v75 discipline, never a VLM verdict.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the savings goal-card's double-wrap heights [230, 230] + the titleRow geometry (flex/8px/center/h 24/dot 8×8/9999px/rgb(59,126,161)) + the card's border/bg at 1280 + the docSW guard | tests/e2e/items.spec.ts |
| 2 | sanity | the pin-sanity mutation: the titleRow's ` lg:items-start` (item-card.tsx:119) → the pin FAILS at exactly the titleRow.alignItems axis ("center" → "flex-start"); restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/item-card.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 283 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v80 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (282→283 + the v80 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v80 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 115 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.37 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v80 section (the new probes + the ledger-verified queue note) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_190.md + the repo worklog Session 115 entry | docs/session_190.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v80.sh census's own measured values, byte-identical on both sides' savings views at 1280x800: the titleRow `{display: "flex", gap: "8px", alignItems: "center", h: 24, dotW: 8, dotH: 8, dotRadius: "9999px", dotBg: "rgb(59, 126, 161)"}`; the card `{border: "1px solid rgb(229, 231, 227)", bg: "rgb(255, 255, 255)"}`; the card heights [230, 230] (the live clone grid probe: childCount 2, heights [230, 230], alignItems "normal"); the docSW 1280.
- **The v80 probe's attribution correction** (the items-start experiment): under the grid's items-start, the income view measures [200, 230] — the Salary card's natural is 200 (3 badges, row 22) and the Freelance card's natural is 230 (4 badges, row 52): the INCOME view's FIRST card is the stretched sibling (the v79 pin's heights[0] 230 = the STRETCH twin — its comment's wrap/stretch attribution inverted between the siblings; the pin's VALUE and its dual guard [a broken wrap OR a broken stretch both flip it] remain exactly right). The savings view's [230, 230] are BOTH natural wrap twins (each card 4 badges, row 52) — no stretch on the savings view (the two naturals happen to be equal).
- The source confirms the values: the titleRow `mb-1 flex items-center gap-2` + the dot `h-2 w-2 rounded-[9999px]` + `backgroundColor: accent` + the h4 `font-semibold` (item-card.tsx:119-124 — the savings accent = TYPE_COLORS.savings = rgb(59,126,161)); the grid `grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3` (items-view.tsx:262 — no items-* class: the default stretch); the card `rounded-xl border bg-white p-5 shadow-sm` family (item-card.tsx — the 1px solid rgb(229,231,227) border + the white bg, the v45-measured twins).
- The pin-sanity target: the titleRow's ` lg:items-start` flips ONLY the titleRow.alignItems axis at 1280 ("center" → "flex-start") — the v80 pin's own headline axis; viewport-scoped so the 390 family (v51/v54) is untouched; the v45 F1a income-1280 pin asserts no alignItems; the row height is alignment-independent (content-governed) so the v79/v58 height pins stay GREEN; grep-verified: no other spec asserts the titleRow's alignItems at 1280.
- The existing pins are SAFE: the v58 pin's savings first-card {w, pad, radius} + footer + badges (disjoint from h/titleRow-border-bg — the v80 pin adds, never duplicates); the v74 pin's h4/amount/hidden-h1 (disjoint); the v65 pin's page-header row (a disjoint surface); the v38 S2 pin's filter card (disjoint); the v51/v54 pins hold the 390 family (a different viewport); the v45 F1a pin holds the INCOME view's twins (a different view — the v80 pin is the savings view's own state, the per-view coverage the v79 pin's accent-completion pattern established).
- The blast radius: ZERO production-code change (every census delta a documented class — the pin-only line holds); the pin-sanity mutation touches `src/components/budget/item-card.tsx:119` (the titleRow's className) REVERTED before ship (`git diff src/` = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` → 282 e2e (**283** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser run; the with-server boots fresh per command; the reference session EXPIRES between long eval gaps — the login-retry loop handles it; the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` + kill before every full-chain run (the v53 orphaned-webServer lesson); one-shot Prisma scripts need `env -u DATABASE_URL`; no dollar sequences in census JS inside double-quoted bash strings (the v64 rule); no attribute-value selectors in the census (the v78 rule — geometry + text-content filters only); the QUOTED heredoc with the env-injected census (the v73 lesson); the mutations need the standalone REBUILD as a SEPARATE command (the v53 lesson); the clean-check gate re-runs AFTER every new file lands (the v69 lesson); the build step is `npm run build` (the v76 F0 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of bounds under the v46 read-only rule): the reference-side verify-email panel census, the forgot-confirm state census, the calculator EMPTY-state reference census, the line-items dialog glyphs.
- The v81 queue (suggestions): (1) the re-run cadence rotates to the next-oldest candidate after this pair (the v59-era login + calculator pair [the login view + the calculator dialog at 1280], last re-shot v75 — now the oldest remaining [v75 < v76 < v77 < v78 < v79 < v80]), (2) the axe-core watch at its next re-check point (only a 5.x wrapper changes the calculus), (3) the deferred reference-write censuses (unchanged).
