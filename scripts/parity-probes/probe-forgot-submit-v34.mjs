(async () => {
  const input = document.querySelector('main form input');
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(input, 'probe-forgot-v34@test.example');
  await new Promise(r => setTimeout(r, 300));
  const submit = [...document.querySelectorAll('main form button')].find(b => /send reset/i.test(b.textContent));
  submit.click();
  await new Promise(r => setTimeout(r, 2500));
  const txt = document.body.innerText;
  return JSON.stringify({
    path: location.pathname,
    h2: [...document.querySelectorAll('h2')].map(h => h.textContent.trim()).slice(0, 3),
    stillForm: !!document.querySelector('main form'),
    stateText: txt.split('\n').filter(l => l.trim().length > 3).slice(0, 12),
  });
})()
