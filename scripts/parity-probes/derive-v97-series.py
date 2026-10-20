#!/usr/bin/env python3
"""Derive the v97 probe series from the v91 lineage (the ITEMS pair —
INCOME + EXPENSES at desktop 1280x800, SIXTH re-run
[v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: v91->v97, refvlm91->refvlm97, clonevlm91->clonevlm97,
     refarbit91->refarbit97, clonearbit91->clonearbit97, /tmp/vlm91->/tmp/vlm97
  2. History corrections (last-re-shot version, re-run bracket + ordinal
     FIFTH->SIXTH, the every-other-pair list).

Every replacement is checked; a miss is reported and fails the run.
"""
import sys

FILES = {
    "scripts/parity-probes/vlm-shots-v91.sh": "scripts/parity-probes/vlm-shots-v97.sh",
    "scripts/parity-probes/clone-vlmshots-v91.sh": "scripts/parity-probes/clone-vlmshots-v97.sh",
    "scripts/parity-probes/vlm-compare-v91.mjs": "scripts/parity-probes/vlm-compare-v97.mjs",
    "scripts/parity-probes/arbit-v91.sh": "scripts/parity-probes/arbit-v97.sh",
}

GENERIC = [
    ("refvlm91", "refvlm97"),
    ("clonevlm91", "clonevlm97"),
    ("refarbit91", "refarbit97"),
    ("clonearbit91", "clonearbit97"),
    ("/tmp/vlm91", "/tmp/vlm97"),
    ("v91", "v97"),
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
    # corrections are applied file-by-file after the fact
    corr_map = {
        "scripts/parity-probes/vlm-shots-v97.sh": [
            ("last re-shot v85 \u2014 the FIFTH re-run of the pair [v57 \u2192 v64 \u2192 v70 \u2192 v79 \u2192 v85\n# \u2192 v97]; every other pair re-ran later [savings v80, login+calculator\n# v81, networth+drill-down v82, dashboard v83, mobile twins v84])",
             "last re-shot v91 \u2014 the SIXTH re-run of the pair [v57 \u2192 v64 \u2192 v70 \u2192 v79 \u2192 v85\n# \u2192 v91 \u2192 v97]; every other pair re-ran later [savings v92, login+calculator\n# v93, networth+drill-down v94, dashboard v95, mobile twins v96])"),
        ],
        "scripts/parity-probes/clone-vlmshots-v97.sh": [
            ("last re-shot v85 \u2014 the FIFTH re-run of the pair [v57 \u2192 v64 \u2192 v70 \u2192 v79 \u2192 v85\n# \u2192 v97])",
             "last re-shot v91 \u2014 the SIXTH re-run of the pair [v57 \u2192 v64 \u2192 v70 \u2192 v79 \u2192 v85\n# \u2192 v91 \u2192 v97])"),
        ],
        "scripts/parity-probes/vlm-compare-v97.mjs": [
            ("the v57-era items pair, last re-shot v85 \u2014\n// the FIFTH re-run of the pair [v57 \u2192 v64 \u2192 v70 \u2192 v79 \u2192 v85 \u2192 v97]; every\n// other pair re-ran later)",
             "the v57-era items pair, last re-shot v91 \u2014\n// the SIXTH re-run of the pair [v57 \u2192 v64 \u2192 v70 \u2192 v79 \u2192 v85 \u2192 v91 \u2192 v97]; every\n// other pair re-ran later)"),
        ],
        "scripts/parity-probes/arbit-v97.sh": [
            ("The v79 census axes\n# (themselves the v70 census re-measured), re-measured on BOTH sides at\n# desktop 1280x800 on BOTH items views \u2014 the FIFTH re-run of the pair\n# [v57 \u2192 v64 \u2192 v70 \u2192 v79 \u2192 v85 \u2192 v97]:",
             "The v79 census axes\n# (themselves the v70 census re-measured), re-measured on BOTH sides at\n# desktop 1280x800 on BOTH items views \u2014 the SIXTH re-run of the pair\n# [v57 \u2192 v64 \u2192 v70 \u2192 v79 \u2192 v85 \u2192 v91 \u2192 v97]:"),
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
    LEGIT = ("last re-shot v91", "v85 \u2192 v91 \u2192 v97", "\u2192 v91 \u2192 v97")
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(r"v91(?![0-9])|refvlm91|clonevlm91|refarbit91|clonearbit91|/tmp/vlm91|FIFTH re-run|re-shot v85|savings v80|mobile twins v84", text):
            ctx = text[max(0, m.start()-30):m.end()+30]
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
