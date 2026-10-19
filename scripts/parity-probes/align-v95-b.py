#!/usr/bin/env python3
"""align-v95-b.py — D4-D6 docs alignment for the v95 cycle:
D4 zero-balance_SKILL.md (Session 130 audit row + the state line),
D5 the PAD's v1.1.52 revision block, D6 the probe README's v95 section
(+ the v96 queue). Idempotent."""

SKILL_ROW = ("| 2026-10-19 | Session 130 — parity iteration v95 (`docs/remediation-plan-v95.md`) | "
"**The re-run cycle's next-oldest candidate (the v89-era dashboard pair's fifth re-run "
"[v61 → v68 → v77 → v83 → v89 → v95] — the BUDGET GUIDELINES card + the QUICK-ACTION card row, both "
"below-the-fold surfaces of the dashboard FULL-PAGE at desktop 1280x800, last re-shot v89; the eighteenth "
"consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the quick-action transition-timing family "
"census pin (PIN-ONLY — no production-code change; +1 e2e = 298)**: the verdict IDENTICAL — zero style flags "
"on the pair's own target surfaces (the third consecutive IDENTICAL for this pair [v83 → v89 → v95]); every "
"flag the documented standing classes (the seed-data figures; the v56 SUPERSET root-URL nav highlight; the FAB "
"platform-chrome class; the avatar user-identity class); the two-half census (BUILT two-half from the start — "
"the ARBIT_G/Q/X blocks md5-identical across the halves) reproducing v89 exactly (zero drift on every axis; the "
"shadow lead-layer the v66 invisible class; the grid mt the v77 mechanism class [rendered gap 340 "
"byte-identical]; the label wrapper-catch the v61 lesson); the +1 pin the TRANSITION-TIMING family at 1280 "
"(the three cards' timing function + delay + the tiles' transition-transform family + the pluses' "
"transition-opacity family — never pinned at ANY viewport, the tile's transitionProperty asserted in the "
"CONTAINS form [the v95 v4 computed-form class]), the pin's own axes first measured byte-identical on both "
"sides by the supplemental two-half census (both sides read-only); the mutation transition-all duration-200 → "
"transition-all duration-200 lg:ease-linear at dashboard-view.tsx:885 (only the v95 pin red — the cardTiming "
"axis alone, cascade-free by construction); 16/16 screenshots byte-identical (the same-day-seed law — the "
"third consecutive pure-form cycle); the lessons: the template-brace generator bug + the two-half form as the "
"default + the v4 transition-property computed-form class |** 108/298/35 green |\n")

