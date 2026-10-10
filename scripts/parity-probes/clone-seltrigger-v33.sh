#!/usr/bin/env bash
# clone-seltrigger-v33.sh — the clone-side SelectTrigger focus-chrome pair
# (session-67 surface #1 extension): open the line-item sub-dialog, REAL-Tab
# to the Status trigger (16 stops forward from X... but simpler: walk forward
# from initial focus until a BUTTON with 'Active' text is focused), settle
# 400ms, read the computed outline + box-shadow. Runs INSIDE with-server.sh.
set -u
BASE="http://localhost:3200"

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
agent-browser eval "var c=[...document.querySelectorAll('button')].find(function(b){return /Calculate/i.test(b.textContent||'')}); c?.click(); 'calc'" >/dev/null 2>&1
sleep 2
agent-browser eval "var a=[...document.querySelectorAll('button')].find(function(b){return /Add First Item|Add Item/i.test(b.textContent||'')}); a?.click(); 'add'" >/dev/null 2>&1
sleep 2
echo "=== walk to the Status trigger (REAL Tabs) ==="
for i in $(seq 1 20); do
  agent-browser eval "document.activeElement.tagName+'|'+String(document.activeElement.textContent||'').trim().slice(0,10)+'|'+(document.activeElement.getAttribute('placeholder')||'')" 2>/dev/null | tail -1 > /tmp/focusstate
  fs=$(cat /tmp/focusstate)
  case "$fs" in *"BUTTON|Active|"*) echo "LANDED: $fs (after $((i-1)) tabs)"; break;; esac
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.32
done
sleep 0.5
echo "=== focused Status trigger chrome (settled) ==="
agent-browser eval "(function(){var a=document.activeElement;var cs=getComputedStyle(a);return JSON.stringify({el:a.tagName+' txt:'+(a.textContent||'').trim().slice(0,12),outline:cs.outlineStyle+' '+cs.outlineWidth+' '+cs.outlineColor,shadow:cs.boxShadow.slice(0,85),h:Math.round(a.getBoundingClientRect().height)})})()" 2>/dev/null
echo ""
echo "=== Frequency trigger chrome (Tab backward to it) ==="
agent-browser press Shift+Tab >/dev/null 2>&1; sleep 0.3
for i in $(seq 1 14); do
  agent-browser press Shift+Tab >/dev/null 2>&1; sleep 0.3
  fs=$(agent-browser eval "document.activeElement.tagName+'|'+String(document.activeElement.textContent||'').trim().slice(0,12)" 2>/dev/null | tail -1)
  case "$fs" in *"BUTTON|Monthly"*) echo "LANDED: $fs"; break;; esac
done
sleep 0.5
agent-browser eval "(function(){var a=document.activeElement;var cs=getComputedStyle(a);return JSON.stringify({el:a.tagName+' txt:'+(a.textContent||'').trim().slice(0,12),outline:cs.outlineStyle+' '+cs.outlineWidth+' '+cs.outlineColor,shadow:cs.boxShadow.slice(0,85)})})()" 2>/dev/null
echo "DONE"
