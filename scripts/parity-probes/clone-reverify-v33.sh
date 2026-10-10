#!/usr/bin/env bash
# clone-reverify-v33.sh — the live re-verification of the v33 fixes on the
# :3200 parity server: (a) the code inputs' REAL-Tab focused chrome vs the
# reference's measurement (byte-compare), (b) the announcer census, (c) the
# mobile-nav R1/R4 spot check. Runs INSIDE with-server.sh.
set -u
BASE="http://localhost:3200"

echo "=== A) the code inputs' focused family (register → verify → REAL Tab) ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(function(){var l=[...document.querySelectorAll('button,a')].find(function(b){return /Need an account|Sign up/i.test(b.textContent||'')});l?.click();return 'nav'})()" >/dev/null 2>&1
sleep 2.5
agent-browser eval "(async function(){var ins=[...document.querySelectorAll('input')];var em=ins.find(function(i){return i.type==='email'});var pws=ins.filter(function(i){return i.type==='password'});var set=function(el,v){Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set.call(el,v);el.dispatchEvent(new Event('input',{bubbles:true}))};set(em,'reverify-v33@zerobalance.app');set(pws[0],'Probe1234!');set(pws[1],'Probe1234!');var btn=[...document.querySelectorAll('button')].find(function(b){return /Create account/i.test(b.textContent||'')});btn?.click();return 'submitted'})()" >/dev/null 2>&1
sleep 3.5
echo "--- initial focus (expect Digit 1) ---"
agent-browser eval "(function(){var a=document.activeElement;return a.tagName+' / '+(a.getAttribute('aria-label')||'')})()" 2>/dev/null
agent-browser press Tab >/dev/null 2>&1
sleep 0.45
echo "--- focused Digit 2 chrome (settled) ---"
agent-browser eval "(function(){var a=document.activeElement;var cs=getComputedStyle(a);return JSON.stringify({label:a.getAttribute('aria-label'),box:cs.boxShadow,border:cs.borderColor,outline:cs.outlineStyle+' '+cs.outlineWidth+' '+cs.outlineColor})})()" 2>/dev/null
echo ""

echo "=== B) the mobile-nav R1/R4 spot check (27th) ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser eval "document.cookie='session=; Max-Age=0; path=/'; 'cleared'" >/dev/null 2>&1
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async function(){var em=document.querySelector('input[type=email]');var pw=document.querySelector('input[type=password]');var set=function(el,v){Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set.call(el,v);el.dispatchEvent(new Event('input',{bubbles:true}))};set(em,'demo@zerobalance.app');set(pw,'Demo1234!');em.closest('form').requestSubmit();return 'in'})()" >/dev/null 2>&1
sleep 3
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
cd /home/z/my-project/zero-balance/scripts/parity-probes
bash run-probe.sh default probe-r1-v31.mjs 2>/dev/null
for p in / /networth; do
  agent-browser open "$BASE$p" >/dev/null 2>&1
  sleep 2.5
  echo -n "$p → "
  agent-browser eval "document.documentElement.scrollWidth" 2>/dev/null
done
echo "DONE"
