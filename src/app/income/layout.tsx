import type { Metadata } from "next";

// v12 G2 (measured live on the reference): the "/income" tab title is
// "Income | ZeroBudget" — composed with the root layout's "%s | ZeroBudget"
// template. The reference's SPA sets its titles client-side after
// navigation; static segment metadata reaches the identical observable
// state (the title ships in the prerendered HTML — no hydration race).
export const metadata: Metadata = { title: "Income" };

export default function IncomeLayout({ children }: { children: React.ReactNode }) {
  return children;
}
