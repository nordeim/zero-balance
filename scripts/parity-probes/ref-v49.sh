#!/usr/bin/env bash
# ref-v49.sh — the reference-side driver for the three v49 surfaces,
# measured live on the reference (READ-ONLY: the login-page census is
# pre-auth; the donut legend census is a passive read; the calculator
# opens via its Calculate click + census + Cancel close — no saves, no
# deletes, the v46 incident rule).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="ref49b"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3

echo "=== REF surface 1: the LOGIN PANEL at 390 (logged out) ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('div')].find(d => {
    const cs = getComputedStyle(d);
    return cs.borderRadius !== '0px' && d.getBoundingClientRect().width >= 300 && d.getBoundingClientRect().width <= 390 && d.querySelector && d.querySelector('input[type=email]');
  }) || document.querySelector('form')?.parentElement;
  if (!panel) return 'no panel';
  const cs = getComputedStyle(panel);
  const r = panel.getBoundingClientRect();
  const bar = panel.querySelector('div[class*=h-1], div[style*=height]') ;
  const content = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).padding && d.querySelector('h1, h2'));
  const csC = content ? getComputedStyle(content) : null;
  const h1 = panel.querySelector('h1, h2');
  return JSON.stringify({
    panel: { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), radius: cs.borderRadius, maxW: cs.maxWidth, shadow: cs.boxShadow, bg: cs.backgroundColor, border: cs.borderWidth + ' ' + cs.borderColor, pad: cs.padding, cls: panel.className.toString().slice(0,110) },
    contentPad: csC ? csC.padding : null,
    heading: h1 ? { fs: getComputedStyle(h1).fontSize, fw: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color } : null
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== login the reference (for surfaces 2+3) ==="
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
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

echo "=== REF surface 2: the DONUT LEGEND at 390 (dashboard) ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  // the legend rows: rounded-lg p-3 blocks with a tinted bg, inside the
  // breakdown card; each row carries a label + an amount + a percent.
  const rows = [...document.querySelectorAll('div')].filter(d => {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return cs.borderRadius === '8px' && cs.padding === '12px' && r.width > 200 && r.width < 360 && (d.textContent||'').includes('%');
  });
  if (!rows.length) return 'no legend rows';
  const container = rows[0].parentElement;
  const csCont = getComputedStyle(container);
  const row = rows[0];
  const cs = getComputedStyle(row);
  const r = row.getBoundingClientRect();
  // the left dot: the first small square child
  const dot = [...row.querySelectorAll('div, span')].find(el => {
    const rr = el.getBoundingClientRect();
    return rr.width >= 14 && rr.width <= 20 && rr.height >= 14 && rr.height <= 20;
  });
  const label = row.querySelector('span, p, h1, h2, h3, h4');
  const amount = [...row.querySelectorAll('p, span, div')].filter(el => (el.textContent||'').trim().startsWith('\$'))[0];
  const pct = [...row.querySelectorAll('p, span, div')].filter(el => /%\$/.test((el.textContent||'').trim() + '') || (el.textContent||'').trim().endsWith('%'))[0];
  return JSON.stringify({
    container: { display: csCont.display, gap: csCont.gap, mt: csCont.marginTop, w: Math.round(container.getBoundingClientRect().width) },
    rowCount: rows.length,
    row: { w: Math.round(r.width), h: Math.round(r.height), radius: cs.borderRadius, pad: cs.padding, bg: cs.backgroundColor, cls: row.className.toString().slice(0,90) },
    dot: dot ? { w: Math.round(dot.getBoundingClientRect().width), h: Math.round(dot.getBoundingClientRect().height), radius: getComputedStyle(dot).borderRadius, bg: getComputedStyle(dot).backgroundColor } : null,
    label: label ? { fs: getComputedStyle(label).fontSize, fw: getComputedStyle(label).fontWeight, color: getComputedStyle(label).color, text: label.textContent.trim().slice(0,20) } : null,
    amount: amount ? { fs: getComputedStyle(amount).fontSize, fw: getComputedStyle(amount).fontWeight, color: getComputedStyle(amount).color, text: amount.textContent.trim() } : null,
    pct: pct ? { fs: getComputedStyle(pct).fontSize, color: getComputedStyle(pct).color, text: pct.textContent.trim() } : null
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== REF surface 3: the CALCULATOR DIALOG at 640 (read-only open+census+close) ==="
agent-browser set viewport 640 960 >/dev/null 2>&1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  // the expense cards' Calculate button (hover-revealed but clickable)
  const btn = [...document.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Calculate');
  if (!btn) return 'no Calculate button';
  btn.click();
  await new Promise(r => setTimeout(r, 1200));
  return 'calculator clicked';
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => {
  // the reference's calculator layer: fixed inset-0 z-50 (no role=dialog)
  const layer = [...document.querySelectorAll('div')].find(d => d.className && d.className.toString().includes('fixed inset-0') && (d.textContent||'').includes('Total Calculated'));
  if (!layer) return 'no calculator layer';
  const panel = [...layer.children].find(c => getComputedStyle(c).position !== 'fixed') || layer.children[0];
  const cs = getComputedStyle(panel);
  const r = panel.getBoundingClientRect();
  const closeBtn = [...panel.querySelectorAll('button')].filter(b => !b.textContent.trim())[0];
  const hdr = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).borderBottomWidth !== '0px');
  return JSON.stringify({
    panel: { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), radius: cs.borderRadius, maxW: cs.maxWidth, maxH: cs.maxHeight, shadow: cs.boxShadow, bg: cs.backgroundColor, overflow: cs.overflow, cls: panel.className.toString().slice(0,120) },
    closeBtn: closeBtn ? { w: Math.round(closeBtn.getBoundingClientRect().width), h: Math.round(closeBtn.getBoundingClientRect().height) } : null,
    hdrBorder: hdr ? getComputedStyle(hdr).borderBottom : null,
    sw: document.documentElement.scrollWidth
  });
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => {
  // close via Cancel (read-only — never a save)
  const cancel = [...document.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Cancel');
  if (cancel) { cancel.click(); await new Promise(r=>setTimeout(r,600)); return 'cancelled'; }
  const x = [...document.querySelectorAll('button')].filter(b => !b.textContent.trim());
  if (x.length) { x[x.length-1].click(); await new Promise(r=>setTimeout(r,600)); return 'x-closed'; }
  return 'no close path';
})()" 2>/dev/null | tail -1
echo "=== ref v49 driver done ==="
