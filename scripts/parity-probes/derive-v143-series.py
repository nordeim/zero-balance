#!/usr/bin/env python3
"""Derive the v143 probe series from the v137 lineage (the DASHBOARD at
desktop 1280x800 FULL-PAGE — the v125-era dashboard pair's THIRTEENTH re-run
[v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention): the
v142-era docs' v143 queue names "the v137-era DASHBOARD pair — the
DASHBOARD at desktop 1280x800 FULL-PAGE [the Budget Guidelines card + the
Quick-Action row below the fold], last re-shot v137 — now the oldest
remaining [v137 < v138]; the pair's THIRTEENTH re-run bracket [v61 →
v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 →
v137 → v143] to be verified against the v137 lineage's own records" —
verified against the v137 lineage BEFORE this derivation: the v137 plan's
own header reads "the v131-era DASHBOARD pair's TWELFTH re-run [v61 → v68 →
v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137]"
— the TWELFTH ordinal on the 13-entry bracket [v61 the original — 13
entries − the original = 12 re-runs], consistent, no off-by-one this
lineage; the v137 shots header carries the FULL bracket form. v143 = the
THIRTEENTH re-run by appending v143 to that bracket. The SIXTY-SIXTH
consecutive queue/ledger agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm137->refvlm143, clonevlm137->clonevlm143,
     refar137->refar143, clonear137->clonear143 (the FOUR EXPLICIT
     session-token swaps — the arbit tokens carry '137' without the 'v'
     prefix, so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm137->/tmp/vlm143, v137->v143
  2. History corrections (the era marker v131-era -> v137-era + last re-shot
     v131 -> v137 + the oldest-remaining bracket [v131 < v132] -> [v137 <
     v138] — the rotation backlog, a within-line edit preserving the line
     count), the re-run ordinal TWELFTH -> THIRTEENTH + the re-run bracket
     extended [-> v119 -> v125 -> v131 -> v143] -> [-> v119 -> v125 -> v131
     -> v137 -> v143], the agreement ordinal SIXTIETH -> SIXTY-SIXTH, the
     re-proves chain v101-v131 -> v101-v137, the arbit verdict/census
     provenance (last re-shot + the verdict + the drift-re-check re-pointed
     at the v137 measurement).
     NOTE: the v137 lineage carries NO plan pointer and NO later-pairs list
     (verified by the pre-derivation sweep — all era tokens confined to the
     file headers, the sole in-body exception the compare script's own
     PAIR console.log line, corrected below).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import re
import subprocess
import sys

FILES = {
    "scripts/parity-probes/vlm-shots-v137.sh": "scripts/parity-probes/vlm-shots-v143.sh",
    "scripts/parity-probes/clone-vlmshots-v137.sh": "scripts/parity-probes/clone-vlmshots-v143.sh",
    "scripts/parity-probes/vlm-compare-v137.mjs": "scripts/parity-probes/vlm-compare-v143.mjs",
    "scripts/parity-probes/arbit-v137.sh": "scripts/parity-probes/arbit-v143.sh",
}

GENERIC = [
    ("refvlm137", "refvlm143"),
    ("clonevlm137", "clonevlm143"),
    ("refar137", "refar143"),
    ("clonear137", "clonear143"),
    ("/tmp/vlm137", "/tmp/vlm143"),
    ("v137", "v143"),
]

# History corrections, per file, written against the POST-generic-swap state.
# The era marker + bracket extension + ordinals, per the v136/v142 derivation's
# own fragment families. Every fragment is a within-line edit (line-count-preserved).
CORR = {
    "scripts/parity-probes/vlm-shots-v143.sh": [
        ("# v131-era pair (the re-run cadence's rotation — the oldest remaining standing\n"
         "# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v131 — now\n"
         "# the oldest remaining [v131 < v132]; the pair's TWELFTH\n"
         "# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v143] — the SIXTIETH consecutive",
         "# v137-era pair (the re-run cadence's rotation — the oldest remaining standing\n"
         "# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v137 — now\n"
         "# the oldest remaining [v137 < v138]; the pair's THIRTEENTH\n"
         "# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143] — the SIXTY-SIXTH consecutive"),
        ("# unpaired before v61]. The v143 re-run re-proves the v61-era surfaces after\n"
         "# v101-v131 (the mobile twins, the height pins, the stat-card divider pin).",
         "# unpaired before v61]. The v143 re-run re-proves the v61-era surfaces after\n"
         "# v101-v137 (the mobile twins, the height pins, the stat-card divider pin)."),
    ],
    "scripts/parity-probes/clone-vlmshots-v143.sh": [
        ("# v131-era pair (the re-run cadence's rotation — the pair's TWELFTH re-run\n"
         "# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v143]): the DASHBOARD at desktop 1280x800",
         "# v137-era pair (the re-run cadence's rotation — the pair's THIRTEENTH re-run\n"
         "# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143]): the DASHBOARD at desktop 1280x800"),
        ("# v61-era surfaces, re-proved again by the v143 re-run after v101-v131). Runs",
         "# v61-era surfaces, re-proved again by the v143 re-run after v101-v137). Runs"),
    ],
    "scripts/parity-probes/vlm-compare-v143.mjs": [
        ("// vlm-compare-v143.mjs — the standing VLM pairwise RE-RUN (v143, the v131-era pair TWELFTH re-run\n"
         "// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v143] — the SIXTIETH consecutive queue/ledger",
         "// vlm-compare-v143.mjs — the standing VLM pairwise RE-RUN (v143, the v137-era pair THIRTEENTH re-run\n"
         "// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143] — the SIXTY-SIXTH consecutive queue/ledger"),
        ("the v143 TWELFTH re-run of the v131-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v143]",
         "the v143 THIRTEENTH re-run of the v137-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143]"),
    ],
    "scripts/parity-probes/arbit-v143.sh": [
        ("# 1280x800 (the v131-era pair's TWELFTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v143]",
         "# 1280x800 (the v137-era pair's THIRTEENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143]"),
        ("# GUIDELINES card + the QUICK-ACTION row, last re-shot v131). The v131\n"
         "# verdict was IDENTICAL with ZERO style flags; per the v75 convention the",
         "# GUIDELINES card + the QUICK-ACTION row, last re-shot v137). The v137\n"
         "# verdict was IDENTICAL with ZERO style flags; per the v75 convention the"),
        ("# censuses are the v61/v83 qa-census axes re-measured (a drift re-check\n# since v131):",
         "# censuses are the v61/v83 qa-census axes re-measured (a drift re-check\n# since v137):"),
    ],
}


def main():
    ok = True
    for src, dst in FILES.items():
        text = open(src, encoding="utf-8").read()
        for old, new in GENERIC:
            text = text.replace(old, new)
        open(dst, "w", encoding="utf-8").write(text)
        print(f"derived {dst} (generic swaps applied)")

    print("\n--- history corrections (against the POST-swap state) ---")
    for dst, frags in CORR.items():
        text = open(dst, encoding="utf-8").read()
        for old, new in frags:
            if old not in text:
                print(f"FAIL: fragment not found in {dst}:\n  {old[:100]}...")
                ok = False
                continue
            if text.count(old) != 1:
                print(f"FAIL: fragment not unique ({text.count(old)}x) in {dst}:\n  {old[:100]}...")
                ok = False
                continue
            text = text.replace(old, new)
        open(dst, "w", encoding="utf-8").write(text)
        print(f"corrected {dst} ({len(frags)} fragments)")

    if not ok:
        sys.exit(1)

    # residual old-token scan (era tokens + ordinals + the old version)
    print("\n--- residual scan ---")
    residual_re = re.compile(
        r"refvlm137|clonevlm137|refar137|clonear137|"
        r"TWELFTH|SIXTIETH|"
        r"v101-v131|last re-shot v131|\[v131 < v132|"
        r"→ v131 → v143\]|→ v125 → v143\]|"
        r"v131-era pair|v131-era DASHBOARD"
    )
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        residual = residual_re.findall(text)
        if residual:
            print(f"FAIL: {dst} retains old tokens: {sorted(set(residual))}")
            ok = False
        else:
            print(f"OK: {dst} zero residual")

    # line-count preservation (within-line edits only)
    print("\n--- line-count preservation ---")
    for src, dst in FILES.items():
        src_n = len(open(src, encoding="utf-8").read().splitlines())
        dst_n = len(open(dst, encoding="utf-8").read().splitlines())
        status = "OK" if src_n == dst_n else "FAIL"
        if src_n != dst_n:
            ok = False
        print(f"{status}: {dst} {dst_n} lines (source {src} {src_n})")

    # syntax gates: bash -n on the .sh files, node --check on the .mjs
    print("\n--- syntax gates ---")
    for dst in FILES.values():
        if dst.endswith(".sh"):
            r = subprocess.run(["bash", "-n", dst], capture_output=True, text=True)
        else:
            r = subprocess.run(["node", "--check", dst], capture_output=True, text=True)
        if r.returncode != 0:
            print(f"FAIL: {dst}: {r.stderr}")
            ok = False
        else:
            print(f"OK: {dst} syntax clean")

    if not ok:
        sys.exit(1)
    print("\nv143 series derived clean (4/4 first run)")


if __name__ == "__main__":
    main()
