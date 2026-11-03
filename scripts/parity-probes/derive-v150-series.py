#!/usr/bin/env python3
"""Derive the v150 probe series from the v144 lineage (the MOBILE-TWINS
pair — BOTH mobile 390x844 full-page twins: the /NETWORTH view + the
DASHBOARD — the pair's FOURTEENTH re-run
[v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138 → v144 → v150]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention): the
v149-era docs' v150 queue names "the v144-era MOBILE-TWINS pair — the
/networth view + the DASHBOARD, both FULL-PAGE at mobile 390x844, last
re-shot v144 — now the oldest remaining [v144]; the pair's FOURTEENTH
re-run bracket [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 ->
v108 -> v114 -> v120 -> v126 -> v132 -> v138 -> v144 -> v150] to be
verified against the v144 lineage's own records" — verified against the
v144 lineage BEFORE this derivation: the v144 plan's own header reads
"the v138-era MOBILE-TWINS pair's THIRTEENTH re-run [v62/v63 → v69 →
v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 →
v138 → v144]" — the THIRTEENTH ordinal on the 14-entry bracket
[v62/v63 the original pair, one entry — 14 entries − the original =
13 re-runs], CONSISTENT (no off-by-one this lineage); the v144 shots
header carries the FULL bracket form. v150 = the FOURTEENTH re-run by
appending v150 to that bracket. The SEVENTY-THIRD consecutive
queue/ledger agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm144->refvlm150, clonevlm144->clonevlm150,
     refarbit144->refarbit150, clonearbit144->clonearbit150 (the FOUR
     EXPLICIT session-token swaps — the arbit tokens carry '144' without
     the 'v' prefix... NOTE the mobile-twins lineage uses the LONG
     'refarbitNNN' token form, so the bare version swap cannot touch
     them; the v121-cycle stale-session-fix precedent), /tmp/vlm144->/tmp/vlm150,
     v144->v150
  2. History corrections (the plan pointer "the v143 plan's own
     suggestion" -> "the v149 plan's", the era marker last-re-shot v138 ->
     v144 + the oldest-remaining list [v138] -> [v144] — the rotation
     backlog, a within-line edit preserving the line count), the re-run
     ordinal THIRTEENTH -> FOURTEENTH + the re-run bracket extended
     [-> v126 -> v132 -> v138 -> v150] -> [-> v126 -> v132 -> v138 ->
     v144 -> v150] in the three corrected files, the verdicts window
     "the v84/v90/v96/v102/v108/v138 re-runs" -> "…v108/v144 re-runs", the
     arbit census-axes provenance "The v138 census axes" -> "The v144
     census axes".
     NOTE: the clone file needs none — verified: zero era tokens (the
     v132/v138/v144 derivations' own finding, re-verified by the
     pre-derivation sweep).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit or a same-line-count block swap; the line-count report
must show OK on all four files).
"""
import re
import subprocess
import sys

FILES = {
    "scripts/parity-probes/vlm-shots-v144.sh": "scripts/parity-probes/vlm-shots-v150.sh",
    "scripts/parity-probes/clone-vlmshots-v144.sh": "scripts/parity-probes/clone-vlmshots-v150.sh",
    "scripts/parity-probes/vlm-compare-v144.mjs": "scripts/parity-probes/vlm-compare-v150.mjs",
    "scripts/parity-probes/arbit-v144.sh": "scripts/parity-probes/arbit-v150.sh",
}

GENERIC = [
    ("refvlm144", "refvlm150"),
    ("clonevlm144", "clonevlm150"),
    ("refarbit144", "refarbit150"),
    ("clonearbit144", "clonearbit150"),
    ("/tmp/vlm144", "/tmp/vlm150"),
    ("v144", "v150"),
]

# History corrections, per file, written against the POST-generic-swap state.
# The era marker + bracket extension + ordinals, per the v138/v144 derivations'
# own fragment families. Every fragment is a same-line-count block swap
# (line-count-preserved).
CORR = {
    "scripts/parity-probes/vlm-shots-v150.sh": [
        ("# The v150 queue (the v143 plan's own suggestion, now confirmed by the\n"
         "# rotation ledger: the twins last re-shot v138 — now the oldest remaining\n"
         "# [v138]; the pair's THIRTEENTH re-run\n"
         "# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138 → v150]). READ-ONLY: login + passive",
         "# The v150 queue (the v149 plan's own suggestion, now confirmed by the\n"
         "# rotation ledger: the twins last re-shot v144 — now the oldest remaining\n"
         "# [v144]; the pair's FOURTEENTH re-run\n"
         "# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138 → v144 → v150]). READ-ONLY: login + passive"),
    ],
    "scripts/parity-probes/vlm-compare-v150.mjs": [
        ("// twins last re-shot v138 — now the oldest remaining candidate [v138];\n"
         "// the pair's THIRTEENTH re-run [v62/v63 → v69 →\n"
         "// v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138 → v150]) and (2) the DASHBOARD (the v62-era mobile twin's",
         "// twins last re-shot v144 — now the oldest remaining candidate [v144];\n"
         "// the pair's FOURTEENTH re-run [v62/v63 → v69 →\n"
         "// v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138 → v144 → v150]) and (2) the DASHBOARD (the v62-era mobile twin's"),
        ("// pin families (dashboard); the v84/v90/v96/v102/v108/v138 re-runs' own verdicts were DIFFERENT",
         "// pin families (dashboard); the v84/v90/v96/v102/v108/v144 re-runs' own verdicts were DIFFERENT"),
    ],
    "scripts/parity-probes/arbit-v150.sh": [
        ("# the drift state and measures the pin's axes). The v138 census axes,\n"
         "# re-measured on BOTH sides at mobile 390 (the pair's THIRTEENTH re-run\n"
         "# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138 → v150]):",
         "# the drift state and measures the pin's axes). The v144 census axes,\n"
         "# re-measured on BOTH sides at mobile 390 (the pair's FOURTEENTH re-run\n"
         "# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138 → v144 → v150]):"),
        ("#   NETWORTH (the v63-era classes, re-confirmed live by the v84/v90/v96/v102/v108/v138 re-runs):",
         "#   NETWORTH (the v63-era classes, re-confirmed live by the v84/v90/v96/v102/v108/v144 re-runs):"),
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

    # the clone file: verify zero corrections were needed (zero era tokens
    # beyond the generic) — the v132/v138/v144 derivations' own finding
    clone_text = open("scripts/parity-probes/clone-vlmshots-v150.sh", encoding="utf-8").read()
    clone_res = re.findall(r"v138|v132|v126|v143|THIRTEENTH|FOURTEENTH", clone_text)
    if clone_res:
        print(f"NOTE: clone-vlmshots-v150.sh carries era tokens: {sorted(set(clone_res))} (review)")
    else:
        print("clone-vlmshots-v150.sh: zero era tokens — no corrections needed (verified)")

    if not ok:
        sys.exit(1)

    # residual old-token scan (era tokens + ordinals + the old version)
    print("\n--- residual scan ---")
    residual_re = re.compile(
        r"vlm144|refarbit144|clonearbit144|"
        r"THIRTEENTH|"
        r"last re-shot v138|\[v138\]|"
        r"→ v138 → v150\]|"
        r"the v138 census|v108/v138 re-runs|"
        r"the v143 plan's"
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
    print("\nv150 series derived clean (4/4 first run)")


if __name__ == "__main__":
    main()
