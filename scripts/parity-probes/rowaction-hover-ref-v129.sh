#!/usr/bin/env bash
# rowaction-hover-ref-v129.sh — the REF-side-only supplementary census for
# the v129 repair-scope decision: the reference's CALCULATOR ROW-ACTION
# buttons' (edit + trash) OWN-HOVER end-states — does the reference's
# ghost-hover family (hover:bg-accent + hover:text-accent-foreground, the
# v27 G1-documented family the X now measured carrying) extend to the row
# actions, or do the red trash + near-black edit keep their base colors
# under hover? READ-ONLY per the v46 rule (login + hover + dialog-open
# only; the reference's OWN Rent calculator carries the standing
# "Contents Insurance" row — no fixture needed on this side).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

PANEL_FINDER='const panel = [...document.querySelectorAll("[role=dialog]")].find((d) => /Rent Calculator/i.test((d.innerText || ""))) ||
  [...document.querySelectorAll("div")].find((d) => getComputedStyle(d).maxWidth === "768px" && d.getBoundingClientRect().width > 300);'

export AGENT_BROWSER_SESSION="refrowact129"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "ref login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4

echo "=== REF: open the Rent calculator (REAL pointer press) ==="
CARD_CENTER="$(agent-browser eval '(async () => {
  const main = document.querySelector("main")||document.body;
  const card = [...main.querySelectorAll("div.rounded-xl")].find((c) => (c.innerText||"").includes("Rent"));
  if (!card) return JSON.stringify({err: "no Rent card"});
  card.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 200));
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()' 2>/dev/null | tail -1 | tr -d '"')"
echo "rent card center: $CARD_CENTER"
CCX="${CARD_CENTER%,*}"; CCY="${CARD_CENTER#*,}"
agent-browser mouse move "$CCX" "$CCY" >/dev/null 2>&1
sleep 1
CALC_CENTER="$(agent-browser eval '(async () => {
  const main = document.querySelector("main")||document.body;
  const card = [...main.querySelectorAll("div.rounded-xl")].find((c) => (c.innerText||"").includes("Rent"));
  const btn = [...card.querySelectorAll("button")].find((b) => /^Calculate$/i.test((b.textContent||"").trim()));
  if (!btn) return JSON.stringify({err: "no Calculate"});
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()' 2>/dev/null | tail -1 | tr -d '"')"
BCX="${CALC_CENTER%,*}"; BCY="${CALC_CENTER#*,}"
agent-browser mouse move "$BCX" "$BCY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

ACTION_STATE_JS="(async () => {
  ${PANEL_FINDER}
  if (!panel) return JSON.stringify({err: \"no panel\"});
  const rows = [...panel.querySelectorAll(\"div\")].filter((d) => {
    const t = (d.innerText || \"\");
    return /Contents Insurance/i.test(t) && d.getBoundingClientRect().height > 80 && d.getBoundingClientRect().height < 140;
  });
  const row = rows[0];
  if (!row) return JSON.stringify({err: \"no row\"});
  const acts = [...row.querySelectorAll(\"button\")].filter((b) => {
    const r = b.getBoundingClientRect();
    return Math.round(r.width) <= 34 && Math.round(r.height) <= 34;
  });
  return JSON.stringify({ btnCount: acts.length });
})()"
echo "=== REF: row action button count (parked) ==="
agent-browser eval "$ACTION_STATE_JS" 2>/dev/null | tail -1

# hover the ROW first (the reveal), then each action button's own center
ROW_CENTER="$(agent-browser eval "(async () => {
  ${PANEL_FINDER}
  if (!panel) return \"ERR\";
  const rows = [...panel.querySelectorAll(\"div\")].filter((d) => {
    const t = (d.innerText || \"\");
    return /Contents Insurance/i.test(t) && d.getBoundingClientRect().height > 80 && d.getBoundingClientRect().height < 140;
  });
  const row = rows[0];
  if (!row) return \"ERR\";
  const r = row.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + \",\" + Math.round(r.y + r.height / 2);
})()" 2>/dev/null | tail -1 | tr -d '"')"
echo "row center: $ROW_CENTER"
RCX="${ROW_CENTER%,*}"; RCY="${ROW_CENTER#*,}"
agent-browser mouse move "$RCX" "$RCY" >/dev/null 2>&1
sleep 1

BTN_CENTERS="$(agent-browser eval "(async () => {
  ${PANEL_FINDER}
  if (!panel) return \"ERR\";
  const rows = [...panel.querySelectorAll(\"div\")].filter((d) => {
    const t = (d.innerText || \"\");
    return /Contents Insurance/i.test(t) && d.getBoundingClientRect().height > 80 && d.getBoundingClientRect().height < 140;
  });
  const row = rows[0];
  if (!row) return \"ERR\";
  const acts = [...row.querySelectorAll(\"button\")].filter((b) => {
    const r = b.getBoundingClientRect();
    return Math.round(r.width) <= 34 && Math.round(r.height) <= 34;
  });
  return acts.map((b) => {
    const r = b.getBoundingClientRect();
    return Math.round(r.x + r.width / 2) + \",\" + Math.round(r.y + r.height / 2);
  }).join(\" \");
})()" 2>/dev/null | tail -1 | tr -d '"' | tr -d '\n')"
echo "action button centers: $BTN_CENTERS"

READ_ACTION_STATE="(async () => {
  ${PANEL_FINDER}
  if (!panel) return JSON.stringify({err: \"no panel in action read\"});
  const rows = [...panel.querySelectorAll(\"div\")].filter((d) => {
    const t = (d.innerText || \"\");
    return /Contents Insurance/i.test(t) && d.getBoundingClientRect().height > 80 && d.getBoundingClientRect().height < 140;
  });
  const row = rows[0];
  if (!row) return JSON.stringify({err: \"no row in action read\"});
  const acts = [...row.querySelectorAll(\"button\")].filter((b) => {
    const r = b.getBoundingClientRect();
    return Math.round(r.width) <= 34 && Math.round(r.height) <= 34;
  });
  return JSON.stringify(acts.map((b) => {
    const cs = getComputedStyle(b);
    return { hoverMatch: b.matches(\":hover\"), bg: cs.backgroundColor, color: cs.color, opacity: getComputedStyle(b.parentElement).opacity };
  }));
})()"

# hover each action button in turn (the centers as "x,y x,y")
for pair in $BTN_CENTERS; do
  AX="${pair%,*}"; AY="${pair#*,}"
  echo "=== REF: action OWN-HOVER at $AX,$AY ==="
  agent-browser mouse move "$AX" "$AY" >/dev/null 2>&1
  sleep 1
  agent-browser eval "$READ_ACTION_STATE" 2>/dev/null | tail -1
done

echo "=== rowaction ref census done ==="
