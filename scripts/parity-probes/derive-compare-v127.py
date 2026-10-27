#!/usr/bin/env python3
"""Derive compare-v127-census.py from compare-v121-census.py (the
axis-by-axis both-sides census comparator for the v127 ITEMS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v121 -> v127 swap (carries the half-log
     paths /tmp/ref-arbit-v127.log + /tmp/clone-arbit-v127.log).
  2. History corrections against the POST-swap state: the provenance
     citations re-pointed at the v121 measurement (the v127 census must
     reproduce the v121 census values EXACTLY, a drift re-check since
     v121; the v121-documented standing classes).
"""
import sys

SRC = "scripts/parity-probes/compare-v121-census.py"
DST = "scripts/parity-probes/compare-v127-census.py"

GENERIC = [
    ("v121", "v127"),
]

CORRECTIONS = [
    # docstring: the whitelist provenance citation
    ('''every leaf axis. Known documented classes are whitelisted (the v115
census values, reproduced exactly):''',
     '''every leaf axis. Known documented classes are whitelisted (the v121
census values, reproduced exactly):'''),
    # the QUADS whitelist comment's provenance citation
    ('''# EXACT-QUAD whitelist: (view, axis, ref value, clone value) — the
# v115-documented standing classes (the v127 census must reproduce the
# v115 values EXACTLY).''',
     '''# EXACT-QUAD whitelist: (view, axis, ref value, clone value) — the
# v121-documented standing classes (the v127 census must reproduce the
# v121 values EXACTLY).'''),
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

if missing:
    print("MISSING SOURCES:", missing)
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)

# residual old-token check — the era tokens v115 outside the axis
# provenance citations (the v57/v70b/v115-lineage classes keep their
# axis names; only the two provenance citations were era tokens)
import re
for m in re.finditer(r"v115", text):
    ctx = text[max(0, m.start() - 80):m.end() + 80]
    if "v115" in ctx and ("reproduce the" in ctx or "whitelisted (the" in ctx):
        print(f"RESIDUAL era token v115 in {DST}: ...{ctx[:80]!r}")
        sys.exit(1)

print(f"OK: {DST} derived — generic swap + 2 history corrections applied; residual check clean")
