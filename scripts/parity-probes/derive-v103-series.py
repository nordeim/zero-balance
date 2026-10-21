#!/usr/bin/env python3
"""Derive the v103 probe series from the v97 lineage (the ITEMS pair —
INCOME + EXPENSES at desktop 1280x800, SEVENTH re-run
[v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97 -> v103]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm97->refvlm103, clonevlm97->clonevlm103,
     refarbit97->refarbit103, clonearbit97->clonearbit103,
     /tmp/vlm97->/tmp/vlm103, v97->v103
  2. History corrections (last-re-shot version v91 -> v97, re-run bracket
     + ordinal SIXTH->SEVENTH, the other-pairs list bumped to the
     current era [savings v98, login+calculator v99, networth+drill-down
     v100, dashboard v101, mobile twins v102]).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (each correction replaces the same
number of lines) so build-twohalf-v103.py inherits the v97 line boundaries.
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v97.sh": "scripts/parity-probes/vlm-shots-v103.sh",
    "scripts/parity-probes/clone-vlmshots-v97.sh": "scripts/parity-probes/clone-vlmshots-v103.sh",
    "scripts/parity-probes/vlm-compare-v97.mjs": "scripts/parity-probes/vlm-compare-v103.mjs",
    "scripts/parity-probes/arbit-v97.sh": "scripts/parity-probes/arbit-v103.sh",
}

GENERIC = [
    ("refvlm97", "refvlm103"),
    ("clonevlm97", "clonevlm103"),
    ("refarbit97", "refarbit103"),
    ("clonearbit97", "clonearbit103"),
    ("/tmp/vlm97", "/tmp/vlm103"),
    ("v97", "v103"),
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
        "scripts/parity-probes/vlm-shots-v103.sh": [
            ("last re-shot v91 — the SIXTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v103]; every other pair re-ran later [savings v92, login+calculator\n# v93, networth+drill-down v94, dashboard v95, mobile twins v96]).",
             "last re-shot v97 — the SEVENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103]; every other pair re-ran later [savings v98, login+calculator\n# v99, networth+drill-down v100, dashboard v101, mobile twins v102])."),
        ],
        "scripts/parity-probes/clone-vlmshots-v103.sh": [
            ("last re-shot v91 — the SIXTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v103]).",
             "last re-shot v97 — the SEVENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103])."),
        ],
        "scripts/parity-probes/vlm-compare-v103.mjs": [
            ("last re-shot v91 —\n// the SIXTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v103]; every\n// other pair re-ran later).",
             "last re-shot v97 —\n// the SEVENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103]; every\n// other pair re-ran later)."),
        ],
        "scripts/parity-probes/arbit-v103.sh": [
            ("desktop 1280x800 on BOTH items views — the SIXTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v103]:",
             "desktop 1280x800 on BOTH items views — the SEVENTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103]:"),
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
    # LEGIT contexts that must survive: the corrected re-run bracket
    # (→ v85 → v91 → v97 → v103), the new-era token (re-shot v97), the
    # lineage/axes provenance (v57-era, v70 census, v70b, v75 convention,
    # v79 census axes, v64/v70 axes, v65 axes), and the standing lesson
    # references (v22, v43, v46, v56).
    LEGIT = ("→ v91 → v97 → v103", "re-shot v97", "v57-era", "v57 →",
             "v64 →", "v70 →", "v79 →", "v85 →", "v70 census", "v70b",
             "v75 convention", "v79 census", "v65 axes", "v64/v70",
             "v43 rule", "v46 ", "v56 lesson", "v22", "v68")
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(r"v91(?![0-9])|refvlm97|clonevlm97|refarbit97|clonearbit97|/tmp/vlm97|SIXTH re-run|re-shot v91|savings v92|mobile twins v96|dashboard v95|drill-down v94", text):
            ctx = text[max(0, m.start() - 40):m.end() + 40]
            if any(l in ctx for l in LEGIT):
                continue  # legitimate provenance/bracket token
            bad.append(m.group(0))
        if bad:
            print(f"RESIDUAL OLD TOKENS in {dst}: {set(bad)}")
            ok = False
        else:
            print(f"residual check {dst}: clean")

    # line-count-preservation check (the two-half builder inherits boundaries)
    for src, dst in FILES.items():
        sn = open(src, encoding="utf-8").read().count("\n")
        dn = open(dst, encoding="utf-8").read().count("\n")
        status = "OK" if sn == dn else "LINE-COUNT DRIFT"
        print(f"line-count {dst}: {dn+1} lines (source {sn+1}) — {status}")
        if sn != dn:
            ok = False

    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
