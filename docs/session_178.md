# Session 178 — Parity iteration v74: the re-run cycle's OLDEST candidate (the v58-era savings pair's second re-run) + the savings goal-card's interior-text chrome + the hidden app-shell h1 pin (PIN-ONLY)

The v74 cycle — the session-177 queue's first item. With the NEW-pair program complete (v73 — every view + dialog + sheet surface carries both a desktop pair and a mobile-390 twin), the cadence rotates to the re-run cycle's OLDEST candidate: the v58-era savings pair, last re-shot v65, the only pre-v70 pair not re-run since. Plus the axe-core watch at its re-check point and the 68th standing checks. **PIN-ONLY for src/ — no production-code change; +1 e2e = 277.** The plan: `docs/remediation-plan-v74.md`.

## The environment (the workspace was reset)

Fresh clone from `main @ f5e03c6`, `.env` re-provisioned from the shipped `.env.example` (DATABASE_URL `file:../db/custom.db`, a fresh AUTH_SECRET), `db/` re-created via `db:push` + `db:seed` (7 budget items, 3 assets, 2 liabilities — the exact documented seed), `npm ci`, and `npx playwright install chromium` — the sandbox reset left an old chromium-1200 cache while the toolchain needs the 1243 build (the v73 session's same first-pass catch, pre-empted this time).

## F0 — the baseline chain FULLY GREEN as-shipped (no F0 finding)

lint ✓ · typecheck ✓ · 108/108 unit ✓ · build ✓ (robots.txt + sitemap.xml prerendered) · **276 e2e ✓** (69 + 92 + 118 chunks = 275 chromium + 3 setups — the exact documented v73 state) · 35/35 smoke ✓.

## F1 — the axe-core watch at its re-check point: NO DRIFT

npm-latest `@axe-core/playwright` = 4.14.0 (the dist-tags carry only 4.14.1 rc/next prereleases — no stable 4.14.1, no 5.x); npm-latest `axe-core` = 4.14.0 (only a canary beyond). The lockfile holds the v68 dedupe state (the wrapper 4.14.0 + ONE hoisted axe-core@4.14.0 — verified via the lockfile's packages tree; no nested engine dir). The engine-contract pin GREEN standalone (2 passed). Only a 5.x wrapper (or a nested-engine change) changes the calculus.

## F2 — the 68th standing checks: ALL GREEN

ref-standing-v68.sh + standing-checks-v68.sh (version-bumped from v67 — version-bump-only diffs verified against the convention). Reference side: the four bugs ALL still live (the toast-blocker `hitIsBurgerChild:false`; the sheet-trap `overlayCount:1`; the no-landmark `navLandmark:false`; the 464px /networth overflow at 390) + the data census UNCHANGED (the 68th consecutive clean drift check: "1 items · $25,000" networth / "1 items · $5000.00" income / "4 items · $525.00" expenses) + the SEO pair live. Clone side: R1–R4 ALL GREEN — the mobile navigation menu VERIFIED WORKING (the 68th consecutive time: `hitIsBurgerChild:true`, the sheet opens, closes on nav, the nav landmark present), zero overflow at 390 on all five views, the SEO pair live.

## F3 — the re-run pair: the savings view at desktop 1280x800 FULL-PAGE — NO NEW GAP, every flag DOM-arbitrated

vlm-shots-v74.sh + clone-vlmshots-v74.sh (login on the first attempt both sides; the parked pointer at (5,5); read-only both sides — the v46 rule holds). The VLM verdict **DIFFERENT** with two layout/style flags + the expected data/avatar classes:

- **The "Card Grid Alignment" flag** (the reference's single left-aligned card vs the clone's two "in a 2-column grid") — arbitrated via arbit-v74.sh to the **SEED-DATA class + BYTE-IDENTICAL grid chrome**: `display:grid`, the template `309.328px 309.328px 309.328px` (ref) vs `309.328px 309.328px 309.344px` (clone — the last track's 0.016px sub-pixel distribution with 2 children vs 1; both match the v58-documented ≈309.33px tracks), the gap 16px, the w 960 — identical; the childCount 1-vs-2 is the reference's own 1-item seed vs the clone's 2-item dev seed. Two cards in a 3-column grid occupy two columns — the count, not the chrome.
- **The "Card Footer Content" flag** (the clone's account-type label + icon, absent on the reference) — arbitrated to the **v58 DATA-CONDITIONAL footer class re-verified live**: the footer row's chrome byte-identical (flex justify-between, fs 12px, color rgb(107,114,128), h 16); the reference's own savings item carries NO paymentMethod so its footer renders ONE child (the date + the 12×12 gray calendar icon), the clone's carry paymentMethods so the footer renders the same two-child structure (the date + the "Brokerage" chip with the 12×12 gray icon) — the v57 conditional-footer contract; every child's chrome byte-identical (flex gap 4px, 12px, gray, iconW/H 12, iconColor gray). **A NEW micro-observation: the reference's footer children are DIVs, the clone's are SPANs** — a DOM-shape divergence of the v72 structural-class family ("the DOM shapes differ, the rendered chrome does not").
- **The badge family** — the classification VALUE is the data class (the reference's "need" red family: bg rgb(254,242,242), border rgb(254,202,202), color rgb(185,28,28) vs the clone's "savings" green family: bg rgb(240,253,244), border rgb(187,247,208), color rgb(21,128,61) — the maps locked by badge-colors.spec.ts); the badge-row chrome byte-identical (flex wrap, 8px gap, 12px mb); the "monthly" (purple) + "active" (slate) badges byte-identical on both sides; the clone's 4th "Recurring" superset badge wraps the row to h 52 (22 + 8 + 22 — the documented v57 wrap arithmetic; the reference's 3-badge row stays h 22); every badge's geometry byte-identical (6px radius, 2px 10px pad, 12px/600, h 22, the 12×12 icons).
- **The card + interior-text chrome** — the card 309/20px pad/12px radius/1px solid rgb(229,231,227)/white byte-identical; the h4 title 16px/600/lh 24px/rgb(26,58,46); the amount 24px/700/lh 32px/rgb(59,126,161) — byte-identical. The card heights 200 (ref) vs 230 (clone) decompose through the badge-wrap arithmetic (the +30 = the wrapped row's 52 vs 22).
- **The hidden first-in-DOM h1 "ZeroBalance"** — the app-shell mobile topbar's h1 (inside the `md:hidden` header), computed chrome byte-identical both sides (20px/700/rgb(26,58,46)) — the v65-documented SEO surface measured live again.
- The docSW 1280 both sides (zero overflow); the seedcheck confirms the exact seed state (7 items / rent 1850 / expenses 2235 / 0 line items / 3 assets / 2 liabilities).

**NO NEW GAP — the v74 iteration is PIN-ONLY.**

## F4 — the pin: the savings goal-card's interior-text chrome + the hidden app-shell h1 census at 1280 (+1 e2e = 277)

The never-pinned axes (the coverage map): the v58 F1 pin covers the savings grid + footer + badge-row GEOMETRY at 1280; the v51 F3 pin covers the title/amount chrome at 390 ONLY; the v65 F3 pin covers the VISIBLE header row at 1280; badge-colors.spec.ts locks the classification color maps; the hidden h1 is documented in the v65 notes but pinned nowhere. The pin (tests/e2e/items.spec.ts, read-only — the logged-in storageState, the seeded Investments card, the v58 pin's own style):

- the h4 TITLE chrome at 1280: fs 16px / fw 600 / **lh 24px** / color rgb(26, 58, 46);
- the AMOUNT chrome at 1280: fs 24px / fw 700 / **lh 32px** / color rgb(59, 126, 161);
- the HIDDEN first-in-DOM h1 "ZeroBalance": text "ZeroBalance", fs 20px / fw 700 / color rgb(26, 58, 46), rendered **ZERO-SIZE (w 0 / h 0, its own display "block")** — the `md:hidden`-header mechanism (the v65 note's "hidden zero-size");
- the docSW 1280 no-overflow guard.

**A pre-pin probe corrected the draft before the RED/GREEN cycle**: the pin's first draft asserted `display === "none"` for the hidden h1; the live h1probe (with-server + one eval) returned display "block" / w 0 / h 0 — an element inside a display:none SUBTREE keeps its OWN computed display while rendering zero-size boxes. The pin asserts w/h 0 instead.

The pin **GREEN on first run**. The pin-sanity mutation (the amount's `text-2xl` → `text-xl` in `src/components/budget/item-card.tsx`): the standalone REBUILD as a SEPARATE command → the pin **FAILS at exactly the cardAmount axis** (line 2612) → restored → rebuilt → GREEN. `git diff src/` = 0 lines — **PIN-ONLY holds.**

## F5 — the full chain re-run + the screenshots

lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ (robots + sitemap) · **277 e2e ✓** (69 + 92 + 118 chunks = 276 chromium + 3 setups) · 35/35 smoke ✓. The 16 standing screenshots regenerated + byte-compared: **16/16 BYTE-IDENTICAL** (the sixth consecutive fully-identical set). The seedcheck (under `env -u DATABASE_URL`): the exact seed state.

## The docs alignment

D1 AGENTS.md (the v74 paragraph), D2 CLAUDE.md (277 + the v74 pin clause), D3 README.md (the counts + the v74 plan-table row), D4 zero-balance_SKILL.md (Session 109 audit row + the state lines), D5 the PAD's v1.1.31 revision block (the title version left at the convention), D6 the probe README's v74 section (the probes + the three lessons), D7 this narrative + the worklog's Session 108 entry. The lint gate re-runs after every new file (the v69 lesson).

## The probe lessons

1. **The dollar-text census corollary (the v64 rule)**: the amount's dollar-prefixed textContent is matched by the `text-2xl` CLASS, never by text — a literal `$` inside a double-quoted bash census string expands against bash's own positional parameters (`$4` in a character class silently empties), so the class-based finder is the only safe detector.
2. **The md-hidden-subtree census**: an element inside a `display:none` subtree keeps its OWN computed display ("block" for an h1) while rendering zero-size boxes — assert w/h 0, never display "none", for md-hidden subtrees.
3. **A pre-pin probe beats a wrong assertion**: the live probe corrected the pin's draft assertion before the mutation check could validate a wrong axis — the mutation check only validates the axes you actually assert.

## The ship

The changeset reviewed clean (`src/` untouched — PIN-ONLY; no key material). The commit + the SSH-wrapper push per `docs/how-to-git-push-using-ssh-wrapper_SKILL.md` (the explicit `--remote` dry-run first, the operator key materialized 0600 and shredded after). **v74 complete: `main` remote-verified via the wrapper.**

## Suggested next (the v75 queue)

(1) The re-run cadence rotates to the next-oldest candidate — the v59-era login pair (last re-shot v66) or the v60-era networth pair (last re-shot v67); the full re-run ledger is in the probe README. (2) The axe-core watch at its next re-check point (only a 5.x wrapper changes the calculus). (3) The deferred reference-write censuses (unchanged, blocked by the v46 read-only rule). The full queue: `docs/remediation-plan-v74.md`.
