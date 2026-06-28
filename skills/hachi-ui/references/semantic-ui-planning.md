# Semantic UI Planning

Use this reference before wireframing product screens, SaaS tools, AI workflows, dashboards, settings, admin tools, mobile task screens, and other application UI.

## Purpose

Translate the brief into a UI Element Plan before drawing boxes. Decide what the user must inspect, decide, write, compare, verify, or act on, then map those needs to screen patterns, UI elements, layout attention, state, and evidence.

A screen should not be a list of plausible components. It should be a semantic arrangement of information units that helps the user make the next decision.

For reusable app/product work, write this planning into `UI_PLAN.md`. Treat older `semantic-plan.md` files as legacy equivalents, but prefer `UI_PLAN.md` for new work so screen inventory, information units, input friction, and flow causality stay in one authoritative file.

## Planning Order

1. Product thesis
2. User job
3. Core objects
4. User decision points
5. Information units
6. Input/view information patterns
7. Information shapes
8. Screen pattern
9. Information-unit patterns
10. Element mapping
11. Input friction audit
12. Area budget
13. Gaze route
14. Flow causality and primary path
15. State, validation, and recovery coverage
16. Evidence/provenance needs
17. Rejected patterns and why

## UI Element Plan Schema

Use this structure in scratch notes or examples before drawing.

When artifact files are being created, this schema belongs inside `UI_PLAN.md`, usually under `Screen Information Plan`, `Input Friction Audit`, `Flow Causality`, and `Rejected Patterns`.

```yaml
product_thesis: "What this product must make possible or trustworthy."
screen: "screen_name"
viewport: "desktop | mobile | flow"
user_job: "What the user must understand, decide, write, verify, or complete."
core_objects:
  - name: Work
    role: primary_object
user_decision_points:
  - "What is the final answer?"
  - "Which step caused the current state?"
information_units:
  - id: final_answer
    label: "最終回答"
    user_intent: view
    shape_pattern: object_summary_view
    shape: long_text_summary
    role: primary_result
    user_question: "依頼への答えは何か？"
    recommended_element: summary_card
    area_need: large
    reason: "The answer is the first thing the user wants to confirm."
screen_pattern:
  name: Agent Execution Trace
  reason: "The main job is step-by-step verification, not dashboard overview."
unit_patterns:
  final_answer: primary_answer_result_block
  trace_step: activity_timeline_step
  evidence: evidence_detail_panel
element_map:
  final_answer: summary_card
input_friction_audit:
  - input: "依頼者"
    source: "already_known"
    reuse_strategy: "inherit from selected work request"
    shown_as: "read-only object header with change action"
  - input: "例外理由"
    source: "exception_only"
    reuse_strategy: "ask only after override or escalation"
    shown_as: "conditional reason note"
area_budget:
  final_answer: large
  raw_logs: collapsed
states:
  - running
  - verified
  - failed
primary_path:
  previous_trigger: "依頼を送信"
  next_trigger: "評価NGを修正"
  why_next_screen_follows: "A failed evidence check requires editing the rubric and prompt."
  supporting_surfaces:
    - raw_logs
    - library
evidence_needs:
  - input
  - output
  - review
  - decision
rejected_patterns:
  - name: generic_dashboard
    reason: "It hides the answer and evidence behind metrics."
```

## Input And Viewing Information Patterns

Use `information-shape-catalog.md` before choosing components. A UI plan should say whether each information unit is being entered, selected, edited, reviewed, verified, compared, or recovered. Then classify it as an input pattern such as `natural_language_request_input`, `structured_form_input`, `file_source_input`, `permission_scope_input`, or as a viewing pattern such as `dense_record_view`, `timeline_audit_view`, `evidence_provenance_view`, `metric_trend_view`, or `relationship_dependency_view`.

If a plan says only `form`, `table`, `card`, `modal`, or `dashboard`, the information pattern is still underspecified.

## Input Friction Audit

Use `input-friction-patterns.md` whenever a screen contains user input, confirmation, approval, setup, repeated rows, uploaded/extracted data, role handoff, or exception reasons.

Do not treat input burden as field count only. The most frustrating burden is repeated meaning: entering the same identity, address, requester, assignee, reason, schedule, item, or extracted value again because the UI has not carried it forward.

For each input unit, decide whether it is:

- already known from a selected object, previous step, profile, integration, upload, or history;
- same as an existing value and should default to reuse;
- system-inferred and should be corrected, not typed from blank;
- selected from suggestions, templates, recent values, or saved presets;
- genuinely new information;
- exception-only and should appear only after override, rejection, escalation, or policy deviation.

