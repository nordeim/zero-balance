#!/usr/bin/env python3
"""D4-D6 docs alignment for the v97 cycle (Session 132).

D4 zero-balance_SKILL.md — the state line (299 -> 300) + the Session 132
    audit row after the Session 131 row.
D5 Project_Architecture_Document.md — the v1.1.54 revision block before
    the v1.1.53 block.
D6 scripts/parity-probes/README.md — the v97 section (findings + lessons
    + the v98 queue) appended at the end.
"""
import sys

ok = True

def must_replace(path, old, new, count=1):
    global ok
    text = open(path, encoding="utf-8").read()
    n = text.count(old)
    if n != count:
        print(f"MISS ({n} found, want {count}) in {path}: {old[:60]!r}")
        ok = False
        return
    open(path, "w", encoding="utf-8").write(text.replace(old, new, count))
    print(f"applied in {path}: {old[:48]!r}")

SKILL_ROW = ("| 2026-10-20 | Session 132 — parity iteration v97 (`docs/remediation-plan-v97.md`) | **The re-run cycle's next-oldest candidate (the v91-era ITEMS pair's sixth re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97] — the INCOME + EXPENSES view pair at desktop 1280x800, full-page, last re-shot v91; the twentieth consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the filter-listbox panel/option-interior census pin at 1280 (PIN-ONLY — no production-code change; +1 e2e = 300)**: BOTH verdicts DIFFERENT (the pair's documented verdict class) with every flag DOM-arbitrated to a documented class — the payment-method footer chips the v57 DATA-CONDITIONAL class (the reference renders payment chips when data carries them — its own income card's footer childCount 2 with the \"Bank Account\" chip — while its expense items ship none), the badge wrap + the card h 200-vs-230 the v57/v70b Recurring-wrap class, the FAB the platform-chrome class (re-arbitrated live: fabCount 0 + bodyHasBase44 false on both sides); the two-half census (BUILT two-half from the start — the CENSUS_JS block md5-identical across the halves) reproducing the v85/v91 values exactly (zero drift on every axis); the +1 pin the LISTBOX PANEL + OPTION-RESTING interior (the missing-middle family: the panel container between the v91 trigger pin and the v36 option-state pin — never pinned at ANY viewport in ANY spec), the pin's own axes first measured byte-identical on both sides by the supplemental two-half census (both sides read-only); the mutation rounded-md → rounded-lg at ui/select.tsx:68 (only the v97 pin red — the panel radius axis alone, cascade-free; the line-scoping keeps the trigger's rounded-md at line 19 [the v91 pin] untouched); the screenshots 16/16 byte-identical (the same-day regeneration); the lessons: the census render-race generalization + the panel-chrome missing-middle family |** 108/300/35 green |\n")

PAD_BLOCK = """#### Revision Block — v1.1.54 (Tracked Changes)
- `[UI]` v1.1.54 (2026-10-20) — the v97 parity iteration (PIN-ONLY — no production-code change): the counts 108 unit / **300 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v91-era ITEMS pair's SIXTH re-run [v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97] — the INCOME + EXPENSES view pair at desktop 1280x800, full-page, last re-shot v91; the twentieth consecutive queue/ledger agreement, the surface names verified against vlm-shots-v91.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 npm-latest, only rc/next sha prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone) + the 91st standing checks (the mobile menu verified the 91st consecutive time; the reference's four bugs all live; the data census the 91st clean drift check — the expenses leg's timing-artifact re-read documented)**: BOTH verdicts DIFFERENT (the pair's documented verdict class) with every flag DOM-arbitrated to a documented class (the avatar the user-identity class; the stats/grids/contents the seed-data classes; the payment-method footer chips the v57 DATA-CONDITIONAL class [the reference renders payment chips when data carries them — its own income card's footer childCount 2 with the "Bank Account" chip — while its expense items ship none]; the badge wrap + the card h 200-vs-230 the v57/v70b Recurring-wrap class; the FAB the platform-chrome class re-arbitrated live by the one-shot both-sides DOM census [fabCount 0 + bodyHasBase44 false on BOTH sides]); the both-sides census — executed in the TWO-HALF controlled form BUILT two-half from the start (ref-arbit-v97.sh + clone-arbit-v97.sh via build-twohalf-v97.py, the ONE census JS block [CENSUS_JS 193 lines] byte-identical across the halves by the md5 line-block contract [b55dcd29]) — REPRODUCING the v85/v91 census values EXACTLY (the avatar/grid/card/titleRow/amount/footer/badge/filterCard families; the docSW 1280 guard); NO NEW CLONE GAP; the +1 e2e pin the filter LISTBOX PANEL + OPTION-RESTING interior census at 1280 (tests/e2e/items.spec.ts — the MISSING-MIDDLE family: the v91 pin holds the TRIGGER's resting chrome, the v36 S2 the OPTION's focus-state family, but the PANEL container itself [bg/radius/border/shadow/max-h/overflow/z + the viewport's 4px pad] and the option's RESTING interior [fs/fw/color/pad/radius/h] were never pinned at ANY viewport in ANY spec — the family-extension survey walking the COMPONENT LAYERS; the pin's own axes first measured byte-identical on both sides by the supplemental two-half census listbox-arbit-v97.sh + listbox-clone-v97.sh via build-listbox-v97.py, the census JS byte-identical by the md5 line-block diff 34c916da]); the pin-sanity mutation rounded-md -> rounded-lg at src/components/ui/select.tsx:68 (by LINE NUMBER; the line-scoping keeps the SelectTrigger's own rounded-md at line 19 untouched [the v91 pin's 6px trigger axis]): ONLY the v97 pin red (41 green under the mutation), the failure diff reads as the panel radius axis ALONE ("6px" -> "8px") — cascade-free BY CONSTRUCTION, then restored (git diff src/ = 0; the standalone REBUILD; the post-restore full run 42/42 green); the F5 chain 135+96+71 = 302 chunk executions = 300 unique tests, zero flakes; the screenshots **16/16 BYTE-IDENTICAL** (the same-day regeneration — both sides Oct 20 UTC, no midnight crossing); the operational lessons: the census render-race generalization (ANY multi-eval reference flow treats a "no match"/empty census as a possible expiry OR render race first — re-login + settle-wait + re-read — before suspecting drift), the panel-chrome missing-middle family (the family-extension survey should walk the COMPONENT LAYERS, not just the axes of one layer), and the two-half form as the default (zero resource-exhaustion symptoms).

"""

