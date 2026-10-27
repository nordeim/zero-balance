#!/usr/bin/env python3
"""Derive the 120th standing-checks pair from the v119 pair.

Three token families (the documented derivation protocol):
  1. v119 -> v120            (version tokens)
  2. 119th -> 120th          (ordinal tokens)
  3. ref119 -> ref120 / clone119 -> clone120  (bare session names)

After derivation, normalize BACK (v120->v119 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v119.sh",
     "scripts/parity-probes/ref-standing-v120.sh"),
    ("scripts/parity-probes/standing-checks-v119.sh",
     "scripts/parity-probes/standing-checks-v120.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("119th" -> "120th"), then bare session names, then version
    text = text.replace("119th", "120th")
    text = text.replace("ref119", "ref120")
    text = text.replace("clone119", "clone120")
    text = text.replace("v119", "v120")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("120th", "119th")
    text = text.replace("ref120", "ref119")
    text = text.replace("clone120", "clone119")
    text = text.replace("v120", "v119")
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
    residual = re.findall(r"v119|119th|ref119|clone119", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        r = subprocess.run(["bash", "-n", dst], capture_output=True, text=True)
        print(f"bash -n {dst}: {'clean' if r.returncode == 0 else r.stderr}")
