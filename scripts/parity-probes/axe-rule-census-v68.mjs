// v68 F1 — the axe-core RULE-COVERAGE census.
// Enumerates the ACTIVATED rule set (the wcag2a/2aa/21a/21aa tags, the
// a11y.spec.ts gate's TAGS) from a given axe-core bundle, as the WRAPPER
// would run it. Usage: node axe-rule-census-v68.mjs <path-to-axe.js> <label>
//
// axe.js is a UMD-ish IIFE: under require() it attaches `axe` to
// module.exports (verified live — no vm sandbox needed).
import { createRequire } from "node:module";
import { resolve } from "node:path";

const require = createRequire(import.meta.url);
const [, , axePathArg, label] = process.argv;
const axePath = axePathArg ? resolve(process.cwd(), axePathArg) : "";
if (!axePath || !label) {
  console.error("usage: node axe-rule-census-v68.mjs <axe.js> <label>");
  process.exit(1);
}

const TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"];

const axe = require(axePath);
if (!axe || typeof axe.getRules !== "function") {
  console.error("axe global did not attach — bundle load failed");
  process.exit(1);
}

// axe.getRules() returns rule metadata; each rule lists its tags (keyed
// `ruleId`, with an `enabled` field). The ACTIVATED set under the gate's
// withTags filter = rules whose tags intersect TAGS (axe's own tag-matching
// semantics: withTags enables every rule carrying at least one requested
// tag and disables the rest).
const all = axe.getRules();
const activated = [];
for (const rule of all) {
  if (!rule || !rule.ruleId) continue;
  const tags = rule.tags || [];
  if (tags.some((t) => TAGS.includes(t))) {
    activated.push({ id: rule.ruleId, enabled: rule.enabled, tags: tags.filter((t) => TAGS.includes(t)).sort() });
  }
}
activated.sort((a, b) => a.id.localeCompare(b.id));

const out = {
  label,
  axeVersion: axe.version?.version ?? axe.version ?? "unknown",
  totalRules: all.length,
  activatedCount: activated.length,
  activated: activated.map((r) => r.id),
};
console.log(JSON.stringify(out, null, 2));
