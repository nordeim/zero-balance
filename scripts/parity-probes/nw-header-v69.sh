#!/usr/bin/env bash
# nw-header-v69.sh — the v69 pin's measurement probe: the /networth view's
# PAGE-HEADER ROW computed census at 390x844 on the CLONE (the never-
# census'd family — the v14 chip test pins x-positions only; the v65
# savings-header-row pin's sibling for the networth surface). Read-only.
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonenw69"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const h1 = [...document.querySelectorAll('main h1')].find(h => (h.textContent || '').trim() === 'Net Worth');
  if (!h1) return 'no h1';
  const block = h1.parentElement;
  const row = block.parentElement;
  const rs = getComputedStyle(row);
  const rr = row.getBoundingClientRect();
  const chip = [...row.children].find(c => c !== block);
  const cs = chip ? getComputedStyle(chip) : null;
  const cr = chip ? chip.getBoundingClientRect() : null;
  const icon = chip ? chip.querySelector('svg') : null;
  const ir = icon ? icon.getBoundingClientRect() : null;
  const hs = getComputedStyle(h1);
  const hr = h1.getBoundingClientRect();
  const p = [...block.children].find(c => c.tagName === 'P');
  const ps = p ? getComputedStyle(p) : null;
  const pr = p ? p.getBoundingClientRect() : null;
  const next = row.nextElementSibling;
  const nr = next ? next.getBoundingClientRect() : null;
  return JSON.stringify({
    docSW: document.documentElement.scrollWidth,
    row: { display: rs.display, alignItems: rs.alignItems, gap: rs.gap, mb: rs.marginBottom, w: Math.round(rr.width), h: Math.round(rr.height), top: Math.round(rr.top), bottom: Math.round(rr.bottom) },
    chip: chip ? { w: Math.round(cr.width), h: Math.round(cr.height), x: Math.round(cr.x), radius: cs.borderRadius, bg: cs.backgroundImage.slice(0, 90), display: cs.display, justify: cs.justifyContent } : null,
    chipIcon: icon ? { w: Math.round(ir.width), h: Math.round(ir.height), color: getComputedStyle(icon).color } : null,
    h1: { fs: hs.fontSize, fw: hs.fontWeight, lh: hs.lineHeight, color: hs.color, w: Math.round(hr.width), h: Math.round(hr.height), x: Math.round(hr.x) },
    block: { w: Math.round(block.getBoundingClientRect().width), h: Math.round(block.getBoundingClientRect().height) },
    subtitle: p ? { text: (p.textContent || '').slice(0, 45), fs: ps.fontSize, fw: ps.fontWeight, color: ps.color, lh: ps.lineHeight, w: Math.round(pr.width), h: Math.round(pr.height) } : null,
    rowToCardGap: nr ? Math.round(nr.top - rr.bottom) : null
  });
})()" 2>/dev/null | tail -1
EOF
echo "=== nw-header v69 done ==="
