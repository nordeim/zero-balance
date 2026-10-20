#!/usr/bin/env python3
"""pixel-diff-v96.py — the 07-add-item-modal DATE-class arbitration (the
v66/v75 discipline): a programmatic PIL diff localizing the overnight
change to the date input's day-digit region, never a VLM verdict. The
v96 cycle crosses the UTC midnight boundary (the seed + the baseline
shots Oct 19 22:41 UTC; the regeneration Oct 20 00:1x UTC) — the Add
Item form's default date (budget-item-dialog.tsx:83, todayIso()) rolls
'2026-10-19' -> '2026-10-20'."""
from PIL import Image, ImageChops
import sys

OLD = "/tmp/shots-v95-baseline/07-add-item-modal.png"
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

left, top, right, bottom = bbox
print(f"changed region: {right-left}x{bottom-top} px at ({left},{top})-({right},{bottom})")

bbox_img = diff.crop(bbox)
hist = bbox_img.convert("L").histogram()
changed = sum(hist[1:])
total = bbox_img.size[0] * bbox_img.size[1]
print(f"changed pixels: {changed}/{total} in the bbox ({100.0*changed/total:.1f}%)")

# The DATE-class acceptance (the v75 form): a small region (<= 48px wide,
# <= 40px tall) inside the dialog's form column (right-of-center at the
# 2x DPR shot), everything else byte-stable. The day digits '19'->'20'.
w_ok = (right - left) <= 48
h_ok = (bottom - top) <= 40
x_ok = left > 1000
print(f"DATE-class verdict: width_ok={w_ok} height_ok={h_ok} x_ok={x_ok}")
if w_ok and h_ok and x_ok:
    print("ARBITRATED: the dialog-default DATE class (the day digits rolled) — documented, never a regression")
    sys.exit(0)
print("REGION OUTSIDE THE DATE FIELD — investigate before accepting")
sys.exit(1)
