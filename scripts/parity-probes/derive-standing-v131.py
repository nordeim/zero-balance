#!/usr/bin/env python3
"""Derive the 125th standing-checks pair from the v124 pair.

Three token families (the documented derivation protocol):
  1. v124 -> v125           (version tokens)
  2. 124th -> 125th         (ordinal tokens — a th->th plain replace,
                             the same plain-replace form as v128's
                             121st->122nd and v130's 123rd->124th)
  3. ref124 -> ref125 / clone124 -> clone125   (bare session names)

After derivation, normalize BACK (v125->v124 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v124.sh",
     "scripts/parity-probes/ref-standing-v125.sh"),
    ("scripts/parity-probes/standing-checks-v124.sh",
     "scripts/parity-probes/standing-checks-v125.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("124th" -> "125th"), then bare session names, then version
    text = text.replace("124th", "125th")
    text = text.replace("ref124", "ref125")
    text = text.replace("clone124", "clone125")
    text = text.replace("v124", "v125")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("125th", "124th")
    text = text.replace("ref125", "ref124")
    text = text.replace("clone125", "clone124")
    text = text.replace("v125", "v124")
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
    residual = re.findall(r"v124|124th|ref124|clone124", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        subprocess.run(["bash", "-n", dst], check=True)
    print("OK: bash -n clean on both halves")
