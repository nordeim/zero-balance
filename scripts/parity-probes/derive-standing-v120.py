#!/usr/bin/env python3
"""Derive the 114th standing-checks pair from the v113 pair.

Three token families (the documented derivation protocol):
  1. v113 -> v114           (version tokens)
  2. 113th -> 114th         (ordinal tokens)
  3. ref113 -> ref114 / clone113 -> clone114   (bare session names)

After derivation, normalize BACK (v114->v113 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v113.sh",
     "scripts/parity-probes/ref-standing-v114.sh"),
    ("scripts/parity-probes/standing-checks-v113.sh",
     "scripts/parity-probes/standing-checks-v114.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("113th" -> "114th"), then bare session names, then version
    text = text.replace("113th", "114th")
    text = text.replace("ref113", "ref114")
    text = text.replace("clone113", "clone114")
    text = text.replace("v113", "v114")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("114th", "113th")
    text = text.replace("ref114", "ref113")
    text = text.replace("clone114", "clone113")
    text = text.replace("v114", "v113")
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
    residual = re.findall(r"v113|113th|ref113|clone113", derived)
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
