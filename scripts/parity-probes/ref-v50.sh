#!/usr/bin/env bash
# ref-v50.sh — the reference-side driver for the three v50 surfaces
# (the session-115 queue): (1) the auth states' FULL 390 census — the
# sign-up state + the forgot state (the v49 F1 verified the spacer on
# sign-up only; this sweep censuses each state's whole panel stack);
# (2) the networth tablist's chrome at 640; (3) the dashboard hero's
# mobile reflow at 390.
# READ-ONLY: the auth state swaps are client state changes (the v49
# precedent); the tablist census is a passive read; the hero census is
# a passive read. No saves, no deletes, no form submits (the v46 rule).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="ref50"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3

echo "=== REF surface 1a: the SIGN-IN state baseline at 390 ==="
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
echo "=== REF surface 1b: the SIGN-UP state at 390 (client state swap) ==="
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
echo "=== REF surface 1c: the FORGOT state at 390 (client state swap) ==="
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
echo "=== login the reference (for surfaces 2+3) ==="
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
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4

echo ""
echo "=== REF surface 2: the NETWORTH TABLIST chrome at 640 ==="
agent-browser set viewport 640 960 >/dev/null 2>&1
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  // the tablist: the container carrying the two tab triggers (Assets / Liabilities)
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
    list: { w: Math.round(rL.w || rL.width), h: Math.round(rL.height), display: csL.display, gridCols: csL.gridTemplateColumns, gap: csL.gap, bg: csL.backgroundColor, radius: csL.borderRadius, pad: csL.padding, x: Math.round(rL.x), y: Math.round(rL.y) },
    triggers: census
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== REF surface 3: the DASHBOARD HERO mobile reflow at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  // the hero: the first grid section — the Net Zero Goal card + the
  // breakdown card. At 390 they stack 1-col. Census the cards + the
  // hero chip + the figure.
  const heroSection = document.querySelector('main') ? [...document.querySelector('main').children].find(c => c.querySelector('h1, h2, h3')) : null;
  // more robust: find the NET ZERO GOAL heading, walk up to its top-level card, then its parent grid
  const goalHeading = [...document.querySelectorAll('h1, h2, h3, div')].find(x => (x.textContent||'').trim().startsWith('NET ZERO GOAL'));
  if (!goalHeading) return 'no goal heading';
  let card = goalHeading;
  while (card && card.parentElement && !/grid|flex/.test(getComputedStyle(card.parentElement).display)) card = card.parentElement;
  const goalCard = card;
  const grid = goalCard.parentElement;
  const csG = getComputedStyle(grid);
  const rGoal = goalCard.getBoundingClientRect();
  // the hero status chip + the figure inside the goal card
  const chip = [...goalCard.querySelectorAll('span, div')].find(s => /balance|surplus|deficit|goal/i.test((s.textContent||'').trim()) && s.getBoundingClientRect().width < 200 && s.getBoundingClientRect().height < 40);
  const fig = [...goalCard.querySelectorAll('h1, h2, div, span, p')].find(x => /^[-+]?\\\$?[0-9][0-9,.]*\$?/.test((x.textContent||'').trim().replace('-', '')) && x.getBoundingClientRect().height > 30 && x.getBoundingClientRect().height < 80);
  const cards = [...grid.children].map(c => { const r = c.getBoundingClientRect(); return { w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y) }; });
  return JSON.stringify({
    grid: { display: csG.display, cols: csG.gridTemplateColumns, gap: csG.gap, w: Math.round(grid.getBoundingClientRect().width), children: grid.children.length },
    goalCard: { w: Math.round(rGoal.width), h: Math.round(rGoal.height), radius: getComputedStyle(goalCard).borderRadius, bg: getComputedStyle(goalCard).backgroundColor, shadow: (getComputedStyle(goalCard).boxShadow||'none').slice(0, 50) },
    cards,
    chip: chip ? { text: chip.textContent.trim().slice(0, 24), h: Math.round(chip.getBoundingClientRect().height), fs: getComputedStyle(chip).fontSize, color: getComputedStyle(chip).color, bg: chip.className.toString().includes('chip') || getComputedStyle(chip).backgroundColor } : null,
    figure: fig ? { text: fig.textContent.trim().slice(0, 16), fs: getComputedStyle(fig).fontSize, fw: getComputedStyle(fig).fontWeight, color: getComputedStyle(fig).color } : null,
    docSW: document.documentElement.scrollWidth
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== ref-v50 done ==="
