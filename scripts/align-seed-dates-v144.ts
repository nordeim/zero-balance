// align-seed-dates-v144.ts — align the re-seeded db's rendered dates to the
// canonical persisted-seed state (the Oct 31 stamps the committed screenshots
// document). The fresh-clone re-seed stamped Nov 1 (isoDate(0) = the seed
// day); the canonical db was seeded Oct 31 and persisted through the
// v141..v143 cycles. This script subtracts one day from every DISPLAYED
// date field (budgetItem.date, asset.lastUpdated, liability.lastUpdated,
// expenseLineItem.date) — amounts untouched, the seedcheck contract intact.
import { PrismaClient } from '@prisma/client';

const db = new PrismaClient();

function minusOneDay(iso: string): string {
  const d = new Date(iso + 'T00:00:00Z');
  d.setUTCDate(d.getUTCDate() - 1);
  return d.toISOString().slice(0, 10);
}

async function main() {
  const items = await db.budgetItem.findMany();
  for (const it of items) {
    await db.budgetItem.update({ where: { id: it.id }, data: { date: minusOneDay(it.date) } });
  }
  const assets = await db.asset.findMany();
  for (const a of assets) {
    await db.asset.update({ where: { id: a.id }, data: { lastUpdated: minusOneDay(a.lastUpdated) } });
  }
  const liabilities = await db.liability.findMany();
  for (const l of liabilities) {
    await db.liability.update({ where: { id: l.id }, data: { lastUpdated: minusOneDay(l.lastUpdated) } });
  }
  const lineItems = await db.expenseLineItem.findMany();
  for (const li of lineItems) {
    if (li.date) {
      await db.expenseLineItem.update({ where: { id: li.id }, data: { date: minusOneDay(li.date) } });
    }
  }
  console.log(JSON.stringify({
    items: items.length,
    assets: assets.length,
    liabilities: liabilities.length,
    lineItems: lineItems.length,
    sampleItemDate: (await db.budgetItem.findFirst())?.date,
    sampleAssetLastUpdated: (await db.asset.findFirst())?.lastUpdated,
  }));
  await db.$disconnect();
}

main().catch((e) => { console.error(e); process.exit(1); });
