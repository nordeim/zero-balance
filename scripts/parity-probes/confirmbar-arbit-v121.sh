#!/usr/bin/env bash
# confirmbar-arbit-v121.sh — the ONE-SHOT clone census for the v121
# candidate pin family: the ITEM-CARD's inline confirm bar (the income/
# savings cards' "Delete this item?" bar) at 1280x800 on /income — the
# never-pinned twin of the pinned confirm-bar family (the v46 F3 pin
# holds the /networth instances; the item-card instance held by NO spec).
# The CLONE-ONLY form (the v46 F3 adapted precedent): the reference has NO
# confirm bars at all (its card-menu Delete destroys immediately — its R6
# bug), so no both-sides census is possible; the pin locks the clone's
# own superset chrome. The family chrome = the v46 F3 contract BY
# CONSTRUCTION (the identical class strings: item-card.tsx:210 vs
# net-worth-view.tsx:124/235); the item-card-only axes: the label text
# "Delete this item?", the bar's width as the card content-width
# consequence (269 = the pinned 309 - the 40 p-5), the bar's junction
# below the footer.
# The interaction: the full PointerEvent/MouseEvent sequence (the v120
# RADIX TAB-SWITCH lesson: Radix activates on pointerdown, the bare
# el.click() is ignored) — the kebab opens the menu, the Delete menuitem
# renders the bar. The FIXTURE-RESTORE discipline: Cancel dismisses the
# bar — the delete NEVER fires (the v46 F3 form).
# READ-ONLY against the data (no API writes fired).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS="(async () => {
  const out = { url: location.pathname };
  // the seeded Salary card (the first income card)
  const card = [...document.querySelectorAll('main div')].find(d => {
    if (typeof d.className !== 'string') return false;
    return d.className.includes('group cursor-pointer rounded-xl') && /Salary/.test(d.textContent || '');
  });
  if (!card) { out.cardFound = false; return JSON.stringify(out); }
  const cr = card.getBoundingClientRect();
  out.cardAtRest = { w: Math.round(cr.width), h: Math.round(cr.height) };
  // the kebab trigger (aria-label 'Actions for Salary')
  const kebab = card.querySelector('button[aria-label^=Actions]');
  if (!kebab) { out.kebabFound = false; return JSON.stringify(out); }
  // the full pointer sequence (the Radix activation form)
  const fire = (el) => {
    const r = el.getBoundingClientRect();
    const opts = { bubbles: true, cancelable: true, view: window, clientX: r.x + r.width / 2, clientY: r.y + r.height / 2, pointerId: 1, pointerType: 'mouse', isPrimary: true, button: 0 };
    el.dispatchEvent(new PointerEvent('pointerdown', opts));
    el.dispatchEvent(new MouseEvent('mousedown', opts));
    el.dispatchEvent(new PointerEvent('pointerup', opts));
    el.dispatchEvent(new MouseEvent('mouseup', opts));
    el.dispatchEvent(new MouseEvent('click', opts));
  };
  fire(kebab);
  await new Promise(r => setTimeout(r, 400));
  // the Delete menuitem
  const delItem = [...document.querySelectorAll('[role=menuitem]')].find(m => (m.textContent || '').trim() === 'Delete');
  if (!delItem) { out.menuFound = false; return JSON.stringify(out); }
  fire(delItem);
  await new Promise(r => setTimeout(r, 400));
  // the confirm bar (the v46 F3 finder family: the bg + the Cancel/Delete pair)
  const bar = [...document.querySelectorAll('div')].find(d => {
    const bcs = getComputedStyle(d);
    if (bcs.backgroundColor !== 'rgb(254, 242, 242)') return false;
    const btns = [...d.querySelectorAll('button')];
    return btns.length === 2 && (btns[0].textContent || '').trim() === 'Cancel' && (btns[1].textContent || '').trim() === 'Delete';
  });
  if (!bar) { out.barFound = false; return JSON.stringify(out); }
  const bcs = getComputedStyle(bar);
  const br = bar.getBoundingClientRect();
  out.bar = {
    mt: bcs.marginTop,
    display: bcs.display,
    align: bcs.alignItems,
    justify: bcs.justifyContent,
    radius: bcs.borderRadius,
    pad: bcs.padding,
    bg: bcs.backgroundColor,
    w: Math.round(br.width),
    h: Math.round(br.height),
  };
  const label = bar.querySelector('p');
  if (label) {
    const lcs = getComputedStyle(label);
    out.label = { fs: lcs.fontSize, fw: lcs.fontWeight, color: lcs.color, text: (label.textContent || '').trim() };
  }
  const cancel = [...bar.querySelectorAll('button')].find(b => (b.textContent || '').trim() === 'Cancel');
  const del = [...bar.querySelectorAll('button')].find(b => (b.textContent || '').trim() === 'Delete');
  if (cancel) {
    const ccs = getComputedStyle(cancel);
    out.cancelPill = {
      bg: ccs.backgroundColor,
      pad: ccs.padding,
      radius: ccs.borderRadius,
      fs: ccs.fontSize,
      fw: ccs.fontWeight,
      color: ccs.color,
      boxShadow: ccs.boxShadow,
      h: Math.round(cancel.getBoundingClientRect().height),
    };
  }
  if (del) {
    const dcs = getComputedStyle(del);
    out.deleteBtn = {
      bg: dcs.backgroundColor,
      color: dcs.color,
      pad: dcs.padding,
      radius: dcs.borderRadius,
      fs: dcs.fontSize,
      fw: dcs.fontWeight,
      h: Math.round(del.getBoundingClientRect().height),
    };
  }
  // the junction: the bar's top vs the card's open-height
  const cr2 = card.getBoundingClientRect();
  out.cardWithBar = { w: Math.round(cr2.width), h: Math.round(cr2.height) };
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

