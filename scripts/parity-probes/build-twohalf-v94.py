#!/usr/bin/env python3
"""Build ref-arbit-v94.sh + clone-arbit-v94.sh from arbit-v94.sh (the
two-half controlled form, BUILT FROM THE START this cycle — the v92/v93
lesson). The TWO census JS blocks (ARBIT_A lines 25..114 and ARBIT_B
lines 116..226) are extracted ONCE and embedded byte-identically in both
halves (the contract, md5-verified)."""
import hashlib

SRC = "scripts/parity-probes/arbit-v94.sh"
lines = open(SRC).read().split("\n")  # 0-indexed; line N = lines[N-1]

# Census JS blocks (1-indexed inclusive): ARBIT_A 25..114, ARBIT_B 116..226.
a_start, a_end = 25, 114
b_start, b_end = 116, 226
a_block = "\n".join(lines[a_start - 1 : a_end])
b_block = "\n".join(lines[b_start - 1 : b_end])
assert a_block.startswith("ARBIT_A='(async () => {"), a_block[:60]
assert a_block.rstrip().endswith("})()'"), a_block[-60:]
assert b_block.startswith("ARBIT_B='(async () => {"), b_block[:60]
assert b_block.rstrip().endswith("})()'"), b_block[-60:]

# Header (lines 1..24): the shared provenance comments + set -u + REF var.
header = "\n".join(lines[0:24])
assert 'set -u' in header and 'REF="https://' in header, "header boundary wrong"

# The reference-side execution block: lines 228..273 (the marker through the
# last ARBIT_B eval).
ref_exec = "\n".join(lines[227:273])
assert ref_exec.startswith("# ---------- REFERENCE side ----------"), ref_exec[:60]
assert ref_exec.rstrip().endswith('agent-browser eval "$ARBIT_B" 2>/dev/null | tail -1'), ref_exec[-80:]

# The clone-side execution block: lines 275..323 (the marker through EOF).
clone_exec = "\n".join(lines[274:323])
assert clone_exec.startswith("# ---------- CLONE side"), clone_exec[:60]
assert clone_exec.rstrip().endswith("EOF"), clone_exec[-40:]

TWOHALF_NOTE = """
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92/v93 lesson):
# the combined arbit form's clone half is the chromium resource-exhaustion
# risk (the v89/v91-documented symptom class), so the census runs as two
# independent halves from the start; the census JS blocks are byte-identical
# across the halves (the md5 line-block contract).
"""

ref_half = f"""{header}
{TWOHALF_NOTE}
{a_block}

{b_block}

########## REFERENCE SIDE (the half) ##########
{ref_exec}
echo "=== ref arbit v94 half done ==="
"""

clone_half = f"""{header}
{TWOHALF_NOTE}
{a_block}

{b_block}

########## CLONE SIDE (the half) ##########
cd "$(dirname "$0")/../.."
{clone_exec}

echo ""
echo "=== seedcheck (env -u DATABASE_URL — the documented pollution discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs
echo "=== clone arbit v94 half done ==="
"""

open("scripts/parity-probes/ref-arbit-v94.sh", "w").write(ref_half)
open("scripts/parity-probes/clone-arbit-v94.sh", "w").write(clone_half)

# The md5 line-block contract: the census blocks byte-identical across halves.
def block_md5(path, start_marker, end_marker):
    text = open(path).read()
    start = text.index(start_marker)
    end = text.index(end_marker, start) + len(end_marker)
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

for marker in ("ARBIT_A='(async () => {", "ARBIT_B='(async () => {"):
    end_marker = "})()'"
    rm, rn = block_md5("scripts/parity-probes/ref-arbit-v94.sh", marker, end_marker)
    cm, cn = block_md5("scripts/parity-probes/clone-arbit-v94.sh", marker, end_marker)
    assert rm == cm, f"CENSUS BLOCK MISMATCH for {marker[:20]}: {rm} vs {cm}"
    print(f"block {marker[:12]}... md5 {rm} — {rn} lines — byte-identical across halves OK")

print("ref-arbit-v94.sh + clone-arbit-v94.sh built")
