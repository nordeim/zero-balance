#!/usr/bin/env python3
"""Derive the 105th standing-checks pair from the v104 pair.

Three token families (the documented derivation protocol):
  1. v104 -> v105           (version tokens)
  2. 104th -> 105th         (ordinal tokens)
  3. ref104 -> ref105 / clone104 -> clone105   (bare session names)

After derivation, normalize BACK (v105->v104 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v104.sh",
     "scripts/parity-probes/ref-standing-v105.sh"),
    ("scripts/parity-probes/standing-checks-v104.sh",
     "scripts/parity-probes/standing-checks-v105.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("104th" -> "105th"), then bare session names, then version
    text = text.replace("104th", "105th")
    text = text.replace("ref104", "ref105")
    text = text.replace("clone104", "clone105")
    text = text.replace("v104", "v105")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("105th", "104th")
    text = text.replace("ref105", "ref104")
    text = text.replace("clone105", "clone104")
    text = text.replace("v105", "v104")
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
    residual = re.findall(r"v104|104th|ref104|clone104", derived)
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
