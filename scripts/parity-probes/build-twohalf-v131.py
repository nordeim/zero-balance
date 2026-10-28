#!/usr/bin/env python3
"""Build ref-arbit-v131.sh + clone-arbit-v131.sh from arbit-v131.sh (the
two-half controlled form, BUILT FROM THE START — the v92..v130 lesson).
The THREE census JS blocks (ARBIT_G lines 28..89, ARBIT_Q lines 91..148,
ARBIT_X lines 151..175) are extracted ONCE and embedded byte-identically
in both halves (the contract, md5-verified). Line numbers inherited
verbatim from build-twohalf-v125.py — the v131 derivation is
line-count-preserving (verified by derive-v131-series.py)."""
import hashlib

SRC = "scripts/parity-probes/arbit-v131.sh"
lines = open(SRC).read().split("\n")  # 0-indexed; line N = lines[N-1]
assert len(lines) >= 258, f"unexpected line count {len(lines)}"

# Census JS blocks (1-indexed inclusive): ARBIT_G 28..89, ARBIT_Q 91..148,
# ARBIT_X 151..175.
blocks = {}
for name, start, end in (("ARBIT_G", 28, 89), ("ARBIT_Q", 91, 148), ("ARBIT_X", 151, 175)):
    block = "\n".join(lines[start - 1 : end])
    assert block.startswith(f'{name}="(function () {{'), block[:60]
    assert block.rstrip().endswith('})()"'), block[-60:]
    blocks[name] = block

# Header (lines 1..25): the shared provenance comments + set -u + REF var.
header = "\n".join(lines[0:25])
assert 'set -u' in header and 'REF="https://' in header, "header boundary wrong"

# The reference-side execution block: lines 177..217 (the marker through the
# last ARBIT_X eval).
ref_exec = "\n".join(lines[176:217])
assert ref_exec.startswith("# ---------- REFERENCE side"), ref_exec[:60]
assert ref_exec.rstrip().endswith('agent-browser eval "$ARBIT_X" 2>/dev/null | tail -1'), ref_exec[-80:]

# The clone-side execution block: lines 218..258 (the marker through EOF).
clone_exec = "\n".join(lines[217:258])
assert clone_exec.startswith("# ---------- CLONE side"), clone_exec[:60]
assert clone_exec.rstrip().endswith('echo "=== arbit v131 done ==="'), clone_exec[-60:]

TWOHALF_NOTE = """
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v130
# lesson): the combined arbit form's clone half is the chromium
# resource-exhaustion risk (the v89/v91-documented symptom class), so the
# census runs as two independent halves from the start; the census JS
# blocks are byte-identical across the halves (the md5 line-block
# contract).
"""

ref_half = f"""{header}
{TWOHALF_NOTE}
{blocks["ARBIT_G"]}

{blocks["ARBIT_Q"]}

{blocks["ARBIT_X"]}

########## REFERENCE SIDE (the half) ##########
{ref_exec}
echo "=== ref arbit v131 half done ==="
"""

clone_half = f"""{header}
{TWOHALF_NOTE}
{blocks["ARBIT_G"]}

{blocks["ARBIT_Q"]}

{blocks["ARBIT_X"]}

########## CLONE SIDE (the half) ##########
{clone_exec}
"""

open("scripts/parity-probes/ref-arbit-v131.sh", "w").write(ref_half)
open("scripts/parity-probes/clone-arbit-v131.sh", "w").write(clone_half)

# The md5 line-block contract: the census blocks byte-identical across halves.
def block_md5(path, start_marker, end_marker):
    text = open(path).read()
    start = text.index(start_marker)
    end = text.index(end_marker, start) + len(end_marker)
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

for marker in ('ARBIT_G="(function () {', 'ARBIT_Q="(function () {', 'ARBIT_X="(function () {'):
    end_marker = '})()"'
    rm, rn = block_md5("scripts/parity-probes/ref-arbit-v131.sh", marker, end_marker)
    cm, cn = block_md5("scripts/parity-probes/clone-arbit-v131.sh", marker, end_marker)
    assert rm == cm, f"CENSUS BLOCK MISMATCH for {marker[:20]}: {rm} vs {cm}"
    print(f"block {marker[:12]}... md5 {rm} — {rn} lines — byte-identical across halves OK")

print("ref-arbit-v131.sh + clone-arbit-v131.sh built")
