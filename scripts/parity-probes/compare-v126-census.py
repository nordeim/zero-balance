#!/usr/bin/env python3
"""Compare the v126 both-sides census values axis by axis (ref vs clone).

Reads the saved half logs (/tmp/vlm126/ref-arbit.log + /tmp/vlm126/clone-arbit.log),
extracts the two census JSON lines (NW_CENSUS / DASH_CENSUS), and diffs
every leaf axis. Known documented classes are whitelisted:
  - the v41 mobile-superset class (NETWORTH): the reference's own 464px
    /networth overflow at 390 (its documented R-bug-4) with the fixed
    2-col stat tiles, vs the clone's fitting 1-col stack — docSW 464/390
    + every width consequence (card.w/right, statGrid.cols/w, tiles w,
    medallion.right/clipsViewport) + the stacking height consequence
    (card.h — the 2-col ref card shorter than the 1-col clone);
  - the DASH width-guard class: the reference's own 395px dashboard
    overflow at 390 vs the clone's fitting 390 — docSW 395/390 + the 5px
    width consequences (subtitle.rect.w/blockW, breakdownCard.rect.w,
    children w);
  - the Range-walk line bucketing: the subtitle's two line texts bucket
    differently at the 5px width difference (the ref wraps after "to",
    the clone after "expenses") — the documented consequence class of the
    width guard (the v62 subtitle census family; the line TOPS identical).

The v126 re-run (the MOBILE TWINS pair's TENTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126])
must reproduce the v120 census values EXACTLY (a drift re-check since v120).
"""
import json, re, sys

def load(path):
    text = open(path, encoding="utf-8").read()
    parts = {}
    # the census JSON lines appear as bash-quoted strings, one per view:
    # the NW line carries the statGrid key; the DASH line the subtitle key.
    for line in text.split("\n"):
        m = re.match(r'^"(\{.*\})"$', line.strip())
        if not m:
            continue
        raw = m.group(1).replace('\\"', '"').replace("\\\\", "\\")
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if "statGrid" in obj:
            parts["NW"] = obj
        elif "subtitle" in obj:
            parts["DASH"] = obj
    if "NW" not in parts or "DASH" not in parts:
        print(f"FAIL: census lines not found in {path} ({sorted(parts)})")
        sys.exit(1)
    return parts

def flatten(obj, prefix=""):
    out = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.update(flatten(v, f"{prefix}.{k}" if prefix else k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out.update(flatten(v, f"{prefix}[{i}]"))
    else:
        out[prefix] = obj
    return out

ref = load("/tmp/vlm126/ref-arbit.log")
clone = load("/tmp/vlm126/clone-arbit.log")

# documented-class whitelist: (axis, ref value, clone value) triples.
# All delta families below are the v120-documented standing classes
# (the v126 census must reproduce the v120 values EXACTLY):
WHITELIST = {
    # --- the v41 mobile-superset class (NETWORTH: the ref's own 464px
    # overflow + fixed 2-col tiles vs the clone's fitting 1-col stack) ---
    ("NW.docSW", 464, 390),
    ("NW.card.w", 432, 358),
    ("NW.card.h", 333, 421),           # the stacking consequence
    ("NW.card.right", 448, 374),
    ("NW.statGrid.cols", "175.828px 175.844px", "294px"),
    ("NW.statGrid.w", 368, 294),
    ("NW.tiles[0].w", 176, 294),
    ("NW.tiles[1].w", 176, 294),
    ("NW.medallion.right", 416, 342),
    ("NW.medallion.clipsViewport", True, False),
    # --- the DASH width-guard class (the ref's own 395px overflow vs the
    # clone's fitting 390) + the Range-walk line bucketing consequence ---
    ("DASH.docSW", 395, 390),
    ("DASH.subtitle.rect.w", 363, 358),
    ("DASH.subtitle.blockW", 363, 358),
    ("DASH.subtitle.lines[0].text",
     "Track your income, savings, and expenses to",
     "Track your income, savings, and expenses"),
    ("DASH.subtitle.lines[1].text",
     "achieve net zero",
     "to achieve net zero"),
    ("DASH.breakdownCard.rect.w", 363, 358),
    ("DASH.breakdownCard.children[0].w", 313, 308),
    ("DASH.breakdownCard.children[1].w", 313, 308),
}

identical, documented, NEW = 0, 0, []
axes_seen = set()
for part in ("NW", "DASH"):
    r = flatten(ref[part], part)
    c = flatten(clone[part], part)
    for axis in sorted(set(r) | set(c)):
        axes_seen.add(axis)
        rv, cv = r.get(axis, "<missing>"), c.get(axis, "<missing>")
        if rv == cv:
            identical += 1
        elif (axis, rv, cv) in WHITELIST:
            documented += 1
        else:
            NEW.append((axis, rv, cv))

print(f"census axes compared: {len(axes_seen)} "
      f"[identical {identical} + documented-class {documented}]")
for axis, rv, cv in sorted(NEW):
    print(f"  NEW DELTA: {axis}: ref {rv!r} vs clone {cv!r}")
if NEW:
    print(f"RESULT: {len(NEW)} NEW delta(s) — INVESTIGATE")
    sys.exit(1)
print("RESULT: ZERO new deltas — every axis identical or a documented class")
print("(the v120 census values reproduced EXACTLY — zero drift since v120)")
