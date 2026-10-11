#!/usr/bin/env bash
# v45: reference-side driver — the items-view CARD census at 1280 (/income
# + /expenses) and the CALCULATOR row census + hover at 640 (the queue's
# three surfaces). Read-only discipline: NO data mutations on the
# reference (the calculator is only OPENED, its rows only read + hovered).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="ref45"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4

echo "=== REF items-card census at 1280 — /income ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref45 "$PB/items-card-v45.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF items-card census at 1280 — /expenses (hover-revealed action rows) ==="
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref45 "$PB/items-card-v45.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF calculator row census + hover at 640 ==="
agent-browser set viewport 640 960 >/dev/null 2>&1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
# Open the calculator: click the hover-revealed Calculate button (still
# clickable at opacity 0 — synthetic click fires regardless).
agent-browser eval "(async () => {
  const btn = [...document.querySelectorAll('button')].find((b) => /Calculate/i.test((b.textContent || '').trim()) && b.closest('div[class*=\"rounded\"]'));
  if (!btn) return 'NO CALC BUTTON';
  btn.click();
  return 'clicked';
})()" 2>/dev/null | tail -1
sleep 2
bash "$PB/run-probe.sh" ref45 "$PB/calc-row-v45.mjs" 2>/dev/null | tail -1

# Close the dialog (Escape — read-only restore of the page state).
agent-browser key Escape >/dev/null 2>&1
sleep 1
echo ""
echo "=== REF done (read-only) ==="
