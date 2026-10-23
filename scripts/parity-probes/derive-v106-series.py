#!/usr/bin/env python3
"""Derive the v106 probe series from the v100 lineage (the NETWORTH +
DRILL-DOWN pair — the networth view + the dashboard drill-down EXPANDED
state at desktop 1280x800, SEVENTH re-run
[v60 -> v67 -> v76 -> v82 -> v88 -> v94 -> v100 -> v106]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm100->refvlm106, clonevlm100->clonevlm106,
     refar100->refar106, clonear100->clonear106,
     /tmp/vlm100->/tmp/vlm106, v100->v106
  2. History corrections (era marker v94-era -> v100-era, last-re-shot
     v94 -> v100, the oldest-remaining list bumped to the current era
     [v100 < v101 < v102 < v103 < v104 < v105], re-run ordinal
     SIXTH->SEVENTH, the re-run bracket extended [v60 -> v67 -> v76 ->
     v82 -> v88 -> v94 -> v100 -> v106], the agreement count
     TWENTY-THIRD -> TWENTY-NINTH, the census provenance "the v94 census
     axes" -> "the v100 census axes").

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING except where the history
corrections deliberately add the bracket-extension token (audited in the
line-count report).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v100.sh": "scripts/parity-probes/vlm-shots-v106.sh",
    "scripts/parity-probes/clone-vlmshots-v100.sh": "scripts/parity-probes/clone-vlmshots-v106.sh",
    "scripts/parity-probes/vlm-compare-v100.mjs": "scripts/parity-probes/vlm-compare-v106.mjs",
    "scripts/parity-probes/arbit-v100.sh": "scripts/parity-probes/arbit-v106.sh",
}

GENERIC = [
    ("refvlm100", "refvlm106"),
    ("clonevlm100", "clonevlm106"),
    ("refar100", "refar106"),
    ("clonear100", "clonear106"),
    ("/tmp/vlm100", "/tmp/vlm106"),
    ("v100", "v106"),
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
        "scripts/parity-probes/vlm-shots-v106.sh": [
            ("a fresh re-run of the\n# v94-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v94-era pair last re-shot v94 —\n# now the oldest remaining [v94 < v95 < v96 < v97 < v98 < v99]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's SIXTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v106] — the TWENTY-THIRD consecutive queue/ledger agreement.",
             "a fresh re-run of the\n# v100-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v100-era pair last re-shot v100 —\n# now the oldest remaining [v100 < v101 < v102 < v103 < v104 < v105]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's SEVENTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106] — the TWENTY-NINTH consecutive queue/ledger agreement."),
        ],
        "scripts/parity-probes/clone-vlmshots-v106.sh": [
            ("a fresh re-run of the\n# v94-era pair (the re-run cadence's rotation — the pair's SIXTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v106], last re-shot v94, the TWENTY-THIRD consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the",
             "a fresh re-run of the\n# v100-era pair (the re-run cadence's rotation — the pair's SEVENTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106], last re-shot v100, the TWENTY-NINTH consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the"),
        ],
        "scripts/parity-probes/vlm-compare-v106.mjs": [
            ("a fresh\n// re-run of the v94-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v94-era\n// pair last re-shot v94 — now the oldest remaining [v94 < v95 < v96 < v97\n// < v98 < v99]; the pair's SIXTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v106] —\n// the TWENTY-THIRD consecutive queue/ledger agreement): (1) the NETWORTH view's",
             "a fresh\n// re-run of the v100-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v100-era\n// pair last re-shot v100 — now the oldest remaining [v100 < v101 < v102 < v103\n// < v104 < v105]; the pair's SEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106] —\n// the TWENTY-NINTH consecutive queue/ledger agreement): (1) the NETWORTH view's"),
        ],
        "scripts/parity-probes/arbit-v106.sh": [
            ("at DESKTOP 1280x800 on BOTH sides (the v94-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v94; the pair's SIXTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v106] — the\n# TWENTY-THIRD consecutive queue/ledger agreement). The censuses (the v94\n# census axes re-measured — a drift re-check):",
             "at DESKTOP 1280x800 on BOTH sides (the v100-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v100; the pair's SEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106] — the\n# TWENTY-NINTH consecutive queue/ledger agreement). The censuses (the v100\n# census axes re-measured — a drift re-check):"),
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
    # (→ v94 → v100 → v106), the corrected state tokens (re-shot v100,
    # v100-era), the pin/axes provenance (the v41/v46/v50/v53/v60/v63/v67/v82
    # pins), the rule/lesson references (v43 rule, v46 rule, v56/v64/v66/v73
    # lessons, the v56 timeout split lesson), and the seedcheck filename
    # (db-seedcheck-v68.cjs).
    LEGIT = (
        "→ v94 → v100 → v106", "re-shot v100", "v100-era",
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
            r"v94-era|re-shot v94|SIXTH re-run|TWENTY-THIRD|v94 < v95|refvlm100|clonevlm100|refar100|clonear100|/tmp/vlm100",
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
        status = "OK" if sn == dn else f"DRIFT ({dn - sn:+d} — expected ONLY the bracket-extension correction)"
        print(f"line-count {dst}: {dn + 1} lines (source {sn + 1}) — {status}")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