PROBE_SECTION = """
## v97 — the items pair's sixth re-run (the missing-middle listbox pin)

The v97 iteration (docs/remediation-plan-v97.md): the re-run cycle's
next-oldest candidate — the ledger-verified queue (the v96-era docs'
v97 suggestion AGREEING with the rotation ledger: the v91-era ITEMS
pair [the INCOME + EXPENSES view pair at desktop 1280x800, full-page],
last re-shot v91, the oldest remaining [v91 < v92 < v93 < v94 < v95 <
v96]; the pair's SIXTH re-run [v57 -> v64 -> v70 -> v79 -> v85 -> v91
-> v97] — the TWENTIETH consecutive queue/ledger agreement, the surface
names verified against vlm-shots-v91.sh's own header before the
derivation), plus the axe watch at its re-check point (NO DRIFT —
4.14.0 npm-latest, only rc/next sha prereleases beyond, no 5.x, the
v68 dedupe holds) and the 91st standing checks (version-bumped from v90
across the three token families — version-bump-only diffs verified by
normalizing back and diffing clean).

The probe series (the v91 lineage, derive-v97-series.py — the generic
swaps then the exact-fragment history corrections [last-re-shot v85 ->
v91, FIFTH -> SIXTH, the re-run bracket extension, the
every-other-pair list], every correction's hit/miss REPORTED, all four
applied clean on the first run; bash -n + node --check clean; zero
residual old tokens — the legitimate "last re-shot v91" provenance +
the SIXTH bracket whitelisted by context):
- vlm-shots-v97.sh — the REFERENCE side (login on the first attempt;
  the parked pointer at (5,5); read-only — the v46 rule).
- clone-vlmshots-v97.sh — the CLONE side (the with-server :3200 parity
  server).
- vlm-compare-v97.mjs — the VLM pairwise.
- arbit-v97.sh + ref-arbit-v97.sh + clone-arbit-v97.sh — the
  both-sides census, BUILT two-half from the start via
  build-twohalf-v97.py (the ONE CENSUS_JS block [193 lines]
  byte-identical across the halves — the md5 line-block contract
  b55dcd29).
- base44-fab-arbit-v97.sh — the one-shot both-sides DOM re-arbitration
  of the recurring FAB flag (fabCount 0 + bodyHasBase44 false on BOTH
  sides — the platform-chrome class; this cycle the VLM attributed the
  FAB to the REFERENCE, the non-inverted form of the v85/v91-documented
  attribution class).
- listbox-arbit-v97.sh + listbox-clone-v97.sh — the supplemental
  two-half census for the pin's own axes (the filter listbox PANEL +
  option-resting interior at 1280), BUILT two-half from the start via
  build-listbox-v97.py (the census JS byte-identical by the md5
  line-block contract 34c916da).

The findings:
1. Both verdicts DIFFERENT, every flag DOM-arbitrated to the v85/v91
   re-run's OWN documented classes (the v57 payment-chip
   DATA-CONDITIONAL footer — PROVEN by the reference's own income
   card's footer childCount 2 with the "Bank Account" chip while its
   expense items ship none; the v57/v70b Recurring superset wrap [the
   card h 200-vs-230, the badgeRow h 22-vs-52]; the seed-count grids;
   the user-identity avatar; the seed-data figures/dates/badges).
2. The both-sides census (the two-half form) REPRODUCES the v85/v91
   census values EXACTLY — zero drift on every axis (the
   avatar/grid/card/titleRow/amount/footer/badge/filterCard families;
   the docSW 1280 guard; the income template's last-column sub-pixel
   the column-distribution rounding noise WITHIN the documented
   309.328px family). NO NEW CLONE GAP — the iteration PIN-ONLY.
3. The v97 pin (+1 e2e = 300): the filter LISTBOX PANEL +
   OPTION-RESTING interior census at 1280 (tests/e2e/items.spec.ts —
   the MISSING-MIDDLE family: the v91 pin holds the TRIGGER's resting
   chrome, the v36 S2 the OPTION's focus-state family, but the PANEL
   container itself [bg/radius/border/shadow/max-h/overflow/z + the
   viewport's 4px pad] and the option's RESTING interior
   [fs/fw/color/pad/radius/h] were never pinned at ANY viewport in ANY
   spec — the family-extension survey walking the COMPONENT LAYERS
   [trigger -> panel -> viewport -> option]) — the pin's own axes first
   measured byte-identical on both sides by the supplemental two-half
   census — GREEN on first run.
4. The pin-sanity mutation (the executed form — the SelectContent
   panel's rounded-md -> rounded-lg at src/components/ui/select.tsx:68,
   by LINE NUMBER; the line-scoping keeps the SelectTrigger's own
   rounded-md at line 19 untouched [the v91 pin's 6px trigger axis]):
   the failure diff reads as the panel radius axis ALONE ("6px" ->
   "8px"); the full items.spec.ts under the mutation reads ONLY the
   v97 pin red (41 green) — cascade-free BY CONSTRUCTION — then
   restored (git diff src/ = 0; the standalone REBUILD; the
   post-restore full run 42/42 green).
5. The full chain re-run GREEN: lint -> typecheck -> 108 unit -> build
   -> 300 e2e (135+96+71 = 302 chunk executions, zero flakes) ->
   35/35 smoke; the screenshots 16/16 BYTE-IDENTICAL (the same-day
   regeneration — both sides Oct 20 UTC, the 07-add-item-modal's day
   digits matching, no midnight crossing this cycle).

**The v97 lessons:**
- THE CENSUS RENDER-RACE GENERALIZATION (the v79 expiry-twin, extended):
  the reference-side expenses census read "no match" — not the session
  expiry (the v79 form) but the eval racing the page's client-side
  render (the timing-artifact family). The generalized discipline: ANY
  multi-eval reference flow treats a "no match"/empty census as a
  possible expiry OR render race first (re-login + settle-wait +
  re-read) before suspecting drift — and never records the state change
  on a single raced read.
- THE PANEL-CHROME MISSING-MIDDLE FAMILY (NEW): the v91/v92
  trigger-interior pins and the v36 option-state pins bracket the
  filter select's popover, but the PANEL container itself was never
  pinned at any viewport — the family-extension survey should walk the
  COMPONENT LAYERS (trigger -> panel -> viewport -> option), not just
  the axes of one layer.
- THE TWO-HALF FORM AS THE DEFAULT (the v92..v96 lesson, applied clean
  again): every census this cycle BUILT two-half from the start — zero
  resource-exhaustion symptoms.

The v98 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the items pair (the v92-era SAVINGS pair [the SAVINGS view + the
goal-card interior pair at desktop 1280x800], last re-shot v92 — now
the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97]; the pair's
re-run bracket to be verified against vlm-shots-v92.sh's own header
before the derivation), (2) the axe-core watch at its next re-check
point (only a 5.x wrapper changes the calculus), (3) the deferred
reference-write censuses (unchanged — out of bounds under the v46
read-only rule).
"""

