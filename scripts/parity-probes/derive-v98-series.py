#!/usr/bin/env python3
"""Derive the v98 probe series from the v92 lineage (the SAVINGS pair —
the savings view at desktop 1280x800, SIXTH re-run
[v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: v92->v98, refvlm92->refvlm98, clonevlm92->clonevlm98,
     refarbit92->refarbit98, clonearbit92->clonearbit98, /tmp/vlm92->/tmp/vlm98
  2. History corrections (last-re-shot version v86 -> v92, re-run bracket +
     ordinal FIFTH->SIXTH, the oldest-remaining bracket, the agreement
     ordinal FIFTEENTH->TWENTY-FIRST, the suggesting plan v91 -> v97).

Every replacement is checked; a miss is reported and fails the run.
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v92.sh": "scripts/parity-probes/vlm-shots-v98.sh",
    "scripts/parity-probes/clone-vlmshots-v92.sh": "scripts/parity-probes/clone-vlmshots-v98.sh",
    "scripts/parity-probes/vlm-compare-v92.mjs": "scripts/parity-probes/vlm-compare-v98.mjs",
    "scripts/parity-probes/arbit-v92.sh": "scripts/parity-probes/arbit-v98.sh",
}

GENERIC = [
    ("refvlm92", "refvlm98"),
    ("clonevlm92", "clonevlm98"),
    ("refarbit92", "refarbit98"),
    ("clonearbit92", "clonearbit98"),
    ("/tmp/vlm92", "/tmp/vlm98"),
    ("v92", "v98"),
]

def main():
    ok = True
    for src, dst in FILES.items():
        text = open(src, encoding="utf-8").read()
        for old, new in GENERIC:
            text = text.replace(old, new)
        open(dst, "w", encoding="utf-8").write(text)
        print(f"derived {dst} (generic swaps applied)")
    print("\n--- history corrections ---")
    # corrections are applied file-by-file after the fact (fragments appear
    # in their POST-SWAP form)
    corr_map = {
        "scripts/parity-probes/vlm-shots-v98.sh": [
            ("the v86-era savings pair, last re-shot\n# v86, now the oldest remaining [v86 < v87 < v88 < v89 < v90 < v91]; the\n# v91 plan's v98 queue suggestion, agreeing with the rotation ledger \u2014\n# the FIFTEENTH consecutive agreement)",
             "the v92-era savings pair, last re-shot\n# v92, now the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97]; the\n# v97 plan's v98 queue suggestion, agreeing with the rotation ledger \u2014\n# the TWENTY-FIRST consecutive agreement)"),
        ],
        "scripts/parity-probes/clone-vlmshots-v98.sh": [
            ("the v86-era savings pair, last re-shot\n# v86, now the oldest remaining [v86 < v87 < v88 < v89 < v90 < v91]; the\n# pair's FIFTH re-run [v58 \u2192 v65 \u2192 v74 \u2192 v80 \u2192 v86 \u2192 v98])",
             "the v92-era savings pair, last re-shot\n# v92, now the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97]; the\n# pair's SIXTH re-run [v58 \u2192 v65 \u2192 v74 \u2192 v80 \u2192 v86 \u2192 v92 \u2192 v98])"),
        ],
        "scripts/parity-probes/vlm-compare-v98.mjs": [
            ("the v86-era savings pair's FIFTH re-run \u2014 last re-shot\n// v86, now the oldest remaining [v86 < v87 < v88 < v89 < v90 < v91] \u2014 agreeing with the rotation ledger, the FIFTEENTH consecutive agreement)",
             "the v92-era savings pair's SIXTH re-run \u2014 last re-shot\n// v92, now the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97] \u2014 agreeing with the rotation ledger, the TWENTY-FIRST consecutive agreement)"),
        ],
        "scripts/parity-probes/arbit-v98.sh": [
            ("(the savings view full-page \u2014\n# the v86-era savings pair's FIFTH re-run, last re-shot v86 \u2014 now the\n# oldest remaining candidate [v86 < v87 < v88 < v89 < v90 < v91])",
             "(the savings view full-page \u2014\n# the v92-era savings pair's SIXTH re-run, last re-shot v92 \u2014 now the\n# oldest remaining candidate [v92 < v93 < v94 < v95 < v96 < v97])"),
        ],
    }
    for path, pairs in corr_map.items():
        text = open(path, encoding="utf-8").read()
        for old, new in pairs:
            if old not in text:
                print(f"MISS in {path}: {old[:60]!r}")
                ok = False
                continue
            text = text.replace(old, new)
            print(f"applied in {path}: {old[:48]!r} -> corrected")
        open(path, "w", encoding="utf-8").write(text)

    # residual old-token check across all four files
    LEGIT = ("v92-era savings pair", "last re-shot v92", "v92 < v93",
             "\u2192 v92 \u2192 v98")
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(r"v86(?![0-9])|v87(?![0-9])|v88(?![0-9])|v89(?![0-9])|v90(?![0-9])|v91(?![0-9])|FIFTH re-run|FIFTEENTH|re-shot v86|v91 plan's|refvlm92|clonevlm92|refarbit92|clonearbit92|/tmp/vlm92", text):
            ctx = text[max(0, m.start()-40):m.end()+40]
            if any(l in ctx for l in LEGIT):
                continue  # legitimate provenance/bracket token
            bad.append(m.group(0))
        if bad:
            print(f"RESIDUAL OLD TOKENS in {dst}: {set(bad)}")
            ok = False
        else:
            print(f"residual check {dst}: clean")

    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
