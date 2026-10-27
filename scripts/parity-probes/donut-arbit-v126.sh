#!/usr/bin/env bash
# donut-arbit-v126.sh — the ONE-SHOT both-sides census for the v126
# candidate pin family: the SPENDING BREAKDOWN DONUT'S GEOMETRY at 390x844
# on /dashboard — the never-pinned family on the mobile twin #2's own
# surface (the coverage map across all 24 specs: the v9/v14 pins hold the
# donut's DATA order + the hover tooltip fill; the v31 pin the keyboard
# semantics; the v44 F3 + v49 pins the LEGEND at 1280/390; the v76 pin the
# LABEL CHROME at 1280 [count/lineCount/fs/fill — never the geometry]; the
# v101 pin the CARD BOX + header at 1280; the donut's rendered GEOMETRY —
# the svg's w/h, the pie circle's bbox/center/radius — held by NO spec at
# ANY viewport).
# BOTH SIDES measured (READ-ONLY — login + passive navigation only, the
# v46 rule; no pointer interaction on this surface). The census reads the
# LIVE geometry after the settle: the card box (the radius/white walk from
# the "Spending Breakdown" text leaf — the v78 finder form, TAG-AGNOSTIC
# [the title is a plain div on both sites, never a role=heading — the v42
# idiom]); the donut wrapper (the svg's parent — the fixed-height
# ResponsiveContainer box); the svg (the .recharts-surface); the pie circle
# (the UNION BBOX of the .recharts-pie-sector paths — the rendered
# diameter/center, never the svg's outer box); the sector/label counts +
# the labelLine contract (the v9 G1b twin at 390); the docSW guard.
# The v73 heredoc lesson: the QUOTED <<'EOF' with the env-injected census
# JS; no literal dollar sequences in the census JS (the v64 rule); no
# single quotes inside the single-quoted census strings (the v60 lesson).
set -u
cd "$(dirname "$0")/../.."

DONUT_JS='(async () => {
  const title = [...document.querySelectorAll("div, h1, h2, h3, h4, span, p")].find((e) =>
    (e.textContent || "").trim() === "Spending Breakdown" && e.children.length === 0);
  if (!title) return JSON.stringify({err: "no Spending Breakdown leaf"});
  let card = title;
  for (let i = 0; i < 8; i++) {
    card = card.parentElement;
    if (!card) break;
    const cs = getComputedStyle(card);
    if ((cs.borderRadius && cs.borderRadius !== "0px") || cs.backgroundColor === "rgb(255, 255, 255)") break;
  }
  if (!card) return JSON.stringify({err: "no card"});
  const cr = card.getBoundingClientRect();
  const svg = card.querySelector("svg.recharts-surface, svg");
  if (!svg) return JSON.stringify({err: "no svg", cardW: Math.round(cr.width)});
  const wrap = svg.parentElement;
  const wr = wrap.getBoundingClientRect();
  const wcs = getComputedStyle(wrap);
  const sr = svg.getBoundingClientRect();
  const sectors = [...card.querySelectorAll(".recharts-pie-sector path, path.recharts-pie-sector")];
  const labels = [...card.querySelectorAll("[class*=recharts-pie-label]")].filter(
    (e) => !/line/i.test(e.getAttribute("class") || ""));
  const labelLines = [...card.querySelectorAll("[class*=recharts-pie-label-line]")];
  let bb = null;
  if (sectors.length) {
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const p of sectors) {
      const r = p.getBoundingClientRect();
      x0 = Math.min(x0, r.x); y0 = Math.min(y0, r.y);
      x1 = Math.max(x1, r.x + r.width); y1 = Math.max(y1, r.y + r.height);
    }
    bb = { x: Math.round(x0), y: Math.round(y0), w: Math.round(x1 - x0), h: Math.round(y1 - y0) };
  }
  return JSON.stringify({
    docSW: document.documentElement.scrollWidth,
    vw: document.documentElement.clientWidth,
    card: { w: Math.round(cr.width), h: Math.round(cr.height) },
    wrap: { w: Math.round(wr.width), h: Math.round(wr.height), pos: wcs.position },
    svg: { w: Math.round(sr.width), h: Math.round(sr.height) },
    pieCircle: bb ? { ...bb, cx: Math.round(bb.x + bb.w / 2), cy: Math.round(bb.y + bb.h / 2), r: Math.round(bb.w / 2) } : null,
    sectorCount: sectors.length,
    labelCount: labels.length,
    labelLineCount: labelLines.length,
  });
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refdonut126"
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
agent-browser open "$REF/dashboard" >/dev/null 2>&1
sleep 5

echo "=== REF: the donut geometry census at 390 ==="
agent-browser eval "$DONUT_JS" 2>/dev/null | tail -1
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
DONUT_JS="$DONUT_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonedonut126"
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
agent-browser open "http://localhost:3200/dashboard" >/dev/null 2>&1
sleep 5

echo "=== CLONE: the donut geometry census at 390 ==="
agent-browser eval "$DONUT_JS" 2>/dev/null | tail -1
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v84.mjs 2>&1 | tail -2
echo "=== donut arbit v126 done ==="
