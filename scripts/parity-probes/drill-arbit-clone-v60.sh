#!/usr/bin/env bash
# drill-arbit-clone-v60.sh — the v60 PAIR 2 flags' DOM arbitration, CLONE
# side (the v43 rule). The same census as drill-arbit-ref-v60.sh against
# the :3200 parity server. Runs inside with-server.sh in ONE invocation.
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonear60"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1

echo "=== CLONE drill-down arbitration census at 1280 ==="
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval '(async () => {
  const out = { view: "drill-arbit-clone-1280" };
  const links = [...document.querySelectorAll("a")];
  const dash = links.find((l) => /dashboard/i.test((l.textContent || "")) && l.getBoundingClientRect().height > 0 && l.getBoundingClientRect().left < 300);
  if (dash) {
    const s = getComputedStyle(dash);
    out.navHighlight = { bg: s.backgroundColor, color: s.color, radius: s.borderRadius, fw: s.fontWeight };
  }
  const avatar = [...document.querySelectorAll("div,span")].find((d) => {
    const r = d.getBoundingClientRect();
    const c = getComputedStyle(d);
    return !d.children.length && r.width > 24 && r.width < 60 && c.borderRadius === "9999px" && /^[A-Z]$/.test((d.textContent || "").trim());
  });
  out.avatarLetter = avatar ? (avatar.textContent || "").trim() : null;
  out.base44Badge = /base44/i.test(document.body.textContent || "");
  const track = [...document.querySelectorAll("div")].find((d) => {
    const r = d.getBoundingClientRect();
    const c = getComputedStyle(d);
    return !d.children.length && r.width > 400 && r.height >= 10 && r.height <= 16 && c.borderRadius === "9999px" && /rgba/.test(c.backgroundColor);
  });
  if (track) {
    const fill = track.parentElement && [...track.parentElement.querySelectorAll("div")].find((d) => d !== track && d.getBoundingClientRect().height >= 8 && getComputedStyle(d).borderRadius === "9999px");
    const tr = track.getBoundingClientRect();
    out.progress = {
      trackW: Math.round(tr.width), trackH: Math.round(tr.height),
      trackBg: getComputedStyle(track).backgroundColor,
      fillW: fill ? Math.round(fill.getBoundingClientRect().width) : null,
      fillBg: fill ? getComputedStyle(fill).backgroundImage.slice(0, 60) : null,
    };
  }
  const pieSvgs = [...document.querySelectorAll("svg")].filter((s) => s.querySelector("[class*=recharts-pie-sector], [class*=recharts-pie-label]"));
  out.pieSvgCount = pieSvgs.length;
  if (pieSvgs.length) {
    const svg = pieSvgs[0];
    const labels = [...svg.querySelectorAll("[class*=recharts-pie-label]")].filter((e) => !/line/i.test(e.getAttribute("class") || ""));
    const labelLines = [...svg.querySelectorAll("[class*=recharts-pie-label-line]")];
    out.donutLabels = {
      count: labels.length,
      texts: labels.map((e) => (e.textContent || "").trim()).slice(0, 6),
      labelLineCount: labelLines.length,
      labelFs: labels.length ? getComputedStyle(labels[0]).fontSize : null,
      labelFill: labels.length ? getComputedStyle(labels[0]).fill : null,
      sectors: [...svg.querySelectorAll("[class*=recharts-pie-sector]")].length,
    };
  }
  return JSON.stringify(out);
})()' 2>/dev/null | tail -1

echo "=== clone drill arbit v60 done ==="
EOF
