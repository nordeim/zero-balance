# Remediation Plan v98 — the re-run cycle's next-oldest candidate (the v92-era SAVINGS pair's sixth re-run) + the axe watch + the goal-card action-menu panel/menuitem-resting census pin (PIN-ONLY)

The formal narrative: `docs/session_235.md` (the v97 cycle's own narrative
log). The queue: the v97 plan's v98 suggestion — **the ledger-verified
target** (the v97-era docs' suggestion AGREEING with the rotation ledger:
the v92-era SAVINGS pair [the SAVINGS view at desktop 1280x800,
full-page], last re-shot v92 — now the oldest remaining
[v92 < v93 < v94 < v95 < v96 < v97]; the pair's SIXTH re-run
[v58 → v65 → v74 → v80 → v86 → v92 → v98] — the TWENTY-FIRST consecutive
queue/ledger agreement), plus the axe-core watch at its re-check point
and the 92nd standing checks.
**PIN-ONLY for src/ — no production-code change; +1 e2e = 301.**

## The pre-execution ledger verification (the queue-prose verification lesson, applied)

The rotation ledger's authority is the PROBE LINEAGE, never the prose
queue phrasing. Verified against `scripts/parity-probes/vlm-shots-v92.sh`
before the derivation: its own header reads "the SAVINGS view at desktop
1280x800, FULL-PAGE — the fresh sweep of the re-run cycle's OLDEST
candidate (the v86-era savings pair, last re-shot v86, now the oldest
remaining [v86 < v87 < v88 < v89 < v90 < v91]; the pair's FIFTH re-run
[v58 → v65 → v74 → v80 → v86 → v92]" — matching the queue's phrasing
exactly (no transcription error; the v92-era surface names confirmed:
the SAVINGS view at desktop 1280x800 full-page). The SIXTH re-run bracket
[v58 → v65 → v74 → v80 → v86 → v92 → v98] constructed from the same
header's FIFTH bracket. The standing-checks pair (ref-standing-v92.sh +
standing-checks-v92.sh) derived from v91 across the THREE token families
(v91→v92, 91st→92nd, ref91→ref92/clone91→clone92), version-bump-only
verified by normalizing back and diffing clean (zero old tokens remaining
— the persisted derive-standing-v98.py, both halves bash -n clean).

## Findings

### F0 — the baseline chain: FULLY GREEN as-shipped (no finding)

seedcheck exact (7 items / rent 1850 / expensesTotal 2235 / 0 line items
/ 3 assets / 2 liabilities) before any flow ran; lint ✓ · typecheck ✓ ·
108/108 unit ✓ · `npm run build` ✓ (robots + sitemap prerendered) ·
**300 e2e ✓** (135 + 96 + 71 chunk executions across three chunk splits
of the 24 files = 302 total = 300 unique tests — the exact documented
v97 state, zero flakes on the first run) · 35/35 smoke ✓. The workspace:
the FRESH-CLONE path (the v86/v88/v90/v91/v92 precedent — the sandbox
had been reset), the environment re-provisioned (npm install 354+
packages; `.env` written [DATABASE_URL="file:../db/custom.db"]; `db/` at
the repo root, db:generate + db:push + db:seed; chromium-1243 installed
for the pinned @playwright/test 1.63.0 — the cache's pre-installed
1200 build belongs to a different playwright generation; the
`/home/z/my-project/tool-results/` dir re-created for with-server.sh).

The codebase audit clean: the two commits since the v97 push 6a6725c
(d4b77c5 + 9152c18) verified session-log-only (docs/session_234.md +
docs/session_235.md — ZERO src/ or lockfile deltas); the production
seams re-audited — auth (scrypt/HMAC), the db-path contract (db-path.ts
+ its unit test; the sandbox's polluted parent DATABASE_URL
re-confirming the reason the `env -u` discipline is load-bearing), the
SEO pair (robots.ts allow-all + sitemap.ts 5-URL structure — both
prerendered by the build), the Tailwind v4 mitigations
(`@variant hover (&:hover)` + the toast pointer-events fix), the three
test tiers; skills/ excluded throughout (the eslint ignores + the
tsconfig exclude verified live).

### F1 — the axe-core watch: NO DRIFT

npm-latest `@axe-core/playwright` 4.14.0 (dist-tags: rc/next sha
prereleases only beyond — no stable 4.14.1, no 5.x exists); the
installed wrapper 4.14.0 + the engine 4.14.0; the lockfile holding the
v68 dedupe state (exactly one `node_modules/axe-core` entry); the
engine-contract pin GREEN standalone (2 passed).

