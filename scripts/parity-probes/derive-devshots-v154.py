#!/usr/bin/env python3
"""Derive the v154 dev-shots pair from the v153 pair (capture + verify),
version-swap-only (v153 -> v154), verified by normalize-back diff — the
documented dev-evidence derivation protocol (the v111 -> v153 chain)."""
import re
import sys

PAIR = [
    ("scripts/capture-dev-shots-v153.mjs", "scripts/capture-dev-shots-v154.mjs"),
    ("scripts/verify-dev-shots-v153.mjs", "scripts/verify-dev-shots-v154.mjs"),
]

for src, dst in PAIR:
    text = open(src, encoding="utf-8").read()
    derived = text.replace("v153", "v154")
    open(dst, "w", encoding="utf-8").write(derived)
    # normalize back and prove swap-only
    back = derived.replace("v154", "v153")
    if back != text:
        print(f"FAIL: {dst} is not version-swap-only vs {src}")
        sys.exit(1)
    residual = re.findall(r"v153", derived)
    if residual:
        print(f"FAIL: {dst} retains old tokens")
        sys.exit(1)
    print(f"OK: {dst} derived — version-swap-only (normalize-back clean), zero old tokens")
