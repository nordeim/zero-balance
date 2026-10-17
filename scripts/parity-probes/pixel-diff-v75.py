#!/usr/bin/env python3
"""pixel-diff-v75.py — the 07-add-item-modal DATE-class arbitration (the v66
discipline): a programmatic PIL diff localizing the overnight change to the
date input's day-digit region, never a VLM verdict."""
from PIL import Image, ImageChops
import sys

OLD = "/tmp/v75-shots/07-add-item-modal.png"
NEW = "/home/z/my-project/zero-balance/docs/screenshots/07-add-item-modal.png"

old = Image.open(OLD).convert("RGB")
new = Image.open(NEW).convert("RGB")
print(f"old size: {old.size}, new size: {new.size}")
if old.size != new.size:
    print("SIZE MISMATCH — not the DATE class")
    sys.exit(1)

diff = ImageChops.difference(old, new)
bbox = diff.getbbox()
print(f"diff bbox: {bbox}")
if bbox is None:
    print("NO DIFF — byte-stable")
    sys.exit(0)

# the changed-region size + the changed-row histogram
left, top, right, bottom = bbox
print(f"changed region: {right-left}x{bottom-top} px at ({left},{top})-({right},{bottom})")

# count changed pixels (any channel > 0)
bbox_img = diff.crop(bbox)
changed_px = 0
hist_r = bbox_img.histogram()[0:256]
hist_g = bbox_img.histogram()[256:512]
hist_b = bbox_img.histogram()[512:768]
for i in range(256):
    if hist_r[i] or hist_g[i] or hist_b[i]:
        changed_px += 1
# that counts DISTINCT values; count actual pixels instead:
px = bbox_img.load()
nonzero = sum(1 for y in range(bbox_img.size[1]) for x in range(bbox_img.size[0]) if px[x, y] != (0, 0, 0))
print(f"changed pixels (any channel): {nonzero} of {bbox_img.size[0]*bbox_img.size[1]} in region")

# the expected DATE class: a small region (~16-40px wide) inside the dialog's
# date input area on the right half of the frame, everything else byte-stable
w_ok = (right - left) <= 48
h_ok = (bottom - top) <= 40
x_ok = left > 1000  # the date field sits in the dialog's form column (right-of-center at 2x DPR)
print(f"DATE-class verdict: width_ok={w_ok} height_ok={h_ok} x_ok={x_ok}")
if w_ok and h_ok and x_ok:
    print("ARBITRATED: the dialog-default DATE class (the day digits rolled) — documented, never a regression")
else:
    print("REGION OUTSIDE THE DATE FIELD — investigate before accepting")
    sys.exit(1)
