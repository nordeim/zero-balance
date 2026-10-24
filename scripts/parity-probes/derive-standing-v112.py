#!/usr/bin/env python3
"""Derive the 106th standing-checks pair from the v105 pair.

Three token families (the documented derivation protocol):
  1. v105 -> v106           (version tokens)
  2. 105th -> 106th         (ordinal tokens)
  3. ref105 -> ref106 / clone105 -> clone106   (bare session names)

After derivation, normalize BACK (v106->v105 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v105.sh",
     "scripts/parity-probes/ref-standing-v106.sh"),
    ("scripts/parity-probes/standing-checks-v105.sh",
     "scripts/parity-probes/standing-checks-v106.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("105th" -> "106th"), then bare session names, then version
    text = text.replace("105th", "106th")
    text = text.replace("ref105", "ref106")
    text = text.replace("clone105", "clone106")
    text = text.replace("v105", "v106")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("106th", "105th")
    text = text.replace("ref106", "ref105")
    text = text.replace("clone106", "clone105")
    text = text.replace("v106", "v105")
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
    residual = re.findall(r"v105|105th|ref105|clone105", derived)
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
