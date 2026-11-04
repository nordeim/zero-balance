#!/usr/bin/env python3
"""Derive compare-v151-census.py from compare-v145-census.py (the
axis-by-axis both-sides census comparator for the v151 ITEMS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v145 -> v151 swap (carries the half-log
     paths /tmp/ref-arbit-v151.log + /tmp/clone-arbit-v151.log).
  2. History corrections against the POST-swap state: the provenance
     citations re-pointed at the v145 measurement (the v151 census must
     reproduce the v145 census values EXACTLY, a drift re-check since
     v145; the v145-documented standing classes).
"""
import sys

SRC = "scripts/parity-probes/compare-v145-census.py"
DST = "scripts/parity-probes/compare-v151-census.py"

GENERIC = [
    ("v145", "v151"),
]

CORRECTIONS = [
    # docstring: the whitelist provenance citation
    ('''every leaf axis. Known documented classes are whitelisted (the v139
census values, reproduced exactly):''',
     '''every leaf axis. Known documented classes are whitelisted (the v145
census values, reproduced exactly):'''),
    # the QUADS whitelist comment's provenance citation
    ('''# v139-documented standing classes (the v151 census must reproduce the
# v139 values EXACTLY).''',
     '''# v145-documented standing classes (the v151 census must reproduce the
# v145 values EXACTLY).'''),
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
# their new fragments carry v151 tokens produced by the generic swap, so
# the generic reverse must run LAST or it corrupts them)
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
residual = re.findall(r"v145|ref-arbit-v145|clone-arbit-v145|/tmp/vlm145", text)
# the corrected provenance citations legitimately mention v145 (the
# era marker 'the v145 census values' + 'v145-documented standing classes')
legit = text.count("v145")
explained = sum(text.count(s) for s in ("the v145\ncensus values", "v145-documented", "the v145 census", "v145 values"))
if residual and len(residual) != explained:
    print(f"FAIL: {DST} retains unexplained old tokens: {sorted(set(residual))} (total {len(residual)}, explained {explained})")
    sys.exit(1)

print(f"derived {DST} (generic swap + provenance corrections; normalize-back clean)")
