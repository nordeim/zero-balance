#!/usr/bin/env python3
"""Derive compare-v122-census.py from compare-v116-census.py (the
savings-view axis-by-axis comparator — the same QUADS/AXES/ASYMMETRIC_DOC
whitelists, the v116 census values now the standing classes the v122
census must reproduce EXACTLY).
Generic swap FIRST (v116 -> v122), then the census-era corrections (the
provenance citations re-pointed from the v104/v110 measurements to the
v116 measurement — the immediately-previous census, the v121 comparator's
own precedent: its v115 form cites the v109 census, the v121 form the
v115). Verified by normalize-back diff; line-count-preserving."""
import sys

SRC = "scripts/parity-probes/compare-v116-census.py"
DST = "scripts/parity-probes/compare-v122-census.py"

SWAPS = [
    # generic version swap FIRST (v116 tokens -> v122, incl. the log paths)
    ("v116", "v122"),
    # census-era corrections (the provenance citations — within-line forms)
    ("the v104/v110 census values,", "the v116 census values,"),
    ("— the v104/v110", "— the v116"),
    ("# v104/v110 values EXACTLY", "# v116 values EXACTLY"),
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
residual = re.findall(r"v104/v110|arbit-v116", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
