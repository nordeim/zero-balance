#!/usr/bin/env python3
"""Derive compare-v148-census.py from compare-v142-census.py (the
networth + drill-down axis-by-axis comparator — the same documented-class
whitelists, the v142 census values now the standing classes the v148
census must reproduce EXACTLY).
Generic swap FIRST (v142 -> v148), then the census-era corrections (the
provenance citations re-pointed from the v136 measurement to the v142
measurement — the immediately-previous census, the v136 comparator's
own precedent: its v130 form cites the v124/v130 censuses, the v142
form the v130/v136, the v148 form the v136/v142). Verified by
normalize-back diff; line-count-preserving."""
import sys

SRC = "scripts/parity-probes/compare-v142-census.py"
DST = "scripts/parity-probes/compare-v148-census.py"

SWAPS = [
    # generic version swap FIRST (v142 tokens -> v148, incl. the log paths;
    # NOTE /tmp/vlm142 carries no 'v142' substring — the v-prefix-less path
    # needs its own explicit swap, the same specific-first rule the series
    # derivation's GENERIC list follows)
    ("/tmp/vlm142", "/tmp/vlm148"),
    ("v142", "v148"),
    # census-era corrections (the provenance citations — within-line forms)
    ("the v136-era NETWORTH + DRILL-DOWN pair's THIRTEENTH re-run",
     "the v142-era NETWORTH + DRILL-DOWN pair's FOURTEENTH re-run"),
    ("the v130/v136 records", "the v136/v142 records"),
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
residual = re.findall(r"v136-era|THIRTEENTH re-run|v130/v136|arbit-v142|vlm142", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
