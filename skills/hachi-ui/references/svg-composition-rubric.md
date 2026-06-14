# SVG Composition Rubric

Use this rubric after generating a screen. Score strictly out of 100. If the score is below 80, redesign the composition and hierarchy before tuning colors or spacing.

## Scorecard

| Item | Points | Strong Result |
|---|---:|---|
| User purpose and context | 15 | The user can tell what to inspect, decide, and do next. |
| Information structure and priority | 15 | Claim, support, detail, and action are clearly layered. |
| Gaze guidance and composition | 15 | The eye moves naturally through the intended sequence. |
| SVG and diagram expression | 15 | SVG expresses structure, relationship, flow, comparison, emphasis, or state. |
| Aesthetic direction and brand character | 10 | The screen has a specific visual thesis and one memorable anchor. |
| Operability and state expression | 10 | Controls, current state, feedback, and risky actions are understandable. |
| Cognitive load and readability | 10 | Meaning is available with little effort and without duplicated explanation. |
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

- What is the user's goal on this screen?
- What is the visual thesis?
- What is the first claim the screen makes?
- What should the user look at second and third?
- Is the screen a composition, or only stacked components?
- Does the SVG carry meaning, or is it decoration?
- Are lines, nodes, grids, arrows, density, and backgrounds used to explain relationships or flow?
- Is there a clear aesthetic direction beyond generic clean UI, generic cards, or decorative chrome?
- Are current state, action priority, disabled/loading/error/empty states, and recovery paths represented when relevant?
- Would longer labels, changed data, or a narrower preview break the layout?

## Repair Playbook

- Purpose is unclear: rewrite the primary claim and move the main action near the decision point.
- Priority is flat: reduce equal-card layouts and create a dominant anchor with quieter supporting regions.
- Gaze path is weak: add meaningful alignment, flow lines, spatial grouping, or a Z/F/center-out structure.
- SVG is decorative: replace ornamental shapes with process lanes, relation lines, status fields, before/after geometry, or bottleneck emphasis.
- Beauty is generic: choose a sharper visual thesis through typography scale, line weight, spacing rhythm, color role, and one recognizable motif.
- Operability is weak: add selected, active, disabled, loading, empty, error, confirmation, or undo state where it affects the user's next step.
- Cognitive load is high: remove duplicate labels, shorten copy, group related facts, and let the diagram explain relationships.
- Responsiveness is brittle: reduce text dependence inside narrow shapes, keep stable dimensions, and provide mobile-specific composition when needed.
