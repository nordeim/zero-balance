#!/usr/bin/env bash
# kb-lisub-v33.sh — the line-item sub-dialog REAL Tab walk (18 real Tab presses
# via agent-browser press; reads activeElement after each). Pre-req: the
# sub-dialog is OPEN on the session.
SESSION="$1"; shift || true
for i in $(seq 1 18); do
  agent-browser --session "$SESSION" press Tab >/dev/null 2>&1
  sleep 0.35
  read -r line < <(agent-browser --session "$SESSION" eval "(function(){var h2=[].slice.call(document.querySelectorAll('h2')).find(function(h){return /Add Line Item|Edit Line Item/.test(h.textContent||'')});var overlay=h2?h2.closest('div.fixed,[data-state=open],div[class*=fixed]')||h2.parentElement:null;for(var i=0;i<6&&overlay&&overlay.parentElement;i++){if(getComputedStyle(overlay.parentElement).position==='fixed'){overlay=overlay.parentElement}else{break}}var a=document.activeElement;var d=a===document.body?'BODY':a.tagName.toLowerCase()+(a.getAttribute('placeholder')?'['+a.getAttribute('placeholder').slice(0,18)+']':a.getAttribute('aria-label')?'['+a.getAttribute('aria-label').slice(0,18)+']':a.type?'['+a.type+']':'['+String(a.textContent||'').trim().slice(0,14)+']');return 'T$i: '+d+' | inSub: '+(overlay?overlay.contains(a):'?')})()" 2>/dev/null | tail -1)
  echo "$line"
  case "$line" in *"| inSub: false"*) break;; esac
done
