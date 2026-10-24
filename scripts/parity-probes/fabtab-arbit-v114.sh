#!/usr/bin/env bash
# fabtab-arbit-v114.sh — the ONE-SHOT both-sides arbitration for the v114
# mobile twins pair's flags (both surfaces at 390x844):
#   (1) the FAB claim (the VLM, BOTH pairs: "an 'Edit with Base44'
#       toast/tooltip overlay present in Image 1 [the REFERENCE], absent
#       in Image 2" — the platform-chrome class; the v85/v91/v97/v103/v108
#       standing disproof form: the FAB never renders in the app DOM on
#       EITHER side — it lives in the reference's platform iframe chrome,
#       outside the queryable body DOM). A FAB flag WAS raised this
#       cycle, so the disproof runs (the v103 standing class).
#   (2) the NEW tab-bar alignment claim (the VLM, networth pair: "the
#       Assets/Liabilities tab buttons in the reference are CENTERED
#       within their container; in the clone, LEFT-ALIGNED (or the
#       container is wider with no centering)" — a width-consequence
#       candidate: the v53 tablist-390 pin documents the reference's own
#       list as 432 wide inside its 464-overflow page vs the clone's 358
#       in-bounds — the v41 mobile-superset width family; the census
#       measures the tablist geometry + the full non-width chrome on BOTH
#       sides — the census is the authority, never the verdict).
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

TABLIST_JS="(async () => {
  const triggers = [...document.querySelectorAll('button[role=tab]')];
  const active = triggers.find(t => t.getAttribute('aria-selected') === 'true');
  const inactive = triggers.find(t => t.getAttribute('aria-selected') === 'false');
  const list = document.querySelector('[role=tablist]');
  if (!active || !inactive || !list) return JSON.stringify({ tablist: 'no tablist' });
  const lcs = getComputedStyle(list);
  const lr = list.getBoundingClientRect();
  const parent = list.parentElement;
  const pr = parent ? parent.getBoundingClientRect() : null;
  const grab = (t) => {
    const cs = getComputedStyle(t);
    const r = t.getBoundingClientRect();
    const icon = t.querySelector('svg');
    return {
      w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x),
      radius: cs.borderRadius, fs: cs.fontSize, fw: cs.fontWeight,
      color: cs.color, bg: cs.backgroundColor, pad: cs.padding,
      icon: icon ? { w: Math.round(icon.getBoundingClientRect().width), h: Math.round(icon.getBoundingClientRect().height) } : null
    };
  };
  return JSON.stringify({
    tablist: {
      x: Math.round(lr.x), w: Math.round(lr.width), h: Math.round(lr.height),
      display: lcs.display, gridCols: lcs.gridTemplateColumns,
      bg: lcs.backgroundColor, radius: lcs.borderRadius,
      pad: lcs.padding, maxW: lcs.maxWidth,
      jc: lcs.justifyContent, ai: lcs.alignItems,
      parentW: pr ? Math.round(pr.width) : null
    },
    active: grab(active), inactive: grab(inactive),
    docSW: document.documentElement.scrollWidth
  });
})()"

echo "=== REFERENCE side (390) ==="
export AGENT_BROWSER_SESSION="reffabtab114"
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

echo "--- /networth: TABLIST census:"
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$TABLIST_JS" 2>/dev/null | tail -1
echo "--- /networth: FAB census:"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
echo "--- /: FAB census:"
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1

echo "=== CLONE side (390) ==="
cd "$(dirname "$0")/../.."
FAB_JS="$FAB_JS" TABLIST_JS="$TABLIST_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonefabtab114"
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

echo "--- /networth: TABLIST census:"
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$TABLIST_JS" 2>/dev/null | tail -1
echo "--- /networth: FAB census:"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
echo "--- /: FAB census:"
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
EOF
echo "=== fabtab arbit v114 done ==="
