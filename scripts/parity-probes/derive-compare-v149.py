#!/usr/bin/env python3
"""Derive compare-v149-census.py from compare-v143-census.py (the
dashboard full-page below-the-fold axis-by-axis comparator — the same
documented-class whitelists, the v143 census values now the standing
classes the v149 census must reproduce EXACTLY).
Generic swap FIRST (v143 -> v149), then the census-era corrections (the
provenance citations re-pointed from the v137 measurement to the v143
measurement — the immediately-previous census, the v136/v142/v143
comparators' own precedent). Verified by normalize-back diff;
line-count-preserving."""
import sys

SRC = "scripts/parity-probes/compare-v143-census.py"
DST = "scripts/parity-probes/compare-v149-census.py"

SWAPS = [
    # generic version swap FIRST (v143 tokens -> v149, incl. the log paths;
    # NOTE /tmp/vlm143 carries no 'v143' substring — the v-prefix-less path
    # needs its own explicit swap, the same specific-first rule the series
    # derivation's GENERIC list follows)
    ("/tmp/vlm143", "/tmp/vlm149"),
    ("v143", "v149"),
    # census-era corrections (the provenance citations — within-line forms)
    ("the v137-era DASHBOARD pair's THIRTEENTH re-run",
     "the v143-era DASHBOARD pair's FOURTEENTH re-run"),
    ("must reproduce the v137 census values EXACTLY (a drift re-check since v137)",
     "must reproduce the v143 census values EXACTLY (a drift re-check since v143)"),
    # the bracket extension (the post-swap trailing '-> v149]' form)
    ("[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125 -> v131 -> v137 -> v149]",
     "[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125 -> v131 -> v137 -> v143 -> v149]"),
    ("the v137-documented standing classes\n# (the v149 census must reproduce the v137 values EXACTLY)",
     "the v143-documented standing classes\n# (the v149 census must reproduce the v143 values EXACTLY)"),
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
residual = re.findall(r"v137-era|THIRTEENTH re-run|since v137|v137 census values|v137-documented|v125 -> v131 -> v137 -> v149\]|arbit-v143|vlm143", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
