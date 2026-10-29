#!/usr/bin/env python3
"""Derive the 127th standing-checks pair from the v126 pair.

Three token families (the documented derivation protocol):
  1. v126 -> v127           (version tokens)
  2. 126th -> 127th         (ordinal tokens — a th->th plain replace,
                             the same plain-replace form as v128's
                             121st->122nd, v130's 123rd->124th, v131's
                             124th->125th, and v132's 125th->126th)
  3. ref126 -> ref127 / clone126 -> clone127   (bare session names)

After derivation, normalize BACK (v127->v126 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v126.sh",
     "scripts/parity-probes/ref-standing-v127.sh"),
    ("scripts/parity-probes/standing-checks-v126.sh",
     "scripts/parity-probes/standing-checks-v127.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("126th" -> "127th"), then bare session names, then version
    text = text.replace("126th", "127th")
    text = text.replace("ref126", "ref127")
    text = text.replace("clone126", "clone127")
    text = text.replace("v126", "v127")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("127th", "126th")
    text = text.replace("ref127", "ref126")
    text = text.replace("clone127", "clone126")
    text = text.replace("v127", "v126")
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
    residual = re.findall(r"v126|126th|ref126|clone126", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        subprocess.run(["bash", "-n", dst], check=True)
    print("OK: bash -n clean on both halves")
