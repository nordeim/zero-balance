#!/usr/bin/env bash
# debug-calc-v59.sh — interactive step-by-step debug of the clone calculator
# open flow (inside with-server on :3200).
set -u
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clone59dbg"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
POS=$(agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$1850'));
  if (!card) return 'ERR';
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1)
echo "rent card center: $POS"
X=$(echo "$POS" | cut -d, -f1); Y=$(echo "$POS" | cut -d, -f2)
agent-browser mouse move "$X" "$Y" >/dev/null 2>&1
sleep 1
# check buttons visible after hover
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$1850'));
  const btns = [...card.querySelectorAll('button')].map(b => ({t: b.textContent.trim().slice(0,10), w: Math.round(b.getBoundingClientRect().width), op: getComputedStyle(b).opacity}));
  return JSON.stringify(btns);
})()" 2>/dev/null | tail -1
CALC=$(agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$1850'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate\$/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2) + ',' + Math.round(r.width) + ',' + Math.round(r.height);
})()" 2>/dev/null | tail -1)
echo "calculate button: $CALC (x,y,w,h)"
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
# what element is at the click point right now?
agent-browser eval "(async () => {
  const el = document.elementFromPoint($CX, $CY);
  return JSON.stringify({ tag: el ? el.tagName : null, txt: el ? (el.textContent||'').trim().slice(0,15) : null, isBtn: el ? el.closest('button') !== null : null });
})()" 2>/dev/null | tail -1
agent-browser mouse down >/dev/null 2>&1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const dlgs = [...document.querySelectorAll('[role=dialog]')];
  return JSON.stringify({ dlgCount: dlgs.length, texts: dlgs.map(d => (d.innerText||'').split('\n')[0]) , bodyHasCalc: /Rent Calculator/.test(document.body.innerText) });
})()" 2>/dev/null | tail -1
EOF
