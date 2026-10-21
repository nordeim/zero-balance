#!/usr/bin/env python3
"""Derive the 97th standing-checks pair from the v96 pair.

Three token families (the documented derivation protocol):
  1. v96 -> v97            (version tokens)
  2. 96th -> 97th          (ordinal tokens)
  3. ref96 -> ref97 / clone96 -> clone97   (bare session names)

After derivation, normalize BACK (v97->v96 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v96.sh",
     "scripts/parity-probes/ref-standing-v97.sh"),
    ("scripts/parity-probes/standing-checks-v96.sh",
     "scripts/parity-probes/standing-checks-v97.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("96th" -> "97th"), then bare session names, then version
    text = text.replace("96th", "97th")
    text = text.replace("ref96", "ref97")
    text = text.replace("clone96", "clone97")
    text = text.replace("v96", "v97")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("97th", "96th")
    text = text.replace("ref97", "ref96")
    text = text.replace("clone97", "clone96")
    text = text.replace("v97", "v96")
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
    residual = re.findall(r"v96|96th|ref96|clone96", derived)
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
