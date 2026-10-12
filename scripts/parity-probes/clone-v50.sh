#!/usr/bin/env bash
# clone-v50.sh — the clone-side driver for the three v50 surfaces
# (mirrors ref-v50.sh): (1) the auth states' FULL 390 census — sign-in
# baseline + the sign-up state + the forgot state; (2) the networth
# tablist's chrome at 640; (3) the dashboard hero's mobile reflow at 390.
# Via with-server on :3200. Read-only (client state swaps only).
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
BASE="http://localhost:3200"
export AGENT_BROWSER_SESSION="clone50"

echo "=== CLONE surface 1a: the SIGN-IN state baseline at 390 ==="
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const wrapper = [...document.querySelectorAll('div')].find(d => d.className.toString().includes('max-w-md')) || document.querySelector('main > div');
  if (!wrapper) return 'no wrapper';
  const panel = wrapper.firstElementChild;
  const spacer = wrapper.children.length > 1 ? wrapper.children[1] : null;
  const csP = getComputedStyle(panel);
  const rP = panel.getBoundingClientRect();
  const h1 = panel.querySelector('h1, h2');
  return JSON.stringify({
    wrapper: { children: wrapper.children.length, w: Math.round(wrapper.getBoundingClientRect().width), h: Math.round(wrapper.getBoundingClientRect().height) },
    panel: { w: Math.round(rP.width), h: Math.round(rP.height), y: Math.round(rP.y), radius: csP.borderRadius, bg: csP.backgroundColor, shadow: csP.boxShadow.slice(0, 60) },
    spacer: spacer ? { tag: spacer.tagName, cls: spacer.className.toString().slice(0, 80), h: Math.round(spacer.getBoundingClientRect().height), display: getComputedStyle(spacer).display } : null,
    heading: h1 ? { text: h1.textContent.slice(0, 30), fs: getComputedStyle(h1).fontSize, fw: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color } : null
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE surface 1b: the SIGN-UP state at 390 (client state swap) ==="
agent-browser eval "(async () => {
  const link = [...document.querySelectorAll('button, a')].find(x => (x.textContent||'').includes('Sign up'));
  if (link) { link.click(); return 'sign-up link clicked'; }
  return 'no sign-up link';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const wrapper = [...document.querySelectorAll('div')].find(d => d.className.toString().includes('max-w-md')) || document.querySelector('main > div');
  if (!wrapper) return 'no wrapper';
  const panel = wrapper.firstElementChild;
  const spacer = wrapper.children.length > 1 ? wrapper.children[1] : null;
  const csP = getComputedStyle(panel);
  const rP = panel.getBoundingClientRect();
  const h1 = panel.querySelector('h1, h2');
  const inputs = [...panel.querySelectorAll('input:not([type=hidden])')].map(i => {
    const cs = getComputedStyle(i);
    const r = i.getBoundingClientRect();
    return { type: i.type, h: Math.round(r.height), w: Math.round(r.width), fs: cs.fontSize, ph: (i.placeholder||'').slice(0, 18) };
  });
  const submit = [...panel.querySelectorAll('button')].find(b => (b.textContent||'').match(/create|sign\s*up/i));
  const sub = submit ? { text: submit.textContent.trim().slice(0, 20), h: Math.round(submit.getBoundingClientRect().height), w: Math.round(submit.getBoundingClientRect().width), bg: getComputedStyle(submit).backgroundColor, color: getComputedStyle(submit).color } : null;
  const back = [...panel.querySelectorAll('button, a')].find(b => /back/i.test(b.textContent||''));
  const bk = back ? { text: back.textContent.trim().slice(0, 22), fs: getComputedStyle(back).fontSize, color: getComputedStyle(back).color } : null;
  return JSON.stringify({
    wrapper: { children: wrapper.children.length, h: Math.round(wrapper.getBoundingClientRect().height) },
    panel: { w: Math.round(rP.width), h: Math.round(rP.height), y: Math.round(rP.y), radius: csP.borderRadius, bg: csP.backgroundColor },
    spacer: spacer ? { h: Math.round(spacer.getBoundingClientRect().height), display: getComputedStyle(spacer).display, cls: spacer.className.toString().slice(0, 70) } : null,
    heading: h1 ? { text: h1.textContent.slice(0, 26), fs: getComputedStyle(h1).fontSize, fw: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color } : null,
    inputs, submit: sub, back: bk
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE surface 1c: the FORGOT state at 390 (client state swap) ==="
agent-browser eval "(async () => {
  const back = [...document.querySelectorAll('button, a')].find(b => /back/i.test(b.textContent||''));
  if (back) { back.click(); return 'back clicked'; }
  return 'no back';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const link = [...document.querySelectorAll('button, a')].find(x => (x.textContent||'').includes('Forgot'));
  if (link) { link.click(); return 'forgot link clicked'; }
  return 'no forgot link';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const wrapper = [...document.querySelectorAll('div')].find(d => d.className.toString().includes('max-w-md')) || document.querySelector('main > div');
  if (!wrapper) return 'no wrapper';
  const panel = wrapper.firstElementChild;
  const spacer = wrapper.children.length > 1 ? wrapper.children[1] : null;
  const csP = getComputedStyle(panel);
  const rP = panel.getBoundingClientRect();
  const h1 = panel.querySelector('h1, h2');
  const inputs = [...panel.querySelectorAll('input:not([type=hidden])')].map(i => {
    const cs = getComputedStyle(i);
    const r = i.getBoundingClientRect();
    return { type: i.type, h: Math.round(r.height), w: Math.round(r.width), fs: cs.fontSize };
  });
  const submit = [...panel.querySelectorAll('button')].find(b => /reset|send/i.test(b.textContent||''));
  const sub = submit ? { text: submit.textContent.trim().slice(0, 22), h: Math.round(submit.getBoundingClientRect().height), bg: getComputedStyle(submit).backgroundColor, color: getComputedStyle(submit).color } : null;
  const back = [...panel.querySelectorAll('button, a')].find(b => /back/i.test(b.textContent||''));
  const bk = back ? { text: back.textContent.trim().slice(0, 22), fs: getComputedStyle(back).fontSize, color: getComputedStyle(back).color } : null;
  return JSON.stringify({
    wrapper: { children: wrapper.children.length, h: Math.round(wrapper.getBoundingClientRect().height) },
    panel: { w: Math.round(rP.width), h: Math.round(rP.height), y: Math.round(rP.y), radius: csP.borderRadius, bg: csP.backgroundColor },
    spacer: spacer ? { h: Math.round(spacer.getBoundingClientRect().height), display: getComputedStyle(spacer).display } : null,
    heading: h1 ? { text: h1.textContent.slice(0, 30), fs: getComputedStyle(h1).fontSize, fw: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color } : null,
    inputs, submit: sub, back: bk
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== login the clone (for surfaces 2+3) ==="
agent-browser eval "(async () => {
  const back = [...document.querySelectorAll('button, a')].find(b => /back/i.test(b.textContent||''));
  if (back) { back.click(); return 'back to signin'; }
  return 'no back';
})()" 2>/dev/null | tail -1
sleep 2
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
echo "=== CLONE surface 2: the NETWORTH TABLIST chrome at 640 ==="
agent-browser set viewport 640 960 >/dev/null 2>&1
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const triggers = [...document.querySelectorAll('[role=tab], button')].filter(b => /^(Assets|Liabilities)$/.test((b.textContent||'').trim()));
  if (!triggers.length) return 'no tab triggers found';
  const list = triggers[0].closest('[role=tablist]') || triggers[0].parentElement;
  const csL = getComputedStyle(list);
  const rL = list.getBoundingClientRect();
  const census = triggers.map(t => {
    const cs = getComputedStyle(t);
    const r = t.getBoundingClientRect();
    const icon = t.querySelector('svg');
    const ics = icon ? getComputedStyle(icon) : null;
    const ir = icon ? icon.getBoundingClientRect() : null;
    return {
      text: t.textContent.trim().slice(0, 12),
      state: t.getAttribute('data-state') || t.getAttribute('aria-selected'),
      w: Math.round(r.width), h: Math.round(r.height),
      radius: cs.borderRadius, fs: cs.fontSize, fw: cs.fontWeight,
      color: cs.color, bg: cs.backgroundColor, shadow: cs.boxShadow === 'none' ? 'none' : cs.boxShadow.slice(0, 50),
      icon: ics && ir ? { w: Math.round(ir.width), h: Math.round(ir.height), color: ics.color } : null
    };
  });
  return JSON.stringify({
    list: { w: Math.round(rL.width), h: Math.round(rL.height), display: csL.display, gridCols: csL.gridTemplateColumns, gap: csL.gap, bg: csL.backgroundColor, radius: csL.borderRadius, pad: csL.padding, x: Math.round(rL.x), y: Math.round(rL.y) },
    triggers: census
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE surface 3: the DASHBOARD HERO mobile reflow at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const h3 = [...document.querySelectorAll('h3')].find(h => (h.textContent||'').trim() === 'NET ZERO GOAL');
  if (!h3) return 'no goal h3';
  let card = h3.parentElement; let hops = 0;
  while (card && card !== document.body && hops < 12) {
    const cs = getComputedStyle(card); const r = card.getBoundingClientRect();
    if (r.width > 300 && r.width < 400 && r.height > 250 && cs.borderRadius !== '0px' && (cs.boxShadow||'none') !== 'none') break;
    card = card.parentElement; hops++;
  }
  const csCard = getComputedStyle(card);
  const wrapper = card.parentElement;
  const grid = wrapper.parentElement;
  const csG = getComputedStyle(grid);
  const siblings = [...grid.children].map(c => { const r = c.getBoundingClientRect(); return { w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y) }; });
  return JSON.stringify({
    card: { w: Math.round(card.getBoundingClientRect().width), h: Math.round(card.getBoundingClientRect().height), pad: csCard.padding, radius: csCard.borderRadius, bg: csCard.background.slice(0, 90), shadow: csCard.boxShadow.slice(0, 56) },
    grid: { display: csG.display, cols: csG.gridTemplateColumns, gap: csG.gap, w: Math.round(grid.getBoundingClientRect().width), children: grid.children.length },
    cards: siblings,
    docSW: document.documentElement.scrollWidth,
    vw: window.innerWidth
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE hero internals (goal card) ==="
agent-browser eval "(async () => {
  const h3 = [...document.querySelectorAll('h3')].find(h => (h.textContent||'').trim() === 'NET ZERO GOAL');
  let card = h3.parentElement; let hops = 0;
  while (card && hops < 12) { const cs = getComputedStyle(card); const r = card.getBoundingClientRect(); if (r.width > 300 && r.width < 400 && r.height > 250 && cs.borderRadius !== '0px' && (cs.boxShadow||'none') !== 'none') break; card = card.parentElement; hops++; }
  const ic = [...card.querySelectorAll('div')].find(d => { const cs = getComputedStyle(d); return cs.borderRadius === '9999px' && d.getBoundingClientRect().width > 40 && d.getBoundingClientRect().width < 60 && !d.querySelector('div[class*=rounded-full]'); });
  const svg = ic ? ic.querySelector('svg') : null;
  const sub = [...card.querySelectorAll('p')].find(p => /Income\s*=\s*Savings/i.test(p.textContent||''));
  const alloc = [...card.querySelectorAll('span, p')].find(s => /allocation/i.test((s.textContent||'').trim()) && s.getBoundingClientRect().width < 160);
  const pct = [...card.querySelectorAll('span, p')].find(s => /^[0-9.]+%$/.test((s.textContent||'').trim()));
  const h3cs = getComputedStyle(h3);
  const bar = [...card.querySelectorAll('div')].filter(d => { const r = d.getBoundingClientRect(); const cs = getComputedStyle(d); return r.height >= 10 && r.height <= 16 && cs.borderRadius === '9999px' && r.width > 200; });
  const track = bar[0]; const fillEl = track && track.firstElementChild;
  const balBox = [...card.querySelectorAll('div')].find(d => { const cs = getComputedStyle(d); const r = d.getBoundingClientRect(); return cs.borderRadius === '12px' && r.width > 200; });
  const balLabel = balBox ? [...balBox.querySelectorAll('p')].find(p => /balance/i.test(p.textContent||'')) : null;
  const fig = balBox ? [...balBox.querySelectorAll('p, div, span')].filter(x => /^[-+]?\\\$[0-9]/.test((x.textContent||'').trim())).pop() : null;
  return JSON.stringify({
    iconCircle: ic ? { w: Math.round(ic.getBoundingClientRect().width), h: Math.round(ic.getBoundingClientRect().height), bg: getComputedStyle(ic).backgroundColor, svg: svg ? { w: Math.round(svg.getBoundingClientRect().width), color: getComputedStyle(svg).color } : null } : null,
    h3: { fs: h3cs.fontSize, fw: h3cs.fontWeight, color: h3cs.color, lh: h3cs.lineHeight },
    sublabel: sub ? { fs: getComputedStyle(sub).fontSize, color: getComputedStyle(sub).color } : null,
    allocLabel: alloc ? { fs: getComputedStyle(alloc).fontSize, color: getComputedStyle(alloc).color } : null,
    pct: pct ? { fs: getComputedStyle(pct).fontSize, fw: getComputedStyle(pct).fontWeight, color: getComputedStyle(pct).color } : null,
    track: track ? { w: Math.round(track.getBoundingClientRect().width), h: Math.round(track.getBoundingClientRect().height), bg: getComputedStyle(track).backgroundColor, radius: getComputedStyle(track).borderRadius } : null,
    fill: fillEl ? { w: Math.round(fillEl.getBoundingClientRect().width), bg: getComputedStyle(fillEl).background.slice(0, 90), radius: getComputedStyle(fillEl).borderRadius } : null,
    balBox: balBox ? { w: Math.round(balBox.getBoundingClientRect().width), h: Math.round(balBox.getBoundingClientRect().height), radius: getComputedStyle(balBox).borderRadius, pad: getComputedStyle(balBox).padding, bg: getComputedStyle(balBox).backgroundColor, blur: getComputedStyle(balBox).backdropFilter } : null,
    balLabel: balLabel ? { fs: getComputedStyle(balLabel).fontSize, color: getComputedStyle(balLabel).color } : null,
    figure: fig ? { text: (fig.textContent||'').trim().slice(0, 14), fs: getComputedStyle(fig).fontSize, fw: getComputedStyle(fig).fontWeight, color: getComputedStyle(fig).color } : null
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE hero chip census ==="
agent-browser eval "(async () => {
  const h3 = [...document.querySelectorAll('h3')].find(h => (h.textContent||'').trim() === 'NET ZERO GOAL');
  let card = h3.parentElement; let hops = 0;
  while (card && hops < 12) { const cs = getComputedStyle(card); const r = card.getBoundingClientRect(); if (r.width > 300 && r.width < 400 && r.height > 250 && cs.borderRadius !== '0px' && (cs.boxShadow||'none') !== 'none') break; card = card.parentElement; hops++; }
  const balBox = [...card.querySelectorAll('div')].find(d => { const cs = getComputedStyle(d); const r = d.getBoundingClientRect(); return cs.borderRadius === '12px' && r.width > 200; });
  const kids = [...balBox.children].map(c => { const r = c.getBoundingClientRect(); const cs = getComputedStyle(c); return { tag: c.tagName, text: (c.textContent||'').trim().slice(0, 30), w: Math.round(r.width), h: Math.round(r.height), display: cs.display }; });
  const chipBox = [...balBox.children].find(c => /Under Budget|Over Budget|Net Zero/i.test(c.textContent||''));
  let chip = null;
  if (chipBox) {
    const svg = chipBox.querySelector('svg');
    const span = [...chipBox.children].find(c => c.tagName === 'SPAN');
    chip = {
      box: { display: getComputedStyle(chipBox).display, gap: getComputedStyle(chipBox).gap, items: getComputedStyle(chipBox).alignItems, w: Math.round(chipBox.getBoundingClientRect().width) },
      svg: svg ? { w: Math.round(svg.getBoundingClientRect().width), h: Math.round(svg.getBoundingClientRect().height), color: getComputedStyle(svg).color, cls: (svg.getAttribute('class')||'').slice(0, 40) } : null,
      span: span ? { text: (span.textContent||'').slice(0, 20), fs: getComputedStyle(span).fontSize, fw: getComputedStyle(span).fontWeight, color: getComputedStyle(span).color } : null
    };
  }
  return JSON.stringify({ balBoxChildren: kids, chip });
})()" 2>/dev/null | tail -1

echo ""
echo "=== clone-v50 done ==="
EOF
