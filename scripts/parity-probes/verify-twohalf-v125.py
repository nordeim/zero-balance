#!/usr/bin/env python3
"""Verify the two-half census byte-identity contract by DIRECT extraction
(the v123/v124 form — the sed-based extraction reads different boundaries;
the python form is the verification). Extracts the ARBIT_G/ARBIT_Q/ARBIT_X
blocks from ref-arbit-v125.sh + clone-arbit-v125.sh by marker scanning and
compares md5 line-block digests across the halves."""
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

pairs = [
    ('ARBIT_G="(function () {', '})()"', "ARBIT_G"),
    ('ARBIT_Q="(function () {', '})()"', "ARBIT_Q"),
    ('ARBIT_X="(function () {', '})()"', "ARBIT_X"),
]
ok = True
for start, end, name in pairs:
    ref = extract_block("scripts/parity-probes/ref-arbit-v125.sh", start, end)
    clone = extract_block("scripts/parity-probes/clone-arbit-v125.sh", start, end)
    md5_ref = hashlib.md5(ref.encode()).hexdigest()
    md5_clone = hashlib.md5(clone.encode()).hexdigest()
    match = "IDENTICAL" if md5_ref == md5_clone else "MISMATCH"
    print(f"{name}: ref {len(ref.splitlines())} lines md5 {md5_ref} | clone {len(clone.splitlines())} lines md5 {md5_clone} -> {match}")
    if md5_ref != md5_clone:
        ok = False

print("CONTRACT:", "HELD — census blocks byte-identical across the halves" if ok else "BROKEN")
exit(0 if ok else 1)
