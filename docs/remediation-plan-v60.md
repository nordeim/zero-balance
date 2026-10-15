# Remediation Plan v60 — The networth-view desktop 1280 VLM standing pair +
# the dashboard drill-down EXPANDED-state pair (PIN-ONLY — no
# production-code change; the tenth iteration since v46, the pin-only
# line's continuation)

Date: 2026-10-15 · Scope: the session-141 v60 queue's first TWO items —
"the NETWORTH view's desktop 1280 VLM pair (the remaining major view
with no DEDICATED pair — the v56 PAIR 2 was the glyph-swap audit pass;
the v52-era pins cover the 390/640 chrome)" and "the DASHBOARD's
drill-down surfaces at 1280 (the v43 F3 family pinned the sub/item rows
at 640 only; the v44 F2b pin at 1280 walked the section/category/footer
heights — the sub/item-row chrome at the pair viewport unpinned)" —
plus the 54th standing checks. Measured live on BOTH sites via the v60
family (vlm-shots-v60.sh + clone-vlmshots-v60.sh + vlm-compare-v60.mjs
— the FULL-PAGE 1280x800 pair of the networth view AND the dashboard
with the drill-down expanded section+category; nw-census-ref-v60.sh +
nw-census-clone-v60.sh — the networth DOM arbitration + census, both
sides; drill-census-ref-v60.sh + drill-census-clone-v60.sh — the
drill-down expanded census, both sides; drill-arbit-ref-v60.sh +
drill-arbit-clone-v60.sh — the PAIR 2 flags' arbitration; +
drill-itemdump-ref-v60.sh — the item-row finder artifact's evidence;
ref-standing-v54.sh + standing-checks-v54.sh — the 54th standing
checks). All READ-ONLY on the reference (the v46 rule) — the drill-down
expansion clicks are VIEW-STATE toggles that mutate no data.

Baseline before the sweep: lint ✓ · typecheck ✓ · 108/108 unit ✓ ·
build ✓ (robots + sitemap prerendered) · **259 e2e ✓ (90 + 94 + 76
chromium + the setup test, three ordered chunks, zero failures)** ·
35/35 smoke ✓. The 54th standing checks all clean (the reference's
four bugs ALL live [toast-blocker hitIsBurgerChild:false, the
sheet-trap overlayCount:1, the no-landmark navLandmark:false, the 464
/networth overflow], the clone's mobile menu VERIFIED WORKING — the
54th time, the data census intact ["1 items · $25,000" networth /
"1 items · $5000.00" income / "4 items · $525.00" expenses — the
expenses census now IN the standing script], the SEO pair live on both
sites).

## The v60 sweep — what the measurement found

