#!/usr/bin/env bash
# survey-itemkebab-v133.sh — the v133 candidate-survey probe (READ-ONLY,
# the v46 rule): read the REFERENCE's first EXPENSE card's action-row
# structure live at 1280x800 — enumerate the card's buttons (Edit /
# Calculate / the kebab trigger) with computed chrome, then measure the
# KEBAB's own-hover ladder (park -> card-hover reveal -> kebab own-hover
# -> restore) so the census finder can be shaped TAG-AGNOSTIC and
# STATE-INDEPENDENT (the v107 lesson; the v131/v132 survey precedents).
# READ-ONLY: hover reveals chrome, nothing is clicked (the kebab's click
# path — the action menu — is out of bounds per the v46 rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refsurvey133"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4

echo "=== the reference's first expense card: action-row structure (at-rest, pointer parked) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find(d => typeof d.className === 'string' && d.className.includes('grid-cols-3'));
  if (!grid) return JSON.stringify({error: 'no grid'});
  const card = grid.children[0];
  const btns = [...card.querySelectorAll('button')].map(b => {
    const r = b.getBoundingClientRect();
    const cs = getComputedStyle(b);
    return {text: (b.textContent || '').trim().slice(0, 24), ariaLabel: b.getAttribute('aria-label') || '', w: Math.round(r.width), h: Math.round(r.height), opacity: cs.opacity, bg: cs.backgroundColor, color: cs.color, radius: cs.borderRadius, pad: cs.padding, fs: cs.fontSize, fw: cs.fontWeight, border: cs.borderColor, transition: cs.transitionDuration, pos: cs.position};
  });
  return JSON.stringify({btnCount: btns.length, buttons: btns});
})()" 2>/dev/null | tail -1

echo "=== the kebab's own-hover ladder (card hover reveals the row; the kebab's own hover tints) ==="
agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find(d => typeof d.className === 'string' && d.className.includes('grid-cols-3'));
  if (!grid) return JSON.stringify({error: 'no grid'});
  const card = grid.children[0];
  // the kebab: the small square button (w<=50 && h<=50) with no text
  const kebab = [...card.querySelectorAll('button')].find(b => {
    const r = b.getBoundingClientRect();
    const t = (b.textContent || '').trim();
    return r.width > 20 && r.width <= 50 && Math.abs(r.width - r.height) < 6 && (!t || t.length < 3);
  });
  if (!kebab) return JSON.stringify({error: 'no kebab found'});
  const cr = card.getBoundingClientRect();
  const kr = kebab.getBoundingClientRect();
  const read = () => {
    const cs = getComputedStyle(kebab);
    return {hoverMatch: kebab.matches(':hover'), cardHover: card.matches(':hover'), opacity: cs.opacity, bg: cs.backgroundColor, color: cs.color, w: Math.round(kr.width), h: Math.round(kr.height), radius: cs.borderRadius, transitionDuration: cs.transitionDuration, transitionProperty: cs.transitionProperty};
  };
  // rung 1: pointer parked at (5,5) — the at-rest state
  const r1 = read();
  // rung 2: pointer at the CARD's center — the row reveals, kebab unhovered
  const cx = Math.round(cr.left + cr.width / 2), cy = Math.round(cr.top + cr.height / 2);
  const kx = Math.round(kr.left + kr.width / 2), ky = Math.round(kr.top + kr.height / 2);
  return JSON.stringify({r1, cardCenter: [cx, cy], kebabCenter: [kx, ky]});
})()" 2>/dev/null | tail -1

agent-browser mouse move "$(agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find(d => typeof d.className === 'string' && d.className.includes('grid-cols-3'));
  const card = grid.children[0];
  const cr = card.getBoundingClientRect();
  return Math.round(cr.left + cr.width / 2) + ' ' + Math.round(cr.top + cr.height / 2);
})()" 2>/dev/null | tail -1 | tr -d '"')" >/dev/null 2>&1
sleep 1
echo "=== rung 2 read (pointer at card center) ==="
agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find(d => typeof d.className === 'string' && d.className.includes('grid-cols-3'));
  const card = grid.children[0];
  const kebab = [...card.querySelectorAll('button')].find(b => {
    const r = b.getBoundingClientRect();
    const t = (b.textContent || '').trim();
    return r.width > 20 && r.width <= 50 && Math.abs(r.width - r.height) < 6 && (!t || t.length < 3);
  });
  const cs = getComputedStyle(kebab);
  const kr = kebab.getBoundingClientRect();
  return JSON.stringify({hoverMatch: kebab.matches(':hover'), cardHover: card.matches(':hover'), opacity: cs.opacity, bg: cs.backgroundColor, color: cs.color, w: Math.round(kr.width), h: Math.round(kr.height)});
})()" 2>/dev/null | tail -1

agent-browser mouse move "$(agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find(d => typeof d.className === 'string' && d.className.includes('grid-cols-3'));
  const card = grid.children[0];
  const kebab = [...card.querySelectorAll('button')].find(b => {
    const r = b.getBoundingClientRect();
    const t = (b.textContent || '').trim();
    return r.width > 20 && r.width <= 50 && Math.abs(r.width - r.height) < 6 && (!t || t.length < 3);
  });
  const kr = kebab.getBoundingClientRect();
  return Math.round(kr.left + kr.width / 2) + ' ' + Math.round(kr.top + kr.height / 2);
})()" 2>/dev/null | tail -1 | tr -d '"')" >/dev/null 2>&1
sleep 1
echo "=== rung 3 read (pointer at the kebab's own center — the OWN-HOVER state) ==="
agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find(d => typeof d.className === 'string' && d.className.includes('grid-cols-3'));
  const card = grid.children[0];
  const kebab = [...card.querySelectorAll('button')].find(b => {
    const r = b.getBoundingClientRect();
    const t = (b.textContent || '').trim();
    return r.width > 20 && r.width <= 50 && Math.abs(r.width - r.height) < 6 && (!t || t.length < 3);
  });
  const cs = getComputedStyle(kebab);
  return JSON.stringify({hoverMatch: kebab.matches(':hover'), cardHover: card.matches(':hover'), opacity: cs.opacity, bg: cs.backgroundColor, color: cs.color, radius: cs.borderRadius, transitionDuration: cs.transitionDuration});
})()" 2>/dev/null | tail -1

agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== rung 4 read (pointer re-parked — the restore) ==="
agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find(d => typeof d.className === 'string' && d.className.includes('grid-cols-3'));
  const card = grid.children[0];
  const kebab = [...card.querySelectorAll('button')].find(b => {
    const r = b.getBoundingClientRect();
    const t = (b.textContent || '').trim();
    return r.width > 20 && r.width <= 50 && Math.abs(r.width - r.height) < 6 && (!t || t.length < 3);
  });
  const cs = getComputedStyle(kebab);
  return JSON.stringify({hoverMatch: kebab.matches(':hover'), cardHover: card.matches(':hover'), opacity: cs.opacity, bg: cs.backgroundColor, color: cs.color});
})()" 2>/dev/null | tail -1

echo "=== survey done ==="
