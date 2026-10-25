#!/usr/bin/env python3
"""Derive the v119 probe series from the v113 lineage (the DASHBOARD
below-the-fold pair — the BUDGET GUIDELINES card + the QUICK-ACTION row at
desktop 1280x800, NINTH re-run
[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119]).

NOTE the ordinal off-by-one in the v113 lineage (flagged by the probe
README's v119 queue note, verified against vlm-shots-v113.sh's own header):
the v113 header reads "SEVENTH re-run" for a 9-entry bracket where the
v112-lineage convention reads EIGHTH for 9 entries. The BRACKET is the
authority per the queue-prose verification lesson; v119 = the NINTH re-run
by the consistent convention (10 entries, v61 the original).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm113->refvlm119, clonevlm113->clonevlm119,
     refar113->refar119, clonear113->clonear119,
     /tmp/vlm113->/tmp/vlm119, v113->v119
  2. History corrections (era marker v107-era -> v113-era, last-re-shot
     v107 -> v113, the oldest-remaining list bumped to the current era
     [v113 < v114 < v115 < v116 < v117 < v118], the ordinal off-by-one
     fixed SEVENTH/EIGHTH -> NINTH, the re-run bracket extended
     [v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119],
     the agreement count THIRTY-SIXTH -> FORTY-SECOND, the re-proves window
     v101-v107 -> v101-v113, the arbit verdict reference "The v107" ->
     "The v113" [the v113 verdict was IDENTICAL — the sixth consecutive
     IDENTICAL for this pair], the drift-re-check "since v107" -> "since
     v113", and the compare PAIR banner's era/ordinal/bracket).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v113.sh": "scripts/parity-probes/vlm-shots-v119.sh",
    "scripts/parity-probes/clone-vlmshots-v113.sh": "scripts/parity-probes/clone-vlmshots-v119.sh",
    "scripts/parity-probes/vlm-compare-v113.mjs": "scripts/parity-probes/vlm-compare-v119.mjs",
    "scripts/parity-probes/arbit-v113.sh": "scripts/parity-probes/arbit-v119.sh",
}

GENERIC = [
    ("refvlm113", "refvlm119"),
    ("clonevlm113", "clonevlm119"),
    ("refar113", "refar119"),
    ("clonear113", "clonear119"),
    ("/tmp/vlm113", "/tmp/vlm119"),
    ("v113", "v119"),
]


def main():
    ok = True
    for src, dst in FILES.items():
        text = open(src, encoding="utf-8").read()
        for old, new in GENERIC:
            text = text.replace(old, new)
        open(dst, "w", encoding="utf-8").write(text)
        print(f"derived {dst} (generic swaps applied)")

    print("\n--- history corrections (against the POST-swap state) ---")
    corr_map = {
        "scripts/parity-probes/vlm-shots-v119.sh": [
            ("# v107-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v107 — now\n# the oldest remaining [v107 < v108 < v109 < v110 < v111 < v112]; the pair's SEVENTH\n# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v119] — the THIRTY-SIXTH consecutive",
             "# v113-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v113 — now\n# the oldest remaining [v113 < v114 < v115 < v116 < v117 < v118]; the pair's NINTH\n# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119] — the FORTY-SECOND consecutive"),
            ("The v119 re-run re-proves the v61-era surfaces after\n# v101-v107 (the mobile twins, the height pins, the stat-card divider pin).",
             "The v119 re-run re-proves the v61-era surfaces after\n# v101-v113 (the mobile twins, the height pins, the stat-card divider pin)."),
        ],
        "scripts/parity-probes/clone-vlmshots-v119.sh": [
            ("# v107-era pair (the re-run cadence's rotation — the pair's EIGHTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v119]): the DASHBOARD at desktop 1280x800",
             "# v113-era pair (the re-run cadence's rotation — the pair's NINTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119]): the DASHBOARD at desktop 1280x800"),
            ("re-proved again by the v119 re-run after v101-v107",
             "re-proved again by the v119 re-run after v101-v113"),
        ],
        "scripts/parity-probes/vlm-compare-v119.mjs": [
            ("the v107-era pair EIGHTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v119] — the THIRTY-SIXTH consecutive queue/ledger",
             "the v113-era pair NINTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119] — the FORTY-SECOND consecutive queue/ledger"),
            ("the v119 EIGHTH re-run of the v107-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v119]",
             "the v119 NINTH re-run of the v113-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119]"),
        ],
        "scripts/parity-probes/arbit-v119.sh": [
            ("# 1280x800 (the v107-era pair's EIGHTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v119]\n# — the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET\n# GUIDELINES card + the QUICK-ACTION row, last re-shot v107). The v107\n# verdict was IDENTICAL with ZERO style flags",
             "# 1280x800 (the v113-era pair's NINTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119]\n# — the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET\n# GUIDELINES card + the QUICK-ACTION row, last re-shot v113). The v113\n# verdict was IDENTICAL with ZERO style flags"),
            ("censuses are the v61/v83 qa-census axes re-measured (a drift re-check\n# since v107):",
             "censuses are the v61/v83 qa-census axes re-measured (a drift re-check\n# since v113):"),
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
    # (→ v101 → v107 → v113 → v119), the corrected state tokens (re-shot v113,
    # v113-era, since v113, v101-v113), the pin/axes provenance (the v41
    # summary, the v44 hero/stat pins, the v45 F3 hover pin, the v51 F4 mobile
    # census, the v43 misattribution lesson), the rule/lesson references
    # (v43 rule, v46 rule, the v56 timeout split lesson, the v60 lesson, the
    # v64 rule, the v66 discipline, the v73 heredoc lesson, the v75
    # login-retry convention), the seedcheck filename (db-seedcheck-v68.cjs),
    # and the v61/v83 qa-census axes provenance.
    LEGIT = (
        "→ v101 → v107 → v113 → v119", "re-shot v113", "v113-era",
        "since v113", "v101-v113",
        "v41 summary", "v44 hero/stat", "v45 F3", "v51 F4", "v61/v83",
        "v43 rule", "v46 ", "v56 lesson", "v60 lesson", "v64 rule",
        "v66 discipline", "v73 heredoc", "seedcheck-v68", "v75",
        "v43 misattribution", "v61-era",
    )
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v107-era|re-shot v107|EIGHTH re-run|SEVENTH|THIRTY-SIXTH|v107 < v108|refvlm113|clonevlm113|refar113|clonear113|/tmp/vlm113",
            text,
        ):
            ctx = text[max(0, m.start() - 45):m.end() + 45]
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
