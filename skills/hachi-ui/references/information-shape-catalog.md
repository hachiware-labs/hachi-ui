# Information Shape Catalog

Use this catalog before choosing information-unit patterns or atomic controls. It separates what the user wants to input from what the user wants to view, because the same data can need different UI treatment when it is written, scanned, verified, compared, or recovered.

## Classification Questions

For each information unit, answer:

1. Is the user entering, selecting, editing, reviewing, verifying, comparing, or recovering this information?
2. Is the information free-form, structured, repeated, ordered, relational, evidential, numeric, temporal, or stateful?
3. Does the user need speed, accuracy, auditability, comparison, confidence, or recovery?
4. Does the information deserve inline treatment, a wide editor, a table, a drilldown, a graph, or a separate flow?

## Canonical Slugs

Use these slugs in UI Element Plans as `shape_pattern`.

| Pattern | Slug |
|---|---|
| Identifier / Naming Input | `identifier_naming_input` |
| Natural Language Request Input | `natural_language_request_input` |
| Long-Form Authoring Input | `long_form_authoring_input` |
| Structured Form Input | `structured_form_input` |
| Rule / Condition / Action Input | `rule_condition_action_input` |
| Choice / Classification Input | `choice_classification_input` |
| Numeric / Threshold / Amount Input | `numeric_threshold_amount_input` |
| File / Source Input | `file_source_input` |
| Mapping / Relationship Input | `mapping_relationship_input` |
| Permission / Scope Input | `permission_scope_input` |
| Annotation / Spatial Input | `annotation_spatial_input` |
| Credential / Secret Input | `credential_secret_input` |
| Confirmation / Destructive Input | `confirmation_destructive_input` |
| Object Summary View | `object_summary_view` |
| Dense Record View | `dense_record_view` |
| Detail Property View | `detail_property_view` |
| Status / Readiness View | `status_readiness_view` |
| Timeline / Audit View | `timeline_audit_view` |
| Evidence / Provenance View | `evidence_provenance_view` |
| Comparison / Diff View | `comparison_diff_view` |
| Metric / Trend View | `metric_trend_view` |
| Alert / Exception View | `alert_exception_view` |
| Relationship / Dependency View | `relationship_dependency_view` |
| Preview / Rendered Artifact View | `preview_rendered_artifact_view` |
| Communication / Thread View | `communication_thread_view` |
| Diagnostic / Validation View | `diagnostic_validation_view` |
| Empty / First-Run View | `empty_first_run_view` |

## Input Information Patterns

### Identifier / Naming Input

Use for names, titles, slugs, labels, owners, and short descriptors.

- Shape: `short_text`.
- Prefer: text input, inline validation, duplicate detection, generated suggestion.
- Avoid: long textareas or generic cards.
- States: empty, duplicate, invalid characters, generated, manually edited.

### Natural Language Request Input

Use for task requests, AI prompts, instructions, questions, and search-like intent capture.

- Shape: `structured_text`.
- Prefer: prompt composer, examples, attachments, submit action, running state.
- Avoid: single-line inputs when the request can contain context or constraints.
- States: draft, missing context, submitted, running, failed, answer ready.

### Long-Form Authoring Input

Use for documents, policies, proposals, markdown, long prompts, and generated text editing.

- Shape: `structured_text` or `long_text_summary`.
- Prefer: wide editor, document surface, comments, save state, preview/export.
- Avoid: narrow right rails and cramped modals.
- States: dirty, saved, conflicted, locked, exported, deleted.

### Structured Form Input

Use for known fields with validation, sections, required/optional state, and dependencies.

- Shape: `tabular_records`, `short_text`, `status`.
- Prefer: grouped fields, inline validation, dependency notices, review summary.
- Avoid: one huge form with no hierarchy or recovery path.
- States: incomplete, invalid, valid, saved, server rejected.

### Rule / Condition / Action Input

Use for automations, targeting, filters, routing, permissions, and policy logic.

- Shape: `structured_text`, `comparison`, `status`.
- Prefer: rule builder, condition rows, simulation preview, test result.
- Avoid: raw JSON unless the user is explicitly technical and validation is shown.
- States: invalid rule, zero matches, test passed, test failed, active, paused.

