#!/usr/bin/env python3
"""Derive the v96 probe series from the v90 lineage (the mobile 390 twins,
FIFTH re-run [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: v90->v96, refvlm90->refvlm96, clonevlm90->clonevlm96,
     refarbit90->refarbit96, clonearbit90->clonearbit96, /tmp/vlm90->/tmp/vlm96
  2. History corrections (queue source, oldest-remaining list, re-run
     bracket, ordinal FOURTH->FIFTH, census-axes provenance, verdict note).

Every replacement is checked; a miss is reported and fails the run.
"""
import sys

FILES = {
    "scripts/parity-probes/vlm-shots-v90.sh": "scripts/parity-probes/vlm-shots-v96.sh",
    "scripts/parity-probes/clone-vlmshots-v90.sh": "scripts/parity-probes/clone-vlmshots-v96.sh",
    "scripts/parity-probes/vlm-compare-v90.mjs": "scripts/parity-probes/vlm-compare-v96.mjs",
    "scripts/parity-probes/arbit-v90.sh": "scripts/parity-probes/arbit-v96.sh",
}

GENERIC = [
    ("refvlm90", "refvlm96"),
    ("clonevlm90", "clonevlm96"),
    ("refarbit90", "refarbit96"),
    ("clonearbit90", "clonearbit96"),
    ("/tmp/vlm90", "/tmp/vlm96"),
    ("v90", "v96"),
]

# History corrections are defined per-file in corr_map inside main()
# (applied AFTER the generic swaps, each verified applied).

def main():
    ok = True
    for src, dst in FILES.items():
        text = open(src, encoding="utf-8").read()
        for old, new in GENERIC:
            text = text.replace(old, new)
        open(dst, "w", encoding="utf-8").write(text)
        print(f"derived {dst} (generic swaps applied)")
    print("\n--- history corrections ---")
    # corrections are applied file-by-file after the fact
    corr_map = {
        "scripts/parity-probes/vlm-shots-v96.sh": [
            ("The v96 queue (the v89 plan's own suggestion",
             "The v96 queue (the v95 plan's own suggestion"),
            ("the twins last re-shot v84 = the oldest remaining\n# [v84 < v85 < v86 < v87 < v88 < v89]; the pair's FOURTH re-run\n# [v62/v63 \u2192 v69 \u2192 v78 \u2192 v84 \u2192 v96]",
             "the twins last re-shot v90 = the oldest remaining\n# [v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH re-run\n# [v62/v63 \u2192 v69 \u2192 v78 \u2192 v84 \u2192 v90 \u2192 v96]"),
        ],
        "scripts/parity-probes/clone-vlmshots-v96.sh": [],
        "scripts/parity-probes/vlm-compare-v96.mjs": [
            ("twins last re-shot v84 = the oldest remaining candidate [v84 < v85 <\n// v86 < v87 < v88 < v89]; the pair's FOURTH re-run [v62/v63 \u2192 v69 \u2192\n// v78 \u2192 v84 \u2192 v96]",
             "twins last re-shot v90 = the oldest remaining candidate [v90 < v91 <\n// v92 < v93 < v94 < v95]; the pair's FIFTH re-run [v62/v63 \u2192 v69 \u2192\n// v78 \u2192 v84 \u2192 v90 \u2192 v96]"),
            ("the v84 re-run's own verdicts were DIFFERENT",
             "the v84/v90 re-runs' own verdicts were DIFFERENT"),
        ],
        "scripts/parity-probes/arbit-v96.sh": [
            ("The v84 census axes,\n# re-measured on BOTH sides at mobile 390 (the pair's FOURTH re-run\n# [v62/v63 \u2192 v69 \u2192 v78 \u2192 v84 \u2192 v96]):",
             "The v90 census axes,\n# re-measured on BOTH sides at mobile 390 (the pair's FIFTH re-run\n# [v62/v63 \u2192 v69 \u2192 v78 \u2192 v84 \u2192 v90 \u2192 v96]):"),
            ("re-confirmed live by the v84 re-run",
             "re-confirmed live by the v84/v90 re-runs"),
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
    import re
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        residual = re.findall(r"v90(?![0-9])|refvlm90|clonevlm90|refarbit90|clonearbit90|/tmp/vlm90|FOURTH re-run|v89 plan|v84 < v85", text)
        # v90 legitimately remains inside the FIFTH re-run bracket + provenance
        allowed = text.count("v84 \u2192 v90 \u2192 v96") + text.count("v84/v90 re-run")
        bad = [r for r in residual if r in ("FOURTH re-run", "v89 plan", "v84 < v85", "refvlm90", "clonevlm90", "refarbit90", "clonearbit90", "/tmp/vlm90")]
        if bad:
            print(f"RESIDUAL OLD TOKENS in {dst}: {set(bad)}")
            ok = False
        else:
            print(f"residual check {dst}: clean")

    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
