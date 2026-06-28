# Design System After Wireframe

Use this reference after `UI_PLAN.md` and the wireframe prove the flow, and before creating a high-fidelity SVG screen. The goal is to make visual decisions from product purpose, handled information, user role, and brand character, not from generic polish.

This reference adopts useful ideas from Google Labs `design.md`: maintain a persistent `DESIGN.md` file that combines machine-readable tokens with human-readable design rationale. Tokens give exact values; prose explains why those values exist and how to apply them.

## Claude Design Reference Model

Use Claude Design as an operating model, not as a visual style to copy. The relevant pattern is source-driven system synthesis:

- Start from real brand and product assets when available: codebases, component libraries, screenshots, existing flows, slide decks, documents, logos, palettes, and typography specimens.
- Extract reusable decisions: color roles, typography, components, layout patterns, spacing systems, page structures, and interaction patterns.
- Generate a compact design system contract before producing high-fidelity screens.
- Validate the system with test outputs such as a landing page, dashboard, or presentation-style screen before treating it as stable.
- Iterate through targeted comments and direct edits: adjust one element or rule, then apply the change consistently across the whole design.
- Preserve handoff intent: name the components, tokens, states, and interaction notes clearly enough that a coding agent or designer can continue the work.

Do not imitate Claude or Anthropic brand visuals unless the user explicitly asks for an Anthropic/Claude-inspired concept. The skill should borrow the workflow: asset ingestion, reusable system extraction, test generation, review, publication, and later updates.

When no assets are provided, synthesize a provisional system from the product brief and clearly label it as assumed.

## Inputs

Define these before styling:

- Product purpose: what the product helps the user achieve.
- User role: operator, executive, creator, consumer, developer, admin, buyer, or other.
- Brand posture: precise, warm, luxurious, technical, calm, playful, editorial, clinical, rugged, or another specific stance.
- Trust level: low-risk exploration, professional productivity, financial/legal/medical confidence, security, or mission-critical operation.
- Data density: sparse, moderate, dense, real-time, archival, or comparative.
- Interaction risk: reversible, reviewable, destructive, permissioned, payment-related, or public-facing.
- Environment: desktop, mobile, large display, embedded widget, dark room, field use, or presentation.
- Source material: code, screenshots, brand files, documents, decks, competitors, or none.
- Planning source: `UI_PLAN.md` screen inventory, information hierarchy, field responsibility matrix, input friction audit, state language, and evidence model.

## Density Gate Before Styling

Do not promote a compressed flow frame directly to visual design when it represents a dense desktop screen. Before `DESIGN.md` or high-fidelity styling, create at least one full-scale wireframe when the product surface contains a table, timeline, prompt editor, rubric, evidence review, inspector, dense form, or long Japanese labels.

Use realistic UI density in that full-scale wireframe: auxiliary text around `12px`, body/table text around `13-14px`, section headings around `16-18px`, page headings around `20-24px`, plausible row heights, visible scroll regions, and controls that could exist in a real product.

For a high-confidence promotion, the full-scale wireframe should use concrete sample data, not abstract placeholders: artifact names, diff summaries, review criteria, stop conditions, state-specific primary actions, and an evidence chain from input to output to judgment to next instruction. If the screen has a timeline or inspector, show long-content capacity, folding rules, remaining counts, and visible scroll behavior before styling.

## Design System Contract

Create a compact system before drawing the final screen. When the system needs to persist across screens, write it as `DESIGN.md`.

- Source basis: supplied assets, inferred brief, competitor reference, or provisional assumption.
- Planning basis: which `UI_PLAN.md` decisions the system must support, such as dense audit work, guided consumer flow, clinical confidence, field operation, or editorial brand.
- Visual thesis: one sentence describing mood, material, density, and energy.
- Typography: family fallback, scale, weight, line height, numeral style, and where display type is allowed.
- Color roles: background, surface, text, muted text, border, accent, focus, success, warning, danger, info, and selected.
- Spacing: base unit, section gap, control gap, row height, and dense-mode rules.
- Surface model: flat, bordered, layered, glassy, tactile, editorial, or instrument-like.
- Shape: corner radius rules for controls, panels, chips, modals, and charts.
- Elevation: when shadows are allowed and what they mean.
- Icon language: outline, filled, geometric, pictorial, technical, or minimal.
- Data visualization: chart weight, grid visibility, status encoding, comparison style, and annotation style.
- Component states: rest, hover, focus, active, selected, disabled, loading, success, warning, error, empty, dirty, saved, and destructive.
- Motion feel: instant, precise, calm, elastic, cinematic, mechanical, or restrained.

Keep the contract outside the product UI when shown in the SVG. It is a design note, not product copy.

## DESIGN.md Output Contract

Create or update `DESIGN.md` when any of these are true:

- The user asks for high-fidelity screens after a wireframe.
- The user asks for a design system, brand system, product visual language, or reusable style.
- Multiple related SVG screens should share one visual system.
- The user provides brand assets, screenshots, existing UI, or a codebase to extract from.

Use this structure:

```markdown
---
version: alpha
name: Product Or System Name
description: One-line system scope
colors:
  primary: "#..."
typography:
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
rounded:
  sm: 4px
spacing:
  md: 16px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    padding: 12px
---

## Overview
...

## Colors
...

## Typography
...

## Layout
...

## Elevation & Depth
...

## Shapes
...

## Components
...

## Do's and Don'ts
...
```

Rules:

