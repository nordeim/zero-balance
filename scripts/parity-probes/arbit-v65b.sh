#!/usr/bin/env bash
# arbit-v65b.sh — the follow-up census for the two arbit-v65.sh items the
# first pass left open: (1) the clone-side AVATAR finder (the clone's
# avatar uses rounded-[9999px], not rounded-full — the v65 pass caught the
# sidebar wrapper instead) — the chrome must be byte-identical to the
# reference's 36x36 / radius 9999px / 14px-600 white; the bg + initial
# are the user-identity class; (2) the Add button's FULL computed shadow
# string on both sides (the v65 pass truncated at 80 chars — the
# multi-layer comparison rule requires the FULL string).
# Census BOTH sides at 1280x800. READ-ONLY.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const out = {};
  // the avatar: a small round element near the sidebar bottom with 1-2
  // text chars inside (works for rounded-full AND rounded-[9999px])
  const cands = [...document.querySelectorAll('div,span')].filter((el) => {
    const r = el.getBoundingClientRect();
    if (r.width < 24 || r.width > 56 || Math.abs(r.width - r.height) > 2) return false;
    const cs = getComputedStyle(el);
    if (parseInt(cs.borderRadius) < 100) return false;
    const t = (el.textContent || '').trim();
    return t.length >= 1 && t.length <= 2 && r.top > 600;
  });
  if (cands.length) {
    const av = cands[0];
    const acs = getComputedStyle(av);
    const ar = av.getBoundingClientRect();
    out.avatar = {
      w: Math.round(ar.width),
      h: Math.round(ar.height),
      radius: acs.borderRadius,
      fs: acs.fontSize,
      fw: acs.fontWeight,
      color: acs.color,
      bg: acs.backgroundColor,
      text: (av.textContent || '').trim().slice(0, 2),
    };
  }
  // the Add button: FULL shadow + geometry
  const btn = [...document.querySelectorAll('button')].find(
    (b) => (b.textContent || '').includes('Add') && b.getBoundingClientRect().width > 0,
  );
  if (btn) {
    const btcs = getComputedStyle(btn);
    out.addButton = {
      text: (btn.textContent || '').trim().slice(0, 20),
      w: Math.round(btn.getBoundingClientRect().width),
      h: Math.round(btn.getBoundingClientRect().height),
      shadowFULL: btcs.boxShadow,
    };
  }
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280, savings) ==="
export AGENT_BROWSER_SESSION="refarbv65b"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
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
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, savings) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbv65b"
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
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== arbit v65b done ==="
