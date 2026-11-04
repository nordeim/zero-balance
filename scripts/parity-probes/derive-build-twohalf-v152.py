#!/usr/bin/env python3
"""Derive build-twohalf-v152.py from build-twohalf-v146.py (the same
arbit-file structure — SV_CENSUS_JS lines 38..190, header 1..36, ref_exec
193..224, clone_exec 227..256 — the v152 derivation is line-count-preserving
on the source arbit-v152.sh, itself a 262-line corrected-swap of
arbit-v146.sh).
Token swaps only; verified by normalize-back diff (swap order: the session
token FIRST, then the generic swap, then the lesson-range bump, the
lineage-note fixup LAST — the v110 swap-order rule).
NOTE the session-token swap (the v121-cycle stale-session-fix precedent):
the v146 builder's ref_exec assertion carries 'refarbit146' — the v146
lineage's own CURRENT token. The v152 derivation bumps it to 'refarbit152'
so the builder's assertion AGREES with the combined arbit-v152.sh's own
'refarbit152' (the bare v146->v152 swap cannot touch it — the token
carries no 'v' prefix)."""
import re
import sys

SRC = "scripts/parity-probes/build-twohalf-v146.py"
DST = "scripts/parity-probes/build-twohalf-v152.py"

SWAPS = [
    # session token FIRST (no 'v' prefix — untouched by the generic swap)
    ("refarbit146", "refarbit152"),
    # generic version swap (raw v146 tokens -> v152)
    ("v146", "v152"),
    # the TWOHALF_NOTE lesson range (the v146 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms incl. the note's line-wrapped tail, the v131 lesson)
    ("v92..v145", "v92..v151"),
    # the lineage note (the source's prose pointer 'build-twohalf-v140.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v146' token)
    ("build-twohalf-v140.py", "build-twohalf-v146.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v146.py' (the source
# pointer), so that occurrence is whitelisted before the scan
# (the v115..v151 residual-precedent discipline).
scan = text.replace("build-twohalf-v146.py", "", 1)
residual = re.findall(r"v146|refarbit146|v92\.\.v145", scan)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

# syntax gate
import subprocess
r = subprocess.run(["python3", "-m", "py_compile", DST], capture_output=True, text=True)
if r.returncode != 0:
    print(f"FAIL: py_compile {DST}: {r.stderr}")
    sys.exit(1)

print(f"derived {DST} (session token + generic + lesson-range + lineage-note swaps; normalize-back clean, zero residual)")
