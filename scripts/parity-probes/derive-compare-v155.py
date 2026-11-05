#!/usr/bin/env python3
"""Derive compare-v155-census.py from compare-v149-census.py (the
dashboard full-page below-the-fold axis-by-axis comparator — the same
documented-class whitelists, the v149 census values now the standing
classes the v155 census must reproduce EXACTLY).
Generic swap FIRST (v149 -> v155), then the census-era corrections (the
provenance citations re-pointed from the v143 measurement to the v149
measurement — the immediately-previous census, the v136/v142/v143/v148
comparators' own precedent). Verified by normalize-back diff;
line-count-preserving."""
import sys

SRC = "scripts/parity-probes/compare-v149-census.py"
DST = "scripts/parity-probes/compare-v155-census.py"

SWAPS = [
    # generic version swap FIRST (v149 tokens -> v155, incl. the log paths;
    # NOTE /tmp/vlm149 carries no 'v149' substring — the v-prefix-less path
    # needs its own explicit swap, the same specific-first rule the series
    # derivation's GENERIC list follows)
    ("/tmp/vlm149", "/tmp/vlm155"),
    ("v149", "v155"),
    # census-era corrections (the provenance citations — within-line forms)
    ("the v143-era DASHBOARD pair's FOURTEENTH re-run",
     "the v149-era DASHBOARD pair's FIFTEENTH re-run"),
    ("must reproduce the v143 census values EXACTLY (a drift re-check since v143)",
     "must reproduce the v149 census values EXACTLY (a drift re-check since v149)"),
    # the bracket extension (the post-swap trailing '-> v155]' form)
    ("[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125 -> v131 -> v137 -> v143 -> v155]",
     "[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125 -> v131 -> v137 -> v143 -> v149 -> v155]"),
    ("the v143-documented standing classes\n# (the v155 census must reproduce the v143 values EXACTLY)",
     "the v149-documented standing classes\n# (the v155 census must reproduce the v149 values EXACTLY)"),
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
residual = re.findall(r"v143-era DASHBOARD pair|FOURTEENTH re-run|since v143|v143 census values|v143-documented|v125 -> v131 -> v137 -> v143 -> v155\]|arbit-v149|vlm149", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
