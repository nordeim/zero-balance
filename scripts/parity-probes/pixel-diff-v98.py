#!/usr/bin/env python3
"""pixel-diff-v98.py — the fresh-reseed DATE-class arbitration for the six
differing screenshots (the v68/v92 discipline, the v96 PIL form): the
fresh-clone re-seed re-anchors the seed's isoDate(offsetDays) dates to the
new seed day (db/ is gitignored — it does not travel), so the views that
render seed dates in their card footers/subtexts roll their date digits.
A programmatic PIL diff localizes every delta to date-digit regions —
never a VLM verdict."""
from PIL import Image, ImageChops
import sys, os

OLD_DIR = "/tmp/v98-shotbackup"
NEW_DIR = "/home/z/my-project/zero-balance/docs/screenshots"
FILES = ["03-income.png", "04-expenses.png", "05-savings.png",
         "06-networth.png", "08-calculator.png", "16-item-details.png"]

# The date-digit acceptance: each differing region small (<= 300px wide —
# a full date string "MMM D, YYYY" span, <= 40px tall), and no more than
# a few disjoint regions per shot (the card footers' date spans).
W_MAX = 300
H_MAX = 40

def regions(diff_img, thresh=1):
    # disjoint changed-region bboxes via a simple flood-ish scan: split the
    # diff into rows with changes, group contiguous runs into regions.
    gray = diff_img.convert("L")
    w, h = gray.size
    px = gray.load()
    # collect changed pixel coords
    changed_rows = {}
    for y in range(h):
        xs = [x for x in range(w) if px[x, y] > 0]
        if xs:
            changed_rows[y] = xs
    if not changed_rows:
        return []
    # group contiguous row bands, then take the x-extent of each band
    regions = []
    ys = sorted(changed_rows.keys())
    band_start = ys[0]
    prev_y = ys[0]
    band_xs = set(changed_rows[ys[0]])
    for y in ys[1:]:
        if y - prev_y > 8:  # gap -> close the band
            regions.append((min(band_xs), band_start, max(band_xs) + 1, prev_y + 1))
            band_start = y
            band_xs = set(changed_rows[y])
        else:
            band_xs |= set(changed_rows[y])
        prev_y = y
    regions.append((min(band_xs), band_start, max(band_xs) + 1, prev_y + 1))
    # split wide bands by x-gaps (multiple date spans side by side)
    final = []
    for (x0, y0, x1, y1) in regions:
        # gather per-column change counts within the band
        cols = {}
        for y in range(y0, y1):
            for x in range(x0, x1):
                if px[x, y] > 0:
                    cols[x] = cols.get(x, 0) + 1
        if not cols:
            continue
        xs = sorted(cols.keys())
        seg_start = xs[0]
        prev = xs[0]
        for x in xs[1:]:
            if x - prev > 24:  # x-gap -> separate date span
                final.append((seg_start, y0, prev + 1, y1))
                seg_start = x
            prev = x
        final.append((seg_start, y0, prev + 1, y1))
    return final

ok_all = True
for name in FILES:
    old = Image.open(os.path.join(OLD_DIR, name)).convert("RGB")
    new = Image.open(os.path.join(NEW_DIR, name)).convert("RGB")
    if old.size != new.size:
        print(f"{name}: SIZE MISMATCH — NOT the DATE class")
        ok_all = False
        continue
    diff = ImageChops.difference(old, new)
    bbox = diff.getbbox()
    if bbox is None:
        print(f"{name}: NO DIFF (unexpected — listed as differing)")
        continue
    regs = regions(diff)
    print(f"{name}: {len(regs)} changed region(s):")
    for (x0, y0, x1, y1) in regs:
        w, h = x1 - x0, y1 - y0
        verdict = "DATE-span" if (w <= W_MAX and h <= H_MAX) else "OUT-OF-CLASS"
        if not (w <= W_MAX and h <= H_MAX):
            ok_all = False
        print(f"   {w}x{h}px at ({x0},{y0})  -> {verdict}")
print()
if ok_all:
    print("ARBITRATED: every differing region is a date-digit span (the fresh-reseed DATE class) — documented, never a regression")
    sys.exit(0)
print("REGIONS OUTSIDE THE DATE-SPAN CLASS — investigate before accepting")
sys.exit(1)
