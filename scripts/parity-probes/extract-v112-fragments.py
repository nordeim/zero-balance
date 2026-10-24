#!/usr/bin/env python3
"""Extract the exact post-swap header fragments from the v106 lineage files.

Simulates the v112 generic swaps on the four v106 sources, then prints the
header comment block (up to the 'set -u' / first non-comment line) with
repr() so every byte is visible for the correction-map transcription.
Also locates the lineage-note lines in arbit-v106.sh and the census-block
boundaries for the md5 contracts.
"""
import hashlib

BASE = "scripts/parity-probes/"
FILES = {
    "vlm-shots-v106.sh": "vlm-shots-v112.sh",
    "clone-vlmshots-v106.sh": "clone-vlmshots-v112.sh",
    "vlm-compare-v106.mjs": "vlm-compare-v112.mjs",
    "arbit-v106.sh": "arbit-v112.sh",
}
GENERIC = [
    ("refvlm106", "refvlm112"),
    ("clonevlm106", "clonevlm112"),
    ("refar106", "refar112"),
    ("clonear106", "clonear112"),
    ("/tmp/vlm106", "/tmp/vlm112"),
    ("v106", "v112"),
]

for src, dst in FILES.items():
    text = open(BASE + src, encoding="utf-8").read()
    for old, new in GENERIC:
        text = text.replace(old, new)
    print(f"===== {dst} — post-swap header (repr) =====")
    lines = text.split("\n")
    # print the leading comment block (shebang + comments) verbatim in repr form
    for i, ln in enumerate(lines):
        if i > 0 and not (ln.startswith("#") or ln.startswith("//")):
            break
        print(f"L{i+1}: {ln!r}")
    print()

# Census-block md5 contracts in arbit-v106.sh (the v106 monolith):
# locate the two census JS heredoc blocks by their marker comments.
arb = open(BASE + "arbit-v106.sh", encoding="utf-8").read()
lines = arb.split("\n")
print("===== arbit-v106.sh census-block markers =====")
for i, ln in enumerate(lines):
    if "CENSUS" in ln or "census" in ln.lower() and ("JS" in ln or "block" in ln.lower()):
        print(f"L{i+1}: {ln!r}")
