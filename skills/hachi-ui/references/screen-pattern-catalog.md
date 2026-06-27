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

## Pattern Index

### AI Work And Evidence

1. Work Intake + History Stack
2. Agent Execution Trace
3. Evidence Drilldown
4. Tool Permission Review
5. Prompt And Rubric Studio
6. Evaluation Lab
7. Human Handoff Console
8. Automation Rule Builder

### Knowledge, Settings, And Configuration

9. Domain Knowledge Workspace
10. Knowledge Library
11. Settings Matrix
12. Permission / Role Matrix
13. Feature Flag Console
14. Integration Health Console
15. Data Import + Field Mapping
16. Form Builder / Schema Designer

### Review, Editing, And Content

17. Wide Artifact Editor / Full Editor Surface
18. Review / Approval Queue
19. Comparison / Diff Review
20. Document Draft + Review
21. Annotation / Labeling Review
22. Version History / Rollback
23. Search Results + Preview
24. Template / Gallery Picker

### Operations And Business SaaS

25. Command Center
26. Object Profile / 360 Detail
27. List + Bulk Action Review
28. Pipeline / Kanban Board
29. SLA Triage Queue
30. Incident War Room
31. Schedule / Resource Planner
32. Calendar Operations Board
33. Billing / Usage Console

### Analytics And Decision Support

34. Report Builder
35. Metric Explorer
36. Segment / Cohort Builder
37. Alert Triage Center

### Spatial, Preview, And Mobile

38. Canvas + Inspector
39. Split Preview
40. Wizard / Stepper
41. Mobile Task Stack

> Use the index as vocabulary. Use the detailed pattern sections below to decide whether the screen deserves that pattern.

## Detailed Patterns

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

### Evidence Drilldown

Use when the main claim is visible but provenance must be inspectable.

- Structure: claim summary, evidence list, selected evidence detail, source metadata, raw source fallback.
- Good for: generated briefs, compliance review, research assistants, audit trails.
- Required: selected evidence, missing evidence, stale evidence, source confidence.

### Tool Permission Review

Use when the user must approve, deny, scope, or audit tools an AI/user can access.

- Structure: requested tool list, reason, scope, risk, permission action, audit note.
- Good for: agent tools, OAuth scopes, enterprise permissioning.
- Required: allow/deny, least-privilege scope, expiration, audit log.

### Prompt And Rubric Studio

Use when prompts, output specs, rubrics, examples, and variables are first-class objects.

- Structure: artifact list, prompt editor, rubric table, variables, examples, validation.
- Good for: AI product configuration, evaluator setup, generation templates.
- Required: dirty/saved state, validation, preview/test run, version state.
- Avoid: one tiny textarea for all instructions.

### Evaluation Lab

Use when users compare outputs against rubrics, datasets, test cases, or evaluators.

- Structure: dataset/test case list, output comparison, rubric scores, failure clusters, rerun controls.
- Good for: AI evals, QA, benchmark review.
- Required: pass/fail, score rationale, sample navigation, rerun state.

### Human Handoff Console

Use when AI or workflow work must be escalated to a person.

- Structure: handoff reason, case summary, evidence, assignee, SLA, resolution actions.
- Good for: support, compliance exceptions, human-in-the-loop workflows.
- Required: assigned, accepted, returned, resolved, timed out.

### Automation Rule Builder

Use when users define triggers, conditions, actions, and exceptions.

- Structure: trigger block, condition builder, action list, preview/simulation, test result.
- Good for: workflow automations, notifications, routing rules.
- Required: invalid rule, dry run, active/inactive, last triggered.

### Domain Knowledge Workspace

Use when users manage domains, knowledge files, artifact specs, rubrics, and prompts.

- Structure: domain list, selected domain detail, file table with upload, artifact summary list, edit actions.
- Good for: knowledge bases, agent configuration, generation systems.
- Required: selected domain, file state, artifact state, validation.
- Avoid: four equal panes that starve prompt/rubric editing.

### Knowledge Library

Use when browsing, uploading, tagging, and validating knowledge assets.

- Structure: filters, file table, upload zone, selected file details, validation state.
- Good for: source libraries, policy repositories, document knowledge bases.
- Required: processing, indexed, stale, invalid, duplicate.

### Settings Matrix

Use for permissions, integrations, feature flags, or dependency-heavy settings.

- Structure: settings navigation, focused panel, dependency warnings, save/revert.
- Good for: workspace preferences, integrations, defaults.
- Required: dirty, saved, invalid, inherited, locked by role.

### Permission / Role Matrix

