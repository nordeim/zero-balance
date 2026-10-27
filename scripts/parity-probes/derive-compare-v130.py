#!/usr/bin/env python3
"""Derive compare-v130-census.py from compare-v124-census.py (the
networth + drill-down axis-by-axis comparator — the same documented-class
whitelists, the v124 census values now the standing classes the v130
census must reproduce EXACTLY).
Generic swap FIRST (v124 -> v130), then the census-era corrections (the
provenance citations re-pointed from the v118 measurement to the v124
measurement — the immediately-previous census, the v129 comparator's
own precedent: its v123 form cites the v105/v111/v117/v123 censuses, the
v130 form the v118/v124). Verified by normalize-back diff; line-count-
preserving."""
import sys

SRC = "scripts/parity-probes/compare-v124-census.py"
DST = "scripts/parity-probes/compare-v130-census.py"

SWAPS = [
    # generic version swap FIRST (v124 tokens -> v130, incl. the log paths;
    # NOTE /tmp/vlm124 carries no 'v124' substring — the v-prefix-less path
    # needs its own explicit swap, the same specific-first rule the series
    # derivation's GENERIC list follows)
    ("/tmp/vlm124", "/tmp/vlm130"),
    ("v124", "v130"),
    # census-era corrections (the provenance citations — within-line forms)
    ("the v118-era NETWORTH + DRILL-DOWN pair's TENTH re-run",
     "the v124-era NETWORTH + DRILL-DOWN pair's ELEVENTH re-run"),
    ("the v112/v118 records", "the v118/v124 records"),
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
residual = re.findall(r"v118-era|TENTH re-run|v112/v118|arbit-v124|vlm124", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
