#!/usr/bin/env python3
"""Derive the 107th standing-checks pair from the v106 pair.

Three token families (the documented derivation protocol):
  1. v106 -> v107           (version tokens)
  2. 106th -> 107th         (ordinal tokens)
  3. ref106 -> ref107 / clone106 -> clone107   (bare session names)

After derivation, normalize BACK (v107->v106 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v106.sh",
     "scripts/parity-probes/ref-standing-v107.sh"),
    ("scripts/parity-probes/standing-checks-v106.sh",
     "scripts/parity-probes/standing-checks-v107.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("106th" -> "107th"), then bare session names, then version
    text = text.replace("106th", "107th")
    text = text.replace("ref106", "ref107")
    text = text.replace("clone106", "clone107")
    text = text.replace("v106", "v107")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("107th", "106th")
    text = text.replace("ref107", "ref106")
    text = text.replace("clone107", "clone106")
    text = text.replace("v107", "v106")
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
    residual = re.findall(r"v106|106th|ref106|clone106", derived)
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
