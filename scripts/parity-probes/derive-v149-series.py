#!/usr/bin/env python3
"""Derive the v149 probe series from the v143 lineage (the DASHBOARD at
desktop 1280x800 FULL-PAGE — the v61-era pair's FOURTEENTH re-run
[v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 →
v131 → v137 → v143 → v149]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v148-era docs' v149 queue names "the v143-era DASHBOARD pair
... the pair's FOURTEENTH re-run bracket [v61 -> v68 -> v77 -> v83 -> v89
-> v95 -> v101 -> v107 -> v113 -> v119 -> v125 -> v131 -> v137 -> v143 ->
v149] to be verified against the v143 lineage's own records" — verified
against the v143 lineage BEFORE this derivation: the v143 plan's own
header reads "the v137-era DASHBOARD pair's THIRTEENTH re-run [v61 → v68 →
v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 →
v143]" — a 14-ENTRY bracket with the THIRTEENTH ordinal (v61 the original,
the entries-minus-one convention: 14 entries − the original = 13 re-runs,
the THIRTEENTH), consistent, no off-by-one this lineage; the v143 shots
header carries the FULL bracket form. v149 = the FOURTEENTH re-run by
appending v149 to the v143 header's THIRTEENTH bracket. The SEVENTY-SECOND
consecutive queue/ledger agreement. The cadence is in its THIRD PASS, the
v143-era DASHBOARD pair the oldest remaining [v143 < v144].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE
— the fragments below were byte-extracted programmatically from the
post-swap simulation BEFORE this deriver was written):
  1. Generic swaps: refvlm143->refvlm149, clonevlm143->clonevlm149,
     refar143->refar149, clonear143->clonear149 (the FOUR EXPLICIT
     session-token swaps — the tokens carry '143' without the 'v' prefix,
     so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm143->/tmp/vlm149, v143->v149
  2. History corrections (the era marker last-re-shot v137 -> v143 + the
     oldest-remaining list [v137 < v138] -> [v143 < v144], the re-run
     ordinal THIRTEENTH -> FOURTEENTH + the re-run bracket extended
     [-> v125 -> v131 -> v137 -> v149] -> [-> v125 -> v131 -> v137 -> v143
     -> v149], the agreement ordinal SIXTY-SIXTH -> SEVENTY-SECOND, the
     re-proves-after windows v101-v137 -> v101-v143 [the shots + clone
     headers' clause], the arbit census provenance "a drift re-check
     since v137" -> "since v143" + "The v137 verdict was IDENTICAL" ->
     "The v143 verdict was IDENTICAL" [the v143 cycle's measured verdict:
     IDENTICAL x2, the cleanest pair form], the compare banner's
     THIRTEENTH/v137-era pair -> FOURTEENTH/v143-era pair).
     NOTE: the v143 lineage carries NO plan pointer and NO later-pairs list
     (verified by the pre-derivation sweep — all era tokens confined to the
     file headers; the two known body lines are the compare banner [line
     38, corrected below] and the arbit done-echo [line 258, carried by the
     generic swap]).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files:
57/42/45/258).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v143.sh": "scripts/parity-probes/vlm-shots-v149.sh",
    "scripts/parity-probes/clone-vlmshots-v143.sh": "scripts/parity-probes/clone-vlmshots-v149.sh",
    "scripts/parity-probes/vlm-compare-v143.mjs": "scripts/parity-probes/vlm-compare-v149.mjs",
    "scripts/parity-probes/arbit-v143.sh": "scripts/parity-probes/arbit-v149.sh",
}

GENERIC = [
    ("refvlm143", "refvlm149"),
    ("clonevlm143", "clonevlm149"),
    ("refar143", "refar149"),
    ("clonear143", "clonear149"),
    ("/tmp/vlm143", "/tmp/vlm149"),
    ("v143", "v149"),
]


def main():
    ok = True
    for src, dst in FILES.items():
        text = open(src, encoding="utf-8").read()
        for old, new in GENERIC:
            text = text.replace(old, new)
        open(dst, "w", encoding="utf-8").write(text)
        print(f"derived {dst} (generic swaps applied)")

    print("\n--- history corrections (against the POST-swap state) ---")
    corr_map = {
        "scripts/parity-probes/vlm-shots-v149.sh": [
            ("# v137-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v137 — now\n# the oldest remaining [v137 < v138]; the pair's THIRTEENTH\n# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v149] — the SIXTY-SIXTH consecutive",
             "# v143-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v143 — now\n# the oldest remaining [v143 < v144]; the pair's FOURTEENTH\n# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v149] — the SEVENTY-SECOND consecutive"),
            ("# unpaired before v61]. The v149 re-run re-proves the v61-era surfaces after\n# v101-v137 (the mobile twins, the height pins, the stat-card divider pin).",
             "# unpaired before v61]. The v149 re-run re-proves the v61-era surfaces after\n# v101-v143 (the mobile twins, the height pins, the stat-card divider pin)."),
        ],
        "scripts/parity-probes/clone-vlmshots-v149.sh": [
            ("# v137-era pair (the re-run cadence's rotation — the pair's THIRTEENTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v149]): the DASHBOARD at desktop 1280x800",
             "# v143-era pair (the re-run cadence's rotation — the pair's FOURTEENTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v149]): the DASHBOARD at desktop 1280x800"),
            ("# v61-era surfaces, re-proved again by the v149 re-run after v101-v137). Runs",
             "# v61-era surfaces, re-proved again by the v149 re-run after v101-v143). Runs"),
        ],
        "scripts/parity-probes/vlm-compare-v149.mjs": [
            ("// vlm-compare-v149.mjs — the standing VLM pairwise RE-RUN (v149, the v137-era pair THIRTEENTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v149] — the SIXTY-SIXTH consecutive queue/ledger",
             "// vlm-compare-v149.mjs — the standing VLM pairwise RE-RUN (v149, the v143-era pair FOURTEENTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v149] — the SEVENTY-SECOND consecutive queue/ledger"),
            ('  console.log("===== PAIR: dashboard below-the-fold (Budget Guidelines + Quick Actions) desktop 1280x800 (ref vs clone — the v149 THIRTEENTH re-run of the v137-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v149]) =====");',
             '  console.log("===== PAIR: dashboard below-the-fold (Budget Guidelines + Quick Actions) desktop 1280x800 (ref vs clone — the v149 FOURTEENTH re-run of the v143-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v149]) =====");'),
        ],
        "scripts/parity-probes/arbit-v149.sh": [
            ("# 1280x800 (the v137-era pair's THIRTEENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v149]\n# — the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET\n# GUIDELINES card + the QUICK-ACTION row, last re-shot v137). The v137",
             "# 1280x800 (the v143-era pair's FOURTEENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v149]\n# — the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET\n# GUIDELINES card + the QUICK-ACTION row, last re-shot v143). The v143"),
            ("# censuses are the v61/v83 qa-census axes re-measured (a drift re-check\n# since v137):",
             "# censuses are the v61/v83 qa-census axes re-measured (a drift re-check\n# since v143):"),
        ],
    }
    for path, pairs in corr_map.items():
        text = open(path, encoding="utf-8").read()
        for old, new in pairs:
            if old not in text:
                print(f"MISS in {path}: {old[:70]!r}")
                ok = False
                continue
            text = text.replace(old, new)
            print(f"applied in {path}: {old[:52]!r} -> corrected")
        open(path, "w", encoding="utf-8").write(text)

    # residual old-token check across all four files
    # LEGIT contexts that must survive: the corrected re-run bracket
    # (→ v125 → v131 → v137 → v143 → v149) — the re-run chain's middle
    # entries are provenance, not stale era tokens; the corrected era
    # marker (the v143-era / last re-shot v143 / [v143 < v144]); the
    # axis-provenance citations (the v44/v45/v46/v51/v61/v75/v83 pin
    # families cited in the headers).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v137-era|re-shot v137|v137 < v138|THIRTEENTH re-run|SIXTY-SIXTH|"
            r"after v101-v137|The v137 verdict|since v137|"
            r"refvlm143|clonevlm143|refar143|clonear143|"
            r"/tmp/vlm143",
            text,
        ):
            bad.append(m.group(0))
        if bad:
            ok = False
            print(f"RESIDUAL in {dst}: {sorted(set(bad))}")
        else:
            print(f"residual scan clean: {dst}")

    # line-count preservation (the documented contract: 57/42/45/258)
    print("\n--- line-count preservation ---")
    expected = {
        "scripts/parity-probes/vlm-shots-v149.sh": 57,
        "scripts/parity-probes/clone-vlmshots-v149.sh": 42,
        "scripts/parity-probes/vlm-compare-v149.mjs": 45,
        "scripts/parity-probes/arbit-v149.sh": 258,
    }
    for dst, want in expected.items():
        got = len(open(dst, encoding="utf-8").read().splitlines())
        status = "OK" if got == want else f"FAIL (want {want})"
        if got != want:
            ok = False
        print(f"{dst}: {got} lines — {status}")

    if not ok:
        sys.exit(1)
    print("\nv149 series derived clean (all four files, zero residual, line counts preserved)")


if __name__ == "__main__":
    main()
