# SVG Composition Rubric

Use this rubric after generating a screen. Score strictly out of 100. If the score is below 80, redesign the composition and hierarchy before tuning colors or spacing.

## Scorecard

| Item | Points | Strong Result |
|---|---:|---|
| User purpose and context | 15 | The user can tell what to inspect, decide, write, verify, or do next. |
| Semantic planning and information structure | 15 | User decisions map to information units, information shapes, suitable elements, evidence, priority, and primary-path causality. |
| Gaze guidance and composition | 15 | The eye moves naturally through the intended sequence. |
| SVG and diagram expression | 15 | SVG expresses structure, relationship, flow, comparison, emphasis, or state. |
| Aesthetic direction and brand character | 10 | The screen has a specific visual thesis and one memorable anchor. |
| Operability and state expression | 10 | Controls, current state, feedback, and risky actions are understandable. |
| Input friction and readability | 10 | Meaning is available with little effort, and required details are split into typed, selected, auto-filled, review-only, exception-only, and evidence/display values instead of being re-entered. |
| Implementation and responsiveness | 10 | The SVG is robust, editable, accessible enough for a prototype, and not over-fixed. |

## Redesign Thresholds

- `90-100`: Suitable for a real product review or proposal.
- `80-89`: Good; fix small details only.
- `70-79`: Direction works, but composition or information hierarchy is weak.
- `60-69`: Looks plausible but still has generic AI UI feel.
- `50-59`: Mostly a list of elements; redesign required.
- `0-49`: Rebuild from purpose and structure.

## Strict Review Questions

Ask these before accepting the screen:

- What is the product thesis and user job on this screen?
- What is the visual thesis?
- What are the user decision points and information units?
- In a flow, does each next screen follow from the prior action, system event, validation result, or recovery condition?
- Do the chosen screen pattern and UI elements match the information shapes?
- What is the first claim the screen makes?
- What should the user look at second and third?
- Is the screen a composition, or only stacked components?
- Does the SVG carry meaning, or is it decoration?
- Are lines, nodes, grids, arrows, density, and backgrounds used to explain relationships or flow?
- Is there a clear aesthetic direction beyond generic clean UI, generic cards, or decorative chrome?
- Are current state, action priority, disabled/loading/error/empty states, and recovery paths represented when relevant?
- Does the screen avoid asking for the same identity, value, reason, schedule, row, or extracted data more than once?
- Are required details classified by field responsibility before they become controls?
- Are repeated similar items supported by copy, template, bulk-add, import, or generation controls?
- Are exception reasons requested only after exception actions?
- If this is a compressed flow frame, has dense desktop UI been validated separately before judging final font size, row density, editor capacity, inspector width, or above-the-fold controls?
- Would longer labels, changed data, or a narrower preview break the layout?

## Repair Playbook

- Purpose is unclear: rewrite the product thesis, user decision points, primary claim, and main action.
- Element planning is weak: create or repair the UI Element Plan before changing visual styling.
- Pattern is wrong: switch to the right screen pattern before moving boxes.
- Flow causality is weak: reorder screens so the main path moves through required decisions, recovery, and result; move libraries, templates, metrics, settings, or logs into supporting units unless they are the required decision.
- Area budget is wrong: move heavy editors, rubrics, prompts, logs, or evidence review to a wider surface.
- Density is unproven: create a full-scale `1440x1024` screen wireframe before judging tables, timelines, editors, rubrics, evidence review, inspectors, long Japanese labels, or final visual design.
- Priority is flat: reduce equal-card layouts and create a dominant anchor with quieter supporting regions.
- Gaze path is weak: add meaningful alignment, flow lines, spatial grouping, or a Z/F/center-out structure.
- SVG is decorative: replace ornamental shapes with process lanes, relation lines, status fields, before/after geometry, or bottleneck emphasis.
- Beauty is generic: choose a sharper visual thesis through typography scale, line weight, spacing rhythm, color role, and one recognizable motif.
- Operability is weak: add selected, active, disabled, loading, empty, error, confirmation, or undo state where it affects the user's next step.
- Input friction is high: replace repeated fields or review-only/evidence-only blank inputs with inherited values, same-as controls, extracted-value correction, review blocks, evidence panels, templates, duplicate/bulk-add, or owner handoff.
- Cognitive load is high: remove duplicate labels, shorten copy, group related facts, and let the diagram explain relationships.
- Responsiveness is brittle: reduce text dependence inside narrow shapes, keep stable dimensions, and provide mobile-specific composition when needed.

