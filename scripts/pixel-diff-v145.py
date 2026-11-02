#!/usr/bin/env python3
"""pixel-diff-v145.py — locate the differing region between HEAD's and the
fresh capture of 07-add-item-modal.png (the v144 diagnosis form)."""
from PIL import Image
import sys

a = Image.open("/tmp/shot07-head.png").convert("RGBA")
b = Image.open(sys.argv[1] if len(sys.argv) > 1 else "docs/screenshots/07-add-item-modal.png").convert("RGBA")
print("sizes:", a.size, b.size)

if a.size != b.size:
    print("DIMENSION MISMATCH — full re-render difference")
    sys.exit(0)

import numpy as np
na = np.array(a)
nb = np.array(b)
diff = np.any(na != nb, axis=2)
count = int(diff.sum())
print("differing pixels:", count)
if count > 0:
    ys, xs = np.where(diff)
    print("bbox: x", int(xs.min()), "-", int(xs.max()), " y", int(ys.min()), "-", int(ys.max()))
    # crop the diff region (with padding) from both for inspection
    pad = 40
    x0, x1 = max(0, int(xs.min()) - pad), min(a.size[0], int(xs.max()) + pad)
    y0, y1 = max(0, int(ys.min()) - pad), min(a.size[1], int(ys.max()) + pad)
    a.crop((x0, y0, x1, y1)).save("/tmp/diff-head.png")
    b.crop((x0, y0, x1, y1)).save("/tmp/diff-fresh.png")
    print("crops saved: /tmp/diff-head.png + /tmp/diff-fresh.png (region x %d-%d y %d-%d)" % (x0, x1, y0, y1))
