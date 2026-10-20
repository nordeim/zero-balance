#!/usr/bin/env python3
"""Derive the 93rd standing-checks pair from the v92 pair.

Three token families (the documented derivation protocol):
  1. v92 -> v93            (version tokens)
  2. 92nd -> 93rd          (ordinal tokens)
  3. ref92 -> ref93 / clone92 -> clone93   (bare session names)

After derivation, normalize BACK (v93->v92 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v92.sh",
     "scripts/parity-probes/ref-standing-v93.sh"),
    ("scripts/parity-probes/standing-checks-v92.sh",
     "scripts/parity-probes/standing-checks-v93.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("92nd" -> "93rd"), then bare session names, then version
    text = text.replace("92nd", "93rd")
    text = text.replace("ref92", "ref93")
    text = text.replace("clone92", "clone93")
    text = text.replace("v92", "v93")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("93rd", "92nd")
    text = text.replace("ref93", "ref92")
    text = text.replace("clone93", "clone92")
    text = text.replace("v93", "v92")
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
    residual = re.findall(r"v92|92nd|ref92|clone92", derived)
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
