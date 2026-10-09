// v21 live check: complete the verify-email flow on the clone parity
// server — read the dev code from the honest box, type it into the six
// inputs, submit, and confirm the dashboard landing.
(() => {
  const code = (document.body.textContent.match(/verification code is (\d{6})/) || [])[1];
  if (!code) return "no code found";
  const inputs = [...document.querySelectorAll("input[inputmode=numeric]")];
  if (inputs.length !== 6) return "inputs: " + inputs.length;
  const setVal = (el, v) => {
    const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, "value").set;
    setter.call(el, v);
    el.dispatchEvent(new Event("input", { bubbles: true }));
  };
  code.split("").forEach((d, i) => setVal(inputs[i], d));
  const btn = [...document.querySelectorAll("button")].find(
    (b) => (b.textContent || "").trim() === "Verify email",
  );
  btn.click();
  return "submitted " + code;
})()
