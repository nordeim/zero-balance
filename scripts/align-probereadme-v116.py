#!/usr/bin/env python3
"""D6 docs alignment for the v116 cycle — the probe README's v116 section
(inserted newest-first, before the v115 section) carrying THE SPEC-ALIAS
COVERAGE LESSON + THE STATIC-HOVER-COORDINATE TRAP and the v117 queue.
Insert-after WITH the idempotency guard (the v113 lesson)."""
import sys

README = "scripts/parity-probes/README.md"
t = open(README, encoding="utf-8").read()

SECTION = """## The v116 cycle (the v110-era SAVINGS pair's NINTH re-run — Session 151)

The re-run cadence's next-oldest candidate: the v110-era SAVINGS pair (the
SAVINGS view at desktop 1280x800, FULL-PAGE, last re-shot v110 — now the
oldest remaining [v110 < v111 < v112 < v113 < v114 < v115]; the pair's
NINTH re-run bracket [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 ->
v104 -> v110 -> v116]; the THIRTY-NINTH consecutive queue/ledger
agreement — the surface names verified against vlm-shots-v110.sh's own
header BEFORE the derivation). PIN-ONLY for src/; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, canary-only prereleases
beyond, the v68 dedupe verified), the npm-audit watch at its seventh
re-check (0 vulnerabilities — the v110 bump holds [next 16.4.3 + zod
4.6.7]), the 110th standing checks (ALL GREEN — the mobile menu the
110th consecutive green; the reference's four bugs all live; the data
census clean on the FIRST reads, no render-race hit this cycle).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v115 environment did not persist; the repo
re-cloned from main @ 3e1c2e8). The v108 FRESH-CLONE lesson applied
END-TO-END: npm ci (run in the foreground — the v114 silent-death
lesson; 354 entries) with the zod extraction verified INTACT [840/840
files, the src/v4 subdirectory present, verified BEFORE any gate]; .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root; db:push +
db:seed (7 items / 3 assets / 2 liabilities); BOTH v1243 playwright
binaries verified DIRECTLY (the fresh cache held only the OLD
chromium-1200 pair). The gates: seedcheck exact (7/1850/2235/0/3/2) ·
lint · typecheck · 108/108 unit · build (robots + sitemap prerendered) ·
318 e2e zero flakes (84+78+77+82 = 321 executions = 318 unique — the
a11y file kept INSIDE chunk 4) · 35/35 smoke.

**F3**: the series derived from the v110 lineage (derive-v116-series.py
— the generic swaps + the EIGHT single-line-safe history corrections,
19 correction instances; ONE derivation REPAIR documented: the
plan-attribution fragment must target the line-internal BARE
"v109 plan's" form — the with-article form spans the v110 headers' line
break, the v107 line-break lesson's bare-form instance — see the lesson
below). The census BUILT two-half from the start (build-twohalf-v116.py
via derive-build-twohalf-v116.py with the swap-order rule; the ONE
census JS block [SV_CENSUS_JS 153 lines] byte-identical across the
halves — the md5 line-block contract [891ab9b6 — the v104/v110 census
blocks VERBATIM, the block itself version-free]; the builder's OWN
repair documented: the ref_exec startswith assertion's bare session
token [refarbit110 -> refarbit116] is a no-'v'-prefix token the generic
swap CANNOT touch — swapped explicitly this cycle, closing the v115
builder's clonearbit109 leftover counter-precedent). The verdict:
SAVINGS DIFFERENT — the pair's documented flag-set class (v104/v98/v110
read DIFFERENT) — every flag DOM-arbitrated (the payment chips the v57
DATA-CONDITIONAL class [the reference's savings item ships no
paymentMethod — its footer renders the date-only DIV, childCount 1;
the clone's render the SPAN pair, childCount 2]; the card grid the
seed-count class; the header stats + card contents the seed-data
classes; the avatar the user-identity class; NO FAB flag raised — the
disproof not required, the v103 standing class). The census compared
AXIS-BY-AXIS by the persisted compare-v116-census.py (120 axes: 80
identical + 40 documented-class deltas, ZERO new — the asymmetric
footer.children[1].*/badges[3].* families the DATA-CONDITIONAL and
superset-chip classes BY CONSTRUCTION) — NO NEW CLONE GAP.

**F4 [PIN]**: the savings goal-card's KEBAB TRIGGER census at 1280
(+1 e2e = 319). THE SPEC-ALIAS COVERAGE LESSON (the cycle's survey
finding — the V94-COLLISION criterion at its live form): the FIRST
mutation attempt (the h axis, h-9 w-9 -> h-10 w-9 at item-card.tsx:139)
failed the sole-failure test with TWO reds — the new pin AND the v45 F1a
pin, which holds the trigger's w 36 / h 36 / at-rest opacity "0" on
/income (items.spec.ts:1264-1266) — the SAME shared component line. The
coverage-map survey had missed it because it grepped the SOURCE token
forms (h-9 w-9, opacity-0, group-hover) instead of the SPECS' own alias:
the trigger's spec name is "kebab", a word that appears NOWHERE in the
source. THE RULES: (a) a coverage map for a shared-component family
must grep the spec-side ALIASES (the census variable names — "kebab",
"trigger", "actions") not just the source class tokens; (b) an axis held
in ANY view is held for EVERY view (the shared component renders them
all); (c) the resolution keeps the pin but re-scopes it to the axes NO
other spec holds — the at-rest {tag/display/radius/bg/color/cardTop/
cardRight} + the HOVER-path group-hover reveal {opacity "1"} (the
focus-path reveal is the tab-walk pin's sibling, never held) — with
the v45-held {w/h/at-rest-opacity} axes left OUT of the census return
value itself (a toEqual census whose return carries held axes would
re-collide); the FIRST mutation's two-red run kept as the collision
evidence (the v94 precedent). The final mutation: rounded-md ->
rounded-lg at item-card.tsx:139 line-scoped — only the v116 pin red at
the radius family axis alone ["6px" -> "8px"], the v45/tab-walk/v98/v80
pins structurally immune; restored, rebuilt, post-restore 46/46 green.

THE STATIC-HOVER-COORDINATE TRAP (the census-side lesson): the first
hover read's STATIC mouse move (640,300) missed the reference's ONLY
card — the reference's 1-item seed renders its Emergency Fund card in
grid COLUMN 1 (x 288-597), and x=640 lands on the column-gap
whitespace; the reference's trigger read hoverOpacity "0" (an apparent
REVEAL DIVERGENCE — the clone's column-2 card had caught the pointer
and read "1"). THE RULE: a hover-state census on seeded data must read
the target element's OWN bounding rect and move the pointer to the
element's OWN center — never a static viewport coordinate (the
reference's and the clone's layouts differ by the seed-count class,
and a static coordinate can land on either side of that boundary). One
more settle discipline: a hover-reveal pin must wait out the
transition-opacity window (~150ms) before reading (the v98 animate-in
settle precedent applied to the reveal — the first run read 0.033
mid-transition).

The ship: 319 e2e zero flakes across the auditable four-chunk split
(84+79+77+82 = 322 executions = 319 unique); 35/35 smoke; the
screenshots 20/20 byte-identical (the same-day-seed law — zero
arbitration); the dev evidence 4/4 byte-identical + VLM-verified (the
menu proof: /income, docSW 390, navLandmark true; the dev-shots scripts
derived v115->v116 with the version-swap-only verification).

"""

if "## The v116 cycle" in t:
    print("ALREADY APPLIED: the v116 section — skipped")
    sys.exit(0)
anchor = "## The v115 cycle (the v109-era ITEMS pair's NINTH re-run — Session 150)"
if t.count(anchor) != 1:
    print(f"AMBIGUOUS/MISS anchor ({t.count(anchor)} hits)")
    sys.exit(1)
t = t.replace(anchor, SECTION + anchor, 1)
open(README, "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (the v116 section)")
