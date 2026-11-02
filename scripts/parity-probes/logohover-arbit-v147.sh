#!/usr/bin/env bash
# logohover-arbit-v147.sh — the ONE-SHOT both-sides census for the v147
# candidate pin family: the LOGIN LOGO's OWN-HOVER LADDER at desktop
# 1280x800 on /login (the login pair's own surface, logged-out) — the
# never-pinned HOVER PATH of the login logo's decorative micro-interaction
# family (the v7 G3 pin holds the .zb-logo-ring 4px white/50 halo AT-REST —
# a DIFFERENT element; the v75 F4 pin the logo img's geometry AT-REST; the
# v141 pin the submit's own-hover — a DIFFERENT element; the logo's own-
# hover end-state held by NO spec at ANY viewport — verified by the
# suite-wide survey: rg 'logo' across tests/e2e/*.spec.ts — every match
# at-rest chrome {the ring color, the 96x96 geometry, the alt}).
#   the logo ladder — the at-rest chrome -> the OWN-HOVERED end-state
#   -> the restored at-rest.
# The construct under test (the discovery-measured DOM, both sides): the
# logo group (div.group) carrying the BLUR HALO layer (opacity 0.3,
# blur(24px), group-hover:opacity-40) + the CHIP span (shadow-lg,
# group-hover:shadow-xl, transition-all 0.3s) + the img (96x96). The
# expected own-hover end-state: the halo opacity 0.3 -> 0.4 + the chip
# shadow-lg -> shadow-xl with the geometry/filter family unchanged.
# BOTH SIDES measured (READ-ONLY — passive navigation + REAL pointer
# MOVES only, the v46 rule; a mouse MOVE on a decorative div dispatches
# no click and the logged-out surface holds no session to mutate — the
# census cannot change state; the logo is NEVER clicked — it is passive
# decoration, no handler). The hover moves the REAL pointer to the logo
# group's OWN center (the coords read live after the settle — never
# guessed; the mouse move takes x y as TWO args — the v123 lesson); the
# ladder parks at (5,5) first (the v22 lesson), reads the at-rest state,
# hovers the logo, reads, parks back, and verifies the restore. The v73
# heredoc lesson: the QUOTED <<'EOF' with the env-injected census JS for
# the clone half; no literal dollar sequences in the census JS (the v64
# rule); no single quotes inside the single-quoted census strings (the
# v60 lesson); the plain comma-pair center return (the v116 convention);
# tr -d '"' on the extraction (the v124 lesson); STRUCTURAL finder
# (img[alt*=logo] -> the group = img.parentElement.parentElement — the
# form shared by both sites, the alt cross-checked in the census output).
set -u
cd "$(dirname "$0")/../.."

CENTER_JS='(async () => {
  const img = document.querySelector("img[alt*=logo i]");
  if (!img) return JSON.stringify({err: "no logo img"});
  const group = img.parentElement ? img.parentElement.parentElement : null;
  if (!group) return JSON.stringify({err: "no group"});
  group.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = group.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

STATE_JS='(async () => {
  const img = document.querySelector("img[alt*=logo i]");
  if (!img) return JSON.stringify({err: "no logo img"});
  const chip = img.parentElement;
  const group = chip ? chip.parentElement : null;
  if (!group) return JSON.stringify({err: "no group"});
  const halo = group.children[0];
  const gs = getComputedStyle(group);
  const hs = getComputedStyle(halo);
  const cs = getComputedStyle(chip);
  const r = chip.getBoundingClientRect();
  return JSON.stringify({
    groupHover: group.matches(":hover"),
    imgAlt: (img.getAttribute("alt") || "").slice(0, 20),
    haloOpacity: hs.opacity,
    haloFilter: hs.filter,
    haloTransition: hs.transitionProperty + " " + hs.transitionDuration,
    chipShadow: cs.boxShadow,
    chipTransition: cs.transitionProperty + " " + cs.transitionDuration,
    chipW: Math.round(r.width),
    chipH: Math.round(r.height),
    groupClass: (group.className && String(group.className).slice(0, 24)) || ""
  });
})()'

# ---------- REFERENCE half (direct, logged-out) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="reflogohov147"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1

echo "=== REF: the logo center (live, never guessed) ==="
CENTER="$(agent-browser eval "$CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "logo center: $CENTER"
CX="${CENTER%,*}"; CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on REF"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: LOGO-HOVERED (real pointer at the logo center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
CENTER_JS="$CENTER_JS" STATE_JS="$STATE_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonelogohov147"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1

echo "=== CLONE: the logo center (live, never guessed) ==="
CENTER="$(agent-browser eval "$CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "logo center: $CENTER"
CX="${CENTER%,*}"; CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on CLONE"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: LOGO-HOVERED (real pointer at the logo center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
echo "=== logohover arbit v147 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
