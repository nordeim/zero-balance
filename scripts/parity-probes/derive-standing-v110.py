#!/usr/bin/env python3
"""Derive the 104th standing-checks pair from the v103 pair.

Three token families (the documented derivation protocol):
  1. v103 -> v104           (version tokens)
  2. 103rd -> 104th         (ordinal tokens)
  3. ref103 -> ref104 / clone103 -> clone104   (bare session names)

After derivation, normalize BACK (v104->v103 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v103.sh",
     "scripts/parity-probes/ref-standing-v104.sh"),
    ("scripts/parity-probes/standing-checks-v103.sh",
     "scripts/parity-probes/standing-checks-v104.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("103rd" -> "104th"), then bare session names, then version
    text = text.replace("103rd", "104th")
    text = text.replace("ref103", "ref104")
    text = text.replace("clone103", "clone104")
    text = text.replace("v103", "v104")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("104th", "103rd")
    text = text.replace("ref104", "ref103")
    text = text.replace("clone104", "clone103")
    text = text.replace("v104", "v103")
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
    residual = re.findall(r"v103|103rd|ref103|clone103", derived)
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
