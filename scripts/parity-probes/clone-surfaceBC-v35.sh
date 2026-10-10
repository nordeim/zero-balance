#!/usr/bin/env bash
# v35: clone-side Surface B — the dashboard Add Item focus-visible family.
# Runs INSIDE with-server.sh (the :3200 parity server).
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone35"

agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 4

echo "=== CLONE Add Item focus-visible (REAL Tab) ==="
bash "$PB/run-probe.sh" clone35 "$PB/probe-focus-add-v35.mjs" 2>/dev/null | tail -1
agent-browser press Tab >/dev/null 2>&1
sleep 0.3
agent-browser press Shift+Tab >/dev/null 2>&1
sleep 0.8
bash "$PB/run-probe.sh" clone35 "$PB/probe-read-add-fv-v35.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE Add Item rest-state shadow (unfocused) ==="
agent-browser eval "(async () => {
  const btn = [...document.querySelectorAll('button')].find(x => /add item/i.test(x.textContent));
  const c = getComputedStyle(btn);
  return JSON.stringify({restShadow: c.boxShadow, restBg: c.backgroundColor});
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE Surface C: deep-link/URL contract ==="
echo "--- /login?from_url=/income redirect ---"
agent-browser open "$BASE/login?from_url=/income" >/dev/null 2>&1
sleep 2
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
agent-browser eval "JSON.stringify({landed: location.pathname})" 2>/dev/null | tail -1
echo "--- 404 route link semantics ---"
agent-browser open "$BASE/no-such-route" >/dev/null 2>&1
sleep 2
agent-browser eval "JSON.stringify({title: document.title, h1: (document.querySelector('h1')||{}).textContent, goHome: (document.querySelector('a')||{}).textContent, linkHref: document.querySelector('a') ? document.querySelector('a').getAttribute('href') : null})" 2>/dev/null | tail -1
