#!/usr/bin/env bash
# arbit-v70b.sh — the follow-up census for the two arbit-v70.sh items the
# first pass left open: (1) the clone-side AVATAR finder (the clone's
# avatar uses rounded-[9999px], not rounded-full — the v70 pass caught the
# sidebar brand block instead; the v65b finder pattern) — the chrome must
# be byte-identical to the reference's 36x36 / radius 9999px / 14px-600
# white; the bg + initial are the user-identity class; (2) the CARD
# INTERNALS decomposition — the income pair's first-card heights measured
# ref 200 vs clone 230 with IDENTICAL badge rows (h 22) and footers (h 16),
# so the 30px delta lives in the title/subcategory/amount blocks: census
# EVERY card's internal blocks (title text, subcategory text + height, the
# amount h + mb, the badge row h + count, the footer h) so the delta
# decomposes arithmetic-wise. Census BOTH sides at 1280x800. READ-ONLY.
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
  // the item grid: EVERY card's internals decomposed
  const grid = [...document.querySelectorAll('div')].find(
    (d) => typeof d.className === 'string' && d.className.includes('grid-cols-3'),
  );
  if (grid) {
    out.cards = [...grid.children].map((card) => {
      const ccs = getComputedStyle(card);
      const kids = [...card.children].filter((k) => getComputedStyle(k).position !== 'absolute');
      const titleBlock = kids[0];
      const amountBlock = kids.find((k) => {
        const p = k.querySelector('p');
        return p && getComputedStyle(p).fontSize === '24px';
      });
      const badgeRow = kids.find(
        (c) => typeof c.className === 'string' && /flex-wrap/.test(c.className),
      );
      const footer = kids[kids.length - 1];
      const h4 = titleBlock ? titleBlock.querySelector('h4') : null;
      const sub = titleBlock ? titleBlock.querySelector('p') : null;
      const amt = amountBlock ? amountBlock.querySelector('p') : null;
      const read = (el) => {
        if (!el) return null;
        const cs = getComputedStyle(el);
        return {
          h: Math.round(el.getBoundingClientRect().height),
          fs: cs.fontSize,
          text: (el.textContent || '').trim().slice(0, 24),
        };
      };
      return {
        cardH: Math.round(card.getBoundingClientRect().height),
        cardW: Math.round(card.getBoundingClientRect().width),
        pad: ccs.padding,
        title: read(h4),
        sub: sub
          ? Object.assign(read(sub), {
              mb: getComputedStyle(titleBlock).marginBottom,
            })
          : null,
        titleBlockH: titleBlock ? Math.round(titleBlock.getBoundingClientRect().height) : null,
        titleBlockMb: titleBlock ? getComputedStyle(titleBlock).marginBottom : null,
        amount: read(amt),
        amountBlockMb: amountBlock ? getComputedStyle(amountBlock).marginBottom : null,
        badgeRow: badgeRow
          ? {
              h: Math.round(badgeRow.getBoundingClientRect().height),
              count: badgeRow.children.length,
              texts: [...badgeRow.children].map((b) => (b.textContent || '').trim()),
              mb: getComputedStyle(badgeRow).marginBottom,
            }
          : null,
        footer: footer
          ? {
              h: Math.round(footer.getBoundingClientRect().height),
              count: footer.children.length,
            }
          : null,
      };
    });
  }
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="refarbv70b"
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
echo "--- ref income ---"
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- ref expenses ---"
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbv70b"
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
echo "--- clone income ---"
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- clone expenses ---"
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== arbit v70b done ==="
