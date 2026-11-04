#!/usr/bin/env python3
"""Derive build-twohalf-v151.py from build-twohalf-v145.py (the same
arbit-file structure — CENSUS_JS lines 22..214, header 1..21, ref_exec
216..250 — the v151 derivation is line-count-preserving on the source
arbit-v151.sh, itself a 285-line corrected-swap of arbit-v145.sh).
Token swaps only; verified by normalize-back diff (swap order: the session
token FIRST, then the generic swap, then the lesson-range bump, the
lineage-note fixup LAST — the v110 swap-order rule).
NOTE the session-token swap (the v121-cycle stale-session-fix precedent):
the v145 builder's embedded clone_login carries 'clonearbit145' — the
v145 lineage's own CURRENT token. The v151 derivation bumps it to
'clonearbit151' so the built clone half's session namespace AGREES with
the combined arbit-v151.sh's own 'clonearbit151' (the bare v145->v151
swap cannot touch it — the token carries no 'v' prefix)."""
import re
import sys

SRC = "scripts/parity-probes/build-twohalf-v145.py"
DST = "scripts/parity-probes/build-twohalf-v151.py"

SWAPS = [
    # session token FIRST (no 'v' prefix — untouched by the generic swap)
    ("clonearbit145", "clonearbit151"),
    # generic version swap (raw v145 tokens -> v151)
    ("v145", "v151"),
    # the TWOHALF_NOTE lesson range (the v145 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms incl. the note's line-wrapped tail, the v131 lesson)
    ("v92..v144", "v92..v150"),
    # the lineage note (the source's prose pointer 'build-twohalf-v139.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v145' token)
    ("build-twohalf-v139.py", "build-twohalf-v145.py"),
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

# normalize back and prove version-swap-only
back = text
for old, new in reversed(SWAPS):
    back = back.replace(new, old)
original = open(SRC, encoding="utf-8").read()
if back != original:
    print("FAIL: not a pure token swap (normalize-back mismatch)")
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)

# residual old-token check on the derived builder — the lineage-note
# fixup deliberately re-inserts 'build-twohalf-v145.py' (the source
# pointer), so that occurrence is whitelisted before the scan
# (the v115..v150 residual-precedent discipline).
scan = text.replace("build-twohalf-v145.py", "", 1)
residual = re.findall(r"v145|clonearbit145|v92\.\.v144", scan)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

# syntax gate
r = subprocess_run = None
import subprocess
r = subprocess.run(["python3", "-m", "py_compile", DST], capture_output=True, text=True)
if r.returncode != 0:
    print(f"FAIL: py_compile {DST}: {r.stderr}")
    sys.exit(1)

print(f"derived {DST} (session token + generic + lesson-range + lineage-note swaps; normalize-back clean, zero residual)")