### F2 — the 92nd standing checks: ALL GREEN (version-bumped from v91 — version-bump-only diffs verified)

ref-standing-v92.sh + standing-checks-v92.sh (version-bumped from v91
via the persisted derive-standing-v98.py across the THREE token families
[v91→v92, 91st→92nd, AND the bare session names ref91→ref92/
clone91→clone92]; after normalizing back the files are version-bump-only:
diffed clean, zero old tokens remaining). Reference side: the four bugs
ALL live [toast-blocker `hitIsBurgerChild:false`; sheet-trap
`overlayCount:1` after nav; no-landmark `navLandmark:false`; the 464px
/networth overflow at 390 measured docSW 464 directly]; the data census
UNCHANGED on the first read (networth "1 items · $25,000" / income
"1 items · $5000.00" / expenses "4 items · $525.00" — no render-race
this cycle; the v97 generalization held in the clean direction); the
SEO pair live. Clone side: R1–R4 ALL GREEN — **the mobile menu
VERIFIED WORKING the 92nd consecutive time** (`hitIsBurgerChild: true`,
the sheet opens, closes on nav, the nav landmark present — the Tailwind
v4 mitigation holds), zero overflow at 390 on all five views, the SEO
pair live.

### F3 — the re-run pair (the v92-lineage derivation, the two-half census form)

The probe series derived from the v92 lineage (derive-v98-series.py,
persisted): vlm-shots-v98.sh + clone-vlmshots-v98.sh +
vlm-compare-v98.mjs + arbit-v98.sh — the generic swaps (v92→v98,
refvlm92→refvlm98, clonevlm92→clonevlm98, refarbit92→refarbit98,
clonearbit92→clonearbit98, /tmp/vlm92→/tmp/vlm98) followed by the
exact-fragment history corrections (last-re-shot v86→v92, FIFTH→SIXTH,
the re-run bracket extension, the oldest-remaining bracket
[v92 < v93 < v94 < v95 < v96 < v97], the agreement ordinal
FIFTEENTH→TWENTY-FIRST, the suggesting plan v91→v97) — every correction
verified applied (the derive script reports each hit/miss; the one
first-run MISS [the arbit header's line break] caught by the report
itself and fixed before any probe executed — the v96 miss-report
discipline). bash -n + node --check clean on all four; zero residual
old tokens (the legitimate v92 provenance/bracket tokens whitelisted by
context). The census BUILT two-half from the start (build-twohalf-v98.py
— ref-arbit-v98.sh + clone-arbit-v98.sh, the ONE census JS block
[SV_CENSUS_JS 153 lines] extracted once and embedded byte-identically
across the halves — the md5 line-block contract [31d181ed]). The
reaping budget applied as the standing step between every half. Login on
the first attempt both sides; the parked pointer at (5,5); read-only —
the v46 rule holds.

**The verdict DIFFERENT, every flag DOM-arbitrated to a documented
class:**

1. The "Card Footer Alignment" (the reference's date-only footer vs the
   clone's date + payment chip) — the **v57 DATA-CONDITIONAL class**
   (the census proving the footer childCount 1-vs-2 with the clone's
   "Brokerage" chip; the reference RENDERS payment chips when data
   carries them — the v97 income-card evidence — its savings item simply
   ships no payment method).
2. The "Card Grid" (the reference's single card vs the clone's two) —
   the seed-count class (grid childCount 1 vs 2).
3. The header subtitle "1 items · $1000.00" vs "2 items · $1250.00" —
   the seed-data class.
4. The card contents (names/amounts/badges/dates) — the seed-data
   classes (the reference's "need"/red badge vs the clone's
   "savings"/green — the classification-VALUE class; the clone's
   "Recurring" 4th badge — the DATA-CONDITIONAL class).
5. The avatar "U" vs "D" — the user-identity class.

The both-sides census (the two-half controlled form) **REPRODUCES the
v86/v92 census values EXACTLY — zero drift on every axis**:

- **The HEADER** {h1 "ZeroBalance" fs 20px / fw 700 / rgb(26, 58, 46)}
  — byte-identical (the hidden-SEO-h1 family).
- **The GRID + CARD chrome** {grid w 960 / gap 16px / the 3-col
  309.328px template family; card w 309 / pad 20px / radius 12px /
  border 1px rgb(229, 231, 227) / bg white} — byte-identical; the
  childCount (1 vs 2) the seed-count class; the card h (200 vs 230) the
  v57/v70b Recurring-wrap class (+30px: the badgeRow h 22 vs 52); the
  clone template's last-column sub-pixel (.328/.328/.344 vs .328 ×3)
  the column-distribution rounding noise WITHIN the documented
  309.328px family (the reference's own expenses template reads
  .328/.328/.344 — byte-identical to the clone's form).
- **The TITLE ROW chrome** {gap 8px / dot 8×8 / dotBg rgb(59, 126, 161)
  / font 16px / weight 600 / lh 24px} — byte-identical.
- **The AMOUNT leaf chrome** {fs 24px / fw 700 / lh 32px / color
  rgb(59, 126, 161)} — byte-identical.
- **The FOOTER + BADGE chrome** {footer flex/space-between/12px/
  rgb(107,114,128)/h 16; badge row flex/wrap/8px gap/mb 12px; badge
  radius 6px/pad 2px 10px/fs 12px/fw 600/h 22} — byte-identical; the
  footer childCount (1 vs 2) the v57 DATA-CONDITIONAL class; the
  badgeRow h (22 vs 52) + texts the wrap/classification-VALUE classes;
  the "monthly" (purple rgb(126, 34, 206)) + "active" (slate
  rgb(51, 65, 85)) badges byte-identical in full chrome.
- **The docSW 1280 guard** on both sides.

**NO NEW CLONE GAP — the v98 iteration PIN-ONLY.**

### F4 [PIN] — the goal-card ACTION-MENU PANEL + MENUITEM-RESTING interior census at 1280 (PIN-ONLY for src/ — no production-code change; +1 e2e = 301)

The never-pinned family (the FAMILY-EXTENSION pattern — the v97
missing-middle lesson applied to the ACTION layer): the savings goal
card's ellipsis dropdown menu. The tokens.spec G5/G9 pins hold the
menu ITEM's COLOR family (editRest rgb(10,10,10) / deleteColor
rgb(220,38,38) / the focus-state bg) and the menu CONTENT's
border-COLOR (rgb(229,229,229)) on the income view; the v35 S1 pin the
keyboard contract — **the menu PANEL's GEOMETRY (bg/radius/shadow/
min-w/overflow/z/w/h) and the menuitem's RESTING interior (fs/fw/pad/
radius/lh/h) are NEVER pinned at ANY viewport in ANY spec** (the
coverage-map grep across all 24 specs: zero specs assert any
`[role="menu"]` radius, pad, shadow, or min-w; zero specs assert any
menuitem pad — the only menu computed-style assertion anywhere is the
G5 contentBorder color axis).

