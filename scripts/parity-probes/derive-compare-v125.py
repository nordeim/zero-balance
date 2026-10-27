#!/usr/bin/env python3
"""Derive compare-v125-census.py from compare-v119-census.py (the
axis-by-axis both-sides census comparator for the v125 DASHBOARD pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the /tmp/vlm-path EXPLICIT swap FIRST (the bare
     v119 swap cannot touch 'vlm119' — no 'v119' substring; the same
     specific-first rule the series derivation's GENERIC list follows),
     then the raw v119 -> v125 swap.
  2. History corrections against the POST-swap state: the era/ordinal
     re-pointed (the v113-era pair's NINTH re-run -> the v119-era pair's
     TENTH re-run, the bracket extended ... -> v113 -> v119 -> v125), the
     provenance citations re-pointed at the v119 measurement (must
     reproduce the v119 census values EXACTLY, a drift re-check since
     v119; the v119-documented standing classes).
"""
import sys

SRC = "scripts/parity-probes/compare-v119-census.py"
DST = "scripts/parity-probes/compare-v125-census.py"

GENERIC = [
    ("/tmp/vlm119", "/tmp/vlm125"),
    ("v119", "v125"),
]

CORRECTIONS = [
    # docstring: the era/ordinal/bracket + the provenance citation
    ('''The v125 re-run (the v113-era DASHBOARD pair's NINTH re-run
[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v125])
must reproduce the v113 census values EXACTLY (a drift re-check since v113).''',
     '''The v125 re-run (the v119-era DASHBOARD pair's TENTH re-run
[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113 -> v119 -> v125])
must reproduce the v119 census values EXACTLY (a drift re-check since v119).'''),
    # the whitelist comment's provenance citation
    ('''All delta families below are the v113-documented standing classes
# (the v125 census must reproduce the v113 values EXACTLY):''',
     '''All delta families below are the v119-documented standing classes
# (the v125 census must reproduce the v119 values EXACTLY):'''),
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

# residual old-token check — the corrected bracket "-> v113 -> v119 -> v125])"
# is the one legitimate v113 survivor (the re-run chain's middle entries)
import re
bad = []
for m in re.finditer(r"v113-era|NINTH re-run|since v113|reproduce the v113|v113-documented|/tmp/vlm119", text):
    ctx = text[max(0, m.start() - 45):m.end() + 45]
    if "-> v113 -> v119 -> v125])" in ctx:
        continue  # the corrected bracket
    bad.append(m.group(0))
if bad:
    print(f"RESIDUAL OLD TOKENS: {set(bad)}")
    ok = False
else:
    print("residual check: clean")

if not ok:
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)
sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived — line-count {'preserved' if sn == dn else f'DRIFT ({dn - sn:+d})'} ({dn + 1} lines)")
