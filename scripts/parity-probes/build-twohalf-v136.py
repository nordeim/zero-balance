#!/usr/bin/env python3
"""Build ref-arbit-v136.sh + clone-arbit-v136.sh from arbit-v136.sh (the
two-half controlled form, BUILT FROM THE START — the v92..v135 lesson).
The TWO census JS blocks (ARBIT_A lines 25..114 and ARBIT_B lines
116..226) are extracted ONCE and embedded byte-identically in both
halves (the contract, md5-verified). Line boundaries mapped from
arbit-v136.sh (the v130-lineage derivation, 328 wc-l lines, markers at
25/114/116/226/228/273/275/323/325/327)."""
import hashlib

SRC = "scripts/parity-probes/arbit-v136.sh"
lines = open(SRC).read().split("\n")  # 0-indexed; line N = lines[N-1]
assert len(lines) >= 327, f"unexpected line count {len(lines)}"

# Census JS blocks (1-indexed inclusive): A 25..114, B 116..226.
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

# The reference-side execution block: lines 228..273 (after the marker at 228).
ref_exec = "\n".join(lines[227:273])

# The clone-side execution block: lines 275..323 (the with-server heredoc
# wrapper + the clone-side login + censuses + the fixture restore, ending
# at the EOF marker at 323).
clone_exec = "\n".join(lines[274:323])

# The trailing seedcheck block: lines 325..327.
seedcheck = "\n".join(lines[324:327])

TWOHALF_NOTE = """
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v135 lesson):
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
echo "=== ref arbit v136 half done ==="
"""

clone_half = f"""{header}
{TWOHALF_NOTE}
{a_block}

{b_block}

########## CLONE SIDE (the half) ##########
{clone_exec}

echo ""
echo "=== seedcheck (env -u DATABASE_URL — the documented pollution discipline) ==="
cd "$(dirname "$0")/../.."
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs
echo "=== clone arbit v136 half done ==="
"""

open("scripts/parity-probes/ref-arbit-v136.sh", "w").write(ref_half)
open("scripts/parity-probes/clone-arbit-v136.sh", "w").write(clone_half)

# The contract check: both census JS blocks must be byte-identical.
md5_a = hashlib.md5(a_block.encode()).hexdigest()
md5_b = hashlib.md5(b_block.encode()).hexdigest()
print(f"ARBIT_A census block md5: {md5_a}")
print(f"ARBIT_A block lines: {a_end - a_start + 1}")
print(f"ARBIT_B census block md5: {md5_b}")
print(f"ARBIT_B block lines: {b_end - b_start + 1}")
print("halves written")
