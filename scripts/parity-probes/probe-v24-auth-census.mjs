// v24 session: the reference auth-form census — ONE eval per state, run right
// after a fresh open+settle (guards the shared-browser-tab false-read lesson:
// the previous "h-11 flat" reads were the CLONE's page left in the tab).
// Captures the responsive height/font families of inputs + submit buttons and
// the label→input gap, for all three states (signin / signup / forgot).
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const states = {};
  const go = async (stateName, btnText) => {
    const btn = [...document.querySelectorAll('main button')].find(b => new RegExp(btnText).test(b.textContent || ''));
    if (btn) { btn.click(); await sleep(1600); }
    const form = document.querySelector('main form');
    if (!form) { states[stateName] = { error: 'no form' }; return; }
    const lbl = form.querySelector('label');
    const rel = lbl ? lbl.parentElement.querySelector(':scope > div') : null;
    const input = form.querySelector('input');
    const submit = [...form.querySelectorAll('button')].find(b => /Sign in|Create account|Send reset link/.test((b.textContent || '').trim()));
    const read = (el, extra) => {
      if (!el) return null;
      const r = el.getBoundingClientRect();
      const cls = el.className.toString();
      return {
        h: Math.round(r.height), w: Math.round(r.width), fs: getComputedStyle(el).fontSize,
        heightCls: cls.split(' ').filter(c => /^h-1|sm:h-/.test(c)).join(' '),
        fsCls: cls.split(' ').filter(c => /^text-(sm|base)$|^sm:text-|^md:text-/.test(c)).join(' '),
        ...extra,
      };
    };
    states[stateName] = {
      formCls: form.className.toString(),
      input: read(input),
      submit: read(submit, { text: (submit.textContent || '').trim() }),
      labelGap: lbl && rel ? Math.round(rel.getBoundingClientRect().y - (lbl.getBoundingClientRect().y + lbl.getBoundingClientRect().height)) : null,
      relMt: rel ? getComputedStyle(rel).marginTop : null,
    };
  };
  // start from the sign-in state (fresh open), then walk signup, then back to signin → forgot
  await go('signin', '^$'); // already on signin after open
  await go('signup', 'Need an account');
  const back = [...document.querySelectorAll('main button')].find(b => /Back to sign in/.test(b.textContent || ''));
  if (back) { back.click(); await sleep(1500); }
  await go('forgot', 'Forgot password');
  states.viewport = { w: innerWidth, h: innerHeight };
  return JSON.stringify(states, null, 1);
})()
