#!/usr/bin/env python3
"""D4-D6 docs alignment for the v110 cycle (Session 145) — part 2.

D4 zero-balance_SKILL.md — the project_state line + the Session 145 review row
               above Session 144's.
D5 PAD        — the v1.1.67 revision block above v1.1.66's.
D6 probe README — the v110 section (lineage + lessons) + the v111 queue
               replacing the v110 queue.
Every edit is assert-applied; a miss fails the run.
"""
import sys


def edit(path, pairs, must=True):
    t = open(path, encoding="utf-8").read()
    for old, new in pairs:
        if old not in t:
            print(f"MISS in {path}: {old[:70]!r}")
            if must:
                sys.exit(1)
        t = t.replace(old, new, 1)
    open(path, "w", encoding="utf-8").write(t)
    print(f"aligned {path} ({len(pairs)} edits)")


# ---------------- D4: zero-balance_SKILL.md ----------------
edit(
    "zero-balance_SKILL.md",
    [
        (
            "project_state: 108 unit tests / 312 e2e tests / 35 smoke steps — all green",
            "project_state: 108 unit tests / 313 e2e tests / 35 smoke steps — all green",
        ),
    ],
)

SESSION_145_ROW = (
    "| 2026-10-24 | Session 145 — parity iteration v110 (`docs/remediation-plan-v110.md`) | "
    "**The re-run cycle's next-oldest candidate (the v104-era SAVINGS pair's EIGHTH re-run "
    "[v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110] — the SAVINGS view at desktop "
    "1280×800 FULL-PAGE, the v58-era savings pair's surface, last re-shot v104, now the oldest "
    "remaining [v104 < v105 < v106 < v107 < v108 < v109]; the THIRTY-THIRD consecutive "
    "queue/ledger agreement — the surface names verified against vlm-shots-v104.sh's own header "
    "before the derivation) + THE SECURITY BUMP (the cycle's FIX item — the first "
    "production-dependency change since the v68 axe-core bump: npm audit added to the F0b audit "
    "for the first time surfaced next 16.4.0 CRITICAL [three advisories published 2026-10-22 — "
    "the Image-Optimization SVG RCE, the Server-Actions DoS, the use-cache RCE — ALL THREE PATHS "
    "UNEXPOSED in this codebase: no next/image, no 'use cache', no Server Actions] + zod 4.6.5 "
    "HIGH [the oversized-collection memory exhaustion — the one real, bounded exposure: zod "
    "validates the PUBLIC register/login inputs, rate-limited 10/IP/15min]; the fix `npm audit "
    "fix` → next 16.4.3 + zod 4.6.7, BOTH within the existing caret ranges so package.json is "
    "UNTOUCHED and only the lockfile's 43 version pins moved; npm audit 0 vulnerabilities; the "
    "re-verification: quick gates green on the bumped tree + the 104th standing checks against "
    "the BUMPED standalone build + the full 313-e2e ship chain + the screenshots byte-compare) + "
    "the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the 104th standing checks "
    "(ALL GREEN — the mobile menu working the 104th consecutive time; the reference's four bugs "
    "all live; the census clean on the first read) + the rail nav-block interior census pin at "
    "1280 (PIN-ONLY; +1 e2e = 313)**: the verdict SAVINGS DIFFERENT (the pair's documented "
    "flag-set class) with every flag DOM-arbitrated to a documented class (the payment-chip "
    "footer the v57 DATA-CONDITIONAL class [ref childCount 1 date-only vs clone 2 with the "
    "'Brokerage' chip]; the card grid 1-vs-2 the seed-count class; the header stats + card "
    "contents the seed-data classes; the avatar the user-identity class; NO FAB flag raised — "
    "the disproof not required); the two-half census (SV_CENSUS_JS 153 lines, md5 891ab9b6 — "
    "the v98/v104 census block verbatim, the builder-form md5 verified against the EXISTING "
    "v104 halves) reproduces the v104 values exactly on every axis (the card h 200-vs-230 the "
    "v57/v70b Recurring-wrap class [badgeRow 22 vs 52]) — NO NEW CLONE GAP; the +1 pin "
    "(tests/e2e/nav-geometry.spec.ts) the rail's NAV-BLOCK INTERIOR family at 1280 on /savings "
    "— the block between the v104 brand-block pin and the v103 user-footer pin, never pinned "
    "at ANY viewport in ANY spec: the 'Navigation' label {32px/12px/600/uppercase/0.6px/"
    "rgb(45,90,74)/8px 12px/6px radius/flex center} + the UL {flex column/gap 4px/215 wide/5 "
    "links} + the LI {relative/mb 0/36px} + the link box {32px/10px 12px/12px gap/14px/400/8px "
    "radius — the session-5 controls re-walked} + the nav ICON {16×16} + the label SPAN's "
    "truncate family {14px/hidden/ellipsis/nowrap} + the ACTIVE link {the 135deg "
    "forest-medium→lime gradient/white/500/32px} — measured byte-identical both sides via the "
    "one-shot nav-arbit-v110.sh (the reference-side finder STRUCTURAL — its documented "
    "no-landmark bug means no nav element; the ul found by its 5-anchor shape, the label by "
    "the wrapper-sibling walk), mutation-verified single-axis AND cascade-free (h-4 w-4 → "
    "h-4 w-5 at sidebar.tsx:96 line-scoped — the ONLY h-4 w-4 in the file, the burger toggle's "
    "icon the [&_svg]:size-4 form — only the v110 pin red at the icon.w axis alone [16 → 20] "
    "after the rebuild; zero specs assert the nav icons' computed w/h); the ship 313 e2e zero "
    "flakes (81+81+78+76 = 316 executions = 313 unique); 35/35 smoke; the screenshots 10/16 "
    "byte-identical + SIX fresh-seed deltas ALL arbitrated (the +1-day rolls on the four "
    "item-view date footers + the details sheet's Date FactRow — VLM glyph-read ['Oct 18' → "
    "'Oct 19', 'October 14, 2026' → 'October 15, 2026']; the 08/16 y817-900 bands the "
    "v105-documented backdrop-blur scrim rounding drift [maxDelta 1-2, zero glyphs] — zero "
    "structural bands, the updated set committed); the dev evidence re-captured + VLM-verified "
    "(the menu proof: /income, docSW 390, navLandmark true); the PHANTOM-GLITCH DISPEL (the "
    "v107-era 'save glitch' never existed — od-hexdump verifies all committed dev scripts "
    "byte-correct on disk; the '[h' loss a display-layer artifact of the tool-output pipeline) "
    "|** 108/313/35 green |\n"
)
t = open("zero-balance_SKILL.md", encoding="utf-8").read()
i = t.find("| 2026-10-24 | Session 144 — parity iteration v109 (`docs/remediation-plan-v109.md`)")
assert i >= 0, "SKILL Session 144 row not found"
t = t[:i] + SESSION_145_ROW + t[i:]
open("zero-balance_SKILL.md", "w", encoding="utf-8").write(t)
print("aligned zero-balance_SKILL.md (Session 145 row inserted)")

