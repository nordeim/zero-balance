// v23 session: the verify-email state at MOBILE (390x844) — never measured
// at this viewport (v21 measured it at desktop). Reports the state's chrome:
// the icon circle, the 6 code inputs, the Verify button, the hint texts.
(() => {
  const out = {};
  const h = [...document.querySelectorAll('h2')].find((el) => /verify your email/i.test(el.textContent || ''));
  if (!h) return 'not on verify state';
  const scope = h.closest('main') || document.body;

  // the icon circle: a rounded-full div above the heading
  const circle = [...scope.querySelectorAll('div')].find((el) => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return Math.abs(r.width - r.height) < 4 && r.width > 40 && r.width < 90 && (cs.borderRadius === '9999px' || cs.borderRadius === '50%');
  });
  if (circle) {
    const r = circle.getBoundingClientRect(); const cs = getComputedStyle(circle);
    out.circle = { w: Math.round(r.width), bg: cs.backgroundColor, radius: cs.borderRadius };
    const svg = circle.querySelector('svg');
    if (svg) { const sr = svg.getBoundingClientRect(); out.circleIcon = { w: Math.round(sr.width), h: Math.round(sr.height), color: getComputedStyle(svg).color }; }
  }

  // the 6 code inputs
  const inputs = [...scope.querySelectorAll('input')].filter((el) => {
    const r = el.getBoundingClientRect();
    return r.height > 30 && r.height < 60 && el.type !== 'hidden';
  });
  out.codeInputs = inputs.slice(0, 6).map((el) => {
    const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
    return { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), radius: cs.borderRadius, border: cs.border.slice(0, 40), ta: cs.textAlign };
  });
  out.inputCount = inputs.length;
  if (inputs.length > 1) out.gap = Math.round(inputs[1].getBoundingClientRect().x - (inputs[0].getBoundingClientRect().x + inputs[0].getBoundingClientRect().width));

  // the Verify button
  const vbtn = [...scope.querySelectorAll('button')].find((b) => /verify email/i.test((b.textContent || '').trim()));
  if (vbtn) {
    const r = vbtn.getBoundingClientRect(); const cs = getComputedStyle(vbtn);
    out.verifyBtn = { w: Math.round(r.width), h: Math.round(r.height), bg: cs.backgroundColor, color: cs.color, radius: cs.borderRadius };
  }
  out.h2 = { text: h.textContent.trim(), size: getComputedStyle(h).fontSize, weight: getComputedStyle(h).fontWeight, color: getComputedStyle(h).color };
  out.vw = innerWidth; out.vh = innerHeight;
  return JSON.stringify(out, null, 1);
})()
