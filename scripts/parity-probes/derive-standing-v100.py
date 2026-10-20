#!/usr/bin/env python3
"""Derive the 94th standing-checks pair from the v93 pair.

Three token families (the documented derivation protocol):
  1. v93 -> v94            (version tokens)
  2. 93rd -> 94th          (ordinal tokens)
  3. ref93 -> ref94 / clone93 -> clone94   (bare session names)

After derivation, normalize BACK (v94->v93 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
"""
import subprocess, sys, re

PAIR = [
    ("scripts/parity-probes/ref-standing-v93.sh",
     "scripts/parity-probes/ref-standing-v94.sh"),
    ("scripts/parity-probes/standing-checks-v93.sh",
     "scripts/parity-probes/standing-checks-v94.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("93rd" -> "94th"), then bare session names, then version
    text = text.replace("93rd", "94th")
    text = text.replace("ref93", "ref94")
    text = text.replace("clone93", "clone94")
    text = text.replace("v93", "v94")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("94th", "93rd")
    text = text.replace("ref94", "ref93")
    text = text.replace("clone94", "clone93")
    text = text.replace("v94", "v93")
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
    residual = re.findall(r"v93|93rd|ref93|clone93", derived)
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
