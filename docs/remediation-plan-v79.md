# Remediation Plan v79 — the re-run cycle's next-oldest candidate (the v57-era items pair's third re-run — last re-shot v70) + the axe watch (NO DRIFT) + the rail-avatar chrome + item-card amount-accent + wrap/stretch card-height pin (PIN-ONLY)

The session's plan, validated against the codebase before execution. The formal narrative ships in `docs/session_188.md`; the repo worklog entry: Session 114.

## The v79 target selection (the ledger-verified queue)

The v78 plan's v79 queue suggested the v57-era items pair (the income + expenses view pair at desktop 1280, last re-shot v70) — and the rotation ledger AGREES: by the cadence's own oldest-first rule (ordering by LAST RE-SHOT DATE), the remaining candidates are the items pair (v70) < the savings pair (v74) < the login + calculator pair (v75) < the networth + drill-down pair (v76) < the dashboard pair (v77) < the mobile 390 twins (v78). The v77 target-selection lesson applied: the queue suggestion verified against the ledger before commitment — no correction needed. This is the pair's THIRD re-run (v57 → v64 → v70 → v79), the cadence's most-re-verified desktop surface; the pair also re-proves the v57 DATA-CONDITIONAL footer chips and the v70b card-height decomposition (the Recurring superset wrap + the sibling stretch) nine iterations after their last measurement.

## The v79 sweep — what the measurement found

### F0 [BASELINE] — fully GREEN as-shipped (no code defect)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (`npm run build` — the v76 static-copy lesson holds; robots + sitemap prerendered; the standalone static + public copies verified present) · **281 e2e ✓** (100 + 106 + 77 chunks = 281 unique tests in 24 files — the exact documented v78 state) · 35/35 smoke ✓. The workspace survived the session boundary intact (no reset): `main @ 387efae` (v78 shipped + the session_187 transcript via git pull), node_modules + `.env` (DATABASE_URL="file:../db/custom.db", db/ at the repo root) + `db/custom.db` + chromium-1243 all verified, no orphaned servers, the seedcheck confirming the exact seed (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities) before any flow ran.

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 4.15, no 5.x); npm-latest `axe-core` = 4.14.0 (only a canary prerelease beyond). The lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0 — verified in the lockfile's packages tree; no nested engine dir under `node_modules/@axe-core/playwright/`). The engine-contract pin executed GREEN standalone (2 passed). Only a 5.x wrapper (or a nested-engine change) changes the calculus; the next re-check point unchanged.

### F2 [STANDING] — the 73rd standing checks: ALL GREEN

