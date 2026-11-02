#!/usr/bin/env python3
"""D6 — the probe README alignment for the v147 cycle: insert the v147
section (Session 182) between the v147 queue's end and '## The v138 cycle'
(each cycle section ends with the NEXT cycle's queue — the v146 section's
tail IS the v147 queue; the new v147 section carries the v148 queue)."""
import io
import sys

PATH = "scripts/parity-probes/README.md"

SECTION = """## The v147 cycle (the v141-era LOGIN + CALCULATOR pair's FOURTEENTH re-run — Session 182)

The re-run cadence's third-pass next-oldest candidate: the v141-era
LOGIN + CALCULATOR pair — the LOGIN view + the CALCULATOR dialog at
desktop 1280x800 (the v59-era login+calc pair's surface family), last
re-shot v141 — now the oldest remaining [v141] — the third entry of
the third-pass pool (the v133–v138 second-pass pool EXHAUSTED at v144;
the v139-era ITEMS pair re-run at v145; the v140-era SAVINGS pair
re-run at v146); the pair's FOURTEENTH re-run bracket [v59 -> v66 ->
v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111 -> v117 -> v123 ->
v129 -> v135 -> v141 -> v147]; the SEVENTIETH consecutive
queue/ledger agreement — the surface names verified against the v141
lineage's own records BEFORE the derivation (the v141 plan's own
header: the THIRTEENTH ordinal on its 14-entry bracket [v59 the
original, one entry — 14 entries − the original = 13 re-runs, no
off-by-one this lineage]; the v141 shots header carries the FULL
bracket form, the verification source). **A PIN-ONLY cycle for src/
— zero production-code changes + one e2e pin (349 -> 350)**; the
cycle's standing items: the axe watch (NO DRIFT — 4.14.0 holds, the
v68 dedupe verified), the npm-audit watch at its thirty-eighth
re-check (0 vulnerabilities --omit=dev — the v110 bump holds [next
16.4.3 + zod 4.6.7]; no new advisories in the watched ranges), the
141st standing checks (ALL GREEN — the reference's four bugs live;
the data census clean on the FIRST reads; the clone's mobile menu
VERIFIED WORKING the 141st consecutive time; zero overflow at 390 on
all five views; the seedcheck exact after the clone half).

The baseline GREEN on the FIRST run (the SAME-PERSISTED workspace —
the v146 environment held: node_modules 354 entries, BOTH chromium
pairs [1200 + 1243], .env + db/ at the repo root with the canonical
Oct 31 seed stamps [verified live: the items' date fields
2026-10-21..29 + the assets'/liabilities' lastUpdated 2026-10-31];
the repo pulled clean to main @ aa88e7c; the seedcheck EXACT
7/1850/2235/0/3/2 before any gate — under the env -u discipline,
the sandbox DATABASE_URL pollution live as documented): lint,
typecheck, 108/108 unit, build [robots + sitemap prerendered], the
4-chunk e2e [352 executions = 349 unique, ZERO flakes], 35/35 smoke;
the production-seam audit clean; skills/ excluded.

The probe series derived from the v141 lineage (derive-v147-series.py
— the generic swaps incl. the SIX explicit session-token families
[refvlm/clonevlm + refcalc/clonecalc + reflogin/clonelogin arbit —
the tokens carry '141' without the 'v' prefix] + the
history-correction fragments [the era marker last re-shot v135->v141
+ the oldest-remaining list v135..v138->v141..v144 + the queue
source the v140 plan->the v146 plan + the agreement ordinal
SIXTY-FOURTH->SEVENTIETH + the re-run ordinal THIRTEENTH->FOURTEENTH
+ the bracket extended in all four files], all applied on the FIRST
run, zero residual, line counts preserved 102/166/65/355; bash -n +
node --check clean; the pre-derivation sweep re-confirmed the
standing finding — all era tokens confined to the file headers [the
sole body v-tokens the version-self-reference echoes]) + the
login-shots sub-series (derive-loginshots-v147.py, 30/30) + the
two-half builder (derive-build-twohalf-v147.py — the generic swap +
the lesson-range bump v92..v140->v92..v146 [the BARE range token] +
the lineage-note fixup "build-twohalf-v135.py"->"build-twohalf-
v141.py" LAST [the v110 swap-order rule]) + the comparator
(derive-compare-v147.py — the generic swap + the provenance
citations re-pointed at the v141 measurement [the lineage ordinal
THIRTEENTH->FOURTEENTH; the records chain extended +v141; the v147
census must reproduce the v141 values EXACTLY]) + the verify script
(derive-verify-twohalf-v147.py — the generic swap + the
lineage-citation chain extended v124..v140->v124..v146; the digests
themselves UNCHANGED) + the 141st standing pair
(derive-standing-v147.py — derived from the v140 pair, three token
families [the ordinal 140th->141st th->st plain replace — the suffix
following the number's English form, the same plain-replace family
as v122's 121st/v132's 131st; the bare session names
ref140/clone140->ref141/clone141, the version v140->v141],
normalize-back diff clean, zero old tokens, line counts preserved
119/74). The halves built + the TWO-block md5 contract verified by
the direct THREE-WAY python extraction (verify-twohalf-v147.py —
CALC_CENSUS_JS 61 lines md5 e1092d12d06677a4 + LOGIN_CENSUS_JS 36
lines md5 9e5a52d2ab0f2ab9, byte-identical across arbit-v147.sh +
ref-arbit-v147.sh + clone-arbit-v147.sh — the documented
v123/v129/v135/v141 login+calc-lineage contract VERBATIM, carried
byte-identical through the version-swap derivation).

The resource discipline applied between every half (the browser
daemons reaped BEFORE every half; both halves + both shot series
executed with first-attempt logins; the full logs captured by the
runner redirection — /tmp/vlm147/{ref,clone}-arbit-full.log, the
comparator's documented input paths). The VLM pairwise run TWICE
with full log capture (/tmp/vlm147/vlm-pass{1,2}.log): pass 1
CALCULATOR DIFFERENT / LOGIN IDENTICAL; pass 2 CALCULATOR DIFFERENT
/ LOGIN IDENTICAL — the pair's documented verdict-VARIATION family
(the login verdict has varied IDENTICAL/DIFFERENT across re-runs —
v105/v129 IDENTICAL, v135 pass 2 DIFFERENT-with-the-sole-disproven-
flag, v141 IDENTICAL x2; here IDENTICAL x2). The login passes' sole
note the reference's own "Edit with Base44" FAB (the PLATFORM-CHROME
class) — DISPROVEN LIVE by base44-fab-arbit-v147.sh (derived from
the v141 form, swap-only verified: fabCount 0 + bodyHasBase44 false
on BOTH sides at 1280 /login — the standing v97/v103/v108/v109/
v115/v120/v123/v127/v129/v135/v141 disproof form re-confirmed).
Every calculator flag in both passes in the documented classes,
arbitration-free (every flag's class already DOM-confirmed by the
census's own axes): the line-item row hover action buttons the
POINTER-POSITION/HOVER-STATE screenshot artifact (the census
actionsAtRest {opacity 0, btnCount 2} IDENTICAL both sides — the
reference's shot carries its hover-revealed buttons, the clone's its
at-rest hidden ones; the v129/v135/v141 documented class); the "Will
update category total" note + the totalCard height + the row-height
consequence the SEED-DATA class (ref false vs clone true —
totalCard.hasWillUpdateSpan; the reference's Rent $25.00 equals its
calculated total so the note hides; the clone's Rent $1850 vs the
recalculated $25.00 shows it — the totalCard box byte-identical).

The both-sides census compared axis-by-axis (compare-v147-census.py):
106 axes — 97 identical + 9 documented-class deltas, ZERO new —
REPRODUCING the v141 census values EXACTLY (the same 106/97/9 split,
zero drift on every axis: the 9 documented = login card.border [the
zero-width computed-color artifact] + login card.shadow + calc
panel.shadow [the v3/v4 construct zero-layer-lead-count class] + the
5 close.* axes [the v99 finder artifact — clone-only present, the
asymmetry direction HOLDS] + calc totalCard.hasWillUpdateSpan [the
seed-data class]). The seedcheck exact after the clone half
(7/1850/2235/0/3/2). NO NEW CLONE GAP on the census axes.

THE PIN — the LOGIN LOGO's OWN-HOVER LADDER at 1280 (PIN-ONLY for
src/ — zero production-code changes + one e2e = 350): the
never-pinned HOVER PATH of the login logo's decorative
micro-interaction family (the v7 G3 pin holds the .zb-logo-ring
4px white/50 halo AT-REST — a DIFFERENT element; the v75 F4 pin the
logo img's geometry AT-REST [96x96 + the alt]; the v141 pin the
submit's own-hover ladder — a DIFFERENT element; the logo's
own-hover end-state held by NO spec at ANY viewport [the suite-wide
survey: rg 'logo' across tests/e2e/*.spec.ts — every match at-rest
chrome; auth.spec.ts's own comment records the span "keeps its
shadow-lg / group-hover:shadow-xl" — the construct documented, never
pinned]). THE CONSTRUCT (the discovery-measured DOM, both sides):
the logo group (div.group) carrying the BLUR HALO layer (opacity-30
blur-xl transition-opacity duration-300 group-hover:opacity-40 —
login-card.tsx:56) + the CHIP span (shadow-lg transition-all
duration-300 group-hover:shadow-xl — login-card.tsx:68) + the img
(96x96). The both-sides one-shot census logohover-arbit-v147.sh
(the v141 submithover form adapted to the logo axis: the STRUCTURAL
finder [img[alt*="logo"] -> the group = img.parentElement.
parentElement — the form shared by both sites, the alt
cross-checked], the (5,5)-parked ladder, the live-read center,
READ-ONLY — a mouse MOVE on a decorative div dispatches no click;
the logo NEVER clicked [passive decoration, no handler]; the
discovery script logohover-discovery-v147.sh ran FIRST to map both
sides' DOM) measured the ladder on BOTH sides CLEAN — NO GAP: the
AT-REST rung {haloOpacity 0.3 + haloFilter blur(24px) + the chip's
shadow-lg VISIBLE ambient pair [rgba(0,0,0,0.1) 0px 10px 15px -3px /
0px 4px 6px -4px] + the geometry 96x96 + the transitions} IDENTICAL
both sides; the LOGO-HOVERED rung {groupHover true + haloOpacity
0.4 — THE INTENSIFIED-HALO contract + the chip's shadow-xl ambient
pair [0px 20px 25px -5px / 0px 8px 10px -6px] + the filter/
geometry UNCHANGED} IDENTICAL both sides (the logo center REF
(640,123) / CLONE (640,123)); the RESTORED rung back to the at-rest
contract; the sole deltas the chip's at-rest INVISIBLE lead-layer
construct (REF the v3 form with the inline white/50 ring vs CLONE
the TW v4 five-slot form + the separate .zb-logo-ring layer — the
v7 G3 construct class, the visible ambient pair byte-identical,
never pinned). The pin appended (append-pin-v147.py — the at-rest
rung -> the LOGO-HOVERED rung {groupHover true + haloOpacity 0.4 +
the chip's shadow-xl ambient pair via toContain + the filter/
geometry UNCHANGED} -> the restored rung; the V7-G3/V75-COLLISION-
safe axis set; the STRUCTURAL finder; the logo NEVER clicked — a
mouse MOVE only; GREEN on the first run; the authoritative --list:
350 in 24 files).

THE PIN-SANITY MUTATION — the HALO-OPACITY-REMOVAL form:
group-hover:opacity-40 removed from the halo layer's className at
login-card.tsx:56 (the single utility; the WIDER blast radius noted:
the LogoMark serves every auth mode — signin/signup/forgot/verify
share the component — but the mutation's consequence surfaces ONLY
on the hovered-halo axis [the chip's shadow-xl is a separate utility
on a separate line, untouched; every at-rest census stays green —
the halo's at-rest opacity 0.3 is the mutation-invariant value]) —
the exact CSS-cleanup drift class the pin exists to guard (the
"consolidation" that kills the micro-interaction's halo
intensification — a regression invisible to every at-rest census):
the at-rest rung UNCHANGED, but the HOVERED rung fails [the halo
stuck at 0.3]. **The SOLE FAILURE verified live — 1 failed [the pin
alone] + 33 passed in the FULL login-parity sweep**, the failure
diff EXACTLY the predicted hovered-rung halo axis (opacity "0.3"
received vs the pinned "0.4" expected, groupHover true + the
filter/geometry/alt axes preserved); restored (git diff src/ = 0
lines) + the FULL REBUILD + the post-restore regression **34
passed** (the full login-parity sweep — the v147 pin + the v141
pin's different-line immunity verified live).

The ship chain: **350 e2e zero flakes** (97+95+79+82 = 353
executions = 350 unique — the +1 landing in ch3 [login-parity];
both closed watches green through the chain); 35/35 smoke; the
screenshots **16/16 captured — ALL byte-identical** (the same-day
law: both the v146 cycle's committed captures and this cycle's
captures ran Nov 2 UTC, every date-bearing surface rendering
identically — NO WALL-CLOCK class this cycle); the dev evidence 4/4
byte-identical + VLM-verified (the menu proof {"url":"/income",
"docSW":390,"navLandmark":true}; the dev-shots scripts derived
v146 -> v147 with the version-swap-only verification on both).

The v148 queue (suggestions — verify against the rotation ledger before
executing; THE CORRECTED CONVENTION — the ordinal ALWAYS derived from
the from-lineage's own bracket [entries − 1, the original not a re-run],
never the prose): (1) the re-run cadence's next-oldest candidate —
**the v142-era NETWORTH + drill-down-DASHBOARD pair** (the NETWORTH
view + the DASHBOARD's drill-down EXPANDED state at desktop 1280x800
[the v60-era pair's surface family], last re-shot v142 — now the
oldest remaining [v142]; the pair's FOURTEENTH re-run bracket [v60 ->
v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112 -> v118 ->
v124 -> v130 -> v136 -> v142 -> v148] to be verified against the v142
lineage's own records before the derivation — the v142 plan's own
header records the THIRTEENTH ordinal on its 14-entry bracket [v60 the
original, one entry — 14 entries − the original = 13 re-runs],
consistent, no off-by-one this lineage; the v142 shots header carries
the FULL bracket form, the verification source),
(2) the axe-core watch at its next re-check point (only a 5.x wrapper
changes the calculus), (3) the npm-audit watch at its re-check point
(only a new advisory in the next/zod ranges changes the calculus),
(4) the deferred reference-write censuses (unchanged — out of bounds
under the v46 read-only rule), (5) the residual-class watch (both
flake classes CLOSED by the v136 dual-stack/localhost fix — the
watch continues in the standing form for any NEW class).

"""

text = io.open(PATH, encoding="utf-8").read()
if "## The v147 cycle" in text:
    print("SKIP: the v147 section already present")
    sys.exit(0)

anchor = "the standing form for any NEW class).\n\n## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)"
n = text.count(anchor)
if n != 1:
    print(f"FAIL: the insert anchor {n}x")
    sys.exit(1)

text = text.replace(anchor, "the standing form for any NEW class).\n\n" + SECTION + "## The v138 cycle (the v132-era MOBILE-TWINS pair's TWELFTH re-run — Session 173)")
io.open(PATH, "w", encoding="utf-8").write(text)
print("OK: the v147 section + the v148 queue inserted (D6)")
