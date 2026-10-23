#!/usr/bin/env bash
# qarow-arbit-v107.sh — the ONE-SHOT both-sides probe of the quick-action
# card's INTERIOR FLEX-ROW family (never pinned: the v61 F3 pin holds the
# card/tile/icon/label/plus BOX chrome ONLY — the row's own flex/gap-12
# centering, the tile's flex centering, the icon's centering offsets, and
# the label's 40+12 junction arithmetic were never pinned at ANY viewport
# in ANY spec; the v45 F3b pin covers the hover shadow only).
# THE STRUCTURAL-FINDER LESSON (the v107 DIV-vs-SPAN finding): the
# reference's row/tile are DIVs while the clone's are SPANs — identical
# computed chrome, different tags — so every finder walks POSITIONALLY
# (firstElementChild children order), never by tag. The label leaf finder
# is TAG-AGNOSTIC (the v61 leaf lesson generalized: exact text + zero
# element children, any tag).
# Run on BOTH sides to verify the family is byte-identical before the pin.
# READ-ONLY: login + passive navigation only (the v46 rule). The parked
# pointer at (5,5). No literal dollar sequences in the census JS (the v64
# rule). Double-quoted-heredoc-safe.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

QAROW_JS="(async () => {
  const qas = [...document.querySelectorAll('button')].filter((b) =>
    /^Add (Income|Savings|Expense)\$/.test((b.textContent || '').trim()));
  if (qas.length !== 3) return JSON.stringify({ err: 'no quick-action buttons', n: qas.length });
  const cards = qas.map((b) => {
    // STRUCTURAL walk: the row is the button's FIRST ELEMENT CHILD —
    // a span on the clone, a div on the reference (the computed-chrome
    // class); never a tag match.
    const row = b.firstElementChild;
    if (!row) return { err: 'no row' };
    const rcs = getComputedStyle(row);
    const rr = row.getBoundingClientRect();
    const tile = row.firstElementChild;
    const tcs = tile ? getComputedStyle(tile) : null;
    const tr = tile ? tile.getBoundingClientRect() : null;
    const svgs = [...row.querySelectorAll('svg')];
    const icon = svgs[0];
    const ir = icon ? icon.getBoundingClientRect() : null;
    const plus = svgs[svgs.length - 1];
    const pr = plus ? plus.getBoundingClientRect() : null;
    // THE TAG-AGNOSTIC LEAF LABEL (the v61 lesson generalized): exact
    // text + zero element children — any tag.
    const label = [...row.querySelectorAll('*')].find((e) =>
      /^Add (Income|Savings|Expense)\$/.test((e.textContent || '').trim()) && e.children.length === 0);
    const lr = label ? label.getBoundingClientRect() : null;
    const lcs = label ? getComputedStyle(label) : null;
    return {
      text: (b.textContent || '').trim(),
      row: {
        display: rcs.display, align: rcs.alignItems, gap: rcs.gap,
        h: Math.round(rr.height), w: Math.round(rr.width),
        childCount: row.children.length,
      },
      tile: tcs ? {
        display: tcs.display, align: tcs.alignItems, justify: tcs.justifyContent,
        w: Math.round(tr.width), h: Math.round(tr.height), radius: tcs.borderRadius,
      } : null,
      icon: ir ? {
        w: Math.round(ir.width), h: Math.round(ir.height),
        offX: Math.round(ir.x - tr.x), offY: Math.round(ir.y - tr.y),
        color: getComputedStyle(icon).color,
      } : null,
      label: lr ? {
        xInRow: Math.round(lr.x - rr.x), fs: lcs.fontSize, fw: lcs.fontWeight,
        color: lcs.color,
      } : null,
      plus: pr ? {
        w: Math.round(pr.width), h: Math.round(pr.height),
        xInRow: Math.round(pr.x - rr.x), opacity: getComputedStyle(plus).opacity,
      } : null,
    };
  });
  return JSON.stringify({ cards: cards, sw: document.documentElement.scrollWidth });
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="refqarow107"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
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
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$QAROW_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280) ==="
cd "$(dirname "$0")/../.."
QAROW_JS="$QAROW_JS" bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="cloneqarow107"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "\$QAROW_JS" 2>/dev/null | tail -1
EOF
echo "=== qarow probe v107 done ==="
