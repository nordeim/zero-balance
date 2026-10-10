#!/usr/bin/env bash
# v33: VLM visual pairs — the dashboard + the verify-email state (this
# session's surface). Both verdicts' flags expected DOM-explained.
set -u
DIR=/tmp/vlm33
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
run_pair verify "Compare these two screenshots of the same budget-planner app's email-verification screen: IMAGE 1 is the reference/original site, IMAGE 2 is a clone. The two sites show DIFFERENT email addresses and hint text by design — IGNORE all text-content differences (emails, hints, dev codes). Focus ONLY on LAYOUT and CHROME: the shield/check circle at top, the 'Verify your email' heading, the 6 digit-input boxes (size, spacing, borders, centered row), the primary verify button, the resend line, the back link at top-left, overall card geometry (width, padding, borders, shadows, background). Answer with VERDICT: IDENTICAL or DIFFERENT, then a one-line layout description, then list ANY layout-level differences (or 'none')."
