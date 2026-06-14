# Frontend Art Direction for SVG Screens

Use this reference for landing pages, websites, demos, concept screens, and other visually led UI prototypes. It adapts the OpenAI `frontend-skill` stance to standalone SVG screen composition.

## Working Model

Start with art direction, not component count.

- Define one visual thesis: mood, material, density, and energy.
- Give each section or region one job and one dominant takeaway.
- Use one strong visual anchor in the first viewport.
- Keep copy short enough to scan quickly.
- Prefer whitespace, alignment, type scale, cropping, and contrast before adding outlines, shadows, or decorative surfaces.

## Landing and Brand Screens

- Make the brand, product, place, or offer unmistakable in the first viewport.
- Use the first viewport as a composed poster, not a centered document.
- Prefer full-bleed or full-canvas visual structure for hero-like screens.
- Keep hero text anchored to a calm area with strong contrast.
- Avoid hero cards, stat strips, logo-cloud filler, pill-heavy decoration, and floating dashboard previews unless the brief explicitly needs them.
- If the first viewport still works after removing the main visual, the visual is too weak.

## Product and App Screens

- Start with the working surface: navigation, workspace, status, task context, filters, tables, charts, or inspector panels.
- Use utility copy: orientation, freshness, scope, status, and action.
- Avoid marketing headlines on operational screens unless the user asks for a launch page.
- Use cards only when the card is the interaction or object being manipulated.
- Prefer layout, lanes, columns, dividers, grouped lists, and meaningful diagram layers over dashboard-card mosaics.

## Visual System

- Use at most two typeface families unless the product has a supplied system.
- Use one accent color by default; add more only for status semantics or an existing brand system.
- Remove decorative shadows, gradients, and icons that do not improve hierarchy or scanning.
- Make one memorable anchor: a diagram motif, crop, geometry, process lane, comparison plane, or data shape.
- For SVG prototypes, treat motion as implied sequence only: use staggered positions, ghost states, arrows, depth, or trails to explain before/after and flow.

## Rejection Checks

Redesign if any of these are true:

- The first impression is a generic SaaS card grid.
- The brand or product disappears if the nav is hidden.
- The screen uses a strong image or diagram but has weak action hierarchy.
- Every section repeats the same mood or claim.
- The screen needs many tiny UI devices to explain itself.
- The design only looks polished because of shadows, gradients, and rounded cards.
