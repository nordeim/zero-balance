#!/usr/bin/env bash
# clone-lisub-v33.sh — the clone-side line-item sub-dialog focus traversal
# (session-67 suggestion #1). Login → /expenses → calculator → Add First Item
# sub-dialog → census → initial focus → REAL Tab walk. Runs INSIDE with-server.sh.
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
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3

echo "=== open calculator + sub-dialog ==="
agent-browser eval "var c=[...document.querySelectorAll('button')].find(function(b){return /Calculate/i.test(b.textContent||'')}); c?.click(); 'calc:'+(!!c)" >/dev/null 2>&1
sleep 2
agent-browser eval "var a=[...document.querySelectorAll('button')].find(function(b){return /Add First Item|Add Item/i.test(b.textContent||'')}); a?.click(); 'add:'+(!!a)" >/dev/null 2>&1
sleep 2

echo "=== CENSUS ==="
bash "$PB/run-probe.sh" default "$PB/probe-lisub-census-v33.mjs" 2>/dev/null
echo ""
echo "=== INITIAL FOCUS (after mouse-open) ==="
agent-browser eval "var a=document.activeElement;a.tagName+' / '+(a.getAttribute('placeholder')||String(a.textContent||'').trim().slice(0,20))" 2>/dev/null
echo ""
echo "=== REAL TAB WALK (18) ==="
for i in $(seq 1 18); do
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.4
  r=$(agent-browser eval "var a=document.activeElement;var dlg=document.querySelector('[role=dialog]');a.tagName+' / '+(a.getAttribute('placeholder')||a.type||String(a.textContent||'').trim().slice(0,16))+' / inDlg:'+(dlg?dlg.contains(a):'n/a')" 2>/dev/null | tail -1)
  echo "T$i: $r"
done
echo "DONE"
