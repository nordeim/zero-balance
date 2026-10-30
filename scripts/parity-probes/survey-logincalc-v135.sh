#!/usr/bin/env bash
# survey-logincalc-v135.sh — the F4 pin-candidate survey, REFERENCE side
# (the login + calculator surface — the v135 pair's own surfaces):
#   (a) the /login view (logged-out): the Sign in submit's own-hover bg
#       tint; the Google button's own-hover {bg,border,shadow}; the mode
#       links' presence + own-hover color;
#   (b) the CALCULATOR dialog (opened READ-ONLY via the REAL pointer press
#       on the Rent card's Calculate button — the ref-arbit v135 finder
#       form): the X close's FOCUS-VISIBLE ladder — at-rest -> the REAL
#       agent-browser-press-Tab FOCUSED rung (finder-bounded, NEVER Enter)
#       -> blurred. The v134 focusladder form; the v87 geometric X finder
#       (the reference's X lost its accessible name).
# READ-ONLY per the v46 rule: login + hover + dialog-open only — no form
# saves, no data mutations, no Delete clicks.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

center_of() { # $1 = the JS body returning "X,Y" or ERR
  agent-browser eval "$1" 2>/dev/null | tail -1 | tr -d '"'
}

echo "=== (a) REF /login (logged-out) — the button families ==="
export AGENT_BROWSER_SESSION="refsurvey135"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

ATREST_JS='(async () => {
  const q = (re) => [...document.querySelectorAll("button, a")].find(b => re.test((b.textContent || "").trim()));
  const submit = [...document.querySelectorAll("button[type=submit]")].find(b => /Sign in/i.test(b.textContent || ""));
  const google = q(/Continue with Google/i);
  const forgot = q(/Forgot password/i);
  const signup = q(/Need an account/i);
  const read = (el) => {
    if (!el) return "ABSENT";
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return { tag: el.tagName, txt: (el.textContent || "").trim().slice(0, 24), w: Math.round(r.width), h: Math.round(r.height), bg: cs.backgroundColor, color: cs.color, border: cs.borderTopColor, shadow: cs.boxShadow.slice(0, 80) };
  };
  return JSON.stringify({ submit: read(submit), google: read(google), forgot: read(forgot), signup: read(signup) });
})()'
agent-browser eval "$ATREST_JS" 2>/dev/null | tail -1

SUBMIT_C='(async () => {
  const b = [...document.querySelectorAll("button[type=submit]")].find(x => /Sign in/i.test(x.textContent || ""));
  if (!b) return "ERR";
  const r = b.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'
P=$(center_of "$SUBMIT_C"); echo "submit center: $P"
SX=$(echo "$P" | cut -d, -f1); SY=$(echo "$P" | cut -d, -f2)
agent-browser mouse move "$SX" "$SY" >/dev/null 2>&1; sleep 1
HOVER_JS='(async () => {
  const q = (re) => [...document.querySelectorAll("button, a")].find(b => re.test((b.textContent || "").trim()));
  const submit = [...document.querySelectorAll("button[type=submit]")].find(b => /Sign in/i.test(b.textContent || ""));
  const read = (el) => el ? { bg: getComputedStyle(el).backgroundColor, color: getComputedStyle(el).color, border: getComputedStyle(el).borderTopColor, shadow: getComputedStyle(el).boxShadow.slice(0, 80) } : "ABSENT";
  return JSON.stringify({ submitHover: read(submit), googleRest: read(q(/Continue with Google/i)), forgotRest: read(q(/Forgot password/i)) });
})()'
agent-browser eval "$HOVER_JS" 2>/dev/null | tail -1

GOOGLE_C='(async () => {
  const b = [...document.querySelectorAll("button")].find(x => /Continue with Google/i.test((x.textContent || "").trim()));
  if (!b) return "ERR";
  const r = b.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'
P=$(center_of "$GOOGLE_C"); echo "google center: $P"
GX=$(echo "$P" | cut -d, -f1); GY=$(echo "$P" | cut -d, -f2)
agent-browser mouse move "$GX" "$GY" >/dev/null 2>&1; sleep 1
agent-browser eval "$HOVER_JS" 2>/dev/null | tail -1

FORGOT_C='(async () => {
  const b = [...document.querySelectorAll("button, a")].find(x => /Forgot password/i.test((x.textContent || "").trim()));
  if (!b) return "ERR";
  const r = b.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'
P=$(center_of "$FORGOT_C"); echo "forgot-link center: $P"
FX=$(echo "$P" | cut -d, -f1); FY=$(echo "$P" | cut -d, -f2)
if [ "$FX" != "ERR" ] && [ -n "$FX" ]; then
  agent-browser mouse move "$FX" "$FY" >/dev/null 2>&1; sleep 1
  agent-browser eval "$HOVER_JS" 2>/dev/null | tail -1
fi
agent-browser mouse move 5 5 >/dev/null 2>&1; sleep 1

