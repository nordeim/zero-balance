import type { ReactNode, SVGProps } from "react";
import { cn } from "@/lib/utils";

// v55 F1 (docs/remediation-plan-v55.md): the reference's OLD lucide glyphs.
//
// The full icon-glyph audit (24 lucide glyphs across the five views + the
// login page, measured live on BOTH sites via scripts/parity-probes/
// glyph-audit-v55.sh + glyph-diff-v55.mjs) found 19 of 24 shared glyphs
// byte-identical — but FOUR glyphs lucide-react 0.525 REDESIGNED since the
// reference's lucide version: piggy-bank, trending-up, search, and mail.
// The reference renders the older geometry everywhere it uses them (the
// nav rail's Savings/Net Worth links, the stat rows, the donut legend,
// the quick actions, the classification chips, the search input, the login
// email input — piggy-sweep-v55.sh measured every surface). The v44
// chevron-swap family: parity is the SHAPE DATA (the path/polyline/rect/
// circle children), which a computed-style census cannot see.
//
// Each component below renders the reference's EXACT svg (the base attrs
// and shape children byte-identical to the live reference DOM captured by
// glyph-exact-v55.sh), mirroring lucide-react's own rendering rules
// (node_modules/lucide-react/dist/esm/Icon.js): the class prefix
// `lucide lucide-<name>` merged with the caller's className (the class is
// part of the reference's DOM — the e2e pins select svg.lucide-*), and
// aria-hidden="true" unless the caller passes an a11y prop (aria-*/role/
// title). Callers pass only className/style/aria-hidden — the SVGProps
// spread lets width/strokeWidth/style override the defaults like lucide.

type IconProps = SVGProps<SVGSVGElement>;

function hasA11yProp(props: IconProps): boolean {
  return Object.keys(props).some(
    (k) => k.startsWith("aria-") || k === "role" || k === "title",
  );
}

function makeLegacyIcon(name: string, children: ReactNode) {
  function LegacyIcon({ className, color, ...props }: IconProps) {
    return (
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width={24}
        height={24}
        viewBox="0 0 24 24"
        fill="none"
        stroke={color ?? "currentColor"}
        strokeWidth={2}
        strokeLinecap="round"
        strokeLinejoin="round"
        className={cn(`lucide lucide-${name}`, className)}
        {...(hasA11yProp(props) ? {} : { "aria-hidden": "true" })}
        {...props}
      >
        {children}
      </svg>
    );
  }
  return LegacyIcon;
}

/** The reference's piggy-bank (the savings family's every surface): the
 *  OLD 3-path body — lucide 0.525 redesigned it into a leg-integrated
 *  body curve. Measured live: the body path + the front leg + the eye. */
export const PiggyBankIcon = makeLegacyIcon(
  "piggy-bank",
  <>
    <path d="M19 5c-1.5 0-2.8 1.4-3 2-3.5-1.5-11-.3-11 5 0 1.8 0 3 2 4.5V20h4v-2h3v2h4v-4c1-.5 1.7-1 2-2h2v-4h-2c0-1-.5-1.5-1-2V5z" />
    <path d="M2 9v1c0 1.1.9 2 2 2h1" />
    <path d="M16 11h.01" />
  </>,
);

/** The reference's trending-up: the OLD two-POLYLINE glyph — the redesign
 *  re-expressed it as two paths. Measured live on the reference's stat
 *  rows, its breakdown net row, its networth trend icons, and its nav
 *  rail's Net Worth link. */
export const TrendingUpIcon = makeLegacyIcon(
  "trending-up",
  <>
    <polyline points="22 7 13.5 15.5 8.5 10.5 2 17" />
    <polyline points="16 7 22 7 22 13" />
  </>,
);

/** The reference's search: the circle + the OLD handle (the redesign
 *  lengthened it 4.3 → 4.34). Measured live on the items-view search
 *  input (20×20, gray). */
export const SearchIcon = makeLegacyIcon(
  "search",
  <>
    <circle cx="11" cy="11" r="8" />
    <path d="m21 21-4.3-4.3" />
  </>,
);

/** The reference's mail: the rect + the OLD envelope flap (the redesign
 *  re-tuned the arc — a1.94 1.94 → a2 2). Measured live on the login
 *  page's email input icon. */
export const MailIcon = makeLegacyIcon(
  "mail",
  <>
    <rect width="20" height="16" x="2" y="4" rx="2" />
    <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7" />
  </>,
);
