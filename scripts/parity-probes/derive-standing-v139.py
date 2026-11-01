#!/usr/bin/env python3
"""Derive the 133rd standing-checks pair from the v132 pair.

Three token families (the documented derivation protocol):
  1. v132 -> v133           (version tokens)
  2. 132nd -> 133rd         (ordinal tokens — an nd->rd plain replace,
                             the same plain-replace form as the chain's
                             prior st/nd/rd transitions, e.g. v101's
                             100th->101st, v137's 130th->131st and v138's
                             131st->132nd: the ordinal is always a single
                             plain replace, the suffix following the
                             number's English form)
  3. ref132 -> ref133 / clone132 -> clone133   (bare session names)

After derivation, normalize BACK (v133->v132 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import re
import subprocess
import sys

PAIR = [
    ("scripts/parity-probes/ref-standing-v132.sh",
     "scripts/parity-probes/ref-standing-v133.sh"),
    ("scripts/parity-probes/standing-checks-v132.sh",
     "scripts/parity-probes/standing-checks-v133.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("132nd" -> "133rd"), then bare session names, then version
    text = text.replace("132nd", "133rd")
    text = text.replace("ref132", "ref133")
    text = text.replace("clone132", "clone133")
    text = text.replace("v132", "v133")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("133rd", "132nd")
    text = text.replace("ref133", "ref132")
    text = text.replace("clone133", "clone132")
    text = text.replace("v133", "v132")
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
    residual = re.findall(r"v132|132nd|ref132|clone132", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if not ok:
    sys.exit(1)

# syntax gates on both halves
for _, dst in PAIR:
    r = subprocess.run(["bash", "-n", dst], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL: bash -n {dst}: {r.stderr}")
        sys.exit(1)

# line-count preservation (the documented contract)
for (src, _), counts in zip(PAIR, [(119,), (74,)]):
    with open(src, "r", encoding="utf-8") as f:
        src_lines = len(f.read().splitlines())
    print(f"{src}: {src_lines} lines")
for (_, dst), counts in zip(PAIR, [(119,), (74,)]):
    with open(dst, "r", encoding="utf-8") as f:
        dst_lines = len(f.read().splitlines())
    print(f"{dst}: {dst_lines} lines")

print("133rd standing pair derived clean (ref-standing-v133.sh + standing-checks-v133.sh)")
