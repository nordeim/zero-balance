#!/usr/bin/env bash
# clone side of vlm-shots-v55.sh — the same two surfaces at 390x844 from
# the clone's standalone server (:3200, with-server boots fresh). The
# calculator dialog's with-row state (the expense view's Rent card →
# Calculate) + the savings goal card (the v55 F1 surface).
set -u
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm55"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1

# PAIR 1: the calculator dialog's with-row state (the Rent card).
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div')].filter(d => /rounded/.test(d.className||'') && d.querySelector('h4') && /Rent|Grocery/i.test(d.textContent||'')).sort((a,b) => a.getBoundingClientRect().y - b.getBoundingClientRect().y)[0];
  if (!card) return 'no card';
  const btn = [...card.querySelectorAll('button')].find(b => /Calculate/i.test(b.textContent||''));
  if (!btn) return 'no calculate button';
  btn.click();
  return 'calculator clicked';
})()" 2>/dev/null | tail -1
sleep 3
agent-browser screenshot /tmp/vlm55/clone-calculator.png 2>/dev/null | tail -1
agent-browser eval "(async () => {
  const layer = [...document.querySelectorAll('div')].find(d => d.className && d.className.toString().includes('fixed inset-0') && (d.textContent||'').includes('Total Calculated'));
  if (!layer) return 'no layer';
  const closeBtn = [...layer.querySelectorAll('button')].filter(b => !b.textContent.trim())[0];
  if (closeBtn) { closeBtn.click(); return 'closed'; }
  return 'no close';
})()" 2>/dev/null | tail -1

# PAIR 2: the savings goal card (the v55 F1 surface).
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 3
agent-browser screenshot /tmp/vlm55/clone-savings.png 2>/dev/null | tail -1
echo "clone shots done"
EOF
