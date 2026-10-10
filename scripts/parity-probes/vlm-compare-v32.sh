#!/usr/bin/env bash
# v32: VLM visual pairs — the dashboard + the calculator (this session's
# surface). Both verdicts' flags were DOM-explained (the Dashboard-active
# rail = superset #3; the X's open-state ring = the v29 Radix superset).
# Prereq: ref-*.png captured on the reference session; clone-*.png captured
# on the clone (login + navigate inside ONE with-server.sh invocation).
set -u
DIR=/tmp/vlm32
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
run_pair calculator "Compare these two screenshots of the same budget-planner app's expense-category Calculator modal dialog: IMAGE 1 is the reference/original site, IMAGE 2 is a clone. The two sites hold DIFFERENT demo data by design — IGNORE all data/text-content differences (category names, amounts). Focus ONLY on LAYOUT and CHROME: the dialog geometry (centered card, rounded corners, border, shadow), header with title + X-close, the icon + empty-state message, the Line Items section with its Add Item button, footer buttons, spacing, typography. Answer with VERDICT: IDENTICAL or DIFFERENT, then a one-line layout description, then list ANY layout-level differences (or 'none')."
