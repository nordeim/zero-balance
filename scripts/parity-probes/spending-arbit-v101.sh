#!/usr/bin/env bash
# spending-arbit-v101.sh — the REFERENCE half of the supplemental two-half
# census for the v101 pin's axes (the DASHBOARD's spending+guidelines
# 2-col row's grid chrome + the Spending Breakdown card's box/header at
# 1280). READ-ONLY (login + passive navigation only — the v46 rule). THE
# TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v100 lesson).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

SPEND_JS="(async () => {
  const out = { view: 'spending-row-1280-v101', docSW: document.documentElement.scrollWidth, vw: window.innerWidth };
  // THE SPENDING CARD (the leaf title -> the bordered card walk — the v61
  // F2 pattern: shadow + radius + a <p> descendant).
  const title = [...document.querySelectorAll('h1,h2,h3,h4,div,span,p')].find(
    (e) => (e.textContent || '').trim() === 'Spending Breakdown' && e.children.length === 0
  );
  if (!title) return JSON.stringify({ err: 'no title' });
  let card = title;
  while (card.parentElement) {
    const cs = getComputedStyle(card);
    if (cs.boxShadow !== 'none' && cs.borderRadius !== '0px' && card.querySelector('p')) break;
    card = card.parentElement;
  }
  const csC = getComputedStyle(card);
  const rC = card.getBoundingClientRect();
  out.card = { w: Math.round(rC.width), h: Math.round(rC.height), radius: csC.borderRadius, border: csC.borderTopColor, bg: csC.backgroundColor, shadow: csC.boxShadow };
  // THE HEADER BLOCK (the title's parent) + the subtitle.
  const header = title.parentElement;
  const csH = getComputedStyle(header);
  const rT = title.getBoundingClientRect();
  const subtitle = header ? header.querySelector('p') : null;
  const rS = subtitle ? subtitle.getBoundingClientRect() : null;
  out.header = { pad: csH.padding };
  out.title = { fs: getComputedStyle(title).fontSize, fw: getComputedStyle(title).fontWeight, color: getComputedStyle(title).color, lh: getComputedStyle(title).lineHeight, tracking: getComputedStyle(title).letterSpacing };
  out.subtitle = subtitle && rS ? { text: (subtitle.textContent || '').trim(), fs: getComputedStyle(subtitle).fontSize, fw: getComputedStyle(subtitle).fontWeight, color: getComputedStyle(subtitle).color, lh: getComputedStyle(subtitle).lineHeight, top: Math.round(rS.top - rT.bottom) } : null;
  // THE BODY (the card's non-header child — the p-6 pt-0 contract).
  const body = [...card.children].find((c) => c !== header);
  out.body = body ? { pad: getComputedStyle(body).padding } : null;
  // THE ROW (the ancestor 2-col grid — the v61 F2 walk).
  let row = card.parentElement;
  while (row) {
    const cls = (row.className || '').toString();
    if (/grid-cols-2/.test(cls) && row.children.length === 2) break;
    row = row.parentElement;
  }
  if (!row) return JSON.stringify({ err: 'no row' });
  const csR = getComputedStyle(row);
  const rR = row.getBoundingClientRect();
  out.row = { display: csR.display, template: csR.gridTemplateColumns, colGap: csR.columnGap, w: Math.round(rR.width), h: Math.round(rR.height) };
  // THE TWO CHILDREN (the spending card + the guidelines wrapper).
  const kids = [...row.children].map((k) => {
    const kr = k.getBoundingClientRect();
    return { w: Math.round(kr.width), h: Math.round(kr.height), display: getComputedStyle(k).display };
  });
  out.children = kids;
  return JSON.stringify(out);
})()"

export AGENT_BROWSER_SESSION="refspend101"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
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
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$SPEND_JS" 2>/dev/null | tail -1
echo "=== ref spending arbit v101 half done ==="
