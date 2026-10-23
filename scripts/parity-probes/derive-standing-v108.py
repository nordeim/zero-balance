#!/usr/bin/env python3
"""Derive the 102nd standing-checks pair from the v101 pair.

Three token families (the documented derivation protocol):
  1. v101 -> v102           (version tokens)
  2. 101st -> 102nd         (ordinal tokens)
  3. ref101 -> ref102 / clone101 -> clone102   (bare session names)

After derivation, normalize BACK (v102->v101 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v101.sh",
     "scripts/parity-probes/ref-standing-v102.sh"),
    ("scripts/parity-probes/standing-checks-v101.sh",
     "scripts/parity-probes/standing-checks-v102.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("101st" -> "102nd"), then bare session names, then version
    text = text.replace("101st", "102nd")
    text = text.replace("ref101", "ref102")
    text = text.replace("clone101", "clone102")
    text = text.replace("v101", "v102")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("102nd", "101st")
    text = text.replace("ref102", "ref101")
    text = text.replace("clone102", "clone101")
    text = text.replace("v102", "v101")
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
    residual = re.findall(r"v101|101st|ref101|clone101", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        r = subprocess.run(["bash", "-n", dst], capture_output=True, text=True)
        print(f"bash -n {dst}: {'clean' if r.returncode == 0 else r.stderr}")
else:
    sys.exit(1)
