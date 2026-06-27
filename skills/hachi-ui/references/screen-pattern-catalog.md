# Screen Pattern Catalog

Use this catalog with `app-layout-patterns.md` when a product screen needs a more specific whole-screen pattern than a generic sidebar, dashboard, or split view. Classify input/view information intent with `information-shape-catalog.md` first, choose the whole-screen pattern here, decompose it with `information-unit-patterns.md`, then choose atomic controls from `input-element-catalog.md`.

## Selection Inputs

Choose from:

- user job: request, inspect, edit, compare, verify, approve, configure, recover;
- core object: Work, Run, AgentStep, Domain, File, Artifact, Account, Ticket, Item, Product, Order, Booking, Lesson, Goal, Thread, Collection;
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
10. Source Governance Library
11. Settings Dependency Map
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
23. Search Investigation Surface
24. Template Decision Gallery

### Operations And Business SaaS

25. Exception Command Center
26. Object Profile / 360 Detail
27. List + Bulk Action Review
28. Pipeline / Kanban Board
29. SLA Triage Queue
30. Incident War Room
31. Schedule / Resource Planner
32. Appointment Readiness Board
33. Plan Usage Entitlement Console

### Analytics And Decision Support

34. Report Builder
35. Metric Explorer
36. Segment / Cohort Builder
37. Alert Triage Center

### Spatial, Preview, And Mobile

38. Canvas + Inspector
39. Edit Preview Workbench
40. Guided Setup / Migration Flow
41. Mobile Field Task Flow

### Activation, Access, Communication, And Data Quality

42. Access Gate / Recovery
43. First-Run Activation Checklist
44. Object Creation Studio
45. Notification / Activity Inbox
46. Help / Support Resolution Center
47. Data Quality Resolution Queue
48. Communication Thread Console
49. Relationship / Dependency Map

### Consumer, Commerce, Learning, And Media

50. Product Discovery / Commerce Browse
51. Checkout / Commitment Flow
52. Booking / Reservation Flow
53. Learning Progress Workspace
54. Lesson / Content Consumption
55. Community Participation Hub
56. Personal Goal / Habit Tracker
57. Collection / Media Library

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

### Source Governance Library

Use when source assets must be trusted, governed, refreshed, and traced to product behavior.

- Structure: source inventory, governance status, freshness/owner, validation findings, selected source detail, affected artifacts.
- Good for: policy repositories, document knowledge bases, RAG source libraries, regulated source review.
- Required: processing, indexed, stale, invalid, duplicate, ownerless, used-by relationship.
- Avoid: generic file browsers that hide freshness, ownership, or downstream impact.

### Settings Dependency Map

Use when settings have dependencies, inheritance, risk, or downstream effects.

- Structure: focused setting group, dependency map/list, impact preview, inherited source, save/revert, recovery note.
- Good for: workspace defaults, model routing, data retention, security controls, integration defaults.
- Required: dirty, saved, invalid, inherited, locked by role, downstream conflict.
- Avoid: long undifferentiated settings pages with no impact model.

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

### Search Investigation Surface

Use when search is not only retrieval, but investigation and rapid narrowing.

- Structure: query, filters, ranked results, highlighted evidence, selected preview, saved/refined query, empty recovery.
- Good for: knowledge search, audit search, admin records, logs, people, documents.
- Required: loading, no results, selected result, relevance hint, filter chips, refined query state.
- Avoid: a search box plus cards when the user must judge why a result matters.

### Template Decision Gallery

Use when the user must choose a reusable starting point by fit, risk, and adaptation effort.

- Structure: category filters, ranked templates, fit criteria, selected preview, required changes, use/customize action.
- Good for: workflow templates, report templates, prompt presets, onboarding recipes.
- Required: selected template, preview, fit reason, empty category, custom template.
- Avoid: decorative template grids with no decision criteria.

### Exception Command Center

Use when the screen exists to surface exceptions and make the next operational decision clear.

- Structure: current operating state, exception groups, decision queue, evidence table, recommended action, acknowledgement state.
- Good for: operations, revenue, security, logistics, executive review.
- Required: normal, warning, critical, acknowledged, owner, recommended action.
- Avoid: executive KPI walls where nothing is actionable.

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

### Appointment Readiness Board

Use when scheduled appointments require readiness, missing-prep detection, and follow-up.

- Structure: time lane, appointment cards, readiness state, missing inputs, agenda/evidence, follow-up queue.
- Good for: executive meetings, healthcare, sales calls, service visits, field operations.
- Required: upcoming, ready, missing prep, completed, no-show, follow-up.
- Avoid: generic calendars when events are not the decision object.

### Plan Usage Entitlement Console

Use when entitlement, limits, invoices, and payment state determine what the user can do next.

