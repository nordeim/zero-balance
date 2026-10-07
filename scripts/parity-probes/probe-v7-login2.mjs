// probe-v7-login2.mjs — login page outer structure + link typography + h1 stack
(() => {
  const out = {};
  // outer wrapper chain above the card
  const card = [...document.querySelectorAll("div")].find(d => /rounded-2xl/.test(d.className?.toString?.() || "") && /bg-white/.test(d.className?.toString?.() || "") && d.querySelector("h1"));
  if (card) {
    const chain = [];
    let el = card.parentElement;
    for (let i = 0; i < 4 && el && el !== document.body; i++) {
      const cs = getComputedStyle(el);
      chain.push({
        tag: el.tagName, cls: (el.className || "").toString().slice(0, 90),
        bg: cs.backgroundColor, bgImage: cs.backgroundImage !== "none" ? cs.backgroundImage.slice(0, 90) : "none",
        minH: cs.minHeight, display: cs.display, justify: cs.justifyContent,
      });
      el = el.parentElement;
    }
    out.chain = chain.reverse();
  }
  // link buttons typography
  out.links = [...document.querySelectorAll("button")].filter(b => /Forgot|Sign up/.test(b.textContent || "")).map(b => {
    const cs = getComputedStyle(b);
    return {
      text: (b.textContent || "").trim(),
      size: cs.fontSize, lineH: cs.lineHeight, pad: cs.padding, h: Math.round(b.getBoundingClientRect().height),
      color: cs.color, hoverColor: (b.className || "").toString().match(/hover:text-\S+/)?.[0] || null,
    };
  });
  // subtitle under h1
  const sub = document.querySelector("h1")?.parentElement?.querySelector("p, span");
  if (sub) {
    const scs = getComputedStyle(sub);
    out.subtitle = { text: sub.textContent?.trim().slice(0, 50), size: scs.fontSize, color: scs.color, cls: (sub.className || "").toString().slice(0, 70) };
  }
  // label typography
  const label = document.querySelector("label");
  if (label) {
    const lcs = getComputedStyle(label);
    out.label = { text: label.textContent?.trim().slice(0, 20), size: lcs.fontSize, weight: lcs.fontWeight, color: lcs.color, cls: (label.className || "").toString().slice(0, 70) };
  }
  // divider "or"
  const or = [...document.querySelectorAll("div,span,p")].find(el => el.children.length === 0 && /^or$/i.test(el.textContent?.trim() || ""));
  out.orDivider = or ? { cls: (or.className || "").toString().slice(0, 60), parentCls: (or.parentElement?.className || "").toString().slice(0, 70) } : null;
  return JSON.stringify(out, null, 1);
})()
