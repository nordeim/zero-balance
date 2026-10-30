#!/usr/bin/env bash
# ref-standing-v129.sh — the 129th standing check, reference side:
# login + the four reference bugs (toast-blocker, sheet-trap, no-landmark,
# /networth overflow) + the read-only data census + the SEO pair.
# READ-ONLY discipline: no Delete clicks, no form saves (the v46 incident rule).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="ref129"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
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

echo "=== R-bug 1: toast-blocker (elementFromPoint at the burger's center) ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const b = [...document.querySelectorAll('button')].find(x => (x.getAttribute('aria-label')||'').includes('menu') || (x.textContent||'').includes('menu'));
  const burger = b || [...document.querySelectorAll('button')].find(x => x.getBoundingClientRect().top < 80 && x.getBoundingClientRect().left < 80 && x.getBoundingClientRect().width < 60);
  if (!burger) return 'no burger found';
  const r = burger.getBoundingClientRect();
  const hit = document.elementFromPoint(r.x + r.width/2, r.y + r.height/2);
  return JSON.stringify({
    burger: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width) },
    hitTag: hit ? hit.tagName + '.' + (hit.className||'').toString().slice(0,60) : 'null',
    hitIsBurgerChild: burger.contains(hit)
  });
})()" 2>/dev/null | tail -1

echo "=== R-bug 2: sheet-trap (open sheet, click nav, sheet stays?) ==="
agent-browser eval "(async () => {
  const b = [...document.querySelectorAll('button')].find(x => (x.getAttribute('aria-label')||'').includes('menu') || (x.textContent||'').includes('menu'));
  const burger = b || [...document.querySelectorAll('button')].find(x => x.getBoundingClientRect().top < 80 && x.getBoundingClientRect().left < 80 && x.getBoundingClientRect().width < 60);
  if (burger) { burger.click(); return 'burger clicked'; }
  return 'no burger';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const link = [...document.querySelectorAll('a')].filter(l => (l.getAttribute('href')||'').includes('income') && l.getBoundingClientRect().width > 0)[0];
  if (link) { link.click(); return 'clicked income link'; }
  return 'no link';
})()" 2>/dev/null | tail -1
sleep 3
agent-browser eval "(async () => {
  const overlay = [...document.querySelectorAll('div')].filter(d => {
    const s = getComputedStyle(d);
    return s.position === 'fixed' && d.getBoundingClientRect().width > 300 && d.getBoundingClientRect().height > 700 && s.backgroundColor && s.backgroundColor !== 'rgba(0, 0, 0, 0)';
  });
  const sheetOpen = overlay.some(o => (o.textContent||'').includes('Income') || (o.textContent||'').includes('Savings'));
  return JSON.stringify({ sheetOpenAfterNav: sheetOpen, overlayCount: overlay.length });
})()" 2>/dev/null | tail -1
# close the sheet if stuck open (the bug itself) — click overlay
agent-browser eval "(async () => {
  const overlay = [...document.querySelectorAll('div')].filter(d => {
    const s = getComputedStyle(d);
    return s.position === 'fixed' && s.zIndex !== 'auto' && parseInt(s.zIndex||'0') >= 50 && d.getBoundingClientRect().width > 300;
  });
  if (overlay.length) { overlay[overlay.length-1].click(); return 'overlay clicked'; }
  return 'no overlay';
})()" 2>/dev/null | tail -1
sleep 2

echo "=== R-bug 3: no nav landmark ==="
agent-browser eval "(async () => {
  return JSON.stringify({ navLandmark: !!document.querySelector('nav') });
})()" 2>/dev/null | tail -1

echo "=== R-bug 4: /networth horizontal overflow at 390 ==="
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  return JSON.stringify({ docSW: document.documentElement.scrollWidth, vw: window.innerWidth });
})()" 2>/dev/null | tail -1

echo "=== DATA CENSUS (read-only) ==="
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 2
agent-browser eval "(async () => {
  const t = (document.querySelector('main')||document.body).textContent;
  const m = t.match(/(\d+)\s*items?\s*·\s*\\\$?([\d,]+\.?\d*)/);
  return JSON.stringify({ networth: m ? m[0] : 'no match' });
})()" 2>/dev/null | tail -1
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 2
agent-browser eval "(async () => {
  const t = (document.querySelector('main')||document.body).textContent;
  const m = t.match(/(\d+)\s*items?\s*·\s*\\\$?([\d,]+\.?\d*)/);
  return JSON.stringify({ income: m ? m[0] : 'no match' });
})()" 2>/dev/null | tail -1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 2
agent-browser eval "(async () => {
  const t = (document.querySelector('main')||document.body).textContent;
  const m = t.match(/(\d+)\s*items?\s*·\s*\\\$?([\d,]+\.?\d*)/);
  return JSON.stringify({ expenses: m ? m[0] : 'no match' });
})()" 2>/dev/null | tail -1

echo "=== SEO PAIR ==="
agent-browser open "$BASE/robots.txt" >/dev/null 2>&1
sleep 2
agent-browser eval "(async () => { return document.body.textContent.slice(0, 120); })()" 2>/dev/null | tail -1
agent-browser open "$BASE/sitemap.xml" >/dev/null 2>&1
sleep 2
agent-browser eval "(async () => { return document.body.textContent.slice(0, 200); })()" 2>/dev/null | tail -1
echo "=== ref standing v129 done ==="
