The workspace was reset — the repo needed a fresh clone. Cloned at main @
900bf8d (the v109 cycle shipped + its session logs [session_267 +
session_268]), re-establishing the full context from the v109 delivery
records + `docs/remediation-plan-v109.md` + the worklog Session 144 entry.

The queue is clear: **v110 targets the v104-era SAVINGS pair** (the probe
README's v110 queue agreeing with the rotation ledger — the SAVINGS view
at desktop 1280x800 FULL-PAGE, the pair's EIGHTH re-run [v58 → v65 → v74
→ v80 → v86 → v92 → v98 → v104 → v110]). The v104 probe header verified
before anything derived (the queue-prose verification lesson): the savings
surface + the SEVENTH bracket [v98 → v104] confirmed. Environment
provisioning started while studying the derivation patterns.

npm install completed in 17s — **the zod extraction INTACT this cycle**
(840/840 files, the v4/ subdirectory present — no npm ci needed, the
v108/v109 provisioning lesson checked proactively). `.env` written
(DATABASE_URL="file:../db/custom.db"), db/ seeded (db:generate +
db:push + db:seed), **seedcheck EXACT** (7 / 1850 / 2235 / 0 / 3 / 2 —
the persisted seedcheck script corrected to the schema's own field names
[category not name, ExpenseLineItem not LineItem] after two failures;
later consolidated: the canonical db-seedcheck-v68.cjs used for the
protocol steps, the ad-hoc script removed). chromium-1243 installed for
the pinned @playwright/test 1.63.0. The post-push commit audit clean
(4bfe5e3 + 900bf8d session-log-only — session_267.md + session_268.md,
zero src/ or lockfile deltas).

**F0 baseline FULLY GREEN** — lint · typecheck · 108/108 unit · build
(robots + sitemap prerendered) · **312 e2e** (81+81+78+75 = 315
executions across FOUR disjoint chunks, zero flakes on the FIRST run —
the per-file counts derived authoritatively via --list [312 in 24 files]
and summed against the authoritative total BEFORE any chunk ran) ·
35/35 smoke.

**THE NEW FINDING — npm audit added to the F0b audit for the first
time**: TWO advisories surfaced — **next 16.4.0 CRITICAL** (three
advisories published 2026-10-22: GHSA-2464-fhr4-w9xw the Image
Optimization API RCE with SVG files, GHSA-p3m5-59mp-jv5r the App Router
Server-Actions DoS, GHSA-673q-mjm6-r5xr the use-cache RCE — the
affected range 16.0.0–16.4.0, patched 16.4.1+) and **zod 4.6.5 HIGH**
(GHSA-mrhx-c7xc-m3w5, memory exhaustion validating oversized constrained
collections, patched 4.6.6+). The exposure audit run BEFORE any fix: the
app uses NO next/image, NO `use cache`, NO Server Actions (API route
handlers only) — all three Next.js paths UNEXPOSED in this codebase; zod
IS the input gate on every API route (register/login are PUBLIC +
zod-validated, rate-limited 10/IP/15min — the one real, bounded
exposure). The fix: `npm audit fix` — the standard minimal remediation
(next 16.4.0 → 16.4.3 + zod 4.6.5 → 4.6.7, both within the existing
caret ranges so **package.json is UNTOUCHED**, only the lockfile's 43
version pins moved — the 9 @next/swc platform binaries + @next/env in
lockstep). **npm audit: 0 vulnerabilities.** The quick gates re-run
green on the bumped tree (lint · typecheck · 108/108 unit · build with
the SEO pair prerendered) — and the decision made to run ALL subsequent
parity evidence (F2 clone half + F3 + F4 + F5) against the BUMPED tree
that actually ships.

**F1 the axe-core watch: NO DRIFT** — npm-latest 4.14.0 (only rc/next
sha prereleases beyond — 4.14.1-d1531a9.0.sha-d1531a9 +
4.14.1-55245d5.0.sha-55245d5 — no stable 4.14.1, no 5.x); the installed
wrapper + engine both 4.14.0; the v68 dedupe verified (exactly one
node_modules/axe-core entry); the engine-contract pin GREEN inside chunk
4's 75.