### Choice / Classification Input

Use when the user assigns a category, label, judgment, status, or decision.

- Shape: `status` or `tabular_records`.
- Prefer: radio group, segmented control, label palette, decision buttons, reason note.
- Avoid: toggles for more than two meanings.
- States: unclassified, selected, conflicted, skipped, reviewed.

### Numeric / Threshold / Amount Input

Use for budgets, limits, quantities, scores, weights, dates, durations, and thresholds.

- Shape: `status`, `rubric_scores`, `tabular_records`.
- Prefer: numeric input, stepper, date/time picker, unit label, min/max validation.
- Avoid: sliders when exact values matter.
- States: out of range, estimated, exact, inherited, calculated, overridden.

### File / Source Input

Use for uploads, imports, knowledge files, attachments, evidence, and source material.

- Shape: `file_collection`.
- Prefer: upload zone, file table, processing state, owner/freshness, validation errors.
- Avoid: chips-only source lists.
- States: uploading, processing, indexed, stale, invalid, duplicate, removed.

### Mapping / Relationship Input

Use when connecting source fields to target fields, linking objects, assigning dependencies, or building lineage.

- Shape: `comparison`, `tabular_records`, `paired_evidence`.
- Prefer: mapping table, relationship picker, dependency graph with selected detail.
- Avoid: plain dropdown lists when many relationships must be checked together.
- States: unmapped, invalid mapping, conflict, suggested, confirmed, removed.

### Permission / Scope Input

Use for roles, tool permissions, OAuth scopes, data access, and enterprise controls.

- Shape: `status`, `tabular_records`.
- Prefer: permission matrix, scope rows, inherited markers, expiration, audit note.
- Avoid: bare toggles without reason, scope, or inheritance.
- States: inherited, overridden, pending, denied, expired, approved.

### Annotation / Spatial Input

Use when the user selects regions, spans, nodes, objects, or coordinates.

- Shape: `paired_evidence`, `comparison`, `ordered_steps`.
- Prefer: canvas, label palette, selected object inspector, keyboardable list fallback.
- Avoid: visual-only selection with no state or review list.
- States: selected, unlabeled, conflict, invalid edge, skipped, accepted.

### Credential / Secret Input

Use for API keys, tokens, passwords, and private connection details.

- Shape: `status`.
- Prefer: secret field, reveal/copy controls, validation, rotation/reconnect action.
- Avoid: showing secrets as normal text or mixing them with low-risk settings.
- States: missing, invalid, expired, connected, rotating, revoked.

### Confirmation / Destructive Input

Use when the user confirms irreversible or high-risk changes.

- Shape: `status` and `comparison`.
- Prefer: consequence summary, affected objects, typed confirmation when risk is high, undo if possible.
- Avoid: generic yes/no dialogs.
- States: pending, blocked, confirmed, cancelled, undo available, irreversible.

## Viewing Information Patterns

### Object Summary View

Use when one object must be understood quickly before action.

- Shape: `short_text`, `status`, `tabular_records`.
- Prefer: object header, key properties, owner, state, primary action.
- Avoid: scattering identity and state across unrelated cards.
- States: active, archived, stale, locked, missing owner.

### Dense Record View

Use for many repeated records that must be scanned, filtered, selected, or bulk edited.

- Shape: `tabular_records`.
- Prefer: table/list, filters, sorting, selected count, row preview, bulk review.
- Avoid: card grids when comparison density matters.
- States: loading, empty, filtered zero, selected, partial failure.

### Detail Property View

Use for inspecting attributes, metadata, ownership, and related facts.

- Shape: `tabular_records`, `short_text`, `status`.
- Prefer: property list, grouped sections, edit affordance, related records.
- Avoid: long ungrouped key/value dumps.
- States: inherited, overridden, stale, missing, locked.

### Status / Readiness View

Use when the user needs to know whether something can proceed.

- Shape: `status`.
- Prefer: readiness summary, blockers, warnings, recovery action, timestamp.
- Avoid: color-only status chips.
- States: ready, blocked, warning, validating, unknown, recovered.

