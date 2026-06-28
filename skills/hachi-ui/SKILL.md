---
name: hachi-ui
description: Create and autonomously refine wireframe-first, beautiful, editable SVG UI prototype screens for web, mobile, dashboard, SaaS, tool, product, onboarding, AI workflow, admin, settings, and landing-page concepts. Use when the user asks for UI mockups, monochrome wireframes, app flows, initial setup flows, design systems, microinteraction states, high-fidelity screen comps, design variants, SVG screen compositions, or visual product prototypes where semantic UI element planning, field responsibility classification, screen pattern selection, input/display element selection, direction varianting, screen family continuity, navigation, information hierarchy, gaze guidance, area budgeting, brand character, evidence/provenance modeling, and rubric-based self-review matter.
license: MIT-0
metadata:
  version: "0.1.0"
  openclaw:
    skillKey: hachi-ui
---

# Hachi UI

## Goal

Create useful UI prototypes before making them beautiful. For application work, use the UI semantic design primer before drawing: identify the product thesis, the user's decisions, the information units required for those decisions, which items are typed/selected/auto-filled/review-only/exception-only/evidence, the information shape of each unit, the appropriate whole-screen pattern, the appropriate input/display/evidence element for each unit, the area each unit deserves, the gaze route through the screen, and the states or provenance needed for trust.

Start from this plan and a monochrome wireframe, then add visual direction only after the navigation, state, and user decision path are clear. The skill should not merely stack plausible components; it should explain why each element exists, why it uses that control or display form, why the screen pattern fits the object model, and why heavy editing or verification work receives enough space.

## Default Output

When the user does not specify a target, create one primary SVG screen:

- Desktop product screen: `1440x1024`
- Multi-screen app flow: use the standard left-to-right template in `references/flow-wireframe-template.md`.
- Full-scale desktop validation screen: `1440x1024`, named like `work-request-composer-1440.svg`, when a flow frame represents a dense desktop surface.
- Mobile app screen: `390x844`
- Dashboard or operations tool: dense, scannable, restrained UI
- Marketing or brand page: use visual assets only when the user asks for that kind of page

For product or app work that should be reusable, create or update the standard artifacts from `references/ui-artifact-workflow.md`: use an existing requirements source when available, create `requirements.md` only when requirements should be preserved and no equivalent durable source exists, use `UI_PLAN.md` as the central semantic plan, use `wireframe-flow.svg` for multi-screen wireframes, and create `DESIGN.md` only after the wireframe is ready for visual design.

Do not treat compressed flow frames as proof that a real desktop screen works. When tables, timelines, editors, rubrics, evidence review, inspectors, dense forms, or long Japanese labels matter, create at least one full-scale screen wireframe before visual design.

Ask a short clarification only when missing information would materially change the screen, such as platform, brand constraints, or the core workflow. Otherwise make conservative assumptions and state them briefly.

## Design Brief

Before drawing, define these points in scratch notes or the final summary when useful:

1. Semantic design primer: for app/product work, read `references/ui-semantic-design-primer.md` to identify objects, user decisions, information units, state, evidence, area budget, and gaze route before choosing components.
2. Artifact set: for reusable app/product work, use `references/ui-artifact-workflow.md` and make `UI_PLAN.md` the planning source of truth.
3. Product thesis: what this product does differently and what the screen must make inspectable, writable, comparable, or decidable.
4. User job: what the user must understand, decide, write, verify, compare, recover from, or complete.
5. Direction choice: for broad product work, propose or inherit a named direction from `references/direction-varianting.md`.
6. Screen family: for multi-screen products, preserve shared navigation, object model, density, state language, and visual thesis using `references/screen-family-continuity.md`.
7. UI element plan: user decisions, information units, input/view information patterns, information shapes, field responsibility classification, screen pattern, element mapping, input friction audit, area budget, gaze route, primary path causality, and state/evidence/recovery needs.
8. Screen contract: question answered, primary action, secondary actions, state, and next screen.
9. Layout pattern: choose from `references/app-layout-patterns.md` and `references/screen-pattern-catalog.md`; when quality is uncertain, check `references/screen-pattern-quality-audit.md`.
10. Information-unit and input/display elements: classify input/view information with `references/information-shape-catalog.md`, decompose the screen with `references/information-unit-patterns.md`, reduce duplicated or repeated input with `references/input-friction-patterns.md`, then choose controls from `references/input-element-catalog.md` based on information shape, validation, density, and evidence needs.
11. Decision surface discipline: for full-scale screens, use `references/decision-surface-discipline.md` to separate always-visible decision surface, selected supporting detail, and collapsed or external diagnostics.
12. Gaze path: for example F-pattern, Z-pattern, center-out, radial, comparison, or process flow.
13. SVG role: structure, relationship, flow, emphasis, comparison, state, bottleneck, or audit trail.
14. UI language: match the user's language; if the user writes Japanese, use Japanese UI labels and screen notes.
15. Design system thesis: purpose, brand posture, density, trust level, and interaction feel.

