#!/usr/bin/env python3
"""Derive compare-v128-census.py from compare-v122-census.py (the
axis-by-axis both-sides census comparator for the v128 SAVINGS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v122 -> v128 swap (carries the half-log
     paths /tmp/ref-arbit-v128.log + /tmp/clone-arbit-v128.log).
  2. History corrections against the POST-swap state: the provenance
     citations re-pointed at the v122 measurement (the v128 census must
     reproduce the v122 census values EXACTLY, a drift re-check since
     v122; the v122-documented standing classes).
"""
import sys

SRC = "scripts/parity-probes/compare-v122-census.py"
DST = "scripts/parity-probes/compare-v128-census.py"

GENERIC = [
    ("v122", "v128"),
]

CORRECTIONS = [
    # docstring: the whitelist provenance citation (carries no v122 token —
    # identical pre/post swap)
    ('''axis. Known documented classes are whitelisted (the v116 census values,
reproduced exactly):''',
     '''axis. Known documented classes are whitelisted (the v122 census values,
reproduced exactly):'''),
    # the QUADS whitelist comment's provenance citation (the middle line's
    # 'v122 census' is the POST-swap form; the outer v116 tokens are
    # pre/post-swap identical)
    ('''# EXACT-QUAD whitelist: (axis, ref value, clone value) — the v116
# documented standing classes (the v128 census must reproduce the
# v116 values EXACTLY).''',
     '''# EXACT-QUAD whitelist: (axis, ref value, clone value) — the v122
# documented standing classes (the v128 census must reproduce the
# v122 values EXACTLY).'''),
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

# residual old-token check — the era tokens v116 must be fully gone
# after the two citation re-pointings (the v122 comparator carried
# exactly three v116 occurrences: the docstring citation + the QUADS
# comment pair; the axis-provenance class names — the v57/v70b classes —
# carry no v116 token)
import re
residual = re.findall(r"v116", text)
if residual:
    print(f"RESIDUAL era tokens v116 in {DST}: {len(residual)} occurrences")
    sys.exit(1)

# line-count preservation report
src_n = open(SRC, encoding="utf-8").read().count("\n")
dst_n = text.count("\n")
print(f"OK: {DST} derived — generic swap + 2 history corrections applied; residual check clean")
print(f"line-count {DST}: {dst_n + 1} lines (source {src_n + 1}) — {'OK' if src_n == dst_n else 'DRIFT'}")
