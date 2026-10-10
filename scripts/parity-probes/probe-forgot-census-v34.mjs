(async () => {
  await new Promise(r => setTimeout(r, 400));
  const h2 = [...document.querySelectorAll('h2')].find(h => /reset your password/i.test(h.textContent));
  if (!h2) return JSON.stringify({error: 'not on forgot state'});
  const card = document.querySelector('main');
  const form = card.querySelector('form');
  const input = form.querySelector('input');
  const submit = [...form.querySelectorAll('button')].find(b => /send reset/i.test(b.textContent));
  const back = [...document.querySelectorAll('button')].find(b => /back to sign in/i.test(b.textContent));
  const ir = input.getBoundingClientRect(), sr = submit.getBoundingClientRect(), br = back.getBoundingClientRect();
  const iSt = getComputedStyle(input), sSt = getComputedStyle(submit), bSt = getComputedStyle(back);
  return JSON.stringify({
    path: location.pathname,
    formGeometry: { inputW: Math.round(ir.width), inputH: Math.round(ir.height), submitW: Math.round(sr.width), submitH: Math.round(sr.height) },
    inputClasses: (input.className || '').toString(),
    submitClasses: (submit.className || '').toString().slice(0, 200),
    backClasses: (back.className || '').toString().slice(0, 200),
    inputComputed: { h: iSt.height, border: iSt.borderColor, radius: iSt.borderRadius, fontSize: iSt.fontSize, bg: iSt.backgroundColor },
    submitComputed: { h: sSt.height, bg: sSt.backgroundColor, radius: sSt.borderRadius, color: sSt.color, fontSize: sSt.fontSize },
    backComputed: { h: bSt.height, color: bSt.color, fontSize: bSt.fontSize, bg: bSt.backgroundColor },
    initialFocus: document.activeElement === input ? 'email-input' : (document.activeElement.tagName + ':' + (document.activeElement.className || '').toString().slice(0, 40)),
    focusableCensus: [...card.querySelectorAll('button, input, a[href], [tabindex]:not([tabindex="-1"])')].map(e => e.tagName + ':' + (e.name || e.textContent.trim().slice(0, 14) || e.getAttribute('aria-label') || '?')).slice(0, 12),
  });
})()
