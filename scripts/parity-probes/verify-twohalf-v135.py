#!/usr/bin/env python3
"""Verify the v135 two-half census byte-identity contracts by DIRECT
extraction (the v124..v134 form, adapted to the LOGIN+CALC lineage's TWO
census blocks). Extracts each census JS block from arbit-v135.sh (the
source) + ref-arbit-v135.sh + clone-arbit-v135.sh by marker scanning and
compares md5 line-block digests across all three — they must be
byte-identical (the documented two-half contract)."""
import hashlib

def extract_block(path, start_marker, end_marker):
    lines = open(path, encoding="utf-8").read().split("\n")
    block, inside = [], False
    for ln in lines:
        if not inside and ln.startswith(start_marker):
            inside = True
            block.append(ln)
            continue
        if inside:
            block.append(ln)
            if ln.rstrip().endswith(end_marker):
                break
    return "\n".join(block)

CONTRACTS = ["CALC_CENSUS_JS", "LOGIN_CENSUS_JS"]

ok = True
for name in CONTRACTS:
    start = f'{name}="(async () => {{'
    end = '})()"'
    src = extract_block("scripts/parity-probes/arbit-v135.sh", start, end)
    ref = extract_block("scripts/parity-probes/ref-arbit-v135.sh", start, end)
    clone = extract_block("scripts/parity-probes/clone-arbit-v135.sh", start, end)
    digests = {
        "arbit-v135.sh": hashlib.md5(src.encode()).hexdigest(),
        "ref-arbit-v135.sh": hashlib.md5(ref.encode()).hexdigest(),
        "clone-arbit-v135.sh": hashlib.md5(clone.encode()).hexdigest(),
    }
    uniq = set(digests.values())
    lines_n = src.count("\n") + 1
    if len(uniq) != 1:
        ok = False
        print(f"FAIL {name}: three-way digest mismatch {digests}")
    else:
        print(f"OK {name}: three-way md5 {list(digests.values())[0][:16]} — {lines_n} lines — byte-identical across source + both halves")

print("verify-twohalf-v135:", "ALL CONTRACTS HELD" if ok else "CONTRACT FAILURE")
import sys
sys.exit(0 if ok else 1)
