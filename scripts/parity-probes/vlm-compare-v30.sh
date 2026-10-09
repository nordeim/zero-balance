#!/usr/bin/env bash
# v30: VLM visual pairs — the dashboard (quick-actions + guidelines region) and
# the mobile details sheet. Reads /tmp/vlm30/{ref,clone}-<name>.png, writes verdicts.
set -u
DIR=/tmp/vlm30

run_pair() {
  local NAME="$1"; local PROMPT="$2"
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
}

run_pair dashboard "Compare these two screenshots of the same budget-planner app's dashboard (scrolled to the quick-action cards and budget-guidelines region): IMAGE 1 is the reference/original site, IMAGE 2 is a clone. The two sites hold DIFFERENT demo data by design (different numbers/percentages) — IGNORE all data/text-content differences. Focus ONLY on LAYOUT and CHROME: the quick-action card buttons (white cards, rounded corners, icon squares, plus icon position), the Budget Guidelines card (tinted rows with colored labels), spacing, alignment, borders, shadows, typography sizes. Answer with VERDICT: IDENTICAL or DIFFERENT, then a one-line layout description, then list ANY layout-level differences (or 'none')."

run_pair mobile-details "Compare these two screenshots of the same budget-planner app's read-only 'Budget Item Details' sheet rendered at MOBILE 390px (bottom-sheet style): IMAGE 1 is the reference/original site, IMAGE 2 is a clone. The two sites hold DIFFERENT demo data by design (different item names, amounts, dates, notes) — IGNORE all data/text-content differences. Focus ONLY on LAYOUT and CHROME: the bottom-sheet geometry (full-width, top rounded corners, bottom-anchored), overlay, sticky header with X-close, the pill badges, the fact rows, the footer action buttons, scroll behavior. Answer with VERDICT: IDENTICAL or DIFFERENT, then a one-line layout description, then list ANY layout-level differences (or 'none')."
