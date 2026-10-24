#!/usr/bin/env python3
"""Derive the 110th standing-checks pair from the v109 pair.

Three token families (the documented derivation protocol):
  1. v109 -> v110           (version tokens)
  2. 109th -> 110th         (ordinal tokens)
  3. ref109 -> ref110 / clone109 -> clone110   (bare session names)

After derivation, normalize BACK (v110->v109 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v109.sh",
     "scripts/parity-probes/ref-standing-v110.sh"),
    ("scripts/parity-probes/standing-checks-v109.sh",
     "scripts/parity-probes/standing-checks-v110.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("109th" -> "110th"), then bare session names, then version
    text = text.replace("109th", "110th")
    text = text.replace("ref109", "ref110")
    text = text.replace("clone109", "clone110")
    text = text.replace("v109", "v110")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("110th", "109th")
    text = text.replace("ref110", "ref109")
    text = text.replace("clone110", "clone109")
    text = text.replace("v110", "v109")
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
    residual = re.findall(r"v109|109th|ref109|clone109", derived)
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