Use when roles, permissions, resources, and inheritance must be compared.

- Structure: role list, resource columns, permission cells, inherited markers, review diff.
- Good for: admin security, team access, regulated systems.
- Required: inherited, overridden, locked, pending change, save/revert.

### Feature Flag Console

Use when flags vary by environment, segment, rollout, and status.

- Structure: flag table, environment tabs, rollout controls, targeting summary, kill switch.
- Good for: product ops, experiments, staged launches.
- Required: on/off, partial rollout, scheduled, conflict, emergency off.

### Integration Health Console

Use when connected services have auth, sync, freshness, and error states.

- Structure: integration cards/list, sync status, last run, error cause, reconnect/retry.
- Good for: OAuth, data sync, webhook health, ETL tools.
- Required: connected, expired, failing, syncing, stale, reconnecting.

### Data Import + Field Mapping

Use when the user imports external data and maps fields before validation.

- Structure: upload/source, preview table, source fields, target fields, mapping status, validation results.
- Good for: CSV import, CRM migration, schema setup.
- Required: unmapped, invalid type, duplicate, preview, dry run, commit.

### Form Builder / Schema Designer

Use when users create fields, validations, sections, and conditional logic.

- Structure: field list/canvas, selected field inspector, validation rules, preview.
- Good for: intake forms, surveys, schemas, internal tools.
- Required: selected field, invalid rule, required/optional, preview mode.

### Wide Artifact Editor / Full Editor Surface

Use for heavy writing, long prompts, structured rubrics, large markdown, YAML, JSON, or code-like editing.

- Structure: large editor, structured metadata, validation banner, save/cancel/delete, dirty/saved state.
- Good for: prompt editor, rubric table, long form, policy editor.
- Required: dirty, saved, invalid, locked, deleting.
- Avoid: narrow right rail editors.

### Review / Approval Queue

Use when the user must process items and decide approve, reject, request changes, or escalate.

- Structure: queue, priority, selected item, evidence, decision controls, next item.
- Good for: approvals, moderation, procurement, release review.
- Required: assigned, blocked, bulk selected, done.

### Comparison / Diff Review

Use when the user chooses between versions or validates changes.

- Structure: before/after, diff annotations, change summary, accept/reject controls.
- Good for: document revisions, prompt versions, config changes, code-like diffs.
- Required: added/removed/changed, conflict, no-change.

### Document Draft + Review

Use when writing and reviewing a document or generated artifact are both central.

- Structure: document body, comments/suggestions, review status, source/evidence links, export/share.
- Good for: briefs, proposals, reports, policies.
- Required: draft, commented, accepted, rejected, exported.

### Annotation / Labeling Review

Use when users inspect items and assign labels, spans, categories, or judgments.

- Structure: item viewer, label palette, annotation list, validation, progress queue.
- Good for: dataset labeling, review workflows, content moderation.
- Required: unlabeled, labeled, conflict, skipped, reviewed.

### Version History / Rollback

Use when history, compare, restore, and audit are key.

- Structure: version timeline, selected version summary, diff preview, restore action, audit metadata.
- Good for: configs, prompts, documents, policies.
- Required: current, selected past, restore confirmation, conflict.

### Search Results + Preview

Use when the main task is finding and inspecting objects quickly.

- Structure: query, filters, result list, preview, highlighted match, empty state.
- Good for: knowledge search, admin records, logs, people, documents.
- Required: loading, no results, selected result, filter chips.

### Template / Gallery Picker

Use when the user starts from reusable templates, examples, or presets.

- Structure: category filters, template grid/list, preview, use/customize action.
- Good for: workflow templates, report templates, prompt presets.
- Required: selected template, preview, empty category, custom template.

### Command Center

Use when status, anomalies, and decisions must be visible at once.

- Structure: summary, flow or anomaly visualization, decision queue, evidence table.
- Good for: operations, revenue, security, logistics, executive review.
- Required: normal, warning, critical, acknowledged, recommended action.

### Object Profile / 360 Detail

Use when one object has many related facts, activity, health, and actions.

- Structure: object header, key properties, activity, related records, action panel.
- Good for: account, customer, employee, asset, ticket, project.
- Required: current state, owner, recent activity, risk, primary action.

### List + Bulk Action Review

Use when selecting many records and applying a reviewed change.

- Structure: table/list, filters, bulk selection, review drawer/modal, apply/undo.
- Good for: admin edits, assignment, cleanup, imports.
- Required: selected count, preview changes, partial failure, undo.

### Pipeline / Kanban Board

