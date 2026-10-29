#!/usr/bin/env python3
"""Derive the 128th standing-checks pair from the v127 pair.

Three token families (the documented derivation protocol):
  1. v127 -> v128           (version tokens)
  2. 127th -> 128th         (ordinal tokens — a th->th plain replace,
                             the same plain-replace form as v128's
                             121st->122nd, v130's 123rd->124th, v131's
                             124th->125th, v132's 125th->126th, and
                             v133's 126th->127th)
  3. ref127 -> ref128 / clone127 -> clone128   (bare session names)

After derivation, normalize BACK (v128->v127 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v127.sh",
     "scripts/parity-probes/ref-standing-v128.sh"),
    ("scripts/parity-probes/standing-checks-v127.sh",
     "scripts/parity-probes/standing-checks-v128.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("127th" -> "128th"), then bare session names, then version
    text = text.replace("127th", "128th")
    text = text.replace("ref127", "ref128")
    text = text.replace("clone127", "clone128")
    text = text.replace("v127", "v128")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("128th", "127th")
    text = text.replace("ref128", "ref127")
    text = text.replace("clone128", "clone127")
    text = text.replace("v128", "v127")
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
    residual = re.findall(r"v127|127th|ref127|clone127", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        subprocess.run(["bash", "-n", dst], check=True)
    print("OK: bash -n clean on both halves")
