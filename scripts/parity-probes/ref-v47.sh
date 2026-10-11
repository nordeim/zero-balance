#!/usr/bin/env bash
# v47: reference-side driver — the three v47 surfaces, measured live on
# the reference (READ-ONLY: the dialog-open + input-focus steps only;
# the sheet-open + census only; NO Delete clicks anywhere — the v46
# incident rule).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="ref47"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4

echo "=== REF dialog input focus composite at 1280 (Add Item) ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').trim() === 'Add Item'); if (b) { b.click(); return 'clicked'; } return 'not found'; })()" 2>/dev/null | tail -1
sleep 2
# The reference's dialog is a plain fixed inset-0 div (no [role=dialog])
# — focus the first input, census the composition (the probe's own
# finder handles the plain-div dialog via the overlay's inputs).
agent-browser eval "(async () => {
  const overlay = [...document.querySelectorAll('div')].filter(d => getComputedStyle(d).position === 'fixed' && d.innerHTML.includes('Save') && d.getBoundingClientRect().width > 200).pop();
  const input = overlay ? overlay.querySelector('input') : document.querySelector('input[type=number]');
  if (!input) return 'no input';
  const cs = getComputedStyle(input);
  const layerCount = (s) => (s.match(/px, /g) || []).length + 1;
  const rest = { shadow: cs.boxShadow, layers: layerCount(cs.boxShadow), h: cs.height, radius: cs.borderRadius, pad: cs.padding, border: cs.border, bg: cs.backgroundColor, outlineStyle: cs.outlineStyle };
  input.focus({ focusVisible: true });
  await new Promise((r) => setTimeout(r, 100));
  const fcs = getComputedStyle(input);
  const focus = { fv: input.matches(':focus-visible'), shadow: fcs.boxShadow, layers: layerCount(fcs.boxShadow), borderColor: fcs.borderColor, outlineStyle: fcs.outlineStyle };
  return JSON.stringify({ rest, focus });
})()" 2>/dev/null | tail -1
# Close the dialog (Cancel — no data touched).
agent-browser eval "(() => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').trim() === 'Cancel'); if (b) b.click(); return 'closed'; })()" 2>/dev/null | tail -1
sleep 1

echo ""
echo "=== REF net-worth card mobile census at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref47 "$PB/nw-mobcard-v47.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF mobile sheet chrome census at 390 ==="
agent-browser eval "(async () => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('Toggle Sidebar')); if (b) { b.click(); return 'opened'; } return 'no toggle'; })()" 2>/dev/null | tail -1
sleep 2
bash "$PB/run-probe.sh" ref47 "$PB/sheet-chrome-v47.mjs" 2>/dev/null | tail -1
# Close the sheet (read-only).
agent-browser eval "(async () => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('Toggle Sidebar')); if (b) { b.click(); return 'closed'; } return 'no toggle'; })()" 2>/dev/null | tail -1
