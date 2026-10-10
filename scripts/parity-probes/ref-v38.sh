#!/usr/bin/env bash
# v38: reference-side standing checks (32nd) + the new v38 surfaces:
#   A) the /expenses frequency-filter option-list census (the payment-method
#      sibling — never measured live)
#   B) the /savings filter-card instance (the third items-view instance)
#   C) the a11y baseline census (read-only: landmark/label/heading structure
#      facts for the superset story; the deep axe scan runs in
#      a11y-scan-v38.mjs via Playwright)
# Read-only discipline: no clicks that mutate; filter probes Escape-close
# without selecting (or restore the input to "" via the native setter).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="ref38"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'NO FORM — maybe already logged in';
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

echo "=== REF census (32nd) — BEFORE probes ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref38 "$PB/census-v35.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF R1 (burger hit) at 390x844 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref38 "$PB/probe-r1-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF R2 (sheet opens, nav, traps — the reference bug) ==="
bash "$PB/run-probe.sh" ref38 "$PB/probe-r2-open-v34.mjs" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" ref38 "$PB/probe-r2-nav-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF R3 (active nav on /) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref38 "$PB/probe-r3-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF R4 (overflow census) ==="
bash "$PB/run-probe.sh" ref38 "$PB/probe-r4a-v34.mjs" 2>/dev/null | tail -1
agent-browser set viewport 1280 800 >/dev/null 2>&1

echo ""
echo "=== REF SEO pair ==="
agent-browser open "$BASE/robots.txt" >/dev/null 2>&1
sleep 2
agent-browser eval "document.body.innerText.slice(0,300)" 2>/dev/null | tail -1
agent-browser open "$BASE/sitemap.xml" >/dev/null 2>&1
sleep 2
agent-browser eval "document.body.innerText.replace(/\\s+/g,' ').slice(0,600)" 2>/dev/null | tail -1

echo ""
echo "=== SURFACE A: /expenses frequency-filter option census ==="
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
# The frequency trigger is the SECOND combobox (category, frequency, PM).
agent-browser eval "(async () => {
  const sels = [...document.querySelectorAll('button[role=combobox]')];
  if (!sels.length) return 'NO COMBOBOXES';
  const out = sels.map(s => ({ text: s.textContent.trim().slice(0,26), w: s.offsetWidth, h: s.offsetHeight, label: s.getAttribute('aria-label'), ariaLabel: !!s.getAttribute('aria-label') }));
  return JSON.stringify({ count: sels.length, triggers: out });
})()" 2>/dev/null | tail -1
# Open the frequency listbox (second combobox), census its options, Escape.
agent-browser eval "(async () => {
  const sels = [...document.querySelectorAll('button[role=combobox]')];
  if (sels.length < 2) return 'NEED 2 COMBOBOXES';
  sels[1].click();
  await new Promise(r => setTimeout(r, 700));
  const opts = [...document.querySelectorAll('[role=option]')].map(o => ({ text: o.textContent.trim().slice(0,30), sel: o.getAttribute('aria-selected') }));
  return JSON.stringify({ options: opts, count: opts.length });
})()" 2>/dev/null | tail -1
agent-browser press Escape >/dev/null 2>&1
sleep 1
# Frequency round-trip: open, select the first non-All option, read cards+header, reset.
agent-browser eval "(async () => {
  const sels = [...document.querySelectorAll('button[role=combobox]')];
  if (sels.length < 2) return 'NEED 2';
  sels[1].click();
  await new Promise(r => setTimeout(r, 700));
  const opts = [...document.querySelectorAll('[role=option]')];
  const target = opts.find(o => o.getAttribute('aria-selected') !== 'true' && !/^all/i.test(o.textContent.trim()));
  if (!target) return 'NO NON-ALL OPTION';
  const name = target.textContent.trim();
  target.click();
  await new Promise(r => setTimeout(r, 900));
  const cards = [...document.querySelectorAll('main h4')].map(h => h.textContent.trim().slice(0,30));
  const header = (document.querySelector('main p') || {}).textContent || '';
  return JSON.stringify({ picked: name, cards, header: header.trim().slice(0,40) });
})()" 2>/dev/null | tail -1
# Reset to All (the fixture-restore discipline).
agent-browser eval "(async () => {
  const sels = [...document.querySelectorAll('button[role=combobox]')];
  if (sels.length < 2) return 'NEED 2';
  sels[1].click();
  await new Promise(r => setTimeout(r, 700));
  const all = [...document.querySelectorAll('[role=option]')].find(o => /^all/i.test(o.textContent.trim()));
  if (all) all.click();
  await new Promise(r => setTimeout(r, 900));
  const cards = [...document.querySelectorAll('main h4')].map(h => h.textContent.trim().slice(0,30));
  return JSON.stringify({ restored: cards.length + ' cards', cards });
})()" 2>/dev/null | tail -1

