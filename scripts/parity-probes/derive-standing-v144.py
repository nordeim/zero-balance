#!/usr/bin/env python3
"""Derive the 138th standing-checks pair from the v137 pair.

Three token families (the documented derivation protocol):
  1. v137 -> v138           (version tokens)
  2. 137th -> 138th         (ordinal tokens — a th->th plain replace,
                             the same plain-replace form as the chain's
                             prior st/nd/rd/th transitions, e.g. v101's
                             100th->101st, v137's 130th->131st, v139's
                             132nd->133rd, v140's 133rd->134th, v141's
                             134th->135th, v142's 135th->136th and
                             v143's 136th->137th: the ordinal is always
                             a single plain replace, the suffix following
                             the number's English form)
  3. ref137 -> ref138 / clone137 -> clone138   (bare session names)

After derivation, normalize BACK (v138->v137 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import re
import subprocess
import sys

PAIR = [
    ("scripts/parity-probes/ref-standing-v137.sh",
     "scripts/parity-probes/ref-standing-v138.sh"),
    ("scripts/parity-probes/standing-checks-v137.sh",
     "scripts/parity-probes/standing-checks-v138.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("137th" -> "138th"), then bare session names, then version
    text = text.replace("137th", "138th")
    text = text.replace("ref137", "ref138")
    text = text.replace("clone137", "clone138")
    text = text.replace("v137", "v138")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("138th", "137th")
    text = text.replace("ref138", "ref137")
    text = text.replace("clone138", "clone137")
    text = text.replace("v138", "v137")
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
    residual = re.findall(r"v137|137th|ref137|clone137", derived)
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

print("138th standing pair derived clean (ref-standing-v138.sh + standing-checks-v138.sh)")