echo "=== (b) REF calculator dialog — the X's FOCUS-VISIBLE ladder ==="
LOGIN_JS='(async () => {
  const em = document.querySelector("input[type=email], input[name=email]");
  const pw = document.querySelector("input[type=password]");
  if (!em || !pw) return "no inputs";
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set.call(el, v);
    el.dispatchEvent(new Event("input", { bubbles: true }));
  };
  set(em, "sepnetflix2023@outlook.com");
  set(pw, "\$Abcd1234");
  em.closest("form").requestSubmit();
  return "submitted";
})()'
agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1
sleep 4
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1; sleep 1

# the Rent card finder RETRIES (the ref-arbit form)
POS=""
for attempt in 1 2 3 4 5; do
  POS=$(center_of '(async () => {
    const main = document.querySelector("main")||document.body;
    const card = [...main.querySelectorAll("div.rounded-xl")].find(c => (c.innerText||"").includes("Rent") && (c.innerText||"").includes("\$25"));
    if (!card) return "ERR";
    const r = card.getBoundingClientRect();
    return Math.round(r.x + r.width/2) + "," + Math.round(r.y + r.height/2);
  })()')
  if [ "$POS" != "ERR" ] && [ -n "$POS" ]; then break; fi
  echo "rent card not ready (attempt $attempt), waiting..."
  sleep 4
done
echo "rent card center: $POS"
RX=$(echo "$POS" | cut -d, -f1); RY=$(echo "$POS" | cut -d, -f2)
agent-browser mouse move "$RX" "$RY" >/dev/null 2>&1; sleep 1
CALC=$(center_of '(async () => {
  const main = document.querySelector("main")||document.body;
  const card = [...main.querySelectorAll("div.rounded-xl")].find(c => (c.innerText||"").includes("Rent") && (c.innerText||"").includes("\$25"));
  if (!card) return "ERR";
  const btn = [...card.querySelectorAll("button")].find(b => /^Calculate$/i.test(b.textContent.trim()));
  if (!btn) return "NOBTN";
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + "," + Math.round(r.y + r.height/2);
})()')
echo "calculate button center: $CALC"
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1; sleep 1
agent-browser mouse down >/dev/null 2>&1; sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3

# the X finder: the ref-arbit DUAL panel finder (the v99 form), then the v87 geometric X
X_FINDER='(function () {
  let panel = [...document.querySelectorAll("[role=dialog]")].find(d => (d.innerText||"").includes("Rent Calculator"));
  if (!panel) panel = [...document.querySelectorAll("div")].find(d => getComputedStyle(d).maxWidth === "768px" && d.getBoundingClientRect().width > 300);
  if (!panel) return null;
  const pr = panel.getBoundingClientRect();
  const cands = [...panel.querySelectorAll("button")].filter(b => {
    const r = b.getBoundingClientRect();
    return r.width > 20 && r.width < 60 && Math.abs(r.width - r.height) < 14 && (r.y - pr.y) < 120;
  });
  return cands[0] || null;
})()'

ATREST_X="(async () => {
  const x = $X_FINDER;
  if (!x) return 'NO X';
  const cs = getComputedStyle(x);
  return JSON.stringify({atRest: {bg: cs.backgroundColor, color: cs.color, outlineStyle: cs.outlineStyle, outlineWidth: cs.outlineWidth, outlineColor: cs.outlineColor, boxShadow: cs.boxShadow.slice(0, 90), opacity: cs.opacity}});
})()"
echo "--- X at-rest:"
agent-browser eval "$ATREST_X" 2>/dev/null | tail -1

echo "--- the REAL Tab walk to the X (finder-bounded, NEVER Enter):"
LANDED="NO"
for i in $(seq 1 25); do
  L=$(agent-browser eval "(async () => { const t = $X_FINDER; return (document.activeElement === t) ? 'LANDED' : 'NO'; })()" 2>/dev/null | tail -1 | tr -d '"')
  if [ "$L" = "LANDED" ]; then LANDED="YES(after $i presses)"; break; fi
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.4
done
echo "walk: $LANDED"
FOCUSED_X="(async () => {
  const x = $X_FINDER;
  if (!x) return 'NO X';
  const cs = getComputedStyle(x);
  return JSON.stringify({focused: document.activeElement === x, fv: x.matches(':focus-visible'), bg: cs.backgroundColor, color: cs.color, outlineStyle: cs.outlineStyle, outlineWidth: cs.outlineWidth, outlineColor: cs.outlineColor, boxShadow: cs.boxShadow.slice(0, 90), opacity: cs.opacity});
})()"
echo "--- X focused:"
agent-browser eval "$FOCUSED_X" 2>/dev/null | tail -1
agent-browser eval "(async () => { document.activeElement.blur(); return 'blurred'; })()" >/dev/null 2>&1
sleep 1
BLURRED_X="(async () => {
  const x = $X_FINDER;
  if (!x) return 'NO X';
  const cs = getComputedStyle(x);
  return JSON.stringify({restored: {bg: cs.backgroundColor, color: cs.color, outlineStyle: cs.outlineStyle, boxShadow: cs.boxShadow.slice(0, 90)}});
})()"
echo "--- X blurred:"
agent-browser eval "$BLURRED_X" 2>/dev/null | tail -1
echo "=== survey v135 reference side done ==="
