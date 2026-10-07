// probe-v7-login-flow.mjs — fill + submit the login form (runs on /login)
(() => {
  const email = document.querySelector("#email");
  const password = document.querySelector("#password");
  if (!email || !password) return "no inputs";
  const setVal = (el, v) => {
    const proto = el instanceof HTMLTextAreaElement ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
    const setter = Object.getOwnPropertyDescriptor(proto, "value").set;
    setter.call(el, v);
    el.dispatchEvent(new Event("input", { bubbles: true }));
  };
  setVal(email, "demo@zerobalance.app");
  setVal(password, "Demo1234!");
  const form = email.closest("form");
  form?.requestSubmit();
  return "submitted";
})()
