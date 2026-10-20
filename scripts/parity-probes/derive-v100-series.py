#!/usr/bin/env python3
"""Derive the v100 probe series from the v94 lineage (the NETWORTH +
DRILL-DOWN pair — the networth view + the dashboard drill-down EXPANDED
state at desktop 1280x800, SIXTH re-run [v60 -> v67 -> v76 -> v82 -> v88 ->
v94 -> v100]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm94->refvlm100, clonevlm94->clonevlm100,
     refar94->refar100, clonear94->clonear100, /tmp/vlm94->/tmp/vlm100,
     v94->v100
  2. History corrections (last-re-shot version v88 -> v94, re-run bracket +
     ordinal FIFTH->SIXTH, the oldest-remaining bracket, the agreement
     ordinal SEVENTEENTH->TWENTY-THIRD, the census-axes reference v88->v94).

Every replacement is checked; a miss is reported and fails the run.
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v94.sh": "scripts/parity-probes/vlm-shots-v100.sh",
    "scripts/parity-probes/clone-vlmshots-v94.sh": "scripts/parity-probes/clone-vlmshots-v100.sh",
    "scripts/parity-probes/vlm-compare-v94.mjs": "scripts/parity-probes/vlm-compare-v100.mjs",
    "scripts/parity-probes/arbit-v94.sh": "scripts/parity-probes/arbit-v100.sh",
}

GENERIC = [
    ("refvlm94", "refvlm100"),
    ("clonevlm94", "clonevlm100"),
    ("refar94", "refar100"),
    ("clonear94", "clonear100"),
    ("/tmp/vlm94", "/tmp/vlm100"),
    ("v94", "v100"),
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
        "scripts/parity-probes/vlm-shots-v100.sh": [
            ("the\n# v88-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v89-era pair covered by v90, the v88-era pair last re-shot v88 —\n# now the oldest remaining [v88 < v89 < v90 < v91 < v92 < v93]): the desktop",
             "the\n# v94-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v94-era pair last re-shot v94 —\n# now the oldest remaining [v94 < v95 < v96 < v97 < v98 < v99]): the desktop"),
            ("The pair's FIFTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v100] — the SEVENTEENTH consecutive queue/ledger agreement.",
             "The pair's SIXTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100] — the TWENTY-THIRD consecutive queue/ledger agreement."),
        ],
        "scripts/parity-probes/clone-vlmshots-v100.sh": [
            ("the\n# v88-era pair (the re-run cadence's rotation — the pair's FIFTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v100], last re-shot v88, the SEVENTEENTH consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the\n# NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED state.",
             "the\n# v94-era pair (the re-run cadence's rotation — the pair's SIXTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100], last re-shot v94, the TWENTY-THIRD consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the\n# NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED state."),
        ],
        "scripts/parity-probes/vlm-compare-v100.mjs": [
            ("// re-run of the v88-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v89-era pair covered by v90, the v88-era\n// pair last re-shot v88 — now the oldest remaining [v88 < v89 < v90 < v91\n// < v92 < v93]; the pair's FIFTH re-run [v60 → v67 → v76 → v82 → v88 → v100] —\n// the SEVENTEENTH consecutive queue/ledger agreement): (1) the NETWORTH view's",
             "// re-run of the v94-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v94-era\n// pair last re-shot v94 — now the oldest remaining [v94 < v95 < v96 < v97\n// < v98 < v99]; the pair's SIXTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100] —\n// the TWENTY-THIRD consecutive queue/ledger agreement): (1) the NETWORTH view's"),
        ],
        "scripts/parity-probes/arbit-v100.sh": [
            ("# rule, at DESKTOP 1280x800 on BOTH sides (the v88-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v88; the pair's FIFTH re-run [v60 → v67 → v76 → v82 → v88 → v100] — the\n# SEVENTEENTH consecutive queue/ledger agreement). The censuses (the v88\n# census axes re-measured — a drift re-check):",
             "# rule, at DESKTOP 1280x800 on BOTH sides (the v94-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v94; the pair's SIXTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100] — the\n# TWENTY-THIRD consecutive queue/ledger agreement). The censuses (the v94\n# census axes re-measured — a drift re-check):"),
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
    # (v60 ... v88 -> v94 -> v100), the new-era tokens (v94-era / re-shot
    # v94 / the v94 census), pin provenance (v41/v44/v46/v50/v53/v60/v63/
    # v67/v82 pins), the v75 login-retry convention, and the compare labels'
    # v60-era origin framing.
    LEGIT = ("v60-era pair's fresh re-run", "→ v94 → v100",
             "v94 < v95", "the v94-era", "re-shot v94", "the v94 census",
             "pin", "v75 login-retry", "The v67", "v67 F4", "v82 completion")
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(r"v88-era|v89-era|covered by v90|\[v88 <|FIFTH re-run|SEVENTEENTH|last re-shot v88|refvlm94|clonevlm94|refar94|clonear94|/tmp/vlm94", text):
            ctx = text[max(0, m.start() - 40):m.end() + 40]
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
