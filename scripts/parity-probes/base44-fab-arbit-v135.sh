#!/usr/bin/env bash
# base44-fab-arbit-v135.sh — the ONE-SHOT both-sides arbitration for the
# v135 login pair's FAB flag (the /login surface at desktop 1280x800):
#   the FAB claim (the VLM: "a black 'Edit with Base44' floating action
#   button in the bottom-right corner of the viewport. Image 2 does not
#   have this element" — the platform-chrome class; the v97/v103/v108/
#   v109/v115 standing disproof form: the FAB never renders in the app DOM
#   on EITHER side — it lives in the reference's platform iframe chrome,
#   outside the queryable body DOM).
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

echo "=== REFERENCE side (1280, /login — the flagged surface, logged-out) ==="
export AGENT_BROWSER_SESSION="reffab135"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census:"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /login — the flagged surface, logged-out) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonefab135"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census:"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
EOF
echo "=== base44-fab arbit v135 done ==="
