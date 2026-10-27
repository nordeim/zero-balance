#!/usr/bin/env bash
# kebabopen-arbit-v124.sh — the ONE-SHOT clone census for the v124
# candidate pin family: the NETWORTH asset-card kebab trigger's OPEN-MENU
# state at 1280x800 on /networth — the never-pinned PATH of the pinned
# reveal family ON THE NETWORTH SURFACE (the v46 F2 pin holds the
# networth kebab's AT-REST opacity-0 + the REAL-HOVER group-hover reveal;
# the v36 S3 pin the KEYBOARD focus-visible reveal; the v122 pin the
# OPEN-path reveal on the SAVINGS item-card — a DIFFERENT FILE whose
# pin-sanity mutation left these networth twins green, the different-file
# immunity proven live in the v122 cycle — so the OPEN-path
# data-[state=open]:opacity-100 reveal on net-worth-view.tsx:82/192,
# superset fix #7's "stays revealed while its menu is open" clause, is
# held by NO spec).
# The CLONE-ONLY form (the v46 F3 adapted precedent + the v122 twin):
# the reference's trigger stays INVISIBLE (opacity 0) when its menu is
# opened (its own superset-#7 bug — documented in AGENTS.md), and a
# reference-side measurement would require a CLICK (the v46 read-only
# rule: passive navigation + real pointer hover only, and the net-worth
# kebab flow is NEVER safe to probe past the menu open — the menu's
# Delete click IS the delete) — so no both-sides census is possible;
# the pin locks the clone's own superset chrome. The family chrome =
# the v122 pinned contract BY CONSTRUCTION (the identical class string:
# net-worth-view.tsx:82/192 ↔ item-card.tsx:139); the never-pinned
# axis: the open+parked opacity "1" (the pointer OFF the card, the
# group-hover disengaged, the data-[state=open] token alone holding
# the reveal).
# The census walks the FULL reveal ladder for context: at-rest 0 (the
# v45/v46 contract) -> hover 1 (the v46 contract) -> open+parked 1
# (THE AXIS) -> after-dismiss (the dismissed state only). The hover
# step moves the REAL pointer to the card's OWN center (the coords
# read live first — never guessed); the open step's synthetic pointer
# sequence does NOT move the real pointer (the parked-at-(5,5) state
# holds through the open read — the group-hover disengaged, the
# data-[state=open] token alone on trial).
# The interaction: the full PointerEvent/MouseEvent sequence (the v120
# RADIX lesson: Radix activates on pointerdown, the bare el.click() is
# ignored) — the kebab opens the menu. The FIXTURE-RESTORE discipline:
# the outside pointerdown dismisses the menu — NO menuitem is ever
# clicked, the data is never touched (READ-ONLY against the data).
set -u
cd "$(dirname "$0")/../.."

CENTER_JS="(async () => {
  // the PLAIN 'x,y' form (the v116 convention — the JSON form's escaped
  // quotes break the shell-side sed extraction; the v116 census returned
  // a bare comma pair for exactly this reason)
  const card = [...document.querySelectorAll('main div')].find(d => {
    if (typeof d.className !== 'string') return false;
    return d.className.includes('group rounded-xl border bg-white p-5') && /Share Portfolio/.test(d.textContent || '');
  });
  if (!card) return '0,0';
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + ',' + Math.round(r.y + r.height / 2);
})()"

HOVER_JS="(async () => {
  // the HOVER-path read (the v46 contract re-verified in the same
  // walk): the real pointer on the card's own center -> group-hover
  // opacity 1.
  const card = [...document.querySelectorAll('main div')].find(d => {
    if (typeof d.className !== 'string') return false;
    return d.className.includes('group rounded-xl border bg-white p-5') && /Share Portfolio/.test(d.textContent || '');
  });
  if (!card) return JSON.stringify({ cardFound: false });
  const kebab = card.querySelector('button[aria-label^=Actions]');
  if (!kebab) return JSON.stringify({ kebabFound: false });
  const cs = getComputedStyle(kebab);
  return JSON.stringify({ hoverOpacity: cs.opacity, dataState: kebab.getAttribute('data-state') });
})()"

