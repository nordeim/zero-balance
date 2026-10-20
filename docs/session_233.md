# Session 233 — the v97 parity cycle (Session 132 work record)

The task chain per the standing instruction: workspace refresh → core
docs re-review → the latest session docs → the codebase audit → the
reference parity iteration → the remediation plan → the TDD execution →
the screenshots → the docs alignment → the commit + the SSH-wrapper
push. The rotation ledger's v97 target verified FIRST against the v91
probe's own header (the queue-prose verification lesson).

## The cycle record

**F0 baseline** — the workspace pulled to main @ 27c5970 (the
session-log-only commit class: the two commits since the v96 push
90f766e — 59e7d14 + 27c5970 — verified docs-only [session_231.md +
session_232.md], ZERO src/ or lockfile deltas, so the v96 environment
carries over unchanged, no re-provisioning). The seedcheck exact (7
items / rent 1850 / expensesTotal 2235 / 0 line items / 3 assets / 2
liabilities) before any flow ran. The chain: lint ✓ · typecheck ✓ ·
108/108 unit ✓ · build ✓ (robots + sitemap prerendered) · 299 e2e in
three chunks (134+96+71 = 301 executions = 299 unique, zero flakes on
the first run) · 35/35 smoke ✓. The codebase audit clean — the
production seams re-audited (auth scrypt/HMAC, the db-path contract
[the sandbox's polluted parent DATABASE_URL re-confirming the env -u
discipline], the SEO pair, the Tailwind v4 mitigations, the three test
tiers); skills/ excluded throughout.

**F1 axe watch** — NO DRIFT: npm-latest 4.14.0 (only rc/next sha
prereleases beyond; no stable 4.14.1, no 5.x); the wrapper + the engine
both 4.14.0; the v68 dedupe holds (one node_modules/axe-core); the
engine-contract pin 2 passed standalone.

**F2 the 91st standing checks** — derived v90 → v91 via the persisted
derive-standing-v97.py (three token families; version-bump-only
verified by the normalize-back diff; bash -n clean). Reference side:
the four bugs ALL live (toast-blocker `hitIsBurgerChild:false`;
sheet-trap `overlayCount:1`; no-landmark; the 464px /networth overflow
measured directly by the settle-wait form). The data census: networth +
income clean on the first read; the expenses leg first read "no match"
— THE RENDER-RACE ARTIFACT (the eval raced the page's client-side
render); the settle-wait re-read after a fresh login measured the exact
documented "4 items · $525.00". The SEO pair live. Clone side: R1–R4
ALL GREEN — **the mobile menu VERIFIED WORKING the 91st consecutive
time** (`hitIsBurgerChild:true`, the sheet opens + closes on nav, the
nav landmark present); zero overflow at 390 on all five views; the SEO
pair live.

**F3 the re-run pair** — the v97 probe series derived from the v91
lineage (derive-v97-series.py: the generic swaps + the exact-fragment
history corrections [last-re-shot v85 → v91, FIFTH → SIXTH, the
bracket extension, the every-other-pair list], every correction
hit/miss-reported, all applied clean; bash -n + node --check clean;
zero residual old tokens). The census BUILT two-half from the start
(build-twohalf-v97.py: ref-arbit-v97.sh + clone-arbit-v97.sh, the ONE
CENSUS_JS block 193 lines byte-identical across the halves — the md5
contract b55dcd29). The reaping between every half; login on the first
attempt both sides; the parked pointer at (5,5); read-only.

