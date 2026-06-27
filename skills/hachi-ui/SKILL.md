---
name: hachi-ui
description: Create and autonomously refine wireframe-first, beautiful, editable SVG UI prototype screens for web, mobile, dashboard, SaaS, tool, product, onboarding, AI workflow, admin, settings, and landing-page concepts. Use when the user asks for UI mockups, monochrome wireframes, app flows, initial setup flows, design systems, microinteraction states, high-fidelity screen comps, design variants, SVG screen compositions, or visual product prototypes where semantic UI element planning, screen pattern selection, input/display element selection, direction varianting, screen family continuity, navigation, information hierarchy, gaze guidance, area budgeting, brand character, evidence/provenance modeling, and rubric-based self-review matter.
license: MIT-0
metadata:
  version: "0.1.0"
  openclaw:
    skillKey: hachi-ui
---

# Hachi UI

## Goal

Create useful UI prototypes before making them beautiful. For application work, use the UI semantic design primer before drawing: identify the product thesis, the user's decisions, the information units required for those decisions, the information shape of each unit, the appropriate whole-screen pattern, the appropriate input/display/evidence element for each unit, the area each unit deserves, the gaze route through the screen, and the states or provenance needed for trust.

Start from this plan and a monochrome wireframe, then add visual direction only after the navigation, state, and user decision path are clear. The skill should not merely stack plausible components; it should explain why each element exists, why it uses that control or display form, why the screen pattern fits the object model, and why heavy editing or verification work receives enough space.

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

1. Semantic design primer: for app/product work, read `references/ui-semantic-design-primer.md` to identify objects, user decisions, information units, state, evidence, area budget, and gaze route before choosing components.
2. Product thesis: what this product does differently and what the screen must make inspectable, writable, comparable, or decidable.
3. User job: what the user must understand, decide, write, verify, compare, recover from, or complete.
4. Direction choice: for broad product work, propose or inherit a named direction from `references/direction-varianting.md`.
5. Screen family: for multi-screen products, preserve shared navigation, object model, density, state language, and visual thesis using `references/screen-family-continuity.md`.
6. UI element plan: user decisions, information units, input/view information patterns, information shapes, screen pattern, element mapping, area budget, gaze route, and state/evidence needs.
7. Screen contract: question answered, primary action, secondary actions, state, and next screen.
8. Layout pattern: choose from `references/app-layout-patterns.md` and `references/screen-pattern-catalog.md`; when quality is uncertain, check `references/screen-pattern-quality-audit.md`.
9. Information-unit and input/display elements: classify input/view information with `references/information-shape-catalog.md`, decompose the screen with `references/information-unit-patterns.md`, then choose controls from `references/input-element-catalog.md` based on information shape, input burden, validation, density, and evidence needs.
10. Gaze path: for example F-pattern, Z-pattern, center-out, radial, comparison, or process flow.
11. SVG role: structure, relationship, flow, emphasis, comparison, state, bottleneck, or audit trail.
12. UI language: match the user's language; if the user writes Japanese, use Japanese UI labels and screen notes.
13. Design system thesis: purpose, brand posture, density, trust level, and interaction feel.

## Workflow

1. Identify the product context, audience, primary workflow, product thesis, required screen state, and target viewport. For app/product work, read `references/ui-semantic-design-primer.md` first and use it to extract core objects, user decisions, information units, state, evidence, area budget, and gaze route.
2. For app/product work, read `references/semantic-ui-planning.md`, `references/screen-pattern-catalog.md`, `references/information-shape-catalog.md`, `references/information-unit-patterns.md`, and `references/input-element-catalog.md` before drawing. Create a UI Element Plan that maps user decisions to information units, input/view information patterns, information shapes, whole-screen patterns, unit patterns, UI elements, area budget, gaze route, states, and evidence/provenance needs. If the selected screen pattern feels generic, check `references/screen-pattern-quality-audit.md` and switch to a sharper replacement.
3. For broad product briefs or multi-screen products, read `references/direction-varianting.md` and propose 2-3 named directions when useful. If the user selects one, preserve that direction in subsequent screens.
4. For multi-screen product surfaces, read `references/screen-family-continuity.md` and define a screen family plan: global navigation, core objects, shared density, shared state language, primary evidence model, and relationships between screens.
5. For user-requested revisions, read `references/ui-correction-loop.md` and treat corrections as UI Element Plan patches before redrawing the SVG.
6. For app/product work, read `references/wireframe-first.md` and create a monochrome flow or screen before adding visual styling.
7. For 3-5 screen app flows, onboarding flows, setup flows, and screen sequences, read `references/flow-wireframe-template.md` and use its left-to-right SVG grid unless the user explicitly asks otherwise.
8. Pick the layout pattern from `references/app-layout-patterns.md` and `references/screen-pattern-catalog.md`; decompose the chosen screen with `references/information-unit-patterns.md`; do not default to a left sidebar or split-screen layout unless it fits the user's job.
9. If the request involves signup, import, workspace creation, permissions, first run, or empty product state, read `references/onboarding-flow-patterns.md`.
10. Decide the semantic structure before drawing: product thesis, user decisions, information units, input/view information patterns, information shapes, whole-screen pattern, unit patterns, input/display/evidence elements, claim, evidence, details, actions, recovery paths, and which elements need expanded editing or inspection space.
11. After the wireframe is clear and before high-fidelity styling, read `references/design-system-after-wireframe.md` and define or update a `DESIGN.md` system file using a Claude Design-style source-driven workflow and Google `design.md`-style tokens plus rationale.
12. For landing pages, brand pages, or visually led prototypes, read `references/frontend-art-direction.md` before the high-fidelity pass.
13. Choose a screen composition, then sketch with SVG layers that guide the eye through that hierarchy.
14. Create an SVG file in the workspace. Use `viewBox`, explicit `width` and `height`, `<title>`, and `<desc>`.
15. Build with editable SVG primitives: `rect`, `path`, `circle`, `line`, `text`, `g`, `defs`, and reusable symbols when helpful.
16. Use real UI density and controls: icon buttons, segmented controls, tabs, toggles, sliders, inputs, menus, tables, and status indicators when the screen calls for them.
17. Render or inspect the SVG before delivery. Fix text overflow, overlaps, off-canvas content, illegible contrast, and accidental blank output.
18. Score the result with `references/svg-composition-rubric.md`. If the score is below `80`, redesign from composition and hierarchy first, not by adding polish.
19. Run `python scripts/svg_smoke_check.py path/to/file.svg` when Python is available.

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

