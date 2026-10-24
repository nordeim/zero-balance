#!/usr/bin/env python3
"""D6 for the v115 cycle: insert the v115 section into the probe README
(immediately before the v114 section — the newest-first insertion point),
carrying THE POST-SWAP-FRAGMENT RULE lesson + the v116 queue. Idempotent."""
import sys

SECTION = """## The v115 cycle (the v109-era ITEMS pair's NINTH re-run — Session 150)

The re-run cadence's next-oldest candidate: the v109-era ITEMS pair (the
ITEMS view — INCOME + EXPENSES — at desktop 1280x800, FULL-PAGE, last
re-shot v109 — now the oldest remaining [v109 < v110 < v111 < v112 <
v113 < v114]; the pair's NINTH re-run bracket [v57 -> v64 -> v70 -> v79
-> v85 -> v91 -> v97 -> v103 -> v109 -> v115]; the THIRTY-EIGHTH
consecutive queue/ledger agreement — the surface names verified against
vlm-shots-v109.sh's own header BEFORE the derivation).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v114 environment did not persist; the repo
re-cloned from main @ 735f612). The v108 FRESH-CLONE lesson applied
END-TO-END: npm ci (run in the foreground — the v114 silent-death
lesson) with the zod extraction verified INTACT [840/840 files, the
src/v4 subdirectory present, verified BEFORE any gate]; .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root; db:push +
db:seed (7 items / 3 assets / 2 liabilities); BOTH v1243 playwright
binaries verified DIRECTLY (the fresh cache held only the OLD
chromium-1200 pair). The gates: seedcheck exact (7/1850/2235/0/3/2 —
the env -u DATABASE_URL discipline, the canonical db-seedcheck-v68.cjs;
an initial ad-hoc seedcheck script hit the PrismaClient CWD-resolution
trap and was replaced by the canonical form before any gate) · lint ·
typecheck · 108/108 unit · build (robots + sitemap prerendered) · 317
e2e zero flakes (84+77+77+82 = 320 executions = 317 unique — the a11y
file kept INSIDE chunk 4) · 35/35 smoke. F0b the npm-audit watch (the
standing step's SIXTH cycle): 0 vulnerabilities — the v110 bump holds.
F1 the axe watch: NO DRIFT (npm-latest 4.14.0; wrapper + engine 4.14.0;
the v68 dedupe verified live — one node_modules/axe-core entry).

**F2: the 109th standing checks ALL GREEN** — derived v108->v109
(derive-standing-v115.py, three token families, normalize-back clean).
Reference: the four bugs ALL live (toast-blocker; sheet-trap; no-
landmark; the 464px /networth overflow) + the data census clean on the
FIRST reads (no render-race hit this cycle) + the SEO pair live. Clone:
R1-R4 ALL GREEN — the mobile menu VERIFIED WORKING the 109TH
CONSECUTIVE TIME, zero overflow at 390 on all five views, the SEO pair
live; the seedcheck exact after the clone half.

**F3**: the series derived from the v109 lineage (derive-v115-series.py
— the generic swaps + the FIVE single-line-safe history corrections, 13
correction instances; ONE derivation REPAIR documented: the bracket-
extension fragment must be written against the POST-generic-swap state
— see the lesson below). The census BUILT two-half from the start
(build-twohalf-v115.py via derive-build-twohalf-v115.py with the
swap-order rule; the ONE census JS block [193 lines] byte-identical
across the halves — the md5 line-block contract [b55dcd29 — the
v97/v103/v109 census blocks VERBATIM, the block itself version-free]).

**The verdicts: INCOME IDENTICAL + EXPENSES DIFFERENT — the pair's
documented verdict split (the same split as v109; v103 read BOTH
DIFFERENT; the income side's documented flags were all-data classes,
so the IDENTICAL verdict this run is the cleaner outcome on the same
chrome — the VLM-verdict variation form, the v105 LOGIN-IDENTICAL
precedent)** — with every flag DOM-arbitrated to a documented class:
the expenses card-footer payment chips the v57 DATA-CONDITIONAL class,
census-proven live (the reference's OWN income card's footer reads
childCount 2 with the "Bank Account" chip + icon — the reference
RENDERS payment chips when data carries them; its expense items simply
ship no payment method — footer childCount 1 — while the clone's carry
them); the badge-arrangement wrap the v57 wrap/classification-VALUE
classes (the expenses badgeRow h ref 22 vs clone 52, badgeCount ref 3
vs clone 4 — the clone's "Recurring" superset chip + the wrap; the chip
CHROME byte-identical); the "Edit with Base44" FAB the platform-chrome
class DISPROVEN live (the one-shot both-sides census
base44-fab-arbit-v115.sh: fabCount 0 + bodyHasBase44 false on BOTH
sides at 1280 on /expenses — the v97/v103/v108/v109 standing disproof
form re-confirmed; a FAB flag WAS raised, so the disproof ran); the
avatar the user-identity class; the header stats + card contents the
seed-data classes. The both-sides census compared AXIS-BY-AXIS by the
persisted compare-v115-census.py (**187 axes: 163 identical + 24
documented-class deltas, ZERO new deltas** — the avatar chrome, the
grid/card/titleRow/amount/footer/badge0 chrome, the filter card on
BOTH variants, the page header row, the docSW 1280 guard all
byte-identical) REPRODUCES the v109 census values EXACTLY — **NO NEW
CLONE GAP.**

**F4 [PIN]**: the family-extension survey walked the items views'
surfaces with the V94-COLLISION criterion (a family is only viable when
the mutation can fail ONE spec) and found **the VIEWPORT-BAND family:
the ITEMS view's md-band state (768 <= w < 1024) — the band NO spec
pins on the items views** (the coverage map: the items views pinned
ONLY at 390 [v52] and 1280 [v45/v64/v91/v92/v109]; the v42 five-route
mid-viewport census sits at 640 — BELOW md, the 1-col state; NOTHING in
the 768-1023 band on ANY items view). The one-shot both-sides census
(mdband-arbit-v115.sh, /income at 800x600 — the finders structural:
the card-like-children grid walk [radius 12px + pad 20px], the
Add-button->row walk [the v109 finder], the search->card->inner-grid
walk): **EVERY chrome axis byte-identical** — the item grid's md state
{the 2-col template `232px 232px`, gap 16px} + the page header row's
md state {flex/row/space-between/center/gap 16px/mb 32px/h 60/
childCount 2} + the filter card's inner grid md state {4 tracks
`95.5px x4`, gap 16px, childCount 3} + the card box at the 2-col width
{w 232/pad 20px/radius 12px/border rgb(229,231,227)/bg white} + the
filter card {w 480, mb 24px} + docSW 800 (no overflow in the band); the
childCount (1 vs 2) the seed-count class and the card h (230 vs 246)
the v70b-decomposed class — both DATA axes deliberately left UNPINNED
(the v107 position-arithmetic discipline). **Pin GREEN on the first
run** (45 passed in items.spec.ts; the count now **318**). **Mutation
verified single-family**: md:grid-cols-2 -> md:grid-cols-1 at
items-view.tsx:262 line-scoped (the ONLY `grid grid-cols-1 gap-4
md:grid-cols-2 lg:grid-cols-3` line in the file; the expenses filter
card's own md:grid-cols-2 on line 175 a DIFFERENT line — untouched by
the full-string scoping) — ONLY the v115 pin red (44 green), the
failure diff reading as the grid-template family axis ALONE
(`232px 232px` -> `480px`) after the standalone REBUILD; the 390/640
states structurally immune (grid-cols-1 base), the >=1024 states
structurally immune (lg:grid-cols-3 overrides md — the v45 1280 pin
green under the mutation), the header row's md:flex-row + the filter
card's md:grid-cols-4 separate tokens — untouched. Restored (git diff
src/ = 0), rebuilt, post-restore 45/45 green.

**F5 the ship chain**: lint · typecheck · 108 unit · 0 vulnerabilities ·
**318 e2e zero flakes** (84+78+77+82 = 321 executions = 318 unique) ·
35/35 smoke · the screenshots 16/16 byte-identical (the same-day-seed
law) · the dev evidence 4/4 byte-identical + re-captured + VLM-verified
(the menu proof: /income, docSW 390, navLandmark true; the menu open
with all 5 links + the brand; the sheet closed post-nav; the dashboard
clean — the dev-shots scripts derived v114->v115 with the
version-swap-only verification).

- THE POST-SWAP-FRAGMENT RULE (the derivation lesson, formalized): a
  history-correction fragment containing the CURRENT cycle's version
  token must be written against the POST-generic-swap state, not the
  pre-swap source form — the generic swap consumes the version token
  FIRST (v109 -> v115), so a correction written against the source
  (e.g. `-> v97 -> v103 -> v109]`) finds ZERO matches and the bracket
  silently loses its newest entry. The v115 run's first pass produced
  `[v57 -> ... -> v103 -> v115]` (the v109 entry MISSING) — caught by
  reading the derived header BEFORE proceeding, repaired by targeting
  the post-swap form (`-> v97 -> v103 -> v115]` -> `-> v97 -> v103 ->
  v109 -> v115]`). The v114 derivation's own precedent (its bracket
  correction targeted the already-swapped `v96 -> v102 -> v114])` form)
  now formalized as a rule: every correction's old-fragment must be
  checked against the file state AS THE CORRECTIONS SEE IT (after the
  generic swaps), and the residual check must include the corrected
  bracket's full expected form.

The v116 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v109-era ITEMS pair (the v110-era SAVINGS pair — the SAVINGS
view at desktop 1280x800, FULL-PAGE, last re-shot v110 — now the oldest
remaining [v110 < v111 < v112 < v113 < v114 < v115]; the pair's NINTH
re-run bracket [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> v104
-> v110 -> v116] to be verified against vlm-shots-v110.sh's own header
before the derivation), (2) the axe-core watch at its next re-check
point (only a 5.x wrapper changes the calculus), (3) the npm-audit
watch at its re-check point (only a new advisory in the next/zod
ranges changes the calculus), (4) the deferred reference-write censuses
(unchanged — out of bounds under the v46 read-only rule).

"""

path = "scripts/parity-probes/README.md"
t = open(path, encoding="utf-8").read()
anchor = "## The v114 cycle (the v108-era MOBILE TWINS pair's EIGHTH re-run — Session 149)"
if "## The v115 cycle (the v109-era ITEMS pair's NINTH re-run" in t:
    print("ALREADY APPLIED: the v115 cycle section")
    sys.exit(1)
if t.count(anchor) != 1:
    print(f"MISS/AMBIGUOUS: the v114 section anchor ({t.count(anchor)} hits)")
    sys.exit(1)
t = t.replace(anchor, SECTION + anchor, 1)
open(path, "w", encoding="utf-8").write(t)
print("aligned the probe README (the v115 cycle section + the POST-SWAP-FRAGMENT lesson + the v116 queue)")
