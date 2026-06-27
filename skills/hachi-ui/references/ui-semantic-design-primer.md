# UI Semantic Design Primer

Use this primer before drawing any app, SaaS, AI workflow, dashboard, admin, onboarding, settings, or tool UI. Its job is to turn a product brief into a semantic UI plan: what the product is about, what the user must understand or decide, what information units exist, and which UI elements are justified.

This is the background knowledge layer for Hachi UI. It draws from object-oriented UX, task analysis, information architecture, interaction design, and evidence-centered AI workflow design, but keeps the output practical enough for SVG prototyping.

## Core Thesis

Do not start from screens, cards, sidebars, or components. Start from the user's work.

A good UI is a semantic arrangement of objects, facts, states, relationships, actions, evidence, and recovery paths. Visual layout comes after those meanings are clear.

## The Pre-Drawing Questions

Answer these before wireframing:

1. What is the product trying to make possible, faster, safer, or more trustworthy?
2. Who is the user at this moment, and what pressure are they under?
3. What core object is the user thinking about: task, file, account, workflow, event, rule, artifact, source, message, record, incident, or metric?
4. What does the user need to decide, input, verify, compare, repair, approve, or understand?
5. What information units are necessary for that decision?
6. For each unit, is the user entering it, viewing it, editing it, verifying it, comparing it, or recovering from it?
7. Which units deserve wide area because they carry writing, comparison, evidence, audit, or risk?
8. What state can each unit be in: empty, draft, running, invalid, stale, conflicted, approved, failed, blocked, recovered?
9. What evidence or provenance must be visible for the user to trust the screen?
10. What should the user's gaze encounter first, second, and last?

## Object-First Thinking

Before drawing layout, identify the user's mental objects.

Examples:

- AI workflow: Work, Run, AgentStep, Evidence, Evaluation, Decision.
- Admin product: User, Role, Permission, Resource, InheritedScope, AuditEvent.
- Import product: SourceFile, SourceField, TargetField, Mapping, ValidationIssue, Commit.
- Operations product: Incident, AlertGroup, Owner, ActionItem, TimelineEvent, Update.
- Analytics product: Metric, Segment, Baseline, Annotation, Anomaly, Recommendation.

For each core object, ask:

- What properties identify it?
- What state changes matter?
- What actions are possible?
- What relationships must be understood?
- What evidence proves it is correct, current, or safe?

If the object model is vague, the UI will usually collapse into generic cards, dashboards, or split panes.

## Task And Decision Thinking

A screen should answer a user question, not merely expose data.

Convert the job into decision language:

- Instead of "show dashboard": "What changed, why, and what should I do next?"
- Instead of "settings page": "Which setting blocks the desired behavior, and what is the impact of changing it?"
- Instead of "AI run log": "Can I trust the answer, and which step explains the result?"
- Instead of "upload screen": "Which source is valid, what failed, and can I safely commit?"
- Instead of "approval queue": "Which item needs my decision now, and what evidence supports it?"

Every major UI region should map to one of these questions.

## Information Unit Extraction

Break the screen into semantic units before choosing components.

A useful unit has:

- a user question;
- a data shape;
- a state model;
- a trust or validation requirement;
- an action or reason for being read;
- an area budget.

Good units:

- final answer summary;
- source evidence strip;
- selected record detail;
- field mapping row;
- validation issue group;
- permission scope row;
- timeline step;
- decision queue item;
- metric insight block;
- relationship node detail.

Weak units:

- card;
- left panel;
- form section;
- table area;
- sidebar item;
- modal content.

Those are containers, not meanings.

## Input And Viewing Intent

The same information needs different UI when the user is entering, scanning, verifying, or comparing it. Use `information-shape-catalog.md` to classify intent before choosing controls.

Common input intents:

- naming something;
- asking in natural language;
- writing long-form content;
- filling structured fields;
- configuring rules;
- choosing or classifying;
- setting numeric thresholds;
- uploading sources;
- mapping relationships;
- granting permission;
- annotating a region/span/node;
- entering credentials;
- confirming a destructive action.

Common viewing intents:

