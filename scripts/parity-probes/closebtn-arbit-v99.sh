#!/usr/bin/env bash
# closebtn-arbit-v99.sh — the one-shot REFERENCE-side close-button
# geometric census (the v98 unlabelled-trigger finder class applied to the
# calculator dialog's X button: the census JS's aria-label/text finder
# misses the reference's textless SVG button, so this probe finds it
# GEOMETRICALLY — the last textless small button in the panel's header row).
# READ-ONLY: login + dialog-open only (the v46 rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="refclose99"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
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
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 3

# open the Rent calculator (the reference's own Rent card carries the line item)
# — the vlm-shots finder (div.rounded-xl + 'Rent' + '$25') + a REAL mouse
# click (the v98 pointer-sequence lesson: the reference's React tree needs
# the full native pointer event sequence)
POS=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
  if (!card) return 'ERR';
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
echo "rent card center: $POS"
X=$(echo "$POS" | cut -d, -f1); Y=$(echo "$POS" | cut -d, -f2)
agent-browser mouse move "$X" "$Y" >/dev/null 2>&1
sleep 1
CALC=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate\$/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
echo "calculate button center: $CALC"
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3

agent-browser eval "(async () => {
  let panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!panel) panel = [...document.querySelectorAll('div')].find(d => getComputedStyle(d).maxWidth === '768px' && d.getBoundingClientRect().width > 300);
  if (!panel) return 'no panel';
  const pr = panel.getBoundingClientRect();
  // GEOMETRIC: every visible button fully inside the panel's header band
  // (top 120px of the panel), with its chrome
  const btns = [...panel.querySelectorAll('button')].map(b => {
    const r = b.getBoundingClientRect();
    const s = getComputedStyle(b);
    return { txt: (b.textContent||'').trim().slice(0, 20), aria: b.getAttribute('aria-label') || null,
             x: Math.round(r.x - pr.x), y: Math.round(r.y - pr.y), w: Math.round(r.width), h: Math.round(r.height),
             radius: s.borderRadius, bg: s.backgroundColor, border: s.borderTopWidth + ' ' + s.borderTopColor,
             svg: b.querySelectorAll('svg').length };
  }).filter(b => b.w > 0 && b.h > 0 && b.y < 120);
  return JSON.stringify(btns);
})()" 2>/dev/null | tail -1
