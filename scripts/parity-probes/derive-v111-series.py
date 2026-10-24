#!/usr/bin/env python3
"""Derive the v111 probe series from the v105 lineage (the LOGIN + CALCULATOR
pair — the login view + the calculator dialog at desktop 1280x800, EIGHTH
re-run [v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm105->refvlm111, clonevlm105->clonevlm111,
     reflogin105->reflogin111, clonelogin105->clonelogin111,
     refcalc105->refcalc111, clonecalc105->clonecalc111,
     /tmp/vlm105->/tmp/vlm111, v105->v111
  2. History corrections (era marker v99-era -> v105-era, last-re-shot
     v99 -> v105, the re-run bracket + ordinal SEVENTH->EIGHTH, the
     oldest-remaining list bumped to the current era [v105 < v106 <
     v107 < v108 < v109 < v110], the plan attribution v104 -> v110, the
     agreement count TWENTY-EIGHTH -> THIRTY-FOURTH).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (each correction replaces the same
number of lines) so build-twohalf-v111.py inherits the v105 line boundaries.
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v105.sh": "scripts/parity-probes/vlm-shots-v111.sh",
    "scripts/parity-probes/login-shots-v105.sh": "scripts/parity-probes/login-shots-v111.sh",
    "scripts/parity-probes/clone-vlmshots-v105.sh": "scripts/parity-probes/clone-vlmshots-v111.sh",
    "scripts/parity-probes/clone-login-shots-v105.sh": "scripts/parity-probes/clone-login-shots-v111.sh",
    "scripts/parity-probes/vlm-compare-v105.mjs": "scripts/parity-probes/vlm-compare-v111.mjs",
    "scripts/parity-probes/arbit-v105.sh": "scripts/parity-probes/arbit-v111.sh",
}

GENERIC = [
    ("refvlm105", "refvlm111"),
    ("clonevlm105", "clonevlm111"),
    ("reflogin105", "reflogin111"),
    ("clonelogin105", "clonelogin111"),
    ("refcalc105", "refcalc111"),
    ("clonecalc105", "clonecalc111"),
    ("/tmp/vlm105", "/tmp/vlm111"),
    ("v105", "v111"),
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
        "scripts/parity-probes/vlm-shots-v111.sh": [
            ("the v99-era LOGIN + CALCULATOR pair, last re-shot\n# v99, now the oldest remaining [v99 < v100 < v101 < v102 < v103 < v104]; the\n# v104 plan's v111 queue suggestion, agreeing with the rotation ledger — the\n# TWENTY-EIGHTH consecutive agreement; the pair's SEVENTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v111]). READ-ONLY",
             "the v105-era LOGIN + CALCULATOR pair, last re-shot\n# v105, now the oldest remaining [v105 < v106 < v107 < v108 < v109 < v110]; the\n# v110 plan's v111 queue suggestion, agreeing with the rotation ledger — the\n# THIRTY-FOURTH consecutive agreement; the pair's EIGHTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111]). READ-ONLY"),
        ],
        "scripts/parity-probes/login-shots-v111.sh": [
            ("cycle's v99-era LOGIN + CALCULATOR pair, last re-shot v99 — the pair's\n# SEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v111], the TWENTY-EIGHTH consecutive\n# queue/ledger agreement)",
             "cycle's v105-era LOGIN + CALCULATOR pair, last re-shot v105 — the pair's\n# EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111], the THIRTY-FOURTH consecutive\n# queue/ledger agreement)"),
        ],
        "scripts/parity-probes/clone-vlmshots-v111.sh": [
            ("v99-era LOGIN + CALCULATOR pair, last re-shot v99 — the pair's SEVENTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v111]). Runs inside",
             "v105-era LOGIN + CALCULATOR pair, last re-shot v105 — the pair's EIGHTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111]). Runs inside"),
        ],
        "scripts/parity-probes/clone-login-shots-v111.sh": [
            ("cycle's v99-era LOGIN + CALCULATOR pair, last re-shot v99 — the pair's\n# SEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v111]). Runs",
             "cycle's v105-era LOGIN + CALCULATOR pair, last re-shot v105 — the pair's\n# EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111]). Runs"),
        ],
        "scripts/parity-probes/vlm-compare-v111.mjs": [
            ("the v99-era LOGIN + CALCULATOR\n// pair last re-shot v99 [v99 < v100 < v101 < v102 < v103 < v104]; the pair's\n// SEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v111] — the TWENTY-EIGHTH\n// consecutive queue/ledger agreement)",
             "the v105-era LOGIN + CALCULATOR\n// pair last re-shot v105 [v105 < v106 < v107 < v108 < v109 < v110]; the pair's\n// EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111] — the THIRTY-FOURTH\n// consecutive queue/ledger agreement)"),
        ],
        "scripts/parity-probes/arbit-v111.sh": [
            ("(the v99-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v99; the pair's\n# SEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v111]). The censuses:",
             "(the v105-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v105; the pair's\n# EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111]). The censuses:"),
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

    # residual old-token check across all six files.
    # LEGIT contexts that must survive: the corrected re-run bracket
    # (→ v93 → v99 → v105 → v111 — the v99 token inside the bracket is
    # history, not a residual), the pin/axes provenance (the v45 F2a /
    # v49 F3 / v59 / v66 / v73 / v87 pins, the v7 G2 login-slate family,
    # the v55 glyph pin), the rule/lesson references (v43 rule, v46
    # incident/read-only, v45 measurement note, v64 rule, v66 lesson/axes,
    # v73 heredoc), and the seedcheck filename (db-seedcheck-v68.cjs).
    # None of those match the residual patterns below.
    RESIDUAL = re.compile(
        r"v99-era|re-shot v99|SEVENTH re-run|TWENTY-EIGHTH|v99 < v100|"
        r"v104 plan's|refvlm105|clonevlm105|reflogin105|clonelogin105|"
        r"calc105arbit|/tmp/vlm105"
    )
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = RESIDUAL.findall(text)
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
