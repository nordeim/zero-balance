import type { Metadata } from "next";

// v12 G2 (measured live on the reference): the "/networth" tab title is
// "Networth | ZeroBudget" — the reference's own ONE-WORD spelling
// (measured directly on its live SPA), composed with the root layout's
// "%s | ZeroBudget" template.
export const metadata: Metadata = { title: "Networth" };

export default function NetWorthLayout({ children }: { children: React.ReactNode }) {
  return children;
}