- understanding one object;
- scanning dense records;
- inspecting details;
- checking readiness;
- following a timeline;
- trusting evidence;
- comparing versions;
- interpreting metrics;
- triaging alerts;
- understanding dependencies;
- previewing an artifact;
- following a thread;
- diagnosing invalid state;
- activating an empty product.

A control is wrong when it ignores intent: a toggle for scope, a card for comparison, a KPI without interpretation, a textarea for a structured rule, or a raw log for audit.

## Area Budget Heuristic

Give the most area to the hardest cognition, not to the most decorative region.

Large or very large area goes to:

- long writing;
- prompt/rubric editing;
- comparison/diff review;
- evidence and provenance review;
- dense records under selection or bulk action;
- timelines under audit;
- canvas or dependency maps;
- validation and recovery when blocked.

Compact area goes to:

- navigation;
- status chips;
- metadata;
- filters;
- secondary actions;
- simple confirmations.

If a long prompt, rubric, diff, map, or evidence review is squeezed into a side rail, the semantic plan is wrong.

## Gaze Route

Define the gaze path before drawing.

Common routes:

- Claim -> proof -> action.
- Object -> state -> action -> related facts.
- Queue -> selected item -> evidence -> decision.
- Input -> validation -> preview -> commit.
- Metric -> anomaly -> explanation -> recommended action.
- Timeline -> failed step -> evidence -> recovery.
- Empty state -> activation task -> sample/preview -> first action.

Do not let navigation be the loudest visual signal unless navigation is the user's job.

## State And Recovery

State is not decoration. It tells the user what can happen next.

For every major information unit, consider:

- empty;
- draft;
- loading/running;
- invalid;
- stale;
- conflicted;
- selected;
- blocked;
- approved/rejected;
- completed;
- failed;
- undo/recovery available.

If a screen can fail but has no recovery path, it is not ready for high-fidelity styling.

## Evidence And Trust

AI, automation, admin, analytics, and operations screens need trust modeling.

Show enough of:

- input;
- output;
- source;
- transformation;
- actor/role;
- confidence/status;
- evaluation/rubric;
- reviewer decision;
- timestamp/freshness;
- raw fallback after structured evidence.

Do not make raw logs primary unless the user is explicitly debugging raw logs.

## Choosing The Pattern Layer

Use Hachi UI's pattern language in this order:

1. `ui-semantic-design-primer.md`: decide the product thesis, objects, user decisions, information units, state, evidence, area budget, and gaze route.
2. `semantic-ui-planning.md`: write the UI Element Plan.
3. `information-shape-catalog.md`: classify input/view information intent.
4. `screen-pattern-catalog.md`: choose the whole-screen work pattern.
5. `screen-pattern-quality-audit.md`: avoid weak generic patterns.
6. `information-unit-patterns.md`: choose repeated or dominant unit patterns.
7. `input-element-catalog.md`: choose atomic controls and displays.
8. `wireframe-first.md`: draw the monochrome structure.
9. `design-system-after-wireframe.md`: define visual system only after the meaning works.

## Common Failure Modes

Redesign from semantics when:

- the UI is a plausible component stack but not a decision aid;
- the screen starts from a sidebar/split layout instead of the user's work;
- object identity and state are scattered;
- the primary answer is hidden behind metrics or logs;
- a table is used when the user needs comparison, evidence, or recovery;
- cards are used because the content is unknown;
- inputs are selected before the input intent is known;
- the screen has no explicit state model;
- the user cannot tell what action produced the next screen;
- high-fidelity styling is compensating for a weak information model.

## Minimal Semantic Plan

Before drawing, produce at least this structure in scratch notes:

```yaml
product_thesis: "..."
core_objects:
  - name: "..."
    properties: ["..."]
    states: ["..."]
    relationships: ["..."]
user_decisions:
  - question: "..."
    risk: "low | medium | high"
information_units:
  - id: "..."
    user_intent: "input | view | edit | verify | compare | recover"
    shape_pattern: "..."
    unit_pattern: "..."
    state_model: ["..."]
    evidence_need: "none | light | strong | audit"
    area_need: "compact | medium | large | very_large"
screen_pattern:
  name: "..."
  reason: "..."
gaze_route:
  - "..."
rejected_patterns:
  - name: "..."
    reason: "..."
```

Draw only after this plan explains why the screen exists and what the user can decide from it.
