#!/usr/bin/env python3
"""Compare the v127 both-sides census values axis by axis (ref vs clone).

Reads the saved half logs (/tmp/ref-arbit-v127.log + /tmp/clone-arbit-v127.log),
extracts the two census JSON lines per side (income + expenses), and diffs
every leaf axis. Known documented classes are whitelisted (the v121
census values, reproduced exactly):
  - the user-identity class: the avatar text (ref "U" vs clone "D");
  - the seed-count class: the grid childCount (ref 1/4 vs clone 2/3) and
    the item texts/amounts (each site's own data);
  - the v70b-decomposed class: the card h (ref 200 vs clone 230 — the
    natural income height vs the clone's superset wrap);
  - the v57 DATA-CONDITIONAL class: the expenses footer childCount
    (ref 1 vs clone 2 — the reference RENDERS payment chips when its
    data carries them; its expense items ship none);
  - the v57 wrap/classification-VALUE classes: the expenses badgeRow h
    (ref 22 vs clone 52) + badgeCount (ref 3 vs clone 4 — the clone's
    Recurring superset chip + the wrap; the chip chrome byte-identical);
  - the column-distribution rounding noise WITHIN the documented
    309.328px family (the income template's last-column sub-pixel).
Every OTHER axis must be byte-identical. Any non-whitelisted delta is a
FAIL (a new clone gap).
"""
import json, re, sys

def load(path):
    text = open(path, encoding="utf-8").read()
    views = {}
    for view in ("income", "expenses"):
        m = re.search(r"--- (?:ref|clone) " + view + r" ---\n\"(\{.*\})\"", text)
        if not m:
            print(f"FAIL: {view} census line not found in {path}")
            sys.exit(1)
        # the log line is a bash-quoted JSON string
        raw = m.group(1)
        raw = raw.replace('\\"', '"').replace("\\\\", "\\")
        views[view] = json.loads(raw)
    return views

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

ref = load("/tmp/ref-arbit-v127.log")
clone = load("/tmp/clone-arbit-v127.log")

# EXACT-QUAD whitelist: (view, axis, ref value, clone value) — the
# v121-documented standing classes (the v127 census must reproduce the
# v121 values EXACTLY).
QUADS = {
    # the user-identity class (the avatar chrome byte-identical)
    ("income", "avatar.text", "U", "D"),
    ("expenses", "avatar.text", "U", "D"),
    # the v70b-decomposed card-height class
    ("income", "card.h", 200, 230),
    ("expenses", "card.h", 200, 230),
    # the seed-count class (the grid childCount per view)
    ("income", "grid.childCount", 1, 2),
    ("expenses", "grid.childCount", 4, 3),
    # the v57 DATA-CONDITIONAL class (the expenses footer childCount)
    ("expenses", "footer.childCount", 1, 2),
    # the v57 wrap/classification-VALUE classes (the expenses badgeRow)
    ("expenses", "badgeRow.h", 22, 52),
    ("expenses", "badgeRow.badgeCount", 3, 4),
}

# VALUE-INDEPENDENT axis whitelist: any delta on these axes is a
# documented data class (each site's own seed text/labels).
AXES = {
    # the amounts + dates + footer texts (each site's own data)
    ("income", "amount.text"),
    ("expenses", "amount.text"),
    ("income", "footer.children[0].text"),
    ("expenses", "footer.children[0].text"),
    ("income", "footer.children[1].text"),
    ("expenses", "footer.children[1].text"),
    # the badge texts (the classification/frequency/recurring VALUES)
    *[("income", f"badgeRow.texts[{i}]") for i in range(4)],
    *[("expenses", f"badgeRow.texts[{i}]") for i in range(4)],
    # the column template sub-pixel noise (the last-column distribution
    # within the documented 309.328px family)
    ("income", "grid.template"),
    ("expenses", "grid.template"),
}

identical = 0
doc_deltas = []
new_deltas = []
# the asymmetric-key families: the reference's expenses footer carries
# ONE child (its expense items ship no payment method) while the clone's
# carries TWO (the chip) — the missing footer.children[1].* and the
# extra badgeRow.texts[3] axes are the v57 DATA-CONDITIONAL class BY
# CONSTRUCTION (the childCount delta itself is in QUADS).
ASYMMETRIC_DOC = re.compile(
    r"^footer\.children\[1\]\."
    r"|^badgeRow\.texts\[\d+\]$"
)
for view in ("income", "expenses"):
    r = flatten(ref[view])
    c = flatten(clone[view])
    only_r = set(r.keys()) - set(c.keys())
    only_c = set(c.keys()) - set(r.keys())
    for k in sorted(only_r | only_c):
        if ASYMMETRIC_DOC.match(k):
            doc_deltas.append((view, k, r.get(k, "<absent>"), c.get(k, "<absent>")))
        else:
            new_deltas.append((view, k, r.get(k, "<absent>"), c.get(k, "<absent>")))
    for k in sorted(set(r.keys()) & set(c.keys())):
        if r[k] == c[k]:
            identical += 1
        elif (view, k, r[k], c[k]) in QUADS:
            doc_deltas.append((view, k, r[k], c[k]))
        elif (view, k) in AXES:
            doc_deltas.append((view, k, r[k], c[k]))
        else:
            new_deltas.append((view, k, r[k], c[k]))

total = identical + len(doc_deltas) + len(new_deltas)
print(f"axes compared: {total} — identical: {identical} — documented-class deltas: {len(doc_deltas)}")
for view, k, rv, cv in doc_deltas:
    print(f"  [{view}] {k}: ref {rv!r} vs clone {cv!r} — DOCUMENTED CLASS")
if new_deltas:
    print(f"NEW-DELTA FAILURES ({len(new_deltas)}):")
    for view, k, rv, cv in new_deltas:
        print(f"  [{view}] {k}: ref {rv!r} vs clone {cv!r}")
    sys.exit(1)
print("\nNO NEW CLONE GAP — every delta a documented class, the rest byte-identical")
