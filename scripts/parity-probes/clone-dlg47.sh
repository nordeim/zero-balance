#!/usr/bin/env bash
# v47 measurement — clone side: the dialog input's focus-state shadow
# composition + rest census (Add Item dialog, first amount input).
set -u
export AGENT_BROWSER_SESSION="clone47a"
BASE="http://localhost:3200"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already?';
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3

echo "=== open the Add Item dialog (quick-action) ==="
agent-browser eval "(() => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('Add Item')); if (b) { b.click(); return 'clicked'; } return 'not found'; })()" 2>/dev/null | tail -1
sleep 2

echo "=== clone input REST census ==="
agent-browser eval "(() => { const dlg = document.querySelector('[role=dialog]'); if (!dlg) return 'no dialog'; const first = dlg.querySelector('input'); const cs = getComputedStyle(first); return JSON.stringify({ h: cs.height, radius: cs.borderRadius, pad: cs.padding, borderW: cs.borderWidth, borderC: cs.borderColor, bg: cs.backgroundColor, boxShadow: cs.boxShadow, outline: cs.outline, transition: cs.transition }); })()" 2>/dev/null | tail -1

echo "=== clone input FOCUS census ==="
agent-browser eval "(() => { const dlg = document.querySelector('[role=dialog]'); if (!dlg) return 'no dialog'; const first = dlg.querySelector('input'); first.focus(); return 'focused'; })()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(() => { const dlg = document.querySelector('[role=dialog]'); if (!dlg) return 'no dialog'; const first = dlg.querySelector('input'); const cs = getComputedStyle(first); return JSON.stringify({ focused: document.activeElement === first, matchesFV: first.matches(':focus-visible'), boxShadow: cs.boxShadow, outline: cs.outline, borderC: cs.borderColor }); })()" 2>/dev/null | tail -1
