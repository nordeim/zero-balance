#!/usr/bin/env bash
# clone-v48.sh — the clone side of the three v48 surfaces, via with-server
# on :3200 (read-only: card-click + census + cancel; filter-to-zero; input focus).
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clone48b"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already?';
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

echo "=== CLONE surface 1: item-details sheet at 1280 ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('main div')].find(d => d.className && d.className.toString().includes('rounded-xl') && d.querySelector('h3'));
  if (card) { card.click(); return 'card clicked'; }
  return 'no card';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const dlg = document.querySelector('[role=dialog]');
  if (!dlg) return 'no dialog';
  const content = dlg.querySelector('[data-radix-dialog-content], div');
  // the panel: the shadow-2xl child
  const panel = [...dlg.querySelectorAll('div')].find(d => {
    const s = getComputedStyle(d);
    return s.boxShadow !== 'none' && d.getBoundingClientRect().width > 200 && s.backgroundColor === 'rgb(255, 255, 255)';
  });
  const overlay = [...document.querySelectorAll('div')].find(d => {
    const cs = getComputedStyle(d);
    return cs.position === 'fixed' && cs.backgroundColor === 'rgba(26, 58, 46, 0.5)';
  });
  const closeBtn = [...dlg.querySelectorAll('button')].find(b => b.getBoundingClientRect().width === 36);
  const ps = panel ? getComputedStyle(panel) : null;
  const pr = panel ? panel.getBoundingClientRect() : null;
  const cs2 = closeBtn ? getComputedStyle(closeBtn) : null;
  return JSON.stringify({
    panel: ps ? { w: Math.round(pr.width), h: Math.round(pr.height), radius: ps.borderRadius, maxW: ps.maxWidth, shadow: ps.boxShadow, cls: panel.className.toString().slice(0, 100) } : null,
    overlay: overlay ? { bg: getComputedStyle(overlay).backgroundColor, z: getComputedStyle(overlay).zIndex, blur: getComputedStyle(overlay).backdropFilter } : null,
    closeBtn: cs2 ? { w: Math.round(closeBtn.getBoundingClientRect().width), h: Math.round(closeBtn.getBoundingClientRect().height), radius: cs2.borderRadius, bg: cs2.backgroundColor, shadow: cs2.boxShadow, border: cs2.borderColor + ' ' + cs2.borderWidth } : null
  });
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => { const x = document.querySelector('[role=dialog] [data-radix-dialog-close], [role=dialog] button[aria-label*=lose i], [role=dialog] button'); if (x) { x.click(); return 'closed'; } return 'no close'; })()" 2>/dev/null | tail -1
sleep 1

echo "=== CLONE surface 2: dialog-input focus composite at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').trim() === 'Add Income'); if (b) { b.click(); return 'add opened'; } return 'not found'; })()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const input = document.querySelector('[role=dialog] input');
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

echo "=== CLONE surface 3: empty state via filter-to-zero at 390 ==="
agent-browser eval "(async () => {
  const sel = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('All Frequencies') || (x.textContent||'').includes('All frequencies'));
  if (!sel) return 'no freq filter';
  sel.click();
  await new Promise(r => setTimeout(r, 500));
  const box = [...document.querySelectorAll('[role=listbox]')].find(b => b.getBoundingClientRect().height > 0);
  const opt = box ? [...box.querySelectorAll('[role=option]')].find(o => /one.?time/i.test((o.textContent||''))) : null;
  if (opt) { opt.click(); return 'One-time selected'; }
  return 'no one-time option';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const main = document.querySelector('main');
  const titleEl = [...main.querySelectorAll('h3')].find(el => (el.textContent||'').trim().includes('No income items yet'));
  if (!titleEl) return 'no empty state: ' + (main.innerText.match(/[\d]+ items/) || ['?'])[0];
  const cont = titleEl.parentElement;
  const cs = getComputedStyle(cont);
  const icon = cont.querySelector('svg');
  const titleS = getComputedStyle(titleEl);
  const p = titleEl.nextElementSibling;
  const btn = [...cont.querySelectorAll('button')].find(b => (b.textContent||'').includes('Add'));
  const btnS = btn ? getComputedStyle(btn) : null;
  return JSON.stringify({
    container: { cls: cont.className.toString(), pad: cs.padding, align: cs.textAlign, w: Math.round(cont.getBoundingClientRect().width), h: Math.round(cont.getBoundingClientRect().height) },
    icon: icon ? { w: icon.getBoundingClientRect().width, opacity: getComputedStyle(icon).opacity, color: getComputedStyle(icon).color, mb: getComputedStyle(icon).marginBottom } : null,
    title: { fs: titleS.fontSize, fw: titleS.fontWeight, color: titleS.color, mb: titleS.marginBottom },
    p: p ? { cls: p.className.toString().slice(0,30), mb: getComputedStyle(p).marginBottom, color: getComputedStyle(p).color, fs: getComputedStyle(p).fontSize } : null,
    btn: btnS ? { h: Math.round(btn.getBoundingClientRect().height), w: Math.round(btn.getBoundingClientRect().width), bg: btnS.backgroundImage.slice(0, 90), shadow: btnS.boxShadow, pad: btnS.padding, radius: btnS.borderRadius, fw: btnS.fontWeight } : null
  });
})()" 2>/dev/null | tail -1
echo "=== restore: reset filter to All ==="
agent-browser eval "(async () => {
  const sel = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('One-time'));
  if (!sel) return 'no filter btn';
  sel.click();
  await new Promise(r => setTimeout(r, 400));
  const box = [...document.querySelectorAll('[role=listbox]')].find(b => b.getBoundingClientRect().height > 0);
  const opt = box ? [...box.querySelectorAll('[role=option]')].find(o => /all/i.test((o.textContent||''))) : null;
  if (opt) { opt.click(); return 'reset'; }
  return 'no all option';
})()" 2>/dev/null | tail -1
EOF