- Structure: entitlement summary, usage meters, limit forecast, invoice/payment table, upgrade or recovery action.
- Good for: SaaS billing, API usage, quotas, enterprise seats, metered products.
- Required: over limit, trial, failed payment, invoice paid, grace period, upgrade.
- Avoid: finance-only billing pages that hide product impact.

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

### Edit Preview Workbench

Use when a wide editing surface and a result preview must remain linked.

- Structure: dominant editor/config surface, live preview/result, validation, selected output detail, publish/save action.
- Good for: email builders, automations, workflows, reporting, design tools, prompt/result authoring.
- Required: draft, preview, validation errors, unsaved changes, stale preview.
- Avoid: arbitrary 50/50 splits when the editor or preview clearly deserves more area.

### Guided Setup / Migration Flow

Use when setup, import, migration, publishing, or irreversible changes need staged validation.

- Structure: progress, current requirement, validation result, preview of consequence, next/back, recovery, completion.
- Good for: OAuth connection, workspace setup, billing, deployment, data migration.
- Required: incomplete, validating, failed validation, skipped optional, blocked, done.
- Avoid: wizard chrome when the user can safely finish from one screen.

### Mobile Field Task Flow

Use when mobile users need one focused field action with state and recovery.

- Structure: compact object header, task state, essential details, capture/input block, thumb-reachable primary action, sync/recovery state.
- Good for: capture, approval, field work, messaging, checklists, inspections.
- Required: offline, draft, sync pending, destructive confirmation, incomplete required input.
- Avoid: shrinking a desktop dashboard into mobile columns.

### Access Gate / Recovery

Use when entry, authentication, authorization, or recovery is the main work.

- Structure: identity context, access state, required action, recovery options, security note, next destination.
- Good for: sign-in, SSO, invite acceptance, locked workspace, expired session, account recovery.
- Required: invalid credentials, expired link, locked role, recovery sent, SSO unavailable.
- Avoid: marketing-style login pages when the issue is operational recovery.

### First-Run Activation Checklist

Use when a new user or workspace must complete a few meaningful setup tasks before value appears.

- Structure: product promise, activation tasks, current blocker, sample/preview, skip/import path, progress state.
- Good for: onboarding, workspace setup, integration setup, empty-state activation.
- Required: not started, blocked, optional skipped, completed, sample data.
- Avoid: generic tours that do not create a usable product state.

### Object Creation Studio

Use when creating the primary object requires naming, configuring, validating, and previewing consequences.

- Structure: object intent, required fields, configuration groups, validation, preview/summary, create action.
- Good for: project creation, campaign setup, workflow creation, policy creation, dataset creation.
- Required: draft, invalid, duplicate name, preview, created.
- Avoid: tiny modals when creation includes meaningful configuration or risk.

### Notification / Activity Inbox

Use when the user must review events, mentions, tasks, and system updates without losing priority.

- Structure: grouped feed, priority/owner filters, event summary, linked object preview, mark/read/action controls.
- Good for: collaboration tools, admin systems, workflow products, incident or approval notifications.
- Required: unread, assigned, muted, action required, archived.
- Avoid: chronological feeds with no grouping or next action.

### Help / Support Resolution Center

Use when the user needs diagnosis, self-service, escalation, or support follow-through.

- Structure: issue description, suggested fixes, product state/evidence, contact/escalate path, ticket status.
- Good for: support centers, troubleshooting, AI help assistants, enterprise admin support.
- Required: unresolved, suggestion tried, escalated, waiting, resolved.
- Avoid: static FAQ pages when the user needs recovery and state.

### Data Quality Resolution Queue

Use when records must be cleaned, merged, mapped, or repaired before downstream work is trustworthy.

- Structure: issue groups, affected records, suggested fix, confidence, bulk repair, audit/revert.
- Good for: CRM cleanup, import validation, deduplication, taxonomy cleanup, data governance.
- Required: duplicate, missing field, invalid format, suggested repair, applied, reverted.
- Avoid: generic data tables that hide why a row is unhealthy.

### Communication Thread Console

Use when conversation is tied to work objects, decisions, and evidence.

- Structure: thread list, selected conversation, linked object/evidence, requested action, resolution state.
- Good for: support cases, handoffs, internal approvals, customer success, review comments.
- Required: unread, assigned, waiting reply, action requested, resolved.
- Avoid: chat-first UI when the conversation is only secondary to a workflow decision.

### Relationship / Dependency Map

Use when understanding connections, impact, or lineage is the user's main decision.

- Structure: graph or dependency lanes, selected node, relationship types, impact summary, filter/legend, affected actions.
- Good for: data lineage, integration dependencies, org relationships, workflow dependencies, permission inheritance.
- Required: selected node, upstream/downstream, missing link, cycle/conflict, impact preview.
- Avoid: decorative node diagrams without selectable relationships or consequences.

