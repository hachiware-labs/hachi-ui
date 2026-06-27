# Screen Pattern Catalog

Use this catalog with `app-layout-patterns.md` when a product screen needs a more specific whole-screen pattern than a generic sidebar, dashboard, or split view.

## Selection Inputs

Choose from:

- user job: request, inspect, edit, compare, verify, approve, configure, recover;
- core object: Work, Run, AgentStep, Domain, File, Artifact, Account, Ticket, Item;
- information density: sparse, moderate, dense, archival;
- editing burden: none, light, structured, long-form, table-heavy;
- verification burden: none, evidence, audit, approval, regulated;
- state complexity: simple, workflow, multi-agent, multi-stage, error-prone.

## Patterns

### Work Intake + History Stack

Use when the user creates new work and reviews all prior work in one place.

- Structure: composer, submit action, history list, answer preview rows, status chips.
- Good for: AI work requests, batch jobs, support tasks, report generation.
- Required: empty state, running state, completed row, failed row, answer preview.
- Avoid: three-column dashboards and speculative controls unrelated to the work request.

### Agent Execution Trace

Use when the user verifies what agents did and whether each step is trustworthy.

- Structure: final answer, verification status, vertical timeline, input/output pairs, review/evaluation panels, organizer decision, collapsed raw logs.
- Good for: AI workflows, orchestrators, review chains, audit tools.
- Required: role, input, output, evaluation, decision, next instruction.
- Avoid: raw log viewer as the primary screen.

### Domain Knowledge Workspace

Use when users manage domains, knowledge files, artifact specs, rubrics, and prompts.

- Structure: domain list, selected domain detail, file table with upload, artifact summary list, edit actions.
- Good for: knowledge bases, agent configuration, generation systems.
- Required: selected domain, file state, artifact state, validation.
- Avoid: four equal panes that starve prompt/rubric editing.

### Wide Artifact Editor / Full Editor Surface

Use for heavy writing, long prompts, structured rubrics, large markdown, YAML, JSON, or code-like editing.

- Structure: large editor, structured metadata, validation banner, save/cancel/delete, dirty/saved state.
- Good for: prompt editor, rubric table, long form, policy editor.
- Required: dirty, saved, invalid, locked, deleting.
- Avoid: narrow right rail editors.

### Review / Approval Queue

Use when the user must process items and decide approve, reject, request changes, or escalate.

- Structure: queue, priority, selected item, evidence, decision controls, next item.
- Required: assigned, blocked, bulk selected, done.

### Evidence Drilldown

Use when the main claim is visible but provenance must be inspectable.

- Structure: claim summary, evidence list, selected evidence detail, source metadata, raw source fallback.
- Required: selected evidence, missing evidence, stale evidence.

### Comparison / Diff Review

Use when the user chooses between versions or validates changes.

- Structure: before/after, diff annotations, change summary, accept/reject controls.
- Required: added/removed/changed, conflict, no-change.

### Knowledge Library

Use when browsing, uploading, tagging, and validating knowledge assets.

- Structure: filters, file table, upload zone, selected file details, validation state.

### Search Results + Preview

Use when the main task is finding and inspecting objects quickly.

- Structure: query, filters, result list, preview, highlighted match, empty state.

### Command Center

Use when status, anomalies, and decisions must be visible at once.

- Structure: summary, flow or anomaly visualization, decision queue, evidence table.

### Canvas + Inspector

Use when spatial relationships matter.

- Structure: canvas, toolbar, selected object, inspector, minimap/legend.

### Split Preview

Use when editing directly affects preview, diff, or result.

- Structure: editor/config and live preview/result.

### Settings Matrix

Use for permissions, integrations, feature flags, or dependency-heavy settings.

- Structure: settings navigation, focused panel, dependency warnings, save/revert.

### Wizard / Stepper

Use for setup, import, migration, publishing, or irreversible changes.

- Structure: progress, current step, validation, next/back, completion.

### Mobile Task Stack

Use for one focused mobile task.

- Structure: header, object state, compact details, primary action near bottom.

## Pattern Switch Rules

- Hidden answer: switch to Work Intake + History Stack or Evidence Drilldown.
- Audit work: switch to Agent Execution Trace.
- Prompt/rubric editing: switch to Wide Artifact Editor.
- Too many equal panes: choose one dominant working surface and progressive disclosure.
- User asks for two columns: treat it as area-budget correction, not pure visual preference.
