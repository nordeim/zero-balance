#!/usr/bin/env bash
# v20 session: VLM visual sweep — compares screenshot pairs through z-ai vision
# with a layout-focused prompt (data differences excluded by instruction).
# Usage: vlm-compare-v20.sh <name> [extra-prompt]
# Reads /tmp/vlm20/ref-<name>.png and /tmp/vlm20/clone-<name>.png, writes
# /tmp/vlm20/vlm-<name>.json, prints the verdict content.
set -u
NAME="$1"
EXTRA="${2:-}"
PROMPT="Compare these two screenshots of the same budget-planner app view: IMAGE 1 is the reference/original site, IMAGE 2 is a clone. The two sites hold DIFFERENT demo data by design (different amounts, item names, counts, avatar letters) — IGNORE all data/text-content differences. Also ignore the floating 'Edit with Base44' platform badge if present (platform chrome, not app design). Focus ONLY on LAYOUT and CHROME: structure, arrangement, alignment, spacing, card geometry, header/nav, colors of surfaces, fonts/sizes of headings, badge shapes, empty-state patterns, overflow. Answer with VERDICT: IDENTICAL or DIFFERENT, then a one-line layout description, then list ANY layout-level differences (or 'none'). $EXTRA"
z-ai vision -p "$PROMPT" -i "/tmp/vlm20/ref-$NAME.png" -i "/tmp/vlm20/clone-$NAME.png" -o "/tmp/vlm20/vlm-$NAME.json" >/dev/null 2>&1
python3 - "$NAME" <<'EOF'
import json, sys
name = sys.argv[1]
try:
    d = json.load(open(f"/tmp/vlm20/vlm-{name}.json"))
    print(f"=== {name} ===")
    print(d.get("choices", [{}])[0].get("message", {}).get("content", "NO CONTENT"))
except Exception as e:
    print(f"=== {name} === ERROR: {e}")
EOF