**F2 the 104th standing checks: ALL GREEN** — the pair derived from the
v103 pair via the persisted derive-standing-v110.py (the THREE token
families: 103rd→104th, ref103→ref104/clone103→clone104, v103→v104;
normalize-back diff clean, zero old tokens, bash -n clean both halves).
Reference side: all four bugs LIVE (toast-blocker `hitIsBurgerChild:false`;
sheet-trap `overlayCount:1` after nav; no-landmark `navLandmark:false`;
the 464px /networth overflow measured docSW 464 directly) + the data
census clean on the FIRST read (networth "1 items · $25,000" / income "1
items · $5000.00" / expenses "4 items · $525.00") + the SEO pair live.
Clone side — **RUN AGAINST THE BUMPED BUILD**: R1–R4 ALL GREEN — **the
mobile menu VERIFIED WORKING the 104th consecutive time** (the sheet
opens, closes on nav, the nav landmark present — the Tailwind v4
mitigation holds), zero overflow at 390 on all five views, the SEO pair
live; the seedcheck exact after the clone half.

**F3 the re-run pair** — the probe series derived from the v104 lineage
via the persisted derive-v110-series.py: the generic swaps + the NINE
exact-fragment history corrections (the plan-source fragment's
"the"-less form — `v103 plan's` NOT `the v103 plan's`, the "the" sits at
the END of the preceding line — a live derivation discovery on the first
run; the era marker v98-era→v104-era; last-re-shot v98→v104;
SEVENTH→EIGHTH; the bracket extension [v58 → … → v98 → v104 → v110];
the oldest-remaining bracket [v104 < v105 < … < v109];
TWENTY-SEVENTH→THIRTY-THIRD; the queue source v103 plan → v109 plan) —
9/9 corrections verified applied on the FIRST run (11 hit-checks), zero
residual correctable fragments, line-count preservation on all four
(49/41/38/261), bash -n + node --check clean. The census BUILT two-half
from the start: the builder itself derived via the persisted
derive-build-twohalf-v110.py — **the swap-order lesson applied** (the
generic version swap FIRST, the lineage-note fixups LAST so no later
swap re-touches the inserted tokens; the FIRST attempt failed its
normalize-back on exactly this); build-twohalf-v110.py produced
ref-arbit-v110.sh + clone-arbit-v110.sh with the ONE census JS block
(SV_CENSUS_JS 153 lines, md5 **891ab9b6**) byte-identical across the
halves — the v98/v104 census block VERBATIM, the builder-form md5
verified against the EXISTING v104 halves. The reaping budget between
the halves; one zombie-chromium cleanup before the clone half (the
documented v109 session-log form: 66 stale chrome processes killed after
the clone half's agent-browser calls failed silently — the eval
returned empty with the errors suppressed; the cleanup restored
everything on the re-run). Login on the first attempt both sides; the
parked pointer at (5,5); read-only — the v46 rule holds.

**The verdict: SAVINGS DIFFERENT** — the pair's documented flag-set
class (v104/v98 read DIFFERENT) with every flag DOM-arbitrated: the
card-footer payment chips the **v57 DATA-CONDITIONAL class** (the
census: ref footer childCount 1 [date-only] vs clone 2 with the
"Brokerage" chip — the reference RENDERS payment chips when data carries
them; its savings item simply ships none); the card grid 1-vs-2 the
seed-count class (the reference's 1 savings item vs the clone's 2-item
dev seed); the header stats + card contents the seed-data classes; the
avatar the user-identity class; **NO FAB flag raised this cycle** (the
disproof not required — the standing disproof form stays documented from
v97/v103/v108/v109). The both-sides census REPRODUCES the v104 census
values EXACTLY — zero drift on every axis (the brand h1; the grid + card
{w 960/gap 16/the 3-col 309.328px family}; the card h 200-vs-230 the
v57/v70b Recurring-wrap class [the badgeRow h 22 vs 52]; the titleRow
{flex/gap 8/center/h 24/the savings-blue dot}; the amount {24px/700/32px/
rgb(59,126,161)}; the footer + badge chrome byte-identical; the docSW
1280 guards) — **NO NEW CLONE GAP**.

**F4 the family-extension survey** — mapping the never-pinned families:
the savings-header interior analyzed and REJECTED (the only unpinned
axis, the left block's gap, lives in the SHARED items-view.tsx line whose
mutation would cascade the v109 income/expenses pins — the
single-axis-AND-single-spec rule); the action-row family already pinned
(v45 F1b); the savings filter card already pinned (v92); the goal-card
subtitle already pinned (v71 at 390, the mutation cascades). The winning
candidate: **the rail's NAV-BLOCK INTERIOR at 1280** — the block BETWEEN
the v104-pinned brand-block (above) and the v103-pinned user-footer
(below); the family every full-page shot walks past. The coverage map:
the session-5 pins hold the link BOX on links[0] only + the
class-string hovers; the v8 G2a pin the inactive color; the v36 S3 bands
the y positions; the glyph-parity spec the icons' PATH data ONLY —
NEVER pinned at ANY viewport in ANY spec: the "Navigation" label's
computed chrome, the UL's flex family, the LI's box, the nav ICON's
computed w/h, the label SPAN's truncate family, and the desktop ACTIVE
link's computed chrome (the v10 pin holds the mobile sheet variant).

**The pin's own axes first measured byte-identical on BOTH sides** by
the one-shot both-sides census (nav-arbit-v110.sh — the header-arbit
one-shot pattern): the label {Navigation, h 32, fs 12px, fw 600,
uppercase, spacing 0.6px, rgb(45,90,74), pad 8px 12px, radius 6px,
flex/center} + the UL {flex/column/gap 4px/w 215/childCount 5} + the LI
{relative/mb 0px/h 36} + the link box {h 32/pad 10px 12px/columnGap 12px/
fs 14px/fw 400/radius 8px — the session-5 controls re-walked} + the icon
{w 16, h 16} + the span {14px/hidden/ellipsis/nowrap} + the active link
{Savings, the 135deg gradient rgb(45,90,74)→rgb(143,188,63), white,
fw 500, h 32} + the counts {5 links, 5 icons}. **The first census run
returned "no nav" on the reference — the no-landmark finder lesson**:
the reference renders NO nav element (its documented bug), so the finder
was rewalked STRUCTURALLY (the ul by its 5-anchor shape; the label by the
wrapper-sibling walk with the childless-uppercase-div fallback; the
active link by aria-current OR the gradient OR the text). The re-run:
every axis byte-identical both sides.

**The plan written + validated BEFORE the pin's execution**
(`docs/remediation-plan-v110.md` — the measured evidence in the
pre-execution validation section, the mutation target verified by reading
the source: sidebar.tsx:96 carries the ONLY `h-4 w-4` in the file; the
burger toggle's icon uses the `[&_svg]:size-4` arbitrary-variant form —
untouched by the line-number scoping).

**The pin executed** (tests/e2e/nav-geometry.spec.ts, the v110 describe
block): GREEN on the FIRST run (11/11 in the file; the authoritative
count now **313**). **The pin-sanity mutation**: `h-4 w-4` → `h-4 w-5`
at sidebar.tsx:96 (line-number-scoped) — after the standalone REBUILD,
ONLY the v110 pin red (10 green), the failure diff reading as the
icon.w axis ALONE ("w": 16 → 20; every sibling axis green — the label,
the ul, the li, the link box, the span, the active link; and the other
specs' pins stay green: the v36 S3 y-bands, the session-5 box, the v8
G2a color, the v103/v104 rail pins — cascade-free BY CONSTRUCTION, zero
specs assert the nav icons' computed w/h). Restored (git diff src/ = 0
lines), the standalone REBUILD via the full npm run build, post-restore
11/11 green.

**F5 the ship chain**: lint ✓ · typecheck ✓ · 108/108 unit ✓ · npm audit
0 vulnerabilities · **313 e2e zero flakes** (81+81+78+76 = 316 chunk
executions = 313 unique) · 35/35 smoke. The screenshots regenerated: 10/16
BYTE-IDENTICAL — **the bump produced ZERO visual drift** (all non-date
surfaces identical, including login, dashboard, mobile shots, drill-down)
— + SIX deltas ALL ARBITRATED: the four item-view date footers + the
details sheet's Date FactRow the **fresh-seed +1-day roll** (the
band-crop + VLM read [vlm-read-crops-v110.mjs]: "Oct 18" → "Oct 19",
"Oct 13" → "Oct 14", "October 14, 2026" → "October 15, 2026"); the
08-calculator + the 16-item-details y817-900 bands the **v105-documented
backdrop-blur scrim rounding drift** (maxDelta 1-2, zero glyphs — the
GPU blur compositing's capture-session variance, the v105 forensics'
own class; the 08 file has ZERO strong-diff pixels at all); **ZERO
structural bands** — the updated set committed (the v103/v105/v109
precedent). The dev-server evidence set re-captured + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the menu open with
all 5 links + the brand; the sheet closed post-nav; the dashboard clean
— the Budget Guidelines card absent from the viewport-only capture the
documented below-the-fold non-defect).