### Timeline / Audit View

Use for ordered events, workflow steps, execution traces, and historical accountability.

- Shape: `ordered_steps` or `audit_log`.
- Prefer: timeline, actor/role, input/output link, decision note, expandable raw log.
- Avoid: raw logs as the primary representation.
- States: running, failed, skipped, retried, reviewed, resolved.

### Evidence / Provenance View

Use when the user must trust where a claim, result, or recommendation came from.

- Shape: `paired_evidence`, `file_collection`.
- Prefer: evidence strip, evidence detail panel, source freshness, confidence, raw fallback.
- Avoid: decorative citations with no inspectable source.
- States: verified, missing, stale, conflicting, low confidence.

### Comparison / Diff View

Use when the user must understand differences between versions, options, or before/after states.

- Shape: `comparison`.
- Prefer: diff hunks, change summary, accept/reject/restore controls, conflict markers.
- Avoid: two panes without highlighting what changed.
- States: added, removed, changed, no change, conflict, restored.

### Metric / Trend View

Use when numbers need interpretation over time, segment, or baseline.

- Shape: `status`, `comparison`, `tabular_records`.
- Prefer: chart, baseline, annotation, selected point detail, likely cause, next action.
- Avoid: disconnected KPI cards without context.
- States: loading, anomaly, normal, missing data, forecast, threshold crossed.

### Alert / Exception View

Use when signals must be grouped, prioritized, acknowledged, and resolved.

- Shape: `status`, `paired_evidence`, `tabular_records`.
- Prefer: grouped alerts, severity, owner, evidence, acknowledge/resolve controls.
- Avoid: one alert per card when grouping is necessary.
- States: new, acknowledged, suppressed, escalated, resolved.

### Relationship / Dependency View

Use when the main task is understanding links, lineage, impact, or inheritance.

- Shape: `comparison`, `tabular_records`, `paired_evidence`.
- Prefer: graph/lane map, selected node detail, relationship type, upstream/downstream, impact summary.
- Avoid: decorative graphs without selectable consequences.
- States: selected, missing link, cycle, conflict, impacted, isolated.

### Preview / Rendered Artifact View

Use when generated or edited content must be inspected as the user will consume it.

- Shape: `long_text_summary`, `comparison`, `status`.
- Prefer: live preview, stale-preview marker, export/share action, responsive state if relevant.
- Avoid: preview that is visually impressive but not connected to editing state.
- States: draft, stale, valid, invalid, exported, published.

### Communication / Thread View

Use when decisions or support happen through messages, comments, notes, or handoffs.

- Shape: `ordered_steps`, `structured_text`.
- Prefer: thread, linked object/evidence, requested action, owner, resolution state.
- Avoid: chat UI when the conversation is secondary to approval or evidence review.
- States: unread, waiting, assigned, action requested, resolved.

### Diagnostic / Validation View

Use when the user must repair invalid data, configuration, permission, or workflow state.

- Shape: `status`, `tabular_records`, `comparison`.
- Prefer: issue list, affected object, severity, suggested fix, apply/retry/undo.
- Avoid: error banners that do not say what to fix.
- States: blocking, warning, suggested, applied, retried, reverted.

### Empty / First-Run View

Use when there is no data yet and the UI must create a useful first state.

- Shape: `status`, `structured_text`.
- Prefer: activation panel, sample data, import/create action, skip path.
- Avoid: generic empty illustrations with no product-specific next action.
- States: empty, sample loaded, setup started, skipped, activated.

## Mapping Rule

A strong UI Element Plan should usually contain both sides:

```yaml
information_units:
  - id: source_files
    user_intent: input
    shape_pattern: file_source_input
    unit_pattern: evidence_strip
    element: file_upload_file_table
  - id: verification_history
    user_intent: view
    shape_pattern: timeline_audit_view
    unit_pattern: activity_timeline_step
    element: vertical_timeline
```

If the plan says only `table`, `card`, `form`, `modal`, or `dashboard`, the information pattern has not been identified yet.
