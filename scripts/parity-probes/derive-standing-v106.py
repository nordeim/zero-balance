#!/usr/bin/env python3
"""Derive the 100th standing-checks pair from the v99 pair.

Three token families (the documented derivation protocol):
  1. v99 -> v100           (version tokens)
  2. 99th -> 100th         (ordinal tokens)
  3. ref99 -> ref100 / clone99 -> clone100   (bare session names)

After derivation, normalize BACK (v100->v99 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (ref99/clone99 would otherwise be
partially rewritten by the v99->v100 swap).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v99.sh",
     "scripts/parity-probes/ref-standing-v100.sh"),
    ("scripts/parity-probes/standing-checks-v99.sh",
     "scripts/parity-probes/standing-checks-v100.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("99th" -> "100th"), then bare session names, then version
    text = text.replace("99th", "100th")
    text = text.replace("ref99", "ref100")
    text = text.replace("clone99", "clone100")
    text = text.replace("v99", "v100")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("100th", "99th")
    text = text.replace("ref100", "ref99")
    text = text.replace("clone100", "clone99")
    text = text.replace("v100", "v99")
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
    residual = re.findall(r"v99|99th|ref99|clone99", derived)
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