# D4 — SKILL
must_replace("zero-balance_SKILL.md",
             "project_state: 108 unit tests / 299 e2e tests / 35 smoke steps — all green",
             "project_state: 108 unit tests / 300 e2e tests / 35 smoke steps — all green")
text = open("zero-balance_SKILL.md", encoding="utf-8").read()
if "Session 132 — parity iteration v97" in text:
    print("D4 row already applied")
else:
    anchor = "| 2026-10-19 | Session 127 — parity iteration v92"
    i = text.index(anchor)
    text = text[:i] + SKILL_ROW + text[i:]
    open("zero-balance_SKILL.md", "w", encoding="utf-8").write(text)
    print("D4 applied: the Session 132 row inserted before the Session 127 row")

# D5 — PAD
text = open("Project_Architecture_Document.md", encoding="utf-8").read()
if "v1.1.54" in text:
    print("D5 already applied")
else:
    anchor = "#### Revision Block — v1.1.53 (Tracked Changes)"
    i = text.index(anchor)
    text = text[:i] + PAD_BLOCK + text[i:]
    open("Project_Architecture_Document.md", "w", encoding="utf-8").write(text)
    print("D5 applied: the v1.1.54 revision block inserted before the v1.1.53 block")

# D6 — probe README
text = open("scripts/parity-probes/README.md", encoding="utf-8").read()
if "## v97 — the items pair's sixth re-run" in text:
    print("D6 already applied")
else:
    if not text.endswith("\n"):
        text += "\n"
    text += PROBE_SECTION
    open("scripts/parity-probes/README.md", "w", encoding="utf-8").write(text)
    print("D6 applied: the v97 section appended to the probe README")

sys.exit(0 if ok else 1)