PAD_BLOCK = """#### Revision Block — v1.1.52 (Tracked Changes)
- `[UI]` v1.1.52 (2026-10-19) — the v95 parity iteration (PIN-ONLY — no production-code change): the counts 108 unit / **298 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v89-era DASHBOARD pair's FIFTH re-run [v61 -> v68 -> v77 -> v83 -> v89 -> v95] — the BUDGET GUIDELINES card + the QUICK-ACTION card row, both below-the-fold surfaces of the dashboard FULL-PAGE at desktop 1280x800, last re-shot v89; the eighteenth consecutive queue/ledger agreement, the surface names verified against vlm-shots-v89.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 npm-latest, only canary prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone) + the 89th standing checks (the mobile menu verified the 89th consecutive time; the reference's four bugs all live; the data census the 89th clean drift check)**: the verdict IDENTICAL with ZERO style flags on the pair's own target surfaces (the THIRD consecutive IDENTICAL for this pair [v83 -> v89 -> v95]); every VLM flag the documented standing classes (the seed-data figures; the v56 SUPERSET root-URL active-nav highlight; the "Edit with Base44" FAB platform-chrome class; the avatar "U" vs "D" user-identity class); the both-sides census — executed in the TWO-HALF controlled form BUILT two-half from the start (ref-arbit-v95.sh + clone-arbit-v95.sh via build-twohalf-v95.py, the THREE census blocks [ARBIT_G/ARBIT_Q/ARBIT_X] byte-identical across the halves by the md5 line-block contract [b500dd29 / da04e995 / 7a381755]) — REPRODUCING the v89 census values EXACTLY (PART G the guidelines card 468x348/the header/the body/the three tiles; PART Q the quick-action grid + the three cards; PART X cardBottom 1122/gridTop 1462/gap 340 — zero drift on every axis; the shadow lead-layer the v66 invisible class; the grid mt the v77 mechanism class; the label wrapper-catch the v61 lesson); NO NEW CLONE GAP; the +1 e2e pin the quick-action TRANSITION-TIMING family census at 1280 (tests/e2e/dashboard.spec.ts — never pinned at ANY viewport: the three cards' transitionTimingFunction {cubic-bezier(0.4, 0, 0.2, 1)} + transitionDelay {0s} [the v89 pin holds the duration/property only] + the three tinted tiles' transition-transform family {dur 0.2s, timing} + the three plus icons' transition-opacity family {prop opacity, dur 0.15s, timing, delay 0s} + the docSW 1280 guard; the tiles' transitionProperty asserted in the CONTAINS form — the v95 TAILWIND v4 COMPUTED-FORM class NEW this cycle [the reference's v3 "transform" vs the clone's v4 "transform, translate, scale, rotate" superset, the rendered behavior identical]; the pin's own axes first measured byte-identical on both sides by the supplemental two-half census [qa-timing-arbit-v95.sh + qa-timing-clone-v95.sh via build-qa-timing-v95.py, the census JS byte-identical by the md5 line-block diff ba296202; both sides read-only]); the pin-sanity mutation transition-all duration-200 -> transition-all duration-200 lg:ease-linear at dashboard-view.tsx:885 (by LINE NUMBER, AT-lg because the pin runs at 1280; the line-scoping keeps the file's OTHER transition-all duration-200 instance [line 578] untouched): ONLY the v95 pin red (41 green under the mutation), the failure diff reads as the cardTiming axis ALONE ("cubic-bezier(0.4, 0, 0.2, 1)" -> "linear") — cascade-free BY CONSTRUCTION (a timing-function flip affects no geometry and no computed style any other pin asserts; lg:ease-linear appears NOWHERE in src/), then restored (git diff src/ = 0; the standalone REBUILD; the post-restore full run 42/42 green); the F5 chain 107+98+95 = 300 chunk executions = 298 unique tests, zero flakes; the screenshots **16/16 BYTE-IDENTICAL** (the same-day-seed byte-identity law — the third consecutive pure-form cycle, ZERO arbitration needed); the operational lessons: the template-brace generator bug (the build-qa-timing-v95.py generator written with .format()-style doubled braces but applied with .replace() — the generated LOGIN_JS kept literal {{ }} which made agent-browser eval return EMPTY on every attempt; the discipline: bash -n + a spot grep for doubled braces after ANY generator run, and a manual open+snapshot diagnosis to separate site-down from script-broken), the two-half form as the default (zero resource-exhaustion symptoms), and the v4 transition-property computed-form class (Tailwind v4's transition-transform computes the expanded property list — the pin form for such axes: CONTAINS, never exact).
"""

