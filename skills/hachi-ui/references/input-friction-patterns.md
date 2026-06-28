# Input Friction Patterns

Use this reference before drawing forms, setup flows, approvals, claims, bookings, reviews, incident updates, evaluations, and any screen where a user may have to enter or confirm information. The goal is not merely fewer fields. The goal is to avoid making the user restate the same meaning in slightly different places.

## Core Rule

Treat repeated meaning as friction.

A screen has input friction when it asks for information that is already known, can be inferred from an earlier step, duplicates a similar field, or asks the user to create multiple near-identical items. Before adding a field, decide whether the information should be reused, confirmed, corrected, selected, or entered.

`Required detail` in a UI plan means information needed for judgment. It does not mean the user should type every item. Separate handled information into user input, user selection, auto-filled values, review-only values, exception-only input, and evidence/display before drawing controls.

## Friction Audit

For every input unit, classify its source:

- `already_known`: captured earlier in the flow, user profile, selected object, uploaded file, history, or integration.
- `same_as_existing`: likely identical to a previous value, such as billing/contact address, applicant/employee identity, previous reason, prior template, or last used settings.
- `system_inferred`: can be inferred from OCR, metadata, selected object, rules, calendar, source file, telemetry, or prior behavior.
- `user_selects`: should be chosen from suggestions, templates, recent values, saved presets, or matched records.
- `user_corrects`: should be prefilled and edited only when wrong.
- `user_enters_new`: genuinely new information that only the user knows.
- `exception_only`: needed only when overriding, rejecting, escalating, deviating from policy, or explaining a risk.

Default to `already_known`, `same_as_existing`, `system_inferred`, `user_selects`, or `user_corrects` before `user_enters_new`.

## Common Friction Patterns

### Duplicate Identity

Avoid asking for the same person, team, account, patient, candidate, vendor, or requester in multiple places.

- Prefer: inherit from selected object, show as read-only with `change` action.
- Use when: expense claimant, candidate, patient, assignee, customer, organizer, approver.
- Repair: replace repeated fields with an object header or inherited value row.

### Same-As Defaults

Avoid separate fields for values that are commonly identical.

- Prefer: `same as previous`, `same as billing`, `use last setting`, `copy from selected template`.
- Use when: addresses, contacts, schedules, notification recipients, payment details, policy reasons, report sections.
- Repair: show one source value, a checked reuse control, and an edit override.

### Repeated Similar Items

Avoid making the user create many near-identical rows, tasks, questions, rules, or reminders one by one.

- Prefer: bulk add, duplicate row, pattern repeat, generated set, import, or template.
- Use when: checklist items, rubric criteria, interview questions, follow-up tasks, alert actions, expense attendees, maintenance steps.
- Repair: group repeated items and expose batch editing or template selection.

### Redundant Confirmation

Avoid asking the user to confirm the same fact across multiple screens.

- Prefer: one confirmation moment with a persistent confirmed state.
- Use when: policies, consent, cancellation terms, destructive actions, payment details, medical instructions.
- Repair: show `confirmed at previous step` with edit/back action.

### Rewriting Instead Of Editing

Avoid making users rewrite text that the system can draft from known facts.

- Prefer: auto-draft, template, suggested phrase, previous note, or generated summary with edit.
- Use when: incident status updates, patient contact scripts, handoff notes, approval rationale, rejection reasons, hiring feedback.
- Repair: create a draft from evidence and ask the user to correct only uncertain parts.

### Exception Reason Overuse

Avoid asking for a reason before there is an exception.

- Prefer: no reason input on the happy path; require concise reason only for override, rejection, escalation, policy deviation, or destructive change.
- Use when: expense exceptions, moderation actions, hiring rejection, incident escalation, access overrides.
- Repair: keep reason fields hidden or compact until the exception action is selected.

### Re-entering Extracted Data

Avoid showing OCR, import, file metadata, telemetry, or integration data and then asking the user to type it again.

- Prefer: extracted values with confidence, mismatch markers, and correction controls.
- Use when: receipts, lab results, CSV import, logs, booking details, identity records.
- Repair: use a comparison/correction table, not blank fields.

### Split Ownership

Avoid asking one role to enter information owned by another role.

- Prefer: assign, request, or wait state for the owner.
- Use when: approver comments, interviewer feedback, doctor instruction, finance account data, incident owner action.
- Repair: replace the field with `request from owner`, due date, and status.

## Planning Fields

Add this to a UI Element Plan when input appears:

```yaml
field_responsibility:
  user_input:
    - "補足メモ"
  user_selection:
    - "候補日時"
  auto_filled:
    - "患者基本情報"
  review_only:
    - "検査値"
  exception_only_input:
    - "例外理由"
  evidence_display:
    - "カルテ履歴"
input_friction_audit:
  - input: "支払先口座"
    source: "already_known"
    reuse_strategy: "vendor profile value with edit action"
    shown_as: "read-only inherited row"
  - input: "例外理由"
    source: "exception_only"
    reuse_strategy: "ask only after policy override"
    shown_as: "reason note on override path"
```

## Wireframe Requirements

Show friction reduction directly in the wireframe:

- Do not draw all required details as blank fields. Show many of them as inherited rows, review blocks, evidence panels, selected chips, or correction tables.
- Prefilled or inherited values should look different from blank fields.
- Reused values should show their source, such as `前回値`, `プロフィールから`, `領収書OCR`, `選択した候補者`, or `医師指示から`.
- Repeated similar rows should have `一括追加`, `複製`, `テンプレート`, or `前回からコピー`.
- Correctable extracted values should show confidence, mismatch, or correction affordance.
- Exception-only fields should appear only after the exception action, or as a collapsed conditional fragment.

## Rejection Checks

Redraw or revise the plan when:

- the same identity, address, requester, assignee, role, or object is entered more than once;
- a `Required detail` list is converted directly into blank input fields without field responsibility classification;
- an uploaded/imported/extracted value is retyped instead of corrected;
- a user must create several similar items one by one without template, copy, or bulk controls;
- a reason field appears on the happy path when it is only needed for exception or override;
- one role is asked to fill information that another role owns;
- the same confirmation appears on multiple screens without carrying forward its confirmed state;
- the UI contains many optional fields before the user has enough context to know whether they matter.
