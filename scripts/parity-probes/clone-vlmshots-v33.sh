#!/usr/bin/env bash
# clone-vlmshots-v33.sh — capture the clone's VLM pair screenshots:
# the dashboard (login demo user) + the verify-email state (register a
# throwaway). Runs INSIDE with-server.sh.
set -u
BASE="http://localhost:3200"

agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async function(){var em=document.querySelector('input[type=email]');var pw=document.querySelector('input[type=password]');var set=function(el,v){Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set.call(el,v);el.dispatchEvent(new Event('input',{bubbles:true}))};set(em,'demo@zerobalance.app');set(pw,'Demo1234!');em.closest('form').requestSubmit();return 'in'})()" >/dev/null 2>&1
sleep 3.5
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 4
agent-browser screenshot /tmp/vlm33/clone-dashboard.png >/dev/null 2>&1
echo "dashboard shot: $(ls -la /tmp/vlm33/clone-dashboard.png 2>/dev/null | wc -l)"

# log out via the API cookie clear + reload, then register a throwaway
agent-browser eval "document.cookie='session=; Max-Age=0; path=/'; 'cleared'" >/dev/null 2>&1
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(function(){var l=[...document.querySelectorAll('button,a')].find(function(b){return /Need an account|Sign up/i.test(b.textContent||'')});l?.click();return 'nav'})()" >/dev/null 2>&1
sleep 2.5
agent-browser eval "(async function(){var ins=[...document.querySelectorAll('input')];var em=ins.find(function(i){return i.type==='email'});var pws=ins.filter(function(i){return i.type==='password'});var set=function(el,v){Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set.call(el,v);el.dispatchEvent(new Event('input',{bubbles:true}))};set(em,'probe2-v33@zerobalance.app');set(pws[0],'Probe1234!');set(pws[1],'Probe1234!');var btn=[...document.querySelectorAll('button')].find(function(b){return /Create account/i.test(b.textContent||'')});btn?.click();return 'submitted'})()" >/dev/null 2>&1
sleep 4
agent-browser eval "(function(){var h=[...document.querySelectorAll('h2')].map(function(h){return (h.textContent||'').trim()}).join('|');return 'h2s:'+h.slice(0,60)})()" 2>/dev/null
agent-browser screenshot /tmp/vlm33/clone-verify.png >/dev/null 2>&1
echo "verify shot done"
echo "DONE"
