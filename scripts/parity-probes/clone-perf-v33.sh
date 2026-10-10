#!/usr/bin/env bash
# clone-perf-v33.sh — the clone-side page-weight census (session-67 surface #4):
# the dashboard document's chunk graph + sizes (raw + gz), the resource-timing
# census, and the live toast semantics check (surface #3 clone side).
# Runs INSIDE with-server.sh.
set -u
BASE="http://localhost:3200"

echo "=== A) document + chunk graph (raw + gz sizes) ==="
HTML=$(curl -s "$BASE/")
echo "doc: $(( $(echo "$HTML" | wc -c) / 1024 ))KB"
CHUNKS=$(echo "$HTML" | grep -oE '/_next/static/chunks/[A-Za-z0-9_.-]+\.js' | sort -u)
TOTAL=0; TOTALGZ=0
for c in $CHUNKS; do
  raw=$(curl -s "$BASE$c" | wc -c)
  gz=$(curl -s -H "Accept-Encoding: gzip" -o /dev/null -w "%{size_download}" "$BASE$c")
  TOTAL=$((TOTAL+raw)); TOTALGZ=$((TOTALGZ+gz))
  [ "$raw" -gt 30000 ] && echo "  $c: $((raw/1024))KB raw / $((gz/1024))KB gz"
done
echo "chunks referenced: $(echo "$CHUNKS" | wc -l) | total: $((TOTAL/1024))KB raw / $((TOTALGZ/1024))KB gz"
CSS=$(echo "$HTML" | grep -oE '/_next/static/chunks/[A-Za-z0-9_.-]+\.css' | sort -u)
for c in $CSS; do raw=$(curl -s "$BASE$c" | wc -c); echo "css $c: $((raw/1024))KB raw"; done

echo ""
echo "=== B) live resource-timing census (agent-browser) ==="
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async function(){var em=document.querySelector('input[type=email]');var pw=document.querySelector('input[type=password]');var set=function(el,v){Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set.call(el,v);el.dispatchEvent(new Event('input',{bubbles:true}))};set(em,'demo@zerobalance.app');set(pw,'Demo1234!');em.closest('form').requestSubmit();return 'in'})()" >/dev/null 2>&1
sleep 4
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 4
agent-browser eval "(function(){var nav=performance.getEntriesByType('navigation')[0];var rs=performance.getEntriesByType('resource');var js=rs.filter(function(r){return /\.js/.test(r.name)});var css=rs.filter(function(r){return /\.css/.test(r.name)});var sum=function(a){return a.reduce(function(s,r){return s+(r.transferSize||0)},0)};return JSON.stringify({nav_ms:Math.round(nav.duration),resources:rs.length,jsCount:js.length,jsTransferKB:Math.round(sum(js)/1024),cssTransferKB:Math.round(sum(css)/1024),domContentLoaded:Math.round(nav.domContentLoadedEventEnd-nav.startTime)})})()" 2>/dev/null

echo ""
echo "=== C) live toast semantics (surface #3 clone side) ==="
agent-browser eval "(function(){var v=document.querySelector('.zb-toast-viewport')?.parentElement;return JSON.stringify({viewportTag:v?v.tagName:null,role:v?v.getAttribute('role'):null,ariaLabel:v?v.getAttribute('aria-label'):null,ti:v?v.tabIndex:null,pe:v?getComputedStyle(v).pointerEvents:null})})()" 2>/dev/null
# trigger a toast: open calculator, add+delete a line item (restores to 0 items)
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "var c=[...document.querySelectorAll('button')].find(function(b){return /Calculate/i.test(b.textContent||'')});c?.click();'calc'" >/dev/null 2>&1
sleep 2
agent-browser eval "var a=[...document.querySelectorAll('button')].find(function(b){return /Add First Item|Add Item/i.test(b.textContent||'')});a?.click();'add'" >/dev/null 2>&1
sleep 2
agent-browser eval "(function(){var h2=[].slice.call(document.querySelectorAll('h2')).find(function(h){return /Add Line Item/.test(h.textContent||'')});var ov=h2.closest('div.fixed');var ins=[].slice.call(ov.querySelectorAll('input')).filter(function(i){return i.type==='text'||i.type==='number'});var set=function(el,v){Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set.call(el,v);el.dispatchEvent(new Event('input',{bubbles:true}))};set(ins[0],'Perf Probe');set(ins[1],'7');var sv=[].slice.call(ov.querySelectorAll('button')).find(function(b){return /Save Item/i.test(b.textContent||'')});sv.click();return 'saved'})()" >/dev/null 2>&1
sleep 1.5
agent-browser eval "(function(){var t=document.querySelector('[data-radix-collection-item], .zb-toast');var live=[...document.querySelectorAll('[aria-live],[role=status],[role=alert]')];return JSON.stringify({liveRegions:live.map(function(e){return {tag:e.tagName,role:e.getAttribute('role'),live:e.getAttribute('aria-live'),txt:(e.textContent||'').trim().slice(0,40),h:Math.round(e.getBoundingClientRect().height)}})})})()" 2>/dev/null
sleep 3
echo "=== D) cleanup: delete the probe line item ==="
agent-browser eval "(function(){var h2=[].slice.call(document.querySelectorAll('h2')).find(function(h){return /Calculator/i.test(h.textContent||'')});var dlg=h2?h2.closest('div.fixed'):null;if(!dlg)return 'no calc';var rows=[].slice.call(dlg.querySelectorAll('button')).filter(function(b){return /Delete/i.test(b.getAttribute('aria-label')||'')||/trash/i.test(b.getAttribute('aria-label')||'')});if(!rows.length){var small=[].slice.call(dlg.querySelectorAll('button')).filter(function(b){return b.getBoundingClientRect().width<40&&b.textContent.trim()===''&&b.closest('.group')});rows=small}rows[rows.length-1]?.click();return 'deleted:'+(rows.length>0)})()" 2>/dev/null
sleep 1.5
# confirm button (the clone's inline confirm) — click the red Delete
agent-browser eval "(function(){var cf=[...document.querySelectorAll('button')].find(function(b){return /Delete/i.test(b.textContent||'')&&b.closest('div.fixed')&&getComputedStyle(b).color!==getComputedStyle(document.body).color});if(!cf){cf=[...document.querySelectorAll('button')].filter(function(b){return b.closest('div.fixed')&&/Delete/.test(b.textContent||'')}).pop()}cf?.click();return 'confirm:'+(!!cf)})()" 2>/dev/null
sleep 1.5
agent-browser eval "(function(){var h2=[].slice.call(document.querySelectorAll('h2')).find(function(h){return /Calculator/i.test(h.textContent||'')});var dlg=h2?h2.closest('div.fixed'):null;var txt=dlg?dlg.textContent:'';return 'based-on-0:'+(/Based on 0 items|No line items|Add First Item/i.test(txt))})()" 2>/dev/null
echo "DONE"