PROBE_SECTION = """
## The v95 cycle (executed 2026-10-19/20 — the v89-era dashboard pair's fifth re-run)

The queue's own paragraph above was EXECUTED this cycle. The probe series
derived from the v89 lineage by the sed substitution families
(vlm89->vlm95, v89->v95, FOURTH->FIFTH, TWELFTH->EIGHTEENTH — the
shots' session names riding the families) PLUS the explicit second-pass
session-name substitutions (refar89->refar95, clonear89->clonear95 —
the "ar" token family, the v94 lesson applied from the start), the
headers history-corrected to the FIFTH re-run [v61 -> v68 -> v77 ->
v83 -> v89 -> v95] + "last re-shot v89" + the oldest-remaining bracket
[v89 < v90 < v91 < v92 < v93 < v94] + the v89-era-pair (not v61-era)
correction + the "after v89-v94" (not "after v83-v88") correction; the
functional bodies verified version-bump-only by the normalize-back
diff (only the intentional history-correction comment lines differ).
The new probes this cycle: vlm-shots-v95.sh + clone-vlmshots-v95.sh +
vlm-compare-v95.mjs + arbit-v95.sh (the intermediate combined form,
header-corrected) + build-twohalf-v95.py (the two-half builder — the
THREE census blocks [ARBIT_G/ARBIT_Q/ARBIT_X] extracted once, embedded
byte-identically across the halves by the md5 line-block contract
[b500dd29 / da04e995 / 7a381755]) + ref-arbit-v95.sh +
clone-arbit-v95.sh + build-qa-timing-v95.py + qa-timing-arbit-v95.sh +
qa-timing-clone-v95.sh (the supplemental one-shot for the v95 pin's own
axes, BUILT two-half from the start — the census JS byte-identical by
the md5 line-block diff [ba296202]) + ref-standing-v89.sh +
standing-checks-v89.sh (the 89th standing checks, version-bumped from
the v88 pair across the three token families).

The verdict: IDENTICAL — ZERO style flags on the pair's own target
surfaces (the Budget Guidelines card and the Quick Action cards both
"visually identical" per the VLM's own targeted analysis) — the THIRD
consecutive IDENTICAL verdict for this pair [v83 -> v89 -> v95]. The
only flags the documented standing classes: the seed-data figures (the
allocation bar 30.5%-vs-62.8%, the balance $3475-vs-$2065, the stat
figures, the donut proportions), the root-URL active-nav highlight
(the v56 SUPERSET class), the "Edit with Base44" FAB (the
platform-chrome class), and the avatar "U" vs "D" (the user-identity
class).

The both-sides census — executed in the TWO-HALF controlled form BUILT
two-half from the start — REPRODUCED the v89 census values EXACTLY
(zero drift on every axis): PART G the guidelines card 468x348/radius
12px/border/bg/the header pad 24px/fs 16px/fw 600/rgb(26,58,46)/lh
16px/tracking -0.4px/the body pad 0px 24px 24px/the three tiles
418x78 with the Needs/Wants/Savings tints and the label/pct/desc
chrome — the only delta the shadow's transparent lead-layer count (the
v66 computed-form INVISIBLE class); PART Q the grid 304px x3/gap
24px/w 960/the three cards 304x90/radius 16px/pad 24px/white/border/
the 40x40 tinted tiles/the 20px icons/the labels/the 0.5-opacity
pluses/transition 0.2s — the TWO census deltas both documented classes
(the grid mt [ref 0px vs clone 32px — the rendered gap IDENTICAL at
340, the v77 mechanism class] and the label finder's wrapper catch
[ref leaf 500/rgb(26,58,46) vs clone wrapper 400/rgb(10,10,10) — the
v61 label lesson: the clone's LEAF span carries the identical chrome,
pinned green by the v61 F3 pin]); PART X cardBottom 1122/gridTop
1462/gap 340 on BOTH sides, byte-identical. NO NEW CLONE GAP — the v95
iteration PIN-ONLY.

The +1 e2e pin: the quick-action TRANSITION-TIMING family census at
1280 (tests/e2e/dashboard.spec.ts — the never-pinned family: the three
cards' transitionTimingFunction + transitionDelay [the v89 pin holds
the duration/property only], the three tinted tiles'
transition-transform family, and the three plus icons'
transition-opacity family — grep-verified never pinned at ANY
viewport), the pin's own axes first measured byte-identical on both
sides by the supplemental two-half census (both sides read-only; the
seedcheck exact after the run). The pin-sanity mutation: the
viewport-scoped transition-all duration-200 -> transition-all
duration-200 lg:ease-linear at dashboard-view.tsx:885 (by LINE
NUMBER, AT-lg because the pin runs at 1280; the line-scoping keeps
the file's OTHER transition-all duration-200 instance [line 578, the
breakdown category card] untouched) — ONLY the v95 pin red (41 green
under the mutation), the failure diff reads as the cardTiming axis
ALONE ("cubic-bezier(0.4, 0, 0.2, 1)" -> "linear") — cascade-free BY
CONSTRUCTION (a timing-function flip affects no geometry and no
computed style any other pin asserts; lg:ease-linear appears NOWHERE
in src/).

The screenshots: **16/16 BYTE-IDENTICAL** — the same-day-seed
byte-identity law, the THIRD consecutive pure-form cycle (the seed
planted and the shots taken on the same calendar day, byte-for-byte
reproduction, ZERO arbitration needed).

The v95 cycle's operational lessons:

- THE TEMPLATE-BRACE GENERATOR BUG: the two-half generator script
  (build-qa-timing-v95.py) was written with .format()-style doubled
  braces but applied with .replace() — the generated LOGIN_JS kept
  literal `{{`/`}}`, a JS syntax error that made agent-browser eval
  return EMPTY on every attempt (the empty-eval signature — the same
  SYMPTOM class as the v89 chromium resource exhaustion, but the
  CAUSE was the generator, not the sandbox). The diagnosis that
  separated them: a manual `agent-browser open` + `snapshot` against
  the reference (the page loaded fine — the site was UP, the script
  was broken). The discipline: bash -n + a spot grep for doubled
  braces after ANY generator run, BEFORE executing the probe; when
  the empty-eval signature appears, check the script first if a fresh
  generator produced it, and only then suspect the sandbox.
- THE TWO-HALF FORM AS THE DEFAULT (the v92/v93/v94 lesson, applied
  clean): the v95 census + the supplemental census were BOTH built
  two-half from the start (the builders extract the census blocks
  once, the md5 line-block contract) — zero resource-exhaustion
  symptoms, no mid-run splits needed, the reaping budget applied as
  the standing pre-run + between-halves step throughout.
- THE v4 TRANSITION-PROPERTY COMPUTED-FORM CLASS (NEW): Tailwind v4's
  `transition-transform` computes `transform, translate, scale,
  rotate` where v3 computed `transform` — a property-LIST superset
  with identical rendered behavior (the tile's only animated property
  `scale` covered by BOTH lists). The pin form for such axes:
  CONTAINS, never exact (the v66 shadow lead-layer / v82 labelBlock
  width / v94 margin-attribution family's newest member). The
  reference-side value was measured in the same census run — the
  class documented from LIVE both-sides evidence, not assumption.

The v96 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after this pair (the v90-era MOBILE 390 twins [the /networth + the
dashboard FULL-PAGE pair at 390x844], last re-shot v90 — now the
oldest remaining [v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH
re-run [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96] — verify the
surface names against vlm-shots-v90.sh's own header before the
derivation), (2) the axe-core watch at its next re-check point (only a
5.x wrapper changes the calculus), (3) the deferred reference-write
censuses (unchanged — out of bounds under the v46 read-only rule).
"""

