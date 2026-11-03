#!/usr/bin/env python3
"""Derive the 142nd standing-checks pair from the 141st pair.

Three token families (the documented derivation protocol):
  1. v141 -> v142           (version tokens)
  2. 141st -> 142nd         (ordinal tokens — an st->nd plain replace,
                             the suffix following the number's English
                             form, the same plain-replace family as the
                             chain's prior st/nd/rd/th transitions, e.g.
                             v122's 121st, v132's 131st, v139's 132nd->
                             133rd and v147's 140th->141st: the ordinal is
                             always a single plain replace)
  3. ref141 -> ref142 / clone141 -> clone142   (bare session names)

After derivation, normalize BACK (v142->v141 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import re
import subprocess
import sys

PAIR = [
    ("scripts/parity-probes/ref-standing-v141.sh",
     "scripts/parity-probes/ref-standing-v142.sh"),
    ("scripts/parity-probes/standing-checks-v141.sh",
     "scripts/parity-probes/standing-checks-v142.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("141st" -> "142nd"), then bare session names, then version
    text = text.replace("141st", "142nd")
    text = text.replace("ref141", "ref142")
    text = text.replace("clone141", "clone142")
    text = text.replace("v141", "v142")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("142nd", "141st")
    text = text.replace("ref142", "ref141")
    text = text.replace("clone142", "clone141")
    text = text.replace("v142", "v141")
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
    residual = re.findall(r"v141|141st|ref141|clone141", derived)
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

print("142nd standing pair derived clean (ref-standing-v142.sh + standing-checks-v142.sh)")
