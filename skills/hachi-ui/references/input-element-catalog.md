# Input Element Catalog

Use this catalog after identifying the information shape and user intent in `information-shape-catalog.md`. Choose controls and display elements from input burden, validation needs, density, evidence needs, and recovery risk.

## Input Elements

### Text Input

Use for short names, titles, labels, slugs, and identifiers.

- Shape: `short_text`.
- Needs: placeholder, inline validation, duplicate detection when relevant.
- Avoid for prompts, long descriptions, or multi-part configuration.

### Prompt Composer

Use for new AI work requests or task instructions.

- Shape: `structured_text`.
- Needs: placeholder, examples, submit, disabled/loading, validation, optional attachments.
- Give enough vertical space for real prompts.

### Long Textarea / Markdown Editor

Use for long prose, policies, prompts, or generated text editing.

- Shape: `structured_text` or `long_text_summary`.
- Use wide modal/page when editing burden is high.

### Structured Prompt Editor

Use when prompt has system, user, constraints, variables, examples, or output schema.

- Shape: `structured_text` with sections.
- Prefer tabs/sections over one cramped textarea.

### Rich Document Editor

Use for documents, reports, policies, and proposal-like artifacts.

- Shape: `long_text_summary` or `structured_text`.
- Needs: comments/suggestions, save state, export/share, conflict or lock state.

### Structured Form Group

Use for known fields with required/optional state and dependencies.

- Shape: `short_text`, `status`, or `tabular_records`.
- Needs: section labels, inline errors, dependency warnings, review summary.

### Numeric Input / Stepper

Use for exact amounts, limits, weights, scores, durations, and thresholds.

- Shape: `status` or `rubric_scores`.
- Needs: unit label, min/max, precision, calculated/inherited state when relevant.

### Date / Time Picker

Use for exact dates, deadlines, schedules, expirations, and time windows.

- Shape: `status` or `tabular_records`.
- Needs: timezone, recurrence, conflict state, overdue/expired state when relevant.

### Combobox / Select

Use for choosing one known object from many.

- Avoid when users need multi-select, long text, or exact numeric entry.

### Multi-Select / Token Picker

Use for tags, owners, segments, related objects, permissions, and filters.

- Shape: `tabular_records` or `status`.
- Needs: selected count, clear all, unavailable option state.

### Segmented Control

Use for 2-4 peer modes, not arbitrary values.

### Radio Group

Use for one-of-many decisions where labels and consequences should be visible.

### Checkbox Checklist

Use for independent requirements, setup tasks, or multiple accepted conditions.

### Toggle

Use only for binary on/off state with immediate meaning.

### Editable Table

Use for structured repeated records where inline editing is light to medium.

### Mapping Table

Use for source-to-target field mapping, relationship assignment, and import repair.

- Shape: `comparison` or `tabular_records`.
- Needs: unmapped, suggested, invalid, conflict, preview, commit.

### Rule Builder

Use for trigger/condition/action logic, filters, targeting, and routing.

- Shape: `structured_text`, `comparison`, or `status`.
- Needs: validation, simulation, match count, active/inactive state.

### Permission Scope Matrix

Use for roles, resources, tools, OAuth scopes, and inherited access.

- Shape: `status` or `tabular_records`.
- Needs: inherited/overridden markers, expiration, audit note, save/revert.

### File Upload + File Table

Use for knowledge files or source material.

- Shape: `file_collection`.
- Needs: upload, status, owner, freshness, validation errors.

### Annotation Canvas / Label Palette

Use for spans, regions, nodes, labels, and spatial object selection.

- Shape: `paired_evidence`, `comparison`, or `ordered_steps`.
- Needs: selected item, label list, conflict state, review progress.

### Code / JSON / YAML Editor

Use for structured technical config. Provide validation and format errors.

### Secret / Credential Field

Use for API keys, tokens, passwords, and private connection details.

- Needs: masked value, reveal/copy when appropriate, validation, rotation/reconnect.

### Destructive Confirmation

Use for irreversible or high-risk actions.

- Needs: affected objects, consequence summary, typed confirmation when risk is high, undo when possible.

## Display Elements

### Summary Card

Use for primary result, final answer, brief, or status summary.

### Object Header

Use for object name, state, owner, key properties, and primary action.

### Property List

Use for grouped metadata, settings, ownership, inheritance, and related facts.

### Record Table / Dense List

Use for repeated records that need scanning, filtering, sorting, selection, or bulk action.

### Answer Preview Row

Use in work history when the user needs to see the answer without opening detail.

- Include request title, answer preview, status, time, and open-detail affordance.

### Status Chip / Badge

Use for compact state labels. Keep color semantic and scarce.

### Readiness / Blocker Panel

Use when the user needs to know whether the next action can proceed.

### Vertical Timeline

Use for ordered steps, agent execution, review flow, or audit trail.

### Agent Role Badge

Use to show which agent or role produced a step.

### Input / Output Pair Block

Use to verify transformation from input to output.

### Evidence Strip / Citation Row

Use for lightweight provenance near a claim or recommendation.

### Evidence Detail Panel

Use when provenance, source context, and raw fallback must be inspected.

### Evaluation / Rubric Score Panel

Use when criteria determine whether the result is acceptable.

### Decision Note

Use for organizer, reviewer, or human decision rationale.

### Diff Hunk / Comparison Block

Use when the user must understand before/after or version differences.

### Metric Chart + Insight Panel

Use when values need trend, baseline, anomaly, and next-action context.

### Alert Group

Use for grouped exceptions with severity, owner, evidence, and acknowledge/resolve actions.

### Relationship Graph / Dependency Map

Use when links, lineage, inheritance, or impact must be understood.

### Artifact Card / Artifact Preview

Use for generated output definitions, previews, or saved artifacts.

### Live Preview / Rendered Artifact

Use when edits affect a user-facing result.

### Communication Thread

Use for comments, notes, handoffs, support conversation, and review discussion tied to work objects.

### Collapsed Log Viewer

Use for raw logs after structured evidence; do not make it primary.

### Validation Banner / Error Recovery Block

Use when input is invalid, permissions fail, files are stale, or generation is blocked.

### Empty State Activation Panel

Use when the product has no data and the screen must create a useful first state.

## Mismatch Rules

- Short name in a large editor: use a text input with validation.
- Long prompt in a small input: use a prompt composer or wide editor.
- Long document in a side rail: use a full editor surface.
- Multi-value choice in a toggle: use checklist, multi-select, table, or matrix.
- Exact value in a slider: use numeric input or stepper.
- Rule logic in raw text: use rule builder unless the user explicitly needs code.
- Field mapping in dropdowns only: use mapping table with preview and validation.
- Rubric in generic cards: use rubric table editor.
- Permissions as bare toggles: use permission scope matrix with inheritance and audit note.
- Audit trail as raw logs only: use timeline plus input/output pairs.
- Work history without answer preview: add answer preview rows.
- Source files as chips only: use file table with upload and validation.
- KPI cards without interpretation: add baseline, anomaly, selected point, and next action.
- Error banner without repair: use diagnostic or validation recovery block.
