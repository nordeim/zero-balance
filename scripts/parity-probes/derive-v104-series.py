#!/usr/bin/env python3
"""Derive the v104 probe series from the v98 lineage (the SAVINGS pair —
SAVINGS view at desktop 1280x800, SEVENTH re-run
[v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> v104]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm98->refvlm104, clonevlm98->clonevlm104,
     refarbit98->refarbit104, clonearbit98->clonearbit104,
     /tmp/vlm98->/tmp/vlm104, v98->v104
  2. History corrections (last-re-shot version v92 -> v98, era marker
     v92-era -> v98-era, re-run bracket + ordinal SIXTH->SEVENTH, the
     oldest-remaining list bumped to the current era [v98 < v99 < v100 <
     v101 < v102 < v103], the plan attribution v97 -> v103, the agreement
     count TWENTY-FIRST -> TWENTY-SEVENTH, and the v98-era pin-candidate
     provenance note kept historical).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (each correction replaces the same
number of lines) so build-twohalf-v104.py inherits the v98 line boundaries.
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v98.sh": "scripts/parity-probes/vlm-shots-v104.sh",
    "scripts/parity-probes/clone-vlmshots-v98.sh": "scripts/parity-probes/clone-vlmshots-v104.sh",
    "scripts/parity-probes/vlm-compare-v98.mjs": "scripts/parity-probes/vlm-compare-v104.mjs",
    "scripts/parity-probes/arbit-v98.sh": "scripts/parity-probes/arbit-v104.sh",
}

GENERIC = [
    ("refvlm98", "refvlm104"),
    ("clonevlm98", "clonevlm104"),
    ("refarbit98", "refarbit104"),
    ("clonearbit98", "clonearbit104"),
    ("/tmp/vlm98", "/tmp/vlm104"),
    ("v98", "v104"),
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
        "scripts/parity-probes/vlm-shots-v104.sh": [
            ("the v92-era savings pair, last re-shot\n# v92, now the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97]; the\n# v97 plan's v104 queue suggestion, agreeing with the rotation ledger —\n# the TWENTY-FIRST consecutive agreement)",
             "the v98-era savings pair, last re-shot\n# v98, now the oldest remaining [v98 < v99 < v100 < v101 < v102 < v103]; the\n# v103 plan's v104 queue suggestion, agreeing with the rotation ledger —\n# the TWENTY-SEVENTH consecutive agreement)"),
        ],
        "scripts/parity-probes/clone-vlmshots-v104.sh": [
            ("the v92-era savings pair, last re-shot\n# v92, now the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97]; the\n# pair's SIXTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v104]). Runs inside",
             "the v98-era savings pair, last re-shot\n# v98, now the oldest remaining [v98 < v99 < v100 < v101 < v102 < v103]; the\n# pair's SEVENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104]). Runs inside"),
        ],
        "scripts/parity-probes/vlm-compare-v104.mjs": [
            ("the v92-era savings pair's SIXTH re-run — last re-shot\n// v92, now the oldest remaining [v92 < v93 < v94 < v95 < v96 < v97] — agreeing with the rotation ledger, the TWENTY-FIRST consecutive agreement).",
             "the v98-era savings pair's SEVENTH re-run — last re-shot\n// v98, now the oldest remaining [v98 < v99 < v100 < v101 < v102 < v103] — agreeing with the rotation ledger, the TWENTY-SEVENTH consecutive agreement)."),
        ],
        "scripts/parity-probes/arbit-v104.sh": [
            ("the v92-era savings pair's SIXTH re-run, last re-shot v92 — now the\n# oldest remaining candidate [v92 < v93 < v94 < v95 < v96 < v97]).",
             "the v98-era savings pair's SEVENTH re-run, last re-shot v98 — now the\n# oldest remaining candidate [v98 < v99 < v100 < v101 < v102 < v103])."),
            ("v104 pin candidate: the 1280 state of the v51/v54 390-only family",
             "v98-era pin candidate: the 1280 state of the v51/v54 390-only family"),
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
    # (→ v92 → v98 → v104), the corrected state tokens (re-shot v98,
    # v98-era), the lineage/axes provenance (v58 axes/footer, v57
    # conditional-footer, v74/v80 axes, v64 rule, v73 heredoc lesson,
    # v51/v54 family), the standing lesson references (v22, v43, v46),
    # and the seedcheck filename (db-seedcheck-v68.cjs).
    LEGIT = ("→ v92 → v98 → v104", "re-shot v98", "v98-era",
             "v58 DATA-CONDITIONAL", "v58 axes", "v57 conditional-footer",
             "v74/v80 axes", "v64 rule", "v73 heredoc",
             "v51/v54 390-only family", "v43 rule", "v46 ", "v46 incident",
             "v22", "seedcheck-v68")
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(r"v92-era|re-shot v92|SIXTH re-run|TWENTY-FIRST|v92 < v93|v93 < v94 < v95 < v96 < v97|v97 plan's|refvlm98|clonevlm98|refarbit98|clonearbit98|/tmp/vlm98", text):
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
