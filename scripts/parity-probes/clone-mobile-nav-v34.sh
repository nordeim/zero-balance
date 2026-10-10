#!/usr/bin/env bash
# v34: clone-side standing checks (28th) — login, R1-R4, data drift, SEO pair.
# Runs INSIDE with-server.sh (the :3200 parity server).
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 3

echo "=== CLONE login + drift census (28th) ==="
agent-browser eval "(async () => {
  const txt = document.body.innerText;
  const pct = txt.split('\n').filter(l => l.includes('%')).slice(0, 4);
  return JSON.stringify({
    path: location.pathname,
    balance: (txt.match(/Balance\s*\\\$[\d,.]+/) || [''])[0].replace(/\n/g, ' '),
    income: (txt.match(/Income\s*\\\$[\d,.]+/) || [''])[0].replace(/\n/g, ' '),
    savings: (txt.match(/Savings\s*\\\$[\d,.]+/) || [''])[0].replace(/\n/g, ' '),
    expenses: (txt.match(/Expenses\s*\\\$[\d,.]+/) || [''])[0].replace(/\n/g, ' '),
    pct,
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R1 (burger hit) at 390x844 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" default "$PB/probe-r1-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R2 (sheet opens, nav, closes — the superset) ==="
bash "$PB/run-probe.sh" default "$PB/probe-r2-open-v34.mjs" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" default "$PB/probe-r2-nav-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R3 (nav landmark + active) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" default "$PB/probe-r3-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R4 (per-route overflow) ==="
bash "$PB/run-probe.sh" default "$PB/probe-r4a-v34.mjs" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" default "$PB/probe-r4b-v34.mjs" 2>/dev/null | tail -1
