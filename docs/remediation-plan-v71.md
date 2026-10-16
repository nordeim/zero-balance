# Remediation Plan v71 — the NEW-pair program opens (the items views' mobile 390 full-page pairs — income + expenses + savings, the below-the-fold surfaces never individually shot) + the axe-core watch at its re-check point + the item-card SUBTITLE-P conditional-render fix (THE FIX — the first production-code change since v61)

Date: 2026-10-17 · Scope: the session-170/171 v71 queue — item #1 "the NEW-pair program opens (the below-the-fold 390 surfaces — the items views' mobile twins never individually shot, the v62/v63 precedent extending the standing-pair matrix to the remaining views)" and item #2 "the axe-core watch continues at its next re-check point (only a 5.x wrapper changes the calculus — the engine-contract pin guards the gate's toolchain)" and item #3 "the deferred reference-write censuses (unchanged, blocked by the v46 read-only rule)" — plus the 65th standing checks. Measured live via the v71 family: `vlm-shots-v71.sh` + `clone-vlmshots-v71.sh` + `vlm-compare-v71.mjs` (all three items pairs) + `arbit-v71.sh` (the flags' DOM arbitration + the subtitle-P discovery census) + `ref-standing-v65.sh` + `standing-checks-v65.sh` (the 65th round, version-bumped from v64).

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · 272 e2e ✓ (95 + 69 + 107 chunk runs = 271 chromium + 3 setups, 272 by the --list convention — the exact documented v70 state) · 35/35 smoke ✓. **No F0 finding this run** — the committed v70 tree passes the full gate chain as-shipped.

## The v71 sweep — what the measurement found

### F1 [WATCH] — the axe-core watch at its re-check point: NO DRIFT

