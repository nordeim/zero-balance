#!/usr/bin/env bash
# v30: clone-side sweep — login + standing mobile-nav R1-R4 (24th), guideline rows,
# quick-action hover family (shadow-lg v3-vs-v4 computation check).
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-sweep-v30.sh
set -u
BASE="http://localhost:3200"

agent-browser --session clone30 open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser --session clone30 eval "(async () => {
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
agent-browser --session clone30 set viewport 390 844 >/dev/null 2>&1

echo "=== R1 (burger hit — clone) ==="
agent-browser --session clone30 open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser --session clone30 eval "(() => {
  const btn = [...document.querySelectorAll('button')].find(b => { const r = b.getBoundingClientRect(); return r.width>20 && r.width<45 && r.top<60 && b.querySelector('svg'); });
  if (!btn) return 'no burger';
  const r = btn.getBoundingClientRect();
  const cx = Math.round(r.x + r.width/2), cy = Math.round(r.y + r.height/2);
  const hit = document.elementFromPoint(cx, cy);
  return JSON.stringify({ burgerBox: {w: Math.round(r.width)}, hitTag: hit ? hit.tagName : null, hitIsBurgerOrChild: hit ? !!hit.closest('button') && hit.closest('button') === btn : false, scrollWidth: document.documentElement.scrollWidth });
})()" 2>/dev/null

echo "=== R2 (sheet closes after nav — clone superset) ==="
agent-browser --session clone30 open "$BASE/" >/dev/null 2>&1
sleep 2
agent-browser --session clone30 eval "(async () => {
  const btn = [...document.querySelectorAll('button')].find(b => { const r = b.getBoundingClientRect(); return r.width>20 && r.width<45 && r.top<60 && b.querySelector('svg'); });
  if (!btn) return 'no burger';
  const r = btn.getBoundingClientRect();
  btn.querySelector('svg').dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true, clientX: r.x+5, clientY: r.y+5}));
  await new Promise(res => setTimeout(res, 1000));
  const sheetOpen = !!document.querySelector('[role=dialog]');
  const link = [...document.querySelectorAll('a')].find(a => /income/i.test(a.textContent) && a.getBoundingClientRect().left < 300);
  let afterNav = 'no-link';
  if (link) {
    const lr = link.getBoundingClientRect();
    link.dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true, clientX: lr.x+lr.width/2, clientY: lr.y+10}));
    await new Promise(res => setTimeout(res, 1500));
    afterNav = document.querySelector('[role=dialog]') ? 'SHEET STILL OPEN' : 'sheet closed';
  }
  return JSON.stringify({ sheetOpened: sheetOpen, afterNavClick: afterNav, url: location.pathname });
})()" 2>/dev/null

echo "=== R4 (per-route overflow — clone) ==="
for p in / /income /expenses /savings /networth; do
  agent-browser --session clone30 open "$BASE$p" >/dev/null 2>&1
  sleep 2
  echo -n "$p → "
  agent-browser --session clone30 eval "document.documentElement.scrollWidth" 2>/dev/null
done

echo "=== R3 (nav landmark + active on / — clone superset) ==="
agent-browser --session clone30 open "$BASE/" >/dev/null 2>&1
sleep 2
agent-browser --session clone30 eval "(() => {
  const nav = document.querySelector('nav');
  const dash = [...document.querySelectorAll('a')].find(a => /dashboard/i.test(a.textContent));
  const active = dash ? getComputedStyle(dash).backgroundImage : null;
  return JSON.stringify({ navLandmark: !!nav, dashActiveGradient: active && active !== 'none' });
})()" 2>/dev/null

# ---- Desktop: guideline rows + quick-action hover ----
agent-browser --session clone30 set viewport 1280 800 >/dev/null 2>&1
agent-browser --session clone30 open "$BASE/" >/dev/null 2>&1
sleep 3

echo "=== G1a. guideline row (clone, rest) ==="
agent-browser --session clone30 eval "(() => {
  const desc = [...document.querySelectorAll('main p, main span')].find(e => /Essential expenses like rent/i.test(e.textContent || ''));
  if (!desc) return 'not found';
  const row = desc.parentElement;
  const cs = getComputedStyle(row);
  return JSON.stringify({ cls: (row.className||''), bg: cs.backgroundColor, border: cs.border, radius: cs.borderRadius, pad: cs.padding, transition: cs.transition, td: cs.transitionDuration, cursor: cs.cursor });
})()" 2>/dev/null

