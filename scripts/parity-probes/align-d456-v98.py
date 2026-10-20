#!/usr/bin/env python3
"""align-d456-v98.py — D4 zero-balance_SKILL.md (Session 133 audit row +
the state line), D5 the PAD's v1.1.55 revision block, D6 the probe
README's v98 section (+ the lessons + the v99 queue)."""
import sys

SKILL_ROW = """| 2026-10-20 | Session 133 — parity iteration v98 (`docs/remediation-plan-v98.md`) | **The re-run cycle's next-oldest candidate (the v92-era SAVINGS pair's sixth re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98] — the SAVINGS view at desktop 1280x800, full-page, last re-shot v92; the twenty-first consecutive queue/ledger agreement) + the axe watch (NO DRIFT) + the goal-card action-menu panel/menuitem-resting census pin at 1280 (PIN-ONLY — no production-code change; +1 e2e = 301)**: the verdict DIFFERENT with every flag DOM-arbitrated to a documented class — the "Card Footer Alignment" the v57 DATA-CONDITIONAL class (the census proving the footer childCount 1-vs-2 with the clone's "Brokerage" chip, the reference RENDERING payment chips when data carries them per the v97 income-card evidence), the card grid the seed-count class (1 vs 2), the header subtitle + card contents the seed-data classes, the avatar the user-identity class; the two-half census (BUILT two-half from the start — the SV_CENSUS_JS block [153 lines] md5-identical [31d181ed] across the halves) reproducing the v86/v92 values exactly (zero drift on every axis); the +1 pin the ACTION-MENU PANEL + MENUITEM-RESTING interior (the v97 missing-middle lesson applied to the ACTION layer — the G5/G9 pins hold the menu ITEM's COLOR family + the CONTENT's border-COLOR only; the menu PANEL's GEOMETRY + the menuitem's RESTING interior never pinned at ANY viewport in ANY spec; the panel w/h + itemCount DATA-INDEPENDENT [the structural Edit+Delete pair: 2×32 + 2×4 pad + 2×1 border = 74] — the axes assert the cross-side-verified values directly), the pin's own axes first measured byte-identical on both sides by the supplemental two-half census (menu-arbit-v98.sh + menu-clone-v98.sh, the census JS md5 0f83b786; both sides read-only — a menu OPEN only, no item clicks); the mutation rounded-md → rounded-lg at ui/dropdown-menu.tsx:20 (only the v98 pin red — the panel radius axis alone, cascade-free; the line-scoping keeps the item's rounded-sm at line 36 untouched); the census discoveries: the reference's action trigger is UNLABELLED (the clone's "Actions for …" is the a11y superset — the cross-side finder is GEOMETRIC [the textless 36×36 svg button]) and the reference's menu opens only on the full POINTER EVENT SEQUENCE (a bare el.click() opens the clone's Radix menu but NOT the reference's); the screenshots 10/16 byte-identical + 6/16 the fresh-reseed DATE class (pixel-arbitrated by pixel-diff-v98.py — every differing region a date-digit span or a max-channel-2 sub-perceptual re-render region, the v68 calculator precedent; the VLM crop re-read over-read the sub-threshold noise as a "missing border" — the measurement is the authority, the v43 rule); the lessons: the reference pointer-event family + the unlabelled-trigger finder class + the data-independent panel |** 108/301/35 green |
"""

