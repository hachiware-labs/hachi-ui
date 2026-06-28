# UI Artifact Workflow

Use this reference when creating an app flow, product prototype, dashboard, onboarding, settings surface, or any multi-screen UI. Keep intermediate artifacts few, stable, and easy to update.

## Standard Artifact Set

Use these files by default:

- Requirements source: user-visible requirements, assumptions, users, goals, constraints, and success criteria. This may already exist as `requirements.md`, `PRD.md`, `concept.md`, `spec.md`, a product brief, an issue, an attached document, or the user's prompt. Create `requirements.md` only when requirements should be preserved and no equivalent durable source already exists.
- `UI_PLAN.md`: the central semantic design artifact. It contains screen inventory, information units, field responsibility, input friction, flow causality, state, recovery, and rejected patterns.
- `wireframe-flow.svg`: the monochrome visual flow generated from `UI_PLAN.md`.
- Full-scale wireframes: create when a flow screen represents a dense desktop or mobile surface that needs real layout validation, using names such as `work-request-composer-1440.svg`, `work-run-trace-1440.svg`, or `result-review-1440.svg`.
- `DESIGN.md`: create only when moving beyond wireframe into visual system, brand direction, high-fidelity screens, or multiple related styled screens.

Optional:

- `evaluation.md`: create only when the user asks for scoring, review history, or comparison across alternatives.

Do not split screen list, information units, input friction, and flow causality into many separate files unless the product is large enough that `UI_PLAN.md` becomes hard to scan. Prefer one authoritative planning file over many stale fragments.

## When To Create Each File

| Situation | Required artifacts |
|---|---|
| One quick screen sketch | SVG only, with a short scratch plan in the response if useful |
| Product/app screen | `UI_PLAN.md` + SVG |
| Multi-screen app flow | Requirements source + `UI_PLAN.md` + `wireframe-flow.svg` |
| Multi-screen flow with dense desktop screen | Requirements source + `UI_PLAN.md` + `wireframe-flow.svg` + at least one `*-1440.svg` full-scale wireframe |
| User gives requirements directly | Treat the prompt as the requirements source; create `UI_PLAN.md` and SVG, create `requirements.md` only if the work should be reusable and no equivalent durable source exists |
| High-fidelity or branded pass | Add `DESIGN.md` after the wireframe is accepted |
| Evaluation or benchmark pass | Add or update `evaluation.md` |

Legacy note: existing `semantic-plan.md` files can be read as older `UI_PLAN.md` equivalents, but new work should use `UI_PLAN.md`.

## Requirements Source Rule

Before creating `requirements.md`, look for an existing requirements-bearing source near the work:

- `requirements.md`, `PRD.md`, `concept.md`, `spec.md`, `product-brief.md`, issue text, attached documents, or the user's prompt;
- product goals, users, workflows, constraints, data requirements, states, and success criteria inside those sources;
- explicit open questions that materially affect the UI.

Do not duplicate an existing PRD, concept, or spec into a new `requirements.md` just to satisfy a filename convention. Reference the chosen requirements source from `UI_PLAN.md`, and create `requirements.md` only when the requirements need a durable local artifact and no equivalent source exists.

## UI_PLAN.md Template

Use this structure for product/app work.

```markdown
# UI Plan: Product Name

## Product Thesis
What the product makes possible, safer, faster, or more trustworthy.

## Users And Roles
Who uses it, what each role owns, and what each role should not be asked to enter.

## Core Objects
The objects users think with: task, record, request, incident, booking, claim, candidate, patient, artifact, source, rule, metric.

## Screen Inventory
| Screen | Type | User Question | Primary Action | State | Pattern |
|---|---|---|---|---|---|

## Flow Causality
| From | Trigger | To | Why This Follows |
|---|---|---|---|

## Screen Information Plan
For each screen:

- dominant information unit;
- supporting evidence;
- input/view intent;
- information shape;
- information-unit pattern;
- field responsibility classification;
- state and recovery;
- secondary action;
- area budget;
- gaze route.

## Field Responsibility Matrix
`Required detail` means information needed for judgment. It does not mean every item is a blank field. For each screen, classify handled information before choosing controls:

| Screen | User Input | User Selection | Auto-filled | Review Only | Exception-only Input | Evidence / Display |
|---|---|---|---|---|---|---|

- `User Input`: genuinely new information only this user can provide.
- `User Selection`: choice among candidates, templates, dates, roles, options, classifications, or generated variants.
- `Auto-filled`: carried from profile, selected object, previous step, integration, upload/OCR, history, schedule, or system inference.
- `Review Only`: information the user must inspect or confirm but should not retype.
- `Exception-only Input`: reason, override, rejection, escalation, deviation, or correction that appears only after the exception action.
- `Evidence / Display`: provenance, audit, reference, status, metric, or context shown to support trust.

If most items are `User Input`, challenge the design before drawing. A good product UI usually turns many required details into auto-filled, selected, reviewed, or exception-only information.

## Input Friction Audit
| Input | Source | Reuse Strategy | Shown As |
|---|---|---|---|

Classify inputs as `already_known`, `same_as_existing`, `system_inferred`, `user_selects`, `user_corrects`, `user_enters_new`, or `exception_only`.

## Screen Family Continuity
Shared navigation, object language, density, state vocabulary, evidence model, and direction choice.

## Rejected Patterns
Patterns or elements intentionally avoided and why.

## Open Questions
Only include questions that materially change the UI.
```

## Artifact Rules

- Make `UI_PLAN.md` the source of truth for the SVG. Do not let screen contracts in the SVG become the only planning artifact.
- Update `UI_PLAN.md` before redrawing when the user changes flow order, screen purpose, input burden, information units, visual direction, or state behavior.
- Classify field responsibility before drawing form controls. Do not convert all required details into visible text inputs.
- Use `wireframe-flow.svg` for navigation and state flow only. Do not use compressed flow frames to judge final font size, table density, editor capacity, sidebar width, inspector width, line wrapping, or whether controls fit above the fold.
- Before `DESIGN.md` or high-fidelity styling, create a full-scale wireframe when a screen contains a table, timeline, prompt editor, rubric, evidence review, inspector, dense form, or long Japanese labels.
- Keep the requirements source user-facing and concise. Do not bury design decisions there.
- Keep `DESIGN.md` visual-system-focused. Do not duplicate all screen inventory there.
- If the SVG and `UI_PLAN.md` disagree, fix the plan first, then redraw.

## Naming Rules

- Use `UI_PLAN.md` exactly for the central plan.
- Use `wireframe-flow.svg` for a multi-screen flow.
- Use names like `work-request-composer-1440.svg`, `work-run-trace-1440.svg`, or `result-review-1440.svg` for full-scale desktop screen validation.
- Use descriptive names for single screens, such as `settings-dependency-map.svg`.
- Use `DESIGN.md` only for design system decisions.
