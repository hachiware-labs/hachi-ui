---
name: hachi-ui
description: Create and autonomously refine beautiful, editable SVG UI prototype screens for web, mobile, dashboard, SaaS, tool, product, and landing-page concepts. Use when the user asks for UI mockups, wireframes, high-fidelity screen comps, design variants, SVG screen compositions, or visual product prototypes where information hierarchy, gaze guidance, brand character, and rubric-based self-review matter.
license: MIT-0
metadata:
  version: "0.1.0"
  openclaw:
    skillKey: hachi-ui
---

# Hachi UI

## Goal

Create polished UI prototype screens as standalone SVG files. Treat the SVG as a designed screen composition, not a pile of components: it must guide understanding, express structure, and survive self-review before delivery.

## Default Output

When the user does not specify a target, create one primary SVG screen:

- Desktop product screen: `1440x1024`
- Mobile app screen: `390x844`
- Dashboard or operations tool: dense, scannable, restrained UI
- Marketing or brand page: use visual assets only when the user asks for that kind of page

Ask a short clarification only when missing information would materially change the screen, such as platform, brand constraints, or the core workflow. Otherwise make conservative assumptions and state them briefly.

## Design Brief

Before drawing, define these six points in scratch notes or the final summary when useful:

1. Visual thesis: mood, material, density, and energy in one sentence.
2. User goal: what the user must understand, decide, or complete.
3. First claim: the one thing the screen should communicate immediately.
4. Gaze path: for example F-pattern, Z-pattern, center-out, radial, comparison, or process flow.
5. SVG role: structure, relationship, flow, emphasis, comparison, state, or bottleneck.
6. Interactive surface: what must remain recognizable as controls rather than decorative SVG.

## Workflow

1. Identify the product context, audience, primary workflow, required screen state, and target viewport.
2. Decide the information hierarchy before drawing: claim, evidence, details, action, and recovery paths.
3. For landing pages, brand pages, or visually led prototypes, read `references/frontend-art-direction.md` before drawing.
4. Choose a screen composition, then sketch with SVG layers that guide the eye through that hierarchy.
5. Create an SVG file in the workspace. Use `viewBox`, explicit `width` and `height`, `<title>`, and `<desc>`.
6. Build with editable SVG primitives: `rect`, `path`, `circle`, `line`, `text`, `g`, `defs`, and reusable symbols when helpful.
7. Use real UI density and controls: icon buttons, segmented controls, tabs, toggles, sliders, inputs, menus, tables, and status indicators when the screen calls for them.
8. Render or inspect the SVG before delivery. Fix text overflow, overlaps, off-canvas content, illegible contrast, and accidental blank output.
9. Score the result with `references/svg-composition-rubric.md`. If the score is below `80`, redesign from composition and hierarchy first, not by adding polish.
10. Run `python scripts/svg_smoke_check.py path/to/file.svg` when Python is available.

## Autonomous Refinement

Iterate without asking the user when the critique points to objective defects:

- Purpose mismatch: move or rewrite the primary claim and action so the target user can decide what to do next.
- Weak hierarchy: separate claim, proof, detail, and action into different visual weights.
- Flat card grid: replace same-strength cards with a composition that has one dominant anchor and supporting regions.
- Decorative SVG: convert lines, nodes, shapes, and background layers into visible relationships, flow, comparison, or status.
- Generic AI look: change the visual system, not just colors; adjust density, typography scale, line weight, icon language, and one memorable anchor.
- Poor operability: clarify active, disabled, loading, empty, error, and destructive states where the screen implies them.
- High cognitive load: remove duplicate explanations, shorten labels, and let the SVG carry relationships.

Stop after the first pass that reaches at least `80/100`, unless the user explicitly asks for presentation-grade output; for that target `90/100`.

## SVG Rules

- Keep the SVG self-contained. Do not reference remote images, fonts, scripts, or stylesheets unless the user explicitly provides them and wants them embedded.
- Prefer grouped, named layers with stable IDs, for example `id="sidebar"` or `id="task-table"`.
- Use `<text>` for editable labels. Convert text to paths only if the user requests logo-like typography.
- Use `font-family` fallbacks such as `Inter, Segoe UI, Arial, sans-serif`; do not assume custom fonts exist.
- Keep corner radii at `8` or less for normal UI cards and controls unless a supplied design system says otherwise.
- Avoid decorative blobs, bokeh, one-note palettes, default purple gradients, and oversized hero treatment for operational tools.
- Use SVG for structure, relationship, flow, emphasis, and visual explanation. Do not SVG-encode complex form controls, tables, or keyboard-operated UI when HTML would be the real implementation surface.
- Do not put instructional copy inside the UI explaining how to use the prototype.
- Do not include JavaScript in the SVG.

## Composition Patterns

- Product dashboard: dominant status summary, supporting diagnostics, clear next action, restrained density.
- Workflow or agent screen: node-link or lane composition that shows sequence, responsibility, bottlenecks, and current state.
- Before/after: split or diagonal comparison with one visual proof point, not two unrelated panels.
- Landing page hero: first viewport makes the product or offer unmistakable and hints at the next section.
- Mobile app: one primary thumb-reachable action, one current state, and fewer simultaneous claims.

## Visual Quality

Use `references/frontend-art-direction.md` for visually led work, `references/svg-ui-quality.md` for final polish, and `references/svg-composition-rubric.md` for scoring and redesign decisions.

Core checks:

- The first viewport immediately communicates the product, object, workflow, or data state.
- The most important action is visible and not visually competing with secondary controls.
- Brand, product, or working surface is the loudest signal; navigation is not the only place it appears.
- The gaze naturally moves from claim to supporting proof to action.
- SVG elements explain structure, relationship, or state; they are not only decoration.
- Layout uses whitespace, scale, cropping, alignment, and contrast before adding chrome.
- Text fits inside buttons, tabs, badges, labels, and table cells.
- Repeated controls have consistent dimensions and alignment.
- Color is functional: status, grouping, emphasis, and contrast are intentional.
- The screen has a clear aesthetic direction and one memorable visual anchor.
- The screen looks like a plausible product interface, not a generic decorative mockup.

## Delivery

Return the absolute path to each SVG. Include the assumed viewport, the main screen state, and the final rubric score when a scoring pass was performed.