PAD_BLOCK = """#### Revision Block — v1.1.55 (Tracked Changes)
- `[UI]` v1.1.55 (2026-10-20) — the v98 parity iteration (PIN-ONLY — no production-code change): the counts 108 unit / **301 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the v92-era SAVINGS pair's SIXTH re-run [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98] — the SAVINGS view at desktop 1280x800, full-page, last re-shot v92; the twenty-first consecutive queue/ledger agreement, the surface names verified against vlm-shots-v92.sh's own header before the derivation) + the axe watch (NO DRIFT — 4.14.0 npm-latest, only rc/next sha prereleases beyond, no stable 4.14.1, no 5.x; the v68 dedupe holds; the engine-contract pin 2 passed standalone) + the 92nd standing checks (the mobile menu verified the 92nd consecutive time; the reference's four bugs all live; the data census the 92nd clean drift check — clean on the FIRST read)**: the verdict DIFFERENT with every flag DOM-arbitrated to a documented class (the "Card Footer Alignment" the v57 DATA-CONDITIONAL class [the footer childCount 1-vs-2 with the clone's "Brokerage" chip]; the card grid the seed-count class [1 vs 2]; the header subtitle + card contents the seed-data classes; the avatar the user-identity class); the both-sides census — executed in the TWO-HALF controlled form BUILT two-half from the start (ref-arbit-v98.sh + clone-arbit-v98.sh via build-twohalf-v98.py, the ONE census JS block [SV_CENSUS_JS 153 lines] byte-identical across the halves by the md5 line-block contract [31d181ed]) — REPRODUCING the v86/v92 census values EXACTLY (the h1/grid/card/cardTitle/titleRow/cardAmount/footer/badge families; the docSW 1280 guard); NO NEW CLONE GAP; the +1 e2e pin the goal-card ACTION-MENU PANEL + MENUITEM-RESTING interior census at 1280 (tests/e2e/items.spec.ts — the v97 missing-middle lesson applied to the ACTION layer: the G5/G9 pins hold the menu ITEM's COLOR family + the CONTENT's border-COLOR, the v35 S1 the keyboard contract, but the menu PANEL's GEOMETRY [bg/radius/shadow/min-w/overflow/z/w/h] and the menuitem's RESTING interior [fs/fw/pad/radius/lh/h] were never pinned at ANY viewport in ANY spec — the coverage-map grep across all 24 specs; the pin's own axes first measured byte-identical on both sides by the supplemental two-half census menu-arbit-v98.sh + menu-clone-v98.sh via build-menu-v98.py, the census JS byte-identical by the md5 line-block diff 0f83b786]); the pin-sanity mutation rounded-md -> rounded-lg at src/components/ui/dropdown-menu.tsx:20 (by LINE NUMBER; the line-scoping keeps the DropdownMenuItem's own rounded-sm at line 36 untouched [the item's 4px radius axis]): ONLY the v98 pin red (42 green under the mutation), the failure diff reads as the panel radius axis ALONE ("6px" -> "8px") — cascade-free BY CONSTRUCTION (no spec asserts any dropdown-menu panel radius — this pin is the first; the v97 listbox panel radius reads select.tsx's SelectContent, a DIFFERENT component; the tokens G5 contentBorder is the border-COLOR axis), then restored (git diff src/ = 0; the standalone REBUILD; the post-restore full run 43/43 green); the F5 chain 136+96+71 = 303 chunk executions = 301 unique tests, zero flakes; the screenshots **10/16 BYTE-IDENTICAL + 6/16 the fresh-reseed DATE class** (the fresh-clone re-seed re-anchoring the seed's isoDate offsets — db/ is gitignored, it does not travel; every differing region pixel-arbitrated to a date-digit span or a max-channel-2 sub-perceptual re-render region, the v68 calculator precedent); the census discoveries: the reference's action trigger is UNLABELLED (the clone's aria-label is the a11y superset — the cross-side finder is GEOMETRIC) and the reference's menu opens only on the full POINTER EVENT SEQUENCE; the operational lessons: the reference pointer-event family, the unlabelled-trigger finder class, and the data-independent panel.
"""

