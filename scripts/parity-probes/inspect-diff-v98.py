#!/usr/bin/env python3
"""inspect-diff-v98.py — magnify the two out-of-class diffs (08-calculator,
16-item-details): channel magnitude histogram + side-by-side crops saved
for visual arbitration."""
from PIL import Image, ImageChops
import os

CASES = [
    ("08-calculator.png", [(2208, 824, 2285, 901)]),
    ("16-item-details.png", [(678, 822, 770, 901), (2187, 822, 2285, 901)]),
]
OLD_DIR = "/tmp/v98-shotbackup"
NEW_DIR = "/home/z/my-project/zero-balance/docs/screenshots"

for name, boxes in CASES:
    old = Image.open(os.path.join(OLD_DIR, name)).convert("RGB")
    new = Image.open(os.path.join(NEW_DIR, name)).convert("RGB")
    diff = ImageChops.difference(old, new)
    print(f"=== {name} ===")
    for (x0, y0, x1, y1) in boxes:
        crop = diff.crop((x0, y0, x1, y1))
        # channel magnitude stats
        maxc = 0
        hist = {}
        px = crop.load()
        for y in range(crop.size[1]):
            for x in range(crop.size[0]):
                r, g, b = px[x, y]
                m = max(r, g, b)
                if m > 0:
                    hist[m] = hist.get(m, 0) + 1
                    maxc = max(maxc, m)
        total = crop.size[0] * crop.size[1]
        changed = sum(hist.values())
        print(f"  region ({x0},{y0})-({x1},{y1}): {changed}/{total} px changed, max channel {maxc}")
        top = sorted(hist.items(), key=lambda kv: -kv[1])[:8]
        print(f"    top magnitudes: {top}")
        # side-by-side crop, 3x zoom
        o = old.crop((x0 - 10, y0 - 10, x1 + 10, y1 + 10))
        n = new.crop((x0 - 10, y0 - 10, x1 + 10, y1 + 10))
        d = crop.crop((0, 0, crop.size[0], crop.size[1]))
        z = 3
        o = o.resize((o.size[0] * z, o.size[1] * z), Image.NEAREST)
        n = n.resize((n.size[0] * z, n.size[1] * z), Image.NEAREST)
        d = d.resize((d.size[0] * z, d.size[1] * z), Image.NEAREST)
        combo = Image.new("RGB", (o.size[0] + n.size[0] + d.size[0] + 20, o.size[1]), (255, 0, 255))
        combo.paste(o, (0, 0))
        combo.paste(n, (o.size[0] + 10, 0))
        combo.paste(d, (o.size[0] + n.size[0] + 20, 0))
        out = f"/tmp/v98-inspect-{name.replace('.png','')}-{x0}-{y0}.png"
        combo.save(out)
        print(f"    saved {out} (old | new | diff, 3x)")
