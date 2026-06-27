# Information Unit Patterns

Use this catalog between whole-screen patterns and input/display elements. A screen pattern defines the total working surface; an information unit pattern defines the repeated blocks inside that surface; the input element catalog defines the atomic controls and displays inside each block.

## Use Order

1. Choose the whole-screen pattern from `screen-pattern-catalog.md`.
2. Break the user's decision into information units.
3. Assign each unit an information shape from `semantic-ui-planning.md`.
4. Choose a unit pattern below for each important unit.
5. Choose the final input/display elements from `input-element-catalog.md`.

## Unit Patterns

### Primary Answer / Result Block

Use when the user first needs the answer, generated result, status conclusion, or decision recommendation.

- Shape: `long_text_summary`, `status`, or `paired_evidence`.
- Contains: claim, confidence/status, short rationale, primary follow-up action.
- Area: large unless the answer is only a table row result.
- Avoid: hiding the answer behind logs, charts, or implementation steps.

### Work History Row

Use when prior requests or jobs must remain scannable.

- Shape: `tabular_records` plus answer preview.
- Contains: request title, answer preview, run state, owner/time, open detail action.
- Area: medium repeated rows.
- Avoid: rows that show only prompts and timestamps.

### Decision Queue Item

Use when the user must approve, reject, assign, escalate, or request changes.

- Shape: `status`, `paired_evidence`, `tabular_records`.
- Contains: decision question, risk/priority, evidence summary, primary decision controls.
- Area: medium; selected item may expand.
- Avoid: making the decision action visually equal to metadata controls.

### Evidence Strip

Use when a claim needs lightweight provenance without opening a full drilldown.

- Shape: `paired_evidence` or `file_collection`.
- Contains: source title, excerpt/metric, freshness, trust marker, open-source action.
- Area: compact to medium.
- Avoid: decorative citations with no inspectable source state.

### Evidence Detail Panel

Use when provenance itself is under review.

- Shape: `paired_evidence`, `audit_log`, `comparison`.
- Contains: source context, extracted evidence, transformation, reviewer note, raw fallback.
- Area: large for audit-heavy screens.
- Avoid: raw logs as the first or only evidence representation.

### Object Header

Use when one object is the screen anchor.

- Shape: `short_text` plus `status`.
- Contains: object name, state, owner, key properties, primary action, destructive/secondary actions.
- Area: compact but visually dominant.
- Avoid: scattering object identity across multiple cards.

### Activity / Timeline Step

Use for sequence, causality, audit, and recovery.

- Shape: `ordered_steps`.
- Contains: actor/role, action, timestamp, input/output link, state, next instruction if relevant.
- Area: medium; expand selected step.
- Avoid: flat log tables when the user needs cause and effect.

### Validation State Block

Use when the user cannot proceed until errors, warnings, permissions, or missing data are resolved.

- Shape: `status`.
- Contains: blocking state, reason, affected field/object, recovery action, retry/undo path.
- Area: medium; top placement if blocking.
- Avoid: only coloring fields red without explaining recovery.

### Requirement Checklist Row

Use for onboarding, setup, import, migration, readiness, or publishing.

- Shape: `status` plus `ordered_steps`.
- Contains: requirement, current state, owner/source, blocking reason, action.
- Area: compact repeated rows.
- Avoid: celebratory setup cards that hide blockers.

### Permission Scope Row

Use for role, tool, OAuth, API, and enterprise access decisions.

- Shape: `status`, `tabular_records`.
- Contains: resource, scope, reason, inherited/overridden state, expiration, allow/deny.
- Area: compact to medium.
- Avoid: toggles without scope, inheritance, and audit note.

### Diff / Change Hunk

Use when the user reviews what changed.

- Shape: `comparison`.
- Contains: before, after, change type, rationale, accept/reject or restore action.
- Area: medium repeated blocks; large for text-heavy changes.
- Avoid: side-by-side panes with no change summary.

### Metric Insight Block

Use when a metric must become an operational decision.

- Shape: `status`, `tabular_records`, `comparison`.
- Contains: metric, movement, baseline, annotation, likely cause, next action.
- Area: medium.
- Avoid: standalone KPI cards that do not answer what changed or what to do.

### Alert Group

Use when many signals must be deduplicated and resolved.

- Shape: `status`, `tabular_records`, `paired_evidence`.
- Contains: severity, group key, count, first/last seen, evidence, owner, acknowledge/resolve.
- Area: medium.
- Avoid: one-card-per-alert views that hide grouping and fatigue.

### Empty State Activation Panel

Use when the product has no data yet and needs a meaningful first action.

- Shape: `status` plus `structured_text`.
- Contains: current absence, why it matters, primary setup action, sample/preview, skip/import path.
- Area: large only when it is the main screen state.
- Avoid: generic illustrations or marketing copy without a next action.

### Communication Thread Block

Use when decisions happen through messages, comments, notes, or handoffs.

- Shape: `ordered_steps`, `structured_text`.
- Contains: participant, message/note, linked object/evidence, action requested, resolution state.
- Area: medium; selected thread can expand.
- Avoid: chat UI when the main task is actually approval, evidence review, or incident control.

## Composition Checks

- Every screen should have one dominant information unit unless the pattern is explicitly comparative or operational.
- Repeated information units should be visually consistent and scannable.
- Large area should go to the unit that carries the user's hardest decision: writing, comparing, verifying, resolving, or recovering.
- Atomic controls should never determine the composition. Choose the unit first, then choose the control.
- If a whole-screen pattern cannot be decomposed into 3-7 meaningful information units, the pattern is probably too vague.
