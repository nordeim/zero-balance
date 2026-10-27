#!/usr/bin/env python3
"""Derive the v125 probe series from the v119 lineage (the DASHBOARD
below-the-fold pair — the BUDGET GUIDELINES card + the QUICK-ACTION card
row on the dashboard at desktop 1280x800 FULL-PAGE, TENTH re-run
[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v124-era docs' v125 queue names "the pair's TENTH re-run
bracket [v61 -> ... -> v119 -> v125]... derived from vlm-shots-v119.sh's
own NINTH/10-entry header" — verified against the v119 header BEFORE this
derivation: vlm-shots-v119.sh's own header reads "the pair's NINTH
re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119]"
— a 10-ENTRY bracket with the NINTH ordinal (v61 the original, the
entries-minus-one convention). v125 = the TENTH re-run by appending v125
to the v119 header's NINTH bracket. The FORTY-EIGHTH consecutive
queue/ledger agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm119->refvlm125, clonevlm119->clonevlm125,
     refar119->refar125, clonear119->clonear125,
     /tmp/vlm119->/tmp/vlm125, v119->v125
  2. History corrections (era marker v113-era -> v119-era, last-re-shot
     v113 -> v119, the oldest-remaining list bumped to the current era
     [v119 < v120 < v121 < v122 < v123 < v124], re-run ordinal
     NINTH->TENTH, the re-run bracket extended [v61 -> v68 -> v77 -> v83
     -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125], the agreement
     count FORTY-SECOND -> FORTY-EIGHTH, the re-proves window
     v101-v113 -> v101-v119, the arbit verdict reference "The v113" ->
     "The v119" [the v119 verdict was IDENTICAL — verified from the v119
     plan's F3 record], the drift-re-check "since v113" -> "since v119").

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v119.sh": "scripts/parity-probes/vlm-shots-v125.sh",
    "scripts/parity-probes/clone-vlmshots-v119.sh": "scripts/parity-probes/clone-vlmshots-v125.sh",
    "scripts/parity-probes/vlm-compare-v119.mjs": "scripts/parity-probes/vlm-compare-v125.mjs",
    "scripts/parity-probes/arbit-v119.sh": "scripts/parity-probes/arbit-v125.sh",
}

GENERIC = [
    ("refvlm119", "refvlm125"),
    ("clonevlm119", "clonevlm125"),
    ("refar119", "refar125"),
    ("clonear119", "clonear125"),
    ("/tmp/vlm119", "/tmp/vlm125"),
    ("v119", "v125"),
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
        "scripts/parity-probes/vlm-shots-v125.sh": [
            ("# v113-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v113 — now\n# the oldest remaining [v113 < v114 < v115 < v116 < v117 < v118]; the pair's NINTH\n# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v125] — the FORTY-SECOND consecutive\n# queue/ledger agreement).",
             "# v119-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v119 — now\n# the oldest remaining [v119 < v120 < v121 < v122 < v123 < v124]; the pair's TENTH\n# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125] — the FORTY-EIGHTH consecutive\n# queue/ledger agreement)."),
            ("# unpaired before v61]. The v125 re-run re-proves the v61-era surfaces after\n# v101-v113 (the mobile twins, the height pins, the stat-card divider pin).",
             "# unpaired before v61]. The v125 re-run re-proves the v61-era surfaces after\n# v101-v119 (the mobile twins, the height pins, the stat-card divider pin)."),
        ],
        "scripts/parity-probes/clone-vlmshots-v125.sh": [
            ("# v113-era pair (the re-run cadence's rotation — the pair's NINTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v125]): the DASHBOARD at desktop 1280x800\n# FULL-PAGE (the Budget Guidelines card + the quick-action row — the two\n# v61-era surfaces, re-proved again by the v125 re-run after v101-v113). Runs",
             "# v119-era pair (the re-run cadence's rotation — the pair's TENTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125]): the DASHBOARD at desktop 1280x800\n# FULL-PAGE (the Budget Guidelines card + the quick-action row — the two\n# v61-era surfaces, re-proved again by the v125 re-run after v101-v119). Runs"),
        ],
        "scripts/parity-probes/vlm-compare-v125.mjs": [
            ("(v125, the v113-era pair NINTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v125] — the FORTY-SECOND consecutive queue/ledger",
             "(v125, the v119-era pair TENTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125] — the FORTY-EIGHTH consecutive queue/ledger"),
            ("the v125 NINTH re-run of the v113-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v125]) =====",
             "the v125 TENTH re-run of the v119-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125]) ====="),
        ],
        "scripts/parity-probes/arbit-v125.sh": [
            ("# 1280x800 (the v113-era pair's NINTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v125]\n# — the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET\n# GUIDELINES card + the QUICK-ACTION row, last re-shot v113). The v113\n# verdict was IDENTICAL with ZERO style flags; per the v75 convention the",
             "# 1280x800 (the v119-era pair's TENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125]\n# — the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET\n# GUIDELINES card + the QUICK-ACTION row, last re-shot v119). The v119\n# verdict was IDENTICAL with ZERO style flags; per the v75 convention the",),
            ("# censuses are the v61/v83 qa-census axes re-measured (a drift re-check\n# since v113):",
             "# censuses are the v61/v83 qa-census axes re-measured (a drift re-check\n# since v119):"),
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
    # (→ v101 → v107 → v113 → v119 → v125), the corrected state tokens
    # (re-shot v119, v119-era, the corrected oldest list [v119 < v120),
    # the corrected re-proves window v101-v119, the corrected drift-re-check
    # since v119 + the verdict reference "The v119", the pin/axes provenance
    # (the v61 F3 pin, the v107 F4 label-leaf pin), the rule/lesson
    # references (v43 misattribution lesson, v45 F3 pin, v46 rule, v51 F4
    # pin, v44 hero/stat pins, v61 STRETCH-fix, v61/v83 qa-census, v64 rule,
    # v66 discipline, v73 heredoc lesson, v75 convention, v75 login-retry),
    # and the v77 mechanism class.
    LEGIT = (
        "→ v101 → v107 → v113 → v119 → v125", "re-shot v119", "v119-era",
        "v119 < v120", "v101-v119", "since v119", "The v119",
        "v61 F3", "v107 F4", "v43 misattribution", "v45 F3", "v46 ",
        "v46 rule", "v51 F4", "v44 hero", "v61 STRETCH", "v61/v83",
        "v64 rule", "v66 discipline", "v73 heredoc", "v75 convention",
        "v75 login-retry", "v77 mechanism",
    )
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v113-era|re-shot v113|NINTH re-run|FORTY-SECOND|v113 < v114|refvlm119|clonevlm119|refar119|clonear119|/tmp/vlm119|v101-v113|since v113|refvlm125 NINTH",
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