**THE PHANTOM-GLITCH DISPEL** (the cycle's tooling finding): while
deriving the dev-shots script, the v109 script's income-link locator
DISPLAYED as `aref*="income"]:visible` — the "v107 save glitch" form.
Empirical test: the displayed selector THROWS in Playwright ("Unknown
engine 'aref*'") — yet the v107/v108/v109 captures all succeeded. The
od-hexdump resolution: ALL committed dev scripts (v107/v108/v109) carry
the byte-correct `a[href*="income"]:visible` on disk — **the "save
glitch" never existed**; the perceived "[h" loss is a DISPLAY-layer
artifact (the tool-output pipeline eats the [h sequence — escape-sequence
filtering), and the v108/v109 comments describe fixing a phantom. Any
tool output showing a bracket-h sequence must be od-verified before
acting on it. The v110 script's comment documents the dispel.

The docs aligned D1–D7 (AGENTS.md the v110 paragraph · CLAUDE.md 313 +
the v110 clause · README.md counts + the v110 plan row ·
zero-balance_SKILL.md the Session 145 row + the state line · PAD v1.1.67
· the probe README's v110 section + the four new lessons [the
security-bump re-verification path, the phantom-glitch dispel, the
no-landmark finder rule, the swap-order rule] + the v111 queue);
`docs/remediation-plan-v110.md` + this record saved. The v110 probe
series + the 104th standing pair + the two-half builder + the one-shot
censuses persisted (derive-v110-series.py · derive-standing-v110.py ·
derive-build-twohalf-v110.py · build-twohalf-v110.py · nav-arbit-v110.sh
· vlm-read-crops-v110.mjs · ref-arbit-v110.sh + clone-arbit-v110.sh ·
ref-standing-v104.sh + standing-checks-v104.sh · vlm-shots-v110.sh +
clone-vlmshots-v110.sh + vlm-compare-v110.mjs + arbit-v110.sh). The
`.env.example` verified matching the codebase (untouched this cycle).

**The next cycle (v111) per the rotation ledger: the v105-era LOGIN +
CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at desktop
1280x800, last re-shot v105 — now the oldest remaining [v105 < v106 <
v107 < v108 < v109 < v110]; the pair's EIGHTH re-run bracket [v59 → v66
→ v75 → v81 → v87 → v93 → v99 → v105 → v111], to be verified against
vlm-shots-v105.sh's own header before the derivation.**