- Weak semantic planning: redraw from `ui-semantic-design-primer.md` and the UI Element Plan when the screen merely lists plausible components instead of mapping objects, user decisions, information units, state, evidence, and suitable elements.
- Missing direction choice: for broad product briefs, propose named directions instead of committing to one generic clean SaaS layout.
- Broken screen family continuity: when a follow-up screen ignores a previously selected direction, navigation model, density, or object model, update the screen family plan and redraw.
- Wrong screen pattern: switch pattern when the current layout fights the user's job, such as using a generic dashboard for audit work, a narrow inspector for heavy editing, raw logs for step verification, or a catalog pattern scored below 80 in `screen-pattern-quality-audit.md`.
- Wrong input or viewing pattern: replace the control or display when the information pattern is mismatched, such as using a small input for long prompts, a toggle for multi-value choices, a slider for exact values, generic cards for structured rubric editing, KPI cards without interpretation, or raw logs when a timeline/evidence view is needed.
- Area budget mismatch: move long-form editing, rubric tables, prompts, logs, or evidence review into a wide editor, modal, full page, or dedicated detail surface instead of squeezing them into a narrow side rail.
- Hidden answer: for work-history or AI result screens, show the user's request and the answer preview in the list row or summary area before exposing implementation logs.
- Auditability mismatch: for AI workflow, agent, review, or orchestration screens, show input, output, role, evaluation, decision, and next instruction as inspectable evidence, not only as generic logs.
- Over-specified controls: remove configuration controls that the user did not ask for and that do not affect the current decision, such as unnecessary agent-count settings.
- Wrong editing surface: if the task is heavy writing or rubric editing, use a focused large editor or dialog; if the task is scan/selection, use compact lists and summary rows.
- Correction handled too literally: classify the user's correction as a pattern, element, hierarchy, area, state, copy, or visual-system issue before changing the drawing.
- Broken flow: redraw the screen sequence and transition points before improving any single screen.
- Wrapped app flow: switch to the standard left-to-right flow template and expand the SVG width.
- Missing transition trigger: add explicit action labels to arrows and make the target screen match the action result.
- Unjustified visual system: define the design-system thesis and state model before changing colors, shadows, or typography.
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

Use `references/ui-semantic-design-primer.md` for the background thinking before UI design: object-first modeling, task/decision framing, information unit extraction, state, evidence, area budget, and gaze route; `references/semantic-ui-planning.md` for translating requirements into product thesis, user decisions, information units, information shapes, UI element mapping, gaze route, area budget, and evidence/provenance needs; `references/information-shape-catalog.md` for classifying input information and viewing information patterns before choosing controls; `references/screen-pattern-catalog.md` for selecting whole-screen patterns from the user job, object model, information density, and editing burden; `references/screen-pattern-quality-audit.md` for avoiding weak generic patterns and checking replacements; `references/information-unit-patterns.md` for decomposing screens into primary result, evidence, queue, timeline, validation, permission, diff, metric, alert, empty-state, and communication units; `references/input-element-catalog.md` for choosing controls and display elements from information shape; `references/direction-varianting.md` for proposing and preserving named directions; `references/screen-family-continuity.md` for multi-screen product consistency; `references/ui-correction-loop.md` for applying user corrections as planning patches; `references/wireframe-first.md` for app structure; `references/flow-wireframe-template.md` for stable multi-screen SVG flow layout; `references/app-layout-patterns.md` for screen type selection; `references/onboarding-flow-patterns.md` for initial setup; `references/design-system-after-wireframe.md` for `DESIGN.md` system definition and microinteractions; `references/frontend-art-direction.md` for visually led work; `references/svg-ui-quality.md` for final polish; and `references/svg-composition-rubric.md` for scoring and redesign decisions.

Core checks:

- The semantic design primer has identified core objects, user decisions, information units, state, evidence, area budget, and gaze route before drawing.
- The UI Element Plan maps user decisions to information units, input/view information patterns, information shapes, pattern choice, elements, area budget, and evidence needs.
- The selected layout pattern matches the user job and object model, and weak/generic catalog patterns have been sharpened or replaced.
- The screen contract is clear: question, state, primary action, secondary action, next screen.
- Every transition has an explicit user action, system event, or validation result label.
- UI copy uses the user's language consistently.
- The design system follows product purpose and brand posture, not generic decoration.
- Key microinteraction states are represented where they affect confidence or task completion.
- The first viewport immediately communicates the product, object, workflow, or data state.
- The screen is decomposed into input/view information patterns, whole-screen pattern, information-unit patterns, and atomic input/display elements before drawing.
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





