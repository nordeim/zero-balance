#!/usr/bin/env bash
# menu-clone-v98.sh — the CLONE half of the supplemental two-half
# census for the v98 pin's axes (the goal-card action-menu PANEL +
# menuitem-resting interior at 1280, the savings view's ellipsis menu).
# READ-ONLY. THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START.
# Runs inside with-server.sh (the :3200 parity server).
set -u
cd "$(dirname "$0")/../.."

MENU_JS="(async () => {
  const trig = [...document.querySelectorAll('button')].find(b => {
    const r = b.getBoundingClientRect();
    return !(b.textContent || '').trim() && b.querySelector('svg') &&
           Math.round(r.width) === 36 && Math.round(r.height) === 36;
  });
  if (!trig) return JSON.stringify({ err: 'no trigger' });
  const trigW = Math.round(trig.getBoundingClientRect().width);
  const r0 = trig.getBoundingClientRect();
  const cx = r0.x + r0.width/2, cy = r0.y + r0.height/2;
  const opts = { bubbles: true, cancelable: true, clientX: cx, clientY: cy, button: 0 };
  trig.dispatchEvent(new PointerEvent('pointerdown', { ...opts, pointerId: 1, pointerType: 'mouse' }));
  trig.dispatchEvent(new MouseEvent('mousedown', opts));
  trig.dispatchEvent(new PointerEvent('pointerup', { ...opts, pointerId: 1, pointerType: 'mouse' }));
  trig.dispatchEvent(new MouseEvent('mouseup', opts));
  trig.dispatchEvent(new MouseEvent('click', opts));
  await new Promise(r => setTimeout(r, 700));
  const menu = document.querySelector('[role=menu]');
  if (!menu) return JSON.stringify({ err: 'no menu' });
  const cs = getComputedStyle(menu);
  const r = menu.getBoundingClientRect();
  const item = menu.querySelector('[role=menuitem]');
  const ics = item ? getComputedStyle(item) : null;
  const ir = item ? item.getBoundingClientRect() : null;
  return JSON.stringify({
    panel: {
      bg: cs.backgroundColor, radius: cs.borderRadius,
      border: cs.borderWidth + ' ' + cs.borderColor,
      shadow: cs.boxShadow, minW: cs.minWidth,
      overflow: cs.overflow, z: cs.zIndex, pos: cs.position,
      w: Math.round(r.width), h: Math.round(r.height)
    },
    item0: ics ? {
      fs: ics.fontSize, fw: ics.fontWeight, color: ics.color,
      pad: ics.padding, radius: ics.borderRadius, lh: ics.lineHeight,
      h: ir ? Math.round(ir.height) : null
    } : null,
    itemCount: menu.querySelectorAll('[role=menuitem]').length,
    trigW,
    docSW: document.documentElement.scrollWidth
  });
})()"

MENU_JS="$MENU_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonemenuarbit98"
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
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 5
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$MENU_JS" 2>/dev/null | tail -1
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== clone menu arbit v98 half done ==="
