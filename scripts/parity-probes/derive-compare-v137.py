#!/usr/bin/env python3
"""Derive compare-v137-census.py from compare-v131-census.py (the
DASHBOARD below-the-fold axis-by-axis comparator — the same documented-class
whitelists, the v131 census values now the standing classes the v137
census must reproduce EXACTLY).
Generic swap FIRST (v131 -> v137, incl. the explicit /tmp/vlm131 log-path
swap — the path carries no 'v131' substring, the same specific-first rule
the series derivation follows), then the census-era corrections (the
provenance citations re-pointed from the v125 measurement to the v131
measurement — the immediately-previous census, the v136 comparator's
own precedent: its v130 form cites the v124 measurement, the v137
form the v131). Verified by normalize-back diff; line-count-preserved."""
import re
import sys

SRC = "scripts/parity-probes/compare-v131-census.py"
DST = "scripts/parity-probes/compare-v137-census.py"

SWAPS = [
    # generic version swap FIRST (specific log path BEFORE the bare token)
    ("/tmp/vlm131", "/tmp/vlm137"),
    ("v131", "v137"),
    # census-era corrections (the provenance citations — within-line forms)
    ("the v125-era DASHBOARD pair's ELEVENTH re-run",
     "the v131-era DASHBOARD pair's TWELFTH re-run"),
    ("[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125 -> v137]",
     "[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125 -> v131 -> v137]"),
    ("must reproduce the v125 census values EXACTLY (a drift re-check since v125)",
     "must reproduce the v131 census values EXACTLY (a drift re-check since v131)"),
    ("# All delta families below are the v125-documented standing classes",
     "# All delta families below are the v131-documented standing classes"),
    ("# (the v137 census must reproduce the v125 values EXACTLY):",
     "# (the v137 census must reproduce the v131 values EXACTLY):"),
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

residual = re.findall(r"v125-era|ELEVENTH re-run|v125 census|v125 values|v125-documented|/tmp/vlm131|arbit-v131", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
