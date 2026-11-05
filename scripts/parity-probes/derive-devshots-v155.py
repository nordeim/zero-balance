#!/usr/bin/env python3
"""Derive the v155 dev-shots pair from the v154 pair (capture + verify),
version-swap-only (v154 -> v155), verified by normalize-back diff — the
documented dev-evidence derivation protocol (the v111 -> v155 chain)."""
import re
import sys

PAIR = [
    ("scripts/capture-dev-shots-v154.mjs", "scripts/capture-dev-shots-v155.mjs"),
    ("scripts/verify-dev-shots-v154.mjs", "scripts/verify-dev-shots-v155.mjs"),
]

for src, dst in PAIR:
    text = open(src, encoding="utf-8").read()
    derived = text.replace("v154", "v155")
    open(dst, "w", encoding="utf-8").write(derived)
    # normalize back and prove swap-only
    back = derived.replace("v155", "v154")
    if back != text:
        print(f"FAIL: {dst} is not version-swap-only vs {src}")
        sys.exit(1)
    residual = re.findall(r"v154", derived)
    if residual:
        print(f"FAIL: {dst} retains old tokens")
        sys.exit(1)
    print(f"OK: {dst} derived — version-swap-only (normalize-back clean), zero old tokens")
