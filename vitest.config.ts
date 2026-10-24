import { defineConfig } from "vitest/config";
import path from "node:path";

// Unit-test layer for this codebase's pure domain seams (money formatting,
// dashboard math, constants, validation, serializers, rate-limit, the
// db-path resolution contract). Browser/E2E coverage lives in
// tests/e2e/*.spec.ts (Playwright — never picked up by this config, which
// matches *.test.ts only) plus scripts/smoke-test.sh.
export default defineConfig({
  test: {
    include: ["src/**/*.test.ts", "tests/**/*.test.ts"],
    environment: "node",
  },
  resolve: {
    alias: {
      "@": path.resolve(import.meta.dirname, "src"),
    },
  },
});
