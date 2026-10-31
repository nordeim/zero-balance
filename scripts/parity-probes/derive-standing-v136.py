#!/usr/bin/env python3
"""Derive the 130th standing-checks pair from the v129 pair.

Three token families (the documented derivation protocol):
  1. v129 -> v130           (version tokens)
  2. 129th -> 130th         (ordinal tokens — a th->th plain replace,
                             the same plain-replace form as v128's
                             121st->122nd, v130's 123rd->124th, v131's
                             124th->125th, v132's 125th->126th, v133's
                             126th->127th, v134's 127th->128th, and
                             v135's 128th->129th)
  3. ref129 -> ref130 / clone129 -> clone130   (bare session names)

After derivation, normalize BACK (v130->v129 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v129.sh",
     "scripts/parity-probes/ref-standing-v130.sh"),
    ("scripts/parity-probes/standing-checks-v129.sh",
     "scripts/parity-probes/standing-checks-v130.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("129th" -> "130th"), then bare session names, then version
    text = text.replace("129th", "130th")
    text = text.replace("ref129", "ref130")
    text = text.replace("clone129", "clone130")
    text = text.replace("v129", "v130")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("130th", "129th")
    text = text.replace("ref130", "ref129")
    text = text.replace("clone130", "clone129")
    text = text.replace("v130", "v129")
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
    residual = re.findall(r"v129|129th|ref129|clone129", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        subprocess.run(["bash", "-n", dst], check=True)
    print("OK: bash -n clean on both halves")