- **THE NETWORTH 1280x800 VLM PAIR (the session-141 queue item #1):
  VERDICT IDENTICAL** — the VLM found ZERO layout/style differences
  (the gradient summary card, the glassy stat tiles, the ratio footer,
  the tab bar, the type-grouped cards); every difference it listed was
  the expected DATA class (the figures, the counts, the groups, the
  ratio "∞:1" vs "0.21:1"). The DOM census (both sides) byte-identical
  on every chrome axis: the summary card w 960 / pad 32px / radius
  16px / the 135deg forest→lime gradient linear-gradient(135deg,
  rgb(45,90,74) 0%, rgb(143,188,63) 100%) / the shadow rgba(26,58,46,
  0.3) 0px 20px 60px; the figure 48px/700/white; the label 14px
  rgba(255,255,255,0.8) mb 8px; the medallion 64×64 bg
  rgba(255,255,255,0.2) svg 32; the stat grid 440px 440px gap 16px;
  the stat tile 440 / pad 16px / radius 12px / bg
  rgba(255,255,255,0.1) / blur(10px) / the label 12px
  rgba(255,255,255,0.7) / the amount 24px/700; the ratio value 18px/700
  (the text the data class: "∞:1" vs "0.21:1" — the pinned formatRatio
  contract); **the tablist 448 / h 36 / template 220px 220px / the
  trigger h 28 / pad 4px 12px / 14px/500 / the icon 16** (the v50 F2's
  own 640 values, re-confirmed at 1280); the group header 18px/600/
  rgb(45,90,74)/mb 12px/capitalize; **the card grid 960 / 3×309.328 /
  gap 16** (the v46 F2 values, live on both sides); the first card
  309 / pad 20px / radius 12px / border 1px solid rgb(229,231,227) /
  bg white / the resting shadow rgba(0,0,0,0.04) 0px 2px 8px / the dot
  8× rgb(143,188,63) / the name 16px/600 / the value 24px (mb 16px —
  the v46 F1 wrap). **The pair CLEAN per the v43 rule.**
  Divergence classes (both documented): the summary card's mb — the
  reference computes marginBottom 0 (its 32px card→tablist GAP lives
  on a different element) while the clone carries mb-8 — the GEOMETRY
  (the 32px gap, v41-measured nw-below-v41.mjs) is the parity
  contract, the DOM shape is not (the v45 lesson); the figure's
  word-break — the clone's break-words guard (the D-5 superset, the
  reference's own 464px overflow at 390 the counter-example).
- **THE DASHBOARD DRILL-DOWN EXPANDED 1280x800 VLM PAIR (the
  session-141 queue item #2): flagged FIVE items, every one
  DOM-arbitrated (the v43 rule):**
  1. the Dashboard nav highlight — the documented **root-URL active-nav
     gap** (the reference shows none at `/`: transparent / zinc-700 /
     400; the clone highlights: white/500 + the forest gradient — the
     superset contrast #3, re-confirmed live: ref bg transparent color
     rgb(63,63,70) fw 400 vs clone color rgb(255,255,255) fw 500);
  2. the avatar "U" vs "D" — the **user-identity class** (each site's
     own logged-in user);
  3. the "Edit with Base44" tooltip — the **platform-chrome class**
     (the reference's own dev overlay, documented since v19);
  4. the hero progress-bar fill 30.5% vs 62.8% — the **pct × 568 data
     class** (the v56 arbitration: the track byte-identical 568×12
     rgba(255,255,255,0.1), the fill's width = each site's own
     allocation pct — the reference 173, the clone 357);
  5. the donut percentage labels (the VLM claimed the reference shows
     none) — a **PERCEPTION ARTIFACT, arbitrated live both sides**: the
     reference DOES render its labels (count 3 individual texts
     "92.3%"/"4.6%"/"3.1%", labelLineCount 0, 16px, fill black — the
     v9 G1b measurement re-confirmed) and the clone renders the same
     chrome (count 3, "81.6%"/"13.8%"/"4.6%", labelLineCount 0, 16px,
     black — the values each site's own data).
  **The drill census (both sides) byte-identical on every axis**: the
  card 304 wide; collapsedH 364 BOTH (the v44 F2b arithmetic's start);
  the section {h 56, pad 8px, ml -8px, radius 8px, cursor pointer,
  labelH 40} — the 2-line WRAP at 1280; the category {h 28, pad
  "6px 12px", radius 8px, bg rgb(249,250,251), label 12px/500/
  rgb(26,58,46)}; **the sub row {h 24, pad "4px 8px", bg
  rgb(250,250,250), label 12px/400/rgb(107,114,128)}**; **the item row
  {h 24, pad "4px 8px", font 12px, color rgb(156,163,175), label
  maxW 120px, trunc ellipsis}**; the footer {h 29, pad "6px 12px",
  borderTop 1px, 12px/600}. The expansion heights 364→445→499
  (reference) vs 364→481→535 (clone) — the DATA class (its one Salary
  category vs the seed's two income categories; the v44 F2b comment
  documents both). One census-axis false alarm arbitrated by
  drill-itemdump-ref-v60.sh: the reference-side census's rows[last]
  caught the item row's INNER label-group div (h 16, pad 0) — the
  reference's REAL item row (flex items-center justify-between py-1
  px-2, h 24, pad "4px 8px", the maxW-120/ellipsis label) is
  byte-identical to the clone's. **The pair CLEAN.**
- **NO production gap found — v60 is PIN-ONLY** (the v53/v54/v56/v57/
  v58/v59 class). The gaps in the pin COVERAGE: the networth view's
  summary card + tablist are pinned at 640 (v41 F2) and 390 (v41 F3)
  but NOT at the 1280 pair viewport; the drill-down's sub/item rows
  are pinned at 640 only (v43 F3) — the v44 F2b 1280 pin walked the
  section/category/footer heights, not the sub/item chrome. The v60
  deliverable pins both surfaces at the pair viewport.

## Findings

### F1. [PIN] the networth view's summary-card + tablist census at 1280

One new test in `tests/e2e/networth.spec.ts` — its own describe "net
worth view census at 1280 (v60 — plan F1)":

**F1** (the read-only logged-in state, the v41-F2 pattern at the pair
viewport) on /networth at 1280×800: (1) the summary card: w 960 / pad
32px / radius 16px / backgroundImage
linear-gradient(135deg, rgb(45, 90, 74) 0%, rgb(143, 188, 63) 100%) /
boxShadow toContain "rgba(26, 58, 46, 0.3)"; (2) the figure 48px/700/
rgb(255,255,255); (3) the label 14px/rgba(255, 255, 255, 0.8); (4)
the medallion 64×64 + bg rgba(255, 255, 255, 0.2) + the svg 32; (5)
the stat grid template "440px 440px" + gap 16px; (6) the stat tile
(pad 16px / radius 12px / bg rgba(255, 255, 255, 0.1) / blur(10px) /
the amount 24px/700); (7) the ratio value 18px/700 (the TEXT is the
seed's "0.21:1" — pinned as the formatRatio contract); (8) the
tablist: w 448 / h 36 / template "220px 220px" (the v50 F2's own
values at the pair viewport); (9) the group header 18px/600/
rgb(45, 90, 74)/mb 12px/text-transform capitalize; (10) the controls:
the grid 960 wide / template 3×309.328 / gap 16px + the first card w
309 / pad 20px / radius 12px (the v46 F2 values re-asserted).

### F2. [PIN] the drill-down's sub/item-row census at 1280

One new test in `tests/e2e/dashboard.spec.ts` — its own describe "the
drill-down sub/item-row census at 1280 (v60 — plan F2)":

**F2** (the v43-F3 pattern at the pair viewport, the v44-F2b expansion
flow) on /dashboard at 1280×800: expand Total Income → its first
category → census the sub-area: (1) the sub row: h 24 / pad "4px 8px"
/ bg rgb(250, 250, 250) / the label 12px/400/rgb(107, 114, 128); (2)
the item row: h 24 / pad "4px 8px" / font 12px / color
rgb(156, 163, 175) / the label maxWidth 120px + textOverflow
ellipsis; (3) the expansion-height controls (the v44 F2b values
re-asserted: cardW 304, collapsed 364, secExpanded 481, fullExpanded
535 — the seed's deterministic arithmetic); (4) the section/category/
footer controls (the v44 F2b values: section {56, 8px, labelH 40},
category {28, "6px 12px", rgb(249, 250, 251)}, footer {29, 1px}).
The sub/item-row FINDER pins the REAL rows (the
justify-between + px-2 py-1 rows), never the inner label-group divs
(the v60 itemdump lesson — filter by pad !== "0px" or the
justify-between class).

### S1. [MUTATION-SANITY] the pins bite

(a) the summary card's `rounded-2xl p-8` → `p-10`
(src/components/budget/net-worth-view.tsx:325) → the F1 summary pad
assertion FAILS (32px vs 40px);
(b) the tablist's `max-w-md` → `max-w-lg`
(net-worth-view.tsx:401) → the F1 tablist w/template assertions FAIL
(448 vs 512, "220px 220px" vs "256px 256px");
(c) the item label's `max-w-[120px]` → `max-w-[140px]`
(dashboard-view.tsx:424) → the F2 item labelMaxW assertion FAILS
("120px" vs "140px").
All restored → GREEN. Each mutation preceded by `npm run build`, run
as a SEPARATE command (the v47–v59 execution lesson).

### P1. [PROBE-INFRA] the v60 probe family persisted

vlm-shots-v60.sh + clone-vlmshots-v60.sh + vlm-compare-v60.mjs (the
networth + drill-down expanded FULL-PAGE pairs),
nw-census-ref-v60.sh + nw-census-clone-v60.sh (the networth DOM
arbitration + census, both sides), drill-census-ref-v60.sh +
drill-census-clone-v60.sh (the drill-down expanded census, both
sides), drill-arbit-ref-v60.sh + drill-arbit-clone-v60.sh (the PAIR 2
flags' arbitration), drill-itemdump-ref-v60.sh (the item-row finder
artifact's evidence), ref-standing-v54.sh + standing-checks-v54.sh
(the 54th standing checks — the expenses census now in the standing
script), plus the probe README's v60 section. The v60 probe lessons:
(1) **a single-quoted bash CENSUS string must contain NO single
quotes** — the JS selectors like '[role="tablist"]' TERMINATE the
bash string (the script's eval silently returns empty) — use escaped
double-quoted JS strings ("[role=\"tablist\"]") inside the
single-quoted wrapper, or a quoted heredoc; the failure signature is
an empty eval line between the === markers; (2) the FULL-PAGE
screenshot (--full) is the pair-shot mode for views taller than the
800 viewport (the networth/drill-down surfaces below the fold) — the
v56-v59 pairs were viewport shots of surfaces that fit; (3) the
drill-down expansion clicks are VIEW-STATE toggles (safe under the
v46 read-only rule) — the reference's own Salary category expanded
with no data mutation; (4) the recharts label census must filter the
individual <text> labels from the group wrapper (the count includes
the wrapper: count 4 = 1 group + 3 labels) and the label-line count
(labelLineCount 0 — the v9 G1b contract) is the arbitration axis; (5)
the census row-finders must pin the REAL rows by their chrome (the
pad/pattern), never by array position — the reference's sub-area
contains the rows' INNER label-group divs (h 16, pad 0) that a
rows[last] finder catches instead of the real item row.

### D1–D8. [DOCS] the doc alignment

D1: AGENTS.md — the v60 paragraph. D2: CLAUDE.md — the E2E count
259 → 261 + the v60 family entries (networth + dashboard). D3:
README — the counts + the v60 row. D4: the SKILL doc — the Session 95
row + the state line. D5: the PAD — a v1.1.17 revision block. D6: the
probe README — the v60 section + the lessons. D7: session_142.md (the
formal log) + the repo worklog Session 94 + the ledger list. D8: the
workspace worklog.

## The remediation ToDo list

| # | Item | Type | Files |
|---|------|------|-------|
| 1 | F1's pin: the networth summary-card + tablist census describe at 1280 → GREEN (pin-only, no RED phase — the surface is already correct; the pin is the deliverable) | test | `tests/e2e/networth.spec.ts` |
| 2 | F2's pin: the drill-down sub/item-row census describe at 1280 → GREEN (the finder pins the REAL rows — the itemdump lesson) | test | `tests/e2e/dashboard.spec.ts` |
| 3 | S1(a)–(c): the three pin-sanity mutations, each verified to FAIL then restored (each preceded by `npm run build`, run as a SEPARATE command) | verify | `net-worth-view.tsx` + `dashboard-view.tsx` |
| 4 | The probe scripts persisted + the probe README's v60 section | docs | `scripts/parity-probes/` |
| 5 | The full chain re-run (108 unit · **261** e2e [+2: the v60 pins] · 35 smoke + lint + typecheck + build) — all green | verify | — |
| 6 | The 16 screenshots regenerated (expect byte-identical OR the seed-date class — the db re-seeded on the capture date; keep whichever diff, arbitrate if not byte-identical) | docs | `docs/screenshots/` |
| 7 | D1–D8 + the formal session log (session_142.md — the formal v60 log; the raw transcript lands as session_144.md in the follow-up commit per the session-141 pattern) + the repo worklog Session 94 + the SKILL doc Session 95 row | docs | repo root + `docs/` |
| 8 | Commit + push to main via the SSH wrapper | ship | — |

## Validation against the codebase (pre-execution)

- `src/components/budget/net-worth-view.tsx:325` — the summary card's
  `relative mb-8 overflow-hidden rounded-2xl p-8` (32px pad, 16px
  radius, the 32px mb — the S1a mutation target); `:326-329` the
  inline gradient + the shadow (the F1 bg assertion's source); `:348`
  the figure `break-words text-2xl font-bold text-white sm:text-5xl`
  (48px at 1280); `:342` the label `mb-2 text-sm` +
  rgba(255,255,255,0.8); `:352-357` the medallion `h-16 w-16` +
  rgba(255,255,255,0.2); `:365` the stat grid `grid grid-cols-1 gap-4
  sm:grid-cols-2` (440px 440px at 960-wide, gap 16); `:366-368` the
  tile `rounded-xl p-4` + rgba(255,255,255,0.1) + blur(10px); `:384-
  396` the ratio footer `mt-6 pt-6` + the inline border; `:392-393`
  the value `text-lg font-bold text-white` (18px/700); `:401` the
  tablist `grid w-full max-w-md grid-cols-2` (448 / 220px 220px — the
  S1b target); `:463-465` the group h3 `mb-3 text-lg font-semibold
  capitalize` + COLORS.forestMedium (rgb(45,90,74)); `:469` the card
  grid `grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3` (3×309.328
  at 960, gap 16); the card `rounded-xl border bg-white p-5` (20px
  pad, 12px radius).
- `src/components/budget/dashboard-view.tsx:392-408` — the sub row
  `flex items-center justify-between rounded px-2 py-1` + the inline
  bg rgb(250,250,250) + the label `text-xs` rgb.gray (12px/400/
  rgb(107,114,128)); `:413-428` the item row `flex items-center
  justify-between px-2 py-1 text-xs` + the inline color
  rgb(156,163,175) + the label `max-w-[120px] truncate` (the S1c
  target at :424).
- The e2e contract: both v60 describes run AUTHENTICATED via the
  setup project's storageState; the deterministic e2e seed
  (prisma/seed.ts, re-seeded into db/e2e.db every run by
  global-setup) puts the same networth data (3 assets / 2 liabilities
  → the "0.21:1" ratio) + the same income drill-down (2 categories,
  the first with 1 sub + 1 item → the 364→481→535 arithmetic) on
  every run — both pins' expected values are the live-measured
  census values (db/custom.db carries the same seed).
- The existing pins are SAFE: the v41 F2/F3 pins are viewport-scoped
  (640/390 — the F1 pin re-asserts the same chrome at 1280, no
  conflict); the v50 F2 (640) + v53 F1 (390) tablist pins likewise;
  the v46 F2 pin's grid/card values at 1280 are re-asserted as the
  F1 controls (same values); the v44 F2b pin walks the expansion
  heights at 1280 (the F2 controls re-assert them); the v43 F3 sub/
  item pins are at 640 (the F2 pin is the 1280 viewport-scoped twin).
  networth-error.spec.ts + the add/delete round-trips untouched (the
  v60 pins are read-only).
- The chain gate: lint → typecheck → 108 unit → build → 259 e2e
  (**261** after: +2 — the v60 pins) → 35 smoke.
- Execution notes: `pkill -f agent-browser` before every
  agent-browser run; the with-server.sh boots fresh per command; the
  reference session EXPIRES between long eval gaps — re-login via
  the same eval before any follow-up census; the e2e-chunk file
  filter: pass FULL file paths (no regex alternation — the v58
  lesson); each mutation's rebuild is a SEPARATE command (the v53
  lesson).
- DEFERRED queue (unchanged, all need reference WRITES — out of
  bounds under the v46 read-only rule): the reference-side
  verify-email panel census, the forgot-confirm state census, the
  calculator EMPTY-state reference census (the reference's Rent
  carries a line item — an empty state would need a reference
  delete), the line-items dialog glyphs. The reference's
  trending-down glyph stays data-conditional (its net is positive —
  the 54th data census confirms "1 items · $25,000" unchanged).
- The v61 queue (suggestions): the QUICK-ACTION card surfaces' 1280
  pair (the v45 F3 hover-shadow pin is at 640; the quick-action row
  at 1280 unpaired), the BUDGET GUIDELINES card's 1280 pair (the v51
  F4 mobile census's desktop twin unpinned), the a11y surface's
  reference-side re-audit (the reference's own axe tree drifted since
  v38?), and the deferred reference-write censuses (unchanged).
