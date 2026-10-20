#!/usr/bin/env python3
"""Derive the v101 probe series from the v95 lineage (the DASHBOARD pair —
the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET GUIDELINES
card + the QUICK-ACTION row, at desktop 1280x800, SIXTH re-run
[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm95->refvlm101, clonevlm95->clonevlm101,
     refar95->refar101, clonear95->clonear101, /tmp/vlm95->/tmp/vlm101,
     v95->v101
  2. History corrections (last-re-shot version v89 -> v95, re-run bracket +
     ordinal FIFTH->SIXTH, the oldest-remaining bracket, the agreement
     ordinal EIGHTEENTH->TWENTY-FOURTH, the previous-verdict reference
     v89->v95, the "after v89-v94"->"after v95-v100", the census-axes
     drift-check baseline -> v95).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (each correction replaces the same
number of lines) so build-twohalf-v101.py inherits the v95 line boundaries.
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v95.sh": "scripts/parity-probes/vlm-shots-v101.sh",
    "scripts/parity-probes/clone-vlmshots-v95.sh": "scripts/parity-probes/clone-vlmshots-v101.sh",
    "scripts/parity-probes/vlm-compare-v95.mjs": "scripts/parity-probes/vlm-compare-v101.mjs",
    "scripts/parity-probes/arbit-v95.sh": "scripts/parity-probes/arbit-v101.sh",
}

GENERIC = [
    ("refvlm95", "refvlm101"),
    ("clonevlm95", "clonevlm101"),
    ("refar95", "refar101"),
    ("clonear95", "clonear101"),
    ("/tmp/vlm95", "/tmp/vlm101"),
    ("v95", "v101"),
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
        "scripts/parity-probes/vlm-shots-v101.sh": [
            ("the\n# v89-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v89 — now\n# the oldest remaining [v89 < v90 < v91 < v92 < v93 < v94]; the pair's FIFTH\n# re-run [v61 → v68 → v77 → v83 → v89 → v101] — the EIGHTEENTH consecutive\n# queue/ledger agreement).",
             "the\n# v95-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v95 — now\n# the oldest remaining [v95 < v96 < v97 < v98 < v99 < v100]; the pair's SIXTH\n# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101] — the TWENTY-FOURTH consecutive\n# queue/ledger agreement)."),
            ("The v101 re-run re-proves the v61-era surfaces after\n# v89-v94 (the mobile twins, the height pins, the stat-card divider pin).",
             "The v101 re-run re-proves the v61-era surfaces after\n# v95-v100 (the mobile twins, the height pins, the stat-card divider pin)."),
        ],
        "scripts/parity-probes/clone-vlmshots-v101.sh": [
            ("the\n# v89-era pair (the re-run cadence's rotation — the pair's FIFTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v101]): the DASHBOARD at desktop 1280x800",
             "the\n# v95-era pair (the re-run cadence's rotation — the pair's SIXTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101]): the DASHBOARD at desktop 1280x800"),
            ("re-proved again by the v101 re-run after v89-v94). Runs",
             "re-proved again by the v101 re-run after v95-v100). Runs"),
        ],
        "scripts/parity-probes/vlm-compare-v101.mjs": [
            ("the v89-era pair FIFTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v101] — the EIGHTEENTH consecutive queue/ledger\n// agreement: the DASHBOARD's",
             "the v95-era pair SIXTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101] — the TWENTY-FOURTH consecutive queue/ledger\n// agreement: the DASHBOARD's"),
            ("the v101 FIFTH re-run of the v89-era pair [v61 → v68 → v77 → v83 → v89 → v101]",
             "the v101 SIXTH re-run of the v95-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101]"),
        ],
        "scripts/parity-probes/arbit-v101.sh": [
            ("the v89-era pair's FIFTH re-run [v61 → v68 → v77 → v83 → v89 → v101]\n# — the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET\n# GUIDELINES card + the QUICK-ACTION row, last re-shot v89). The v89\n# verdict was IDENTICAL with ZERO style flags",
             "the v95-era pair's SIXTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101]\n# — the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET\n# GUIDELINES card + the QUICK-ACTION row, last re-shot v95). The v95\n# verdict was IDENTICAL with ZERO style flags"),
            ("a drift re-check\n# since v61/v83):",
             "a drift re-check\n# since v95):"),
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
    # (v61 ... v89 -> v95 -> v101), the new-era tokens (v95-era / re-shot
    # v95 / the v95 verdict / since v95 / after v95-v100 / v95 < v96),
    # pin provenance (v45/v46/v51/v60/v61/v64/v66/v68/v73/v75/v83 tokens),
    # and the axes provenance (v61/v83).
    LEGIT = ("→ v95 → v101", "v95 < v96", "the v95-era", "re-shot v95",
             "the v95 verdict", "since v95", "after v95-v100",
             "v61/v83", "v61-era", "v61 STRETCH", "v45 F3", "v46 ",
             "v51 F4", "v60 lesson", "v64 rule", "v66 discipline",
             "db-seedcheck-v68", "v73 heredoc", "v75 convention")
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(r"v89-era|FIFTH re-run|EIGHTEENTH|last re-shot v89|\[v89 <|after v89-v94|refvlm95|clonevlm95|refar95|clonear95|/tmp/vlm95", text):
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
