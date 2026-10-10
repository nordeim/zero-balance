#!/usr/bin/env bash
# clone-seltrigger-deep-v33.sh — root-cause probe for the SelectTrigger focus
# ring. Compares the trigger's ring custom-props + settled shadow against the
# v32-fixed calculator row action (known green) IN THE SAME PAGE. Also dumps
# what the built CSS emits for the focus:ring utilities. INSIDE with-server.sh.
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

echo "=== A) SelectTrigger under REAL focus (settle 1.2s) ==="
for i in $(seq 1 20); do
  fs=$(agent-browser eval "document.activeElement.tagName+'|'+String(document.activeElement.textContent||'').trim().slice(0,10)" 2>/dev/null | tail -1)
  case "$fs" in *"BUTTON|Active"*) break;; esac
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.32
done
sleep 1.2
agent-browser eval "(function(){var a=document.activeElement;var cs=getComputedStyle(a);return JSON.stringify({matchesFocus: a.matches(':focus'), cls:String(a.className).slice(0,130), ringColor: cs.getPropertyValue('--tw-ring-color').trim(), ringShadowVar: cs.getPropertyValue('--tw-ring-shadow').trim().slice(0,70), offsetShadowVar: cs.getPropertyValue('--tw-ring-offset-shadow').trim().slice(0,50), insetShadowVar: cs.getPropertyValue('--tw-inset-shadow').trim().slice(0,30), shadowVar: cs.getPropertyValue('--tw-shadow').trim().slice(0,40), boxshadow: cs.boxShadow.slice(0,110)})})()" 2>/dev/null
echo ""
echo "=== B) the CSS the build emits for focus:ring-1 (grep the stylesheet) ==="
CSS=$(agent-browser eval "var l=[...document.querySelectorAll('link[rel=stylesheet]')].map(function(l){return l.href}); l[0]||'none'" 2>/dev/null | tail -1 | tr -d '"')
echo "sheet: $CSS"
curl -s "$CSS" | grep -oE "\.focus\\\\:ring-1:focus[^}]*\}" | head -2
curl -s "$CSS" | grep -oE "\.focus\\\\:ring-ring:focus[^}]*\}" | head -2
echo ""
echo "=== C) control: the v32-fixed row action ring (needs a line item) ==="
echo "(skip — no fixture; the e2e pins it green)"
echo "DONE"
