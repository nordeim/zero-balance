#!/usr/bin/env bash
# debug-calc3-v59.sh — third debug: snapshot + @ref hover/click flow.
set -u
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clone59db3"
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
# hover via the unique "Apartment" subtitle (inside the Rent card)
agent-browser find text "Apartment" hover 2>&1 | tail -1
sleep 1
# the rent card index among div.rounded-xl (filter card + entertainment + groceries + rent)
IDX=$(agent-browser eval "(async () => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')];
  const i = cards.findIndex(c => (c.innerText||'').includes('Rent'));
  return JSON.stringify({idx: i, total: cards.length});
})()" 2>/dev/null | tail -1)
echo "rent card index: $IDX"
# click the rent card's Calculate button via eval-found position + real mouse events
POS=$(agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('main div.rounded-xl')].find(c => (c.innerText||'').includes('Rent'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate\$/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  const el = document.elementFromPoint(r.x + r.width/2, r.y + r.height/2);
  return JSON.stringify({cx: Math.round(r.x + r.width/2), cy: Math.round(r.y + r.height/2), hit: el ? el.tagName + '/' + (el.textContent||'').trim().slice(0,10) : null, hitInBtn: el ? btn.contains(el) : false});
})()" 2>/dev/null | tail -1)
echo "button + hit test: $POS"
CX=$(echo "$POS" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())['cx'])" 2>/dev/null)
CY=$(echo "$POS" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())['cy'])" 2>/dev/null)
echo "parsed: $CX $CY"
agent-browser mouse move "$CX" "$CY" --duration 300 --steps 8 >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const dlgs = [...document.querySelectorAll('[role=dialog]')];
  return JSON.stringify({ dlgCount: dlgs.length, texts: dlgs.map(d => (d.innerText||'').split('\n')[0]), bodyHasCalc: /Rent Calculator/.test(document.body.innerText) });
})()" 2>/dev/null | tail -1
EOF
