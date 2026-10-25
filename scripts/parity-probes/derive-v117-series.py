#!/usr/bin/env python3
"""Derive the v117 probe series from the v111 lineage (the LOGIN + CALCULATOR
pair — the login view + the calculator dialog at desktop 1280x800, NINTH
re-run [v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 -> v105 -> v111 -> v117]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied — the
POST-SWAP-FRAGMENT RULE: corrections are written against the POST-swap
state because the generic swap consumes the version tokens first):
  1. Generic swaps: refvlm111->refvlm117, clonevlm111->clonevlm117,
     reflogin111->reflogin117, clonelogin111->clonelogin117,
     refcalc111->refcalc117, clonecalc111->clonecalc117,
     /tmp/vlm111->/tmp/vlm117, v111->v117
  2. History corrections (era marker v105-era -> v111-era, last-re-shot
     v105 -> v111, the re-run bracket + ordinal EIGHTH->NINTH, the
     oldest-remaining list bumped to the current era [v111 < v112 <
     v113 < v114 < v115 < v116], the plan attribution v110 -> v116, the
     agreement count THIRTY-FOURTH -> FORTIETH).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (each correction replaces the same
number of lines) so build-twohalf-v117.py inherits the v111 line boundaries.
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v111.sh": "scripts/parity-probes/vlm-shots-v117.sh",
    "scripts/parity-probes/login-shots-v111.sh": "scripts/parity-probes/login-shots-v117.sh",
    "scripts/parity-probes/clone-vlmshots-v111.sh": "scripts/parity-probes/clone-vlmshots-v117.sh",
    "scripts/parity-probes/clone-login-shots-v111.sh": "scripts/parity-probes/clone-login-shots-v117.sh",
    "scripts/parity-probes/vlm-compare-v111.mjs": "scripts/parity-probes/vlm-compare-v117.mjs",
    "scripts/parity-probes/arbit-v111.sh": "scripts/parity-probes/arbit-v117.sh",
}

GENERIC = [
    ("refvlm111", "refvlm117"),
    ("clonevlm111", "clonevlm117"),
    ("reflogin111", "reflogin117"),
    ("clonelogin111", "clonelogin117"),
    ("refcalc111", "refcalc117"),
    ("clonecalc111", "clonecalc117"),
    ("/tmp/vlm111", "/tmp/vlm117"),
    ("v111", "v117"),
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
    # in their POST-SWAP form — the POST-SWAP-FRAGMENT RULE)
    corr_map = {
        "scripts/parity-probes/vlm-shots-v117.sh": [
            ("the v105-era LOGIN + CALCULATOR pair, last re-shot\n# v105, now the oldest remaining [v105 < v106 < v107 < v108 < v109 < v110]; the\n# v110 plan's v117 queue suggestion, agreeing with the rotation ledger — the\n# THIRTY-FOURTH consecutive agreement; the pair's EIGHTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v117]). READ-ONLY",
             "the v111-era LOGIN + CALCULATOR pair, last re-shot\n# v111, now the oldest remaining [v111 < v112 < v113 < v114 < v115 < v116]; the\n# v116 plan's v117 queue suggestion, agreeing with the rotation ledger — the\n# FORTIETH consecutive agreement; the pair's NINTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117]). READ-ONLY"),
        ],
        "scripts/parity-probes/login-shots-v117.sh": [
            ("cycle's v105-era LOGIN + CALCULATOR pair, last re-shot v105 — the pair's\n# EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v117], the THIRTY-FOURTH consecutive\n# queue/ledger agreement)",
             "cycle's v111-era LOGIN + CALCULATOR pair, last re-shot v111 — the pair's\n# NINTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117], the FORTIETH consecutive\n# queue/ledger agreement)"),
        ],
        "scripts/parity-probes/clone-vlmshots-v117.sh": [
            ("v105-era LOGIN + CALCULATOR pair, last re-shot v105 — the pair's EIGHTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v117]). Runs inside",
             "v111-era LOGIN + CALCULATOR pair, last re-shot v111 — the pair's NINTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117]). Runs inside"),
        ],
        "scripts/parity-probes/clone-login-shots-v117.sh": [
            ("cycle's v105-era LOGIN + CALCULATOR pair, last re-shot v105 — the pair's\n# EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v117]). Runs",
             "cycle's v111-era LOGIN + CALCULATOR pair, last re-shot v111 — the pair's\n# NINTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117]). Runs"),
        ],
        "scripts/parity-probes/vlm-compare-v117.mjs": [
            ("the v105-era LOGIN + CALCULATOR\n// pair last re-shot v105 [v105 < v106 < v107 < v108 < v109 < v110]; the pair's\n// EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v117] — the THIRTY-FOURTH\n// consecutive queue/ledger agreement)",
             "the v111-era LOGIN + CALCULATOR\n// pair last re-shot v111 [v111 < v112 < v113 < v114 < v115 < v116]; the pair's\n// NINTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117] — the FORTIETH\n// consecutive queue/ledger agreement)"),
        ],
        "scripts/parity-probes/arbit-v117.sh": [
            ("(the v105-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v105; the pair's\n# EIGHTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v117]). The censuses:",
             "(the v111-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v111; the pair's\n# NINTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117]). The censuses:"),
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
    # (→ v93 → v99 → v105 → v111 → v117 — the v105/v111 tokens inside the
    # bracket are history, not residuals), the pin/axes provenance (the
    # v45 F2a / v49 F3 / v59 / v66 / v73 / v87 / v111 pins, the v7 G2
    # login-slate family, the v55 glyph pin), the rule/lesson references
    # (v43 rule, v46 incident/read-only, v45 measurement note, v64 rule,
    # v66 lesson/axes, v73 heredoc, v72 structural class), and the seedcheck
    # filename (db-seedcheck-v68.cjs). None of those match the residual
    # patterns below.
    RESIDUAL = re.compile(
        r"v105-era|re-shot v105|EIGHTH re-run|THIRTY-FOURTH|v105 < v106|"
        r"v110 plan's|refvlm111|clonevlm111|reflogin111|clonelogin111|"
        r"refcalc111|clonecalc111|calc111arbit|/tmp/vlm111"
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
