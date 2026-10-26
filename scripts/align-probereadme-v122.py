#!/usr/bin/env python3
"""D6 docs alignment for the v122 cycle — the probe README's v122 section
(inserted newest-first, before the v121 section) carrying the v123 queue.
Insert-after WITH the idempotency guard (the v113 lesson)."""
import sys

README = "scripts/parity-probes/README.md"
t = open(README, encoding="utf-8").read()

SECTION = """## The v122 cycle (the v116-era SAVINGS pair's TENTH re-run — Session 157)

The re-run cadence's next-oldest candidate: the v116-era SAVINGS pair —
the SAVINGS view at desktop 1280x800 FULL-PAGE, the v58-era savings
pair's surface family, last re-shot v116 — now the oldest remaining
[v116 < v117 < v118 < v119 < v120 < v121]; the pair's TENTH re-run
bracket [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> v104 -> v110
-> v116 -> v122]; the FORTY-FIFTH consecutive queue/ledger agreement —
the surface names verified against vlm-shots-v116.sh's own header
BEFORE the derivation, with the v116 header's own NINTH ordinal
CONSISTENT with its 10-entry bracket [v58 the original — no off-by-one
this lineage]. **A PIN-ONLY cycle for src/ — zero production-code
changes** + one e2e pin + ONE tests-only spec repair (the cycle's
baseline find); the cycle's standing items: the axe watch (NO DRIFT —
4.14.0 holds, only the canary sha prerelease beyond, the v68 dedupe
verified), the npm-audit watch at its thirteenth re-check (0
vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]), the
116th standing checks (ALL GREEN — the mobile menu the 116th
consecutive green; the reference's four bugs all live; the data census
clean on the FIRST reads, no render-race hit this cycle).

**F0 baseline: ONE LIVE RED on the first chunk — THE v120 PIN'S
DATE-AXIS TIME-BOMB, repaired tests-only (the cycle's baseline find)**:
the chunk-1 run (dashboard + networth + networth-error) failed the
v120 liability-card pin at its third facts row — `txt: "Updated Oct 25,
2026"` expected vs `"Oct 26, 2026"` received. THE MECHANISM:
prisma/seed.ts stamps the liabilities' `lastUpdated: isoDate(0)` —
TODAY at seed time — and net-worth-view.tsx renders it via
toLocaleDateString; the e2e global-setup re-seeds db/e2e.db on EVERY
run, so the rendered text is always the RUN DAY. The v120 cycle
authored the pin with the LITERAL date string — green on its own seed
day (2026-10-25, both the v120 and v121 cycles shipping before the UTC
rollover), red every day after: a TIME-BOMB AXIS, the same-day-seed
law's spec-side blind spot (the screenshots side has honored the law
since v77; the e2e side never hit it because every prior run happened
same-day). It is the ONLY literal-date assertion in the suite. THE
REPAIR (TDD — the live red IS the red phase): the axis computed from
the seed's own rule — `new Date().toLocaleDateString("en-US", {month:
"short", day: "numeric", year: "numeric"})` in the spec process (the
same TZ class as the seed and the rendered page), the row asserted as
the template `Updated ${seedDay}` (the midnight-crossing window
accepted per the law); the full networth file 36/36 green after the
repair; the mutation proof inherent (the axis red when the underlying
value rolled a day). The rest of the baseline FULLY GREEN on the
FRESH-CLONE-PROVISIONED workspace (the RESET class — the v121
environment did not persist; the repo re-cloned from main @ 075df6d;
the v108 FRESH-CLONE provisioning end-to-end: npm ci in the foreground
[354 entries], the zod extraction verified intact, BOTH v1243
playwright pairs installed with INSTALLATION_COMPLETE verified, the
explicit-env-prefix Prisma discipline, the seedcheck exact before any
gate). The gates: lint · typecheck · 108/108 unit · build (robots +
sitemap prerendered) · **324 e2e ZERO FLAKES after the repair**
(87+81+77+82 = 327 executions = 324 unique, every chunk green on its
FIRST run) · 35/35 smoke. The post-push commits audited
session-log-only.

**F2 the 116th standing checks ALL GREEN** (the pair derived from the
v115 pair via the persisted derive-standing-v122.py — three token
families, normalize-back diff clean, zero old tokens): the reference's
four bugs all live [toast-blocker hitIsBurgerChild:false; sheet-trap
overlayCount:1 after nav; no-landmark navLandmark:false; the 464px
/networth overflow measured docSW 464 directly]; the data census clean
on the FIRST reads; the SEO pair live both sides; the clone's mobile
menu VERIFIED WORKING the 116th consecutive time (zero overflow at 390
on all five views); the seedcheck exact after the clone half.

**F3 the re-run pair**: the probe series derived from the v116 lineage
(the persisted derive-v122-series.py — the generic swaps + EIGHT
exact-fragment history corrections [the era re-pointed v110-era ->
v116-era, last-re-shot v110 -> v116, the oldest-remaining list
re-pointed, NINTH -> TENTH, the plan attribution v115 plan's -> v121
plan's, THIRTY-NINTH -> FORTY-FIFTH, the bracket extension], 8/8
families applied on the FIRST run, 19 instances, line counts preserved
50/42/39/262); the census BUILT two-half from the start
(build-twohalf-v122.py — ref-arbit-v122.sh + clone-arbit-v122.sh, the
ONE census JS block [SV_CENSUS_JS 153 lines] byte-identical across the
halves, the md5 line-block contract [891ab9b6 — the v104/v110/v116
census blocks VERBATIM]; the STALE refarbit116 SESSION TOKEN in the
builder's ref_exec assertion FIXED to refarbit122 — the no-'v'-prefix
bare token the generic swap cannot touch, the v116 lineage's own
documented repair class); the comparator derived
(derive-compare-v122.py -> compare-v122-census.py — the census-era
corrections, the provenance citations re-pointed at the v116
measurement). **The verdict pass 1 IDENTICAL / pass 2 DIFFERENT — the
pair's VLM-verdict VARIATION form (the documented class: v98/v104/v110/
v116 read DIFFERENT; the IDENTICAL pass the cleaner all-data-classes
outcome — the v105 LOGIN-IDENTICAL + the v121 pass-2 INCOME-IDENTICAL
precedents)** — every pass-2 flag DOM-arbitrated: the card-grid the
SEED-COUNT class (grid.childCount 1-vs-2, the template/gap/w
byte-identical, the card w 309 both sides); the footer content the v58
DATA-CONDITIONAL class (the reference's savings item ships no
paymentMethod — the date-only DIV, childCount 1 — while the clone's
render the SPAN pair, the same two-child structure the reference's own
income card renders); the badge styles the classification-VALUE + v57
wrap/SUPERSET-CHIP classes (badges[0] need-red vs savings-green,
badges[2] active-slate vs Recurring-green-iconed; badgeRow h 22-vs-52
+ n 3-vs-4 — the Recurring superset chip + the wrap; the per-badge
chrome byte-identical); the avatar the user-identity class; the figures
the seed-data classes. The both-sides census compared AXIS-BY-AXIS by
the persisted compare-v122-census.py: **120 axes — 80 identical + 40
documented-class deltas, ZERO new** (the v116 values reproduced
EXACTLY, the same 120/80/40 split). NO NEW CLONE GAP.

**F4 the pin — the SAVINGS goal-card kebab-trigger's OPEN-MENU reveal
census at 1280 (the never-pinned PATH of the pinned reveal family,
PIN-ONLY — +1 e2e = 325)**: the trigger's reveal has THREE paths — the
HOVER path (group-hover:opacity-100, pinned by the v116 pin), the
KEYBOARD path (focus-visible:opacity-100, pinned by the v36 S3
Tab-order census), and the OPEN path (data-[state=open]:opacity-100 —
superset fix #7's "stays revealed while its menu is open" clause) —
the OPEN path held by NO spec (the v98 pin opens the menu but
censuses the PANEL + menuitem interior only; the behavioral specs
never read the trigger's opacity). The CLONE-ONLY form (the v46 F3
adapted precedent): the reference's trigger stays INVISIBLE (opacity
0) when its menu is opened (its own superset-#7 bug) and a
reference-side measurement would require a CLICK (the v46 read-only
rule: passive navigation + real pointer hover only) — the pin locks
the CLONE's own superset chrome; the family chrome = the v116 pinned
contract BY CONSTRUCTION (the identical class string: item-card.tsx:
139). The one-shot census (kebabopen-arbit-v122.sh — the
REVEAL-LADDER form: at-rest 0 -> hover 1 -> open+parked 1 [THE AXIS]
-> dismissed; the synthetic PointerEvent/MouseEvent sequence does NOT
move the real pointer, so the group-hover path stays disengaged
through the open read, isolating the data-[state=open] token; the
dynamic card-center read in the v116 plain 'x,y' convention — the
JSON form's escaped quotes break the shell-side extraction) measured:
the open+parked state {opacity "1" / dataState "open" / the box chrome
unchanged 36x36 / radius 6px / bg transparent / color rgb(10,10,10) /
cardTop 21 / cardRight 21} — with the REAL pointer parked at (5,5),
the data-[state=open] token ALONE holding the reveal. TWO
census-world artifacts documented (the synthetic-pointerdown
focus-return leaves Chromium's focus-visible heuristic in keyboard
mode — the post-restore trigger reads the v36 keyboard-path "1", not
the at-rest "0"; the restore read asserts the DISMISSED state only).
THE PIN'S LIVE-RED DISCOVERY (documented in the spec comment):
getByRole(name) is UNRESOLVABLE mid-open — Radix's modal layer marks
the app aria-hidden, EXCLUDING the trigger from the accessibility
tree — the STRUCTURAL aria-label CSS finder the fix (the v72
discipline). The +1 e2e pin (tests/e2e/items.spec.ts, appended by the
persisted append-pin-v122.py): the open+parked reveal census at 1280 —
the at-rest baseline + the axis + the unchanged box chrome + the
fixture-restore Escape (the v98 form; no menuitem ever clicked — the
data never touched). The pin-sanity mutation (item-card.tsx:139
line-scoped data-[state=open]:opacity-100 -> opacity-90; the
net-worth-view.tsx:82/192 family twins untouched by the file+line
scoping): the SOLE FAILURE verified live — the pin ALONE red at the
opacity axis ("1" -> "0.9"), the full items run 47 others green (the
v116 hover-path / v36 keyboard / v98 panel / v121 confirm-bar / v45
at-rest pins all immune); restored + the full rebuild (the v98
REBUILD discipline) + the 48/48 post-restore regression + the networth
kebab twins green (the different-file immunity).

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**325 e2e zero flakes** (87+82+77+82 = 328 executions = 325 unique) ·
35/35 smoke. **The screenshots 7/16 regenerated — the DAY-ROLLOVER
REFRESH (the same-day-seed law's expected consequence: the committed
set was same-day with the Oct 25 seed, the re-capture same-day with
the Oct 26 seed — the date-only diffs VLM-verified [the card footers'
Updated dates Oct 17->18 / Oct 18->19], ZERO chrome drift, the other 9
byte-identical)**; the dev evidence 4/4 captured + VLM-verified (3
byte-identical + dev-mobile-income-390 the date-only refresh; the menu
proof: /income, docSW 390, navLandmark true; the menu open with all 5
links + the brand; the sheet closed post-nav; the dashboard clean —
the dev-shots scripts derived v121->v122 with the version-swap-only
verification).

The v123 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v116-era SAVINGS pair (the v117-era LOGIN + CALCULATOR pair —
the LOGIN page + the CALCULATOR dialog at desktop 1280x800, the
v59-era pair's surface family, last re-shot v117 — now the oldest
remaining [v117 < v118 < v119 < v120 < v121 < v122]; the pair's TENTH
re-run bracket [v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 -> v105
-> v111 -> v117 -> v123] to be verified against vlm-shots-v117.sh's
own header before the derivation — the v117 header's own NINTH ordinal
should be consistent with its 10-entry bracket [v59 the original], so
v123 = the TENTH re-run by the same convention), (2) the axe-core
watch at its next re-check point (only a 5.x wrapper changes the
calculus), (3) the npm-audit watch at its re-check point (only a new
advisory in the next/zod ranges changes the calculus), (4) the
deferred reference-write censuses (unchanged — out of bounds under the
v46 read-only rule).

"""

if "## The v122 cycle" in t:
    print("ALREADY APPLIED: the v122 section — skipped")
    sys.exit(0)
anchor = "## The v121 cycle (the v115-era ITEMS pair's TENTH re-run — Session 156)"
if t.count(anchor) != 1:
    print(f"AMBIGUOUS/MISS anchor ({t.count(anchor)} hits)")
    sys.exit(1)
t = t.replace(anchor, SECTION + anchor, 1)
open(README, "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (the v122 section + the v123 queue)")
