#!/usr/bin/env python3
"""Derive the 117th standing-checks pair from the v116 pair.

Three token families (the documented derivation protocol):
  1. v116 -> v117            (version tokens)
  2. 116th -> 117th          (ordinal tokens)
  3. ref116 -> ref117 / clone116 -> clone117  (bare session names)

After derivation, normalize BACK (v117->v116 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v116.sh",
     "scripts/parity-probes/ref-standing-v117.sh"),
    ("scripts/parity-probes/standing-checks-v116.sh",
     "scripts/parity-probes/standing-checks-v117.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("116th" -> "117th"), then bare session names, then version
    text = text.replace("116th", "117th")
    text = text.replace("ref116", "ref117")
    text = text.replace("clone116", "clone117")
    text = text.replace("v116", "v117")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("117th", "116th")
    text = text.replace("ref117", "ref116")
    text = text.replace("clone117", "clone116")
    text = text.replace("v117", "v116")
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
    residual = re.findall(r"v116|116th|ref116|clone116", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        r = subprocess.run(["bash", "-n", dst], capture_output=True, text=True)
        print(f"bash -n {dst}: {'clean' if r.returncode == 0 else r.stderr}")
