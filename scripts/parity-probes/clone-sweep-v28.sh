#!/usr/bin/env bash
# v28: the clone-side parity sweep — login + button census + badge hover
# probes on the :3200 parity server, ALL inside ONE with-server.sh
# invocation (the server dies between split invocations — the v27 lesson).
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-sweep-v28.sh
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes

# 1. login
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  const set = (el, v) => {
    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
    setter.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  const form = em.closest('form');
  if (form) form.requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 3

# 2. desktop viewport + expenses census
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
echo "=== CLONE expenses button census ==="
bash "$PB/run-probe.sh" default "$PB/probe-v28-btn-census.mjs" 2>/dev/null

# 3. badge dump (classes) on the first expense card
echo "=== CLONE expense-card badges ==="
agent-browser eval "(async () => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter((c) => c.getBoundingClientRect().width > 200);
  const card = cards[0];
  if (!card) return JSON.stringify({ error: 'no card' });
  const badges = [...card.querySelectorAll('span, div')].filter((e) => {
    const t = (e.textContent || '').trim();
    return t.length > 0 && t.length < 14 && /inline-flex/.test((e.className || '').toString()) && /px-2\.5/.test((e.className || '').toString()) && !e.querySelector('.inline-flex');
  }).map((e) => ({ txt: (e.textContent || '').trim().slice(0, 12), cls: (e.className || '').toString() }));
  return JSON.stringify(badges, null, 1);
})()" 2>/dev/null
