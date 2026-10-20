#!/usr/bin/env python3
"""Derive the 95th standing-checks pair from the v94 pair.

Three token families (the documented derivation protocol):
  1. v94 -> v95            (version tokens)
  2. 94th -> 95th          (ordinal tokens)
  3. ref94 -> ref95 / clone94 -> clone95   (bare session names)

After derivation, normalize BACK (v95->v94 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v94.sh",
     "scripts/parity-probes/ref-standing-v95.sh"),
    ("scripts/parity-probes/standing-checks-v94.sh",
     "scripts/parity-probes/standing-checks-v95.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("94th" -> "95th"), then bare session names, then version
    text = text.replace("94th", "95th")
    text = text.replace("ref94", "ref95")
    text = text.replace("clone94", "clone95")
    text = text.replace("v94", "v95")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("95th", "94th")
    text = text.replace("ref95", "ref94")
    text = text.replace("clone95", "clone94")
    text = text.replace("v95", "v94")
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
    residual = re.findall(r"v94|94th|ref94|clone94", derived)
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
