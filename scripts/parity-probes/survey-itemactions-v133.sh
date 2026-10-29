#!/usr/bin/env bash
# survey-itemactions-v133.sh — the v133 candidate-survey probe v2 (READ-ONLY,
# the v46 rule): the reference's first EXPENSE card carries TWO action
# buttons (Edit + Calculate — NO kebab; the kebab is the clone's superset
# #7). Measure BOTH buttons' own-hover ladders live at 1280x800 — the
# at-rest rung (pointer parked), the card-hover rung (the reveal state,
# buttons unhovered), the OWN-HOVER rung (the pointer at each button's
# own center), the restore — plus the action-row container's opacity at
# each rung, so the census can be shaped STATE-INDEPENDENTLY (the v107
# lesson; the v131/v132 survey precedents).
# READ-ONLY: hover reveals chrome, nothing is clicked.
set -u
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refsurvey133b"
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

READ_JS="(async () => {
  const grid = [...document.querySelectorAll('div')].find(d => typeof d.className === 'string' && d.className.includes('grid-cols-3'));
  if (!grid) return JSON.stringify({error: 'no grid'});
  const card = grid.children[0];
  // the action-row container: the positioned ancestor of the buttons
  const edit = [...card.querySelectorAll('button')].find(b => (b.textContent || '').trim() === 'Edit');
  const calc = [...card.querySelectorAll('button')].find(b => (b.textContent || '').trim() === 'Calculate');
  if (!edit || !calc) return JSON.stringify({error: 'buttons missing'});
  let row = edit.parentElement;
  while (row && row !== card) {
    const cs = getComputedStyle(row);
    if (cs.position === 'absolute') break;
    row = row.parentElement;
  }
  const rd = (b) => {
    const cs = getComputedStyle(b);
    const r = b.getBoundingClientRect();
    return {hoverMatch: b.matches(':hover'), bg: cs.backgroundColor, color: cs.color, border: cs.borderColor, shadow: cs.boxShadow.slice(0, 80), w: Math.round(r.width), h: Math.round(r.height), transitionDuration: cs.transitionDuration};
  };
  const rowCs = row ? getComputedStyle(row) : null;
  return JSON.stringify({
    edit: rd(edit), calc: rd(calc),
    row: rowCs ? {position: rowCs.position, opacity: rowCs.opacity, top: rowCs.top, right: rowCs.right, gap: rowCs.gap} : null,
    cardHover: card.matches(':hover'),
    editCenter: [Math.round(edit.getBoundingClientRect().left + edit.getBoundingClientRect().width / 2), Math.round(edit.getBoundingClientRect().top + edit.getBoundingClientRect().height / 2)],
    calcCenter: [Math.round(calc.getBoundingClientRect().left + calc.getBoundingClientRect().width / 2), Math.round(calc.getBoundingClientRect().top + calc.getBoundingClientRect().height / 2)]
  });
})()"

echo "=== rung 1: at-rest (pointer parked at 5,5) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$READ_JS" 2>/dev/null | tail -1

echo "=== rung 2: OWN-HOVER the Edit button (pointer at its center) ==="
EDIT_XY=$(agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find(d => typeof d.className === 'string' && d.className.includes('grid-cols-3'));
  const card = grid.children[0];
  const edit = [...card.querySelectorAll('button')].find(b => (b.textContent || '').trim() === 'Edit');
  const r = edit.getBoundingClientRect();
  return Math.round(r.left + r.width / 2) + ' ' + Math.round(r.top + r.height / 2);
})()" 2>/dev/null | tail -1 | tr -d '"')
agent-browser mouse move $EDIT_XY >/dev/null 2>&1
sleep 1
agent-browser eval "$READ_JS" 2>/dev/null | tail -1

echo "=== rung 3: OWN-HOVER the Calculate button (pointer at its center) ==="
CALC_XY=$(agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find(d => typeof d.className === 'string' && d.className.includes('grid-cols-3'));
  const card = grid.children[0];
  const calc = [...card.querySelectorAll('button')].find(b => (b.textContent || '').trim() === 'Calculate');
  const r = calc.getBoundingClientRect();
  return Math.round(r.left + r.width / 2) + ' ' + Math.round(r.top + r.height / 2);
})()" 2>/dev/null | tail -1 | tr -d '"')
agent-browser mouse move $CALC_XY >/dev/null 2>&1
sleep 1
agent-browser eval "$READ_JS" 2>/dev/null | tail -1

echo "=== rung 4: restore (pointer re-parked at 5,5) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$READ_JS" 2>/dev/null | tail -1

echo "=== survey v2 done ==="