# ---------------- D5: PAD ----------------
V117_PAD_BLOCK = (
    "#### Revision Block — v1.1.67 (Tracked Changes)\n"
    "- `[UI]` v1.1.67 (2026-10-24) — the v110 parity iteration (PIN-ONLY for src/ — no "
    "production-code change; the cycle's FIX item is the SECURITY BUMP: `npm audit` added to "
    "the F0b audit for the first time surfaced next 16.4.0 CRITICAL [three 2026-10-22 "
    "advisories — the Image-Optimization SVG RCE, the Server-Actions DoS, the use-cache RCE — "
    "ALL THREE PATHS UNEXPOSED in this codebase: no next/image, no 'use cache', no Server "
    "Actions] + zod 4.6.5 HIGH [the oversized-collection memory exhaustion — the one real, "
    "bounded exposure: zod validates the PUBLIC register/login inputs, rate-limited "
    "10/IP/15min]; the fix `npm audit fix` → next 16.4.3 + zod 4.6.7, BOTH within the "
    "existing caret ranges so package.json is UNTOUCHED and only the lockfile's 43 version "
    "pins moved [the 9 @next/swc platform binaries + @next/env in lockstep]; npm audit: 0 "
    "vulnerabilities; the re-verification: quick gates green on the bumped tree + the 104th "
    "standing checks against the BUMPED standalone build + the full 313-e2e ship chain + the "
    "screenshots byte-compare [10/16 byte-identical — the bump produced ZERO visual drift; "
    "the six deltas all the documented fresh-seed date-roll + scrim classes]): the counts "
    "108 unit / **313 e2e** (+1) / 35 smoke; **the re-run cycle's next-oldest candidate (the "
    "v104-era SAVINGS pair's EIGHTH re-run [v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> "
    "v104 -> v110] — the SAVINGS view at desktop 1280x800 FULL-PAGE, the v58-era savings "
    "pair's surface, last re-shot v104; the THIRTY-THIRD consecutive queue/ledger agreement) "
    "+ the axe watch (NO DRIFT — 4.14.0 holds, the v68 dedupe verified) + the 104th standing "
    "checks (ALL GREEN — the mobile menu working the 104th consecutive time; the reference's "
    "four bugs all live; the census clean on the first read) + the rail nav-block interior "
    "census pin at 1280 (PIN-ONLY; +1 e2e = 313)**: the verdict SAVINGS DIFFERENT (the pair's "
    "documented flag-set class) with every flag DOM-arbitrated to a documented class (the "
    "payment-chip footer the v57 DATA-CONDITIONAL class; the card grid 1-vs-2 the seed-count "
    "class; the header stats + card contents the seed-data classes; the avatar the "
    "user-identity class; NO FAB flag — the disproof not required); the two-half census "
    "(SV_CENSUS_JS 153 lines, md5 891ab9b6 — the v98/v104 census block verbatim, the "
    "builder-form md5 verified against the EXISTING v104 halves) reproduces the v104 values "
    "exactly on every axis — NO NEW CLONE GAP; the +1 pin (tests/e2e/nav-geometry.spec.ts) "
    "the rail's NAV-BLOCK INTERIOR family at 1280 on /savings — the 'Navigation' label "
    "{32px/12px/600/uppercase/0.6px/rgb(45,90,74)} + the UL {flex column/gap 4px/5 links} + "
    "the LI {relative/36px} + the link box controls + the nav ICON {16x16} + the span "
    "truncate family + the ACTIVE link {the 135deg gradient/white/500} — measured "
    "byte-identical both sides via the one-shot nav-arbit-v110.sh; the mutation h-4 w-4 -> "
    "h-4 w-5 at sidebar.tsx:96 line-scoped — only the v110 pin red at the icon.w axis alone "
    "after the rebuild (cascade-free by construction: zero specs assert the nav icons' "
    "computed w/h); restored, rebuilt, post-restore 11/11 green; the ship chain 313 e2e "
    "zero flakes (81+81+78+76 = 316 executions across four chunks), 35/35 smoke, the "
    "screenshots 10/16 byte-identical + SIX fresh-seed deltas all arbitrated (the +1-day "
    "date rolls VLM glyph-read + the v105-documented scrim rounding drift — zero structural "
    "bands), the dev evidence re-captured + VLM-verified; the PHANTOM-GLITCH DISPEL (the "
    "v107-era 'save glitch' never existed — od-verified: all committed dev scripts "
    "byte-correct on disk; the '[h' loss a display-layer artifact).\n\n"
)
t = open("Project_Architecture_Document.md", encoding="utf-8").read()
anchor = "#### Revision Block — v1.1.66 (Tracked Changes)"
i = t.find(anchor)
assert i >= 0, "PAD v1.1.66 block not found"
t = t[:i] + V117_PAD_BLOCK + t[i:]
open("Project_Architecture_Document.md", "w", encoding="utf-8").write(t)
print("aligned Project_Architecture_Document.md (v1.1.67 block inserted)")

