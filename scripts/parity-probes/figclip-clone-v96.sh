#!/usr/bin/env bash
# figclip-clone-v96.sh — the supplemental one-shot census arbitrating the
# v96 cycle's NEW VLM flag: the net FIGURE "-$245,950.00" claimed
# "clipped/truncated on the left side" on the clone's networth summary
# card at 390x844. Measures the figure element's text geometry + overflow
# on the CLONE side (the reference's own figure is "$25,000.00" — its
# own data class; the flag concerns the clone's rendering of ITS figure).
# READ-ONLY. The v87/v88/v89/v90 one-shot precedent.
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="figclip96"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== CLONE net-FIGURE clip arbitration at 390 ==="
agent-browser eval "(async () => {
  // the gradient summary card (same finder as NW_CENSUS)
  const cards = [...document.querySelectorAll('main div, div')].filter(d => {
    const s = getComputedStyle(d);
    return d.getBoundingClientRect().height > 100 && d.getBoundingClientRect().width > 200
      && s.backgroundImage && s.backgroundImage.includes('linear-gradient');
  });
  const card = cards.find(c => c.getBoundingClientRect().width < 500) || cards[0];
  if (!card) return 'no summary card found';
  const cr = card.getBoundingClientRect();
  const cs = getComputedStyle(card);
  // the figure: the largest-font text child inside the card
  let fig = null; let figFs = 0;
  for (const el of card.querySelectorAll('h1,h2,h3,p,span,div')) {
    const s = getComputedStyle(el);
    const fs = parseFloat(s.fontSize);
    const t = (el.textContent || '').trim();
    if (!t || t.length > 40) continue;
    if (/^[-−]?\s*\\\$/.test(t) && fs > figFs) { fig = el; figFs = fs; }
  }
  if (!fig) return 'no figure found';
  const fr = fig.getBoundingClientRect();
  const fs2 = getComputedStyle(fig);
  // the card's content box (padding-aware)
  const padL = parseFloat(cs.paddingLeft); const padR = parseFloat(cs.paddingRight);
  const contentL = cr.left + padL; const contentR = cr.right - padR;
  // the figure's own text overflow state
  const range = document.createRange();
  range.selectNodeContents(fig);
  const tr = range.getBoundingClientRect();
  return JSON.stringify({
    figureText: (fig.textContent || '').trim(),
    figureEl: { tag: fig.tagName, x: Math.round(fr.x), y: Math.round(fr.y), w: Math.round(fr.width), h: Math.round(fr.height) },
    textRect: { x: Math.round(tr.x), w: Math.round(tr.width) },
    font: { fs: fs2.fontSize, fw: fs2.fontWeight, ls: fs2.letterSpacing },
    cardBox: { x: Math.round(cr.x), w: Math.round(cr.width), padL: padL, padR: padR, contentL: Math.round(contentL), contentR: Math.round(contentR) },
    clipArbitration: {
      textLeftOfContent: Math.round(contentL - tr.x),
      textRightOfContent: Math.round(tr.right - contentR),
      textWiderThanBox: Math.round(tr.width - fr.width),
      figureScrolls: fig.scrollWidth > fig.clientWidth,
      docSW: document.documentElement.scrollWidth
    }
  });
})()" 2>/dev/null | tail -1
EOF
echo "=== figclip clone v96 done ==="
