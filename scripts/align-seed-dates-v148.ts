// align-seed-dates-v148.ts — align the re-seeded db's rendered dates to the
// canonical persisted-seed state (the Oct 31 stamps the committed screenshots
// document). The fresh-clone re-seed stamped Nov 3 (isoDate(0) = the seed
// day); the canonical db was seeded Oct 31 and persisted through the
// v141..v147 cycles. This script subtracts THREE days from every DISPLAYED
// date field (budgetItem.date, asset.lastUpdated, liability.lastUpdated,
// expenseLineItem.startDate/endDate) — amounts untouched, the seedcheck
// contract intact. The day-count is auto-computed from the observed seed-day
// (max lastUpdated) against the 2026-10-31 canonical target, so a re-run on
// a different day still converges (idempotent only in the zero-delta case).
// The v145 correction carried forward: the ExpenseLineItem model carries
// startDate/endDate (NOT `date`).
import { PrismaClient } from '@prisma/client';

const db = new PrismaClient();
const CANONICAL_SEED_DAY = '2026-10-31';

function shift(iso: string, days: number): string {
  const d = new Date(iso + 'T00:00:00Z');
  d.setUTCDate(d.getUTCDate() + days);
  return d.toISOString().slice(0, 10);
}

function dayDiff(from: string, to: string): number {
  const a = new Date(from + 'T00:00:00Z').getTime();
  const b = new Date(to + 'T00:00:00Z').getTime();
  return Math.round((b - a) / 86400000);
}

async function main() {
  const assets = await db.asset.findMany();
  const seedDay = assets
    .map((a) => a.lastUpdated)
    .sort()
    .pop();
  if (!seedDay) throw new Error('no assets — seed first');
  const delta = dayDiff(seedDay, CANONICAL_SEED_DAY);
  console.log(`observed seed day ${seedDay}, canonical ${CANONICAL_SEED_DAY}, shift ${delta}d`);
  if (delta === 0) {
    console.log('already canonical — no-op');
    await db.$disconnect();
    return;
  }

  const items = await db.budgetItem.findMany();
  for (const it of items) {
    await db.budgetItem.update({ where: { id: it.id }, data: { date: shift(it.date, delta) } });
  }
  for (const a of assets) {
    await db.asset.update({ where: { id: a.id }, data: { lastUpdated: shift(a.lastUpdated, delta) } });
  }
  const liabilities = await db.liability.findMany();
  for (const l of liabilities) {
    await db.liability.update({ where: { id: l.id }, data: { lastUpdated: shift(l.lastUpdated, delta) } });
  }
  const lineItems = await db.expenseLineItem.findMany();
  for (const li of lineItems) {
    const data: { startDate?: string; endDate?: string } = {};
    if (li.startDate) data.startDate = shift(li.startDate, delta);
    if (li.endDate) data.endDate = shift(li.endDate, delta);
    if (Object.keys(data).length > 0) {
      await db.expenseLineItem.update({ where: { id: li.id }, data });
    }
  }
  console.log(
    JSON.stringify({
      shifted: delta,
      items: items.length,
      assets: assets.length,
      liabilities: liabilities.length,
      lineItems: lineItems.length,
      sampleItemDate: (await db.budgetItem.findFirst({ orderBy: { date: 'asc' } }))?.date,
      sampleAssetLastUpdated: (await db.asset.findFirst())?.lastUpdated,
    }),
  );
  await db.$disconnect();
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
