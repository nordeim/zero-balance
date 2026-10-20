#!/usr/bin/env python3
"""Derive the v99 probe series from the v93 lineage (the LOGIN + CALCULATOR
pair — the login view + the calculator dialog at desktop 1280x800, SIXTH
re-run [v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm93->refvlm99, clonevlm93->clonevlm99,
     reflogin93->reflogin99, clonelogin93->clonelogin99,
     refcalc93arbit->refcalc99arbit, clonecalc93arbit->clonecalc99arbit,
     /tmp/vlm93->/tmp/vlm99, v93->v99
  2. History corrections (last-re-shot version v87 -> v93, re-run bracket +
     ordinal FIFTH->SIXTH, the oldest-remaining bracket, the agreement
     ordinal SIXTEENTH->TWENTY-SECOND, the suggesting plan v92 -> v98).

Every replacement is checked; a miss is reported and fails the run.
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v93.sh": "scripts/parity-probes/vlm-shots-v99.sh",
    "scripts/parity-probes/login-shots-v93.sh": "scripts/parity-probes/login-shots-v99.sh",
    "scripts/parity-probes/clone-vlmshots-v93.sh": "scripts/parity-probes/clone-vlmshots-v99.sh",
    "scripts/parity-probes/clone-login-shots-v93.sh": "scripts/parity-probes/clone-login-shots-v99.sh",
    "scripts/parity-probes/vlm-compare-v93.mjs": "scripts/parity-probes/vlm-compare-v99.mjs",
    "scripts/parity-probes/arbit-v93.sh": "scripts/parity-probes/arbit-v99.sh",
}

GENERIC = [
    ("refvlm93", "refvlm99"),
    ("clonevlm93", "clonevlm99"),
    ("reflogin93", "reflogin99"),
    ("clonelogin93", "clonelogin99"),
    ("refcalc93arbit", "refcalc99arbit"),
    ("clonecalc93arbit", "clonecalc99arbit"),
    ("/tmp/vlm93", "/tmp/vlm99"),
    ("v93", "v99"),
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
        "scripts/parity-probes/vlm-shots-v99.sh": [
            ("the v87-era LOGIN + CALCULATOR pair, last re-shot\n# v87, now the oldest remaining [v87 < v88 < v89 < v90 < v91 < v92]; the\n# v92 plan's v99 queue suggestion, agreeing with the rotation ledger \u2014 the\n# SIXTEENTH consecutive agreement; the pair's FIFTH re-run [v59 \u2192 v66 \u2192 v75 \u2192\n# v81 \u2192 v87 \u2192 v99])",
             "the v93-era LOGIN + CALCULATOR pair, last re-shot\n# v93, now the oldest remaining [v93 < v94 < v95 < v96 < v97 < v98]; the\n# v98 plan's v99 queue suggestion, agreeing with the rotation ledger \u2014 the\n# TWENTY-SECOND consecutive agreement; the pair's SIXTH re-run [v59 \u2192 v66 \u2192 v75 \u2192\n# v81 \u2192 v87 \u2192 v93 \u2192 v99])"),
        ],
        "scripts/parity-probes/login-shots-v99.sh": [
            ("cycle's v87-era LOGIN + CALCULATOR pair, last re-shot v87 \u2014 the pair's\n# FIFTH re-run [v59 \u2192 v66 \u2192 v75 \u2192 v81 \u2192 v87 \u2192 v99], the SIXTEENTH consecutive\n# queue/ledger agreement)",
             "cycle's v93-era LOGIN + CALCULATOR pair, last re-shot v93 \u2014 the pair's\n# SIXTH re-run [v59 \u2192 v66 \u2192 v75 \u2192 v81 \u2192 v87 \u2192 v93 \u2192 v99], the TWENTY-SECOND consecutive\n# queue/ledger agreement)"),
        ],
        "scripts/parity-probes/clone-vlmshots-v99.sh": [
            ("the re-run cycle's\n# v87-era LOGIN + CALCULATOR pair, last re-shot v87 \u2014 the pair's FIFTH\n# re-run [v59 \u2192 v66 \u2192 v75 \u2192 v81 \u2192 v87 \u2192 v99])",
             "the re-run cycle's\n# v93-era LOGIN + CALCULATOR pair, last re-shot v93 \u2014 the pair's SIXTH\n# re-run [v59 \u2192 v66 \u2192 v75 \u2192 v81 \u2192 v87 \u2192 v93 \u2192 v99])"),
        ],
        "scripts/parity-probes/clone-login-shots-v99.sh": [
            ("the re-run\n# cycle's v87-era LOGIN + CALCULATOR pair, last re-shot v87 \u2014 the pair's\n# FIFTH re-run [v59 \u2192 v66 \u2192 v75 \u2192 v81 \u2192 v87 \u2192 v99])",
             "the re-run\n# cycle's v93-era LOGIN + CALCULATOR pair, last re-shot v93 \u2014 the pair's\n# SIXTH re-run [v59 \u2192 v66 \u2192 v75 \u2192 v81 \u2192 v87 \u2192 v93 \u2192 v99])"),
        ],
        "scripts/parity-probes/vlm-compare-v99.mjs": [
            ("the v87-era LOGIN + CALCULATOR\n// pair last re-shot v87 [v87 < v88 < v89 < v90 < v91 < v92]; the pair's\n// FIFTH re-run [v59 \u2192 v66 \u2192 v75 \u2192 v81 \u2192 v87 \u2192 v99] \u2014 the SIXTEENTH\n// consecutive queue/ledger agreement)",
             "the v93-era LOGIN + CALCULATOR\n// pair last re-shot v93 [v93 < v94 < v95 < v96 < v97 < v98]; the pair's\n// SIXTH re-run [v59 \u2192 v66 \u2192 v75 \u2192 v81 \u2192 v87 \u2192 v93 \u2192 v99] \u2014 the TWENTY-SECOND\n// consecutive queue/ledger agreement)"),
        ],
        "scripts/parity-probes/arbit-v99.sh": [
            ("(the v87-era pair's fresh sweep \u2014\n# the calculator dialog + the login view, last re-shot v87; the pair's\n# FIFTH re-run [v59 \u2192 v66 \u2192 v75 \u2192 v81 \u2192 v87 \u2192 v99])",
             "(the v93-era pair's fresh sweep \u2014\n# the calculator dialog + the login view, last re-shot v93; the pair's\n# SIXTH re-run [v59 \u2192 v66 \u2192 v75 \u2192 v81 \u2192 v87 \u2192 v93 \u2192 v99])"),
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

    # residual old-token check across all six files
    LEGIT = ("v87 pin (the close-button", "\u2192 v93 \u2192 v99",
             "v93 < v94", "the v93-era")
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(r"v87(?![0-9])|v88(?![0-9])|v89(?![0-9])|v90(?![0-9])|v91(?![0-9])|v92(?![0-9])|FIFTH re-run|SIXTEENTH|FIFTEENTH|re-shot v87|v92 plan's|refvlm93|clonevlm93|reflogin93|clonelogin93|calc93|/tmp/vlm93", text):
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
