#!/usr/bin/env python3
"""Derive the 98th standing-checks pair from the v97 pair.

Three token families (the documented derivation protocol):
  1. v97 -> v98            (version tokens)
  2. 97th -> 98th          (ordinal tokens)
  3. ref97 -> ref98 / clone97 -> clone98   (bare session names)

After derivation, normalize BACK (v98->v97 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v97.sh",
     "scripts/parity-probes/ref-standing-v98.sh"),
    ("scripts/parity-probes/standing-checks-v97.sh",
     "scripts/parity-probes/standing-checks-v98.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("97th" -> "98th"), then bare session names, then version
    text = text.replace("97th", "98th")
    text = text.replace("ref97", "ref98")
    text = text.replace("clone97", "clone98")
    text = text.replace("v97", "v98")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("98th", "97th")
    text = text.replace("ref98", "ref97")
    text = text.replace("clone98", "clone97")
    text = text.replace("v98", "v97")
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
    residual = re.findall(r"v97|97th|ref97|clone97", derived)
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
