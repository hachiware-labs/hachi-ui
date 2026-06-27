# App Layout Patterns

Choose the layout pattern before drawing. Use this with `screen-pattern-catalog.md`: first map the brief to product thesis, user decisions, information units, information shapes, editing burden, and verification burden; then choose the whole-screen pattern. Do not default to a left sidebar or left/right split unless the user job requires it.

## Split Layout Guardrail

Avoid dividing the screen into two large vertical panes by habit. A split layout is valid only when both panes must remain visible at the same time:

- Compare two states, versions, or objects.
- Select an item while inspecting its details.
- Edit configuration while seeing a live preview or result.
- Use a canvas while inspecting a selected node/object.

Prefer a single focused working surface when the user is reading, deciding, onboarding, reviewing a dashboard, or completing a linear task. Use top navigation, tabs, stacked sections, progressive disclosure, stepper flow, full-canvas composition, or a focused table/detail page before reaching for a split.

## Patterns

### 1. Left Pane Workspace

Use for mature tools with many modules and repeated daily navigation.

- Structure: global sidebar, top bar, main workspace, optional right inspector.
- Good for: admin tools, dashboards, CRM, dev tools, analytics, settings-heavy SaaS.
- Avoid when: the app has a short linear setup flow or one dominant object.
- Do not use merely to fill the left side of the screen.

### 2. Top Nav Product

Use when there are few primary sections and the main screen should feel broad.

- Structure: top navigation, wide content, section tabs or filters.
- Good for: lightweight SaaS, reports, content products, billing, portfolio tools.
- Avoid when: users switch between many modules constantly.

### 3. List Detail

Use when the user selects an object, inspects it, and acts on it.

- Structure: list/table, selected object detail, action panel.
- Good for: CRM accounts, issues, tickets, leads, documents, inventory.
- Required states: selected, empty selection, filtered zero state, stale data, unsaved edits.
- Avoid when: users do not need to keep the list visible while acting on the selected object.

### 4. Inbox / Queue

Use when the job is triage and throughput.

- Structure: priority groups, queue list, item preview, resolve/assign controls.
- Good for: support, review queues, approvals, incident response, moderation.
- Required states: unread/new, assigned, blocked, bulk selected, done, next item.

### 5. Guided Setup / Migration Flow

Use when setup, import, migration, checkout, publishing, or irreversible changes need staged validation and consequence preview.

- Structure: progress, current step, requirement checklist, validation, next/back.
- Good for: initial setup, OAuth connection, workspace creation, billing, deployment.
- Required states: incomplete, validating, failed validation, skipped optional, done.

### 6. Edit Preview Workbench

Use when a wide editor/config surface and a preview, diff, or result must stay linked.

- Structure: editor/config on one side, live preview/result on the other.
- Good for: email builders, automations, workflows, reporting, design tools.
- Required states: draft, preview, validation errors, unsaved changes.
- Avoid when: preview is only decorative or can be shown after the primary action.

### 7. Canvas + Inspector

Use when spatial relationships matter.

- Structure: central canvas/graph/board, toolbar, minimap or legend, right inspector.
- Good for: diagrams, agents, workflows, maps, org charts, data lineage.
- Required states: selected object, pan/zoom, invalid edge, empty canvas, layout conflict.
- Keep the canvas dominant; the inspector should not make the screen feel like two equal halves.

### 8. Exception Command Center

Use when the user must understand exceptions and make one or more operational decisions.

- Structure: summary strip, anomaly/flow visualization, decision queue, evidence table.
- Good for: operations, revenue, security, logistics, executive review.
- Required states: normal, warning, critical, acknowledged, recommended action.

### 9. Settings Dependency Map

Use when users configure settings with dependencies, inheritance, risk, or downstream effects.

- Structure: settings navigation, focused panel, dependency warnings, save/revert bar.
- Good for: permissions, integrations, feature flags, workspace preferences.
- Required states: dirty, saved, invalid, inherited, locked by role.

### 10. Mobile Field Task Flow

Use when the user performs one focused mobile or field task with state and recovery.

- Structure: header, current object/state, primary action near bottom, secondary overflow.
- Good for: field apps, approvals, capture, messaging, checklists.
- Required states: offline, draft, sync pending, destructive confirmation.

## Semantic Selection Heuristic

- Heavy verification or audit: Agent Execution Trace or Evidence Drilldown from `screen-pattern-catalog.md`.
- New AI work plus history: Work Intake + History Stack.
- Domain files, artifacts, rubrics, and prompts: Domain Knowledge Workspace plus Wide Artifact Editor.
- Long prompt/rubric editing: never use a narrow inspector; use a wide editor, modal, full page, or dedicated detail surface.
- User correction about columns or cramped editing: treat it as area budget and screen pattern correction, not cosmetic layout tuning.

## Selection Heuristic

- Many modules: left pane workspace.
- One object at a time: list detail.
- Many items to process: inbox/queue.
- Linear setup: guided setup / migration flow.
- Config affects output: edit preview workbench.
- Relationships matter: canvas + inspector.
- Decision under uncertainty: exception command center.
- Permissions or integrations: settings dependency map.
- Small-screen task: mobile field task flow.

## Anti-Patterns

- Two equal columns because the canvas feels empty.
- Sidebar plus right inspector plus dense content before the object model is proven.
- Split screen for onboarding when a stepper would be clearer.
- List-detail when the real task is bulk review or queue processing.
- Dashboard split where the left half is summary cards and the right half is unrelated detail.
- Landing page split hero with text on one side and a generic product card on the other.


