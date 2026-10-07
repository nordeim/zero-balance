import { execSync } from "node:child_process";
import { rmSync } from "node:fs";
import path from "node:path";

/**
 * Playwright global setup: guarantee the isolated e2e database exists in a
 * FRESH, deterministic state every run — the specs are order-dependent on
 * the seed's exact arithmetic (dashboard totals, filter counts), so a
 * leftover item from a previously failed run would poison every subsequent
 * run. The database is DELETED, schema-pushed, and re-seeded from scratch.
 *
 * The database lives at <repo>/db/e2e.db (gitignored like every db/*.db).
 * `DATABASE_URL="file:../db/e2e.db"` resolves against prisma/ for the CLI
 * and against the schema anchor at runtime — one file, both tools.
 */
export default function globalSetup(): void {
  const repo = path.resolve(__dirname, "..", "..");
  const env = {
    ...process.env,
    DATABASE_URL: "file:../db/e2e.db",
  } as NodeJS.ProcessEnv;

  // Fresh slate: drop the previous run's database (and its WAL/SHM twins).
  for (const suffix of ["", "-wal", "-shm"]) {
    try {
      rmSync(path.join(repo, "db", `e2e.db${suffix}`), { force: true });
    } catch {
      // already gone
    }
  }

  // Prefer bun (the documented runtime); fall back to npx tsx for npm users.
  const run = (cmd: string) =>
    execSync(cmd, { cwd: repo, env, stdio: "pipe" }).toString();

  try {
    run("bunx prisma db push --skip-generate");
  } catch {
    run("npx prisma db push --skip-generate");
  }
  try {
    run("bun prisma/seed.ts");
  } catch {
    run("npx tsx prisma/seed.ts");
  }
}
