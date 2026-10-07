import type { Metadata, Viewport } from "next";
import { ToastProvider } from "@/components/ui/toast";
import "./globals.css";

const siteUrl = process.env.NEXT_PUBLIC_SITE_URL ?? "http://localhost:3000";

// Head parity (docs/remediation-plan-v7.md G8): the reference ships its
// marketing description verbatim, OG + Twitter cards keyed off its origin,
// a canonical link, a web manifest and the apple-mobile-web-app meta set —
// all measured on the live site. The favicon stays the clone's own local
// logo (never hotlink the reference's hosted storage).
const REFERENCE_DESCRIPTION =
  "Your personal zero-budget planner to manage income, savings, and expenses effortlessly. Achieve financial clarity and meet your goals with intuitive tools and a clear net zero overview. Also features a handy Net Worth Calculator.";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: "ZeroBudget",
    template: "%s · ZeroBudget",
  },
  description: REFERENCE_DESCRIPTION,
  manifest: "/manifest.webmanifest",
  icons: { icon: "/zerobalance-logo.png" },
  alternates: { canonical: "/" },
  openGraph: {
    title: "ZeroBudget",
    description: REFERENCE_DESCRIPTION,
    type: "website",
    url: siteUrl,
    siteName: "ZeroBudget",
    images: [{ url: "/zerobalance-logo.png", alt: "ZeroBudget logo" }],
  },
  twitter: {
    card: "summary_large_image",
    title: "ZeroBudget",
    description: REFERENCE_DESCRIPTION,
    images: ["/zerobalance-logo.png"],
  },
  appleWebApp: {
    capable: true,
    statusBarStyle: "black",
    title: "ZeroBudget",
  },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="antialiased">
        <ToastProvider>{children}</ToastProvider>
      </body>
    </html>
  );
}
