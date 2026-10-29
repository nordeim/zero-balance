#!/usr/bin/env bash
# badgehover-arbit-v132.sh — the ONE-SHOT both-sides census for the v132
# candidate pin family: the NETWORTH asset-card TYPE BADGE's HOVER
# END-STATE at mobile 390x844 on /networth — the never-pinned HOVER PATH
# of the pinned networth badge family (the v29 G1 pins hold the class
# TOKEN + the AT-REST computed bg/color — networth.spec.ts:193-198/229-234,
# the class-token form, never the hover END-STATE; the hovered tint
# rgba(245,245,245,0.8) — globals.css's .zb-badge-hover:hover rule, the
# reference's own measured value [the v28 G1 family] — held on THIS FILE
# by NO spec at ANY viewport; the v127 pin holds the hover path on the
# ITEM-CARD badge only [item-card.tsx — a different file, a different
# at-rest family rgb(248,250,252)]):
#   the TYPE badge's ladder — the at-rest bg rgb(243,244,246) (the
#   networth family's hex-pinned #f3f4f6) -> the hovered
#   rgba(245,245,245,0.8) -> the restored at-rest.
# The badge target: the "Bank Account" leaf — the SAME LABEL TEXT on both
# sides (the reference's only asset carries it; the clone's Everyday
# Account card carries it), so the w/h axes compare byte-for-byte too.
# BOTH SIDES measured (READ-ONLY — login + passive navigation + a REAL
# pointer hover only, the v46 rule; the hover reveals chrome, it clicks
# nothing — the v125/v127 badge-hover precedent's own form). The hover
# moves the REAL pointer to the badge's OWN center (the coords read live
# after the scrollIntoView — never guessed; the mouse move takes x y as
# TWO args — the v123 lesson); the ladder parks at (5,5) first (the v22
# lesson), reads the at-rest state, hovers, reads the end-state, parks
# back, and verifies the restore. The v73 heredoc lesson: the QUOTED
# <<'EOF' with the env-injected census JS for the clone half; no literal
# dollar sequences in the census JS (the v64 rule); no single quotes
# inside the single-quoted census strings (the v60 lesson); the plain
# comma-pair center return (the v116 convention); tr -d '"' on the
# extraction (the v124 lesson); TAG-AGNOSTIC finders (the v107 lesson —
# the reference's badge is a Badge-base DIV, the clone's a SPAN).
set -u
cd "$(dirname "$0")/../.."

BADGE_FINDER='(async () => {
  // TAG-AGNOSTIC leaf finder: the "Bank Account" text leaf with the badge
  // chrome guards (radius 6px + fs 12px — state-independent, shared by
  // both sites per the v132 survey probe: ref DIV 115x22, clone SPAN).
  const badges = [...document.querySelectorAll("span, div")].filter((s) => {
    const t = (s.textContent || "").trim();
    if (t !== "Bank Account" || s.children.length !== 0) return false;
    const cs = getComputedStyle(s);
    return cs.borderRadius === "6px" && cs.fontSize === "12px";
  });
  if (badges.length !== 1) return JSON.stringify({err: "badge count " + badges.length});
  badges[0].scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = badges[0].getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

STATE_JS='(async () => {
  const badges = [...document.querySelectorAll("span, div")].filter((s) => {
    const t = (s.textContent || "").trim();
    if (t !== "Bank Account" || s.children.length !== 0) return false;
    const cs = getComputedStyle(s);
    return cs.borderRadius === "6px" && cs.fontSize === "12px";
  });
  if (badges.length !== 1) return JSON.stringify({err: "badge count " + badges.length});
  const badge = badges[0];
  const cs = getComputedStyle(badge);
  const r = badge.getBoundingClientRect();
  return JSON.stringify({
    hoverMatch: badge.matches(":hover"),
    bg: cs.backgroundColor,
    color: cs.color,
    transitionProperty: cs.transitionProperty,
    transitionDuration: cs.transitionDuration,
    w: Math.round(r.width),
    h: Math.round(r.height),
  });
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refbadge132"
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
  echo "ref login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 5

echo "=== REF: the badge finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$BADGE_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
echo "$CENTER"
CX="${CENTER%,*}"
CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on REF"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: HOVERED (real pointer at the badge center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
BADGE_FINDER="$BADGE_FINDER" STATE_JS="$STATE_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonebadge132"
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
sleep 5

echo "=== CLONE: the badge finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$BADGE_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
echo "$CENTER"
CX="${CENTER%,*}"
CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on CLONE"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: HOVERED (real pointer at the badge center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
echo "=== badgehover arbit v132 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