README_SECTION = """
## v98 — the savings pair's sixth re-run + the goal-card action-menu pin (2026-10-20)

The cycle (`docs/remediation-plan-v98.md` — the plan validated against
the codebase before execution; the narrative: `docs/session_236.md`):
the v97-era docs' v98 queue suggestion agreeing with the rotation
ledger — the TWENTY-FIRST consecutive agreement (the surface names
verified against vlm-shots-v92.sh's own header before the derivation,
the queue-prose verification lesson applied) — the v92-era SAVINGS pair
(the savings view at desktop 1280x800, full-page, last re-shot v92; the
pair's SIXTH re-run [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98]),
plus the axe watch at its re-check point (NO DRIFT: 4.14.0 npm-latest,
no stable beyond, no 5.x, the v68 dedupe holds) and the 92nd standing
checks (ref-standing-v92.sh + standing-checks-v92.sh, version-bumped
from v91 across the three token families — version-bump-only diffs
verified by normalizing back and diffing clean; the persisted
derive-standing-v98.py).

The workspace REBUILT (the fresh-clone path, the v86/v88/v90/v91/v92
precedent — the sandbox had been reset): git clone at main @ 9152c18,
the tree clean; the environment re-provisioned (npm install; .env
written [DATABASE_URL="file:../db/custom.db"]; db/ at the repo root,
db:generate + db:push + db:seed; chromium-1243 installed for the pinned
@playwright/test 1.63.0 — the cache's pre-installed 1200 build belongs
to a different playwright generation, the first e2e chunk failed with
"Executable doesn't exist" until the install; the
/home/z/my-project/tool-results/ dir re-created for with-server.sh); the
seedcheck exact before any flow (7 items / rent 1850 / expensesTotal
2235 / 0 line items / 3 assets / 2 liabilities); the full baseline
chain green on the first run after the browser install (lint ->
typecheck -> 108 unit -> build [robots + sitemap prerendered] -> 300
e2e [135+96+71 = 302 chunk executions = 300 unique, zero flakes] ->
35/35 smoke). The two commits since the v97 push (d4b77c5 + 9152c18)
audited session-log-only (session_234.md + session_235.md — ZERO src/
or lockfile deltas).

The probe series (the v92 lineage, derived via the PERSISTED
derive-v98-series.py — the generic swaps then the exact-fragment
history corrections, every correction's hit/miss REPORTED; the one
first-run MISS [the arbit header's line break — "(the savings view
full-page —\n# the v86-era..." vs the assumed "...full-page — the\n#..."]
caught by the report itself and fixed before any probe executed — the
v96 miss-report discipline; bash -n + node --check clean on all four;
zero residual old tokens):
- vlm-shots-v98.sh — the REFERENCE side (login on the first attempt;
  the parked pointer at (5,5); read-only — the v46 rule).
- clone-vlmshots-v98.sh — the CLONE side (the with-server :3200 parity
  server).
- vlm-compare-v98.mjs — the VLM pairwise.
- arbit-v98.sh — the both-sides census (the v86/v92 axes re-measured;
  the census runs regardless of the verdict — the v75 convention).
- ref-arbit-v98.sh + clone-arbit-v98.sh — the TWO-HALF controlled form,
  BUILT two-half from the start via build-twohalf-v98.py (the
  SV_CENSUS_JS block [153 lines] extracted once and embedded
  byte-identically across the halves — the md5 line-block contract
  [31d181ed]). The reference half's first run hit the 300s tool
  timeout with buffered output (the census itself completed — the
  login/census/done markers all present in the partial output); the
  re-run with the output streamed completed clean. The reaping budget
  applied between every half.
- menu-arbit-v98.sh + menu-clone-v98.sh — the supplemental one-shot
  two-half census for the pin's own axes (the v87..v97 precedent),
  BUILT two-half from the start via build-menu-v98.py (the census JS
  md5 0f83b786 — 42 lines — byte-identical across the halves).
- pixel-diff-v98.py + inspect-diff-v98.py — the screenshot DATE-class
  arbitration (the v68/v92/v96 discipline, programmatic PIL diffs;
  never a VLM verdict for the acceptance).

The findings:
1. The verdict DIFFERENT, every flag DOM-arbitrated to the documented
   classes (the v57 DATA-CONDITIONAL footer [the census proving the
   footer childCount 1-vs-2 with the clone's "Brokerage" chip]; the
   seed-count grid [1 vs 2]; the seed-data figures/badges/subtexts;
   the user-identity avatar; no FAB flag this cycle — the platform
   iframe chrome absent from this verdict's flag set, same as v92).
2. The both-sides census (the two-half form) REPRODUCES the v86/v92
   census values EXACTLY — zero drift on every axis (the h1/grid/card/
   cardTitle/titleRow/cardAmount/footer/badge families; the docSW 1280
   guard; the clone template's last-column sub-pixel the documented
   column-distribution rounding noise). NO NEW CLONE GAP — the
   iteration PIN-ONLY.
3. The v98 pin (+1 e2e = 301): the goal-card ACTION-MENU PANEL +
   MENUITEM-RESTING interior census at 1280 (tests/e2e/items.spec.ts —
   the v97 missing-middle lesson applied to the ACTION layer: the
   tokens G5/G9 pins hold the menu ITEM's COLOR family [editRest
   rgb(10,10,10) / deleteColor rgb(220,38,38) / the focus-state bg] +
   the CONTENT's border-COLOR on the income view, the v35 S1 pin the
   keyboard contract — but the menu PANEL's GEOMETRY {bg/radius/shadow/
   min-w/overflow/z/w/h} and the menuitem's RESTING interior {fs/fw/
   pad/radius/lh/h} were NEVER pinned at ANY viewport in ANY spec — the
   coverage-map grep across all 24 specs; the panel {bg white, radius
   6px, border 1px rgb(229,229,229), minW 128px, overflow hidden, z 50,
   pos static, w 128, h 74} + the shadow-md VISIBLE layers via
   toContain [the v37 O1 v3/v4-construct precedent] + the item0
   {fs 14px, fw 400, color rgb(10,10,10), pad 6px 8px, radius 4px,
   lh 20px, h 32} + the itemCount 2 + the docSW 1280 guard — the panel
   w/h + itemCount DATA-INDEPENDENT [the structural Edit+Delete pair:
   2x32 + 2x4 pad + 2x1 border = 74], so unlike the v97 pin's
   clone-only guards these axes assert the cross-side-verified values
   directly) — the pin's own axes first measured byte-identical on
   both sides by the supplemental two-half census — GREEN on first
   run.
4. The pin-sanity mutation (the executed form — the DropdownMenuContent
   panel's rounded-md -> rounded-lg at src/components/ui/dropdown-menu.
   tsx:20, by LINE NUMBER; the line-scoping keeps the DropdownMenuItem's
   own rounded-sm at line 36 untouched): the failure diff reads as the
   panel radius axis alone ("6px" -> "8px"); the full items.spec.ts
   under the mutation reads ONLY the v98 pin red (42 green) —
   cascade-free BY CONSTRUCTION (no spec asserts any dropdown-menu
   panel radius — this pin is the first; the v97 listbox panel radius
   6px reads select.tsx's SelectContent, a DIFFERENT component; the
   tokens G5 contentBorder is the border-COLOR axis, not radius) —
   NOTE the mutation only bites after the standalone REBUILD (the e2e
   runs the PREBUILT standalone server; the first mutation run against
   the stale build read 43 green — the rebuild-then-test discipline);
   restored (git diff src/ = 0; the standalone REBUILD; the
   post-restore full run 43/43 green).
5. The full chain re-run GREEN: lint -> typecheck -> 108 unit -> build
   -> 301 e2e (136+96+71 = 303 chunk executions, zero flakes) ->
   35/35 smoke; the screenshots 10/16 BYTE-IDENTICAL + 6/16 the
   fresh-reseed DATE class (the fresh-clone re-seed re-anchoring the
   seed's isoDate offsets to the new seed day — db/ is gitignored, it
   does not travel; every differing region pixel-arbitrated by
   pixel-diff-v98.py: 03-income 2 date spans, 04-expenses 3,
   05-savings 2, 06-networth 1, 16-item-details 1 date span + two
   max-channel-2 sub-perceptual re-render regions, 08-calculator one
   77x77 max-channel-2 region — the v68 calculator precedent, below
   the ~2.5 JND; the VLM crop re-read over-read the sub-threshold
   noise as a "missing border" — the measurement is the authority, the
   v43 rule).

The operational lessons (the D6 section):
- THE REFERENCE POINTER-EVENT FAMILY (NEW): the reference's React tree
  opens its ellipsis dropdown only on the full pointer event SEQUENCE
  (pointerdown -> mousedown -> pointerup -> mouseup -> click); a bare
  synthetic el.click() opens the clone's Radix menu but NOT the
  reference's. Any future census that must OPEN reference-side
  interactive chrome dispatches the full sequence.
- THE UNLABELLED-TRIGGER FINDER CLASS (NEW): the reference's card
  action trigger carries NO aria-label (the clone's "Actions for ..."
  is the a11y superset — the v38 search-input aria-label note's
  sibling) — cross-side finders for action chrome must be GEOMETRIC
  (the textless 36x36 svg button), with the clone-only aria-label
  reserved for the e2e pin's locator.
- THE DATA-INDEPENDENT PANEL: the action menu's Edit+Delete pair is
  STRUCTURAL (both sides render exactly 2 items), so the panel w/h +
  itemCount are data-independent — these axes assert cross-side-
  verified values directly (unlike the v97 pin's clone-only h/optCount
  guards).
- THE MUTATION-REBUILD DISCIPLINE: a pin-sanity mutation only bites
  after the standalone REBUILD (the e2e runs the PREBUILT
  .next/standalone server) — a mutation run against the stale build
  reads green and proves nothing.

The v99 queue (suggestions — verify against the rotation ledger before
executing): (1) the re-run cadence rotates to the next-oldest candidate
after the savings pair (the v93-era LOGIN + CALCULATOR pair [the login
view + the calculator card pair at desktop 1280x800], last re-shot v93 —
now the oldest remaining [v93 < v94 < v95 < v96 < v97 < v98]; the
pair's re-run bracket to be verified against vlm-shots-v93.sh's own
header before the derivation), (2) the axe-core watch at its next
re-check point (only a 5.x wrapper changes the calculus), (3) the
deferred reference-write censuses (unchanged — out of bounds under the
v46 read-only rule).
"""

