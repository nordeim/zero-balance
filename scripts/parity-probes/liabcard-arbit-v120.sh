#!/usr/bin/env bash
# liabcard-arbit-v120.sh — the ONE-SHOT census of the LIABILITY CARD family
# at mobile 390 on the CLONE (the v120 pin's own axes — the never-pinned
# family on the /networth view, the mobile twin #1's surface).
#
# WHY CLONE-ONLY (the family-consistency form, the v29 G1 precedent): the
# reference's own liability data is EMPTY (its seeded account carries 0
# liabilities — its Total Liabilities reads $0.00 with no cards to
# measure), and the v46 READ-ONLY rule forbids writing liability data on
# the reference. The liability card's chrome family is the AssetCard's
# pinned contract BY CONSTRUCTION (the identical class strings —
# net-worth-view.tsx:169 'group rounded-xl border bg-white p-5
# transition-all duration-200 hover:shadow-lg' vs :65 the asset twin; the
# v46 F1 liability-twin fix comment documents the shared mb-4 P + the
# space-y-2 text-xs facts stack) — the pin locks the family-consistency
# contract + the liability-ONLY interior axes (the 3-row facts stack with
# the interest row).
#
# READ-ONLY on the app (login + the tab switch + passive census only).
# Double-quoted-heredoc-safe: no dollar sequences in the census JS; no
# attribute-value selectors.
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneliab120"
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

# switch to the LIABILITIES tab (the tablist's second trigger) — the FULL
# pointer-event sequence (the Radix tabs activate on pointerdown, not the
# bare el.click(); the v29-era spec's locator click dispatches all events)
agent-browser eval "(async () => {
  const tab = [...document.querySelectorAll('[role=tab]')].find(t => /Liabilities/i.test(t.textContent || ''));
  if (!tab) return 'no tab';
  const r = tab.getBoundingClientRect();
  const x = r.left + r.width / 2, y = r.top + r.height / 2;
  const opts = { bubbles: true, cancelable: true, clientX: x, clientY: y, button: 0 };
  tab.dispatchEvent(new PointerEvent('pointerdown', opts));
  tab.dispatchEvent(new MouseEvent('mousedown', opts));
  tab.dispatchEvent(new PointerEvent('pointerup', opts));
  tab.dispatchEvent(new MouseEvent('mouseup', opts));
  tab.dispatchEvent(new MouseEvent('click', opts));
  await new Promise(rs => setTimeout(rs, 800));
  return 'tab state: ' + tab.getAttribute('data-state');
})()" 2>/dev/null | tail -1
sleep 2

echo "--- LIAB CARD census (390, first card = Home Loan):"
agent-browser eval "(async () => {
  const cards = [...document.querySelectorAll('main div')].filter(d => {
    if (typeof d.className !== 'string') return false;
    return d.className.includes('group rounded-xl border bg-white p-5') && /Home Loan/.test(d.textContent || '');
  });
  const card = cards[0];
  if (!card) return 'no liability card found';
  const cr = card.getBoundingClientRect();
  const cs = getComputedStyle(card);
  const head = card.querySelector('div');
  const hs = head ? getComputedStyle(head) : null;
  const dot = [...card.querySelectorAll('div')].find(d => (d.className || '').toString().includes('h-2 w-2'));
  const dotS = dot ? getComputedStyle(dot) : null;
  const dotR = dot ? dot.getBoundingClientRect() : null;
  const h4 = card.querySelector('h4');
  const h4S = h4 ? getComputedStyle(h4) : null;
  const badge = [...card.querySelectorAll('span')].find(s => /home loan/i.test((s.textContent || '').trim()) && s.className.includes('zb-badge-hover'));
  const bS = badge ? getComputedStyle(badge) : null;
  const bR = badge ? badge.getBoundingClientRect() : null;
  const valP = [...card.querySelectorAll('p')].find(p => /^[-]?[\$]?[0-9]/.test((p.textContent || '').trim()));
  const vS = valP ? getComputedStyle(valP) : null;
  const vR = valP ? valP.getBoundingClientRect() : null;
  const facts = [...card.children].find(c => (c.className || '').toString().includes('space-y-2'));
  const fS = facts ? getComputedStyle(facts) : null;
  const rowRects = facts ? [...facts.children].map(r => r.getBoundingClientRect()) : [];
  const rowGap = rowRects.length >= 2 ? Math.round(rowRects[1].top - rowRects[0].bottom) : null;
  const rows = facts ? [...facts.children].map(r => {
    const s = getComputedStyle(r);
    const rr = r.getBoundingClientRect();
    const icon = r.querySelector('svg');
    const ir = icon ? icon.getBoundingClientRect() : null;
    return { txt: (r.textContent || '').trim().slice(0, 22), display: s.display, align: s.alignItems, gap: s.gap, h: Math.round(rr.height), icon: ir ? { w: Math.round(ir.width), h: Math.round(ir.height) } : null };
  }) : [];
  const headRow = head ? head.getBoundingClientRect() : null;
  return JSON.stringify({
    docSW: document.documentElement.scrollWidth,
    vw: document.documentElement.clientWidth,
    card: { w: Math.round(cr.width), h: Math.round(cr.height), radius: cs.borderRadius, pad: cs.padding, border: cs.border, shadow: cs.boxShadow, bg: cs.backgroundColor, transition: cs.transitionProperty + ' ' + cs.transitionDuration },
    headRow: headRow ? { mb: hs ? hs.marginBottom : null, display: hs ? hs.display : null, align: hs ? hs.alignItems : null, justify: hs ? hs.justifyContent : null, h: Math.round(headRow.height) } : null,
    dot: dotS && dotR ? { w: Math.round(dotR.width), h: Math.round(dotR.height), radius: dotS.borderRadius, bg: dotS.backgroundColor } : null,
    h4: h4S ? { fs: h4S.fontSize, fw: h4S.fontWeight, color: h4S.color } : null,
    badge: bS && bR ? { h: Math.round(bR.height), fs: bS.fontSize, fw: bS.fontWeight, bg: bS.backgroundColor, color: bS.color, pad: bS.padding, radius: bS.borderRadius } : null,
    valueP: vS && vR ? { fs: vS.fontSize, fw: vS.fontWeight, color: vS.color, mb: vS.marginBottom, h: Math.round(vR.height) } : null,
    facts: fS ? { fs: fS.fontSize, color: fS.color, rowGap: rowGap, rowCount: rows.length } : null,
    rows: rows,
    valueToFactsGap: valP && facts ? Math.round(facts.getBoundingClientRect().top - valP.getBoundingClientRect().bottom) : null
  });
})()" 2>/dev/null | tail -1

echo "--- seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== liabcard arbit v120 done ==="
EOF