ref-standing-v73.sh + standing-checks-v73.sh (version-bumped from v72 — version-bump-only diffs verified). Reference side: the four bugs ALL still live (the toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 73rd consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses — the income leg re-read after a mid-script session expiry, the documented login-retry pattern) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED WORKING (the 73rd consecutive time: `hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

### F3 [PAIR] — the v57-era items pair's third re-run (the income + expenses view pair at desktop 1280x800, full-page, last re-shot v70): every flag DOM-arbitrated to a documented class — NO NEW GAP

vlm-shots-v79.sh + clone-vlmshots-v79.sh + vlm-compare-v79.mjs (login on the first attempt both sides; the parked pointer at (5,5); read-only on the reference — the v46 rule holds). Both verdicts DIFFERENT, every flag a documented class:

- **PAIR 1 (INCOME at 1280)**: the avatar letter "U" vs "D" — the user-identity class; the 1-card vs 2-card grid — the seed-count data class; the card figures — the seed-data class. Matching the v70 re-run's own flag set exactly.
- **PAIR 2 (EXPENSES at 1280)**: the card footer's payment-method chips (ref: date only on its first card) — the v57 DATA-CONDITIONAL class; the badge arrangement/height — the v57 Recurring superset wrap class; the avatar — the user-identity class (again). Matching the v70 re-run's own flag set exactly.

The both-sides DOM census (arbit-v79.sh — the v75 convention: the census runs regardless of the verdict; the v70 census axes re-measured on BOTH sides at 1280x800 on BOTH views, plus the v70b avatar finder):

- **The AVATAR chrome BYTE-IDENTICAL** (w 36 × h 36 / radius 9999px / fs 14px / fw 600 / color rgb(255,255,255) / bg rgb(143,188,63) — the identity text "U" vs "D" the only delta, the user-identity class).
- **The GRID + CARD chrome BYTE-IDENTICAL** (grid w 960 / gap 16px / the 3-col 309.328px template; card w 309 / pad 20px / radius 12px / border rgb(229,231,227)); the childCount (1 vs 2 income, 4 vs 3 expenses) the seed-count class; the card h (ref 200 vs clone 230) the v70b-decomposed class — the Recurring superset badge's wrap h 52 (22+8+22) → +30px, and the 1-row grid STRETCHES the shorter sibling to the taller card's natural height.
- **The TITLE ROW BYTE-IDENTICAL** (gap 8px / dot 8×8 / income dotBg rgb(143,188,63) + expenses dotBg rgb(224,122,59) on BOTH sides / font 16px / weight 600).
- **The AMOUNT leaf chrome BYTE-IDENTICAL** (fs 24px / fw 700 / lh 32px / h 32; the income accent rgb(143,188,63) + the expenses accent rgb(224,122,59) matching per type — the texts the seed-data class).
- **The FOOTER + BADGE chrome BYTE-IDENTICAL** (footer flex/space-between/12px/rgb(107,114,128)/h 16 with both children flex gap 4px icons 12×12; the badge row flex/wrap/8px gap/mb 12px; badge0 radius 6px/pad 2px 10px/fs 12px/fw 600/h 22); the footer childCount (1 vs 2) the v57 DATA-CONDITIONAL class (the payment-method chips); the badgeRow h (22 vs 52) + texts the v57 wrap/classification-VALUE data classes.
- **The FILTER CARD BYTE-IDENTICAL on BOTH variants** (the income variant: card 960×86/pad 24px/radius 16px/search 447×36 SPANNING/3 children/2 comboboxes 216×36 at 14px; the expenses variant: search 216×36 NOT spanning/4 children/3 comboboxes — the v64/v70 pins' own values, zero drift) + the header row + the docSW 1280 guard on both views.

**NO NEW GAP — the v79 iteration is PIN-ONLY.**

### F4 [PIN] — the rail-avatar chrome + the item-card amount-accent + wrap/stretch card-height census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 282)

The never-pinned axes (the existing pins cover around them: the v45 F1a pin asserts the income card's box/titleRow/kebab but never its HEIGHT; the v57 pins the footer + badge chrome; the v64/v70 pins the filter cards; the v65 pin the page-header row; the v74 pin the SAVINGS goal-card's amount variant only — the income/expenses accent variants + the amount's box h never pinned; the tokens.spec pin the avatar's RADIUS only, via a width-36 + class finder — the avatar's full chrome (w/h/fs/fw/color/bg) never pinned):

- **The AVATAR's full chrome** at 1280 (sidebar.tsx:120 — `h-9 w-9 rounded-[9999px] font-semibold text-sm text-white` + bg `var(--lime-green)`): w 36 / h 36 / radius 9999px / fs 14px / fw 600 / color rgb(255,255,255) / bg rgb(143,188,63);
- **The AMOUNT leaf's per-type accent family** at 1280 (item-card.tsx:161 — `text-2xl font-bold` + `style={{ color: accent }}`, accent = TYPE_COLORS[item.type]): fs 24px / fw 700 / lh 32px / h 32 with the INCOME accent rgb(143,188,63) (COLORS.limeGreen) and the EXPENSES accent rgb(224,122,59) (COLORS.orangeDark) — the v74 pin's savings twin (rgb(59,126,161)) completed to all three types;
- **The CARD HEIGHT at 1280 — the wrap/stretch arithmetic** (the v70b lesson's regression guard): the income view's first card h 230 (the Salary card's Recurring-wrap natural 230 + the 1-row grid stretching the Freelance sibling to match — if the grid stretch or the badge wrap ever breaks, the pin fails);
- the docSW 1280 guard on both views.

The pin asserts the arbitration's own measured values, byte-identical on both sides' items views at 1280x800.

**The pin-sanity mutation**: the avatar's `font-semibold` → `font-medium` (sidebar.tsx:120) — flips exactly the avatar's fw axis (600 → 500) and nothing else (the tokens.spec avatar pin asserts the RADIUS via a width-36 finder — the size untouched; the boot-failure pin asserts the shell's visibility only; no other pin asserts the avatar's text chrome — the mutation is cascade-free), then restored (the standalone REBUILD as a SEPARATE command).

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → build (`npm run build`) → **282 e2e** in chunks (+1) → 35 smoke; the 16 standing screenshots regenerated + byte-compared (the same-DB discipline; the seedcheck under `env -u DATABASE_URL`). EXPECTED: any DATE-class diff pixel-arbitrated per the v66/v75 discipline, never a VLM verdict.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the avatar chrome + the amount's per-type accents + the wrap/stretch card height at 1280 (the avatar's w/h/radius/fs/fw/color/bg; the amount's fs/fw/lh/h + the income lime + expenses orange accents; the income first card's h 230; the docSW guards — the arbitration's own measured values) | tests/e2e/items.spec.ts |
| 2 | sanity | the pin-sanity mutation: the avatar's `font-semibold` → `font-medium` (sidebar.tsx:120) → the pin FAILS at exactly the avatar.fw axis (600 → 500); restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/sidebar.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → `npm run build` → 282 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared (any DATE-class diff pixel-arbitrated) | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v79 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (281→282 + the v79 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v79 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 114 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.36 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v79 section (the new probes + the ledger-verified queue note) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_188.md + the repo worklog Session 114 entry | docs/session_188.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v79.sh census's own measured values, byte-identical on both sides' items views at 1280x800: the avatar `{w: 36, h: 36, radius: "9999px", fs: "14px", fw: "600", color: "rgb(255, 255, 255)", bg: "rgb(143, 188, 63)"}`; the income amount `{fs: "24px", fw: "700", color: "rgb(143, 188, 63)", lh: "32px", h: 32}`; the expenses amount `{color: "rgb(224, 122, 59)"}` (fs/fw/lh/h identical); the income first card `{h: 230}`; the docSW 1280.
- The source confirms the values: the avatar's `flex h-9 w-9 items-center justify-center rounded-[9999px] font-semibold text-sm text-white` + `backgroundColor: "var(--lime-green)"` (sidebar.tsx:120-122 — var(--lime-green) = rgb(143,188,63)); the amount's `text-2xl font-bold` + `style={{ color: accent }}` (item-card.tsx:161) with `TYPE_COLORS = { income: COLORS.limeGreen, savings: COLORS.blueMedium, expense: COLORS.orangeDark }` (constants.ts:92-96); the card's `p-5` + the badge row's `mb-3 flex flex-wrap gap-2` (the 230 = the wrap-governed row arithmetic + the sibling stretch).
- The pin-sanity target: the avatar's `font-semibold` → `font-medium` flips ONLY the avatar's fw (600 → 500) — the family's own headline axis; the tokens.spec avatar-radius pin's finder (width 36 + the rounded-[9999px] class) is size- and class-based, untouched by a font-weight change; the boot-failure shell-visibility pin untouched; no other pin asserts the avatar's text chrome (grep-verified: the only avatar assertions in tests/ are tokens.spec's radius + boot-failure's shell visibility).
- The existing pins are SAFE: the v45 F1a pin asserts the income card's w/pad/radius/border/boxShadow/bg/cursor/transition + the titleRow + the kebab (disjoint from h/avatar/amount); the v57 pins the footer + badge chrome (disjoint); the v64/v70 pins the filter cards (disjoint surfaces); the v65 pin the page-header row (disjoint); the v74 pin the savings amount variant (a different type accent — the v79 pin adds the income/expenses twins, not a duplicate); the v52/v71 mobile pins assert the 390 state (a different viewport); the amount finder (the ≥20px-font P inside the card) resolves to the same leaf the arbitration measured — the v76 finder-description lesson applied (the census dumps the leaf's text, and the pin's card finder is the exact grid-cols-3 walk the v45/v57/v74 pins use).
- The blast radius: ZERO production-code change (every census delta a documented class — the pin-only line holds); the pin-sanity mutation touches `src/components/budget/sidebar.tsx:120` (the avatar's className) REVERTED before ship (`git diff src/` = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → `npm run build` → 281 e2e (**282** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser run; the with-server boots fresh per command; the reference session EXPIRES between long eval gaps — the login-retry loop handles it (the F2 income-census expiry re-verified live this session); the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` + kill before every full-chain run (the v53 orphaned-webServer lesson); one-shot Prisma scripts need `env -u DATABASE_URL`; no dollar sequences in census JS inside double-quoted bash strings (the v64 rule); no attribute-value selectors in the census (the v78 rule — geometry + text-content filters only); the QUOTED heredoc with the env-injected census (the v73 lesson); the mutations need the standalone REBUILD as a SEPARATE command (the v53 lesson); the clean-check gate re-runs AFTER every new file lands (the v69 lesson); the build step is `npm run build` (the v76 F0 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of bounds under the v46 read-only rule): the reference-side verify-email panel census, the forgot-confirm state census, the calculator EMPTY-state reference census, the line-items dialog glyphs.
- The v80 queue (suggestions): (1) the re-run cadence rotates to the next-oldest candidate after this pair (the v58-era savings pair [the savings view + goal-card surfaces at desktop 1280], last re-shot v74 — now the oldest remaining [v74 < v75 < v76 < v77 < v78 < v79]), (2) the axe-core watch at its next re-check point (only a 5.x wrapper changes the calculus), (3) the deferred reference-write censuses (unchanged).