echo "=== G1b. guideline row REAL hover (clone) ==="
agent-browser --session clone30 eval "(() => {
  const desc = [...document.querySelectorAll('main p, main span')].find(e => /Essential expenses like rent/i.test(e.textContent || ''));
  desc.parentElement.scrollIntoView({block: 'center'});
  return 'ok';
})()" 2>/dev/null
sleep 0.5
agent-browser --session clone30 mouse move 5 5 >/dev/null 2>&1
sleep 0.3
COORDS=$(agent-browser --session clone30 eval "(() => {
  const desc = [...document.querySelectorAll('main p, main span')].find(e => /Essential expenses like rent/i.test(e.textContent || ''));
  const r = desc.parentElement.getBoundingClientRect();
  return JSON.stringify({x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2)});
})()" 2>/dev/null)
echo "row coords: $COORDS"
X=$(echo "$COORDS" | python3 -c "import sys,json; print(json.loads(json.load(sys.stdin))['x'])")
Y=$(echo "$COORDS" | python3 -c "import sys,json; print(json.loads(json.load(sys.stdin))['y'])")
agent-browser --session clone30 mouse move "$X" "$Y" >/dev/null 2>&1
sleep 0.9
agent-browser --session clone30 eval "(() => {
  const desc = [...document.querySelectorAll('main p, main span')].find(e => /Essential expenses like rent/i.test(e.textContent || ''));
  const row = desc.parentElement;
  const cs = getComputedStyle(row);
  return JSON.stringify({ hovered: row.matches(':hover'), bg: cs.backgroundColor, border: cs.border, shadow: cs.boxShadow });
})()" 2>/dev/null

echo "=== G2a. quick-action button (clone, rest) ==="
agent-browser --session clone30 mouse move 5 5 >/dev/null 2>&1
sleep 0.4
agent-browser --session clone30 eval "(() => {
  const b = [...document.querySelectorAll('main button')].find(x => /^Add Income$/i.test((x.textContent || '').trim()));
  if (!b) return 'not found';
  b.scrollIntoView({block: 'center'});
  const cs = getComputedStyle(b);
  const iconBox = b.querySelector('div[class*=rounded-xl], span[class*=rounded-xl]');
  const plus = [...b.querySelectorAll('svg')].pop();
  return JSON.stringify({ cls: (b.className||'').slice(0,250), bg: cs.backgroundColor, border: cs.border, radius: cs.borderRadius, pad: cs.padding, transition: cs.transition, cursor: cs.cursor, shadow: cs.boxShadow,
    iconBoxCls: iconBox ? (iconBox.className||'').toString().slice(0,200) : null, iconBoxTransition: iconBox ? getComputedStyle(iconBox).transition : null,
    plusCls: plus ? (plus.getAttribute('class')||'').slice(0,150) : null, plusTransition: plus ? getComputedStyle(plus).transition : null, plusOpacity: plus ? getComputedStyle(plus).opacity : null });
})()" 2>/dev/null

echo "=== G2b. quick-action REAL hover (clone) ==="
sleep 0.6
QCOORDS=$(agent-browser --session clone30 eval "(() => {
  const b = [...document.querySelectorAll('main button')].find(x => /^Add Income$/i.test((x.textContent || '').trim()));
  const r = b.getBoundingClientRect();
  return JSON.stringify({x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2)});
})()" 2>/dev/null)
echo "btn coords: $QCOORDS"
QX=$(echo "$QCOORDS" | python3 -c "import sys,json; print(json.loads(json.load(sys.stdin))['x'])")
QY=$(echo "$QCOORDS" | python3 -c "import sys,json; print(json.loads(json.load(sys.stdin))['y'])")
agent-browser --session clone30 mouse move "$QX" "$QY" >/dev/null 2>&1
sleep 0.9
agent-browser --session clone30 eval "(() => {
  const b = [...document.querySelectorAll('main button')].find(x => /^Add Income$/i.test((x.textContent || '').trim()));
  const cs = getComputedStyle(b);
  const iconBox = b.querySelector('div[class*=rounded-xl], span[class*=rounded-xl]');
  const plus = [...b.querySelectorAll('svg')].pop();
  return JSON.stringify({ hovered: b.matches(':hover'), shadow: cs.boxShadow, transform: cs.transform, iconTransform: iconBox ? getComputedStyle(iconBox).transform : null, plusOpacity: plus ? getComputedStyle(plus).opacity : null });
})()" 2>/dev/null
