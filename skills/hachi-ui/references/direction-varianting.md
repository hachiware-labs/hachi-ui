# Direction Varianting

Use this reference for broad product briefs, early visual direction, or multi-screen products where the user has not chosen a clear posture.

## Purpose

Do not lock into one generic clean SaaS screen too early. Offer 2-3 named directions that differ in structure, density, trust posture, and interaction feel. Once the user selects a direction, preserve it across follow-up screens unless they explicitly change it.

## Direction Schema

```yaml
name: Frost
visual_thesis: "White, thin rules, calm trust, answer-first evidence UI."
density: moderate
navigation_model: left_pane_tabs
surface_model: flat_bordered
state_language: restrained
primary_rule: "Final answer and evidence before raw logs."
heavy_edit_rule: "Prompts and rubrics open wide editors."
```

## When To Propose Directions

Propose directions when:

- the product brief is broad or brand posture is unclear;
- the user asks for high fidelity but gives no visual system;
- multiple screens should feel like one product family;
- the screen could validly be minimal, dense, editorial, technical, or executive;
- the user is comparing taste, not only function.

Do not propose directions for a tiny correction, a known existing design system, or a narrow wireframe repair.

## Direction Examples

### Frost

- Visual thesis: white, thin gray rules, restrained, high-trust, calm.
- Density: moderate.
- Good for: AI workflow verification, review tools, knowledge settings.
- Rule: answer first, evidence second, raw logs last.

### Slate

- Visual thesis: gray panels, denser operations surface, command-center feel.
- Density: high.
- Good for: monitoring, support operations, heavy queues, incident review.
- Rule: exceptions and decisions stay visible.

### Verdant Ledger

- Visual thesis: blue-green, document-like, boardroom or audit packet.
- Density: moderate.
- Good for: executive brief, provenance, business review.
- Rule: strong focal document, restrained status semantics.

### Studio Canvas

- Visual thesis: artifact-first, broad canvas, inspector only when needed.
- Density: variable.
- Good for: creative tools, workflow builders, diagram editors.
- Rule: artifact/canvas is the hero.

## Direction Inheritance

When a user selects a direction, carry forward:

- visual thesis;
- navigation model;
- density;
- surface model;
- state language;
- primary evidence model;
- heavy-editing rule;
- typography and color posture where already defined.

If a later request conflicts, identify whether it is a direction change, screen-pattern correction, or local exception.

## Rejection Checks

Reject direction work when:

- all directions differ only by color;
- directions do not change density, surface model, or evidence hierarchy;
- the selected direction is forgotten on follow-up screens;
- the screen becomes a generic SaaS card grid despite a named direction.
