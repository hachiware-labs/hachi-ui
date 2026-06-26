---
name: hachi-ui
description: Create and autonomously refine wireframe-first, beautiful, editable SVG UI prototype screens for web, mobile, dashboard, SaaS, tool, product, onboarding, and landing-page concepts. Use when the user asks for UI mockups, monochrome wireframes, app flows, initial setup flows, design systems, microinteraction states, high-fidelity screen comps, design variants, SVG screen compositions, or visual product prototypes where navigation, information hierarchy, gaze guidance, brand character, and rubric-based self-review matter.
license: MIT-0
metadata:
  version: "0.1.0"
  openclaw:
    skillKey: hachi-ui
---

# Hachi UI

## Goal

Create useful UI prototypes before making them beautiful. For application work, start from a monochrome wireframe and a screen contract, then add visual direction only after the navigation, state, and user decision path are clear. Treat the SVG as a designed screen composition, not a pile of components: it must guide understanding, express structure, and survive self-review before delivery.

## Default Output

When the user does not specify a target, create one primary SVG screen:

- Desktop product screen: `1440x1024`
- Multi-screen app flow: use the standard left-to-right template in `references/flow-wireframe-template.md`.
- Mobile app screen: `390x844`
- Dashboard or operations tool: dense, scannable, restrained UI
- Marketing or brand page: use visual assets only when the user asks for that kind of page

Ask a short clarification only when missing information would materially change the screen, such as platform, brand constraints, or the core workflow. Otherwise make conservative assumptions and state them briefly.

## Design Brief

Before drawing, define these points in scratch notes or the final summary when useful:

1. User job: what the user must understand, decide, or complete.
2. Screen contract: question answered, primary action, secondary actions, state, and next screen.
3. Layout pattern: choose from `references/app-layout-patterns.md`.
4. Gaze path: for example F-pattern, Z-pattern, center-out, radial, comparison, or process flow.
5. SVG role: structure, relationship, flow, emphasis, comparison, state, or bottleneck.
6. UI language: match the user's language; if the user writes Japanese, use Japanese UI labels and screen notes.
7. Design system thesis: purpose, brand posture, density, trust level, and interaction feel.

## Workflow

1. Identify the product context, audience, primary workflow, required screen state, and target viewport.
2. For app/product work, read `references/wireframe-first.md` and create a monochrome flow or screen before adding visual styling.
3. For 3-5 screen app flows, onboarding flows, setup flows, and screen sequences, read `references/flow-wireframe-template.md` and use its left-to-right SVG grid unless the user explicitly asks otherwise.
4. Pick the layout pattern from `references/app-layout-patterns.md`; do not default to a left sidebar or split-screen layout unless it fits the user's job.
5. If the request involves signup, import, workspace creation, permissions, first run, or empty product state, read `references/onboarding-flow-patterns.md`.
6. Decide the information hierarchy before drawing: claim, evidence, details, action, and recovery paths.
7. After the wireframe is clear and before high-fidelity styling, read `references/design-system-after-wireframe.md` and define or update a `DESIGN.md` system file using a Claude Design-style source-driven workflow and Google `design.md`-style tokens plus rationale.
8. For landing pages, brand pages, or visually led prototypes, read `references/frontend-art-direction.md` before the high-fidelity pass.
9. Choose a screen composition, then sketch with SVG layers that guide the eye through that hierarchy.
10. Create an SVG file in the workspace. Use `viewBox`, explicit `width` and `height`, `<title>`, and `<desc>`.
11. Build with editable SVG primitives: `rect`, `path`, `circle`, `line`, `text`, `g`, `defs`, and reusable symbols when helpful.
12. Use real UI density and controls: icon buttons, segmented controls, tabs, toggles, sliders, inputs, menus, tables, and status indicators when the screen calls for them.
13. Render or inspect the SVG before delivery. Fix text overflow, overlaps, off-canvas content, illegible contrast, and accidental blank output.
14. Score the result with `references/svg-composition-rubric.md`. If the score is below `80`, redesign from composition and hierarchy first, not by adding polish.
15. Run `python scripts/svg_smoke_check.py path/to/file.svg` when Python is available.

## Wireframe First

For application screens, make the first pass monochrome unless the user explicitly asks for high-fidelity visual design:

