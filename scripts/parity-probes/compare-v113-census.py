#!/usr/bin/env python3
"""Compare the v113 both-sides census values axis by axis (ref vs clone).

Reads the saved half logs (/tmp/ref-arbit-v113.log + /tmp/clone-arbit-v113.log),
extracts the three census JSON lines (PART G / PART Q / PART X), and diffs
every leaf axis. Known documented classes are whitelisted:
  - the v77 mechanism class: grid mt [ref 0px vs clone 32px] with the
    rendered gap byte-identical (cardBottom/gridTop/gap);
  - the v66 INVISIBLE class: the shadow's transparent lead-layer count;
  - gridCls: the class-string itself differs by construction (each site's
    own source) — only its rendered consequences are pinned.
"""
import json, re, sys

def load(path):
    text = open(path, encoding="utf-8").read()
    parts = {}
    for name in ("G", "Q", "X"):
        m = re.search(r"=== PART " + name + r"[^\n]*===\n\"(\{.*\})\"", text)
        if not m:
            print(f"FAIL: PART {name} not found in {path}")
            sys.exit(1)
        # the log line is a bash-quoted JSON string
        raw = m.group(1)
        raw = raw.replace('\\"', '"').replace("\\\\", "\\")
        parts[name] = json.loads(raw)
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

ref = load("/tmp/ref-arbit-v113.log")
clone = load("/tmp/clone-arbit-v113.log")

# documented-class whitelist: (axis, ref value, clone value) triples.
# All four delta families below are the v107-documented standing classes
# (the v113 census reproduces the v107 values EXACTLY):
WHITELIST = {
    # the v66 INVISIBLE class: the shadow's transparent lead-layer count
    # (ref 2 leads vs clone 4 — computed-form only, zero visual effect)
    ("Gcard.shadow",
     "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px",
     "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px"),
    # the v61 label lesson: the census finder catches the clone's WRAPPER
    # (400/rgb(10,10,10)) while the ref's is the leaf itself — the clone's
    # LEAF span carries the identical chrome (16px/500/rgb(26,58,46)),
    # pinned green by the v61 F3 pin + the v107 F4 label-leaf pin
    ("Qcards[0].label.color", "rgb(26, 58, 46)", "rgb(10, 10, 10)"),
    ("Qcards[0].label.fw", "500", "400"),
    ("Qcards[1].label.color", "rgb(26, 58, 46)", "rgb(10, 10, 10)"),
    ("Qcards[1].label.fw", "500", "400"),
    ("Qcards[2].label.color", "rgb(26, 58, 46)", "rgb(10, 10, 10)"),
    ("Qcards[2].label.fw", "500", "400"),
    # the v77 mechanism class: explicit mt-8 on the clone vs structural
    # spacing on the ref — rendered geometry byte-identical (checked below)
    ("Qgrid.mt", "0px", "32px"),
    # the class string itself is site-source, never pinned (its rendered
    # consequences byte-identical)
    ("XgridCls", "grid md:grid-cols-3 gap-6", "mt-8 grid grid-cols-1 gap-6 md:grid-cols-3"),
    ("XgridMt", "0px", "32px"),
}

diffs, same = [], 0
for part in ("G", "Q", "X"):
    rf, cf = flatten(ref[part]), flatten(clone[part])
    for axis in sorted(set(rf) | set(cf)):
        rv, cv = rf.get(axis, "<missing>"), cf.get(axis, "<missing>")
        key = f"{part}{axis}"
        if rv == cv:
            same += 1
            continue
        if (key, str(rv), str(cv)) in WHITELIST:
            diffs.append(f"  {key}: ref {rv!r} vs clone {cv!r}  [documented class]")
        else:
            diffs.append(f"  {key}: ref {rv!r} vs clone {cv!r}  [!! UNCLASSIFIED]")

print(f"axes compared: {same + len(diffs)} — identical: {same} — deltas: {len(diffs)}")
for d in diffs:
    print(d)

# hard assertions: the rendered geometry must be byte-identical
assert ref["X"]["cardBottom"] == clone["X"]["cardBottom"] == 1122, "cardBottom drift"
assert ref["X"]["gridTop"] == clone["X"]["gridTop"] == 1462, "gridTop drift"
assert ref["X"]["gap"] == clone["X"]["gap"] == 340, "gap drift"
assert ref["X"]["gridParentMt"] == clone["X"]["gridParentMt"] == "0px"

unclassified = [d for d in diffs if "UNCLASSIFIED" in d]
if unclassified:
    print("\nFAIL: unclassified deltas present")
    sys.exit(1)
print("\nOK: every delta a documented class; rendered geometry byte-identical")
