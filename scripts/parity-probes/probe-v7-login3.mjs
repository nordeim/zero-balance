// probe-v7-login3.mjs — ref login inputs + icons + misc computed values
(() => {
  const out = {};
  const email = document.querySelector('input[type="email"]');
  if (email) {
    const cs = getComputedStyle(email);
    out.emailInput = {
      w: Math.round(email.getBoundingClientRect().width), h: Math.round(email.getBoundingClientRect().height),
      bg: cs.backgroundColor, border: cs.borderTopWidth + " " + cs.borderTopColor,
      radius: cs.borderRadius, padL: cs.paddingLeft,
      phColor: cs.color,
    };
  }
  // icon inside the input row? (mail/lock svg positioned absolutely)
  const wrap = email?.parentElement;
  out.inputWrap = wrap ? {
    cls: (wrap.className || "").toString().slice(0, 60),
    svgCount: wrap.querySelectorAll("svg").length,
    svgCls: wrap.querySelector("svg") ? (wrap.querySelector("svg").getAttribute("class") || "").slice(0, 60) : null,
    svgColor: wrap.querySelector("svg") ? getComputedStyle(wrap.querySelector("svg")).color : null,
  } : null;
  // google button full dump
  const gbtn = [...document.querySelectorAll("button")].find(b => /Google/.test(b.textContent || ""));
  if (gbtn) {
    const cs = getComputedStyle(gbtn);
    out.google = {
      cls: (gbtn.className || "").toString().slice(0, 160),
      border: cs.borderTopWidth + " " + cs.borderTopColor,
      bg: cs.backgroundColor, color: cs.color, size: cs.fontSize,
      pad: cs.padding, h: Math.round(gbtn.getBoundingClientRect().height),
    };
  }
  // submit button
  const sub = [...document.querySelectorAll('button[type="submit"], form button')].find(b => /Sign in|Create/.test(b.textContent || ""));
  if (sub) {
    const cs = getComputedStyle(sub);
    out.submit = {
      cls: (sub.className || "").toString().slice(0, 160),
      bg: cs.backgroundColor, color: cs.color, h: Math.round(sub.getBoundingClientRect().height),
      hoverBg: (sub.className || "").toString().match(/hover:bg-\S+/)?.[0] || null,
      shadow: cs.boxShadow.slice(0, 40),
    };
  }
  // top gradient bar on the card
  const bar = document.querySelector(".rounded-2xl > div");
  if (bar && getComputedStyle(bar).backgroundImage !== "none") {
    out.topBar = { h: Math.round(bar.getBoundingClientRect().height), bgImage: getComputedStyle(bar).backgroundImage.slice(0, 100) };
  }
  // logo ring
  const logoWrap = document.querySelector("img")?.parentElement;
  if (logoWrap) {
    const cs = getComputedStyle(logoWrap);
    out.logoWrap = {
      cls: (logoWrap.className || "").toString().slice(0, 120),
      w: Math.round(logoWrap.getBoundingClientRect().width),
      ring: cs.boxShadow.slice(0, 60), ringColor: getComputedStyle(logoWrap, "::after")?.borderColor,
      radius: cs.borderRadius,
    };
  }
  return JSON.stringify(out, null, 1);
})()
