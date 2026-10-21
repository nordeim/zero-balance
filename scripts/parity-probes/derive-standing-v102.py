#!/usr/bin/env python3
"""Derive the 96th standing-checks pair from the v95 pair.

Three token families (the documented derivation protocol):
  1. v95 -> v96            (version tokens)
  2. 95th -> 96th          (ordinal tokens)
  3. ref95 -> ref96 / clone95 -> clone96   (bare session names)

After derivation, normalize BACK (v96->v95 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v95.sh",
     "scripts/parity-probes/ref-standing-v96.sh"),
    ("scripts/parity-probes/standing-checks-v95.sh",
     "scripts/parity-probes/standing-checks-v96.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("95th" -> "96th"), then bare session names, then version
    text = text.replace("95th", "96th")
    text = text.replace("ref95", "ref96")
    text = text.replace("clone95", "clone96")
    text = text.replace("v95", "v96")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("96th", "95th")
    text = text.replace("ref96", "ref95")
    text = text.replace("clone96", "clone95")
    text = text.replace("v96", "v95")
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
    residual = re.findall(r"v95|95th|ref95|clone95", derived)
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
