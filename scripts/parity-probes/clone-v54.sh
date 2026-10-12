#!/usr/bin/env bash
# clone-v54.sh — the clone-side driver for the v54 surface (the
# session-125 v54 queue's first member): the SAVINGS VIEW's GOAL-CARD
# INTERNALS at 390 — the badge chip row + the date/payment footer —
# the internals BEYOND the v51 F3 chrome pin. Census mirrors ref-v54.sh
# exactly. Read-only on our own db (writes allowed but not needed).
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clone54"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
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
echo "=== CLONE surface: the SAVINGS GOAL-CARD INTERNALS at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const h4 = [...document.querySelectorAll('h4')].find((x) =>
    (x.textContent || '').trim().length > 3);
  if (!h4) return 'no h4';
  let card = h4.closest('div.rounded-xl') || h4.parentElement;
  for (let i = 0; card && i < 5; i++) {
    const pcs = getComputedStyle(card.parentElement);
    if (pcs.display === 'grid') break;
    card = card.parentElement;
  }
  if (!card) return 'no card';
  const rows = [...card.querySelectorAll('div')].filter((d) => {
    const cs = getComputedStyle(d);
    return cs.display === 'flex' && cs.flexWrap === 'wrap' &&
      [...d.children].every(c => getComputedStyle(c).display.includes('inline-flex') || getComputedStyle(c).display === 'flex') &&
      d.children.length >= 2;
  });
  const badgeRow = rows[0];
  if (!badgeRow) return 'no badge row';
  const brcs = getComputedStyle(badgeRow);
  const chipGrab = (el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const icon = el.querySelector('svg');
    return {
      text: (el.textContent || '').trim().slice(0, 14),
      w: Math.round(r.width), h: Math.round(r.height),
      radius: cs.borderRadius, pad: cs.padding,
      fs: cs.fontSize, fw: cs.fontWeight,
      color: cs.color, bg: cs.backgroundColor,
      border: cs.borderTopWidth + ' ' + cs.borderTopColor,
      gap: cs.gap,
      icon: icon ? {
        w: Math.round(icon.getBoundingClientRect().width),
        h: Math.round(icon.getBoundingClientRect().height),
        color: getComputedStyle(icon).color,
        mr: getComputedStyle(icon).marginRight
      } : null
    };
  };
  // The footer row: the LAST justify-between direct child WITHOUT an h4
  // (the header row also carries justify-between + an svg — the v54
  // probe-debug lesson: the generic filter matched the header first).
  const footer = [...card.children].filter((d) => {
    const cs = getComputedStyle(d);
    return cs.display === 'flex' && cs.justifyContent === 'space-between' &&
      !d.querySelector('h4');
  }).pop();
  const fcs = footer ? getComputedStyle(footer) : null;
  const dateSpan = footer ? footer.children[0] : null;
  const paySpan = footer ? footer.children[footer.children.length - 1] : null;
  const dateIcon = dateSpan ? dateSpan.querySelector('svg') : null;
  const payIcon = paySpan && paySpan !== dateSpan ? paySpan.querySelector('svg') : null;
  const amount = [...card.querySelectorAll('p')].find((p) =>
    /^[\\\$]?[\\d,]/.test((p.textContent || '').trim()) &&
    parseFloat(getComputedStyle(p).fontSize) >= 20);
  const acs = amount ? getComputedStyle(amount) : null;
  const hdrRow = h4.parentElement;
  const hcs = hdrRow ? getComputedStyle(hdrRow) : null;
  const dot = hdrRow ? hdrRow.querySelector('div[class*=rounded-full], div[style*=border-radius]') ||
    [...hdrRow.querySelectorAll('div')].find(d => d.getBoundingClientRect().width < 12) : null;
  const dcs = dot ? getComputedStyle(dot) : null;
  const dr = dot ? dot.getBoundingClientRect() : null;
  return JSON.stringify({
    card: { h: Math.round(card.getBoundingClientRect().height) },
    hdrRow: hcs ? { display: hcs.display, gap: hcs.gap, mb: hcs.marginBottom, alignItems: hcs.alignItems } : null,
    dot: dcs ? { w: Math.round(dr.width), h: Math.round(dr.height), radius: dcs.borderRadius, bg: dcs.backgroundColor } : null,
    h4: { fs: getComputedStyle(h4).fontSize, fw: getComputedStyle(h4).fontWeight, color: getComputedStyle(h4).color },
    sub: { mb: amount ? '' : '' },
    amount: acs ? { fs: acs.fontSize, fw: acs.fontWeight, mb: acs.marginBottom } : null,
    badgeRow: { display: brcs.display, gap: brcs.gap, wrap: brcs.flexWrap, mb: brcs.marginBottom,
      h: Math.round(badgeRow.getBoundingClientRect().height), n: badgeRow.children.length },
    chips: [...badgeRow.children].map(chipGrab),
    footer: fcs ? { display: fcs.display, justify: fcs.justifyContent, fs: fcs.fontSize, color: fcs.color,
      mt: fcs.marginTop, h: Math.round(footer.getBoundingClientRect().height) } : null,
    dateSpan: dateSpan ? { fs: getComputedStyle(dateSpan).fontSize, color: getComputedStyle(dateSpan).color,
      display: getComputedStyle(dateSpan).display, gap: getComputedStyle(dateSpan).gap,
      icon: dateIcon ? { w: Math.round(dateIcon.getBoundingClientRect().width), h: Math.round(dateIcon.getBoundingClientRect().height),
        color: getComputedStyle(dateIcon).color } : null } : null,
    paySpan: (paySpan && paySpan !== dateSpan) ? { text: (paySpan.textContent || '').trim().slice(0, 16),
      fs: getComputedStyle(paySpan).fontSize, color: getComputedStyle(paySpan).color,
      display: getComputedStyle(paySpan).display, gap: getComputedStyle(paySpan).gap,
      icon: payIcon ? { w: Math.round(payIcon.getBoundingClientRect().width), h: Math.round(payIcon.getBoundingClientRect().height),
        color: getComputedStyle(payIcon).color } : null } : null,
    docSW: document.documentElement.scrollWidth
  });
})()" 2>/dev/null | tail -1
echo ""
echo "=== clone-v54 done ==="
EOF