def main():
    # D4 — zero-balance_SKILL.md: the state line + the Session 130 row.
    t = open("zero-balance_SKILL.md").read()
    changed = 0
    if "108 unit tests / 297 e2e tests / 35 smoke steps" in t:
        t = t.replace("108 unit tests / 297 e2e tests / 35 smoke steps",
                      "108 unit tests / 298 e2e tests / 35 smoke steps", 1)
        changed += 1
    anchor = "| 2026-10-19 | Session 129 — parity iteration v94"
    if anchor in t and "Session 130 — parity iteration v95" not in t:
        idx = t.index(anchor)
        line_end = t.index("\n", idx) + 1
        t = t[:line_end] + SKILL_ROW + t[line_end:]
        changed += 1
    open("zero-balance_SKILL.md", "w").write(t)
    print(f"D4 zero-balance_SKILL.md: {changed} edits applied")

    # D5 — PAD: the v1.1.52 revision block before v1.1.51.
    t = open("Project_Architecture_Document.md").read()
    anchor = "#### Revision Block — v1.1.51 (Tracked Changes)"
    if anchor in t and "Revision Block — v1.1.52" not in t:
        t = t.replace(anchor, PAD_BLOCK + anchor, 1)
        open("Project_Architecture_Document.md", "w").write(t)
        print("D5 PAD: v1.1.52 revision block inserted")
    else:
        print("D5 PAD: already present")

    # D6 — the probe README: the v95 section + the v96 queue appended.
    t = open("scripts/parity-probes/README.md").read()
    if "## The v95 cycle (executed" not in t:
        if not t.endswith("\n"):
            t += "\n"
        t += PROBE_SECTION
        open("scripts/parity-probes/README.md", "w").write(t)
        print("D6 probe README: v95 section + v96 queue appended")
    else:
        print("D6 probe README: already present")

if __name__ == "__main__":
    main()
