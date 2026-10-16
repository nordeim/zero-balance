#!/usr/bin/env bash
# arbit-v71.sh — the v71 NEW-pair program's flags, DOM-arbitrated per the
# v43 rule, at MOBILE 390x844 on BOTH sides (reference first, clone via
# with-server):
#   PAIR 2 (expenses) flags:
#   (1) the card footer content (payment-method labels) — the expected
#       v57 DATA-CONDITIONAL class (chrome byte-identical, chips data)
#   (2) the badge wrapping (the Recurring superset wrap) — the v57 wrap
#       data class (chrome byte-identical, wrap arithmetic)
#   (3) the floating "Edit with Base44" element — platform chrome
#       (excluded by rule, never arbitrated)
#   PAIR 3 (savings) flags:
#   (1) the card footer content — the v57/v58 DATA-CONDITIONAL class
#   (2) the badge arrangement — the v57 wrap class
#   (3) the badge styling (the "need" red vs "savings" green
#       classification VALUE + the "active" badge chrome) — the v58
#       data class (color maps locked by badge-colors.spec.ts) + the
#       active-badge chrome census (the "padding different" claim)
#   THE NEW AXIS (the v71 discovery): the SUBTITLE P's conditional
#   render — the reference's cards with an EMPTY subcategory render NO
#   subtitle P at all (titleRow h 28, card h 180); the census measures
#   subtitleP presence + geometry per card on BOTH sides.
# READ-ONLY.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const out = { view: location.pathname, docSW: document.documentElement.scrollWidth };
  // find item cards: h4 headings inside the content, walk up to the
  // rounded card root (radius 12 card with pad 20)
  const h4s = [...document.querySelectorAll('h4')].filter(h => h.getBoundingClientRect().width > 0 && h.getBoundingClientRect().width < 360);
  const cards = [];
  for (const h of h4s) {
    let card = h;
    while (card && card !== document.body) {
      const cs = getComputedStyle(card);
      if (parseInt(cs.borderRadius) === 12 && parseInt(cs.paddingTop||cs.padding) >= 15 && card.getBoundingClientRect().width < 380 && card.getBoundingClientRect().width > 200) break;
      card = card.parentElement;
    }
    if (!card || card === document.body) continue;
    if (cards.includes(card)) continue;
    cards.push(card);
  }
  out.cardCount = cards.length;
  out.cards = cards.map((card, i) => {
    const ccs = getComputedStyle(card);
    const cr = card.getBoundingClientRect();
    const c = { title: '', cardH: Math.round(cr.height), cardW: Math.round(cr.width), pad: ccs.padding, radius: ccs.borderRadius, border: ccs.borderTopColor, shadow: ccs.boxShadow.slice(0, 60) };
    // the title row: the flex row that is the card's first block child
    const titleRow = [...card.children].find(ch => getComputedStyle(ch).display.includes('flex') && (ch.textContent||'').trim().length > 0 && ch.querySelector('h4'));
    if (titleRow) {
      const trcs = getComputedStyle(titleRow);
      c.titleRowH = Math.round(titleRow.getBoundingClientRect().height);
      c.titleRowMb = trcs.marginBottom;
      const h4 = titleRow.querySelector('h4');
      c.title = (h4 ? h4.textContent : '').trim().slice(0, 24);
      const h4cs = h4 ? getComputedStyle(h4) : null;
      c.titleFs = h4cs ? h4cs.fontSize : null;
      c.titleFw = h4cs ? h4cs.fontWeight : null;
      c.titleColor = h4cs ? h4cs.color : null;
      // the subtitle P: the p sibling AFTER the h4's wrapper inside the flex-1 block
      const titleBlock = h4 ? h4.parentElement : null;
      const flex1 = titleBlock ? titleBlock.parentElement : null;
      const subP = flex1 ? [...flex1.children].find(ch => ch.tagName === 'P') : null;
      c.subtitleP = subP ? {
        present: true,
        h: Math.round(subP.getBoundingClientRect().height),
        fs: getComputedStyle(subP).fontSize,
        lh: getComputedStyle(subP).lineHeight,
        color: getComputedStyle(subP).color,
        text: (subP.textContent || '').trim().slice(0, 24),
      } : { present: false };
    }
    // the amount block (the text-2xl p)
    const amountP = [...card.querySelectorAll('p')].find(p => parseFloat(getComputedStyle(p).fontSize) >= 20);
    if (amountP) {
      c.amountFs = getComputedStyle(amountP).fontSize;
      c.amountFw = getComputedStyle(amountP).fontWeight;
      c.amountH = Math.round(amountP.getBoundingClientRect().height);
      const ab = amountP.parentElement;
      c.amountMb = getComputedStyle(ab).marginBottom;
    }
    // the badge row (flex-wrap)
    const badgeRow = [...card.children].find(ch => typeof ch.className === 'string' && /flex-wrap/.test(ch.className));
    if (badgeRow) {
      const bcs = getComputedStyle(badgeRow);
      c.badgeRow = {
        display: bcs.display, wrap: bcs.flexWrap, gap: bcs.gap, mb: bcs.marginBottom,
        h: Math.round(badgeRow.getBoundingClientRect().height),
        badgeCount: badgeRow.children.length,
        texts: [...badgeRow.children].map(b => (b.textContent || '').trim()),
      };
      c.badge0 = [...badgeRow.children].map(b => {
        const cs = getComputedStyle(b);
        return { text: (b.textContent || '').trim().slice(0, 12), h: Math.round(b.getBoundingClientRect().height), w: Math.round(b.getBoundingClientRect().width), pad: cs.padding, radius: cs.borderRadius, fs: cs.fontSize, fw: cs.fontWeight, bg: cs.backgroundColor, color: cs.color, border: cs.borderTopColor };
      });
    }
    // the footer row (the last flex justify-between child)
    const footer = [...card.children].filter(ch => getComputedStyle(ch).display.includes('flex')).pop();
    if (footer) {
      const fcs = getComputedStyle(footer);
      c.footer = {
        display: fcs.display, justify: fcs.justifyContent, fs: fcs.fontSize,
        color: fcs.color, h: Math.round(footer.getBoundingClientRect().height),
        childCount: footer.children.length,
        children: [...footer.children].map(el => {
          const cs = getComputedStyle(el);
          const icon = el.querySelector('svg');
          return { display: cs.display, gap: cs.gap, text: (el.textContent || '').trim().slice(0, 20), iconW: icon ? Math.round(icon.getBoundingClientRect().width) : null };
        }),
      };
    }
    return c;
  });
  return JSON.stringify(out);
})()"

run_ref () {
  local VIEW="$1"
  agent-browser open "$REF$VIEW" >/dev/null 2>&1
  sleep 4
  echo "=== REF $VIEW (390) ==="
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
}

echo "########## REFERENCE SIDE ##########"
export AGENT_BROWSER_SESSION="refarbit71"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {
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
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  if echo "$RESULT" | grep -q "submitted"; then echo "login ok"; break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
run_ref "/expenses"
run_ref "/savings"
run_ref "/income"

echo ""
echo "########## CLONE SIDE ##########"
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbit71"
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
for VIEW in /expenses /savings /income; do
  agent-browser open "http://localhost:3200\$VIEW" >/dev/null 2>&1
  sleep 4
  echo "=== CLONE \$VIEW (390) ==="
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
done
EOF
echo "=== arbit-v71 done ==="
