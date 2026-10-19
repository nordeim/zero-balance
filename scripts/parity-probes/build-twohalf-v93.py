#!/usr/bin/env python3
"""Build ref-arbit-v93.sh + clone-arbit-v93.sh from arbit-v93.sh (the
two-half controlled form, BUILT FROM THE START this cycle — the v92
lesson). The TWO census JS blocks (CALC_CENSUS_JS lines 22..82 and
LOGIN_CENSUS_JS lines 84..119) are extracted ONCE and embedded
byte-identically in both halves (the contract, md5-verified)."""
import hashlib

SRC = "scripts/parity-probes/arbit-v93.sh"
lines = open(SRC).read().split("\n")  # 0-indexed; line N = lines[N-1]

# Census JS blocks (1-indexed inclusive): CALC 22..82, LOGIN 84..119.
calc_start, calc_end = 22, 82
login_start, login_end = 84, 119
calc_block = "\n".join(lines[calc_start - 1 : calc_end])
login_block = "\n".join(lines[login_start - 1 : login_end])
assert calc_block.startswith('CALC_CENSUS_JS="(async () => {'), calc_block[:60]
assert calc_block.rstrip().endswith('})()"'), calc_block[-60:]
assert login_block.startswith('LOGIN_CENSUS_JS="(async () => {'), login_block[:60]
assert login_block.rstrip().endswith('})()"'), login_block[-60:]

# Header (lines 1..21): the shared provenance comments + set -u + REF var.
header = "\n".join(lines[0:21])

# The reference-side execution block: lines 122..199 (after the marker at 121).
ref_exec = "\n".join(lines[121:199])

# The clone-side execution block: lines 203..348 (between the CLONE SIDE
# marker at 202 and the seedcheck at 350), minus the marker echo.
clone_exec = "\n".join(lines[202:348])

# The trailing seedcheck block: lines 350..354.
seedcheck = "\n".join(lines[349:354])

TWOHALF_NOTE = """
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92 lesson):
# the combined arbit form's clone half is the chromium resource-exhaustion
# risk (the v89/v91-documented symptom class), so the census runs as two
# independent halves from the start; the census JS blocks are byte-identical
# across the halves (the md5 line-block contract).
"""

ref_half = f"""{header}
{TWOHALF_NOTE}
{calc_block}

{login_block}

########## REFERENCE SIDE (the half) ##########
{ref_exec}
echo "=== ref arbit v93 half done ==="
"""

clone_half = f"""{header}
{TWOHALF_NOTE}
{calc_block}

{login_block}

########## CLONE SIDE (the half) ##########
{clone_exec}

echo ""
{seedcheck}
echo "=== clone arbit v93 half done ==="
"""

open("scripts/parity-probes/ref-arbit-v93.sh", "w").write(ref_half)
open("scripts/parity-probes/clone-arbit-v93.sh", "w").write(clone_half)

# The contract check: both census JS blocks must be byte-identical.
md5_calc = hashlib.md5(calc_block.encode()).hexdigest()
md5_login = hashlib.md5(login_block.encode()).hexdigest()
print(f"CALC_CENSUS_JS block md5: {md5_calc}")
print(f"CALC block lines: {calc_end - calc_start + 1}")
print(f"LOGIN_CENSUS_JS block md5: {md5_login}")
print(f"LOGIN block lines: {login_end - login_start + 1}")
print("halves written")
