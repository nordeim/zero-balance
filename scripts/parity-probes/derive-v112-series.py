#!/usr/bin/env python3
"""Derive the v112 probe series from the v106 lineage (the NETWORTH +
DRILL-DOWN pair — the networth view + the dashboard drill-down EXPANDED
state at desktop 1280x800, EIGHTH re-run
[v60 -> v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106 -> v112]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm106->refvlm112, clonevlm106->clonevlm112,
     refar106->refar112, clonear106->clonear112,
     /tmp/vlm106->/tmp/vlm112, v106->v112
  2. History corrections (era marker v100-era -> v106-era, last-re-shot
     v100 -> v106, the oldest-remaining list bumped to the current era
     [v106 < v107 < v108 < v109 < v110 < v111], re-run ordinal
     SEVENTH->EIGHTH, the re-run bracket extended [v60 -> v67 -> v76 ->
     v82 -> v88 -> v94 -> v100 -> v106 -> v112], the agreement count
     TWENTY-NINTH -> THIRTY-FIFTH, the census provenance "the v100
     census axes" -> "the v106 census axes").

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v106.sh": "scripts/parity-probes/vlm-shots-v112.sh",
    "scripts/parity-probes/clone-vlmshots-v106.sh": "scripts/parity-probes/clone-vlmshots-v112.sh",
    "scripts/parity-probes/vlm-compare-v106.mjs": "scripts/parity-probes/vlm-compare-v112.mjs",
    "scripts/parity-probes/arbit-v106.sh": "scripts/parity-probes/arbit-v112.sh",
}

GENERIC = [
    ("refvlm106", "refvlm112"),
    ("clonevlm106", "clonevlm112"),
    ("refar106", "refar112"),
    ("clonear106", "clonear112"),
    ("/tmp/vlm106", "/tmp/vlm112"),
    ("v106", "v112"),
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
    corr_map = {
        "scripts/parity-probes/vlm-shots-v112.sh": [
            ("# v100-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v100-era pair last re-shot v100 —\n# now the oldest remaining [v100 < v101 < v102 < v103 < v104 < v105]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's SEVENTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v112] — the TWENTY-NINTH consecutive queue/ledger agreement.",
             "# v106-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v106-era pair last re-shot v106 —\n# now the oldest remaining [v106 < v107 < v108 < v109 < v110 < v111]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's EIGHTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112] — the THIRTY-FIFTH consecutive queue/ledger agreement."),
        ],
        "scripts/parity-probes/clone-vlmshots-v112.sh": [
            ("# v100-era pair (the re-run cadence's rotation — the pair's SEVENTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v112], last re-shot v100, the TWENTY-NINTH consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the",
             "# v106-era pair (the re-run cadence's rotation — the pair's EIGHTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112], last re-shot v106, the THIRTY-FIFTH consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the"),
        ],
        "scripts/parity-probes/vlm-compare-v112.mjs": [
            ("// re-run of the v100-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v100-era\n// pair last re-shot v100 — now the oldest remaining [v100 < v101 < v102 < v103\n// < v104 < v105]; the pair's SEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v112] —\n// the TWENTY-NINTH consecutive queue/ledger agreement): (1) the NETWORTH view's",
             "// re-run of the v106-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v106-era\n// pair last re-shot v106 — now the oldest remaining [v106 < v107 < v108 < v109\n// < v110 < v111]; the pair's EIGHTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112] —\n// the THIRTY-FIFTH consecutive queue/ledger agreement): (1) the NETWORTH view's"),
        ],
        "scripts/parity-probes/arbit-v112.sh": [
            ("# rule, at DESKTOP 1280x800 on BOTH sides (the v100-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v100; the pair's SEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v112] — the\n# TWENTY-NINTH consecutive queue/ledger agreement). The censuses (the v100\n# census axes re-measured — a drift re-check):",
             "# rule, at DESKTOP 1280x800 on BOTH sides (the v106-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v106; the pair's EIGHTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112] — the\n# THIRTY-FIFTH consecutive queue/ledger agreement). The censuses (the v106\n# census axes re-measured — a drift re-check):"),
        ],
    }
    for path, pairs in corr_map.items():
        text = open(path, encoding="utf-8").read()
        for old, new in pairs:
            if old not in text:
                print(f"MISS in {path}: {old[:70]!r}")
                ok = False
                continue
            text = text.replace(old, new)
            print(f"applied in {path}: {old[:52]!r} -> corrected")
        open(path, "w", encoding="utf-8").write(text)

    # residual old-token check across all four files
    # LEGIT contexts that must survive: the corrected re-run bracket
    # (→ v100 → v106 → v112), the corrected state tokens (re-shot v106,
    # v106-era), the pin/axes provenance (the v41/v44/v46/v50/v53/v60/v63/
    # v67/v82 pins), the rule/lesson references (v43 rule, v46 rule, the
    # v56 timeout split lesson, the v64 rule, the v66 discipline, the v73
    # heredoc lesson, the v75 login-retry), the seedcheck filename
    # (db-seedcheck-v68.cjs), and the v43 misattribution lesson.
    LEGIT = (
        "→ v100 → v106 → v112", "re-shot v106", "v106-era",
        "v41 summary", "v46 asset-card pin", "v50/v53", "v60 F1", "v60 F2",
        "v63 stat-tile pin", "v67 F4 pin", "v67 networth", "v82 completion",
        "v44 drill-height", "v43 rule", "v46 ", "v56 lesson", "v64 rule",
        "v66 discipline", "v73 heredoc", "seedcheck-v68", "v75 login-retry",
        "v43 misattribution",
    )
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v100-era|re-shot v100|SEVENTH re-run|TWENTY-NINTH|v100 < v101|refvlm106|clonevlm106|refar106|clonear106|/tmp/vlm106",
            text,
        ):
            ctx = text[max(0, m.start() - 45) : m.end() + 45]
            if any(l in ctx for l in LEGIT):
                continue  # legitimate provenance/bracket token
            bad.append(m.group(0))
        if bad:
            print(f"RESIDUAL OLD TOKENS in {dst}: {set(bad)}")
            ok = False
        else:
            print(f"residual check {dst}: clean")

    # line-count report (the two-half builder inherits boundaries)
    for src, dst in FILES.items():
        sn = open(src, encoding="utf-8").read().count("\n")
        dn = open(dst, encoding="utf-8").read().count("\n")
        status = "OK" if sn == dn else f"DRIFT ({dn - sn:+d})"
        print(f"line-count {dst}: {dn + 1} lines (source {sn + 1}) — {status}")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
