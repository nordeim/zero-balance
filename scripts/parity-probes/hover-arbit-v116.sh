#!/usr/bin/env bash
# hover-arbit-v116.sh — the v116 pre-plan one-shot both-sides census: the
# SAVINGS goal-card's kebab TRIGGER at 1280x800 (the hover-revealed action
# element's box chrome + the at-rest/hover opacity behavior) — measured on
# BOTH sides (the reference + the clone) in one script, two sessions.
# STRUCTURAL finders (the class strings NOT trusted): the goal card via the
# Emergency Fund h4's rounded-xl ancestor (the v54 walk), the trigger via
# the at-rest opacity-0 button INSIDE the card's title area.
# READ-ONLY on BOTH sides (login + passive navigation + a REAL pointer hover
# only — the v46 rule; the hover reveals chrome, it clicks nothing).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS='(async () => {
  const h4 = [...document.querySelectorAll("h4")].find((x) =>
    /Emergency Fund/i.test((x.textContent || "").trim()));
  if (!h4) return JSON.stringify({err: "no Emergency Fund h4"});
  let card = h4.closest("div.rounded-xl") || h4.parentElement;
  if (!card) return JSON.stringify({err: "no card"});
  const grab = (b) => {
    const cs = getComputedStyle(b);
    const r = b.getBoundingClientRect();
    const cr = card.getBoundingClientRect();
    return {
      tag: b.tagName,
      opacity: cs.opacity,
      display: cs.display,
      h: Math.round(r.height),
      w: Math.round(r.width),
      radius: cs.borderRadius,
      bg: cs.backgroundColor,
      color: cs.color,
      cardTop: Math.round(r.top - cr.top),
      cardRight: Math.round(cr.right - r.right),
      docSW: document.documentElement.scrollWidth,
    };
  };
  // At REST (pointer parked at 5,5 — the v22 lesson): the trigger is the
  // button inside the card whose computed opacity reads "0".
  const buttons = [...card.querySelectorAll("button")];
  const trigger = buttons.find((b) => getComputedStyle(b).opacity === "0" && Math.round(b.getBoundingClientRect().width) < 60);
  if (!trigger) return JSON.stringify({err: "no at-rest trigger", btnCount: buttons.length});
  return JSON.stringify(grab(trigger));
})()'

HOVER_JS='(async () => {
  const h4 = [...document.querySelectorAll("h4")].find((x) =>
    /Emergency Fund/i.test((x.textContent || "").trim()));
  if (!h4) return JSON.stringify({err: "no Emergency Fund h4"});
  let card = h4.closest("div.rounded-xl") || h4.parentElement;
  if (!card) return JSON.stringify({err: "no card"});
  const cr = card.getBoundingClientRect();
  const buttons = [...card.querySelectorAll("button")];
  const trigger = buttons.find((b) => Math.round(b.getBoundingClientRect().width) < 60 && Math.round(b.getBoundingClientRect().height) < 60 && (b.className.toString().includes("opacity") || getComputedStyle(b).opacity !== "1" || true));
  // the title-area trigger: the small square button in the card (the
  // kebab); on the clone it is the ONLY small square button at rest.
  const small = buttons.filter((b) => {
    const r = b.getBoundingClientRect();
    return r.width < 60 && r.height < 60 && (r.width === r.height);
  });
  if (small.length !== 1) return JSON.stringify({err: "small-button count", n: small.length});
  const t = small[0];
  const cs = getComputedStyle(t);
  const r = t.getBoundingClientRect();
  return JSON.stringify({
    hoverOpacity: cs.opacity,
    h: Math.round(r.height),
    w: Math.round(r.width),
    radius: cs.borderRadius,
    bg: cs.backgroundColor,
    color: cs.color,
  });
})()'

LOGIN_JS='(async () => {
  const em = document.querySelector("input[type=email], input[name=email]");
  const pw = document.querySelector("input[type=password]");
  if (!em || !pw) return "no inputs";
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set.call(el, v);
    el.dispatchEvent(new Event("input", { bubbles: true }));
  };
  set(em, "EMAIL_HERE");
  set(pw, "PASSWORD_HERE");
  em.closest("form").requestSubmit();
  return "submitted";
})()'

