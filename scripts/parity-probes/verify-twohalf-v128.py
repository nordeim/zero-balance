#!/usr/bin/env python3
"""Verify the v128 two-half census byte-identity contract by DIRECT
extraction (the v123/v124/v125/v126/v127 form, adapted to the SAVINGS
lineage's single SV_CENSUS_JS block). Extracts the census JS block from
arbit-v128.sh (the source) + ref-arbit-v128.sh + clone-arbit-v128.sh by
marker scanning and compares md5 line-block digests across all three —
they must equal the documented v122 lineage contract (891ab9b6)
VERBATIM."""
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

CONTRACTS = {
    "SV_CENSUS_JS": "891ab9b6",
}

ok = True
for name, expected in CONTRACTS.items():
    start = f'{name}="(async () => {{'
    end = '})()"'
    src = extract_block("scripts/parity-probes/arbit-v128.sh", start, end)
    ref = extract_block("scripts/parity-probes/ref-arbit-v128.sh", start, end)
    clone = extract_block("scripts/parity-probes/clone-arbit-v128.sh", start, end)
    digests = {
        "arbit-v128.sh": hashlib.md5(src.encode()).hexdigest()[:8],
        "ref-arbit-v128.sh": hashlib.md5(ref.encode()).hexdigest()[:8],
        "clone-arbit-v128.sh": hashlib.md5(clone.encode()).hexdigest()[:8],
    }
    uniq = set(digests.values())
    lines_n = src.count("\n") + 1
    if len(uniq) != 1:
        ok = False
        print(f"FAIL {name}: three-way digest mismatch {digests}")
    elif uniq.pop() != expected:
        ok = False
        print(f"FAIL {name}: digest {list(digests.values())[0]} != documented contract {expected}")
    else:
        print(f"OK {name}: three-way md5 {list(digests.values())[0]} == {expected} — {lines_n} lines — byte-identical across source + both halves")

print("verify-twohalf-v128:", "ALL CONTRACTS HELD" if ok else "CONTRACT FAILURE")
import sys
sys.exit(0 if ok else 1)
