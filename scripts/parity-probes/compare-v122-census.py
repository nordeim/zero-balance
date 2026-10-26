#!/usr/bin/env python3
"""Compare the v122 both-sides census values axis by axis (ref vs clone).

Reads the saved half logs (/tmp/ref-arbit-v122.log + /tmp/clone-arbit-v122.log),
extracts the savings-view census JSON line per side, and diffs every leaf
axis. Known documented classes are whitelisted (the v116 census values,
reproduced exactly):
  - the seed-count class: the grid childCount (ref 1 vs clone 2 — the
    reference's 1-item savings seed vs the clone's 2-item dev seed);
  - the v57/v70b Recurring-wrap class: the card h (ref 200 vs clone 230,
    +30px = the badgeRow h 22 vs 52);
  - the v57 DATA-CONDITIONAL class: the footer childCount (ref 1 vs
    clone 2 — the reference RENDERS payment chips when its data carries
    them; its savings item ships no paymentMethod so its footer renders
    the date-only DIV while the clone's items carry paymentMethods and
    render the SPAN pair — the same two-child structure the reference's
    own income card renders);
  - the v57 wrap/classification-VALUE classes: the badgeRow h (22 vs 52)
    + badge count (3 vs 4 — the clone's Recurring superset chip + the
    wrap; the "monthly" + "active" badges byte-identical in full chrome);
  - the classification-VALUE badge-axis classes: badges[0] (ref "need"
    red vs clone "savings" green) + badges[2] (ref "active" slate vs
    clone "Recurring" green, icon-bearing) — text/border/bg/color/icon
    are value-dependent axes;
  - the seed-data class: the footer date texts (each site's own data);
  - the column-distribution rounding noise WITHIN the documented
    309.328px family (the template's last-column sub-pixel: .328 x3 vs
    .328/.328/.344 — the reference's own expenses template reads the
    same .344 form);
  - the asymmetric families BY CONSTRUCTION: footer.children[1].* (the
    clone-only payment chip) + badges[3].* (the clone-only 4th badge —
    the childCount/count deltas themselves are in QUADS).
Every OTHER axis must be byte-identical. Any non-whitelisted delta is a
FAIL (a new clone gap).
"""
import json, re, sys

VIEW = "savings"

def load(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"=== (?:REF|CLONE) /savings census [^\n]*===\n\"(\{.*\})\"", text)
    if not m:
        print(f"FAIL: savings census line not found in {path}")
        sys.exit(1)
    # the log line is a bash-quoted JSON string
    raw = m.group(1)
    raw = raw.replace('\\"', '"').replace("\\\\", "\\")
    return json.loads(raw)

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

ref = load("/tmp/ref-arbit-v122.log")
clone = load("/tmp/clone-arbit-v122.log")

# EXACT-QUAD whitelist: (axis, ref value, clone value) — the v116
# documented standing classes (the v122 census must reproduce the
# v116 values EXACTLY).
QUADS = {
    # the seed-count class (the grid childCount)
    ("grid.childCount", 1, 2),
    # the v57/v70b Recurring-wrap class (the card h)
    ("card.h", 200, 230),
    # the v57 DATA-CONDITIONAL class (the footer childCount)
    ("footer.childCount", 1, 2),
    # the v57 wrap class (the badgeRow h) + the superset-chip count class
    ("badgeRow.h", 22, 52),
    ("badgeRow.n", 3, 4),
}

# VALUE-INDEPENDENT axis whitelist: any delta on these axes is a
# documented data class (seed text, the classification-VALUE map, the
# v57 conditional tag form, or the template sub-pixel family).
AXES = {
    # the seed-data class (each site's own footer date)
    "footer.children[0].text",
    # the v57 DATA-CONDITIONAL class's tag form (the reference renders
    # its date-only footer as a DIV; the clone's payment-carrying items
    # render the SPAN pair — the reference's own income card's form)
    "footer.children[0].tag",
    # the classification-VALUE map axes (badge[0]: need-red vs
    # savings-green; badge[2]: active-slate-iconless vs
    # Recurring-green-iconed — value-dependent axes)
    "badges[0].text", "badges[0].border", "badges[0].bg", "badges[0].color",
    "badges[2].text", "badges[2].border", "badges[2].bg", "badges[2].color",
    "badges[2].iconW", "badges[2].iconH",
    # the column template sub-pixel noise (the last-column distribution
    # within the documented 309.328px family)
    "grid.template",
}

identical = 0
doc_deltas = []
new_deltas = []
# the asymmetric-key families: the reference's savings footer carries ONE
# child (its savings item ships no paymentMethod) while the clone's
# carries TWO (the chip) — the missing footer.children[1].* and the extra
# badges[3].* axes are the v57 DATA-CONDITIONAL / superset-chip classes
# BY CONSTRUCTION (the childCount/n deltas themselves are in QUADS).
ASYMMETRIC_DOC = re.compile(
    r"^footer\.children\[1\]\."
    r"|^badges\[3\]\."
)
r = flatten(ref)
c = flatten(clone)
only_r = set(r.keys()) - set(c.keys())
only_c = set(c.keys()) - set(r.keys())
for k in sorted(only_r | only_c):
    if ASYMMETRIC_DOC.match(k):
        doc_deltas.append((k, r.get(k, "<absent>"), c.get(k, "<absent>")))
    else:
        new_deltas.append((k, r.get(k, "<absent>"), c.get(k, "<absent>")))
for k in sorted(set(r.keys()) & set(c.keys())):
    if r[k] == c[k]:
        identical += 1
    elif (k, r[k], c[k]) in QUADS:
        doc_deltas.append((k, r[k], c[k]))
    elif k in AXES:
        doc_deltas.append((k, r[k], c[k]))
    else:
        new_deltas.append((k, r[k], c[k]))

total = identical + len(doc_deltas) + len(new_deltas)
print(f"axes compared: {total} — identical: {identical} — documented-class deltas: {len(doc_deltas)}")
for k, rv, cv in doc_deltas:
    print(f"  {k}: ref {rv!r} vs clone {cv!r} — DOCUMENTED CLASS")
if new_deltas:
    print(f"NEW-DELTA FAILURES ({len(new_deltas)}):")
    for k, rv, cv in new_deltas:
        print(f"  {k}: ref {rv!r} vs clone {cv!r}")
    sys.exit(1)
print("\nNO NEW CLONE GAP — every delta a documented class, the rest byte-identical")