Use when objects move across stages and stage health matters.

- Structure: stage columns, cards, stage counts, blocked indicators, drag/drop or action menu.
- Good for: sales, recruiting, issue states, workflows.
- Required: empty stage, blocked card, stale card, move confirmation.

### SLA Triage Queue

Use when time-to-action and priority dominate.

- Structure: aging buckets, priority rows, owner, SLA timer, resolve/escalate controls.
- Good for: support, incident, healthcare/admin queues.
- Required: overdue, due soon, assigned, escalated, paused.

### Incident War Room

Use when a live incident requires timeline, roles, actions, and status.

- Structure: current severity, timeline, owner roles, action checklist, communications.
- Good for: reliability, security, logistics disruption.
- Required: investigating, mitigated, resolved, postmortem, update sent.

### Schedule / Resource Planner

Use when assigning people/assets over time.

- Structure: timeline/grid, resources, demand, conflicts, assignment controls.
- Good for: staffing, capacity, field ops, rooms/equipment.
- Required: conflict, overbooked, unassigned, tentative, confirmed.

### Calendar Operations Board

Use when calendar events are operational objects with preparation and follow-up.

- Structure: time lane, event cards, readiness, agenda/evidence, follow-up queue.
- Good for: executive meetings, healthcare, sales calls, service visits.
- Required: upcoming, ready, missing prep, completed, follow-up.

### Billing / Usage Console

Use when plan, usage, invoices, limits, and payment state must be inspectable.

- Structure: plan summary, usage meters, invoice table, payment method, alerts.
- Good for: SaaS billing, API usage, quotas.
- Required: over limit, trial, failed payment, invoice paid, upgrade.

### Report Builder

Use when users assemble charts, sections, filters, and narrative into a report.

- Structure: report outline, canvas/preview, chart config, filters, export/share.
- Good for: analytics, board decks, scheduled reports.
- Required: draft, preview, invalid chart, scheduled, exported.

### Metric Explorer

Use when the user investigates one or more metrics interactively.

- Structure: metric selector, time controls, chart, breakdowns, annotations, insight list.
- Good for: product analytics, finance, ops metrics.
- Required: loading, empty, anomaly, selected point, comparison.

### Segment / Cohort Builder

Use when building groups from rules and previewing membership.

- Structure: rule builder, count preview, sample members, save/use action.
- Good for: marketing, permissions, experiments, analytics.
- Required: invalid rule, zero members, preview loading, saved.

### Alert Triage Center

Use when alerts must be grouped, deduplicated, acknowledged, and resolved.

- Structure: alert groups, severity, evidence, owner, acknowledge/resolve controls.
- Good for: security, reliability, fraud, monitoring.
- Required: new, acknowledged, suppressed, escalated, resolved.

### Canvas + Inspector

Use when spatial relationships matter.

- Structure: canvas, toolbar, selected object, inspector, minimap/legend.
- Good for: diagrams, agents, workflows, maps, org charts, data lineage.
- Required: selected object, pan/zoom, invalid edge, empty canvas, layout conflict.

### Split Preview

Use when editing directly affects preview, diff, or result.

- Structure: editor/config and live preview/result.
- Good for: email builders, automations, workflows, reporting, design tools.
- Required: draft, preview, validation errors, unsaved changes.

### Wizard / Stepper

Use for setup, import, migration, publishing, or irreversible changes.

- Structure: progress, current step, validation, next/back, completion.
- Good for: OAuth connection, workspace setup, billing, deployment.
- Required: incomplete, validating, failed validation, skipped optional, done.

### Mobile Task Stack

Use for one focused mobile task.

- Structure: header, object state, compact details, primary action near bottom.
- Good for: capture, approval, field work, messaging, checklists.
- Required: offline, draft, sync pending, destructive confirmation.

## Pattern Switch Rules

- Hidden answer: switch to Work Intake + History Stack or Evidence Drilldown.
- Audit work: switch to Agent Execution Trace.
- Prompt/rubric editing: switch to Wide Artifact Editor or Prompt And Rubric Studio.
- Many settings with dependencies: switch to Settings Matrix, Permission / Role Matrix, Feature Flag Console, or Integration Health Console.
- Import/migration: switch to Data Import + Field Mapping.
- Batch changes: switch to List + Bulk Action Review.
- Live incident or SLA pressure: switch to Incident War Room, SLA Triage Queue, or Alert Triage Center.
- Too many equal panes: choose one dominant working surface and progressive disclosure.
- User asks for two columns: treat it as area-budget correction, not pure visual preference.