CENSUS_JS="(async () => {
  const out = { url: location.pathname, docSW: document.documentElement.scrollWidth };
  // the seeded Share Portfolio asset card (the first networth asset —
  // the v106 settle pattern's own card)
  const card = [...document.querySelectorAll('main div')].find(d => {
    if (typeof d.className !== 'string') return false;
    return d.className.includes('group rounded-xl border bg-white p-5') && /Share Portfolio/.test(d.textContent || '');
  });
  if (!card) { out.cardFound = false; return JSON.stringify(out); }
  const cr = card.getBoundingClientRect();
  out.card = { w: Math.round(cr.width), h: Math.round(cr.height) };
  const kebab = card.querySelector('button[aria-label^=Actions]');
  if (!kebab) { out.kebabFound = false; return JSON.stringify(out); }
  const grab = () => {
    const cs = getComputedStyle(kebab);
    const r = kebab.getBoundingClientRect();
    return {
      tag: kebab.tagName,
      opacity: cs.opacity,
      dataState: kebab.getAttribute('data-state'),
      w: Math.round(r.width),
      h: Math.round(r.height),
      radius: cs.borderRadius,
      bg: cs.backgroundColor,
      color: cs.color,
      cardTop: Math.round(r.top - cr.top),
      cardRight: Math.round(cr.right - r.right),
    };
  };
  // The AT-REST read (the real pointer parked at 5,5 before this eval —
  // the v22 lesson): opacity 0, data-state closed (the v45/v46
  // contract).
  out.atRest = grab();
  // The full pointer sequence (the Radix activation form) OPENS the
  // menu — the SYNTHETIC events do not move the real pointer (it stays
  // parked at 5,5), so the open read below isolates the
  // data-[state=open] token from the group-hover path.
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
  await new Promise(r => setTimeout(r, 500));
  const menu = document.querySelector('[role=menu]');
  out.menuOpen = !!menu;
  out.menuItems = menu ? menu.querySelectorAll('[role=menuitem]').length : 0;
  // THE OPEN+PARKED read: the real pointer still at (5,5) — the
  // group-hover disengaged, the data-[state=open] token alone holding
  // the reveal (the never-pinned superset axis).
  out.openParked = grab();
  return JSON.stringify(out);
})()"

RESTORE_JS="(async () => {
  // The FIXTURE-RESTORE: the outside synthetic pointerdown dismisses the
  // menu (no menuitem ever clicked — the data never touched). The read
  // asserts the DISMISSED state only (menu gone + data-state closed);
  // the trigger's post-restore opacity is deliberately NOT read here:
  // Radix's focus-return after an UNTRUSTED (synthetic) pointerdown
  // leaves Chromium's focus-visible heuristic in keyboard mode, so the
  // returned focus engages focus-visible:opacity-100 (the v36
  // keyboard-path contract) — a synthetic-world artifact. In the
  // Playwright pin the restore is the REAL Escape press (the v98 form),
  // where the keyboard focus-return legitimately holds the reveal.
  const opts = { bubbles: true, cancelable: true, view: window, clientX: 5, clientY: 5, pointerId: 1, pointerType: 'mouse', isPrimary: true, button: 0 };
  document.body.dispatchEvent(new PointerEvent('pointerdown', opts));
  await new Promise(r => setTimeout(r, 400));
  let menuGone = !document.querySelector('[role=menu]');
  if (!menuGone) {
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true, cancelable: true }));
    await new Promise(r => setTimeout(r, 400));
    menuGone = !document.querySelector('[role=menu]');
  }
  const card = [...document.querySelectorAll('main div')].find(d => {
    if (typeof d.className !== 'string') return false;
    return d.className.includes('group rounded-xl border bg-white p-5') && /Share Portfolio/.test(d.textContent || '');
  });
  const kebab = card ? card.querySelector('button[aria-label^=Actions]') : null;
  return JSON.stringify({
    menuDismissed: menuGone,
    dataState: kebab ? kebab.getAttribute('data-state') : null,
  });
})()"

bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="cloneopen124"
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
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
CENTER=\$(agent-browser eval "$CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')
echo "--- card center: \$CENTER"
CX="\${CENTER%,*}"
CY="\${CENTER#*,}"
echo "--- hover-path read (the real pointer on the card's own center):"
agent-browser mouse move "\$CX" "\$CY" >/dev/null 2>&1
sleep 1
agent-browser eval "$HOVER_JS" 2>/dev/null | tail -1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- open+parked census (the reveal ladder: at-rest -> menu open, the pointer parked):"
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- fixture-restore (the outside pointerdown dismisses the menu):"
agent-browser eval "$RESTORE_JS" 2>/dev/null | tail -1
EOF

echo "=== kebabopen arbit v124 done ==="