echo ""
echo "=== SURFACE B: /savings filter-card instance ==="
agent-browser open "$BASE/savings" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const card = document.querySelector('main .rounded-2xl') || document.querySelector('main [class*=rounded-2xl]');
  if (!card) return 'NO FILTER CARD';
  const cs = card && getComputedStyle(card);
  const input = card.querySelector('input');
  const ics = input ? getComputedStyle(input) : null;
  const sels = [...card.querySelectorAll('button[role=combobox]')];
  return JSON.stringify({
    card: card ? { w: card.offsetWidth, h: card.offsetHeight, bg: cs.backgroundColor, radius: cs.borderRadius, border: cs.borderColor, pad: cs.padding } : null,
    input: input ? { w: input.offsetWidth, h: input.offsetHeight, placeholder: input.placeholder, label: input.getAttribute('aria-label'), border: ics.borderColor, shadow: ics.boxShadow.slice(0,120) } : null,
    combos: sels.map(s => ({ text: s.textContent.trim().slice(0,26), w: s.offsetWidth, h: s.offsetHeight })),
    grid: card.firstElementChild ? getComputedStyle(card.firstElementChild).gridTemplateColumns.slice(0,60) : null,
  });
})()" 2>/dev/null | tail -1
# The savings category-filter round-trip (first combobox) — read-only restore.
agent-browser eval "(async () => {
  const card = document.querySelector('main .rounded-2xl');
  const sels = card ? [...card.querySelectorAll('button[role=combobox]')] : [];
  if (!sels.length) return 'NO COMBOS';
  sels[0].click();
  await new Promise(r => setTimeout(r, 700));
  const opts = [...document.querySelectorAll('[role=option]')].map(o => o.textContent.trim().slice(0,30));
  const nonAll = [...document.querySelectorAll('[role=option]')].find(o => o.getAttribute('aria-selected') !== 'true' && !/^all/i.test(o.textContent.trim()));
  let after = 'none';
  if (nonAll) {
    nonAll.click();
    await new Promise(r => setTimeout(r, 900));
    after = JSON.stringify([...document.querySelectorAll('main h4')].map(h => h.textContent.trim().slice(0,30)));
  }
  return JSON.stringify({ options: opts, picked: nonAll ? nonAll.textContent.trim() : null, cardsAfter: after });
})()" 2>/dev/null | tail -1
# restore
agent-browser eval "(async () => {
  const card = document.querySelector('main .rounded-2xl');
  const sels = card ? [...card.querySelectorAll('button[role=combobox]')] : [];
  if (!sels.length) return 'no restore needed';
  sels[0].click();
  await new Promise(r => setTimeout(r, 700));
  const all = [...document.querySelectorAll('[role=option]')].find(o => /^all/i.test(o.textContent.trim()));
  if (all) all.click();
  await new Promise(r => setTimeout(r, 900));
  return 'restored: ' + document.querySelectorAll('main h4').length + ' cards';
})()" 2>/dev/null | tail -1

echo ""
echo "=== SURFACE C: reference a11y structural census (read-only) ==="
agent-browser eval "(async () => {
  const out = {};
  out.landmarks = [...document.querySelectorAll('main,nav,aside,header,footer,[role=navigation],[role=main]')].map(e => e.tagName.toLowerCase() + (e.getAttribute('role') ? '[role=' + e.getAttribute('role') + ']' : ''));
  out.h1 = document.querySelector('h1') ? document.querySelector('h1').textContent.trim().slice(0,40) : null;
  out.title = document.title;
  // unlabeled icon-only buttons census (button-name rule pre-check)
  out.iconOnlyButtons = [...document.querySelectorAll('button')].filter(b => !b.textContent.trim() && !b.getAttribute('aria-label') && !b.querySelector('.sr-only')).length;
  out.totalButtons = document.querySelectorAll('button').length;
  // unlabeled inputs
  out.unlabeledInputs = [...document.querySelectorAll('input')].filter(i => !i.labels?.length && !i.getAttribute('aria-label') && !i.getAttribute('aria-labelledby') && i.type !== 'hidden').map(i => i.type + ':' + (i.placeholder || ''));
  // images without alt
  out.imgNoAlt = [...document.querySelectorAll('img:not([alt])')].length;
  return JSON.stringify(out);
})()" 2>/dev/null | tail -1

echo ""
echo "=== REF census (32nd) — AFTER probes (read-only discipline) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref38 "$PB/census-v35.mjs" 2>/dev/null | tail -1
