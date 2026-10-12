#!/usr/bin/env bash
# clone-v51.sh — the clone-side driver for the three v51 surfaces
# (mirrors ref-v51.sh): (1) the dashboard's STATS ROW at 390; (2) the
# SAVINGS view at 390 (goal-card + view chrome); (3) the BUDGET
# GUIDELINES card at 390. Via with-server on :3200. Read-only.
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
BASE="http://localhost:3200"
export AGENT_BROWSER_SESSION="clone51"

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
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4

echo ""
echo "=== CLONE surface 1: the DASHBOARD STATS ROW at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const h3 = [...document.querySelectorAll('h3')].find(x => (x.textContent||'').trim() === 'Total Income');
  if (!h3) return 'no Total Income h3';
  let card = h3;
  while (card && card.parentElement) {
    const p = card.parentElement;
    if ([...p.children].filter(c => c.querySelector && [...c.querySelectorAll('h3')].some(h => /^(Total Income|Total Savings|Total Expenses)$/.test((h.textContent||'').trim()))).length >= 2) break;
    card = p;
  }
  const grid = card.parentElement;
  const csG = getComputedStyle(grid);
  const first = [...grid.children].find(c => c.querySelector && [...c.querySelectorAll('h3')].some(h => (h.textContent||'').trim() === 'Total Income'));
  const csC = getComputedStyle(first);
  const rC = first.getBoundingClientRect();
  const iconCircle = first.querySelector('[class*=rounded-xl], div');
  const ic = first.querySelector('svg');
  const amount = [...first.querySelectorAll('p')].find(p => /^[-+]?[0-9]/.test((p.textContent||'').trim()));
  const countRow = [...first.querySelectorAll('div')].filter(d => d.textContent.includes('item'));
  const trend = [...first.querySelectorAll('svg')].pop();
  const cards = [...grid.children].map(c => { const r = c.getBoundingClientRect(); return { w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y) }; });
  return JSON.stringify({
    grid: { display: csG.display, cols: csG.gridTemplateColumns, gap: csG.gap, children: grid.children.length },
    cards,
    firstCard: { w: Math.round(rC.width), h: Math.round(rC.height), radius: csC.borderRadius, pad: csC.padding, border: csC.border, bg: csC.backgroundColor, shadow: (csC.boxShadow||'none').slice(0, 70) },
    iconCircle: iconCircle ? { w: Math.round(iconCircle.getBoundingClientRect().width), h: Math.round(iconCircle.getBoundingClientRect().height), radius: getComputedStyle(iconCircle).borderRadius, bg: getComputedStyle(iconCircle).backgroundColor } : null,
    icon: ic ? { w: Math.round(ic.getBoundingClientRect().width), h: Math.round(ic.getBoundingClientRect().height), color: getComputedStyle(ic).color } : null,
    title: { fs: getComputedStyle(h3).fontSize, fw: getComputedStyle(h3).fontWeight, color: getComputedStyle(h3).color, mb: getComputedStyle(h3).marginBottom },
    amount: amount ? { text: amount.textContent.trim().slice(0, 14), fs: getComputedStyle(amount).fontSize, fw: getComputedStyle(amount).fontWeight, color: getComputedStyle(amount).color, mb: getComputedStyle(amount).marginBottom } : null,
    countRow: countRow.length ? { fs: getComputedStyle(countRow[0]).fontSize, color: getComputedStyle(countRow[0]).color, gap: getComputedStyle(countRow[0]).gap } : null,
    trendIcon: trend ? { w: Math.round(trend.getBoundingClientRect().width), h: Math.round(trend.getBoundingClientRect().height) } : null
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE surface 2: the SAVINGS view at 390 (goal-card census) ==="
agent-browser open "$BASE/savings" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const h4s = [...document.querySelectorAll('h4')];
  if (!h4s.length) return 'no item cards (empty view?)';
  const first = h4s[0].closest('div[class*=rounded]');
  if (!first) return 'no card container';
  const csC = getComputedStyle(first);
  const rC = first.getBoundingClientRect();
  const titleEl = h4s[0];
  const amount = [...first.querySelectorAll('p')].find(p => /^[-+]?[0-9]/.test((p.textContent||'').trim()));
  const dot = first.querySelector('div[class*=rounded-[9999px]], .h-2');
  const badges = [...first.querySelectorAll('span')].filter(s => s.parentElement.className.toString().includes('flex-wrap'));
  const grid = first.parentElement;
  const csG = getComputedStyle(grid);
  return JSON.stringify({
    card: { w: Math.round(rC.width), h: Math.round(rC.height), radius: csC.borderRadius, pad: csC.padding, border: csC.border, bg: csC.backgroundColor, shadow: (csC.boxShadow||'none').slice(0, 70) },
    title: { text: (titleEl.textContent||'').trim().slice(0, 22), fs: getComputedStyle(titleEl).fontSize, fw: getComputedStyle(titleEl).fontWeight, color: getComputedStyle(titleEl).color },
    amount: amount ? { text: amount.textContent.trim().slice(0, 12), fs: getComputedStyle(amount).fontSize, fw: getComputedStyle(amount).fontWeight, color: getComputedStyle(amount).color } : null,
    dot: dot ? { w: Math.round(dot.getBoundingClientRect().width), h: Math.round(dot.getBoundingClientRect().height), bg: getComputedStyle(dot).backgroundColor } : null,
    badges: badges.map(b => ({ text: b.textContent.trim().slice(0, 14), fs: getComputedStyle(b).fontSize, pad: getComputedStyle(b).padding, radius: getComputedStyle(b).borderRadius })),
    grid: { display: csG.display, cols: csG.gridTemplateColumns, gap: csG.gap, children: grid.children.length },
    docSW: document.documentElement.scrollWidth
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE surface 2b: the SAVINGS view chrome at 390 (header + filter card) ==="
agent-browser eval "(async () => {
  const h1 = document.querySelector('h1, h2');
  if (!h1) return 'no header';
  const header = h1.closest('div');
  const sub = [...document.querySelectorAll('p')].find(p => (p.textContent||'').includes('item'));
  const search = document.querySelector('input[type=search], input[placeholder*=Search i]');
  let filterCard = search;
  while (filterCard && filterCard.parentElement && !getComputedStyle(filterCard).borderRadius.includes('16')) filterCard = filterCard.parentElement;
  const csF = filterCard ? getComputedStyle(filterCard) : null;
  const csH = getComputedStyle(h1);
  return JSON.stringify({
    header: { text: h1.textContent.trim().slice(0, 14), fs: csH.fontSize, fw: csH.fontWeight, color: csH.color },
    sub: sub ? { text: sub.textContent.trim().slice(0, 20), fs: getComputedStyle(sub).fontSize, color: getComputedStyle(sub).color } : null,
    filterCard: csF ? { w: Math.round(filterCard.getBoundingClientRect().width), radius: csF.borderRadius, pad: csF.padding, bg: csF.backgroundColor, border: csF.border } : null,
    search: search ? { w: Math.round(search.getBoundingClientRect().width), h: Math.round(search.getBoundingClientRect().height) } : null
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE surface 3: the BUDGET GUIDELINES card at 390 ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const heading = [...document.querySelectorAll('h1, h2, h3, div')].find(x => (x.textContent||'').trim() === 'Budget Guidelines');
  if (!heading) return 'no Budget Guidelines heading';
  let card = heading;
  while (card && card.parentElement && !(getComputedStyle(card).boxShadow !== 'none' && getComputedStyle(card).borderRadius && card.querySelector('span, p'))) card = card.parentElement;
  const csC = getComputedStyle(card);
  const rC = card.getBoundingClientRect();
  const tiles = [...card.querySelectorAll('div')].filter(d => {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return cs.borderRadius === '8px' && r.height > 60 && r.height < 200 && d.querySelector('span, p') && cs.backgroundColor !== 'rgba(0, 0, 0, 0)';
  });
  const grid = tiles.length ? tiles[0].parentElement : null;
  return JSON.stringify({
    card: { w: Math.round(rC.width), h: Math.round(rC.height), radius: csC.borderRadius, pad: csC.padding, border: csC.border, bg: csC.backgroundColor, shadow: (csC.boxShadow||'none').slice(0, 60) },
    grid: grid ? { display: getComputedStyle(grid).display, cols: getComputedStyle(grid).gridTemplateColumns, gap: getComputedStyle(grid).gap, children: grid.children.length } : null,
    tiles: tiles.slice(0, 3).map(t => {
      const cs = getComputedStyle(t);
      const r = t.getBoundingClientRect();
      const label = t.querySelector('span');
      const pct = [...t.querySelectorAll('span')].pop();
      const desc = t.querySelector('p');
      return {
        w: Math.round(r.width), h: Math.round(r.height), radius: cs.borderRadius, pad: cs.padding, bg: cs.backgroundColor, border: cs.border,
        label: label ? { text: label.textContent.trim().slice(0, 12), fs: getComputedStyle(label).fontSize, fw: getComputedStyle(label).fontWeight, color: getComputedStyle(label).color } : null,
        pct: pct && pct !== label ? { text: pct.textContent.trim().slice(0, 8), fs: getComputedStyle(pct).fontSize, color: getComputedStyle(pct).color } : null,
        desc: desc ? { fs: getComputedStyle(desc).fontSize, color: getComputedStyle(desc).color } : null
      };
    })
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== clone-v51 done ==="
EOF
