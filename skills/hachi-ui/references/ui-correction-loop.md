# UI Correction Loop

Use this reference when the user critiques or revises a generated UI. Treat corrections as planning patches before redrawing.

## Purpose

Do not handle corrections as cosmetic tweaks by default. Classify each correction as a pattern, element, hierarchy, area, state, copy, direction, or visual-system issue, then patch the UI Element Plan.

## Correction Classes

```yaml
correction:
  user_text: "3列ではなく2列にしたい"
  class: screen_pattern | element_choice | hierarchy | area_budget | object_model | state | evidence | copy | visual_system | direction
  plan_patch: "Change from three-column dashboard to left pane plus stacked main work surface."
  redraw_scope: whole_screen | region | element | copy_only
```

## Common Corrections

### 3 columns to 2 columns

- Class: screen_pattern + area_budget.
- Patch: remove equal columns; preserve navigation; stack primary work and history in one main surface.
- Redraw: whole screen.

### Add answer preview

- Class: hierarchy + element_choice.
- Patch: add `answer_preview_row` to work history; show request, answer excerpt, status, and open detail.
- Redraw: list rows and detail entry point.

### Remove agent count setting

- Class: speculative_control.
- Patch: remove controls that do not affect the current user decision.
- Redraw: local region.

### Add AI agent auditability

- Class: evidence + screen_pattern.
- Patch: use Agent Execution Trace; include input, output, role, evaluation, organizer decision, next instruction, and collapsed raw logs.
- Redraw: detail screen.

### Move prompt/rubric editing to wide editor

- Class: area_budget + element_choice.
- Patch: use Wide Artifact Editor; use large markdown prompt editor and editable rubric table.
- Redraw: editor surface/modal.

### Screen feels generic or not beautiful

- Class: visual_system + composition.
- Patch: revise visual thesis, surface model, focal anchor, type contrast, and hierarchy before color tuning.
- Redraw: whole screen if focal anchor is weak.

## Patch Before Drawing

For every meaningful correction:

1. Quote or summarize the user correction.
2. Classify the correction.
3. Patch product thesis, object model, pattern, element map, area budget, gaze route, state, or evidence needs.
4. Redraw only the necessary scope.
5. Re-run the relevant rejection checks.

## Rejection Checks

- The correction is implemented literally but the underlying mismatch remains.
- A narrow editor remains narrow after the user says editing is cramped.
- A removed speculative control returns elsewhere.
- Answer preview exists only in detail, not in the history row where the user asked to see it.
- Auditability is represented as raw logs rather than structured evidence.
