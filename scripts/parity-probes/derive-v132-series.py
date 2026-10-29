#!/usr/bin/env python3
"""Derive the v132 probe series from the v126 lineage (the MOBILE 390x844
full-page TWINS — the /NETWORTH view [the v63-era pair's surface] + the
DASHBOARD [the v62-era mobile twin's surface], ELEVENTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 ->
v120 -> v126 -> v132]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v131-era docs' v132 queue names "the pair's ELEVENTH re-run
bracket [v62/v63 -> ... -> v120 -> v126 -> v132]... derived from
vlm-shots-v126.sh's own TENTH/11-entry header" — verified against the v126
header BEFORE this derivation: vlm-shots-v126.sh's own header reads "the
pair's TENTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 →
v114 → v120 → v126]" — an 11-ENTRY bracket with the TENTH ordinal (v62/v63
the original pair, one entry — the entries-minus-one convention,
consistent, no off-by-one this lineage). v132 = the ELEVENTH re-run by
appending v132 to the v126 header's TENTH bracket. The FIFTY-FIFTH
consecutive queue/ledger agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm126->refvlm132, clonevlm126->clonevlm132,
     refarbit126->refarbit132, clonearbit126->clonearbit132,
     /tmp/vlm126->/tmp/vlm132, v126->v132
  2. History corrections (plan pointer "the v125 plan's"->"the v131 plan's",
     era marker last-re-shot v120 -> v126, the oldest-remaining list bumped
     to the current era [v126 < v127 < v128 < v129 < v130 < v131], re-run
     ordinal TENTH->ELEVENTH, the re-run bracket extended
     [v62/v63 -> ... -> v120 -> v126 -> v132], the verdicts window
     "the v84/v90/v96/v102/v108/v120 re-runs"->"...v108/v126 re-runs"
     [the v126 verdict was BOTH PAIRS DIFFERENT — the pair's documented
     verdict class, verified from the v126 plan's F3 record], the arbit's
     "re-confirmed live by the v84/v90/v96/v102/v108/v120 re-runs"->"...
     v108/v126 re-runs" + the census-axes era "The v120 census axes"->
     "The v126 census axes").

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v126.sh": "scripts/parity-probes/vlm-shots-v132.sh",
    "scripts/parity-probes/clone-vlmshots-v126.sh": "scripts/parity-probes/clone-vlmshots-v132.sh",
    "scripts/parity-probes/vlm-compare-v126.mjs": "scripts/parity-probes/vlm-compare-v132.mjs",
    "scripts/parity-probes/arbit-v126.sh": "scripts/parity-probes/arbit-v132.sh",
}

GENERIC = [
    ("refvlm126", "refvlm132"),
    ("clonevlm126", "clonevlm132"),
    ("refarbit126", "refarbit132"),
    ("clonearbit126", "clonearbit132"),
    ("/tmp/vlm126", "/tmp/vlm132"),
    ("v126", "v132"),
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
        "scripts/parity-probes/vlm-shots-v132.sh": [
            ("# The v132 queue (the v125 plan's own suggestion, now confirmed by the\n# rotation ledger: the twins last re-shot v120 = the oldest remaining\n# [v120 < v121 < v122 < v123 < v124 < v125]; the pair's TENTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v132]). READ-ONLY: login + passive",
             "# The v132 queue (the v131 plan's own suggestion, now confirmed by the\n# rotation ledger: the twins last re-shot v126 = the oldest remaining\n# [v126 < v127 < v128 < v129 < v130 < v131]; the pair's ELEVENTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132]). READ-ONLY: login + passive"),
        ],
        "scripts/parity-probes/vlm-compare-v132.mjs": [
            ("// twins last re-shot v120 = the oldest remaining candidate [v120 < v121 <\n// v122 < v123 < v124 < v125]; the pair's TENTH re-run [v62/v63 → v69 →\n// v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v132]) and (2) the DASHBOARD (the v62-era mobile twin's",
             "// twins last re-shot v126 = the oldest remaining candidate [v126 < v127 <\n// v128 < v129 < v130 < v131]; the pair's ELEVENTH re-run [v62/v63 → v69 →\n// v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132]) and (2) the DASHBOARD (the v62-era mobile twin's"),
            ("the v84/v90/v96/v102/v108/v120 re-runs' own verdicts were DIFFERENT",
             "the v84/v90/v96/v102/v108/v126 re-runs' own verdicts were DIFFERENT"),
        ],
        "scripts/parity-probes/arbit-v132.sh": [
            ("# the drift state and measures the pin's axes). The v120 census axes,\n# re-measured on BOTH sides at mobile 390 (the pair's TENTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v132]):",
             "# the drift state and measures the pin's axes). The v126 census axes,\n# re-measured on BOTH sides at mobile 390 (the pair's ELEVENTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132]):"),
            ("#   NETWORTH (the v63-era classes, re-confirmed live by the v84/v90/v96/v102/v108/v120 re-runs):",
             "#   NETWORTH (the v63-era classes, re-confirmed live by the v84/v90/v96/v102/v108/v126 re-runs):"),
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
    # (→ v114 → v120 → v126 → v132) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the pin/provenance references
    # (the v41 mobile-superset census, the v43 rule, the v45/v44 pin
    # families, the v46 incident rule, the v51 F4 guidelines census, the
    # v53 tablist-390 pin, the v62/v63-era surfaces, the v62
    # header-subtitle pin, the v63 stat-tile pin, the v75 convention);
    # the clone file needs NO corrections (verified: zero era tokens).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v120|v120 < v121|TENTH re-run|the v125 plan's|"
            r"v102/v108/v120 re-runs|The v120 census|"
            r"refvlm126|clonevlm126|refarbit126|clonearbit126|/tmp/vlm126",
            text,
        ):
            bad.append(m.group(0))
        # bare-v120 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v120", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v114 → v120 → v126 → v132" in ctx:
                continue
            if "v120" not in bad:
                bad.append("v120 (outside the corrected bracket)")
        if bad:
            print(f"RESIDUAL OLD TOKENS in {dst}: {sorted(set(bad))}")
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