**The pin's own axes first measured byte-identical on BOTH sides** by
the supplemental two-half census (menu-arbit-v98.sh + menu-clone-v98.sh
— BUILT two-half from the start via build-menu-v98.py, the census JS
byte-identical by the md5 line-block contract [0f83b786 — 42 lines];
both sides read-only — a menu OPEN only, no item clicks, the v46 rule
intact; the seedcheck exact after the run; the doubled-brace spot grep
clean):

- The PANEL: {bg `rgb(255, 255, 255)`, radius `6px`, border `1px
  rgb(229, 229, 229)`, minW `128px`, overflow `hidden`, z `50`, pos
  `static`, w `128`, h `74`} — **byte-identical across sides** (the
  rounded-md/border-input/bg-popover/min-w-[8rem]/p-1 family). The h 74
  is DATA-INDEPENDENT (both sides' menus carry exactly the Edit+Delete
  pair: 2×32 item + 2×4 pad + 2×1 border = 74).
- The shadow's VISIBLE layers: `rgba(0, 0, 0, 0.1) 0px 4px 6px -1px` +
  `rgba(0, 0, 0, 0.1) 0px 2px 4px -2px` (the shadow-md family) —
  byte-identical; the full string's zero-layer LEAD count differs (ref
  2 leads vs clone 4) — the **v3/v4 shadow-construct class** (the
  documented v37 O1 note — every lead is a 0px-spread shadow, invisible
  by construction; the VISIBLE layers are the contract — asserted via
  containment, the established toContain form).
- The ITEM's RESTING interior: {fs `14px`, fw `400`, color
  `rgb(10, 10, 10)`, pad `6px 8px`, radius `4px`, lh `20px`, h `32`} —
  **byte-identical across sides** (the text-sm/rounded-sm/px-2 py-1.5
  family).
- The trigger's w (36 — the h-9 w-9 family) + the itemCount (2) +
  the docSW 1280 — byte-identical.

