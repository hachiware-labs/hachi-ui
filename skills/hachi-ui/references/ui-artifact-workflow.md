# UI Artifact Workflow

Use this reference when creating an app flow, product prototype, dashboard, onboarding, settings surface, or any multi-screen UI. Keep intermediate artifacts few, stable, and easy to update.

## Standard Artifact Set

Use these files by default:

- `requirements.md`: user-visible requirements, assumptions, users, goals, constraints, and success criteria.
- `UI_PLAN.md`: the central semantic design artifact. It contains screen inventory, information units, input friction, flow causality, state, recovery, and rejected patterns.
- `wireframe-flow.svg`: the monochrome visual flow generated from `UI_PLAN.md`.
- `DESIGN.md`: create only when moving beyond wireframe into visual system, brand direction, high-fidelity screens, or multiple related styled screens.

Optional:

- `evaluation.md`: create only when the user asks for scoring, review history, or comparison across alternatives.

Do not split screen list, information units, input friction, and flow causality into many separate files unless the product is large enough that `UI_PLAN.md` becomes hard to scan. Prefer one authoritative planning file over many stale fragments.

## When To Create Each File

| Situation | Required artifacts |
|---|---|
| One quick screen sketch | SVG only, with a short scratch plan in the response if useful |
| Product/app screen | `UI_PLAN.md` + SVG |
| Multi-screen app flow | `requirements.md` + `UI_PLAN.md` + `wireframe-flow.svg` |
| User gives requirements directly | Treat the prompt as requirements; create `UI_PLAN.md` and SVG, create `requirements.md` only if the work should be reusable |
| High-fidelity or branded pass | Add `DESIGN.md` after the wireframe is accepted |
| Evaluation or benchmark pass | Add or update `evaluation.md` |

Legacy note: existing `semantic-plan.md` files can be read as older `UI_PLAN.md` equivalents, but new work should use `UI_PLAN.md`.

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
- state and recovery;
- secondary action;
- area budget;
- gaze route.

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
- Keep `requirements.md` user-facing and concise. Do not bury design decisions there.
- Keep `DESIGN.md` visual-system-focused. Do not duplicate all screen inventory there.
- If the SVG and `UI_PLAN.md` disagree, fix the plan first, then redraw.

## Naming Rules

- Use `UI_PLAN.md` exactly for the central plan.
- Use `wireframe-flow.svg` for a multi-screen flow.
- Use descriptive names for single screens, such as `settings-dependency-map.svg`.
- Use `DESIGN.md` only for design system decisions.