## Workflow

1. Identify the product context, audience, primary workflow, product thesis, required screen state, and target viewport. For app/product work, read `references/ui-semantic-design-primer.md` first and use it to extract core objects, user decisions, information units, state, evidence, area budget, and gaze route.
2. For reusable app/product work, read `references/ui-artifact-workflow.md` and choose the artifact set. Use `UI_PLAN.md` as the central plan, identify the requirements source first, create `requirements.md` only when the brief should be preserved and no equivalent requirements source exists, and create `DESIGN.md` only after the wireframe is accepted for visual design.
3. For app/product work, read `references/semantic-ui-planning.md`, `references/information-shape-catalog.md`, `references/screen-pattern-catalog.md`, `references/information-unit-patterns.md`, `references/input-friction-patterns.md`, and `references/input-element-catalog.md` before drawing. Create or update `UI_PLAN.md` with user decisions, screen inventory, flow causality, screen information plan, field responsibility matrix, input friction audit, state/recovery, evidence/provenance, and rejected patterns. If the selected screen pattern feels generic, check `references/screen-pattern-quality-audit.md` and switch to a sharper replacement.
4. For broad product briefs or multi-screen products, read `references/direction-varianting.md` and propose 2-3 named directions when useful. If the user selects one, preserve that direction in subsequent screens.
5. For multi-screen product surfaces, read `references/screen-family-continuity.md` and define the screen family plan inside `UI_PLAN.md`: global navigation, core objects, shared density, shared state language, primary evidence model, and relationships between screens.
6. For user-requested revisions, read `references/ui-correction-loop.md` and treat corrections as `UI_PLAN.md` patches before redrawing the SVG.
7. For app/product work, read `references/wireframe-first.md` and create a monochrome flow or screen before adding visual styling.
8. For 3-5 screen app flows, onboarding flows, setup flows, and screen sequences, read `references/flow-wireframe-template.md` and use its left-to-right SVG grid unless the user explicitly asks otherwise. Treat it as flow validation, not final screen density validation.
9. Pick the layout pattern from `references/app-layout-patterns.md` and `references/screen-pattern-catalog.md`; decompose the chosen screen with `references/information-unit-patterns.md`; do not default to a left sidebar or split-screen layout unless it fits the user's job.
10. If the request involves signup, import, workspace creation, permissions, first run, or empty product state, read `references/onboarding-flow-patterns.md`.
11. Decide the semantic structure in `UI_PLAN.md` before drawing: product thesis, user decisions, information units, input/view information patterns, information shapes, field responsibility classification, whole-screen pattern, unit patterns, input friction and reuse strategy, input/display/evidence elements, claim, evidence, details, actions, primary path causality, recovery paths, and which elements need expanded editing or inspection space.
12. If a flow frame represents a dense desktop or mobile screen, read `references/decision-surface-discipline.md`, then create a full-scale `1440x1024` desktop or `390x844` mobile wireframe before high-fidelity styling.
13. After the wireframe is clear and before high-fidelity styling, read `references/design-system-after-wireframe.md` and define or update `DESIGN.md` using a Claude Design-style source-driven workflow and Google `design.md`-style tokens plus rationale.
14. For landing pages, brand pages, or visually led prototypes, read `references/frontend-art-direction.md` before the high-fidelity pass.
15. Choose a screen composition, then sketch with SVG layers that guide the eye through that hierarchy.
16. Create an SVG file in the workspace. Use `viewBox`, explicit `width` and `height`, `<title>`, and `<desc>`.
17. Build with editable SVG primitives: `rect`, `path`, `circle`, `line`, `text`, `g`, `defs`, and reusable symbols when helpful.
18. Use real UI density and controls: icon buttons, segmented controls, tabs, toggles, sliders, inputs, menus, tables, and status indicators when the screen calls for them.
19. Render or inspect the SVG before delivery. Fix text overflow, overlaps, off-canvas content, illegible contrast, and accidental blank output.
20. Score the result with `references/svg-composition-rubric.md`. If the score is below `80`, redesign from composition and hierarchy first, not by adding polish.
21. Run `python scripts/svg_smoke_check.py path/to/file.svg` when Python is available.

