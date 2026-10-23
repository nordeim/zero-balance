#!/usr/bin/env python3
"""Derive the 101st standing-checks pair from the v100 pair.

Three token families (the documented derivation protocol):
  1. v100 -> v101           (version tokens)
  2. 100th -> 101st         (ordinal tokens)
  3. ref100 -> ref101 / clone100 -> clone101   (bare session names)

After derivation, normalize BACK (v101->v100 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v100.sh",
     "scripts/parity-probes/ref-standing-v101.sh"),
    ("scripts/parity-probes/standing-checks-v100.sh",
     "scripts/parity-probes/standing-checks-v101.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("100th" -> "101st"), then bare session names, then version
    text = text.replace("100th", "101st")
    text = text.replace("ref100", "ref101")
    text = text.replace("clone100", "clone101")
    text = text.replace("v100", "v101")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("101st", "100th")
    text = text.replace("ref101", "ref100")
    text = text.replace("clone101", "clone100")
    text = text.replace("v101", "v100")
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
    residual = re.findall(r"v100|100th|ref100|clone100", derived)
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
