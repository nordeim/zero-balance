#!/usr/bin/env python3
"""Derive the 147th standing-checks pair from the 146th pair (the cycle-v153
standing checks — the files carry the ORDINAL as their version token: the
146th pair ran in cycle v152, the 147th pair runs in cycle v153).

Three token families (the documented derivation protocol):
  1. v146 -> v147           (version tokens — the ordinal-as-version form)
  2. 146th -> 147th         (ordinal tokens — a th->th plain replace,
                             the suffix following the number's English
                             form, the same plain-replace family as the
                             chain's prior st/nd/rd/th transitions, e.g.
                             v122's 121st, v132's 131st, v139's 132nd->
                             133rd, v147's 140th->141st, v148's 141st->
                             142nd, v149's 142nd->143rd, v150's 143th->
                             144th, v151's 144th->145th and v152's 145th->
                             146th: the ordinal is always a single plain
                             replace)
  3. ref146 -> ref147 / clone146 -> clone147   (bare session names)

After derivation, normalize BACK (v153->v152 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import re
import subprocess
import sys

PAIR = [
    ("scripts/parity-probes/ref-standing-v146.sh",
     "scripts/parity-probes/ref-standing-v147.sh"),
    ("scripts/parity-probes/standing-checks-v146.sh",
     "scripts/parity-probes/standing-checks-v147.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("146th" -> "147th"), then bare session names, then version
    text = text.replace("146th", "147th")
    text = text.replace("ref146", "ref147")
    text = text.replace("clone146", "clone147")
    text = text.replace("v146", "v147")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("147th", "146th")
    text = text.replace("ref147", "ref146")
    text = text.replace("clone147", "clone146")
    text = text.replace("v147", "v146")
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
    residual = re.findall(r"v146|146th|ref146|clone146", derived)
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

print("147th standing pair derived clean (ref-standing-v153.sh + standing-checks-v153.sh)")