## Quick Route

Use the smallest route that can produce a sound screen:

- **Light single screen**: read `ui-semantic-design-primer.md`, create the minimal semantic plan, then use `wireframe-first.md` and the rubric.
- **Normal product/app screen**: read primer, `ui-artifact-workflow.md`, `semantic-ui-planning.md`, `information-shape-catalog.md`, `screen-pattern-catalog.md`, `information-unit-patterns.md`, `input-friction-patterns.md`, `input-element-catalog.md`, create `UI_PLAN.md`, then wireframe.
- **AI, audit, settings, import, approval, or regulated work**: use the normal route plus `screen-pattern-quality-audit.md` and model evidence/provenance explicitly.
- **Multi-screen product flow**: use the normal route plus `screen-family-continuity.md`, `flow-wireframe-template.md`, and onboarding patterns when setup or first run is involved. Add a full-scale `*-1440.svg` screen when density, copy length, tables, editors, timelines, evidence, or review surfaces matter.
- **High-fidelity or brand-sensitive work**: complete the wireframe route first, then read `design-system-after-wireframe.md` and, for visually led screens, `frontend-art-direction.md`.

## Wireframe First

For application screens, make the first pass monochrome unless the user explicitly asks for high-fidelity visual design:

- Use white, black, and grays only.
- Use no shadows, gradients, hero imagery, decorative texture, or brand color.
- Show 3-5 connected screens when the request is about a workflow, setup, or onboarding.
- For sequential flows, use the left-to-right grid in `references/flow-wireframe-template.md`; make the SVG wider instead of wrapping rows.
- Do not judge final desktop density from the compressed flow frames. Create a full-scale `1440x1024` screen wireframe for tables, timelines, prompt editors, rubrics, evidence review, inspectors, dense forms, or long Japanese labels.
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
- Flow frame used as final layout: create a full-scale screen wireframe before judging font size, table density, editor capacity, sidebars, inspectors, line wrapping, or above-the-fold controls.
- Full-scale screen remains abstract: replace placeholder labels with concrete artifacts, diff summaries, review criteria, stop conditions, state variants, and state-specific primary actions.
- Generic full-scale screen outside AI workflows: replace the template table with the product's own operational structure, such as incident ledger, receipt exception ledger, booking hold board, learning weakness map, moderation decision queue, clinic follow-up board, field evidence packet, hiring scorecard ledger, or habit recovery timeline.
- Source-screen mismatch: when a full-scale screen is derived from a flow frame, make the largest region answer that frame's exact user question, object, and pattern; use ledgers, boards, and queues only when the source screen's current job requires multi-record comparison.
- Overexposed full-scale screen: if the screen shows every rubric proof item as product UI, move diagnostic proof to `UI_PLAN.md`, external annotations, variant frames, state sheets, or collapsed diagnostics; keep the product screen focused on one dominant user question.
- Thin evidence inspector: show the selected evidence needed for the current decision; keep full input-to-output-to-judgment chains collapsed, external, or in `UI_PLAN.md` unless the current task is diagnostic review.
- Missing transition trigger: add explicit action labels to arrows and make the target screen match the action result.
- Broken flow causality: reorder screens when a supporting surface such as metrics, saved items, templates, logs, or settings interrupts the user's primary path; make it an optional branch or compact supporting unit unless the user must decide from it.
- Missing recovery visibility: when the plan names empty, invalid, failed, blocked, waiting, abandoned, or missed states, draw the reason and recovery action as visible UI, not only as contract text.
- Repeated input friction: remove fields that ask for already-known, same-as, extracted, review-only, evidence-only, or role-owned values; show the source value with edit/correct/request controls instead.
- Similar item burden: when the user must create many similar rows, tasks, questions, rules, attendees, reminders, or criteria, use templates, duplicate, bulk add, import, or generated sets.
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

