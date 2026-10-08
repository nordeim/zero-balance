"use client";

import * as React from "react";
import * as LabelPrimitive from "@radix-ui/react-label";
import { cn } from "@/lib/utils";

function Label({
  className,
  ...props
}: React.ComponentProps<typeof LabelPrimitive.Root>) {
  return (
    <LabelPrimitive.Root
      data-slot="label"
      // The reference's field labels are the plain shadcn-v1 form —
      // `text-sm font-medium leading-none` on an INLINE element. The inline
      // glyph box (rect h 16 on 14px text) is what produces its 12px
      // label→input gap under the same space-y-2 wrapper; the v4-shadcn
      // `flex items-center gap-2` form rendered flex boxes (h 14) with an
      // 8px gap (plan v9 G3). The classification-tile Label re-adds its own
      // flex layout via className.
      className={cn(
        "text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
        className,
      )}
      {...props}
    />
  );
}

export { Label };
