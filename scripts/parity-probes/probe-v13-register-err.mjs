// probe-v13-register-err.mjs — register duplicate-email error: banner text + chrome
// (run on a LOGGED-OUT login page; switch to the sign-up state first, then
// fill the existing account's email + matching valid passwords and submit —
// the 409 lands before any write, so this is a read-only probe).
(() => {
  const banner = document.querySelector("[role=alert]") ||
    [...document.querySelectorAll("div")].find(d => getComputedStyle(d).backgroundColor === "rgba(254, 242, 242, 0.7)");
  if (!banner) return JSON.stringify({ err: "no banner (submit first)" });
  const cs = getComputedStyle(banner);
  const inner = banner.firstElementChild;
  const ics = inner ? getComputedStyle(inner) : null;
  const r = banner.getBoundingClientRect();
  return JSON.stringify({
    text: banner.textContent.trim().slice(0, 100),
    w: Math.round(r.width), h: Math.round(r.height),
    bg: cs.backgroundColor, border: cs.border, radius: cs.borderRadius, pad: cs.padding,
    inner: ics ? { color: ics.color, fs: ics.fontSize, fw: ics.fontWeight, lh: ics.lineHeight, ta: ics.textAlign } : null,
  }, null, 1);
})()