The registry state: npm-latest `@axe-core/playwright` = **4.14.0** (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 4.15); npm-latest `axe-core` = **4.14.0** (no 5.x engine exists). The lockfile holds the v68 dedupe state: the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0 (the wrapper's `require.resolve('axe-core')` → `node_modules/axe-core/axe.js`, no nested dir — verified live). The engine-contract pin (the v68 a11y.spec.ts tail) executed GREEN in the baseline chain. **NO DRIFT — the 4.x story stays closed; only a 5.x wrapper (or a nested-engine change) changes the calculus. The next re-check point unchanged.**

### F2 [STANDING] — the 65th standing checks: ALL GREEN

- **Reference side** (`ref-standing-v65.sh`): the four bugs ALL still live — the toast-blocker (`hitIsBurgerChild:false`, the burger's center hit intercepted by `DIV.fixed top-0 z-[100]`), the sheet-trap (the overlay remains after the nav click, `overlayCount:1`), the no-landmark (`navLandmark:false`), the 464px `/networth` overflow at 390 (`docSW:464`). The data census UNCHANGED (the 65th consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses). The SEO pair live.
- **Clone side** (`standing-checks-v65.sh`): R1 the burger hit-test TRUE + the sheet opens · R2 the sheet CLOSES + navigates (`sheetGone:true, overlayGone:true` on /income) · R3 the nav landmark present · R4 ZERO overflow at 390 on all five views (docSW 390 each) · the SEO pair live. **The mobile navigation menu VERIFIED WORKING — the 65th consecutive time.**

### F3 [PAIR] — the NEW-pair program: the items views' mobile 390 full-page pairs (income + expenses + savings): ONE REAL GAP FOUND

The below-the-fold 390 surfaces never individually shot (the v62/v63 precedent extending the standing-pair matrix). Both sides captured via `vlm-shots-v71.sh` + `clone-vlmshots-v71.sh` (login on the first attempt both sides, the parked pointer at (5,5)), compared via `vlm-compare-v71.mjs`, every flag DOM-arbitrated via `arbit-v71.sh` (the card-internals census on BOTH sides at 390).

**PAIR 1 (income): VERDICT IDENTICAL** — zero layout/style flags; every difference the expected data class (the seed's 2 cards vs the reference's 1; the Recurring badge wrap; the payment-method footer child the reference's own income card also renders; the avatar "U" vs "D"). **CLEAN.**

**PAIR 2 (expenses): VERDICT DIFFERENT with three style flags, every one arbitrated:** (1) the card footer layout — the footer CHROME byte-identical (flex/space-between/12px/rgb(107,114,128)/h 16; every child span flex gap 4px with the 12×12 gray icon); the childCount 1-vs-2 is the reference's own data (its expense items carry no paymentMethod values → date-only footers) = the **v57 DATA-CONDITIONAL class**; (2) the badge wrapping — the badge CHROME byte-identical (flex/wrap/gap 8px/mb 12px/2px 10px/12px/600/h 22); the clone's 4th Recurring superset badge wraps the row to h 52 = the **v57 wrap class**; (3) the floating "Edit with Base44" element = **platform chrome** (excluded by rule, never arbitrated).

**PAIR 3 (savings): VERDICT DIFFERENT with the style flags, every one arbitrated:** (1) the card footer content = the **v57/v58 DATA-CONDITIONAL class** (the same chrome census as PAIR 2); (2) the badge arrangement = the **v57 wrap class** (the same arithmetic); (3) the badge styling — the reference's savings item is classified "need" (the red family: bg rgb(254,242,242)/color rgb(185,28,28)) while the clone's are "savings" (the green family) = the **v58 classification-VALUE data class** (the color maps byte-identical per classification — the reference's own Investments expense card carries the "savings" badge with EXACTLY the clone's values: bg rgb(240,253,244)/color rgb(21,128,61)/border rgb(187,247,208); the maps are locked by badge-colors.spec.ts); (4) the "active badge padding different" claim — the active badge measures BYTE-IDENTICAL on every card on BOTH sides (h 22/w 63/pad "2px 10px"/radius 6px/fs 12px/fw 600/bg rgb(248,250,252)/color rgb(51,65,85)/border transparent) = a **PERCEPTION ARTIFACT**.

**THE REAL GAP (the v71 discovery — the first production-code parity gap since v61):** the arbitration's card-internals census measured the SUBTITLE P's presence per card — the reference's Miscellaneous and Investments expense cards (EMPTY subcategory) render `subtitleP: {present:false}` with titleRow h **28** and card h **180** (the arithmetic: pad 20 + titleRow 28 + mb 12 + amount 32 + mb 16 + badge 22 + mb 12 + footer 16 + pad 20 + border 2 = 180), while its Netflix/Rent cards (WITH subcategory) render the P (h 20, fs 14px, lh 20px, color rgb(107,114,128)) with titleRow h 48 and card h 200 — **the reference CONDITIONALLY RENDERS the subtitle P on the non-empty value**. The clone's `item-card.tsx:127` renders `{item.subcategory ?? ""}` UNCONDITIONALLY — a user-created item with an empty subcategory renders a 20px EMPTY BLOCK (titleRow 48, card +20px) the reference never renders. The details sheet already carries the conditional idiom (the v52 fix: `{item.subcategory ? (<p>…</p>) : null}` — the dialog's own optional-field idiom); the item-card is the one site that never got it. The clone's dev seed carries no empty-subcategory items (all 7 seeded items have subcategories), which is why every prior census (which pins seeded cards) passed — the gap lives in the UNSHIPPED state space (user-created empty-subcategory items), exactly the class the NEW-pair program's richer flag surfaces expose.

### F4 [FIX] — the item-card subtitle-P conditional render (THE production-code change)

The fix mirrors the reference's measured contract and the v52 details-sheet idiom — `src/components/budget/item-card.tsx`:

```tsx
{item.subcategory ? (
  <p className="text-sm" style={{ color: rgb.gray }}>
    {item.subcategory}
  </p>
) : null}
```

TDD: the F4 REGRESSION test (a user-created no-subcategory expense card renders NO subtitle P, titleRow 28, card h 180 at 390 in the 1-col grid — the reference's own no-subtitle geometry) runs RED on the unfixed build, GREEN after; the F5 PIN (the seeded WITH-subtitle card's subtitle-P chrome — h 20/fs 14px/lh 20px/color, titleRow 48, titleRowMb 12) pins the other side of the conditional so the fix can't regress the with-subtitle state (GREEN before AND after). The pin-sanity mutation check (the reverted conditional → the F4 test fails) proves the regression net bites.

### F5 [VERIFY] — the screenshots + the full chain re-run

The 16 screenshots regenerated against the seed and byte-compared against the committed set (any DATE-class diff pixel-arbitrated via the v66 PIL-diff method). The full gate chain re-run on the fixed tree: lint → typecheck → 108 unit → build → 274 e2e in 3 chunks → 35 smoke.

## ToDo

| # | type | item | file |
|---|------|------|------|
| 1 | test | F4 regression: create an empty-subcategory expense → the card renders NO subtitle P, titleRow 28, card h 180 at 390 (RED first) | tests/e2e/items.spec.ts |
| 2 | test | F5 pin: the seeded Rent card's WITH-subtitle geometry (subtitle-P chrome + titleRow 48 + titleRowMb 12) | tests/e2e/items.spec.ts |
| 3 | fix | the subtitle-P conditional render (the v52 details-sheet idiom) | src/components/budget/item-card.tsx |
| 4 | sanity | the pin-sanity mutation: revert the conditional → F4 must FAIL; re-apply → GREEN (each with the standalone REBUILD as a SEPARATE command) | src/components/budget/item-card.tsx |
| 5 | verify | the full chain re-run (lint → typecheck → 108 unit → build → 274 e2e in chunks → 35 smoke) | — |
| 6 | verify | the 16 screenshots regenerated + byte-compared | docs/screenshots/ |
| 7 | docs | D1: AGENTS.md v71 paragraph | AGENTS.md |
| 8 | docs | D2: CLAUDE.md state bump (the E2E count 272→274 + the v71 fix entry) | CLAUDE.md |
| 9 | docs | D3: README state + the v71 plan-table row | README.md |
| 10 | docs | D4: SKILL doc Session 106 audit row + the state line | zero-balance_SKILL.md |
| 11 | docs | D5: PAD revision block v1.1.28 | Project_Architecture_Document.md |
| 12 | docs | D6: the probe README's v71 section (the new probes + the v71 lessons) | scripts/parity-probes/README.md |
| 13 | docs | D7: session_171.md + the repo worklog Session 105 entry | docs/session_171.md + worklog.md |
| 14 | ship | the full chain re-run + commit + SSH-wrapper push (the explicit --remote flag — the v70 lesson) | — |

## Pre-execution validation (done before the plan's execution)

- The F4 fix's mechanism verified live: `arbit-v71.sh` ran the exact census the F4 test's page.evaluate carries (the h4 → the title row → the flex-1 block → the P child) on BOTH sides — the no-subtitle geometry (titleRow 28, card 180) is the reference's OWN measured value, not a derived guess; the with-subtitle geometry (titleRow 48, P h 20/fs 14px/lh 20px/color rgb(107,114,128)) measured on both sides' seeded cards byte-identical.
- The F4 test's fixture mechanics: the Add Expense flow (the v52 F3/v70 family's documented dialog contract — Amount + Category fills, the defaults need/monthly/active = 3 badges, recurring OFF) creates the probe card; the cleanup rides the expense card's Edit dialog → Delete → the inline "Delete this item?" confirm (the superset delete path, the documented flow — expense cards carry NO kebab); the header count restores to "3 items · $2235.00".
- The F4 test runs at the 390 viewport (setViewportSize + goto, the v52 F3 pattern): the 1-col grid gives the probe card its NATURAL height (the grid STRETCH governs only same-row siblings — the v67/v70 lesson; at 390 every card is its own row).
- The F5 pin is read-only: it rides the seeded Rent card (subtitle "Apartment") — no fixture flow, no restore.
- The existing pins are SAFE: no existing test asserts the subtitle P on an empty-subcategory card (the seed has none); the v52 F2/F3 mobile censuses pin seeded WITH-subtitle cards (unchanged by the fix); the v57/v58 footer + badge censuses are subcategory-independent; the item-details v52 pin already asserts its OWN conditional.
- The fix's blast radius: `item-card.tsx:127` is the ONLY unconditional subcategory render site in a visual surface (the details sheet since v52 conditional; the drill-down's "Other" literal is its own documented mapping; the search haystack's `?? ""` is a string concat, not a render).
- The chain gate: lint → typecheck → 108 unit → build → 272 e2e (**274** after: +2 — the F4 regression + the F5 pin) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every agent-browser run; the with-server boots fresh per command; the reference session EXPIRES between long eval gaps — the login-retry loop handles it; the e2e chunks pass FULL file paths; `ss -tlnp | grep :3100` + kill before every full-chain run (the v53 orphaned-webServer lesson); one-shot Prisma scripts need `env -u DATABASE_URL` (the sandbox's inherited parent-workspace URL is the documented pollution); no dollar sequences in census JS inside double-quoted bash strings (the v64 rule); no attribute-value selectors in single-quoted eval strings (the v60/v67 rule — geometry + text-content filters instead); the mutations need the standalone REBUILD as a SEPARATE command (the v53 lesson).
- The deferred queue (unchanged, all need reference WRITES — out of bounds under the v46 read-only rule): the reference-side verify-email panel census, the forgot-confirm state census, the calculator EMPTY-state reference census, the line-items dialog glyphs.
- The v72 queue (suggestions): (1) the NEW-pair program continues (the remaining below-the-fold 390 surfaces: the drill-down EXPANDED mobile twin, the details-sheet mobile twin) or the re-run cadence's second cycle (the v58-era savings pair, last re-shot v65), (2) the axe-core watch continues at its next re-check point (only a 5.x wrapper changes the calculus), (3) the deferred reference-write censuses (unchanged).
