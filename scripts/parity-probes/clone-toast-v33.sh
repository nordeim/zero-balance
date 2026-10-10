#!/usr/bin/env bash
# clone-toast-v33.sh — the clone's LIVE toast semantics (session-67 surface #3):
# trigger the line-item-added toast, read the toast's role/aria-live/focus
# semantics + the F8 viewport affordance, then clean up the fixture.
# Runs INSIDE with-server.sh.
set -u
BASE="http://localhost:3200"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async function(){var em=document.querySelector('input[type=email]');var pw=document.querySelector('input[type=password]');var set=function(el,v){Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set.call(el,v);el.dispatchEvent(new Event('input',{bubbles:true}))};set(em,'demo@zerobalance.app');set(pw,'Demo1234!');em.closest('form').requestSubmit();return 'in'})()" >/dev/null 2>&1
sleep 3.5
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 4

S1=$(agent-browser eval "(function(){var c=[...document.querySelectorAll('button')].find(function(b){return /Calculate/i.test(b.textContent||'')});if(c){c.click();return 'opened'}return 'no-calc-btn'})()" 2>/dev/null | tail -1)
echo "calculator: $S1"
sleep 2.5
S2=$(agent-browser eval "(function(){var h2=[].slice.call(document.querySelectorAll('h2,[role=dialog] h2')).find(function(h){return /Calculator/i.test(h.textContent||'')});if(!h2)return 'no-calc';var host=h2.closest('[data-state=open],div.fixed,[role=dialog]')||document;if(host===document)return 'no-host';var a=[...host.querySelectorAll('button')].find(function(b){return /Add First Item|Add Item/i.test(b.textContent||'')});if(a){a.click();return 'subdialog-opened'}return 'no-add-btn'})()" 2>/dev/null | tail -1)
echo "sub-dialog: $S2"
sleep 2.5
S3=$(agent-browser eval "(function(){var h2=[].slice.call(document.querySelectorAll('h2')).find(function(h){return /Add Line Item/i.test(h.textContent||'')});if(!h2)return 'no-subdialog';var ov=h2.closest('[data-state=open],[role=dialog]');if(!ov)return 'no-host';var ins=[].slice.call(ov.querySelectorAll('input')).filter(function(i){return i.type==='text'||i.type==='number'});var set=function(el,v){Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set.call(el,v);el.dispatchEvent(new Event('input',{bubbles:true}))};set(ins[0],'Toast Probe');set(ins[1],'9');var sv=[].slice.call(ov.querySelectorAll('button')).find(function(b){return /Save Item/i.test(b.textContent||'')});sv.click();return 'saved'})()" 2>/dev/null | tail -1)
echo "save: $S3"
sleep 1.2
echo "=== live toast semantics ==="
agent-browser eval "(function(){var live=[...document.querySelectorAll('[aria-live],[role=status],[role=alert],.zb-toast')];return JSON.stringify(live.map(function(e){var cs=getComputedStyle(e);var r=e.getBoundingClientRect();return {tag:e.tagName,cls:String(e.className).slice(0,30),role:e.getAttribute('role'),live:e.getAttribute('aria-live'),ti:e.tabIndex,txt:(e.textContent||'').trim().slice(0,40),h:Math.round(r.height),vis:r.height>0,pe:cs.pointerEvents}}),null,0)})()" 2>/dev/null
echo ""
echo "=== F8 affordance ==="
agent-browser press F8 >/dev/null 2>&1
sleep 0.6
agent-browser eval "(function(){var a=document.activeElement;return 'after-F8: '+a.tagName+'.'+String(a.className).slice(0,30)+' role:'+(a.getAttribute('role')||'none')})()" 2>/dev/null
echo ""
echo "=== cleanup ==="
agent-browser eval "(function(){var h2=[].slice.call(document.querySelectorAll('h2')).find(function(h){return /Calculator/i.test(h.textContent||'')});if(!h2)return 'calc-closed';var dlg=h2.closest('div.fixed');var del=[].slice.call(dlg.querySelectorAll('button')).filter(function(b){return (b.getAttribute('aria-label')||'').toLowerCase().indexOf('delete')>-1});if(!del.length){return 'no-del'}del[del.length-1].click();return 'del-click'})()" 2>/dev/null
sleep 1.2
agent-browser eval "(function(){var cf=[...document.querySelectorAll('button')].filter(function(b){return b.closest('div.fixed')&&/^Delete$/i.test((b.textContent||'').trim())});if(cf.length){cf[cf.length-1].click();return 'confirmed'}return 'no-confirm'})()" 2>/dev/null
sleep 1.5
agent-browser eval "(function(){var h2=[].slice.call(document.querySelectorAll('h2')).find(function(h){return /Calculator/i.test(h.textContent||'')});var txt=h2?h2.closest('div.fixed').textContent:'';return 'restored:'+(/Add First Item/i.test(txt))})()" 2>/dev/null
echo "DONE"
