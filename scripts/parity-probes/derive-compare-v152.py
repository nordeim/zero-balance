#!/usr/bin/env python3
"""Derive compare-v152-census.py from compare-v146-census.py (the
axis-by-axis both-sides census comparator for the v152 SAVINGS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v146 -> v152 swap (carries the half-log
     paths /tmp/ref-arbit-v152.log + /tmp/clone-arbit-v152.log).
  2. History corrections against the POST-swap state: the provenance
     citations re-pointed at the v146 measurement (the v152 census must
     reproduce the v146 census values EXACTLY, a drift re-check since
     v146; the v146-documented standing classes).
"""
import sys

SRC = "scripts/parity-probes/compare-v146-census.py"
DST = "scripts/parity-probes/compare-v152-census.py"

GENERIC = [
    ("v146", "v152"),
]

CORRECTIONS = [
    # docstring: the whitelist provenance citation
    ('''axis. Known documented classes are whitelisted (the v140 census values,
reproduced exactly):''',
     '''axis. Known documented classes are whitelisted (the v146 census values,
reproduced exactly):'''),
    # the QUADS whitelist comment's provenance citations
    ('''# EXACT-QUAD whitelist: (axis, ref value, clone value) — the v140
# documented standing classes (the v152 census must reproduce the
# v140 values EXACTLY).''',
     '''# EXACT-QUAD whitelist: (axis, ref value, clone value) — the v146
# documented standing classes (the v152 census must reproduce the
# v146 values EXACTLY).'''),
]

text = open(SRC, encoding="utf-8").read()
missing = []
for old, new in GENERIC:
    if old not in text:
        missing.append(old)
    text = text.replace(old, new)

for old, new in CORRECTIONS:
    if old not in text:
        missing.append(old[:60])
        continue
    text = text.replace(old, new)
    print(f"applied correction: {old[:52]!r} -> corrected")

if missing:
    print("MISSING SOURCES:", missing)
    sys.exit(1)

# normalize back and prove swap-only (the CORRECTIONS reversed FIRST —
# their new fragments carry v146 tokens that the generic reverse must
# not corrupt; the generic reverse runs LAST)
back = text
for old, new in reversed(CORRECTIONS):
    back = back.replace(new, old)
for old, new in reversed(GENERIC):
    back = back.replace(new, old)
original = open(SRC, encoding="utf-8").read()
if back != original:
    print("FAIL: not a pure token swap (normalize-back mismatch)")
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)

import re
residual = re.findall(r"v140", text)
# after the corrections NO v140 token may survive (both citations re-pointed
# at the v146 measurement)
if residual:
    print(f"FAIL: {DST} retains unexplained old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"derived {DST} (generic swap + provenance corrections; normalize-back clean)")
