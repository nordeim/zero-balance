// align-seed-dates-v144.ts — align the re-seeded db's rendered dates to the
// canonical persisted-seed state (the Oct 31 stamps the committed screenshots
// document). The fresh-clone re-seed stamped Nov 1 (isoDate(0) = the seed
// day); the canonical db was seeded Oct 31 and persisted through the
// v141..v143 cycles. This script subtracts one day from every DISPLAYED
// date field (budgetItem.date, asset.lastUpdated, liability.lastUpdated,
// expenseLineItem.startDate/endDate) — amounts untouched, the seedcheck
// contract intact.
// v145 correction: the ExpenseLineItem model carries startDate/endDate
// (NOT `date` — the v144 cycle committed this script after its typecheck
// gate ran, so the field-name error slipped through; caught by the v145 F0
// baseline chain).
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
    const data: { startDate?: string; endDate?: string } = {};
    if (li.startDate) data.startDate = minusOneDay(li.startDate);
    if (li.endDate) data.endDate = minusOneDay(li.endDate);
    if (Object.keys(data).length > 0) {
      await db.expenseLineItem.update({ where: { id: li.id }, data });
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
