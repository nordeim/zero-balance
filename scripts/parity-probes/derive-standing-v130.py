#!/usr/bin/env python3
"""Derive the 124th standing-checks pair from the v123 pair.

Three token families (the documented derivation protocol):
  1. v123 -> v124           (version tokens)
  2. 123rd -> 124th         (ordinal tokens — the rd->th suffix transition,
                             the same plain-replace form as v107's 100th->101st,
                             v128's 121st->122nd, and v129's 122nd->123rd)
  3. ref123 -> ref124 / clone123 -> clone124   (bare session names)

After derivation, normalize BACK (v124->v123 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v123.sh",
     "scripts/parity-probes/ref-standing-v124.sh"),
    ("scripts/parity-probes/standing-checks-v123.sh",
     "scripts/parity-probes/standing-checks-v124.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("123rd" -> "124th"), then bare session names, then version
    text = text.replace("123rd", "124th")
    text = text.replace("ref123", "ref124")
    text = text.replace("clone123", "clone124")
    text = text.replace("v123", "v124")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("124th", "123rd")
    text = text.replace("ref124", "ref123")
    text = text.replace("clone124", "clone123")
    text = text.replace("v124", "v123")
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
    residual = re.findall(r"v123|123rd|ref123|clone123", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        subprocess.run(["bash", "-n", dst], check=True)
    print("OK: bash -n clean on both halves")
