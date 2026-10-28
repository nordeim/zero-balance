#!/usr/bin/env python3
"""Derive compare-v131-census.py from compare-v125-census.py (the
dashboard guidelines + quick-action axis-by-axis comparator — the same
documented-class whitelists, the v125 census values now the standing
classes the v131 census must reproduce EXACTLY).
Generic swap FIRST (/tmp/vlm125 -> /tmp/vlm131 explicit, then v125 ->
v131), then the census-era corrections (the provenance citations
re-pointed from the v119 measurement to the v125 measurement — the
immediately-previous census, the v130 comparator's own precedent: its
v124 form cites the v118/v124 measurements). Verified by normalize-back
diff; line-count-preserving."""
import sys

SRC = "scripts/parity-probes/compare-v125-census.py"
DST = "scripts/parity-probes/compare-v131-census.py"

SWAPS = [
    # generic version swap FIRST (v125 tokens -> v131, incl. the log paths;
    # NOTE /tmp/vlm125 carries no 'v125' substring — the v-prefix-less path
    # needs its own explicit swap, the same specific-first rule the series
    # derivation's GENERIC list follows)
    ("/tmp/vlm125", "/tmp/vlm131"),
    ("v125", "v131"),
    # census-era corrections (the provenance citations — within-line forms)
    ("The v131 re-run (the v119-era DASHBOARD pair's TENTH re-run\n[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v131])\nmust reproduce the v119 census values EXACTLY (a drift re-check since v119).",
     "The v131 re-run (the v125-era DASHBOARD pair's ELEVENTH re-run\n[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125 -> v131])\nmust reproduce the v125 census values EXACTLY (a drift re-check since v125)."),
    ("# All delta families below are the v119-documented standing classes\n# (the v131 census must reproduce the v119 values EXACTLY):",
     "# All delta families below are the v125-documented standing classes\n# (the v131 census must reproduce the v125 values EXACTLY):"),
]

text = open(SRC, encoding="utf-8").read()
missing = []
for old, new in SWAPS:
    if old not in text:
        missing.append(old)
    text = text.replace(old, new)
if missing:
    print("MISSING SOURCES:", missing)
    sys.exit(1)

# normalize back and prove swap-only
back = text
for old, new in reversed(SWAPS):
    back = back.replace(new, old)
original = open(SRC, encoding="utf-8").read()
if back != original:
    print("FAIL: not a pure token swap (normalize-back mismatch)")
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)

import re
residual = re.findall(r"v119-era|TENTH re-run|the v119 census|since v119|v119-documented|the v119 values|arbit-v125|vlm125", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)
# bare-v119 sweep: the corrected bracket is the sole legitimate survivor
for m in re.finditer(r"v119", text):
    ctx = text[max(0, m.start() - 60):m.end() + 60]
    if "-> v119 -> v125 -> v131" in ctx:
        continue
    print(f"FAIL: {DST} retains v119 outside the corrected bracket")
    sys.exit(1)

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
