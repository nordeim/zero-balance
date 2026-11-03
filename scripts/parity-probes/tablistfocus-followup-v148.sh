#!/usr/bin/env bash
# tablistfocus-followup-v148.sh — the FOLLOW-UP census for the v148
# discovery: two questions. (1) The outline-color resolution (the v148
# discovery measured the focused outline geometry; the color determines
# visibility — captured here at every rung). (2) THE LIABILITIES-ACTIVE
# TABLIST CHROME: the discovery found the Radix AUTOMATIC-ACTIVATION
# onFocus handler (react-tabs dist: onFocus -> onValueChange when
# !isSelected && automatic) flips the tab on a bare focus of the inactive
# trigger — and the flipped state read DIFFERENTLY on the two sites
# (REF Liabilities-active bg rgb(255,237,213) color rgb(124,45,18) vs
# CLONE bg rgb(220,252,231) color rgb(20,83,45)). The reference own
# construct needs the deliberate read: the Liabilities tab activated by
# the FULL POINTER-EVENT SEQUENCE (the v120 lesson — the Radix tabs
# activate on pointerdown, not the bare el.click()), both triggers
# measured before + after, PLUS the Assets restore. VIEW-STATE only
# (tab switching mutates no data — the v46 rule holds).
# The v73 heredoc lesson: the QUOTED <<'EOF' with the env-injected census
# JS for the clone half; no literal dollar sequences in the census JS
# (the v64 rule); no apostrophes in the single-quoted census strings
# (the v60 lesson); tr -d '"' on the extraction (the v124 lesson).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS='(async () => {
  const readTabs = () => {
    const triggers = [...document.querySelectorAll("button[role=tab]")];
    return triggers.map((t) => {
      const cs = getComputedStyle(t);
      return {
        txt: (t.textContent || "").replace(/[^A-Za-z]/g, "").slice(0, 12),
        sel: t.getAttribute("aria-selected"),
        state: t.getAttribute("data-state"),
        bg: cs.backgroundColor,
        color: cs.color,
        shadow: cs.boxShadow,
        cls: (t.className || "").slice(0, 400),
      };
    });
  };
  const out = { view: "tablistfollowup-390-v148" };
  out.atRest = readTabs();
  const liab = document.querySelectorAll("button[role=tab]")[1];
  const r = liab.getBoundingClientRect();
  const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
  for (const typ of ["pointerdown", "mousedown", "pointerup", "mouseup", "click"]) {
    const Ctor = typ.startsWith("pointer") ? window.PointerEvent : window.MouseEvent;
    liab.dispatchEvent(new Ctor(typ, { bubbles: true, cancelable: true, button: 0, clientX: cx, clientY: cy }));
    await new Promise((res) => setTimeout(res, 80));
  }
  await new Promise((res) => setTimeout(res, 500));
  out.liabilitiesActive = readTabs();
  const assets = document.querySelectorAll("button[role=tab]")[0];
  const r2 = assets.getBoundingClientRect();
  const ax = r2.x + r2.width / 2, ay = r2.y + r2.height / 2;
  for (const typ of ["pointerdown", "mousedown", "pointerup", "mouseup", "click"]) {
    const Ctor = typ.startsWith("pointer") ? window.PointerEvent : window.MouseEvent;
    assets.dispatchEvent(new Ctor(typ, { bubbles: true, cancelable: true, button: 0, clientX: ax, clientY: ay }));
    await new Promise((res) => setTimeout(res, 80));
  }
  await new Promise((res) => setTimeout(res, 500));
  out.assetsRestored = readTabs();
  return JSON.stringify(out);
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="reffoll148"
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
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF: the liabilities-active tablist follow-up (390) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1 | tr -d '"'
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
CENSUS_JS="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonefoll148"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
LOGIN_JS="(async () => {
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
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "clone login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
  sleep 3
done
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== CLONE: the liabilities-active tablist follow-up (390) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1 | tr -d '"'
pkill -f "agent-browser" 2>/dev/null
echo "=== tablistfocus follow-up v148 done ==="
EOF
