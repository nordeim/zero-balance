"use client";

import * as React from "react";
import Link from "next/link";
import { HomeIcon } from "lucide-react";

// Custom 404 — the reference's not-found surface (docs/remediation-plan-v7.md
// G7), replacing Next's default "This page could not be found." card. Every
// slate value is an arbitrary-hex pin of the reference's computed styles
// (v4 computes named slates in Lab): 50 #f8fafc · 200 #e2e8f0 · 300 #cbd5e1
// · 600 #475569 · 700 #334155 · 800 #1e293b.
//
// The path inside the message (and the tab title) is read client-side from
// window.location — Next renders not-found.tsx without handing it the
// unmatched path. Lazy useState init + suppressHydrationWarning keeps the
// static prerender (empty span) and the hydrated render (real path) from
// tripping React's mismatch warning.

function titleFromPath(pathname: string): string {
  const segment = pathname.split("/").filter(Boolean).pop() ?? "";
  const cased = segment
    .split(/[-_]+/)
    .filter(Boolean)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
  return `${cased || "Not Found"} | ZeroBudget`;
}

export default function NotFound() {
  // The reference quotes the path WITHOUT its leading slash ("nonexistent-
  // page-xyz", not "/nonexistent-page-xyz").
  const [path] = React.useState(() =>
    typeof window === "undefined" ? "" : window.location.pathname.replace(/^\/+/, ""),
  );

  React.useEffect(() => {
    // The reference sets a path-aware tab title ("Nonexistent Page Xyz |
    // ZeroBudget") — a plain DOM side effect, no state.
    document.title = titleFromPath(window.location.pathname);
  }, []);

  return (
    <div className="flex min-h-screen items-center justify-center bg-[#f8fafc] p-6">
      <div className="w-full max-w-md">
        <div className="space-y-6 text-center">
          <div className="space-y-2">
            <h1 className="text-7xl font-light text-[#cbd5e1]">404</h1>
            <div className="mx-auto h-0.5 w-16 bg-[#e2e8f0]" />
          </div>
          <div className="space-y-3">
            <h2 className="text-2xl font-medium text-[#1e293b]">Page Not Found</h2>
            <p className="leading-relaxed text-[#475569]">
              The page <span className="font-medium text-[#334155]" suppressHydrationWarning>&quot;{path}&quot;</span> could
              not be found in this application.
            </p>
          </div>
          <div className="pt-6">
            <Link
              href="/"
              className="inline-flex items-center rounded-lg border border-[#e2e8f0] bg-white px-4 py-2 text-sm font-medium text-[#334155] transition-colors duration-200 hover:border-[#cbd5e1] hover:bg-[#f8fafc] focus-visible:ring-2 focus-visible:ring-[#94a3b8] focus-visible:ring-offset-2 focus-visible:outline-none"
            >
              <HomeIcon className="mr-2 h-4 w-4" aria-hidden="true" />
              Go Home
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
