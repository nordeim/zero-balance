#!/usr/bin/env bash
# v34: VLM visual pairs — the dashboard + the forgot-password state (this
# session's surface). Both verdicts' flags expected DOM-explained.
set -u
DIR=/tmp/vlm34
run_pair() {
  local NAME="$1"; local PROMPT="$2"
  z-ai vision -p "$PROMPT" -i "$DIR/ref-$NAME.png" -i "$DIR/clone-$NAME.png" -o "$DIR/vlm-$NAME.json" >/dev/null 2>&1
  python3 - "$NAME" "$DIR" <<'PYEOF'
import json, sys
name, d = sys.argv[1], sys.argv[2]
try:
    j = json.load(open(f"{d}/vlm-{name}.json"))
    print(f"=== {name} ===")
    print(j.get("choices", [{}])[0].get("message", {}).get("content", "NO CONTENT"))
except Exception as e:
    print(f"=== {name} === ERROR: {e}")
PYEOF
}
run_pair dashboard "Compare these two screenshots of the same budget-planner app's dashboard: IMAGE 1 is the reference/original site, IMAGE 2 is a clone. The two sites hold DIFFERENT demo data by design (different numbers/percentages) — IGNORE all data/text-content differences. Focus ONLY on LAYOUT and CHROME: the Net Zero Breakdown card, the Spending Breakdown donut + legend, stat cards, spacing, alignment, borders, shadows, typography sizes, colors of chart sectors and legend icons. Answer with VERDICT: IDENTICAL or DIFFERENT, then a one-line layout description, then list ANY layout-level differences (or 'none')."
run_pair forgot "Compare these two screenshots of the same budget-planner app's forgot-password screen: IMAGE 1 is the reference/original site, IMAGE 2 is a clone. The two sites may show different heading/description text by design — IGNORE text-content differences. Focus ONLY on LAYOUT and CHROME: the back-to-sign-in link at top (arrow icon + text), the heading, the description paragraph, the labeled email input field (icon, border, height, rounded corners, background), the full-width dark submit button (height, color, radius, shadow), overall card geometry (width, padding, borders, shadows, background), spacing and alignment. Answer with VERDICT: IDENTICAL or DIFFERENT, then a one-line layout description, then list ANY layout-level differences (or 'none')."
