#!/usr/bin/env python3
"""Derive build-twohalf-v113.py from build-twohalf-v107.py (the same
arbit-file structure — ARBIT_G lines 28..89, ARBIT_Q lines 91..148,
ARBIT_X lines 151..175, header 1..25, ref_exec 177..217, clone_exec
218..258 — the v113 derivation is line-count-preserving on the source
arbit-v113.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lineage-note fixups that must NOT be re-touched by later
swaps — the v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v107.py"
DST = "scripts/parity-probes/build-twohalf-v113.py"

SWAPS = [
    # generic version swap FIRST (raw v107 tokens -> v113)
    ("v107", "v113"),
    # the TWOHALF_NOTE lesson range (the v107 builder carries the original
    # slash form twice: the docstring single-line + the note where the
    # 'lesson' word wraps to the NEXT line — so the bare slash form, not
    # the '... lesson' phrase)
    ("v92/v93/v94/v95", "v92..v112"),
    # the lineage note (post-generic state: 'build-twohalf-v101.py' ->
    # 'build-twohalf-v107.py'; runs LAST so no later swap touches the
    # inserted 'v107' token)
    ("build-twohalf-v101.py", "build-twohalf-v107.py"),
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
open(DST, "w", encoding="utf-8").write(text)

# normalize-back verification: the derived file must differ from the source
# by version tokens ONLY (every swapped token reverses cleanly)
def normalize_back(t):
    t = t.replace("build-twohalf-v107.py", "build-twohalf-v101.py")
    t = t.replace("v92..v112", "v92/v93/v94/v95")
    t = t.replace("v113", "v107")
    return t

if normalize_back(text) != open(SRC, encoding="utf-8").read():
    print("FAIL: derived builder is NOT token-swap-only vs source")
    sys.exit(1)

# residual check on the derived file: no un-swapped v107 lineage tokens
import re
bad = re.findall(r"v92/v93/v94/v95|build-twohalf-v101", text)
if bad:
    print("RESIDUAL OLD TOKENS in derived file:", set(bad))
    sys.exit(1)

print(f"OK: {DST} derived; token-swap-only verified by normalize-back diff")
print("run it now: python3 scripts/parity-probes/build-twohalf-v113.py")