**The cross-side trigger FINDER (a new documented arbitration note)**:
the reference's savings-card action trigger carries NO aria-label (the
clone's `Actions for {category}` label is the a11y SUPERSET — like the
search input's aria-label in the v38 S2 note), so the census's
cross-side finder is GEOMETRIC — the textless 36×36 svg button. And the
menu OPEN on the reference requires the full POINTER EVENT SEQUENCE
(pointerdown → mousedown → pointerup → mouseup → click — the Base44
React tree's listener family); a bare `el.click()` opens the clone's
Radix menu but NOT the reference's. The e2e pin (clone-side,
Playwright's real mouse) needs no such sequence — Playwright's click
dispatches the full native sequence by construction.

**The pin** (tests/e2e/items.spec.ts, appended as the v98 describe
block): hover the Emergency Fund card → click the clone's
aria-labelled trigger (`Actions for Emergency Fund`) → settle past the
animate-in window [700ms] → the `[role="menu"]` panel → the first
`[role="menuitem"]`; asserts — the panel {bg, radius `6px`, border
`1px rgb(229,229,229)`, minW `128px`, overflow `hidden`, z `50`, pos
`static`, w `128`, h `74`}; the shadow's visible layers via toContain
(both `rgba(0, 0, 0, 0.1) 0px 4px 6px -1px` and `rgba(0, 0, 0, 0.1)
0px 2px 4px -2px`); the item0 resting interior {fs `14px`, fw `400`,
color `rgb(10, 10, 10)`, pad `6px 8px`, radius `4px`, lh `20px`, h
`32`}; the itemCount 2 + the docSW 1280 guard. Unlike the v97 pin (whose
panel h + optCount were the clone's own data-dependent values), this
pin's panel w/h + itemCount are DATA-INDEPENDENT (the Edit+Delete pair
is structural on both sides) — the census values assert directly.

**The pin-sanity mutation (the planned form)**: the DropdownMenuContent
panel's `rounded-md` → `rounded-lg` (src/components/ui/dropdown-menu.tsx:20,
by LINE NUMBER — the line-scoping keeps the DropdownMenuItem's own
`rounded-sm` at line 36 untouched [the item's 4px radius axis]). Expected:
the pin FAILS at exactly the panel radius axis alone (`6px` → `8px`);
cascade-free BY CONSTRUCTION (no spec asserts any dropdown-menu panel
radius — this pin is the first; the v97 listbox panel radius 6px reads
select.tsx's SelectContent — a DIFFERENT component at a different line;
the tokens G5 contentBorder is the border-COLOR axis, not radius; the
radius never changes bg/border/shadow/min-w/overflow/z/w/h/item-interior;
`rounded-lg` on the panel does not affect the CLOSED state — the panel
renders only when open). Then restored (git diff src/ = 0 lines; the
standalone REBUILD via the FULL npm run build; the post-restore full
items.spec.ts run green).

**The disproven-in-advance candidates (documented without execution):**
the item pad mutation (py-1.5 → py-2: cascades to the item's h
arithmetic [32 → 36] AND the panel h [74 → 82] — a three-axis failure,
not the clean single-axis form); the min-w mutation (min-w-[8rem] →
min-w-[10rem]: changes minW AND the panel w [128 → 160] — two axes);
the border mutation (border-input → border-2: changes borderWidth AND
the panel h — two axes); the bg mutation (bg-popover → bg-white: the
visual-identical no-op class — not a demonstration).

## The ToDo list

| # | Step | Status |
|---|------|--------|
| 1 | F0 baseline chain on the fresh-clone workspace (provisioned: npm install, prisma, seed, chromium-1243) | DONE — all green |
| 2 | F1 axe-core watch | DONE — NO DRIFT |
| 3 | F2 92nd standing checks (derived v91→v92, version-bump-only verified) | DONE — ALL GREEN (census clean on the first read) |
| 4 | F3 the v92-lineage probe derivation (generic swaps + exact-fragment history corrections + residual checks) | DONE |
| 5 | F3 two-half census builder (build-twohalf-v98.py, md5 contract) + both halves executed | DONE |
| 6 | F3 the VLM pairwise | DONE — verdict DIFFERENT, all flags arbitrated |
| 7 | F4 the supplemental menu two-half census (the pin's own axes measured byte-identical) | DONE |
| 8 | F4 THIS PLAN written + validated BEFORE the pin's execution | DONE |
| 9 | F4 append the v98 pin to tests/e2e/items.spec.ts | PENDING |
| 10 | F4 pin first run (GREEN expected) | PENDING |
| 11 | F4 pin-sanity mutation (ui/dropdown-menu.tsx:20, line-number-scoped) → single-axis failure → restore (git diff src/ = 0) → standalone REBUILD → post-restore full file run | PENDING |
| 12 | F5 full chain re-run (lint/typecheck/108 unit/build/301 e2e/35 smoke) + the screenshots regeneration + byte-compare | PENDING |
| 13 | D1–D7 docs alignment + session_236.md + the worklog Session 133 entry | PENDING |
| 14 | ship: the full chain re-run + commit + SSH-wrapper push | PENDING |

## The pre-execution validation section (the measured evidence)

- The pin's measured values (the menu two-half census, this session):
  panel {bg rgb(255,255,255), radius 6px, border 1px rgb(229,229,229),
  minW 128px, overflow hidden, z 50, pos static, w 128, h 74}
  byte-identical; the shadow's visible layers {rgba(0,0,0,0.1) 0px 4px
  6px -1px + rgba(0,0,0,0.1) 0px 2px 4px -2px} byte-identical (the
  zero-layer lead count 2-vs-4 the v3/v4 construct class); the item0
  resting interior {fs 14px, fw 400, color rgb(10,10,10), pad 6px 8px,
  radius 4px, lh 20px, h 32} byte-identical; the itemCount 2 + trigW
  36 + docSW 1280 byte-identical; the seedcheck exact after the run.
- The mutation target line verified by reading the source:
  src/components/ui/dropdown-menu.tsx:20 — the DropdownMenuContent
  className carries EXACTLY ONE `rounded-md` (grep-count 1 on the line);
  the DropdownMenuItem's `rounded-sm` token sits at line 36 (the item's
  4px radius axis — untouched by the line-number scoping).
- The coverage-map grep (run across ALL 24 specs): zero specs assert any
  `[role="menu"]` radius, pad, shadow, or min-width; zero specs assert
  any menuitem pad — the only menu computed-style assertion anywhere is
  the tokens.spec G5 `contentBorder` (the border-COLOR axis, income
  view); the item COLOR family (editRest/deleteColor) pinned G5/G9 —
  the RESTING GEOMETRY never.
- The rotation ledger verified: the savings pair last re-shot v92 = the
  oldest remaining [v92 < v93 < v94 < v95 < v96 < v97] — the v97-era
  docs' v98 suggestion agreeing with the ledger (the TWENTY-FIRST
  consecutive agreement), the surface names verified against
  vlm-shots-v92.sh's own header before the derivation.