CANCEL_JS="(async () => {
  const bar = [...document.querySelectorAll('div')].find(d => {
    const bcs = getComputedStyle(d);
    if (bcs.backgroundColor !== 'rgb(254, 242, 242)') return false;
    const btns = [...d.querySelectorAll('button')];
    return btns.length === 2 && (btns[0].textContent || '').trim() === 'Cancel';
  });
  if (!bar) return JSON.stringify({ barStillUp: false });
  const cancel = [...bar.querySelectorAll('button')].find(b => (b.textContent || '').trim() === 'Cancel');
  if (cancel) {
    const r = cancel.getBoundingClientRect();
    const opts = { bubbles: true, cancelable: true, view: window, clientX: r.x + r.width / 2, clientY: r.y + r.height / 2, pointerId: 1, pointerType: 'mouse', isPrimary: true, button: 0 };
    cancel.dispatchEvent(new PointerEvent('pointerdown', opts));
    cancel.dispatchEvent(new MouseEvent('mousedown', opts));
    cancel.dispatchEvent(new PointerEvent('pointerup', opts));
    cancel.dispatchEvent(new MouseEvent('mouseup', opts));
    cancel.dispatchEvent(new MouseEvent('click', opts));
  }
  await new Promise(r => setTimeout(r, 300));
  const gone = ![...document.querySelectorAll('div')].some(d => {
    const bcs = getComputedStyle(d);
    return bcs.backgroundColor === 'rgb(254, 242, 242)' && /Delete this item/.test(d.textContent || '');
  });
  const card = [...document.querySelectorAll('main div')].find(d => {
    if (typeof d.className !== 'string') return false;
    return d.className.includes('group cursor-pointer rounded-xl') && /Salary/.test(d.textContent || '');
  });
  const cr = card ? card.getBoundingClientRect() : null;
  return JSON.stringify({ barDismissed: gone, cardRestoredH: cr ? Math.round(cr.height) : null });
})()"

bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonebar121"
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
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- confirm-bar census:"
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- fixture-restore (Cancel):"
agent-browser eval "$CANCEL_JS" 2>/dev/null | tail -1
EOF

echo "=== confirmbar arbit v121 done ==="
