# Input Element Catalog

Use this catalog after identifying information shape. Choose controls and display elements from user burden, validation needs, density, and evidence needs.

## Input Elements

### Prompt Composer

Use for new AI work requests or task instructions.

- Shape: structured_text.
- Needs: placeholder, examples, submit, disabled/loading, validation.
- Give enough vertical space for real prompts.

### Long Textarea / Markdown Editor

Use for long prose, policies, prompts, or generated text editing.

- Shape: structured_text or long_text_summary.
- Use wide modal/page when editing burden is high.

### Structured Prompt Editor

Use when prompt has system, user, constraints, variables, examples, or output schema.

- Shape: structured_text with sections.
- Prefer tabs/sections over one cramped textarea.

### Rubric Table Editor

Use for criteria, weights, thresholds, and scoring rationale.

- Shape: rubric_scores.
- Needs: editable rows, validation, add/remove, dirty/saved state.

### File Upload + File Table

Use for knowledge files or source material.

- Shape: file_collection.
- Needs: upload, status, owner, freshness, validation errors.

### Combobox / Select

Use for choosing one known object from many.

- Avoid when users need multi-select, long text, or exact numeric entry.

### Segmented Control

Use for 2-4 peer modes, not arbitrary values.

### Checkbox Checklist

Use for independent requirements or setup tasks.

### Toggle

Use only for binary on/off state with immediate meaning.

### Editable Table

Use for structured repeated records where inline editing is light to medium.

### Code / JSON / YAML Editor

Use for structured technical config. Provide validation and format errors.

## Display Elements

### Summary Card

Use for primary result, final answer, brief, or status summary.

### Answer Preview Row

Use in work history when the user needs to see the answer without opening detail.

- Include request title, answer preview, status, time, and open-detail affordance.

### Status Chip / Badge

Use for compact state labels. Keep color semantic and scarce.

### Vertical Timeline

Use for ordered steps, agent execution, review flow, or audit trail.

### Agent Role Badge

Use to show which agent or role produced a step.

### Input / Output Pair Block

Use to verify transformation from input to output.

### Evaluation / Rubric Score Panel

Use when criteria determine whether the result is acceptable.

### Decision Note

Use for organizer, reviewer, or human decision rationale.

### Collapsed Log Viewer

Use for raw logs after structured evidence; do not make it primary.

### Artifact Card / Artifact Preview

Use for generated output definitions, previews, or saved artifacts.

### Validation Banner / Error Recovery Block

Use when input is invalid, permissions fail, files are stale, or generation is blocked.

## Mismatch Rules

- Long prompt in a small input: use a wide editor.
- Multi-value choice in a toggle: use checklist, multi-select, or table.
- Exact value in a slider: use numeric input or stepper.
- Rubric in generic cards: use rubric table editor.
- Audit trail as raw logs only: use timeline plus input/output pairs.
- Work history without answer preview: add answer preview rows.
- Source files as chips only: use file table with upload and validation.
