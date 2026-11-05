#!/usr/bin/env python3
"""Derive the 148th standing-checks pair from the 147th pair (the cycle-v154
standing checks — the files carry the ORDINAL as their version token: the
147th pair ran in cycle v153, the 148th pair runs in cycle v154).

Three token families (the documented derivation protocol):
  1. v147 -> v148           (version tokens — the ordinal-as-version form)
  2. 147th -> 148th         (ordinal tokens — a th->th plain replace,
                             the suffix following the number's English
                             form, the same plain-replace family as the
                             chain's prior st/nd/rd/th transitions, e.g.
                             v122's 121st, v132's 131st, v139's 132nd->
                             133rd, v147's 140th->141st, v148's 141st->
                             142nd, v149's 142nd->143rd, v150's 143th->
                             144th, v151's 144th->145th, v152's 145th->
                             146th and v153's 146th->147th: the ordinal is
                             always a single plain replace)
  3. ref147 -> ref148 / clone147 -> clone148   (bare session names)

After derivation, normalize BACK (v148->v147 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import re
import subprocess
import sys

PAIR = [
    ("scripts/parity-probes/ref-standing-v147.sh",
     "scripts/parity-probes/ref-standing-v148.sh"),
    ("scripts/parity-probes/standing-checks-v147.sh",
     "scripts/parity-probes/standing-checks-v148.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("147th" -> "148th"), then bare session names, then version
    text = text.replace("147th", "148th")
    text = text.replace("ref147", "ref148")
    text = text.replace("clone147", "clone148")
    text = text.replace("v147", "v148")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("148th", "147th")
    text = text.replace("ref148", "ref147")
    text = text.replace("clone148", "clone147")
    text = text.replace("v148", "v147")
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
    residual = re.findall(r"v147|147th|ref147|clone147", derived)
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

print("148th standing pair derived clean (ref-standing-v148.sh + standing-checks-v148.sh)")
