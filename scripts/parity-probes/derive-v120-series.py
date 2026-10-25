#!/usr/bin/env python3
"""Derive the v120 probe series from the v114 lineage (the MOBILE TWINS
pair — BOTH mobile 390x844 full-page twins: (1) the /NETWORTH view (the
v63-era pair's surface) and (2) the DASHBOARD (the v62-era mobile twin's
surface), NINTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120]).

NOTE the v114 header's own EIGHTH ordinal is CONSISTENT with its 9-entry
bracket [v62/v63 the original pair] — no off-by-one this lineage (unlike
the v113 lineage's SEVENTH-vs-bracket). v120 = the NINTH re-run by the
same convention (10 entries, v62/v63 the original).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm114->refvlm120, clonevlm114->clonevlm120,
     refarbit114->refarbit120, clonearbit114->clonearbit120,
     /tmp/vlm114->/tmp/vlm120, v114->v120
  2. History corrections (the plan pointer "the v113 plan's own suggestion"
     -> "the v119 plan's", last-re-shot v108 -> v114, the oldest-remaining
     list bumped to the current era [v114 < v115 < v116 < v117 < v118 <
     v119], the ordinal EIGHTH -> NINTH, the re-run bracket extended
     [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114
     -> v120], the re-runs verdict list extended
     v84/v90/v96/v102/v108 -> v84/v90/v96/v102/v108/v114 [the v114
     verdict was BOTH PAIRS DIFFERENT — the pair's documented verdict
     class], and the census-axes era "The v108 census axes" -> "The v114
     census axes").

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v114.sh": "scripts/parity-probes/vlm-shots-v120.sh",
    "scripts/parity-probes/clone-vlmshots-v114.sh": "scripts/parity-probes/clone-vlmshots-v120.sh",
    "scripts/parity-probes/vlm-compare-v114.mjs": "scripts/parity-probes/vlm-compare-v120.mjs",
    "scripts/parity-probes/arbit-v114.sh": "scripts/parity-probes/arbit-v120.sh",
}

GENERIC = [
    ("refvlm114", "refvlm120"),
    ("clonevlm114", "clonevlm120"),
    ("refarbit114", "refarbit120"),
    ("clonearbit114", "clonearbit120"),
    ("/tmp/vlm114", "/tmp/vlm120"),
    ("v114", "v120"),
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
        "scripts/parity-probes/vlm-shots-v120.sh": [
            ("# The v120 queue (the v113 plan's own suggestion, now confirmed by the\n# rotation ledger: the twins last re-shot v108 = the oldest remaining\n# [v108 < v109 < v110 < v111 < v112 < v113]; the pair's EIGHTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v120]). READ-ONLY: login + passive",
             "# The v120 queue (the v119 plan's own suggestion, now confirmed by the\n# rotation ledger: the twins last re-shot v114 = the oldest remaining\n# [v114 < v115 < v116 < v117 < v118 < v119]; the pair's NINTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120]). READ-ONLY: login + passive"),
        ],
        "scripts/parity-probes/vlm-compare-v120.mjs": [
            ("the\n// twins last re-shot v108 = the oldest remaining candidate [v108 < v109 <\n// v110 < v111 < v112 < v113]; the pair's EIGHTH re-run [v62/v63 → v69 →\n// v78 → v84 → v90 → v96 → v102 → v108 → v120]) and (2) the DASHBOARD",
             "the\n// twins last re-shot v114 = the oldest remaining candidate [v114 < v115 <\n// v116 < v117 < v118 < v119]; the pair's NINTH re-run [v62/v63 → v69 →\n// v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120]) and (2) the DASHBOARD"),
            ("the v84/v90/v96/v102/v108 re-runs' own verdicts were DIFFERENT",
             "the v84/v90/v96/v102/v108/v114 re-runs' own verdicts were DIFFERENT"),
        ],
        "scripts/parity-probes/arbit-v120.sh": [
            ("# the drift state and measures the pin's axes). The v108 census axes,\n# re-measured on BOTH sides at mobile 390 (the pair's EIGHTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v120]):",
             "# the drift state and measures the pin's axes). The v114 census axes,\n# re-measured on BOTH sides at mobile 390 (the pair's NINTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120]):"),
            ("#   NETWORTH (the v63-era classes, re-confirmed live by the v84/v90/v96/v102/v108 re-runs):",
             "#   NETWORTH (the v63-era classes, re-confirmed live by the v84/v90/v96/v102/v108/v114 re-runs):"),
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
    # (→ v108 → v114 → v120), the corrected re-runs list
    # (v102/v108/v114 re-runs), the pin/axes provenance (the v63 stat-tile
    # pin, the v53 tablist-390 pin, the v41 F3 mobile superset census, the
    # v62 header-subtitle pin, the v51 F4 mobile guidelines census, the
    # v45/v44 pin families, the v61 STRETCH fix, the v62 subtitle census),
    # the rule/lesson references (the v43 rule, the v46 incident rule, the
    # v75 convention, the v66 discipline), the seedcheck filename
    # (db-seedcheck-v68.cjs), the md5 provenance (remediation-plan-v102.md
    # in the builder lineage), and the v62/v63-era surface names.
    LEGIT = (
        "→ v108 → v114 → v120", "v102/v108/v114 re-runs",
        "v63 stat-tile", "v53 tablist", "v41 F3", "v41",
        "v62 header-subtitle", "v51 F4", "v45/v44", "v62/v63",
        "v43 rule", "v46 ", "v75", "v66 discipline", "seedcheck-v68",
        "v61 STRETCH", "v62 subtitle", "v62-era", "v63-era",
        "v62 mobile twin", "remediation-plan-v102",
    )
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"The v108 census|re-shot v108|EIGHTH re-run|v108 < v109|v111 < v112 < v113|the v113 plan|the v84/v90/v96/v102/v108 re-runs|refvlm114|clonevlm114|refarbit114|clonearbit114|/tmp/vlm114",
            text,
        ):
            ctx = text[max(0, m.start() - 45):m.end() + 45]
            if any(l in ctx for l in LEGIT):
                continue  # legitimate provenance/bracket token
            bad.append(m.group(0))
        if bad:
            print(f"RESIDUAL OLD TOKENS in {dst}: {set(bad)}")
            ok = False
        else:
            print(f"residual check {dst}: clean")

    # line-count report (the two-half builder inherits boundaries)
    for src, dst in FILES.items():
        sn = open(src, encoding="utf-8").read().count("\n")
        dn = open(dst, encoding="utf-8").read().count("\n")
        status = "OK" if sn == dn else f"DRIFT ({dn - sn:+d})"
        print(f"line-count {dst}: {dn + 1} lines (source {sn + 1}) — {status}")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
