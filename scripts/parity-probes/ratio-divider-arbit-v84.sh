#!/usr/bin/env bash
# ratio-divider-arbit-v84.sh — DOM arbitration for the v84 NETWORTH VLM
# flag: "the reference includes a horizontal divider line above the
# 'Asset to Liability Ratio' text; this divider is missing in the clone".
# Measures the ratio footer row's computed borderTop (width/style/color)
# + its geometry on BOTH sides at mobile 390x844. The clone's source pins
# the divider unconditionally (net-worth-view.tsx: borderTop 1px solid
# rgba(255,255,255,0.2), no responsive variant; the v4-era structure test
# asserts it at 1280) — the census is the authority, not the VLM claim.
# READ-ONLY on the reference (the v46 rule). Double-quoted-heredoc-safe:
# no dollar sequences in the census JS; text-content filters only.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

DIVIDER_CENSUS="(async () => {
  const labels = [...document.querySelectorAll('span, p, div')].filter(el => {
    const t = (el.textContent || '').trim();
    return t === 'Asset to Liability Ratio' && el.children.length === 0;
  });
  if (!labels.length) return 'no ratio label found';
  const label = labels[0];
  let footer = label;
  for (let i = 0; i < 6; i++) {
    footer = footer.parentElement;
    if (!footer) break;
    const s = getComputedStyle(footer);
    if (s.borderTopWidth !== '0px' && s.borderTopStyle !== 'none') break;
  }
  if (!footer) return 'no footer found';
  const fs = getComputedStyle(footer);
  const fr = footer.getBoundingClientRect();
  const lr = label.getBoundingClientRect();
  const card = footer.closest('div');
  let walk = footer.parentElement;
  let gradient = null;
  while (walk && walk !== document.body) {
    const s = getComputedStyle(walk);
    if (s.backgroundImage && s.backgroundImage.includes('linear-gradient') && walk.getBoundingClientRect().height > 100) { gradient = walk; break; }
    walk = walk.parentElement;
  }
  const gr = gradient ? gradient.getBoundingClientRect() : null;
  return JSON.stringify({
    docSW: document.documentElement.scrollWidth,
    footer: {
      borderTopWidth: fs.borderTopWidth,
      borderTopStyle: fs.borderTopStyle,
      borderTopColor: fs.borderTopColor,
      marginTop: fs.marginTop,
      paddingTop: fs.paddingTop,
      rect: { w: Math.round(fr.width), h: Math.round(fr.height), top: Math.round(fr.top) }
    },
    label: { fs: getComputedStyle(label).fontSize, fw: getComputedStyle(label).fontWeight, rect: { w: Math.round(lr.width), h: Math.round(lr.height) } },
    cardBottom: gr ? Math.round(gr.bottom) : null,
    footerTop: Math.round(fr.top),
    dividerGap: gr ? Math.round(fr.top - gr.bottom) : null
  });
})()"

echo "=== REFERENCE side (390): ratio divider ==="
export AGENT_BROWSER_SESSION="refdiv84"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$DIVIDER_CENSUS" 2>/dev/null | tail -1

echo "=== CLONE side (390): ratio divider ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonediv84"
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
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$DIVIDER_CENSUS" 2>/dev/null | tail -1
EOF
echo "=== ratio divider arbit v84 done ==="
