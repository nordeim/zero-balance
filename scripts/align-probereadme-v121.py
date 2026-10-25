#!/usr/bin/env python3
"""D6 docs alignment for the v121 cycle — the probe README's v121 section
(inserted newest-first, before the v120 section) carrying the v122 queue.
Insert-after WITH the idempotency guard (the v113 lesson)."""
import sys

README = "scripts/parity-probes/README.md"
t = open(README, encoding="utf-8").read()

SECTION = """## The v121 cycle (the v115-era ITEMS pair's TENTH re-run — Session 156)

The re-run cadence's next-oldest candidate: the v115-era ITEMS pair —
the ITEMS view (income + expenses) at desktop 1280x800 FULL-PAGE, the
v57-era items pair's surface family, last re-shot v115 — now the oldest
remaining [v115 < v116 < v117 < v118 < v119 < v120]; the pair's TENTH
re-run bracket [v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97 -> v103
-> v109 -> v115 -> v121]; the FORTY-FOURTH consecutive queue/ledger
agreement — the surface names verified against vlm-shots-v115.sh's own
header BEFORE the derivation, with the v115 header's own NINTH ordinal
CONSISTENT with its 10-entry bracket [v57 the original — no off-by-one
this lineage]. **A PIN-ONLY cycle for src/ — zero production-code
changes** + one e2e pin; the cycle's standing items: the axe watch (NO
DRIFT — 4.14.0 holds, only the canary sha prerelease beyond, the v68
dedupe verified), the npm-audit watch at its twelfth re-check (0
vulnerabilities — the v110 bump holds [next 16.4.3 + zod 4.6.7]), the
115th standing checks (ALL GREEN — the mobile menu the 115th
consecutive green; the reference's four bugs all live; the data census
clean on the FIRST reads, no render-race hit this cycle).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v120 environment did not persist; the repo
re-cloned from main @ 19d6d1f; the v108 FRESH-CLONE provisioning
end-to-end: npm ci in the foreground, the zod extraction verified
intact, BOTH v1243 playwright pairs installed with
INSTALLATION_COMPLETE verified, the explicit-env-prefix Prisma
discipline [the v119 workspace-root .env discovery], the seedcheck
exact before any gate). The gates: lint · typecheck · 108/108 unit ·
build (robots + sitemap prerendered) · **323 e2e ZERO FLAKES**
(87+80+77+82 = 326 executions = 323 unique, every chunk green on its
FIRST run) · 35/35 smoke. The post-push commits audited
session-log-only.

**F2 the 115th standing checks ALL GREEN** (the pair derived from the
v114 pair via the persisted derive-standing-v121.py — three token
families, normalize-back diff clean, zero old tokens): the reference's
four bugs all live [toast-blocker hitIsBurgerChild:false; sheet-trap
overlayCount:1 after nav; no-landmark navLandmark:false; the 464px
/networth overflow measured docSW 464 directly]; the data census clean
on the FIRST reads; the SEO pair live both sides; the clone's mobile
menu VERIFIED WORKING the 115th consecutive time (zero overflow at 390
on all five views); the seedcheck exact after the clone half.

**F3 the re-run pair**: the probe series derived from the v115 lineage
(the persisted derive-v121-series.py — the generic swaps + FIVE
exact-fragment history corrections [last-re-shot v109->v115, the
ordinal NINTH->TENTH, the bracket extension -> v109 -> v115 -> v121,
the later-pairs list re-pointed, the re-shot era], 5/5 applied on the
FIRST run, 12 instances, line counts preserved 57/49/50/285); the
census BUILT two-half from the start (build-twohalf-v121.py —
ref-arbit-v121.sh + clone-arbit-v121.sh, the ONE census JS block
[CENSUS_JS 193 lines] byte-identical across the halves, the md5
line-block contract [b55dcd29 — the v97/v103/v109/v115 census blocks
VERBATIM]; the STALE clonearbit109 SESSION TOKEN in the v115 builder's
clone_login FIXED to clonearbit121 in this lineage — the same quirk
class as the v114 builder's clonearbit108 fixed in the v120 lineage).
**The verdict pass 1 BOTH PAIRS DIFFERENT / pass 2 INCOME IDENTICAL +
EXPENSES DIFFERENT — the pair's documented verdict classes (the same
split as v109/v115; v103 read BOTH DIFFERENT; the income side's
documented flags all-data classes, so the IDENTICAL verdict on pass 2
the cleaner outcome on the same chrome — the VLM-verdict variation
form, the v105 LOGIN-IDENTICAL precedent)** — every flag
DOM-arbitrated: the payment chips the v57 DATA-CONDITIONAL class (the
reference's own income card footer childCount 2 with the Bank Account
chip — it RENDERS payment chips when data carries them); the badge
wrap the v57 wrap/classification-VALUE classes (badgeRow h 22-vs-52,
badgeCount 3-vs-4 — the Recurring superset chip + the wrap, the chip
chrome byte-identical); the "Edit with Base44" widget the
platform-chrome class DISPROVEN LIVE (the INVERTED reading this cycle
— the VLM claimed the widget present in the CLONE: base44-fab-arbit-
v121.sh measured fabCount 0 + bodyHasBase44 false on BOTH sides at
1280 /expenses — the overlay lives in the reference's platform iframe
chrome); the avatar the user-identity class; the figures the seed-data
classes. The both-sides census compared AXIS-BY-AXIS by the persisted
compare-v121-census.py: **187 axes — 163 identical + 24
documented-class deltas, ZERO new** (the v115 values reproduced
EXACTLY, the same 187/163/24 split — the avatar chrome, the grid +
card chrome [the 3-col 309.328px family], the titleRow, the amount
leaf, the footer + badge chrome, the filter card on BOTH variants,
the page-header family, the docSW 1280 guards). NO NEW CLONE GAP.

**F4 the pin — the ITEM-CARD's inline CONFIRM-BAR census at 1280 (the
never-pinned twin of the pinned family, PIN-ONLY — the v120
LIABILITY-TWIN precedent form)**: the FIRST candidate (the expenses
filter's md-band state at 800 — measured BYTE-IDENTICAL on both sides
by the one-shot census expband-arbit-v121.sh: the inner grid cols
207px 207px + the not-spanning search wrapper w 207 + the 3 comboboxes
207/36/14px + the card 480/138/mb 24 + the docSW 800, both census JSON
lines the IDENTICAL string) **REJECTED by the LIVE SOLE-FAILURE TEST**
(the v116 first-attempt precedent, the SPEC-ALIAS COVERAGE lesson
re-hit: the v1-era items.spec.ts:622 asserts the RAW `md:grid-cols-2`
CLASS TOKEN itself — the line-175 mutation reds both the new pin AND
the old spec; the re-scope analysis found NO alternative sole-failure
axis on the family: the gap-4 token -> the v70 pin's innerGrid.gap at
1280, the lg:grid-cols-4 token -> the 622 token + the v70 cols, the
wrapper col-span -> the v70 searchW, the shared card lines -> the
v64/v70/v115 pins). The candidate the ITEM-CARD's inline confirm bar
(the income/savings cards' "Delete this item?" bar): the confirm-bar
FAMILY pinned ONLY on the /networth instances (the v46 F3 pin — the
asset card's bar), the ITEM-CARD instance held by NO spec (every
existing confirm-bar assertion in the items specs BEHAVIORAL only —
the text visibility, the click paths, the failed-delete toast); the
reference has NO confirm bars at all (its card-menu Delete destroys
immediately — its R6 bug), so no both-sides census is possible (the
v46 F3 adapted form); the family chrome = the v46 F3 contract BY
CONSTRUCTION (the identical class strings: item-card.tsx:210 <->
net-worth-view.tsx:124/235). The one-shot clone census
(confirmbar-arbit-v121.sh — the full PointerEvent/MouseEvent sequence
for the Radix menu [the v120 TAB-SWITCH lesson applied to the
dropdown], the FIXTURE-RESTORE Cancel — the delete never fired, the
card restored to its at-rest 230) measured: the bar {mt 16px / display
flex / align center / justify space-between / radius 8px / pad 12px /
bg rgb(254,242,242) / w 267 — the pinned card 309 - the 40 p-5 - the
2px border}, the label {fs 14px / fw 400 / the item-card-only text
"Delete this item?"}, the cancelPill {bg white / pad 4px 12px /
radius 6px / fs 12px / fw 500 / h 24 / the shadow-sm VISIBLE layer
rgba(0,0,0,0.05) 0px 1px 2px 0px — the regression net's SIXTH site},
the deleteBtn {color white / pad 4px 12px / radius 6px / fs 12px /
fw 500 / h 24}, the BAR-OPEN DELTA +80 (the at-rest 230 -> the
bar-open 310 = the mt 16 + the bar 64, THE ARITHMETIC EXACT — the
data-independent chrome delta); the colors (the label red-700 / the
delete bg red-600) deliberately NOT asserted (the lab() named-palette
drift — the v46 F3 family form, the engine-independence discipline).
The +1 e2e pin (tests/e2e/items.spec.ts, appended by the persisted
append-pin-v121.py): the confirm-bar census at 1280 — the family + the
delta + the fixture-restore Cancel, the finders STRUCTURAL (the v46 F3
finder family: the bg + the Cancel/Delete button pair); the PIN-ONLY
form (the standalone GREEN 47/47 — the first run's 622 red the STALE
mutated standalone, the v98 REBUILD discipline + THE PIN-SANITY
MUTATION [item-card.tsx:210 the bar's p-3 -> p-4, LINE-SCOPED — the
SOLE FAILURE VERIFIED LIVE: the v121 pin ALONE red, bar.pad 12px ->
16px the primary axis + the co-moving delta 80 -> 88, the full items +
networth run 81 GREEN including the v46 F3 networth twin — the
different-file immunity verified live; restored + the full rebuild +
the 47/47 post-restore regression]).

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**324 e2e zero flakes** (87+81+77+82 = 327 executions = 324 unique) ·
35/35 smoke. **The screenshots 16/16 byte-IDENTICAL (the same-day-seed
law — the seed and the capture ran the same day, the relative dates
matching)**; the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the menu open with
all 5 links + the brand; the sheet closed post-nav; the dashboard
clean — the dev-shots scripts derived v120->v121 with the
version-swap-only verification).

The v122 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v115-era ITEMS pair (the v116-era SAVINGS pair — the SAVINGS
view at desktop 1280x800 FULL-PAGE, the v58-era savings pair's surface
family, last re-shot v116 — now the oldest remaining [v116 < v117 <
v118 < v119 < v120 < v121]; the pair's TENTH re-run bracket [v58 -> v65
-> v74 -> v80 -> v86 -> v92 -> v98 -> v104 -> v110 -> v116 -> v122] to
be verified against vlm-shots-v116.sh's own header before the
derivation — the v116 header's own NINTH ordinal should be consistent
with its 10-entry bracket [v58 the original], so v122 = the TENTH
re-run by the same convention), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
npm-audit watch at its re-check point (only a new advisory in the
next/zod ranges changes the calculus), (4) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).

"""

if "## The v121 cycle" in t:
    print("ALREADY APPLIED: the v121 section — skipped")
    sys.exit(0)
anchor = "## The v120 cycle (the v114-era MOBILE TWINS pair's NINTH re-run — Session 155)"
if t.count(anchor) != 1:
    print(f"AMBIGUOUS/MISS anchor ({t.count(anchor)} hits)")
    sys.exit(1)
t = t.replace(anchor, SECTION + anchor, 1)
open(README, "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (the v121 section + the v122 queue)")
