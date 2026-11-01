#!/usr/bin/env python3
"""Derive compare-v144-census.py from compare-v138-census.py (the
axis-by-axis both-sides census comparator for the v144 MOBILE TWINS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the /tmp/vlm-path EXPLICIT swap FIRST (the bare
     v138 swap cannot touch 'vlm138' — no 'v138' substring; the same
     specific-first rule the series derivation's GENERIC list follows),
     then the raw v138 -> v144 swap.
  2. History corrections against the POST-swap state: the era/ordinal
     re-pointed (the MOBILE TWINS pair's TWELFTH re-run -> the THIRTEENTH
     re-run, the bracket extended ... -> v120 -> v126 -> v132 -> v138 ->
     v144), the provenance citations re-pointed at the v138 measurement
     (must reproduce the v138 census values EXACTLY, a drift re-check
     since v138; the v138-documented standing classes)."""
import sys

SRC = "scripts/parity-probes/compare-v138-census.py"
DST = "scripts/parity-probes/compare-v144-census.py"

GENERIC = [
    ("/tmp/vlm138", "/tmp/vlm144"),
    ("v138", "v144"),
]

CORRECTIONS = [
    # docstring: the era/ordinal/bracket + the provenance citation
    ('''The v144 re-run (the MOBILE TWINS pair's TWELFTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126 -> v132 -> v144])
must reproduce the v132 census values EXACTLY (a drift re-check since v132).''',
     '''The v144 re-run (the MOBILE TWINS pair's THIRTEENTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126 -> v132 -> v138 -> v144])
must reproduce the v138 census values EXACTLY (a drift re-check since v138).'''),
    # the whitelist comment's provenance citation
    ('''All delta families below are the v132-documented standing classes
# (the v144 census must reproduce the v132 values EXACTLY):''',
     '''All delta families below are the v138-documented standing classes
# (the v144 census must reproduce the v138 values EXACTLY):'''),
    # the final print's provenance citation
    ('''print("(the v132 census values reproduced EXACTLY — zero drift since v132)")''',
     '''print("(the v138 census values reproduced EXACTLY — zero drift since v138)")'''),
]

text = open(SRC, encoding="utf-8").read()
for old, new in GENERIC:
    text = text.replace(old, new)

ok = True
for old, new in CORRECTIONS:
    if old not in text:
        print(f"MISS: {old[:70]!r}")
        ok = False
        continue
    text = text.replace(old, new)
    print(f"applied: {old[:52]!r} -> corrected")

# residual old-token check — the corrected bracket "-> v120 -> v126 -> v132 -> v138 -> v144])"
# is the one legitimate v132 survivor (the re-run chain's middle entries)
import re
bad = []
for m in re.finditer(r"re-shot v132|TENTH re-run|ELEVENTH re-run|TWELFTH re-run|since v132|reproduce the v132|v132-documented|/tmp/vlm138|arbit-v138", text):
    ctx = text[max(0, m.start() - 60):m.end() + 60]
    if "-> v120 -> v126 -> v132 -> v138 -> v144])" in ctx:
        continue  # the corrected bracket
    bad.append(m.group(0))
for m in re.finditer(r"v132", text):
    ctx = text[max(0, m.start() - 60):m.end() + 60]
    if "-> v120 -> v126 -> v132 -> v138 -> v144])" in ctx:
        continue  # the corrected bracket
    if "v132 (outside the corrected bracket)" not in bad:
        bad.append("v132 (outside the corrected bracket)")
if bad:
    print(f"RESIDUAL OLD TOKENS: {sorted(set(bad))}")
    ok = False
else:
    print("residual check: clean")

if not ok:
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)
sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived — line-count {'preserved' if sn == dn else f'DRIFT ({dn - sn:+d})'} ({dn + 1} lines)")
