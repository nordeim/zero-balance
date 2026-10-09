import type { MetadataRoute } from "next";

// v21 G1 (docs/remediation-plan-v21.md): the reference serves /sitemap.xml
// with five URLs — its origin at priority 1.0 and its four app routes at
// 0.8, all changefreq weekly; /login is excluded (measured live). The clone
// mirrors the structure with its own lowercase routes. Authed-only budget
// data is never listed: the sitemap reflects the public surface, and the
// signed-in views sit behind the cookie session anyway.
const siteUrl = process.env.NEXT_PUBLIC_SITE_URL ?? "http://localhost:3000";

export default function sitemap(): MetadataRoute.Sitemap {
  const routes = [
    { path: "/", priority: 1.0 },
    { path: "/income", priority: 0.8 },
    { path: "/savings", priority: 0.8 },
    { path: "/expenses", priority: 0.8 },
    { path: "/networth", priority: 0.8 },
  ];
  return routes.map(({ path, priority }) => ({
    url: `${siteUrl}${path}`,
    // No lastModified: the reference's sitemap carries exactly
    // loc + changefreq + priority (measured live) — a per-build timestamp
    // would drift the file from the reference's shape for no SEO gain.
    changeFrequency: "weekly",
    priority,
  }));
}
