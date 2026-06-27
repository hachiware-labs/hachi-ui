# Semantic UI Planning

Use this reference before wireframing product screens, SaaS tools, AI workflows, dashboards, settings, admin tools, mobile task screens, and other application UI.

## Purpose

Translate the brief into a UI Element Plan before drawing boxes. Decide what the user must inspect, decide, write, compare, verify, or act on, then map those needs to screen patterns, UI elements, layout attention, state, and evidence.

A screen should not be a list of plausible components. It should be a semantic arrangement of information units that helps the user make the next decision.

## Planning Order

1. Product thesis
2. User job
3. Core objects
4. User decision points
5. Information units
6. Information shapes
7. Screen pattern
8. Information-unit patterns
9. Element mapping
10. Area budget
11. Gaze route
12. State coverage
13. Evidence/provenance needs
14. Rejected patterns and why

## UI Element Plan Schema

Use this structure in scratch notes or examples before drawing.

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
area_budget:
  final_answer: large
  raw_logs: collapsed
states:
  - running
  - verified
  - failed
evidence_needs:
  - input
  - output
  - review
  - decision
rejected_patterns:
  - name: generic_dashboard
    reason: "It hides the answer and evidence behind metrics."
```

## Pattern Layers

Use three layers before drawing:

- Whole-screen pattern: the complete working surface, chosen from `screen-pattern-catalog.md`.
- Information-unit pattern: repeated or dominant blocks inside the screen, chosen from `information-unit-patterns.md`.
- Input/display element: atomic controls and visual elements, chosen from `input-element-catalog.md`.

Do not jump from a whole-screen pattern directly to buttons and cards when the screen contains evidence, queues, timelines, validation, permissions, diffs, metrics, alerts, empty states, or communication threads.

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
- information units are not decomposed before choosing controls;
- rejected patterns are not named, so the same mistake can return.