- Treat YAML tokens as normative values and Markdown prose as application rationale.
- Make the prose specific. Prefer a concrete reference world over vague adjectives like "modern", "clean", or "premium".
- Include tokens for colors, typography, rounded corners, spacing, and key components when they affect generated screens.
- Use component variants for states, for example `button-primary-hover`, `button-primary-active`, `button-primary-loading`, and `input-error`.
- Preserve custom sections if the project needs them, such as `## Motion`, `## Iconography`, `## Data Visualization`, or `## Microinteractions`.
- If the system is inferred rather than asset-derived, say so in `description` or `## Overview`.
- Do not create token values that contradict the prose.

Recommended validation when Node and network access are available:

```bash
npx -p @google/design.md designmd lint DESIGN.md
```

If comparing revisions:

```bash
npx -p @google/design.md designmd diff DESIGN-before.md DESIGN.md
```

On Windows, prefer the `designmd` alias because the `.md` suffix can collide with Markdown file associations.

## Source Extraction Checklist

If assets are available, inspect them for:

- Repeated colors and whether they are primitive tokens or semantic roles.
- Font families, scale jumps, line heights, capitalization, and number treatment.
- Button, card, nav, table, form, modal, chart, and notification patterns.
- Spacing rhythm, grid width, panel density, and row height.
- Border, radius, elevation, divider, and background rules.
- Existing error, empty, loading, selected, disabled, and success states.
- Voice and tone in labels, empty states, confirmation text, and risk warnings.

If the source material is incomplete, identify the missing system decisions and fill them conservatively from the product purpose.

## Product Archetypes

Use these as starting points, then adapt to the specific brand.

### Operational SaaS

- Visual thesis: quiet, precise, dense, low-drama.
- Use compact type, strong tables, restrained surfaces, clear status semantics, and minimal decorative effects.
- Microinteractions should confirm action, validation, save state, and error recovery quickly.

### Executive Insight

- Visual thesis: high-trust, calm, spacious, selective.
- Use fewer elements, larger summary numbers, confident typography, subdued status colors, and evidence drill-down.
- Microinteractions should reveal provenance, confidence, and next recommended decision.

### Creative Or Prosumer Tool

- Visual thesis: expressive but controlled, with the canvas or artifact as the hero.
- Use toolbars, inspectors, swatches, previews, and clear active states.
- Microinteractions should show selection, transform handles, undo, preview, and export feedback.

### Developer Or AI Workflow

- Visual thesis: technical, transparent, inspectable.
- Use logs, nodes, traces, version states, prompts, diffs, and execution feedback.
- Microinteractions should show queued, running, streamed, failed, retried, and completed states.

### Consumer Or Lifestyle

- Visual thesis: emotionally legible, tactile, approachable.
- Use warm hierarchy, clear affordances, human labels, and fewer simultaneous choices.
- Microinteractions should create confidence around completion, personalization, and recovery.

### Regulated Or High-Trust Product

- Visual thesis: sober, legible, auditable.
- Use conservative color, explicit state, clear provenance, accessible contrast, and reversible actions.
- Microinteractions should emphasize confirmation, permission, audit trail, and error prevention.

### High-End Or Luxury Product

- Visual thesis: specific, material, spacious, and quiet; never merely "premium" colors.
- Choose a concrete reference world such as private banking, gallery catalogues, board packets, fine stationery, atelier tools, or hospitality concierge systems.
- Express quality through typography contrast, restrained color scarcity, hairline rules, measured spacing, tactile surfaces, and fewer stronger focal points.
- Avoid low-contrast fashion styling, ornate borders, generic gold accents, stock luxury gradients, and decorative texture that does not clarify the user's decision.
- Microinteractions should feel precise and composed: quick state changes, no bounce, no playful overshoot, and visible confirmation for high-value actions.

## Microinteraction Model

For every primary or risky action, define:

- Trigger: click, tap, selection, drag, submit, shortcut, validation result, system event.
- Immediate feedback: visible within about 100ms.
- Progress: spinner, skeleton, progress bar, streaming text, pending row, or queued badge.
- Success: changed state, confirmation, generated result, saved marker, or next screen.
- Failure: readable cause, preserved input, retry path, and safe exit.
- Recovery: undo, edit, reconnect, rollback, or contact support when relevant.
- Duration: instant, 120ms, 180ms, 240ms, 400ms, or long-running with progress.
- Easing: linear for progress, ease-out for arrival, restrained spring for tactile tools only.

In SVG, represent microinteractions with adjacent state fragments, ghost states, small timelines, or external annotations. Do not rely on JavaScript or hidden behavior.

## Visual Promotion Checklist

Do not promote a wireframe to high fidelity until:

- The flow has one dominant user job.
- The design system contract is defined, preferably as `DESIGN.md` for reusable systems.
- The contract states whether it is asset-derived or assumed.
- At least one test output or state fragment validates the design system.
- Token values and prose rationale agree.
- The primary action has loading, success, and error behavior where relevant.
- Color roles are semantic, not decorative.
- The type scale matches the product density.
- Surfaces and shadows have meaning.
- The brand can be recognized if the logo is removed.
- The final screen still respects the wireframe's hierarchy.

## Rejection Checks

Redesign the visual pass if any are true:

- The screen is just the wireframe with nicer colors.
- The palette is a generic purple/blue SaaS gradient.
- Every component has the same radius, shadow, and card treatment.
- Microinteractions are absent for risky or long-running actions.
- Status colors conflict with the domain's trust requirements.
- The design system contradicts the user's product purpose or brand.
- Design notes appear as product UI copy.



