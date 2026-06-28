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
- In full-scale screens, do concrete artifact names, diff summaries, review criteria, and stop conditions replace abstract placeholder labels?
- In non-AI product screens, does the main full-scale structure match the domain's operational object instead of a generic table, such as incident ledger, receipt exception ledger, booking hold board, weakness map, moderation queue, clinic board, evidence packet, scorecard ledger, or recovery timeline?
- If the full-scale screen came from a flow frame, does the largest region answer that source screen's exact user question, object, and pattern?
- Is a ledger, board, or queue used only when the source screen's job really requires simultaneous comparison of many records?
- Does the product screen answer one dominant user question rather than displaying every rubric proof item?
- Are state variants shown in the product screen only when the real product would show them simultaneously?
- Is the current state's primary action clear, with inactive state-specific actions moved to variant frames, external annotations, or `UI_PLAN.md`?
- Does selected supporting detail show only the evidence needed for the current decision, while full evidence chains and review criteria stay collapsed or external unless the current task is diagnostic review?
- Does the screen avoid asking for the same identity, value, reason, schedule, row, or extracted data more than once?
- Are required details classified by field responsibility before they become controls?
- Are repeated similar items supported by copy, template, bulk-add, import, or generation controls?
- Are exception reasons requested only after exception actions?
- If this is a compressed flow frame, has dense desktop UI been validated separately before judging final font size, row density, editor capacity, inspector width, or above-the-fold controls?
- In full-scale screens, are scroll capacity, folded sections, remaining item counts, and long evidence/timeline behavior visible?
- Is the main region visually dominant over context and inspector regions, instead of presenting equal-strength columns?
- Is the area budget plausible: 50-70% primary decision surface, 15-30% selected support, 0-20% diagnostics, and no raw logs initially unless failure/debug is current?
- Would longer labels, changed data, or a narrower preview break the layout?

## Overexposure Penalties

Penalize overexposed information when:

- more than one dominant user question is visible;
- the largest region answers a different question than the selected source screen;
- rubric evidence is displayed as product UI instead of plan annotation;
- diagnostic details compete with the primary action;
- state variants appear as controls even though they are not available in the current state;
- the screen feels like a system audit sheet rather than a user decision surface.

## Repair Playbook

- Purpose is unclear: rewrite the product thesis, user decision points, primary claim, and main action.
- Element planning is weak: create or repair the UI Element Plan before changing visual styling.
- Pattern is wrong: switch to the right screen pattern before moving boxes.
- Flow causality is weak: reorder screens so the main path moves through required decisions, recovery, and result; move libraries, templates, metrics, settings, or logs into supporting units unless they are the required decision.
- Area budget is wrong: move heavy editors, rubrics, prompts, logs, or evidence review to a wider surface.
- Density is unproven: create a full-scale `1440x1024` screen wireframe before judging tables, timelines, editors, rubrics, evidence review, inspectors, long Japanese labels, or final visual design.
- Data is too abstract: replace generic labels with concrete artifacts, diffs, review criteria, stop conditions, and example evidence records.
- Domain structure is generic: rename and reshape the primary surface around the product's real operational object before tuning spacing.
- Source-screen alignment is wrong: rebuild the full-scale screen from the selected flow frame's question, object, and pattern instead of reusing an app-wide ledger, board, or map.
- State operations are vague: add state variants and state-specific primary actions, such as review, answer, recover, approve, retry, or hand off.
- State variants are overexposed: move inactive states to separate variant frames, state sheets, external annotations, or `UI_PLAN.md`.
- Evidence inspector is thin: show selected input, output, judgment, and next instruction only when they support the current decision; collapse or externalize the full chain when it would compete with the primary action.
- Scroll behavior is unproven: add folded sections, visible scroll track, and remaining count without turning diagnostics into the main surface.
- Rubric proof is overexposed: move secondary proof items out of the product UI and into plan annotations, external notes, or collapsed states.
- Priority is flat: reduce equal-card layouts and create a dominant anchor with quieter supporting regions.
- Gaze path is weak: add meaningful alignment, flow lines, spatial grouping, or a Z/F/center-out structure.
- SVG is decorative: replace ornamental shapes with process lanes, relation lines, status fields, before/after geometry, or bottleneck emphasis.
- Beauty is generic: choose a sharper visual thesis through typography scale, line weight, spacing rhythm, color role, and one recognizable motif.
- Operability is weak: add selected, active, disabled, loading, empty, error, confirmation, or undo state where it affects the user's next step.
- Input friction is high: replace repeated fields or review-only/evidence-only blank inputs with inherited values, same-as controls, extracted-value correction, review blocks, evidence panels, templates, duplicate/bulk-add, or owner handoff.
- Cognitive load is high: remove duplicate labels, shorten copy, group related facts, and let the diagram explain relationships.
- Responsiveness is brittle: reduce text dependence inside narrow shapes, keep stable dimensions, and provide mobile-specific composition when needed.

