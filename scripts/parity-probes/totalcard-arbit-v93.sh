#!/usr/bin/env bash
# totalcard-arbit-v93.sh — the ONE-SHOT census for the v93 pin's own
# axes, REFERENCE half (the v87/v88/v89/v90/v91/v92 supplemental
# precedent, BUILT TWO-HALF from the start): the CALCULATOR DIALOG's
# TOTAL-CARD inner-text census at desktop 1280 — the v73 390 family's
# DESKTOP twin (the summary amount + the based-on line + the
# data-conditional will-update span, all pinned at 390 only, never at
# 1280) PLUS the "Total Calculated" LABEL leaf's chrome (never pinned
# at ANY viewport — only toBeVisible elsewhere). The reference's OWN
# Rent calculator natively carries the single "Contents Insurance"
# $25.00 monthly-active line item (the v45 measurement note) — the
# census rides that native 1-row state, READ-ONLY (login + hover +
# dialog-open only — the v46 rule; no form saves, no deletes).
# Double-quoted-heredoc-safe: no literal dollar sequences (the amount
# leaf matched via String.fromCharCode(36) — the v64 rule); no
# backticks.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const out = {};
  let panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!panel) panel = [...document.querySelectorAll('div')].find(d => getComputedStyle(d).maxWidth === '768px' && d.getBoundingClientRect().width > 300);
  if (!panel) return JSON.stringify({ panel: 'not found' });
  const totalCard = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).backgroundColor === 'rgb(255, 247, 245)');
  if (!totalCard) return JSON.stringify({ totalCard: 'not found' });
  const D = String.fromCharCode(36);
  const leaf = (scope, test) => [...scope.querySelectorAll('*')].find(e => e.children.length === 0 && test((e.textContent||'').trim()));
  const labelEl = leaf(totalCard, t => t === 'Total Calculated');
  const amountEl = leaf(totalCard, t => t === D + '25.00');
  const basedOnEl = leaf(totalCard, t => /^Based on 1 item$/.test(t));
  const willUpdateEl = leaf(totalCard, t => /Will update category total/.test(t));
  if (labelEl) { const s = getComputedStyle(labelEl); out.label = { fs: s.fontSize, fw: s.fontWeight, lh: s.lineHeight, color: s.color }; }
  if (amountEl) { const s = getComputedStyle(amountEl); out.amount = { fs: s.fontSize, fw: s.fontWeight, lh: s.lineHeight, color: s.color }; }
  if (basedOnEl) { const s = getComputedStyle(basedOnEl); out.basedOn = { fs: s.fontSize, lh: s.lineHeight, color: s.color }; }
  out.willUpdate = willUpdateEl ? (() => { const s = getComputedStyle(willUpdateEl); return { fs: s.fontSize, fw: s.fontWeight, color: s.color }; })() : 'absent';
  const topRow = labelEl ? labelEl.parentElement : null;
  if (topRow) { const s = getComputedStyle(topRow); out.topRow = { display: s.display, justify: s.justifyContent, align: s.alignItems, mb: s.marginBottom }; }
  const bottomRow = basedOnEl ? basedOnEl.parentElement : null;
  if (bottomRow) { const s = getComputedStyle(bottomRow); out.bottomRow = { display: s.display, justify: s.justifyContent, fs: s.fontSize, color: s.color }; }
  const tcs = getComputedStyle(totalCard); const tr = totalCard.getBoundingClientRect();
  out.totalCard = { w: Math.round(tr.width), h: Math.round(tr.height), pad: tcs.padding, radius: tcs.borderRadius, border: tcs.border };
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

echo "########## REFERENCE SIDE (the native 1-row state — read-only) ##########"
export AGENT_BROWSER_SESSION="reftc93"
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
  echo "ref login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
POS=""
for attempt in 1 2 3 4 5; do
  POS=$(agent-browser eval "(async () => {
    const main = document.querySelector('main')||document.body;
    const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
    if (!card) return 'ERR';
    const r = card.getBoundingClientRect();
    return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
  })()" 2>/dev/null | tail -1 | tr -d '"')
  if [ "$POS" != "ERR" ] && [ -n "$POS" ]; then break; fi
  echo "rent card not ready (attempt $attempt), waiting..."
  sleep 4
done
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
# park the pointer FAR from the dialog before the census (the rest state)
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 2
echo "=== REF totalCard inner-text census (label + amount + basedOn + willUpdate + rows + card) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== ref totalcard arbit v93 half done ==="