- The pin's finder: the clone-side aria-labelled trigger
  (`Actions for Emergency Fund` — the superset) via getByRole; the
  census's cross-side GEOMETRIC finder (the textless 36×36 svg button)
  proven stable across this session's runs (the manual reference probe +
  the two-half census halves).

## Operational lessons this cycle (the probe README's D6 section)

- THE REFERENCE POINTER-EVENT FAMILY (NEW): the reference's React tree
  opens its ellipsis dropdown only on the full pointer event SEQUENCE
  (pointerdown → mousedown → pointerup → mouseup → click); a bare
  synthetic `el.click()` opens the clone's Radix menu but NOT the
  reference's. Any future census that must OPEN reference-side
  interactive chrome dispatches the full sequence.
- THE UNLABELLED-TRIGGER FINDER CLASS (NEW): the reference's card action
  trigger carries NO aria-label (the clone's is the a11y superset — the
  v38 search-input aria-label note's sibling) — cross-side finders for
  action chrome must be GEOMETRIC (the textless 36×36 svg button), with
  the clone-only aria-label reserved for the e2e pin's locator.
- THE DATA-INDEPENDENT PANEL (a pin-strength note): the action menu's
  Edit+Delete pair is STRUCTURAL (both sides render exactly 2 items), so
  the panel w/h + itemCount are data-independent — unlike the v97
  listbox pin (whose h/optCount were clone-only guards), these axes
  assert cross-side-verified values directly.

## The next queue (the v99 suggestion — verify against the rotation ledger before executing)

(1) the re-run cadence rotates to the next-oldest candidate after the
savings pair (the v93-era LOGIN + CALCULATOR pair [the login view + the
calculator card pair at desktop 1280x800], last re-shot v93 — now the
oldest remaining [v93 < v94 < v95 < v96 < v97 < v98]; the pair's re-run
bracket to be verified against vlm-shots-v93.sh's own header before the
derivation), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).
