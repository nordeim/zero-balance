#!/usr/bin/env python3
"""Derive compare-v135-census.py from compare-v129-census.py (the
axis-by-axis both-sides census comparator for the v135 LOGIN + CALCULATOR
pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v129 -> v135 swap (carries the half-log
     paths /tmp/vlm129/ref-arbit-full.log + clone-arbit-full.log and the
     docstring's file-name + 'the v129 two-half census' citation).
  2. History corrections against the POST-swap state: the lineage ordinal
     citation (the v123-era pair's ELEVENTH re-run -> the v129-era pair's
     TWELFTH re-run) and the provenance chain extended (the
     v105/v111/v117/v123 records -> the v105/v111/v117/v123/v129 records
     — the v129 record re-verified the classes; the v135 census must
     reproduce the v129 values EXACTLY, a drift re-check since v129).
"""
import sys

SRC = "scripts/parity-probes/compare-v129-census.py"
DST = "scripts/parity-probes/compare-v135-census.py"

GENERIC = [
    # the explicit log-path swap FIRST ('vlm129' carries no 'v129'
    # substring — the same explicit-token discipline as the series
    # derivation's session tokens)
    ("/tmp/vlm129", "/tmp/vlm135"),
    ("v129", "v135"),
]

CORRECTIONS = [
    # docstring: the lineage ordinal citation (carries no v129 token —
    # identical pre/post swap)
    ("(the v123-era LOGIN + CALCULATOR pair's ELEVENTH re-run).",
     "(the v129-era LOGIN + CALCULATOR pair's TWELFTH re-run)."),
    # the DOCUMENTED dict's provenance chain (the records that established
    # + re-verified the classes — extended with the v129 record)
    ("the v105/v111/v117/v123 records",
     "the v105/v111/v117/v123/v129 records"),
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

# residual old-token check — the era tokens must be gone or confined to
# the extended provenance chain; the axis-provenance class names (the v99
# FINDER ARTIFACT, the v87 pin, the v45 sweep, the v10 convention) carry
# no stale era token and must survive untouched
import re
ok = True
for m in re.finditer(r"v123-era|ELEVENTH|/tmp/vlm129", text):
    print(f"RESIDUAL era token {m.group(0)!r} in {DST}")
    ok = False
for m in re.finditer(r"v123", text):
    ctx = text[max(0, m.start() - 40):m.end() + 40]
    if "v105/v111/v117/v123/v129 records" in ctx:
        continue
    print(f"RESIDUAL bare v123 outside the provenance chain in {DST}")
    ok = False
if ok:
    print(f"OK: {DST} derived — generic swap + 2 corrections applied; residual check clean")

# line-count preservation report
src_n = open(SRC, encoding="utf-8").read().count("\n")
dst_n = text.count("\n")
print(f"line-count {DST}: {dst_n + 1} lines (source {src_n + 1}) — {'OK' if src_n == dst_n else 'DRIFT'}")
sys.exit(0 if ok else 1)
