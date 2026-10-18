#!/usr/bin/env bash
# filter-interior-clone-v91.sh — the CLONE half of the v91 pin's
# supplemental one-shot census (the two-half controlled form, the v89
# lesson). The census JS block is byte-identical to the reference half's
# (filter-interior-arbit-v91.sh) — the JS identity IS the contract.
# READ-ONLY (the clone side rides the with-server :3200 parity server).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS="(async () => {
  const out = { url: location.pathname };
  const search = [...document.querySelectorAll('input')].find(
    (i) => i.getBoundingClientRect().width > 100,
  );
  const filterCard = search ? search.closest('div.rounded-2xl') : null;
  if (search && filterCard) {
    const srcs = getComputedStyle(search);
    out.searchTypography = {
      tag: search.tagName,
      type: search.type,
      fs: srcs.fontSize,
      fw: srcs.fontWeight,
      lh: srcs.lineHeight,
      color: srcs.color,
      placeholder: (search.getAttribute('placeholder') || '').slice(0, 30),
      pad: srcs.padding,
      radius: srcs.borderRadius,
    };
    const inner = [...filterCard.children].find(
      (c) => getComputedStyle(c).display === 'grid',
    );
    out.triggers = inner
      ? [...inner.querySelectorAll('[role=combobox]')].map((c) => {
          const r = c.getBoundingClientRect();
          const cs = getComputedStyle(c);
          const chev = c.querySelector('svg');
          const chcs = chev ? getComputedStyle(chev) : null;
          const chr = chev ? chev.getBoundingClientRect() : null;
          return {
            tag: c.tagName,
            w: Math.round(r.width),
            h: Math.round(r.height),
            pad: cs.padding,
            justify: cs.justifyContent,
            align: cs.alignItems,
            bg: cs.backgroundColor,
            radius: cs.borderRadius,
            borderW: cs.borderTopWidth,
            borderC: cs.borderTopColor,
            fs: cs.fontSize,
            fw: cs.fontWeight,
            color: cs.color,
            text: (c.textContent || '').trim().slice(0, 22),
            chevW: chr ? Math.round(chr.width) : null,
            chevH: chr ? Math.round(chr.height) : null,
            chevColor: chcs ? chcs.color : null,
          };
        })
      : [];
  }
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonefiltr91"
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
echo "--- clone income filter interiors ---"
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- clone expenses filter interiors ---"
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== filter-interior clone half done ==="
