#!/usr/bin/env python3
"""Derive the 126th standing-checks pair from the v125 pair.

Three token families (the documented derivation protocol):
  1. v125 -> v126           (version tokens)
  2. 125th -> 126th         (ordinal tokens — a th->th plain replace,
                             the same plain-replace form as v128's
                             121st->122nd, v130's 123rd->124th, and
                             v131's 124th->125th)
  3. ref125 -> ref126 / clone125 -> clone126   (bare session names)

After derivation, normalize BACK (v126->v125 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v125.sh",
     "scripts/parity-probes/ref-standing-v126.sh"),
    ("scripts/parity-probes/standing-checks-v125.sh",
     "scripts/parity-probes/standing-checks-v126.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("125th" -> "126th"), then bare session names, then version
    text = text.replace("125th", "126th")
    text = text.replace("ref125", "ref126")
    text = text.replace("clone125", "clone126")
    text = text.replace("v125", "v126")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("126th", "125th")
    text = text.replace("ref126", "ref125")
    text = text.replace("clone126", "clone125")
    text = text.replace("v126", "v125")
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
    residual = re.findall(r"v125|125th|ref125|clone125", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        subprocess.run(["bash", "-n", dst], check=True)
    print("OK: bash -n clean on both halves")
