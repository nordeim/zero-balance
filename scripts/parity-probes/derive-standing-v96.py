#!/usr/bin/env python3
"""Derive the 90th standing-checks pair from the v89 pair.

Three token families (the documented derivation protocol):
  1. v89 -> v90            (version tokens)
  2. 89th -> 90th          (ordinal tokens)
  3. ref89 -> ref90 / clone89 -> clone90   (bare session names)

After derivation, normalize BACK (v90->v89 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v89.sh",
     "scripts/parity-probes/ref-standing-v90.sh"),
    ("scripts/parity-probes/standing-checks-v89.sh",
     "scripts/parity-probes/standing-checks-v90.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("89th" -> "90th"), then bare session names, then version
    text = text.replace("89th", "90th")
    text = text.replace("ref89", "ref90")
    text = text.replace("clone89", "clone90")
    text = text.replace("v89", "v90")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("90th", "89th")
    text = text.replace("ref90", "ref89")
    text = text.replace("clone90", "clone89")
    text = text.replace("v90", "v89")
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
    residual = re.findall(r"v89|89th|ref89|clone89", derived)
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