Use `references/ui-semantic-design-primer.md` for the background thinking before UI design: object-first modeling, task/decision framing, information unit extraction, state, evidence, area budget, and gaze route; `references/ui-artifact-workflow.md` for identifying the requirements source and deciding when to create `requirements.md`, `UI_PLAN.md`, `wireframe-flow.svg`, `DESIGN.md`, and optional `evaluation.md`; `references/semantic-ui-planning.md` for translating requirements into product thesis, user decisions, information units, information shapes, field responsibility classification, UI element mapping, gaze route, area budget, and evidence/provenance needs; `references/information-shape-catalog.md` for classifying input information and viewing information patterns before choosing screen patterns or controls; `references/screen-pattern-catalog.md` for selecting whole-screen patterns from the user job, object model, information density, and editing burden; `references/screen-pattern-quality-audit.md` for avoiding weak generic patterns and checking replacements; `references/information-unit-patterns.md` for decomposing screens into primary result, evidence, queue, timeline, validation, permission, diff, metric, alert, empty-state, and communication units; `references/input-friction-patterns.md` for avoiding repeated same-meaning input, same-as fields, retyped extracted data, exception reason overuse, role-owned fields, and blank fields for review-only/evidence-only values; `references/input-element-catalog.md` for choosing controls and display elements from information shape; `references/direction-varianting.md` for proposing and preserving named directions; `references/screen-family-continuity.md` for multi-screen product consistency; `references/ui-correction-loop.md` for applying user corrections as planning patches; `references/wireframe-first.md` for app structure; `references/decision-surface-discipline.md` for limiting full-scale screen visibility to the immediate decision surface; `references/flow-wireframe-template.md` for stable multi-screen SVG flow layout; `references/app-layout-patterns.md` for screen type selection; `references/onboarding-flow-patterns.md` for initial setup; `references/design-system-after-wireframe.md` for `DESIGN.md` system definition and microinteractions; `references/frontend-art-direction.md` for visually led work; `references/svg-ui-quality.md` for final polish; and `references/svg-composition-rubric.md` for scoring and redesign decisions.

Core checks:

- The semantic design primer has identified core objects, user decisions, information units, state, evidence, area budget, and gaze route before drawing.
- `UI_PLAN.md` is the source of truth for reusable app/product work, and the SVG matches its screen inventory, information plan, field responsibility matrix, input friction audit, and flow causality.
- The UI Element Plan maps user decisions to information units, input/view information patterns, information shapes, field responsibility, pattern choice, elements, area budget, and evidence needs.
- The input friction audit avoids repeated same-meaning input, retyped extracted data, same-as fields, unnecessary reason fields, and role-owned fields.
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

Return the absolute path to each SVG. Include the absolute path to `UI_PLAN.md` for reusable app/product work, the absolute path to the requirements source when one was used or created, the absolute path to `DESIGN.md` when one was created or updated, the assumed viewport, the main screen state, design-system thesis when a high-fidelity pass was performed, and the final rubric score when a scoring pass was performed.





