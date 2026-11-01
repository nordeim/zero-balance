#!/usr/bin/env python3
"""Derive the v138 probe series from the v132 lineage (the MOBILE-TWINS
pair — BOTH mobile 390x844 full-page twins: the /NETWORTH view + the
DASHBOARD — the pair's TWELFTH re-run
[v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention): the
v137-era docs' v138 queue names "the v132-era MOBILE-TWINS pair — the
/NETWORTH view + the DASHBOARD, both FULL-PAGE at mobile 390x844, last
re-shot v132 — now the oldest remaining [v132]; the pair's TWELFTH re-run
bracket [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 →
v120 → v126 → v132 → v138] to be verified against the v132 lineage's own
records" — verified against the v132 lineage BEFORE this derivation: the
v132 plan's own header reads "the v126-era MOBILE 390x844 full-page TWINS
pair's ELEVENTH re-run [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 →
v108 → v114 → v120 → v126 → v132]" — the ELEVENTH ordinal on the 12-entry
bracket [v62/v63 the original pair, one entry — 12 entries − the original
= 11 re-runs], CONSISTENT (no off-by-one this lineage); the v132 shots
header carries the FULL bracket form. v138 = the TWELFTH re-run by
appending v138 to that bracket. The SIXTY-FIRST consecutive queue/ledger
agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm132->refvlm138, clonevlm132->clonevlm138,
     refarbit132->refarbit138, clonearbit132->clonearbit138 (the FOUR
     EXPLICIT session-token swaps — the arbit tokens carry '132' without
     the 'v' prefix, so the bare version swap cannot touch them; the
     v121-cycle stale-session-fix precedent), /tmp/vlm132->/tmp/vlm138,
     v132->v138
  2. History corrections (the plan pointer "the v131 plan's own
     suggestion" -> "the v137 plan's", the era marker last-re-shot v126 ->
     v132 + the oldest-remaining list [v126 < v127 < v128 < v129 < v130 <
     v131] -> [v132] — the rotation backlog, a within-line edit preserving
     the line count), the re-run ordinal ELEVENTH -> TWELFTH + the re-run
     bracket extended [-> v120 -> v126 -> v138] -> [-> v120 -> v126 ->
     v132 -> v138] in the three corrected files, the verdicts window
     "the v84/v90/v96/v102/v108/v126 re-runs" -> "…v108/v132 re-runs", the
     arbit census-axes provenance "The v126 census axes" -> "The v132
     census axes".
     NOTE: the clone file needs none — verified: zero era tokens (the
     v132 derivation's own finding, re-verified by the pre-derivation
     sweep).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit or a same-line-count block swap; the line-count report
must show OK on all four files).
"""
import re
import subprocess
import sys

FILES = {
    "scripts/parity-probes/vlm-shots-v132.sh": "scripts/parity-probes/vlm-shots-v138.sh",
    "scripts/parity-probes/clone-vlmshots-v132.sh": "scripts/parity-probes/clone-vlmshots-v138.sh",
    "scripts/parity-probes/vlm-compare-v132.mjs": "scripts/parity-probes/vlm-compare-v138.mjs",
    "scripts/parity-probes/arbit-v132.sh": "scripts/parity-probes/arbit-v138.sh",
}

GENERIC = [
    ("refvlm132", "refvlm138"),
    ("clonevlm132", "clonevlm138"),
    ("refarbit132", "refarbit138"),
    ("clonearbit132", "clonearbit138"),
    ("/tmp/vlm132", "/tmp/vlm138"),
    ("v132", "v138"),
]

# History corrections, per file, written against the POST-generic-swap state.
# The era marker + bracket extension + ordinals, per the v137 derivation's own
# fragment families. Every fragment is a same-line-count block swap
# (line-count-preserved).
CORR = {
    "scripts/parity-probes/vlm-shots-v138.sh": [
        ("# The v138 queue (the v131 plan's own suggestion, now confirmed by the\n"
         "# rotation ledger: the twins last re-shot v126 = the oldest remaining\n"
         "# [v126 < v127 < v128 < v129 < v130 < v131]; the pair's ELEVENTH re-run\n"
         "# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v138]). READ-ONLY: login + passive",
         "# The v138 queue (the v137 plan's own suggestion, now confirmed by the\n"
         "# rotation ledger: the twins last re-shot v132 — now the oldest remaining\n"
         "# [v132]; the pair's TWELFTH re-run\n"
         "# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138]). READ-ONLY: login + passive"),
    ],
    "scripts/parity-probes/vlm-compare-v138.mjs": [
        ("// twins last re-shot v126 = the oldest remaining candidate [v126 < v127 <\n"
         "// v128 < v129 < v130 < v131]; the pair's ELEVENTH re-run [v62/v63 → v69 →\n"
         "// v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v138]) and (2) the DASHBOARD (the v62-era mobile twin's",
         "// twins last re-shot v132 — now the oldest remaining candidate [v132];\n"
         "// the pair's TWELFTH re-run [v62/v63 → v69 →\n"
         "// v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138]) and (2) the DASHBOARD (the v62-era mobile twin's"),
        ("// pin families (dashboard); the v84/v90/v96/v102/v108/v126 re-runs' own verdicts were DIFFERENT",
         "// pin families (dashboard); the v84/v90/v96/v102/v108/v132 re-runs' own verdicts were DIFFERENT"),
    ],
    "scripts/parity-probes/arbit-v138.sh": [
        ("# the drift state and measures the pin's axes). The v126 census axes,\n"
         "# re-measured on BOTH sides at mobile 390 (the pair's ELEVENTH re-run\n"
         "# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v138]):",
         "# the drift state and measures the pin's axes). The v132 census axes,\n"
         "# re-measured on BOTH sides at mobile 390 (the pair's TWELFTH re-run\n"
         "# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102 → v108 → v114 → v120 → v126 → v132 → v138]):"),
        ("#   NETWORTH (the v63-era classes, re-confirmed live by the v84/v90/v96/v102/v108/v126 re-runs):",
         "#   NETWORTH (the v63-era classes, re-confirmed live by the v84/v90/v96/v102/v108/v132 re-runs):"),
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
    # beyond the generic) — the v132 derivation's own finding
    clone_text = open("scripts/parity-probes/clone-vlmshots-v138.sh", encoding="utf-8").read()
    clone_res = re.findall(r"v126|v127|v128|v129|v130|v131|ELEVENTH|TWELFTH", clone_text)
    if clone_res:
        print(f"NOTE: clone-vlmshots-v138.sh carries era tokens: {sorted(set(clone_res))} (review)")
    else:
        print("clone-vlmshots-v138.sh: zero era tokens — no corrections needed (verified)")

    if not ok:
        sys.exit(1)

    # residual old-token scan (era tokens + ordinals + the old version)
    print("\n--- residual scan ---")
    residual_re = re.compile(
        r"vlm132|refarbit132|clonearbit132|"
        r"ELEVENTH|"
        r"last re-shot v126|\[v126 < v127|"
        r"→ v126 → v138\]|"
        r"the v126 census|v108/v126 re-runs|"
        r"the v131 plan's"
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
    print("\nv138 series derived clean (4/4 first run)")


if __name__ == "__main__":
    main()
