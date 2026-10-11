#!/usr/bin/env bash
# v48: reference-side driver — the three v48 surfaces, measured live on
# the reference (READ-ONLY: the card-click + census + close; the
# dialog-open + input-focus + cancel; the filter-to-zero + restore —
# no Delete clicks anywhere, the v46 incident rule).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="ref48"
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

echo "=== REF surface 1: item-details sheet at 1280 (card-body click) ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('main div')].find(d => d.className && d.className.toString().includes('rounded-xl') && d.textContent && d.textContent.includes('\$'));
  if (card) { card.click(); return 'card clicked'; }
  return 'no card';
})()" 2>/dev/null | tail -1
sleep 2
# The reference's details layer: fixed inset-0 z-50 (no [role=dialog]) —
# the census keys on the layer's text ('Budget Item Details').
agent-browser eval "(async () => {
  const layer = [...document.querySelectorAll('div')].find(d => d.className && d.className.toString().includes('fixed inset-0 z-50') && (d.textContent||'').includes('Budget Item Details'));
  if (!layer) return 'no dialog layer';
  const panel = layer.children[0];
  const ps = getComputedStyle(panel);
  const pr = panel.getBoundingClientRect();
  const ls = getComputedStyle(layer);
  const closeBtn = [...panel.querySelectorAll('button')].filter(b => !b.textContent.trim())[0] || [...panel.querySelectorAll('button')][0];
  const cb = closeBtn ? getComputedStyle(closeBtn) : null;
  return JSON.stringify({
    layer: { bg: ls.backgroundColor, z: ls.zIndex },
    panel: { w: Math.round(pr.width), h: Math.round(pr.height), radius: ps.borderRadius, maxW: ps.maxWidth, shadow: ps.boxShadow, cls: panel.className.toString().slice(0, 100) },
    closeBtn: cb ? { w: Math.round(closeBtn.getBoundingClientRect().width), h: Math.round(closeBtn.getBoundingClientRect().height), radius: cb.borderRadius, bg: cb.backgroundColor, borderW: cb.borderWidth } : null
  });
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => { const b = [...document.querySelectorAll('button')].filter(x => !x.textContent.trim()); if (b.length) { b[b.length-1].click(); return 'closed'; } return 'no close'; })()" 2>/dev/null | tail -1
sleep 1

echo ""
echo "=== REF surface 2: dialog-input focus composite at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').trim() === 'Add Income'); if (b) { b.click(); return 'add opened'; } return 'not found'; })()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const overlay = [...document.querySelectorAll('div')].filter(d => getComputedStyle(d).position === 'fixed' && d.innerHTML.includes('Save') && d.innerHTML.includes('input'));
  const layer = overlay.pop();
  const input = layer ? layer.querySelector('input') : null;
  if (!input) return 'no input';
  const cs = getComputedStyle(input);
  const layerCount = (s) => (s.match(/px, /g) || []).length + 1;
  const rest = { shadow: cs.boxShadow, layers: layerCount(cs.boxShadow), h: cs.height, radius: cs.borderRadius, pad: cs.padding, border: cs.borderColor + ' ' + cs.borderWidth, bg: cs.backgroundColor, w: Math.round(input.getBoundingClientRect().width) };
  input.focus({ focusVisible: true });
  await new Promise((r) => setTimeout(r, 100));
  const fcs = getComputedStyle(input);
  const focus = { fv: input.matches(':focus-visible'), shadow: fcs.boxShadow, layers: layerCount(fcs.boxShadow), borderColor: fcs.borderColor, outlineStyle: fcs.outlineStyle };
  return JSON.stringify({ rest, focus });
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').trim() === 'Cancel'); if (b) { b.click(); return 'closed'; } return 'no cancel'; })()" 2>/dev/null | tail -1
sleep 1

echo ""
echo "=== REF surface 3: empty state via frequency filter-to-zero at 390 ==="
agent-browser eval "(async () => {
  const sel = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('All Frequencies'));
  if (!sel) return 'no freq filter';
  sel.click();
  await new Promise(r => setTimeout(r, 500));
  const boxes = [...document.querySelectorAll('[role=listbox]')].filter(b => b.getBoundingClientRect().height > 0);
  const freqBox = boxes.find(b => (b.textContent||'').includes('One-time'));
  const opt = freqBox ? [...freqBox.querySelectorAll('[role=option]')].find(o => (o.textContent||'').trim() === 'One-time') : null;
  if (opt) { opt.click(); return 'One-time selected'; }
  return 'no one-time option';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const main = document.querySelector('main');
  const titleEl = [...main.querySelectorAll('h3')].find(el => (el.textContent||'').trim() === 'No income items yet');
  if (!titleEl) return 'no empty state';
  const cont = titleEl.parentElement;
  const cs = getComputedStyle(cont);
  const icon = cont.querySelector('svg');
  const titleS = getComputedStyle(titleEl);
  const p = titleEl.nextElementSibling;
  const btn = [...cont.querySelectorAll('button')].find(b => (b.textContent||'').includes('Add Income'));
  const btnS = btn ? getComputedStyle(btn) : null;
  return JSON.stringify({
    container: { cls: cont.className.toString(), pad: cs.padding, align: cs.textAlign, w: Math.round(cont.getBoundingClientRect().width), h: Math.round(cont.getBoundingClientRect().height), borderW: cs.borderTopWidth, bg: cs.backgroundColor },
    icon: icon ? { w: icon.getBoundingClientRect().width, opacity: getComputedStyle(icon).opacity, color: getComputedStyle(icon).color, mb: getComputedStyle(icon).marginBottom } : null,
    title: { fs: titleS.fontSize, fw: titleS.fontWeight, color: titleS.color, mb: titleS.marginBottom },
    p: p ? { mb: getComputedStyle(p).marginBottom, color: getComputedStyle(p).color, fs: getComputedStyle(p).fontSize } : null,
    btn: btnS ? { h: Math.round(btn.getBoundingClientRect().height), w: Math.round(btn.getBoundingClientRect().width), bg: btnS.backgroundImage.slice(0, 90), shadow: btnS.boxShadow, pad: btnS.padding, radius: btnS.borderRadius, fw: btnS.fontWeight } : null
  });
})()" 2>/dev/null | tail -1
echo "=== restore: reset the frequency filter to All (read-only) ==="
agent-browser eval "(async () => {
  const sel = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('One-time'));
  if (!sel) return 'no filter btn';
  sel.click();
  await new Promise(r => setTimeout(r, 400));
  const boxes = [...document.querySelectorAll('[role=listbox]')].filter(b => b.getBoundingClientRect().height > 0);
  const box = boxes.find(b => (b.textContent||'').includes('One-time')) || boxes[0];
  const opt = box ? [...box.querySelectorAll('[role=option]')].find(o => /all/i.test((o.textContent||''))) : null;
  if (opt) { opt.click(); return 'reset'; }
  return 'no all option';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const main = document.querySelector('main');
  return JSON.stringify({ census: (main.innerText.match(/[\d]+ items · [\$\d,\.]+/) || ['NOT RESET'])[0] });
})()" 2>/dev/null | tail -1