The VLM verdicts: BOTH DIFFERENT (the pair's documented class). Every
flag DOM-arbitrated: the avatar the user-identity class; the
stats/grids/card contents the seed-data classes; the payment-method
footer chips the **v57 DATA-CONDITIONAL class** — the census proves the
reference RENDERS payment chips when data carries them (its own income
card's footer childCount 2 with the "Bank Account" chip) while its
expense items ship none (footer childCount 1); the badge wrap + the
card h 200-vs-230 the **v57/v70b Recurring-wrap class** (the superset
badge wraps → h 52 [22+8+22] → +30px + the 1-row sibling stretch); the
"Edit with Base44" FAB the platform-chrome class re-arbitrated live by
base44-fab-arbit-v97.sh (fabCount 0 + bodyHasBase44 false on BOTH
sides — the FAB renders in the reference's platform iframe chrome; this
cycle the VLM attributed it to the reference — the non-inverted form of
the v85/v91 attribution class).

The two-half census REPRODUCES the v85/v91 census values EXACTLY —
zero drift on every axis (the avatar/grid/card/titleRow/amount/footer/
badge/filterCard families; the docSW 1280 guard; the income template's
last-column sub-pixel the column-distribution rounding noise WITHIN the
documented 309.328px family). **NO NEW CLONE GAP.**

**F4 the +1 e2e pin (299 → 300)** — the family-extension survey walked
the filter select's COMPONENT LAYERS (trigger → panel → viewport →
option): the v91 pin holds the trigger's resting chrome, the v36 S2 the
option's focus-state family — **the PANEL container (bg/radius/border/
shadow/max-h/overflow/z + the viewport's 4px pad) and the option's
RESTING interior (fs/fw/color/pad/radius/h) were never pinned at ANY
viewport in ANY spec** (the coverage-map grep across all 24 specs). The
supplemental two-half census (build-listbox-v97.py:
listbox-arbit-v97.sh + listbox-clone-v97.sh, the census JS md5
34c916da) measured the pin's axes byte-identical on both sides: the
panel {bg white, radius 6px, border 1px rgb(229,229,229), maxH 384px,
overflow hidden, z 50, pos relative, w 218}; the shadow-md visible
layers byte-identical (the zero-layer lead count 2-vs-4 the documented
v3/v4 construct class — the v37 O1 precedent, asserted via toContain);
the viewport {pad 4px, display block}; the opt0 {fs 14px, fw 400,
color rgb(23,23,23), pad 6px 32px 6px 8px, radius 4px, h 32}; the
deltas (panel h 74-vs-106, optCount 2-vs-3) the seed-data class.

The remediation plan v97 written and validated BEFORE the pin's
execution (the pre-execution validation section: the measured values,
the mutation target line verified by reading the source [select.tsx:68
carries EXACTLY ONE rounded-md; the trigger's identical token sits at
line 19], the coverage-map grep, the disproven-in-advance candidates).

The pin appended to items.spec.ts — GREEN on first run. The pin-sanity
mutation (rounded-md → rounded-lg at select.tsx:68, by LINE NUMBER):
ONLY the v97 pin red (41 green), the failure diff reads as the panel
radius axis ALONE ("6px" → "8px") — cascade-free BY CONSTRUCTION (no
spec asserts any listbox panel radius; the calculator's 16px panel is
the dialog, a different element; the radius changes no other axis).
Restored (git diff src/ = 0 lines); the standalone REBUILD; the
post-restore full items.spec.ts run 42/42 green.

**F5 the full chain** — lint ✓ · typecheck ✓ · 108 unit ✓ · build ✓ ·
300 e2e in three chunks (135+96+71 = 302 executions = 300 unique, zero
flakes) · 35/35 smoke ✓. The screenshots **16/16 BYTE-IDENTICAL** (the
same-day regeneration — both sides Oct 20 UTC, the 07-add-item-modal's
day digits matching, no midnight crossing this cycle). The final
seedcheck exact.

**The docs alignment** — D1 AGENTS.md (the v97 paragraph), D2 CLAUDE.md
(299 → 300 + the v97 clause at the E2E line's tail), D3 README.md (the
counts + the v97 plan-table row), D4 zero-balance_SKILL.md (Session 132
audit row + the state line), D5 the PAD's v1.1.54 revision block, D6
the probe README's v97 section (+ the v98 queue), D7 this file + the
worklog Session 132 entry. The workspace worklog updated.

## Cycle summary

| Phase | Result |
|---|---|
| **F0 baseline** (carried-over workspace) | seedcheck exact · lint/typecheck/108 unit/build ✓ · 299 e2e zero flakes · 35/35 smoke |
| **F1 axe watch** | NO DRIFT (4.14.0 both sides, dedupe holds, engine-contract pin 2 passed) |
| **F2 91st standing checks** | Mobile menu working the **91st consecutive time** (Tailwind v4 mitigation holds); ref's four bugs live; the expenses census render-race re-read documented |
| **F3 items-pair re-run** | Both verdicts DIFFERENT (documented class); every flag DOM-arbitrated (the payment-chip DATA-CONDITIONAL class proven by the reference's own income footer; the Recurring-wrap class; the FAB platform-chrome class); census reproduces v85/v91 exactly — **NO NEW CLONE GAP** |
| **F4 pin (+1 e2e = 300)** | The listbox PANEL + option-RESTING interior (the missing-middle family) — never pinned at any viewport; green first run; mutation hit exactly the panel radius axis (41 green); restored 42/42 |
| **F5 + ship** | 300 e2e · 35 smoke · screenshots 16/16 byte-identical (same-day) · PIN-ONLY — zero src/ changes |

**New documented classes this cycle:** the census render-race
generalization (the "no match" expiry/render-race first discipline) and
the panel-chrome missing-middle family (the family-extension survey
walking the component layers).

Per the rotation ledger, the **v98 cycle** targets the v92-era SAVINGS
pair (last re-shot v92 — now the oldest remaining) — reply "continue
v98" to proceed, or ask for any adjustments to this cycle's
deliverables.