# ---------------- D6: probe README ----------------
V110_PROBE_SECTION = (
    "### The v110 cycle (Session 145) — the v104-lineage derivation\n\n"
    "- `derive-v110-series.py` (persisted) — the v110 series derived from\n"
    "  the v104 lineage: vlm-shots-v110.sh + clone-vlmshots-v110.sh +\n"
    "  vlm-compare-v110.mjs + arbit-v110.sh; the generic swaps + the NINE\n"
    "  exact-fragment history corrections (the plan-source fragment reads\n"
    "  `v103 plan's` NOT `the v103 plan's` — the 'the' sits at the END of\n"
    "  the preceding line, a live derivation discovery; last-re-shot\n"
    "  v98->v104, the era marker v98-era->v104-era, SEVENTH->EIGHTH, the\n"
    "  re-run bracket extension [v58 -> ... -> v98 -> v104 -> v110], the\n"
    "  oldest-remaining bracket [v104 < v105 < ... < v109],\n"
    "  TWENTY-SEVENTH->THIRTY-THIRD, the queue-source v103 plan -> v109\n"
    "  plan) — 9/9 on the FIRST run (11 hit-checks), zero residuals,\n"
    "  line-count-preserving on all four (49/41/38/261).\n"
    "- `derive-build-twohalf-v110.py` (persisted) + `build-twohalf-v110.py`\n"
    "  — the builder derivation (the swap-order lesson: the GENERIC version\n"
    "  swap FIRST, the lineage-note fixups LAST so no later swap re-touches\n"
    "  the inserted tokens; normalize-back verified) + the two-half builder\n"
    "  (SV_CENSUS_JS 153 lines, md5 891ab9b6 — the v98/v104 census block\n"
    "  VERBATIM, the builder-form md5 verified against the EXISTING v104\n"
    "  halves): ref-arbit-v110.sh + clone-arbit-v110.sh, the census JS\n"
    "  byte-identical across the halves.\n"
    "- `derive-standing-v110.py` — the 104th standing pair\n"
    "  (ref-standing-v104.sh + standing-checks-v104.sh) from the v103\n"
    "  pair, the THREE token families (the ordinal token's suffix flip\n"
    "  103rd->104th), normalize-back verified version-bump-only.\n"
    "- `nav-arbit-v110.sh` — the ONE-SHOT both-sides census of the RAIL's\n"
    "  NAV-BLOCK INTERIOR family (the v110 pin's own axes measured\n"
    "  byte-identical on both sides at 1280x800 on /savings before the\n"
    "  pin): the 'Navigation' label {32px/12px/600/uppercase/0.6px/\n"
    "  rgb(45,90,74)/8px 12px/6px radius} + the UL {flex column/gap 4/5\n"
    "  links/215 wide} + the LI {relative/mb 0/36px} + the link box\n"
    "  controls + the nav ICON {16x16} + the span truncate family + the\n"
    "  ACTIVE link {the 135deg gradient/white/500/32px}. The\n"
    "  reference-side finder is STRUCTURAL (the reference renders NO nav\n"
    "  landmark — its documented no-landmark bug): the ul is found by its\n"
    "  5-anchor shape, the label by the wrapper-sibling walk with the\n"
    "  childless-uppercase-div fallback, the active link by\n"
    "  aria-current OR the gradient OR the text.\n"
    "- `vlm-read-crops-v110.mjs` — the screenshot arbitration read for the\n"
    "  SIX fresh-seed deltas (the +1-day date rolls VLM glyph-read: 'Oct\n"
    "  18' -> 'Oct 19', 'Oct 13' -> 'Oct 14', 'October 14, 2026' ->\n"
    "  'October 15, 2026'; the 08/16 y817-900 bands the v105-documented\n"
    "  backdrop-blur scrim rounding drift [maxDelta 1-2, zero glyphs] —\n"
    "  zero structural bands, the updated set committed).\n\n"
    "### D6 — the operational lessons this cycle (v110)\n\n"
    "- THE SECURITY-BUMP RE-VERIFICATION PATH (a dependency note): the\n"
    "  first production-dependency change since v68 ran through the full\n"
    "  parity apparatus — npm audit added to the F0b audit (a NEW standing\n"
    "  audit step), the exposure analysis FIRST (all three next paths\n"
    "  unexposed; the zod exposure real but rate-limit-bounded), the\n"
    "  minimal in-range fix (package.json untouched, 43 lockfile pins),\n"
    "  then the standing checks + the VLM pair + the census + the ship\n"
    "  chain + the screenshots byte-compare ALL re-run against the bumped\n"
    "  tree — 10/16 byte-identical proves the bump produced ZERO visual\n"
    "  drift (the six deltas all the documented date-roll/scrim classes).\n"
    "- THE PHANTOM-GLITCH DISPEL (a tooling note): the v107-era 'save\n"
    "  glitch' never existed — od-hexdump verifies ALL committed dev\n"
    "  scripts (v107/v108/v109) carry the byte-correct a[href*=\n"
    "  \"income\"]:visible locator on disk; the perceived '[h' loss is a\n"
    "  DISPLAY-layer artifact (the tool-output pipeline eats the [h\n"
    "  sequence — escape-sequence filtering), never a file defect. The\n"
    "  v108/v109 comments described fixing a phantom. ANY tool output\n"
    "  showing a bracket-h sequence must be od-verified before acting on\n"
    "  it.\n"
    "- THE NO-LANDMARK FINDER RULE (a census note): a census finder must\n"
    "  never assume the clone's element semantics exist on the reference —\n"
    "  the reference's documented no-landmark bug means NO nav element on\n"
    "  its side; the first nav-arbit-v110 run returned 'no nav' until the\n"
    "  finder was rewalked STRUCTURALLY (the ul by its 5-anchor shape).\n"
    "  The reference's OWN bugs are part of the finder contract.\n"
    "- THE SWAP-ORDER RULE (a derivation note): when deriving a builder\n"
    "  script with token swaps PLUS lineage-note fixups that insert\n"
    "  version tokens, the GENERIC version swap runs FIRST and the\n"
    "  fixups LAST — else the generic swap re-touches the inserted tokens\n"
    "  (the first derive-build-twohalf-v110 attempt failed its\n"
    "  normalize-back on exactly this).\n\n"
    "The v111 queue (suggestions — verify against the rotation ledger before\n"
    "executing): (1) the re-run cadence rotates to the next-oldest candidate\n"
    "after the v104-era SAVINGS pair (the v105-era LOGIN + CALCULATOR pair —\n"
    "the LOGIN view + the CALCULATOR dialog at desktop 1280x800, last re-shot\n"
    "v105 — now the oldest remaining [v105 < v106 < v107 < v108 < v109 <\n"
    "v110]; the pair's EIGHTH re-run bracket [v59 -> v66 -> v75 -> v81 ->\n"
    "v87 -> v93 -> v99 -> v105 -> v111] to be verified against\n"
    "vlm-shots-v105.sh's own header before the derivation), (2) the axe-core\n"
    "watch at its next re-check point (only a 5.x wrapper changes the\n"
    "calculus), (3) the npm-audit watch at its re-check point (the NEW\n"
    "standing audit step — only a new advisory in the next/zod ranges\n"
    "changes the calculus), (4) the deferred reference-write censuses\n"
    "(unchanged — out of bounds under the v46 read-only rule).\n"
)
t = open("scripts/parity-probes/README.md", encoding="utf-8").read()
i = t.find("The v110 queue (suggestions")
assert i >= 0, "v110 queue anchor not found"
t = t[:i] + V110_PROBE_SECTION
open("scripts/parity-probes/README.md", "w", encoding="utf-8").write(t)
print("aligned scripts/parity-probes/README.md (v110 section + v111 queue)")
print("D4-D6 aligned")
