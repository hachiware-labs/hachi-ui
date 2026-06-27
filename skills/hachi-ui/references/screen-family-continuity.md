# Screen Family Continuity

Use this reference for multi-screen products, follow-up screens, settings/detail surfaces, or any request where a previous direction should continue.

## Purpose

Treat screens as a family, not isolated mockups. Preserve shared objects, navigation, density, state language, evidence model, and visual thesis.

## Screen Family Plan Schema

```yaml
product_thesis: "Inspectable AI work engine."
selected_direction: Frost
navigation_model: left_pane_tabs
core_objects:
  - Work
  - Run
  - AgentStep
  - Domain
  - ArtifactSpec
shared_state_language:
  work_status: [queued, running, reviewing, completed, failed]
  verification_status: [passed, needs_revision, failed]
primary_evidence_model:
  - final_answer
  - step_input
  - step_output
  - reviewer_evaluation
  - organizer_decision
screens:
  Work Home:
    pattern: Work Intake + History Stack
    opens: Work Detail
  Work Detail:
    pattern: Agent Execution Trace
  Domain Knowledge Settings:
    pattern: Domain Knowledge Workspace
  Artifact Editor Dialog:
    pattern: Wide Artifact Editor
```

## Continuity Rules

- Use the same object names across screens.
- Keep status names consistent between list rows, detail screens, and settings.
- Preserve selected direction unless the user asks to change it.
- Keep heavy-editing rules consistent: long prompts, rubrics, and code-like content need wide editors.
- Keep evidence hierarchy consistent: answer/claim first, structured evidence next, raw logs last.
- Reuse navigation and density decisions unless the screen type truly requires a local exception.

## Screen Relationship Map

For every screen family, name how screens open each other:

```text
Work Home
  -> click work history row
  -> Work Detail

Domain Knowledge Settings
  -> edit artifact spec
  -> Artifact Editor Dialog
```

## Continuity Failure Modes

- A detail screen uses different state names from the list.
- A settings screen introduces objects that do not appear in work evidence.
- A selected direction disappears in follow-up screens.
- A long prompt is forced into a narrow sidebar.
- Raw logs become primary despite a structured evidence model.
- Navigation changes without user reason.
