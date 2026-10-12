#!/usr/bin/env node
// glyph-diff-v55.mjs — diff the reference vs clone lucide glyph
// dictionaries captured by glyph-audit-v55.sh (per view, per glyph name).
// Reports: MISSING (one side only), IDENTICAL, DRIFTED (shape data differs).
import { readFileSync } from "node:fs";

const refTxt = readFileSync("/tmp/ref-glyphs.txt", "utf8");
const cloneTxt = readFileSync("/tmp/clone-glyphs.txt", "utf8");

const parse = (txt) => {
  const views = {};
  let current = null;
  for (const line of txt.split("\n")) {
    const m = line.match(/^=== (\w+) (\S+): lucide glyph dictionary ===$/);
    if (m) {
      current = m[2];
      views[current] = {};
      continue;
    }
    if (current && line.trim().startsWith('"')) {
      // agent-browser eval output is a JSON-encoded string (possibly
      // doubly-encoded) — unwrap before parsing the dictionary.
      try {
        let v = JSON.parse(line.trim());
        while (typeof v === "string") v = JSON.parse(v);
        if (v && typeof v === "object") views[current] = v;
      } catch {
        /* skip */
      }
    }
  }
  return views;
};

const ref = parse(refTxt);
const clone = parse(cloneTxt);
const allNames = new Set();
for (const v of Object.values(ref)) for (const n of Object.keys(v)) allNames.add(n);
for (const v of Object.values(clone)) for (const n of Object.keys(v)) allNames.add(n);

// Normalize shape strings: sort segments (order of path children is not
// visually meaningful for a diff), canonicalize nothing else.
const norm = (s) => (s || "").split(" || ").sort().join(" || ");

let drifted = 0;
const report = {};
for (const name of [...allNames].sort()) {
  const refViews = Object.entries(ref).filter(([, d]) => d[name]).map(([v]) => v);
  const cloneViews = Object.entries(clone).filter(([, d]) => d[name]).map(([v]) => v);
  if (!refViews.length || !cloneViews.length) {
    report[name] = { status: "ONE-SIDE-ONLY", ref: refViews, clone: cloneViews };
    continue;
  }
  const r = norm(ref[refViews[0]][name]);
  const c = norm(clone[cloneViews[0]][name]);
  if (r === c) {
    report[name] = { status: "IDENTICAL" };
  } else {
    drifted++;
    report[name] = { status: "DRIFTED", refShape: r.slice(0, 130), cloneShape: c.slice(0, 130) };
  }
}

for (const [name, info] of Object.entries(report)) {
  if (info.status === "IDENTICAL") continue;
  console.log(`[ ${info.status} ] ${name}`);
  if (info.status === "DRIFTED") {
    console.log(`   ref  : ${info.refShape}`);
    console.log(`   clone: ${info.cloneShape}`);
  } else {
    console.log(`   ref views: ${info.ref.join(",")} | clone views: ${info.clone.join(",")}`);
  }
}
const identical = Object.values(report).filter((i) => i.status === "IDENTICAL").length;
console.log(`\nTOTAL: ${allNames.size} glyphs · ${identical} identical · ${drifted} drifted · ${Object.values(report).filter((i) => i.status === "ONE-SIDE-ONLY").length} one-side-only`);
