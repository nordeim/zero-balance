import type { MetadataRoute } from "next";

// v21 G1 (docs/remediation-plan-v21.md): the reference serves /robots.txt as
// a two-line allow-all + Sitemap link (measured live). Self-hosted parity:
// crawlers may fetch everything (the app's budget data is behind the cookie
// session regardless) and the sitemap link points at this origin's
// /sitemap.xml — keyed off NEXT_PUBLIC_SITE_URL exactly like the root
// layout's metadataBase so canonical robots/sitemap/metadata all agree.
const siteUrl = process.env.NEXT_PUBLIC_SITE_URL ?? "http://localhost:3000";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: "*", allow: "/" },
    sitemap: `${siteUrl}/sitemap.xml`,
  };
}
