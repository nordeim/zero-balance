#!/usr/bin/env python3
"""Derive the 144th standing-checks pair from the 143rd pair.

Three token families (the documented derivation protocol):
  1. v143 -> v144           (version tokens)
  2. 143rd -> 144th         (ordinal tokens — an rd->th plain replace,
                             the suffix following the number's English
                             form, the same plain-replace family as the
                             chain's prior st/nd/rd/th transitions, e.g.
                             v122's 121st, v132's 131st, v139's 132nd->
                             133rd, v147's 140th->141st, v148's 141st->
                             142nd and v149's 142nd->143rd: the ordinal
                             is always a single plain replace)
  3. ref143 -> ref144 / clone143 -> clone144   (bare session names)

After derivation, normalize BACK (v144->v143 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import re
import subprocess
import sys

PAIR = [
    ("scripts/parity-probes/ref-standing-v143.sh",
     "scripts/parity-probes/ref-standing-v144.sh"),
    ("scripts/parity-probes/standing-checks-v143.sh",
     "scripts/parity-probes/standing-checks-v144.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("143rd" -> "144th"), then bare session names, then version
    text = text.replace("143rd", "144th")
    text = text.replace("ref143", "ref144")
    text = text.replace("clone143", "clone144")
    text = text.replace("v143", "v144")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("144th", "143rd")
    text = text.replace("ref144", "ref143")
    text = text.replace("clone144", "clone143")
    text = text.replace("v144", "v143")
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
    residual = re.findall(r"v143|143rd|ref143|clone143", derived)
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
for (src, _) in PAIR:
    with open(src, "r", encoding="utf-8") as f:
        src_lines = len(f.read().splitlines())
    print(f"{src}: {src_lines} lines")
for (_, dst) in PAIR:
    with open(dst, "r", encoding="utf-8") as f:
        dst_lines = len(f.read().splitlines())
    print(f"{dst}: {dst_lines} lines")

print("144th standing pair derived clean (ref-standing-v144.sh + standing-checks-v144.sh)")