run_side () {
  local BASE="$1" EMAIL="$2" PASSWORD="$3" SESS="$4" LABEL="$5"
  export AGENT_BROWSER_SESSION="$SESS"
  agent-browser open "$BASE/login" >/dev/null 2>&1
  sleep 4
  local JS="${LOGIN_JS/EMAIL_HERE/$EMAIL}"; JS="${JS/PASSWORD_HERE/$PASSWORD}"
  local RESULT=""
  for attempt in 1 2 3; do
    RESULT=$(agent-browser eval "$JS" 2>/dev/null | tail -1)
    if echo "$RESULT" | grep -q "submitted"; then break; fi
    agent-browser open "$BASE/login" >/dev/null 2>&1
    sleep 4
  done
  echo "$LABEL login: $RESULT"
  sleep 4
  agent-browser set viewport 1280 800 >/dev/null 2>&1
  agent-browser open "$BASE/savings" >/dev/null 2>&1
  sleep 4
  echo "=== $LABEL AT-REST (pointer parked 5,5) ==="
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
  echo "=== $LABEL HOVER (pointer at the card's OWN center — dynamic; the static 640,300 missed the reference's col-1 card) ==="
  local CENTER
  CENTER=$(agent-browser eval "(async () => {
    const h4 = [...document.querySelectorAll('h4')].find((x) => /Emergency Fund/i.test((x.textContent || '').trim()));
    if (!h4) return '0,0';
    let card = h4.closest('div.rounded-xl') || h4.parentElement;
    if (!card) return '0,0';
    const r = card.getBoundingClientRect();
    return Math.round(r.left + r.width / 2) + ',' + Math.round(r.top + r.height / 2);
  })()" 2>/dev/null | tail -1 | tr -d '"')
  echo "$LABEL card center: $CENTER"
  agent-browser mouse move "${CENTER%,*}" "${CENTER#*,}" >/dev/null 2>&1
  sleep 1
  agent-browser eval "$HOVER_JS" 2>/dev/null | tail -1
}

echo "########## REFERENCE SIDE ##########"
run_side "$REF" "sepnetflix2023@outlook.com" '$Abcd1234' "hoverref116" "ref"

pkill -f "agent-browser" >/dev/null 2>&1
sleep 2

echo "########## CLONE SIDE (the :3200 parity server) ##########"
bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="hoverclone116"
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
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 4
CENSUS_JS='(async () => {
  const h4 = [...document.querySelectorAll("h4")].find((x) =>
    /Emergency Fund/i.test((x.textContent || "").trim()));
  if (!h4) return JSON.stringify({err: "no Emergency Fund h4"});
  let card = h4.closest("div.rounded-xl") || h4.parentElement;
  if (!card) return JSON.stringify({err: "no card"});
  const grab = (b) => {
    const cs = getComputedStyle(b);
    const r = b.getBoundingClientRect();
    const cr = card.getBoundingClientRect();
    return {
      tag: b.tagName,
      opacity: cs.opacity,
      display: cs.display,
      h: Math.round(r.height),
      w: Math.round(r.width),
      radius: cs.borderRadius,
      bg: cs.backgroundColor,
      color: cs.color,
      cardTop: Math.round(r.top - cr.top),
      cardRight: Math.round(cr.right - r.right),
      docSW: document.documentElement.scrollWidth,
    };
  };
  const buttons = [...card.querySelectorAll("button")];
  const trigger = buttons.find((b) => getComputedStyle(b).opacity === "0" && Math.round(b.getBoundingClientRect().width) < 60);
  if (!trigger) return JSON.stringify({err: "no at-rest trigger", btnCount: buttons.length});
  return JSON.stringify(grab(trigger));
})()'
HOVER_JS='(async () => {
  const h4 = [...document.querySelectorAll("h4")].find((x) =>
    /Emergency Fund/i.test((x.textContent || "").trim()));
  if (!h4) return JSON.stringify({err: "no Emergency Fund h4"});
  let card = h4.closest("div.rounded-xl") || h4.parentElement;
  if (!card) return JSON.stringify({err: "no card"});
  const buttons = [...card.querySelectorAll("button")];
  const small = buttons.filter((b) => {
    const r = b.getBoundingClientRect();
    return r.width < 60 && r.height < 60 && (r.width === r.height);
  });
  if (small.length !== 1) return JSON.stringify({err: "small-button count", n: small.length});
  const t = small[0];
  const cs = getComputedStyle(t);
  const r = t.getBoundingClientRect();
  return JSON.stringify({
    hoverOpacity: cs.opacity,
    h: Math.round(r.height),
    w: Math.round(r.width),
    radius: cs.borderRadius,
    bg: cs.backgroundColor,
    color: cs.color,
  });
})()'
echo "=== CLONE AT-REST (pointer parked 5,5) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE HOVER (pointer at the card's OWN center — dynamic) ==="
CENTER=$(agent-browser eval "(async () => {
  const h4 = [...document.querySelectorAll('h4')].find((x) => /Emergency Fund/i.test((x.textContent || '').trim()));
  if (!h4) return '0,0';
  let card = h4.closest('div.rounded-xl') || h4.parentElement;
  if (!card) return '0,0';
  const r = card.getBoundingClientRect();
  return Math.round(r.left + r.width / 2) + ',' + Math.round(r.top + r.height / 2);
})()" 2>/dev/null | tail -1 | tr -d '"')
echo "clone card center: $CENTER"
agent-browser mouse move "${CENTER%,*}" "${CENTER#*,}" >/dev/null 2>&1
sleep 1
agent-browser eval "$HOVER_JS" 2>/dev/null | tail -1
EOF
echo "=== hover arbit v116 done ==="