- Use white, black, and grays only.
- Use no shadows, gradients, hero imagery, decorative texture, or brand color.
- Show 3-5 connected screens when the request is about a workflow, setup, or onboarding.
- For sequential flows, use the left-to-right grid in `references/flow-wireframe-template.md`; make the SVG wider instead of wrapping rows.
- Label the primary action, secondary action, back/cancel path, empty state, error state, and confirmation state when relevant.
- Label every transition arrow with the exact trigger, such as a button click, selection change, submit action, OAuth success, validation error, or generation completion.
- Use the user's language for all UI labels and screen notes unless the user requests another locale.
- Keep screen contracts outside the screen frame. They are review annotations, not product UI.
- Do not proceed to high-fidelity styling if the wireframe makes the next user action unclear.

## Design System Pass

After the wireframe proves the flow, define the visual system before styling:

- Base it on product purpose, audience, brand posture, trust level, data density, and interaction risk.
- Choose typography, color roles, spacing rhythm, surface model, corner radius, borders, shadows, icons, charts, and status semantics as one coherent system.
- Create or update a nearby `DESIGN.md` when the user asks for a design system, a high-fidelity pass, reusable brand direction, or multiple related screens.
- Define microinteraction states for primary actions: rest, hover/focus, active, loading, success, error, disabled, undo, and recovery when relevant.
- Show key interaction states as adjacent state fragments, small callouts outside the product UI, or separate state frames. Do not add JavaScript to the SVG.
- Reject styling that is only a nicer version of the wireframe without a product-specific design thesis.

## Autonomous Refinement

Iterate without asking the user when the critique points to objective defects:

- Broken flow: redraw the screen sequence and transition points before improving any single screen.
- Wrapped app flow: switch to the standard left-to-right flow template and expand the SVG width.
- Missing transition trigger: add explicit action labels to arrows and make the target screen match the action result.
- Unjustified visual system: define the design-system thesis and state model before changing colors, shadows, or typography.
- Wrong layout pattern: switch patterns, for example from left sidebar to list-detail, wizard, inbox, canvas, or command center.
- Lazy split layout: remove unnecessary left/right division and use a single focused working surface, top nav, stepper, stacked flow, or full-canvas composition instead.
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
- Avoid splitting the canvas into two large halves by habit. Use split layouts only when two panes must stay visible at the same time for comparison, selection/detail, edit/preview, or configuration/result.
- Do not put instructional copy inside the UI explaining how to use the prototype.
- Do not include JavaScript in the SVG.

## Composition Patterns

- App flow wireframe: 3-5 monochrome screens showing entry, overview, detail, action, and result.
- Setup wizard: progress, requirement, connected service, validation, and done state.
- Left pane workspace: persistent navigation plus a dense working area for repeated use.
- List-detail: objects on the left or center, selected object details and actions on the right.
- Inbox/queue: triage list, priority grouping, selected item, bulk actions, and done state.
- Canvas/diagram: central object or graph plus inspector, toolbar, and state legend.
- Command center: summary, exceptions, decision queue, and supporting table.
- Product dashboard: dominant status summary, supporting diagnostics, clear next action, restrained density.
- Workflow or agent screen: node-link or lane composition that shows sequence, responsibility, bottlenecks, and current state.
- Before/after: split or diagonal comparison with one visual proof point, not two unrelated panels.
- Landing page hero: first viewport makes the product or offer unmistakable and hints at the next section.
- Mobile app: one primary thumb-reachable action, one current state, and fewer simultaneous claims.

## Visual Quality

Use `references/wireframe-first.md` for app structure, `references/flow-wireframe-template.md` for stable multi-screen SVG flow layout, `references/app-layout-patterns.md` for screen type selection, `references/onboarding-flow-patterns.md` for initial setup, `references/design-system-after-wireframe.md` for `DESIGN.md` system definition and microinteractions, `references/frontend-art-direction.md` for visually led work, `references/svg-ui-quality.md` for final polish, and `references/svg-composition-rubric.md` for scoring and redesign decisions.

Core checks:

- The selected layout pattern matches the user job and object model.
- The screen contract is clear: question, state, primary action, secondary action, next screen.
- Every transition has an explicit user action, system event, or validation result label.
- UI copy uses the user's language consistently.
- The design system follows product purpose and brand posture, not generic decoration.
- Key microinteraction states are represented where they affect confidence or task completion.
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

Return the absolute path to each SVG. Include the absolute path to `DESIGN.md` when one was created or updated, the assumed viewport, the main screen state, design-system thesis when a high-fidelity pass was performed, and the final rubric score when a scoring pass was performed.


