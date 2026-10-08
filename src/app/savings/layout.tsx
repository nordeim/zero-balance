import type { Metadata } from "next";

// v12 G2 (measured live on the reference): the "/savings" tab title is
// "Savings | ZeroBudget" — composed with the root layout's
// "%s | ZeroBudget" template.
export const metadata: Metadata = { title: "Savings" };

export default function SavingsLayout({ children }: { children: React.ReactNode }) {
  return children;
}
