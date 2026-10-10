#!/usr/bin/env bash
# v37: clone-side standing checks (31st) + the session-76 suggested surfaces:
#   A) the filter Select triggers' focus-visible family (the ring contract)
#   B) the search input's focus + typing contract (match / no-match / cleared)
#   C) the /expenses payment-method filter (the third Select — its dynamic list)
# Runs INSIDE with-server.sh (the :3200 parity server).
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone37"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 3

echo "=== CLONE census (31st) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone37 "$PB/census-v35.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R1 (burger hit) at 390x844 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone37 "$PB/probe-r1-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R2 (sheet opens, nav, closes — the superset) ==="
bash "$PB/run-probe.sh" clone37 "$PB/probe-r2-open-v34.mjs" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" clone37 "$PB/probe-r2-nav-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R3 (active nav on /) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone37 "$PB/probe-r3-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R4 (overflow census) ==="
bash "$PB/run-probe.sh" clone37 "$PB/probe-r4a-v34.mjs" 2>/dev/null | tail -1
agent-browser set viewport 1280 800 >/dev/null 2>&1

echo ""
echo "=== SURFACE A: filter trigger rest + focus-visible family (/income) ==="
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3
agent-browser eval "(() => {
  const t = document.querySelector('button[role=combobox]');
  if (!t) return 'NO TRIGGER';
  const cs = getComputedStyle(t);
  return JSON.stringify({ text: t.textContent.trim().slice(0,20), w: t.offsetWidth, h: t.offsetHeight, borderColor: cs.borderColor, boxShadow: cs.boxShadow, bg: cs.backgroundColor });
})()" 2>/dev/null | tail -1

# REAL Tab walk to the trigger (5 nav + Add + search = 7, then 1 more = combobox)
agent-browser eval "(() => { document.activeElement?.blur?.(); return 'ok'; })()" >/dev/null 2>&1
sleep 1
for i in 1 2 3 4 5 6 7 8; do agent-browser press Tab >/dev/null 2>&1; sleep 0.6; done
agent-browser eval "(() => {
  const a = document.activeElement;
  if (!a) return 'NONE';
  const cs = getComputedStyle(a);
  return JSON.stringify({ tag: a.tagName, role: a.getAttribute('role'), text: (a.textContent||'').trim().slice(0,20), fv: a.matches(':focus-visible'), boxShadow: cs.boxShadow, borderColor: cs.borderColor });
})()" 2>/dev/null | tail -1

echo ""
echo "=== SURFACE B: search input focus family (Shift+Tab onto it) ==="
agent-browser press Shift+Tab >/dev/null 2>&1
sleep 0.8
agent-browser eval "(() => {
  const a = document.activeElement;
  if (!a) return 'NONE';
  const cs = getComputedStyle(a);
  return JSON.stringify({ tag: a.tagName, ph: a.getAttribute('placeholder'), w: a.offsetWidth, h: a.offsetHeight, fv: a.matches(':focus-visible'), boxShadow: cs.boxShadow, borderColor: cs.borderColor, borderWidth: cs.borderWidth, bg: cs.backgroundColor });
})()" 2>/dev/null | tail -1

echo ""
echo "=== SURFACE B: typing contract (real keys — match / no-match / cleared) ==="
agent-browser keyboard type "Salary" >/dev/null 2>&1
sleep 1.5
agent-browser eval "(() => {
  const main = document.querySelector('main');
  return JSON.stringify({ val: document.activeElement?.value, cards: [...main.querySelectorAll('h4')].map(h => h.textContent.trim()), header: main.innerText.split('\n').slice(0,4).join(' | ') });
})()" 2>/dev/null | tail -1
agent-browser keyboard type "zzz" >/dev/null 2>&1
sleep 1.5
agent-browser eval "(() => {
  const main = document.querySelector('main');
  return JSON.stringify({ val: document.activeElement?.value, cards: [...main.querySelectorAll('h4')].map(h => h.textContent.trim()), empty: main.querySelector('h3')?.textContent?.trim() });
})()" 2>/dev/null | tail -1
# clear via native setter + input event (React onChange — the same discipline as the reference probe)
agent-browser eval "(async () => {
  const el = document.activeElement;
  Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, '');
  el.dispatchEvent(new Event('input', { bubbles: true }));
  return 'cleared';
})()" >/dev/null 2>&1
sleep 1.5
agent-browser eval "(() => {
  const main = document.querySelector('main');
  return JSON.stringify({ val: document.activeElement?.value, cards: [...main.querySelectorAll('h4')].map(h => h.textContent.trim()) });
})()" 2>/dev/null | tail -1

echo ""
echo "=== SURFACE C: /expenses — the 3 comboboxes + card titles ==="
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(() => {
  const combos = [...document.querySelectorAll('button[role=combobox]')];
  return JSON.stringify({
    searchPh: document.querySelector('input[placeholder*=Search i]')?.getAttribute('placeholder'),
    combos: combos.map(c => ({ text: c.textContent.trim().slice(0,22), w: c.offsetWidth, h: c.offsetHeight, ariaLabel: c.getAttribute('aria-label') })),
    cardTitles: [...document.querySelectorAll('main h4')].map(h => h.textContent.trim())
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== SURFACE C: payment-method filter open (the dynamic option list) ==="
agent-browser eval "(async () => {
  const combos = [...document.querySelectorAll('button[role=combobox]')];
  const pm = combos[2];
  if (!pm) return 'NO PM TRIGGER';
  pm.click();
  return 'clicked: ' + pm.textContent.trim();
})()" 2>/dev/null | tail -1
sleep 1.5
agent-browser eval "(() => {
  const opts = [...document.querySelectorAll('[role=listbox] [role=option]')];
  const read = (o) => ({ t: o.textContent.trim().slice(0,16), sel: o.getAttribute('aria-selected'), hl: o.getAttribute('data-highlighted') });
  return JSON.stringify({ open: !!document.querySelector('[role=listbox]'), opts: opts.map(read) });
})()" 2>/dev/null | tail -1

echo ""
echo "=== SURFACE C: select 'Credit Card' → filter + header update ==="
agent-browser eval "(async () => {
  const opts = [...document.querySelectorAll('[role=listbox] [role=option]')];
  const cc = opts.find(o => o.textContent.trim() === 'Credit Card');
  if (!cc) return 'NO CC OPTION';
  cc.click();
  return 'selected';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(() => {
  const main = document.querySelector('main');
  const combos = [...document.querySelectorAll('button[role=combobox]')];
  return JSON.stringify({
    triggerText: combos[2]?.textContent.trim(),
    cards: [...main.querySelectorAll('h4')].map(h => h.textContent.trim()),
    header: main.innerText.split('\n').slice(0,4).join(' | ')
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== restore: reset the payment filter to All ==="
agent-browser eval "(async () => {
  const combos = [...document.querySelectorAll('button[role=combobox]')];
  const pm = combos[2];
  pm.click();
  return 'reopened';
})()" >/dev/null 2>&1
sleep 1.2
agent-browser eval "(async () => {
  const opts = [...document.querySelectorAll('[role=listbox] [role=option]')];
  const all = opts.find(o => o.textContent.trim().startsWith('All'));
  if (all) all.click();
  return 'reset';
})()" >/dev/null 2>&1
sleep 1.5
agent-browser eval "(() => {
  const combos = [...document.querySelectorAll('button[role=combobox]')];
  return JSON.stringify({ triggerText: combos[2]?.textContent.trim(), cards: [...document.querySelectorAll('main h4')].map(h => h.textContent.trim()).length });
})()" 2>/dev/null | tail -1
