#!/usr/bin/env bash
# base44-fab-arbit-v108.sh — the ONE-SHOT both-sides arbitration for the
# v108 mobile twins pair's flags (the dashboard surface at 390x844):
#   (1) the FAB claim (the VLM: "an 'Edit with Base44' tooltip/button
#       overlay present in Image 1 [the REFERENCE], absent in Image 2" —
#       the platform-chrome class; the v97/v103 standing disproof form:
#       the FAB never renders in the app DOM on EITHER side — it lives in
#       the reference's platform iframe chrome, outside the queryable
#       body DOM).
#   (2) the NEW burger flag (the VLM's first run: "the hamburger menu icon
#       in the top-left corner is missing in Image 2 [the CLONE]" — an
#       icon-glyph misread candidate: remediation-plan-v3/v7 document the
#       REFERENCE's own toggle as a 28x28 button with the lucide
#       panel-left icon at 16px, near-black — the SAME glyph the clone
#       renders; the census measures the rect + the accessible name + the
#       svg glyph fingerprint on BOTH sides — the census is the authority,
#       never the verdict).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

FAB_JS="(async () => {
  const hits = [...document.querySelectorAll('body *')].filter(el => {
    const t = (el.textContent || '').trim();
    return t.length > 0 && t.length < 40 && /Base44/i.test(t) && el.children.length <= 2;
  });
  const out = hits.map(el => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return {
      tag: el.tagName,
      text: (el.textContent || '').trim().slice(0, 30),
      fixed: cs.position,
      bottom: Math.round(window.innerHeight - r.bottom),
      right: Math.round(window.innerWidth - r.right),
      w: Math.round(r.width),
      h: Math.round(r.height),
      bg: cs.backgroundColor,
      color: cs.color,
    };
  });
  return JSON.stringify({ fabCount: out.length, fabs: out, bodyHasBase44: /Base44/.test(document.body.textContent || '') });
})()"

BURGER_JS="(async () => {
  // the topbar burger: the topmost-leftmost small button in the header band
  // (the standing-check fallback finder, position-based — tag-agnostic)
  const btns = [...document.querySelectorAll('button')].filter(b => {
    const r = b.getBoundingClientRect();
    return r.top < 90 && r.width < 60 && r.height < 60 && r.width > 0;
  });
  const b = btns.sort((x, y) => (x.getBoundingClientRect().x - y.getBoundingClientRect().x) || (x.getBoundingClientRect().y - y.getBoundingClientRect().y))[0];
  if (!b) return JSON.stringify({ burgerFound: false });
  const r = b.getBoundingClientRect();
  const svg = b.querySelector('svg');
  const path = svg ? svg.querySelector('path') : null;
  return JSON.stringify({
    burgerFound: true,
    rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
    accessibleName: (b.getAttribute('aria-label') || b.textContent || '').trim().slice(0, 30),
    svgClass: svg ? (svg.getAttribute('class') || '').slice(0, 60) : null,
    svgW: svg ? Math.round(svg.getBoundingClientRect().width) : null,
    svgH: svg ? Math.round(svg.getBoundingClientRect().height) : null,
    pathD: path ? (path.getAttribute('d') || '').slice(0, 40) : null,
    stroke: svg ? getComputedStyle(svg).stroke : null,
  });
})()"

echo "=== REFERENCE side (390, /) ==="
export AGENT_BROWSER_SESSION="reffab108"
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
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census:"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
echo "--- burger census:"
agent-browser eval "$BURGER_JS" 2>/dev/null | tail -1

echo "=== CLONE side (390, /) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonefab108"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census:"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
echo "--- burger census:"
agent-browser eval "$BURGER_JS" 2>/dev/null | tail -1
EOF
echo "=== base44-fab arbit v108 done ==="
