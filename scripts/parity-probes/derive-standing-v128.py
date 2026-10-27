#!/usr/bin/env python3
"""Derive the 122nd standing-checks pair from the v121 pair.

Three token families (the documented derivation protocol):
  1. v121 -> v122           (version tokens)
  2. 121st -> 122nd         (ordinal tokens — the st->nd suffix transition,
                             the same plain-replace form as v107's 100th->101st
                             and v127's 120th->121st)
  3. ref121 -> ref122 / clone121 -> clone122   (bare session names)

After derivation, normalize BACK (v122->v121 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v121.sh",
     "scripts/parity-probes/ref-standing-v122.sh"),
    ("scripts/parity-probes/standing-checks-v121.sh",
     "scripts/parity-probes/standing-checks-v122.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("121st" -> "122nd"), then bare session names, then version
    text = text.replace("121st", "122nd")
    text = text.replace("ref121", "ref122")
    text = text.replace("clone121", "clone122")
    text = text.replace("v121", "v122")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("122nd", "121st")
    text = text.replace("ref122", "ref121")
    text = text.replace("clone122", "clone121")
    text = text.replace("v122", "v121")
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
    residual = re.findall(r"v121|121st|ref121|clone121", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if ok:
    print("OK: both halves derived; version-bump-only verified by normalize-back diff; zero old tokens remaining")
    for _, dst in PAIR:
        r = subprocess.run(["bash", "-n", dst], capture_output=True, text=True)
        print(f"bash -n {dst}: {'clean' if r.returncode == 0 else r.stderr}")
