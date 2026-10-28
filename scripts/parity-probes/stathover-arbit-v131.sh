#!/usr/bin/env bash
# stathover-arbit-v131.sh — the ONE-SHOT both-sides census for the v131
# candidate pin family: the INTERACTIVE STAT CARD's OWN-HOVER REVEAL
# END-STATES at 1280x800 on /dashboard — the never-pinned PATH of the
# pinned stat-card family (the v40 pin holds the TAB stops + the geometry
# bands + the Enter/Space SUPERSET activation; the v42 pin the hero grid
# census; the v51 F2 pin the AT-REST grid/card/circle/icon chrome; the
# v88 pin the count-row + the divider + the trend colors; the stat
# card's HOVER END-STATES held by NO spec):
#   (1) the RADIAL-GRADIENT CIRCLE's group-hover:opacity-10 reveal — the
#       at-rest opacity 0 -> the hovered 0.1 (the decorative
#       absolute top-0 right-0 w-32 h-32 rounded-full circle, present on
#       BOTH sites — the reference's own group-hover idiom, verified
#       live this cycle on its card: absolute top-0 right-0 w-32 h-32
#       rounded-full opacity-0 group-hover:opacity-10, transition
#       opacity 0.3s);
#   (2) the CHEVRON-RIGHT's group-hover:opacity-100 reveal — the
#       at-rest opacity 0 -> the hovered 1 (the trailing affordance svg,
#       w-5 h-5 = 20px, transition opacity 0.2s, present on BOTH sites).
# BOTH SIDES measured (READ-ONLY — login + passive navigation + a REAL
# pointer hover only, the v46 rule; the hover reveals chrome, it clicks
# nothing — the CLONE's card CLICKS NAVIGATE to the type view
# (/income for the Total Income card), so the card is NEVER clicked; the
# reference's card is an INERT div — cursor-pointer styling, no role,
# no tabindex, no handler — the v40 dead-UI class, its hover reveals
# pure CSS group-hover chrome). The hover moves the REAL pointer to the
# card's OWN center (the coords read live after the scrollIntoView —
# never guessed; the mouse move takes x y as TWO args — the v123
# lesson); the ladder parks at (5,5) first (the v22 lesson), reads the
# at-rest state, hovers, reads the end-states, parks back, and verifies
# the restore. The v73 heredoc lesson: the QUOTED <<'EOF' with the
# env-injected census JS; no literal dollar sequences in the census JS
# (the v64 rule); no single quotes inside the single-quoted census
# strings (the v60 lesson).
set -u
cd "$(dirname "$0")/../.."

CARD_FINDER='(async () => {
  const h3 = [...document.querySelectorAll("h3")].find((x) =>
    (x.textContent || "").trim() === "Total Income");
  if (!h3) return JSON.stringify({err: "no Total Income h3"});
  let card = h3;
  while (card && card.parentElement) {
    const p = card.parentElement;
    const statCards = [...p.children].filter((c) =>
      [...c.querySelectorAll("h3")].some((h) =>
        /^(Total Income|Total Savings|Total Expenses)$/.test((h.textContent || "").trim())));
    if (statCards.length >= 2) break;
    card = p;
  }
  const first = [...card.parentElement.children].find((c) =>
    [...c.querySelectorAll("h3")].some((h) => (h.textContent || "").trim() === "Total Income"));
  if (!first) return JSON.stringify({err: "no first card"});
  first.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = first.getBoundingClientRect();
  // the PLAIN comma-pair return (the v116 convention — the JSON form is
  // printed with escaped quotes that break the shell-side sed extraction)
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

STATE_JS='(async () => {
  const h3 = [...document.querySelectorAll("h3")].find((x) =>
    (x.textContent || "").trim() === "Total Income");
  if (!h3) return JSON.stringify({err: "no h3"});
  let card = h3;
  while (card && card.parentElement) {
    const p = card.parentElement;
    const statCards = [...p.children].filter((c) =>
      [...c.querySelectorAll("h3")].some((h) =>
        /^(Total Income|Total Savings|Total Expenses)$/.test((h.textContent || "").trim())));
    if (statCards.length >= 2) break;
    card = p;
  }
  const first = [...card.parentElement.children].find((c) =>
    [...c.querySelectorAll("h3")].some((h) => (h.textContent || "").trim() === "Total Income"));
  if (!first) return JSON.stringify({err: "no card in state read"});
  // the RADIAL CIRCLE: the absolute rounded-full decorative div
  // (TAG-AGNOSTIC, by computed shape — the 9999px radius + the absolute
  // position; present on BOTH sites)
  const radial = [...first.querySelectorAll("div")].find((d) => {
    const cs = getComputedStyle(d);
    return cs.position === "absolute" && cs.borderRadius === "9999px";
  });
  // the CHEVRON: the affordance svg in the 19..21 width band (w-5 = 20px;
  // TAG/CLASS-AGNOSTIC by computed shape, STATE-INDEPENDENT across the
  // ladder rungs — the v107 lesson: the reference carries
  // lucide-chevron-right w-5 h-5, the clone the same glyph at h-5 w-5;
  // the type icon is w-6 = 24px, the trend icon w-4 = 16px — the 20px
  // band is the chevron alone at EVERY rung, its opacity the animated
  // axis this census measures)
  const chevron = [...first.querySelectorAll("svg")].find((s) => {
    const r = s.getBoundingClientRect();
    return r.width >= 19 && r.width <= 21;
  });
  if (!radial || !chevron) return JSON.stringify({err: "no radial/chevron", radial: !!radial, chevron: !!chevron});
  const cr = getComputedStyle(radial);
  const cc = getComputedStyle(chevron);
  return JSON.stringify({
    cardHover: first.matches(":hover"),
    cardCursor: getComputedStyle(first).cursor,
    radial: { opacity: cr.opacity, transition: cr.transitionProperty + " " + cr.transitionDuration,
              w: Math.round(radial.getBoundingClientRect().width), h: Math.round(radial.getBoundingClientRect().height) },
    chevron: { opacity: cc.opacity, transition: cc.transitionProperty + " " + cc.transitionDuration,
               w: Math.round(chevron.getBoundingClientRect().width) },
  });
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refstathover131"
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/dashboard" >/dev/null 2>&1
sleep 4

echo "=== REF: the stat-card finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$CARD_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
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
  echo "=== REF: HOVERED (real pointer at the card center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
CARD_FINDER="$CARD_FINDER" STATE_JS="$STATE_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonestathover131"
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/dashboard" >/dev/null 2>&1
sleep 4

echo "=== CLONE: the stat-card finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$CARD_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
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
  echo "=== CLONE: HOVERED (real pointer at the card center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== stathover arbit v131 done ==="
