#!/usr/bin/env bash
# v29: VLM visual pair — the details sheet. Reads /tmp/vlm29/ref-item-details.png
# and /tmp/vlm29/clone-item-details.png, writes the verdict.
set -u
DIR=/tmp/vlm29
NAME=item-details
PROMPT="Compare these two screenshots of the same budget-planner app's read-only 'Budget Item Details' dialog: IMAGE 1 is the reference/original site, IMAGE 2 is a clone. The two sites hold DIFFERENT demo data by design (different item names, amounts, dates, notes) — IGNORE all data/text-content differences. Focus ONLY on LAYOUT and CHROME: dialog panel geometry and centering, overlay, sticky header with X-close button, the pill badge row, name/amount typography sizes and colors, the tinted classification block, the icon-led fact rows spacing, the Created/Last Updated footer grid, scroll behavior. Answer with VERDICT: IDENTICAL or DIFFERENT, then a one-line layout description, then list ANY layout-level differences (or 'none')."
z-ai vision -p "$PROMPT" -i "$DIR/ref-$NAME.png" -i "$DIR/clone-$NAME.png" -o "$DIR/vlm-$NAME.json" >/dev/null 2>&1
python3 - "$NAME" "$DIR" <<'EOF'
import json, sys
name, d = sys.argv[1], sys.argv[2]
try:
    j = json.load(open(f"{d}/vlm-{name}.json"))
    print(f"=== {name} ===")
    print(j.get("choices", [{}])[0].get("message", {}).get("content", "NO CONTENT"))
except Exception as e:
    print(f"=== {name} === ERROR: {e}")
EOF
