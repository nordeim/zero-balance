#!/usr/bin/env python3
"""Derive the 115th standing-checks pair from the v114 pair.

Three token families (the documented derivation protocol):
  1. v114 -> v115           (version tokens)
  2. 114th -> 115th         (ordinal tokens)
  3. ref114 -> ref115 / clone114 -> clone115   (bare session names)

After derivation, normalize BACK (v115->v114 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v114.sh",
     "scripts/parity-probes/ref-standing-v115.sh"),
    ("scripts/parity-probes/standing-checks-v114.sh",
     "scripts/parity-probes/standing-checks-v115.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("114th" -> "115th"), then bare session names, then version
    text = text.replace("114th", "115th")
    text = text.replace("ref114", "ref115")
    text = text.replace("clone114", "clone115")
    text = text.replace("v114", "v115")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("115th", "114th")
    text = text.replace("ref115", "ref114")
    text = text.replace("clone115", "clone114")
    text = text.replace("v115", "v114")
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
    residual = re.findall(r"v114|114th|ref114|clone114", derived)
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
