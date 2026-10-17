# Remediation Plan v74 — the re-run cycle's OLDEST candidate (the v58-era savings pair's second re-run — the only pre-v70 pair not re-shot since v65) + the axe watch (NO DRIFT) + the savings goal-card's interior-text chrome + the hidden app-shell h1 pin (PIN-ONLY)

The session's plan, validated against the codebase before execution. The formal narrative ships in `docs/session_178.md`; the repo worklog entry: Session 108.

## The v74 sweep — what the measurement found

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 4.15, no 5.x); npm-latest `axe-core` = 4.14.0 (only a canary prerelease beyond). The lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0, verified live via the lockfile's packages tree; no nested engine dir). The engine-contract pin executed GREEN standalone (2 passed). Only a 5.x wrapper (or a nested-engine change) changes the calculus; the next re-check point unchanged.

### F2 [STANDING] — the 68th standing checks: ALL GREEN

ref-standing-v68.sh + standing-checks-v68.sh (version-bumped from v67 — version-bump-only diffs verified). Reference side: the four bugs ALL still live (the toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 68th consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED WORKING (the 68th consecutive time), zero overflow at 390 on all five views, the SEO pair live.

### F3 [PAIR] — the re-run cycle's OLDEST candidate: the v58-era savings pair's fresh sweep (the second re-run — the v65 shots predate the v70-era pins) — NO NEW GAP, every flag DOM-arbitrated

vlm-shots-v74.sh + clone-vlmshots-v74.sh + vlm-compare-v74.mjs (login on the first attempt both sides; the parked pointer at (5,5); read-only both sides — the v46 rule). The VLM verdict DIFFERENT with two layout/style flags + the expected data/avatar classes, every one DOM-arbitrated via arbit-v74.sh (the both-sides /savings census at 1280):

- **The "Card Grid Alignment" flag (the reference's single card vs the clone's two "in a 2-column grid") = the SEED-DATA class + BYTE-IDENTICAL grid chrome** — the grid `display:grid`, the template `309.328px 309.328px 309.328px` (ref) vs `309.328px 309.328px 309.344px` (clone — the last track's 0.016px sub-pixel distribution with 2 children vs 1, both matching the v58-documented ≈309.33px tracks), the gap 16px, the w 960 — identical; the childCount 1-vs-2 is the reference's own 1-item seed vs the clone's 2-item dev seed (the documented v58 class). Two cards in a 3-column grid occupy two columns — the count, not the chrome.
- **The "Card Footer Content" flag (the clone's account-type label + icon, absent on the reference) = the v58 DATA-CONDITIONAL footer class re-verified live** — the footer row's chrome byte-identical (flex justify-between, fs 12px, color rgb(107,114,128), h 16); the reference's own savings item carries NO paymentMethod so its footer renders ONE child (the date + the 12×12 gray calendar icon), the clone's carry paymentMethods so the footer renders the SAME two-child structure (the date + the "Brokerage" chip with the 12×12 gray icon) — the v57 conditional-footer contract, every child's chrome byte-identical (flex gap 4px, 12px, gray, iconW/H 12, iconColor gray). A NEW micro-observation: the reference's footer children are DIVs, the clone's are SPANs — a DOM-shape divergence of the v72 structural-class family ("the DOM shapes differ, the rendered chrome does not").
- **The badge family** — the classification VALUE is the data class (the reference's "need" red family: bg rgb(254,242,242), border rgb(254,202,202), color rgb(185,28,28) vs the clone's "savings" green family: bg rgb(240,253,244), border rgb(187,247,208), color rgb(21,128,61) — the color maps locked by badge-colors.spec.ts); the badge-row chrome byte-identical (flex wrap, 8px gap, 12px mb); the "monthly" (purple) + "active" (slate) badges byte-identical on both sides; the clone's 4th "Recurring" superset badge wraps the row to h 52 (22 + 8 + 22 — the documented v57 wrap arithmetic; the reference's 3-badge row stays h 22); every badge's geometry byte-identical (6px radius, 2px 10px pad, 12px/600, h 22, the 12×12 icons).
- **The card + interior-text chrome** — the card 309/20px pad/12px radius/1px solid rgb(229,231,227)/white byte-identical; the h4 title 16px/600/lh 24px/rgb(26,58,46); the amount 24px/700/lh 32px/rgb(59,126,161) — byte-identical. The card heights 200 (ref) vs 230 (clone) decompose through the badge-wrap arithmetic (the +30 = the wrapped row's 52 vs 22).
- **The hidden first-in-DOM h1 "ZeroBalance"** — the app-shell mobile header's h1 (display:none at 1280), computed chrome byte-identical both sides (20px/700/rgb(26,58,46)) — the v65-documented SEO surface, measured live for the first time since.
- The docSW 1280 both sides (zero overflow); the seedcheck confirms the exact seed state (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities).

### F4 [PIN] — the savings goal-card's interior-text chrome + the hidden app-shell h1 census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 277)

The never-pinned axes (the existing pins: the v58 F1 pin covers the savings grid + footer + badge-row GEOMETRY at 1280; the v51 F3 pin covers the title/amount chrome at 390 ONLY; the v65 F3 pin covers the VISIBLE header row at 1280; badge-colors.spec.ts locks the classification color maps; the hidden h1 is documented in the v65 notes but pinned nowhere):

- the savings goal-card's h4 TITLE chrome at 1280: fs 16px / fw 600 / lh 24px / color rgb(26, 58, 46) (the 390 pin covers fs/fw/color; the lh + the 1280 state never pinned);
- the savings goal-card's AMOUNT chrome at 1280: fs 24px / fw 700 / lh 32px / color rgb(59, 126, 161) (same — the lh + the 1280 state never pinned);
- the HIDDEN first-in-DOM h1 "ZeroBalance" (the app-shell mobile topbar's h1 — `src/components/budget/sidebar.tsx:234`, `text-xl font-bold`, inside the `md:hidden` header): computed chrome fs 20px / fw 700 / color rgb(26, 58, 46) + the ZERO-SIZE hiding mechanism (the header's `md:hidden` puts the subtree out of layout at ≥768px — the h1 keeps its OWN display (block) but renders w 0 / h 0, the v65 note's "hidden zero-size") — the v65-documented surface, byte-identical on both sides, pinned for the first time;
- the docSW 1280 no-overflow guard on the same surface.

The pin rides no fixture (the logged-in storageState, the seeded Investments card — the v58 pin's own style) and asserts the arbit-v74.sh census's own measured values, byte-identical on both sides' savings views at 1280.

### F5 [VERIFY] — the full chain re-run + the screenshots

lint → typecheck → 108 unit → build → **277 e2e** in chunks (+1) → 35 smoke; the 16 standing screenshots regenerated + byte-compared (the same-DB discipline; the seedcheck under `env -u DATABASE_URL`).

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 pin: the savings goal-card's interior-text chrome (h4 title + amount, the lh family at 1280) + the hidden app-shell h1 census at 1280 (the arbitration's own measured values) | tests/e2e/items.spec.ts |
| 2 | sanity | the pin-sanity mutation: the amount's `text-2xl` → `text-xl` (or the h1's `text-xl` → `text-2xl`) → the pin FAILS at exactly that axis; restored → GREEN (the standalone REBUILD as a SEPARATE command) | src/components/budget/item-card.tsx (mutation only, then reverted) |
| 3 | verify | the full chain re-run (lint → typecheck → 108 unit → build → 277 e2e in chunks → 35 smoke) | — |
| 4 | verify | the 16 screenshots regenerated + byte-compared | docs/screenshots/ |
| 5 | docs | D1: AGENTS.md v74 paragraph | AGENTS.md |
| 6 | docs | D2: CLAUDE.md state bump (276→277 + the v74 entry) | CLAUDE.md |
| 7 | docs | D3: README state + the v74 plan-table row | README.md |
| 8 | docs | D4: SKILL doc Session 109 audit row + the state line | zero-balance_SKILL.md |
| 9 | docs | D5: PAD revision block v1.1.31 | Project_Architecture_Document.md |
| 10 | docs | D6: the probe README's v74 section (the new probes + the v74 lesson: the amount's dollar text matched by CLASS never text — the v64 dollar rule's census corollary) | scripts/parity-probes/README.md |
| 11 | docs | D7: session_178.md + the repo worklog Session 108 entry | docs/session_178.md + worklog.md |
| 12 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag) | — |

## Pre-execution validation (done before the plan's execution)

- The pin's expected values are the arbit-v74.sh census's own measured values, byte-identical on both sides' savings views at 1280: the h4 title (16px/600/lh 24px/rgb(26,58,46)), the amount (24px/700/lh 32px/rgb(59,126,161)), the hidden h1 (20px/700/rgb(26,58,46), text "ZeroBalance", first-in-DOM, ZERO-SIZE — w 0/h 0 with its own display "block" — the md:hidden-header mechanism verified live by the h1probe pre-pin probe).
- The existing pins are SAFE: the v58 F1 pin asserts the same grid/card/footer/badge axes (untouched by the new pin — the interior-text chrome is disjoint); the v51 390 pin rides the mobile viewport; the v65 header pin walks UP from the Add button (not the first-h1 query — no collision with the hidden-h1 census); badge-colors.spec.ts locks colors via its own chipProbe (no geometry overlap).
- The blast radius: ZERO production-code change (every flag arbitrated to a documented class or disproven — the pin-only line holds); the pin-sanity mutation touches `src/components/budget/item-card.tsx` (the amount's `text-2xl` class) REVERTED before ship (`git diff src/` = 0 lines at commit).
- The chain gate: lint → typecheck → 108 unit → build → 276 e2e (**277** after: +1 — the F4 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser run; the with-server boots fresh per command; the reference session EXPIRES between long eval gaps — the login-retry loop handles it; the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` + kill before every full-chain run (the v53 orphaned-webServer lesson); one-shot Prisma scripts need `env -u DATABASE_URL` (the sandbox's inherited parent-workspace URL is the documented pollution); no dollar sequences in census JS inside double-quoted bash strings (the v64 rule — the amount's dollar-prefixed textContent is matched by the `text-2xl` CLASS, never by text); no attribute-value selectors in single-quoted eval strings (the v60/v67 rule); the QUOTED heredoc with the env-injected census (the v73 lesson); the mutations need the standalone REBUILD as a SEPARATE command (the v53 lesson); the clean-check gate re-runs AFTER every new file lands (the v69 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of bounds under the v46 read-only rule): the reference-side verify-email panel census, the forgot-confirm state census, the calculator EMPTY-state reference census, the line-items dialog glyphs.
- The v75 queue (suggestions): (1) the re-run cadence rotates to the next-oldest candidate (the v59-era login pair, last re-shot v66 — or the v60-era networth pair, last re-shot v67; the full re-run ledger is in the probe README), (2) the axe-core watch at its next re-check point (only a 5.x wrapper changes the calculus), (3) the deferred reference-write censuses (unchanged).