def main():
    ok = True
    # D4: zero-balance_SKILL.md — the Session 133 row after the Session 132 row
    text = open("zero-balance_SKILL.md", encoding="utf-8").read()
    if "Session 133 — parity iteration v98" in text:
        print("D4: Session 133 row already present")
    else:
        anchor_row = None
        for line in text.split("\n"):
            if line.startswith("| 2026-10-20 | Session 132 — parity iteration v97"):
                anchor_row = line
                break
        if not anchor_row:
            print("D4 MISS: Session 132 row"); ok = False
        else:
            idx = text.index(anchor_row) + len(anchor_row)
            text = text[:idx] + "\n" + SKILL_ROW.rstrip("\n") + text[idx:]
            open("zero-balance_SKILL.md", "w", encoding="utf-8").write(text)
            print("D4: SKILL Session 133 row inserted after the Session 132 row")

    # D5: PAD — the v1.1.55 revision block before v1.1.54
    text = open("Project_Architecture_Document.md", encoding="utf-8").read()
    if "Revision Block — v1.1.55" in text:
        print("D5: v1.1.55 block already present")
    else:
        anchor = "#### Revision Block — v1.1.54 (Tracked Changes)"
        if anchor not in text:
            print("D5 MISS: v1.1.54 anchor"); ok = False
        else:
            idx = text.index(anchor)
            text = text[:idx] + PAD_BLOCK + "\n" + text[idx:]
            open("Project_Architecture_Document.md", "w", encoding="utf-8").write(text)
            print("D5: PAD v1.1.55 revision block inserted before v1.1.54")

    # D6: the probe README — the v98 section at the tail (after the v98 queue)
    text = open("scripts/parity-probes/README.md", encoding="utf-8").read()
    if "## v98 — the savings pair's sixth re-run" in text:
        print("D6: v98 section already present")
    else:
        # the v98 queue's closing paragraph is the current tail; the v98
        # section (with its own v99 queue) replaces nothing — appended.
        text = text.rstrip("\n") + "\n" + README_SECTION
        open("scripts/parity-probes/README.md", "w", encoding="utf-8").write(text)
        print("D6: probe README v98 section appended at the tail")

    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
