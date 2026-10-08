// probe-v9-login-states.mjs — login card sign-up + forgot states at computed depth
// Run on /login with the card in the sign-up state (or forgot state) — pass state via window flag
(() => {
  const out = { url: location.pathname };
  const card = document.querySelector("form")?.closest("div[class*='bg-white'], div[class*='rounded']");
  if (!card) return JSON.stringify({ err: "no card" });
  const text = (card.textContent || "").replace(/\s+/g, " ").slice(0, 200);
  out.state = /Create account|Sign up/i.test(text) ? "signup" : (/forgot/i.test(text) ? "forgot" : "signin");
  out.cardText = text;
  const cardCS = getComputedStyle(card);
  out.card = { bg: cardCS.backgroundColor, radius: cardCS.borderRadius, border: cardCS.borderColor, pad: cardCS.padding, shadow: cardCS.boxShadow.slice(0, 80) };
  // heading
  const h1 = card.querySelector("h1, h2");
  if (h1) {
    const hcs = getComputedStyle(h1);
    const hr = h1.getBoundingClientRect();
    out.heading = { t: (h1.textContent || "").trim(), fs: hcs.fontSize, fw: hcs.fontWeight, c: hcs.color, ls: hcs.letterSpacing, h: Math.round(hr.height) };
  }
  // subheading / description
  const sub = [...card.querySelectorAll("p, div, span")].filter(el => el.children.length === 0 && (el.textContent || "").trim().length > 10 && !el.querySelector("*")).slice(0, 3);
  out.subs = sub.map(el => { const s = getComputedStyle(el); return { t: (el.textContent || "").trim().slice(0, 60), fs: s.fontSize, c: s.color, fw: s.fontWeight }; });
  // primary action button
  const btns = [...card.querySelectorAll("button")].filter(b => (b.textContent || "").trim().match(/Sign in|Sign up|Create|Reset|Send/i) && b.type !== "button" || b.closest("form"));
  out.buttons = btns.slice(0, 3).map(b => {
    const bcs = getComputedStyle(b);
    const br = b.getBoundingClientRect();
    return { t: (b.textContent || "").trim().slice(0, 24), h: Math.round(br.height), bg: bcs.backgroundColor, color: bcs.color, radius: bcs.borderRadius, fw: bcs.fontWeight, fs: bcs.fontSize };
  });
  // google button
  const google = [...card.querySelectorAll("button")].find(b => /Google/i.test(b.textContent || ""));
  if (google) {
    const gcs = getComputedStyle(google);
    const gr = google.getBoundingClientRect();
    out.googleBtn = { h: Math.round(gr.height), w: Math.round(gr.width), bg: gcs.backgroundColor, border: gcs.borderColor, bw: gcs.borderWidth, color: gcs.color, radius: gcs.borderRadius, fs: gcs.fontSize, fw: gcs.fontWeight };
  }
  // links (footer)
  out.links = [...card.querySelectorAll("button, a")].filter(el => /Sign in|Sign up|Forgot|back/i.test(el.textContent || "")).slice(0, 4).map(el => { const ecs = getComputedStyle(el); return { t: (el.textContent || "").trim().slice(0, 40), fs: ecs.fontSize, c: ecs.color, fw: ecs.fontWeight, u: ecs.textDecorationLine }; });
  // confirm-password field presence (signup state)
  out.hasConfirm = !!card.querySelector("input[name='confirmPassword'], input[placeholder*='Confirm' i], input[id*='confirm' i]");
  out.inputs = [...card.querySelectorAll("input")].map(i => { const ics = getComputedStyle(i); return { type: i.type, name: i.name || i.id, h: Math.round(i.getBoundingClientRect().height), fs: ics.fontSize, border: ics.borderColor, bg: ics.backgroundColor, radius: ics.borderRadius }; }).slice(0, 4);
  return JSON.stringify(out, null, 1);
})()
