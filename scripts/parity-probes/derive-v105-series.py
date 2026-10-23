#!/usr/bin/env python3
"""Derive the v105 probe series from the v99 lineage (the LOGIN + CALCULATOR
pair — the login view + the calculator dialog at desktop 1280x800, SEVENTH
re-run [v59 -> v66 -> v75 -> v81 -> v87 -> v93 -> v99 -> v105]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm99->refvlm105, clonevlm99->clonevlm105,
     reflogin99->reflogin105, clonelogin99->clonelogin105,
     refcalc99->refcalc105, clonecalc99->clonecalc105,
     /tmp/vlm99->/tmp/vlm105, v99->v105
  2. History corrections (last-re-shot version v93 -> v99, era marker
     v93-era -> v99-era, re-run bracket + ordinal SIXTH->SEVENTH, the
     oldest-remaining list bumped to the current era [v99 < v100 < v101 <
     v102 < v103 < v104], the plan attribution v98 -> v104, the agreement
     count TWENTY-SECOND -> TWENTY-EIGHTH).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (each correction replaces the same
number of lines) so build-twohalf-v105.py inherits the v99 line boundaries.
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v99.sh": "scripts/parity-probes/vlm-shots-v105.sh",
    "scripts/parity-probes/login-shots-v99.sh": "scripts/parity-probes/login-shots-v105.sh",
    "scripts/parity-probes/clone-vlmshots-v99.sh": "scripts/parity-probes/clone-vlmshots-v105.sh",
    "scripts/parity-probes/clone-login-shots-v99.sh": "scripts/parity-probes/clone-login-shots-v105.sh",
    "scripts/parity-probes/vlm-compare-v99.mjs": "scripts/parity-probes/vlm-compare-v105.mjs",
    "scripts/parity-probes/arbit-v99.sh": "scripts/parity-probes/arbit-v105.sh",
}

GENERIC = [
    ("refvlm99", "refvlm105"),
    ("clonevlm99", "clonevlm105"),
    ("reflogin99", "reflogin105"),
    ("clonelogin99", "clonelogin105"),
    ("refcalc99", "refcalc105"),
    ("clonecalc99", "clonecalc105"),
    ("/tmp/vlm99", "/tmp/vlm105"),
    ("v99", "v105"),
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
        "scripts/parity-probes/vlm-shots-v105.sh": [
            ("the v93-era LOGIN + CALCULATOR pair, last re-shot\n# v93, now the oldest remaining [v93 < v94 < v95 < v96 < v97 < v98]; the\n# v98 plan's v105 queue suggestion, agreeing with the rotation ledger — the\n# TWENTY-SECOND consecutive agreement; the pair's SIXTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v105]). READ-ONLY",
             "the v99-era LOGIN + CALCULATOR pair, last re-shot\n# v99, now the oldest remaining [v99 < v100 < v101 < v102 < v103 < v104]; the\n# v104 plan's v105 queue suggestion, agreeing with the rotation ledger — the\n# TWENTY-EIGHTH consecutive agreement; the pair's SEVENTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105]). READ-ONLY"),
        ],
        "scripts/parity-probes/login-shots-v105.sh": [
            ("cycle's v93-era LOGIN + CALCULATOR pair, last re-shot v93 — the pair's\n# SIXTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v105], the TWENTY-SECOND consecutive\n# queue/ledger agreement)",
             "cycle's v99-era LOGIN + CALCULATOR pair, last re-shot v99 — the pair's\n# SEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105], the TWENTY-EIGHTH consecutive\n# queue/ledger agreement)"),
        ],
        "scripts/parity-probes/clone-vlmshots-v105.sh": [
            ("v93-era LOGIN + CALCULATOR pair, last re-shot v93 — the pair's SIXTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v105]). Runs inside",
             "v99-era LOGIN + CALCULATOR pair, last re-shot v99 — the pair's SEVENTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105]). Runs inside"),
        ],
        "scripts/parity-probes/clone-login-shots-v105.sh": [
            ("cycle's v93-era LOGIN + CALCULATOR pair, last re-shot v93 — the pair's\n# SIXTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v105]). Runs",
             "cycle's v99-era LOGIN + CALCULATOR pair, last re-shot v99 — the pair's\n# SEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105]). Runs"),
        ],
        "scripts/parity-probes/vlm-compare-v105.mjs": [
            ("the v93-era LOGIN + CALCULATOR\n// pair last re-shot v93 [v93 < v94 < v95 < v96 < v97 < v98]; the pair's\n// SIXTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v105] — the TWENTY-SECOND\n// consecutive queue/ledger agreement)",
             "the v99-era LOGIN + CALCULATOR\n// pair last re-shot v99 [v99 < v100 < v101 < v102 < v103 < v104]; the pair's\n// SEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105] — the TWENTY-EIGHTH\n// consecutive queue/ledger agreement)"),
        ],
        "scripts/parity-probes/arbit-v105.sh": [
            ("(the v93-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v93; the pair's\n# SIXTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v105]). The censuses:",
             "(the v99-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v99; the pair's\n# SEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105]). The censuses:"),
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
    # LEGIT contexts that must survive: the corrected re-run bracket
    # (→ v93 → v99 → v105), the corrected state tokens (re-shot v99,
    # v99-era), the pin/axes provenance (the v45 F2a/v49 F3/v59/v66/v73/
    # v87 pins, the v7 G2 login-slate family, the v55 glyph pin), the
    # rule/lesson references (v43 rule, v46 incident/read-only, v45
    # measurement note, v64 rule, v66 lesson/axes, v73 heredoc), and the
    # seedcheck filename (db-seedcheck-v68.cjs).
    LEGIT = ("→ v93 → v99 → v105", "re-shot v99", "v99-era",
             "v45 F2a pin", "v49 F3 pin", "v59 pin", "v66 pin", "v73 pin",
             "v87 pin (the close-button", "v7 G2", "v55 glyph pin",
             "v43 rule", "v46 ", "v46 incident", "v45 measurement",
             "v64 rule", "v66 lesson", "v66 axes", "v73 heredoc",
             "seedcheck-v68")
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(r"v93-era|re-shot v93|SIXTH re-run|TWENTY-SECOND|v93 < v94|v98 plan's|refvlm99|clonevlm99|reflogin99|clonelogin99|calc99arbit|/tmp/vlm99", text):
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
