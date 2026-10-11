#!/usr/bin/env bash
# clone-v49.sh — the clone-side driver for the three v49 surfaces, run via
# with-server on :3200 (the standalone build). Mirrors ref-v49.sh exactly:
# (1) the login panel at 390, (2) the donut legend at 390, (3) the
# calculator dialog at 640. READ-ONLY (open + census + close).
set -u
bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clone49"
B="http://localhost:3200"

echo "=== CLONE surface 1: the LOGIN PANEL at 390 (logged out) ==="
agent-browser open "$B/login" >/dev/null 2>&1
sleep 3
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
  const content = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).padding && d.querySelector('h1, h2'));
  const csC = content ? getComputedStyle(content) : null;
  const h1 = panel.querySelector('h1, h2');
  const bar = panel.querySelector('div.h-1') || [...panel.children].find(c => c.getBoundingClientRect().height <= 4 && c.getBoundingClientRect().height > 0);
  return JSON.stringify({
    panel: { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), radius: cs.borderRadius, maxW: cs.maxWidth, shadow: cs.boxShadow, bg: cs.backgroundColor, border: cs.borderWidth + ' ' + cs.borderColor, pad: cs.padding, shadowLayers: cs.boxShadow.split('rgba').length - 1, cls: panel.className.toString().slice(0,110) },
    contentPad: csC ? csC.padding : null,
    heading: h1 ? { fs: getComputedStyle(h1).fontSize, fw: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color } : null,
    bar: bar ? { h: Math.round(bar.getBoundingClientRect().height), bg: getComputedStyle(bar).backgroundImage.slice(0,80) } : null
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== login the clone (demo) for surfaces 2+3 ==="
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

echo "=== CLONE surface 2: the DONUT LEGEND at 390 (dashboard) ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$B/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const rows = [...document.querySelectorAll('div')].filter(d => {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return cs.borderRadius === '8px' && cs.padding === '12px' && r.width > 200 && r.width < 360 && (d.textContent||'').includes('%');
  });
  if (!rows.length) return 'no legend rows';
  const row = rows[0];
  const cs = getComputedStyle(row);
  const r = row.getBoundingClientRect();
  const leaves = [...row.querySelectorAll('p, span, div, h4')].filter(el => el.children.length === 0);
  const census = leaves.map(el => {
    const cs = getComputedStyle(el);
    return { tag: el.tagName, text: el.textContent.trim().slice(0,14), fs: cs.fontSize, fw: cs.fontWeight, color: cs.color, ta: cs.textAlign };
  });
  const cont = rows[0].parentElement;
  const csCont = getComputedStyle(cont);
  const rightBlock = leaves[leaves.length-1].parentElement;
  const dot = leaves[0];
  const svg = row.querySelector('svg');
  return JSON.stringify({
    container: { display: csCont.display, dir: csCont.flexDirection, gap: csCont.gap, mt: csCont.marginTop, w: Math.round(cont.getBoundingClientRect().width) },
    rowCount: rows.length,
    row: { w: Math.round(r.width), h: Math.round(r.height), radius: cs.borderRadius, pad: cs.padding, bg: cs.backgroundColor, cls: row.className.toString().slice(0,90) },
    dot: dot ? { w: Math.round(dot.getBoundingClientRect().width), h: Math.round(dot.getBoundingClientRect().height), radius: getComputedStyle(dot).borderRadius, bg: getComputedStyle(dot).backgroundColor } : null,
    leaves: census,
    rightAlign: rightBlock ? getComputedStyle(rightBlock).textAlign : null,
    svg: svg ? { w: Math.round(svg.getBoundingClientRect().width), color: getComputedStyle(svg).color } : null
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE surface 3: the CALCULATOR DIALOG at 640 (open+census+close) ==="
agent-browser set viewport 640 960 >/dev/null 2>&1
agent-browser open "$B/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const btn = [...document.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Calculate');
  if (!btn) return 'no Calculate button';
  btn.click();
  await new Promise(r => setTimeout(r, 1200));
  return 'calculator clicked';
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => {
  const panel = document.querySelector('[role=dialog]');
  if (!panel) return 'no dialog role';
  const cs = getComputedStyle(panel);
  const r = panel.getBoundingClientRect();
  const closeBtn = [...panel.querySelectorAll('button')].filter(b => (b.getAttribute('aria-label')||'').includes('Close') || !(b.textContent||'').trim())[0];
  const hdr = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).borderBottomWidth !== '0px');
  return JSON.stringify({
    panel: { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), radius: cs.borderRadius, maxW: cs.maxWidth, maxH: cs.maxHeight, shadow: cs.boxShadow, shadowLayers: cs.boxShadow.split('rgba').length - 1, bg: cs.backgroundColor, overflow: cs.overflow, cls: panel.className.toString().slice(0,130) },
    closeBtn: closeBtn ? { w: Math.round(closeBtn.getBoundingClientRect().width), h: Math.round(closeBtn.getBoundingClientRect().height) } : null,
    hdrBorder: hdr ? getComputedStyle(hdr).borderBottom : null,
    sw: document.documentElement.scrollWidth
  });
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => {
  const cancel = [...document.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Cancel');
  if (cancel) { cancel.click(); await new Promise(r=>setTimeout(r,600)); return 'cancelled'; }
  return 'no cancel';
})()" 2>/dev/null | tail -1
echo "=== clone v49 driver done ==="
EOF
