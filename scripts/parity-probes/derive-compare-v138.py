#!/usr/bin/env python3
"""Derive compare-v138-census.py from compare-v132-census.py (the
axis-by-axis both-sides census comparator for the v138 MOBILE TWINS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the /tmp/vlm-path EXPLICIT swap FIRST (the bare
     v132 swap cannot touch 'vlm132' — no 'v132' substring; the same
     specific-first rule the series derivation's GENERIC list follows),
     then the raw v132 -> v138 swap.
  2. History corrections against the POST-swap state: the era/ordinal
     re-pointed (the MOBILE TWINS pair's ELEVENTH re-run -> the TWELFTH
     re-run, the bracket extended ... -> v120 -> v126 -> v132 -> v138),
     the provenance citations re-pointed at the v132 measurement (must
     reproduce the v132 census values EXACTLY, a drift re-check since
     v132; the v132-documented standing classes).
NOTE: the v132 derivation's residual loop carried a latent 'textax'
typo (never hit — its scans found zero matches); this derivation writes
the correct text[max(0, m.start() - 60):m.end() + 60] slice form, the
fix carried forward per the change-management discipline."""
import sys

SRC = "scripts/parity-probes/compare-v132-census.py"
DST = "scripts/parity-probes/compare-v138-census.py"

GENERIC = [
    ("/tmp/vlm132", "/tmp/vlm138"),
    ("v132", "v138"),
]

CORRECTIONS = [
    # docstring: the era/ordinal/bracket + the provenance citation
    ('''The v138 re-run (the MOBILE TWINS pair's ELEVENTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126 -> v138])
must reproduce the v126 census values EXACTLY (a drift re-check since v126).''',
     '''The v138 re-run (the MOBILE TWINS pair's TWELFTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126 -> v132 -> v138])
must reproduce the v132 census values EXACTLY (a drift re-check since v132).'''),
    # the whitelist comment's provenance citation
    ('''All delta families below are the v126-documented standing classes
# (the v138 census must reproduce the v126 values EXACTLY):''',
     '''All delta families below are the v132-documented standing classes
# (the v138 census must reproduce the v132 values EXACTLY):'''),
    # the final print's provenance citation
    ('''print("(the v126 census values reproduced EXACTLY — zero drift since v126)")''',
     '''print("(the v132 census values reproduced EXACTLY — zero drift since v132)")'''),
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

# residual old-token check — the corrected bracket "-> v120 -> v126 -> v132 -> v138])"
# is the one legitimate v126 survivor (the re-run chain's middle entries)
import re
bad = []
for m in re.finditer(r"re-shot v126|TENTH re-run|ELEVENTH re-run|since v126|reproduce the v126|v126-documented|/tmp/vlm132|arbit-v132", text):
    ctx = text[max(0, m.start() - 60):m.end() + 60]
    if "-> v120 -> v126 -> v132 -> v138])" in ctx:
        continue  # the corrected bracket
    bad.append(m.group(0))
for m in re.finditer(r"v126", text):
    ctx = text[max(0, m.start() - 60):m.end() + 60]
    if "-> v120 -> v126 -> v132 -> v138])" in ctx:
        continue  # the corrected bracket
    if "v126 (outside the corrected bracket)" not in bad:
        bad.append("v126 (outside the corrected bracket)")
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
