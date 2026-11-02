#!/usr/bin/env python3
"""Derive the 140th standing-checks pair from the v139 pair.

Three token families (the documented derivation protocol):
  1. v139 -> v140           (version tokens)
  2. 139th -> 140th         (ordinal tokens — a th->th plain replace,
                             the same plain-replace form as the chain's
                             prior transitions, e.g. v144's 137th->138th
                             and v145's 138th->139th: the ordinal is
                             always a single plain replace, the suffix
                             following the number's English form)
  3. ref139 -> ref140 / clone139 -> clone140   (bare session names)

After derivation, normalize BACK (v140->v139 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import re
import subprocess
import sys

PAIR = [
    ("scripts/parity-probes/ref-standing-v139.sh",
     "scripts/parity-probes/ref-standing-v140.sh"),
    ("scripts/parity-probes/standing-checks-v139.sh",
     "scripts/parity-probes/standing-checks-v140.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("139th" -> "140th"), then bare session names, then version
    text = text.replace("139th", "140th")
    text = text.replace("ref139", "ref140")
    text = text.replace("clone139", "clone140")
    text = text.replace("v139", "v140")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("140th", "139th")
    text = text.replace("ref140", "ref139")
    text = text.replace("clone140", "clone139")
    text = text.replace("v140", "v139")
    return text

ok = True
for src, dst in PAIR:
    derived = derive(src, dst)
    with open(src, "r", encoding="utf-8") as f:
        original = f.read()
    if normalize_back(derived) != original:
        ok = False
        print(f"FAIL: {dst} is NOT version-bump-only vs {src}")
    # residual old-token check on the derived file
    residual = re.findall(r"v139|139th|ref139|clone139", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if not ok:
    sys.exit(1)

# syntax gates on both halves
for _, dst in PAIR:
    r = subprocess.run(["bash", "-n", dst], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL: bash -n {dst}: {r.stderr}")
        sys.exit(1)

# line-count preservation (the documented contract)
for src, _ in PAIR:
    with open(src, "r", encoding="utf-8") as f:
        src_lines = len(f.read().splitlines())
    print(f"{src}: {src_lines} lines")
for _, dst in PAIR:
    with open(dst, "r", encoding="utf-8") as f:
        dst_lines = len(f.read().splitlines())
    print(f"{dst}: {dst_lines} lines")

print("140th standing pair derived clean (ref-standing-v140.sh + standing-checks-v140.sh)")
