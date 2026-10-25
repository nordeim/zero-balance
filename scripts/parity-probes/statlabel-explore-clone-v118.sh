#!/usr/bin/env bash
# statlabel-explore-clone-v118.sh — the CLONE half of the stat-card label
# exploration (the v118 NEW flag arbitration: the reference's labels read
# 'Total Income'/'Total Savings'/'Total Expenses' — the VLM's 'Total
# Expense' singular claim a misread; this half confirms the clone's label
# family byte-identical). READ-ONLY. Runs inside with-server on :3200.
set -u
cd "$(dirname "$0")/../.."

EXPLORE_JS="(() => {
  const hits = [...document.querySelectorAll('main p, main span, main h1, main h2, main h3, main h4')].filter(el => {
    const t = (el.textContent || '').trim();
    return /^Total/.test(t) && t.length < 30 && el.children.length === 0;
  });
  return JSON.stringify(hits.map(el => {
    const cs = getComputedStyle(el);
    let p = el;
    for (let i = 0; i < 6 && p.parentElement; i++) {
      p = p.parentElement;
      const pc = getComputedStyle(p);
      const pr = p.getBoundingClientRect();
      if (pc.borderRadius !== '0px' && pr.width > 100 && pr.width < 600 && pr.height > 50 && pr.height < 250) break;
    }
    const pr = p.getBoundingClientRect();
    const pc = getComputedStyle(p);
    return {
      text: (el.textContent || '').trim(),
      tag: el.tagName,
      fs: cs.fontSize,
      fw: cs.fontWeight,
      color: cs.color,
      cardTag: p.tagName,
      cardW: Math.round(pr.width),
      cardH: Math.round(pr.height),
      cardPad: pc.padding,
      cardRadius: pc.borderRadius,
      cardBg: pc.backgroundColor,
    };
  }));
})()"

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonestat118b"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
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
echo "--- stat label explore (clone):"
agent-browser eval "(() => {
  const hits = [...document.querySelectorAll('main p, main span, main h1, main h2, main h3, main h4')].filter(el => {
    const t = (el.textContent || '').trim();
    return /^Total/.test(t) && t.length < 30 && el.children.length === 0;
  });
  return JSON.stringify(hits.map(el => {
    const cs = getComputedStyle(el);
    let p = el;
    for (let i = 0; i < 6 && p.parentElement; i++) {
      p = p.parentElement;
      const pc = getComputedStyle(p);
      const pr = p.getBoundingClientRect();
      if (pc.borderRadius !== '0px' && pr.width > 100 && pr.width < 600 && pr.height > 50 && pr.height < 250) break;
    }
    const pr = p.getBoundingClientRect();
    const pc = getComputedStyle(p);
    return {
      text: (el.textContent || '').trim(),
      tag: el.tagName,
      fs: cs.fontSize,
      fw: cs.fontWeight,
      color: cs.color,
      cardTag: p.tagName,
      cardW: Math.round(pr.width),
      cardH: Math.round(pr.height),
      cardPad: pc.padding,
      cardRadius: pc.borderRadius,
      cardBg: pc.backgroundColor,
    };
  }));
})()" 2>/dev/null | tail -1
echo "=== clone explore done ==="
EOF
