#!/usr/bin/env python3
"""D6 docs alignment for the v117 cycle — the probe README's v117 section
(inserted newest-first, before the v116 section) carrying THE SM:TIER
FREEZE lesson and the v118 queue. Insert-after WITH the idempotency guard
(the v113 lesson)."""
import sys

README = "scripts/parity-probes/README.md"
t = open(README, encoding="utf-8").read()

SECTION = """## The v117 cycle (the v111-era LOGIN + CALCULATOR pair's NINTH re-run — Session 152)

The re-run cadence's next-oldest candidate: the v111-era LOGIN +
CALCULATOR pair (the LOGIN view + the CALCULATOR dialog at desktop
1280x800, last re-shot v111 — now the oldest remaining [v111 < v112 <
v113 < v114 < v115 < v116]; the pair's NINTH re-run bracket [v59 -> v66
-> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111 -> v117]; the
FORTIETH consecutive queue/ledger agreement — the surface names verified
against vlm-shots-v111.sh's own header BEFORE the derivation). **A FIX
CYCLE for src/ — the sixth production-code change since v46** (the
globals.css sm:space-y-3 restore) + one e2e pin; the cycle's standing
items: the axe watch (NO DRIFT — 4.14.0 holds, only a canary sha
prerelease beyond, the v68 dedupe verified), the npm-audit watch at its
eighth re-check (0 vulnerabilities — the v110 bump holds [next 16.4.3 +
zod 4.6.7]), the 111th standing checks (ALL GREEN — the mobile menu the
111th consecutive green; the reference's four bugs all live; the data
census clean on the FIRST reads, no render-race hit this cycle).

**F0 baseline FULLY GREEN on the FRESH-CLONE-PROVISIONED workspace**
(the RESET class — the v116 environment did not persist; the repo
re-cloned from main @ b40d034). The v108 FRESH-CLONE lesson applied
END-TO-END: npm ci (run in the foreground — the v114 silent-death
lesson; 354 entries) with the zod extraction verified INTACT [840/840
files, the src/v4 subdirectory present, verified BEFORE any gate; one
node_modules/zod entry — the v68 dedupe]; .env
[DATABASE_URL="file:../db/custom.db"] + db/ at the repo root; db:push +
db:seed (7 items / 3 assets / 2 liabilities); BOTH v1243 playwright
binaries verified DIRECTLY (the fresh cache held only the OLD
chromium-1200 pair). The gates: seedcheck exact (7/1850/2235/0/3/2) ·
lint · typecheck · 108/108 unit · build (robots + sitemap prerendered) ·
319 e2e (ONE documented flake: the not-found document-head-parity test
red on chunk 3's first run, green on the isolated spec re-run AND the
full chunk re-run [77/77] — the transient head-metadata read class) ·
35/35 smoke. The post-push commit since the v116 parity push (b40d034)
audited: session log + the owner's skills/ tree prune — ZERO src/,
tests/, prisma/ or lockfile deltas.

**F3**: the series derived from the v111 lineage (derive-v117-series.py
— the generic swaps + the SIX exact-fragment history corrections, 6/6
applied on the FIRST run; line counts preserved). The census BUILT
two-half from the start (build-twohalf-v117.py via
derive-build-twohalf-v117.py with the swap-order rule; the TWO census JS
blocks [CALC_CENSUS_JS 61 lines + LOGIN_CENSUS_JS 36 lines]
byte-identical across the halves — the md5 line-block contracts
[e1092d12 / 9e5a52d2 — the v99/v105/v111 census blocks VERBATIM]; ONE
builder derivation REPAIR documented: the lineage-note fragment must
target the LINE-INTERNAL bare form "build-twohalf-v105.py — the v117
derivation" — the source wraps the line after "from", so the
with-prefix fragment missed silently on the first pass [the MISSING-
SOURCES report], the v107 line-break lesson's builder instance). The
verdicts: CALCULATOR DIFFERENT (the pair's documented verdict class —
the will-update note the SEED-DATA class [ref hasWillUpdateSpan:false,
its own Rent $25.00 equals its calculated total]; the hover-action row
the RESTING-STATE parity class [actionsAtRest {opacity 0, btnCount 2}
identical both sides]; the row-height flag their consequence) + LOGIN
DIFFERENT (the FAB flag alone — DISPROVEN live by the one-shot
base44-fab-arbit-v117.sh on the flagged /login surface at 1280: fabCount
0 + bodyHasBase44 false on BOTH sides — the platform-iframe chrome
class, the v97/v103/v108/v109/v115 standing disproof form re-confirmed).
The census compared AXIS-BY-AXIS by the persisted compare-v117-census.py
(**106 axes: 97 identical + 9 documented-class deltas, ZERO new** — the
card.shadow/panel.shadow zero-layer lead counts the v3/v4 construct
class [the visible layer the contract, the v45 F4 pin]; the card.border
zero-width computed-color artifact [border-width 0 both sides, nothing
renders — the v3 base default gray-200 vs the app's measured
--color-border token, the card line exactly as pinned in v7]; the
close-key family the v99 finder artifact [the v87 pin the authority, the
asymmetry direction verified still clone-only]; hasWillUpdateSpan the
SEED-DATA class) — with the strip census's `bottom` axis divergence (ref
742 vs clone 738) NOT whitelisted but root-caused (below) — the cycle's
find.

**F4 [FIX + PIN] — THE SM:TIER FREEZE (a new member of the trap-4b
family, the cycle's Tailwind v4 bug)**: the pin-candidate survey (the
login card's TOP ACCENT STRIP — the element every login census walked
past: the v7 G2 pin holds its gradient COLORS via toContain only, its
geometry never pinned at ANY viewport in ANY spec) measured the strip
byte-identical both sides — but the census's `bottom` axis read ref 742
vs clone 738, exposing a 4px card-height delta (ref 746 vs clone 742).
The drill-down (cardheight-arbit-v117.sh + the h1/subtitle reads): the
padding (48px 40px 40px), the form blocks (172 + 80), the h1 (72), the
subtitle (24) all IDENTICAL — the delta isolated to the h1 BLOCK's
internal gap: **the reference's subtitle margin-top 12px (its
sm:space-y-3 tier at >=640) vs the clone's 8px (its space-y-2 base tier
— the sm: tier FROZEN OUT)**. Both sides declare the reference's own
verbatim classes `space-y-2 sm:space-y-3` (login-card.tsx:574, the ONLY
sm-paired tier in the codebase). THE MECHANISM (the built-CSS
verification): the v9 G3 mitigation restores v3 space-y semantics for
the BASE tiers with class-specificity rules (`.space-y-2 > * + *
{ margin-block-start: 0.5rem }`, 0-1-2) — which BEAT v4's
zero-specificity `:where(.sm\\:space-y-3 > :not(:last-child))` media
variant at >=640: **the sm: tier can never override the mitigated
base**. The v3 engine (the reference): the base and the media variant
share specificity and the media rule wins at >=640 — 12px. THE FIX (the
v50 zb-sm6 precedent's form): the sm:-variant restore in globals.css's
@layer utilities — `@media (min-width: 640px) { .sm\\:space-y-3 > * + *
{ margin-block-start: 0.75rem } }` (source order after the base restore
decides the same-specificity tie). Cascade-verified SURGICAL: exactly
ONE element in the codebase carries sm:space-y-3; the v99 social-row
pin's rhythm axis is RELATIVE (both elements shift equally), the
v105/v7/v25/v45/v55/v51 pins element-local or other-mode — zero
existing pins redden (verified live, 52/52). THE RULE: a base-tier
mitigation restore MUST be accompanied by its responsive-variant
members — the class-specificity restore freezes out every
zero-specificity :where() variant of the same utility family at the
media breakpoint (check the built CSS for the :where() media form
whenever a mitigated utility carries an sm:/md:/lg: sibling in the
source classes).

The +1 pin (tests/e2e/login-parity.spec.ts): the login card's
TOP-ACCENT-STRIP + H1-BLOCK census at 1280 (+1 e2e = 320) — the strip's
never-pinned geometry {tag DIV/position absolute/top 0px/right 0px/
left 0px/h 4/w 448/bgImage the full 3-stop slate gradient} + the FIXED
family {subtitle mt "12px"/block h 108} + the card context {w 448/h
746} + the docSW guard; the finders STRUCTURAL (the form-walk-up card
finder; the strip as the card's absolutely-positioned thin top child;
the `bottom` axis deliberately UNPINNED — the card-height-derived data
axis, the v107 position-arithmetic discipline). TDD-verified: the
pre-fix RED run failed at the sm:TIER axes alone [subMt "8px" vs
"12px"] — the fix load-bearing; the standalone REBUILD; the post-fix
GREEN; the 52/52 surface regression check.

The ship: 320 e2e zero flakes across the auditable four-chunk split
(84+80+77+82 = 323 executions = 320 unique); 35/35 smoke; the
screenshots regenerated with 9 byte-diffs ARBITRATED (2 fix-effects
[01-login + 14-login-error — the +4px card shift, the fix's own
evidence] + 7 date-drifts [the relative-seed dates rolled a day:
03/04/05/06/07/08/16, the footer-band bboxes — the standing
same-day-seed law's boundary]; 15-forgot-reset byte-IDENTICAL — the
surgical-fix confirmation, the forgot mode rides the .zb-auth-mode
container untouched); the dev evidence 3 same + 1 date-drift +
VLM-verified (the menu proof: /income, docSW 390, navLandmark true; the
menu open with all 5 links + the brand; the sheet closed post-nav; the
dashboard clean — the dev-shots scripts derived v116->v117 with the
version-swap-only verification).

The v118 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the v111-era LOGIN + CALCULATOR pair (the v112-era NETWORTH +
drill-down-DASHBOARD pair — the desktop 1280x800 FULL-PAGE state of
(1) the NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED
state, last re-shot v112 — now the oldest remaining [v112 < v113 <
v114 < v115 < v116 < v117]; the pair's NINTH re-run bracket [v60 -> v67
-> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112 -> v118] to be
verified against vlm-shots-v112.sh's own header before the
derivation), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the npm-audit watch at its
re-check point (only a new advisory in the next/zod ranges changes the
calculus), (4) the deferred reference-write censuses (unchanged — out
of bounds under the v46 read-only rule).

"""

if "## The v117 cycle" in t:
    print("ALREADY APPLIED: the v117 section — skipped")
    sys.exit(0)
anchor = "## The v116 cycle (the v110-era SAVINGS pair's NINTH re-run — Session 151)"
if t.count(anchor) != 1:
    print(f"AMBIGUOUS/MISS anchor ({t.count(anchor)} hits)")
    sys.exit(1)
t = t.replace(anchor, SECTION + anchor, 1)
open(README, "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (the v117 section + the v118 queue)")
