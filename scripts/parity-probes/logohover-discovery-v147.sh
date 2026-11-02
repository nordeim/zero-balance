#!/usr/bin/env bash
# logohover-discovery-v147.sh — the ONE-SHOT both-sides DISCOVERY census for
# the v147 candidate: the LOGIN LOGO's OWN-HOVER family at 1280 on /login.
# Dumps the logo img's ancestor chain + the group's children chrome so the
# formal ladder census can be written against BOTH sides' real structure.
# READ-ONLY: passive navigation + REAL pointer MOVES only (the v46 rule).
set -u
cd "$(dirname "$0")/../.."

DISCOVER_JS='(async () => {
  const img = document.querySelector("img[alt*=logo i]");
  if (!img) return JSON.stringify({err: "no logo img"});
  const chain = [];
  let el = img;
  for (let i = 0; i < 3 && el; i++) {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    chain.push({
      level: i,
      tag: el.tagName,
      cls: (el.className && String(el.className).slice(0, 60)) || "",
      opacity: cs.opacity,
      filter: cs.filter,
      boxShadow: cs.boxShadow.slice(0, 90),
      transition: cs.transitionProperty + " " + cs.transitionDuration,
      w: Math.round(r.width),
      h: Math.round(r.height),
      hover: el.matches(":hover")
    });
    el = el.parentElement;
  }
  const group = img.parentElement ? img.parentElement.parentElement : null;
  const kids = group ? [...group.children].map((k) => {
    const cs = getComputedStyle(k);
    return {
      tag: k.tagName,
      cls: (k.className && String(k.className).slice(0, 40)) || "",
      opacity: cs.opacity,
      filter: cs.filter,
      boxShadow: cs.boxShadow.slice(0, 70)
    };
  }) : [];
  return JSON.stringify({ alt: img.getAttribute("alt"), chain, kids });
})()'

HOVER_JS='(async () => {
  const img = document.querySelector("img[alt*=logo i]");
  if (!img) return JSON.stringify({err: "no logo img"});
  const group = img.parentElement.parentElement;
  const halo = group.children[0];
  const chip = img.parentElement;
  const read = () => {
    const gs = getComputedStyle(group);
    const hs = getComputedStyle(halo);
    const cs = getComputedStyle(chip);
    return {
      groupHover: group.matches(":hover"),
      haloOpacity: hs.opacity,
      haloFilter: hs.filter,
      haloTransition: hs.transitionProperty + " " + hs.transitionDuration,
      chipShadow: cs.boxShadow,
      chipTransition: cs.transitionProperty + " " + cs.transitionDuration,
      imgAlt: (img.getAttribute("alt") || "").slice(0, 20)
    };
  };
  return JSON.stringify(read());
})()'

REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="reflogodisc147"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF: logo DOM discovery (at-rest) ==="
agent-browser eval "$DISCOVER_JS" 2>/dev/null | tail -1
pkill -f "agent-browser" 2>/dev/null
sleep 3

DISCOVER_JS="$DISCOVER_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonelogodisc147"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== CLONE: logo DOM discovery (at-rest) ==="
agent-browser eval "$DISCOVER_JS" 2>/dev/null | tail -1
EOF
echo "=== discovery done ==="
