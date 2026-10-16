#!/usr/bin/env bash
# vlm-shots-v72.sh — the v72 NEW-pair program, REFERENCE side: the
# DETAILS-SHEET + DRILL-DOWN mobile 390x844 twins —
#   (1) the WITH-subtitle details sheet (the Rent card, subcategory
#       "Apartment" — the seeded twin both sides share),
#   (2) the EMPTY-subcategory details sheet (the Miscellaneous card — the
#       v71 fix's SIBLING surface: the v52 sheet conditional's empty side
#       was never shot against the reference's own empty-side sheet, the
#       v52 assumption "every reference item carries a subcategory"
#       disproven by v71's card-side discovery),
#   (3) the dashboard's drill-down EXPANDED state at 390 (the v67 pair's
#       MOBILE twin — the desktop expanded pair was re-run v67; the 390
#       expanded state was never shot).
# READ-ONLY: login + passive navigation + VIEW-STATE clicks only (the v46
# incident rule — the card-open and drill-expand clicks mutate no data).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm72

export AGENT_BROWSER_SESSION="refvlm72"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1

# (1) The Rent card's details sheet (WITH subtitle) — the card body click
# opens the read-only sheet (the v28 G3 contract; the reference's card
# root is div.rounded-xl.cursor-pointer — the CARD ROOT click is the
# verified mechanism, and the reference's sheet carries NO role=dialog:
# the detection censuses the fixed inset-0 z-50 overlay whose text starts
# with "Budget Item Details").
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const h4 = [...document.querySelectorAll('h4')].find(h => (h.textContent||'').trim() === 'Rent');
  const card = h4 ? h4.closest('div.rounded-xl') : null;
  if (!card) return 'no Rent card';
  card.click();
  return 'Rent clicked';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('div')].find(d => {
    const s = getComputedStyle(d);
    return s.position === 'fixed' && parseInt(s.zIndex||'0') >= 50 && (d.textContent||'').trim().startsWith('Budget Item Details');
  });
  return JSON.stringify({ sheetOpen: !!dlg, head: dlg ? (dlg.textContent||'').trim().slice(0, 60) : '' });
})()" 2>/dev/null | tail -1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot /tmp/vlm72/ref-sheet-withsub.png 2>/dev/null | tail -1

# (2) The Miscellaneous card's details sheet (EMPTY subcategory) — a fresh
# navigation resets the prior sheet state.
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const h4 = [...document.querySelectorAll('h4')].find(h => (h.textContent||'').trim() === 'Miscellaneous');
  const card = h4 ? h4.closest('div.rounded-xl') : null;
  if (!card) return 'no Miscellaneous card';
  card.click();
  return 'Miscellaneous clicked';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('div')].find(d => {
    const s = getComputedStyle(d);
    return s.position === 'fixed' && parseInt(s.zIndex||'0') >= 50 && (d.textContent||'').trim().startsWith('Budget Item Details');
  });
  return JSON.stringify({ sheetOpen: !!dlg, head: dlg ? (dlg.textContent||'').trim().slice(0, 60) : '' });
})()" 2>/dev/null | tail -1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot /tmp/vlm72/ref-sheet-nosub.png 2>/dev/null | tail -1

# (3) The dashboard's drill-down EXPANDED state at mobile 390 — expand the
# Total Income section, then its first category (view-state clicks only —
# the v67 pattern, re-run at the mobile twin).
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const sec = [...card.querySelectorAll('button')].find(b => /Total Income/i.test(b.textContent||''));
  if (!sec) return 'no section';
  sec.click();
  return 'section clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const cat = [...card.querySelectorAll('button')].find(b => b.offsetParent !== null && /\\\$/.test(b.textContent||'') && !/Total|Net Balance/i.test(b.textContent||''));
  if (!cat) return 'no category';
  cat.click();
  return 'category clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm72/ref-drilldown-mobile.png 2>/dev/null | tail -1

echo "ref v72 shots done (sheet-withsub + sheet-nosub + drilldown-mobile)"