### Product Discovery / Commerce Browse

Use when the user compares products, offers, plans, or content before choosing one.

- Structure: discovery filters, ranked item list/grid, comparison attributes, selected item preview, saved/compare action.
- Good for: ecommerce, marketplaces, plan selection, catalog browsing, travel/product discovery.
- Required: loading, no results, filtered results, selected item, unavailable item, saved/compared item.
- Avoid: decorative card grids when fit criteria, price, availability, or comparison drive the decision.

### Checkout / Commitment Flow

Use when the user commits to purchase, subscribe, enroll, reserve, publish, or apply.

- Structure: commitment summary, required details, cost/consequence, validation, payment/confirmation, recovery.
- Good for: checkout, subscription purchase, enrollment, application submission, publishing.
- Required: incomplete, invalid, payment pending, failed payment, confirmed, cancellation/undo when possible.
- Avoid: single final button without consequence summary and error recovery.

### Booking / Reservation Flow

Use when availability, time, resource, and confirmation must be coordinated.

- Structure: availability search, slot/resource options, selected option summary, required details, confirmation.
- Good for: appointments, travel, rooms, service visits, events, classes.
- Required: unavailable, conflicting, selected slot, waitlist, confirmed, reschedule/cancel.
- Avoid: generic calendars when availability and commitment are the main work.

### Learning Progress Workspace

Use when the user must understand progress, next lesson, weak areas, and practice actions.

- Structure: progress overview, current objective, weak/strong areas, recommended next action, history.
- Good for: courses, onboarding education, coaching, training, certification.
- Required: not started, in progress, completed, overdue, needs practice, passed/failed.
- Avoid: static course lists that do not show the learner's next decision.

### Lesson / Content Consumption

Use when reading, watching, listening, or practicing is the primary surface.

- Structure: content surface, progress/position, notes/highlights, related resources, next/complete action.
- Good for: articles, lessons, videos, podcasts, tutorials, guided practice.
- Required: current position, incomplete, completed, bookmarked, note/highlight, next item.
- Avoid: burying the content behind navigation, cards, or promotional panels.

### Community Participation Hub

Use when users browse, contribute, react, moderate, or follow social/community activity.

- Structure: feed or topic list, composer, selected discussion, participation state, moderation/reporting actions.
- Good for: communities, forums, social products, internal collaboration, creator products.
- Required: unread, draft, posted, replied, reported, muted, moderated.
- Avoid: pure infinite feeds when the product's value depends on topic, object, or decision context.

### Personal Goal / Habit Tracker

Use when users set goals, record progress, review trends, and recover from lapses.

- Structure: goal state, logging input, streak/progress, trend insight, next action, recovery prompt.
- Good for: fitness, finance, health, learning, personal productivity.
- Required: not logged, logged, missed, streak, milestone, reset/recovery.
- Avoid: charts without a concrete next action or recovery path.

### Collection / Media Library

Use when users organize, revisit, filter, and act on saved content or assets.

- Structure: collection navigation, filters, item grid/list, selected item preview, organization actions.
- Good for: media libraries, bookmarks, files, playlists, asset managers, saved products.
- Required: empty collection, selected item, unavailable item, duplicate, favorite, archived.
- Avoid: flat galleries when organization, retrieval, or reuse is the user's job.
## Pattern Switch Rules

- Hidden answer: switch to Work Intake + History Stack or Evidence Drilldown.
- Audit work: switch to Agent Execution Trace.
- Prompt/rubric editing: switch to Wide Artifact Editor or Prompt And Rubric Studio.
- Many settings with dependencies: switch to Settings Dependency Map, Permission / Role Matrix, Feature Flag Console, or Integration Health Console.
- Import/migration: switch to Data Import + Field Mapping.
- Batch changes: switch to List + Bulk Action Review.
- Live incident or SLA pressure: switch to Incident War Room, SLA Triage Queue, or Alert Triage Center.
- Too many equal panes: choose one dominant working surface and progressive disclosure.
- User asks for two columns: treat it as area-budget correction, not pure visual preference.
- Empty product state: switch to First-Run Activation Checklist or Object Creation Studio.
- Access failure: switch to Access Gate / Recovery.
- Search task becomes diagnosis: switch from Search Investigation Surface to Evidence Drilldown or Data Quality Resolution Queue.
- Relationship understanding dominates: switch to Relationship / Dependency Map.
- Browsing becomes purchase/subscription/enrollment: switch to Checkout / Commitment Flow.
- Availability is the primary constraint: switch to Booking / Reservation Flow.
- Learning work dominates: switch to Learning Progress Workspace or Lesson / Content Consumption.
- Saved content or media organization dominates: switch to Collection / Media Library.



