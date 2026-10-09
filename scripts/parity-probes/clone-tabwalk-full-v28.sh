#!/usr/bin/env bash
# v28: real-Tab walk on the clone's /expenses with FULL reads at the
# Edit/Calculate stops (untruncated box-shadow + outline + class).
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-tabwalk-full-v28.sh
set -u
BASE="http://localhost:3200"

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
  em.closest('form').requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser mouse move 5 5 >/dev/null 2>&1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3

for i in $(seq 1 12); do
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.4
  TXT=$(agent-browser eval "(() => { const el = document.activeElement; return (el && el !== document.body) ? (el.textContent || '').trim().slice(0, 12) : 'body'; })()" 2>/dev/null | tr -d '"')
  if [ "$TXT" = "Edit" ] || [ "$TXT" = "Calculate" ]; then
    echo "=== stop $i: $TXT (FULL) ==="
    agent-browser eval "(() => {
      const el = document.activeElement;
      const cs = getComputedStyle(el);
      return JSON.stringify({
        txt: (el.textContent || '').trim(),
        cls: (el.className || '').toString(),
        boxShadow: cs.boxShadow,
        outline: cs.outlineStyle + ' ' + cs.outlineWidth + ' ' + cs.outlineColor,
        fv: el.matches(':focus-visible'),
      }, null, 1);
    })()" 2>/dev/null
  else
    echo "stop $i: $TXT"
  fi
done
