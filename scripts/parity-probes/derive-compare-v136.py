#!/usr/bin/env python3
"""Derive compare-v136-census.py from compare-v130-census.py (the
networth + drill-down axis-by-axis comparator — the same documented-class
whitelists, the v130 census values now the standing classes the v136
census must reproduce EXACTLY).
Generic swap FIRST (v130 -> v136), then the census-era corrections (the
provenance citations re-pointed from the v124 measurement to the v130
measurement — the immediately-previous census, the v130 comparator's
own precedent: its v124 form cites the v118/v124 censuses, the v136
form the v124/v130). Verified by normalize-back diff; line-count-
preserving."""
import sys

SRC = "scripts/parity-probes/compare-v130-census.py"
DST = "scripts/parity-probes/compare-v136-census.py"

SWAPS = [
    # generic version swap FIRST (v130 tokens -> v136, incl. the log paths;
    # NOTE /tmp/vlm130 carries no 'v130' substring — the v-prefix-less path
    # needs its own explicit swap, the same specific-first rule the series
    # derivation's GENERIC list follows)
    ("/tmp/vlm130", "/tmp/vlm136"),
    ("v130", "v136"),
    # census-era corrections (the provenance citations — within-line forms)
    ("the v124-era NETWORTH + DRILL-DOWN pair's ELEVENTH re-run",
     "the v130-era NETWORTH + DRILL-DOWN pair's TWELFTH re-run"),
    ("the v118/v124 records", "the v124/v130 records"),
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
residual = re.findall(r"v124-era|ELEVENTH re-run|v118/v124|arbit-v130|vlm130", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