Redesign before drawing if the plan asks the user to retype known values, create many similar items one by one, provide reason text on the happy path, or fill information owned by another role.

## Pattern Layers

Use four layers before drawing:

- Input/view information pattern: the user's intent for each information unit, chosen from `information-shape-catalog.md`.
- Whole-screen pattern: the complete working surface, chosen from `screen-pattern-catalog.md`.
- Information-unit pattern: repeated or dominant blocks inside the screen, chosen from `information-unit-patterns.md`.
- Input/display element: atomic controls and visual elements, chosen from `input-element-catalog.md`.

Do not jump from a whole-screen pattern directly to buttons and cards when the screen contains evidence, queues, timelines, validation, permissions, diffs, metrics, alerts, empty states, or communication threads. Classify the input/view intent first, because the same object needs different UI when the user is entering it, scanning it, verifying it, comparing it, or recovering from it.

## Flow Causality

For multi-screen flows, evaluate the path before drawing. A screen sequence is valid only when each next screen is caused by a user action, system event, validation result, or risk/recovery condition from the previous screen.

Use this check for every transition:

- The source screen has enough information for the user to decide the trigger action.
- The trigger label says the exact action or event, not the destination.
- The target screen is the natural consequence of the trigger.
- The target screen answers the next user question created by the previous screen.
- Supporting surfaces such as libraries, templates, metrics, logs, and settings do not interrupt the main path unless they are the object being decided.
- If a state can block the path, the flow shows validation, failure, recovery, retry, edit, skip, or undo before pretending the path is complete.

Common repairs:

- If a metrics screen is used to diagnose a problem, follow it with a plan, practice, review, or recovery screen, not a generic library.
- If a library, template gallery, or saved collection is useful but not mandatory, make it a supporting surface or optional branch instead of the next primary screen.
- If a triage screen asks for a decision, follow it with a review, assignment, resolution, or confirmation surface before broad monitoring.
- If checkout, booking, import, connection, generation, or approval can fail, show the failure reason and recovery action in the same flow.
- If a user correction changes flow order, update the UI Element Plan as a flow patch before redrawing.

## Information Shapes

Choose shape before element:

- `short_text`: names, titles, labels.
- `structured_text`: prompts, instructions, decision notes.
- `long_text_summary`: answers, summaries, generated briefs.
- `tabular_records`: history rows, accounts, domains, files.
- `ordered_steps`: timelines, workflow steps, agent traces.
- `paired_evidence`: input/output pairs, before/after, request/response.
- `rubric_scores`: criteria, scores, rationale, pass/fail.
- `file_collection`: uploaded files, knowledge libraries.
- `status`: state, confidence, approval, progress.
- `audit_log`: raw logs, traces, low-level events.
- `comparison`: versions, diffs, alternatives.

## Area Budget Rules

- Give `very_large` area to prompts, rubrics, long editors, logs under inspection, and rich evidence review.
- Give `large` area to the primary answer, work history, execution trace, tables, and main canvas.
- Give `medium` area to summaries, selected details, review scores, and validation notices.
- Keep status, filters, metadata, and secondary controls compact.
- Move heavy writing or verification out of narrow side rails into a wide editor, modal, full page, or dedicated detail surface.

## Evidence And Provenance

For AI workflow, review, orchestration, or generated-content screens, model trust explicitly:

- user request
- final answer
- step input
- step output
- agent role
- reviewer evaluation
- organizer decision
- next instruction
- confidence or status
- raw logs only after structured evidence

## Rejection Checks

Redraw from the plan when:

- the screen is a plausible component stack but not a decision aid;
- the primary answer is hidden behind logs or metrics;
- long prompts or rubrics are squeezed into a narrow pane;
- the chosen screen pattern fights the object model or is scored below 80 in `screen-pattern-quality-audit.md`;
- state and evidence are represented only as generic badges;
- input/view information patterns are not identified before choosing controls;
- information units are not decomposed before choosing controls;
- repeated same-meaning input is not audited before choosing controls;
- already-known, same-as, extracted, or role-owned values are shown as blank fields;
- repeated similar items have no copy, template, bulk-add, import, or generation affordance;
- a supporting surface interrupts the primary path without a user decision that requires it;
- a transition label names a destination instead of the trigger that caused the transition;
- a failure, empty, blocked, or recovery state is named in the plan but not represented in the wireframe;
- rejected patterns are not named, so the same mistake can return.






