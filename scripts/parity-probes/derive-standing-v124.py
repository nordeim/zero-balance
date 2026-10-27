#!/usr/bin/env python3
"""Derive the 118th standing-checks pair from the v117 pair.

Three token families (the documented derivation protocol):
  1. v117 -> v118            (version tokens)
  2. 117th -> 118th          (ordinal tokens)
  3. ref117 -> ref118 / clone117 -> clone118  (bare session names)

After derivation, normalize BACK (v118->v117 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v117.sh",
     "scripts/parity-probes/ref-standing-v118.sh"),
    ("scripts/parity-probes/standing-checks-v117.sh",
     "scripts/parity-probes/standing-checks-v118.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("117th" -> "118th"), then bare session names, then version
    text = text.replace("117th", "118th")
    text = text.replace("ref117", "ref118")
    text = text.replace("clone117", "clone118")
    text = text.replace("v117", "v118")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("118th", "117th")
    text = text.replace("ref118", "ref117")
    text = text.replace("clone118", "clone117")
    text = text.replace("v118", "v117")
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
    residual = re.findall(r"v117|117th|ref117|clone117", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        r = subprocess.run(["bash", "-n", dst], capture_output=True, text=True)
        print(f"bash -n {dst}: {'clean' if r.returncode == 0 else r.stderr}")
