# Hachi UI Skill

Hachi UI is an agent skill for creating editable UI prototype screens as standalone SVG files. It is optimized for product UI work that needs to move from semantic object/decision modeling, to semantic UI planning, to input/view information classification, to whole-screen pattern selection, to information-unit decomposition, to input/display element selection, to a clear wireframe, to a reusable design system, and then to a higher-fidelity SVG prototype.

## Workflow

Hachi UI uses a staged workflow:

1. **UI semantic design primer**: identify core objects, user decisions, information units, state, evidence, area budget, and gaze route before drawing.
2. **Semantic UI planning**: convert the product brief into product thesis, user decisions, information units, input/view information patterns, information shapes, screen pattern choices, information-unit patterns, UI element choices, gaze route, area budget, and state/evidence requirements.
3. **Direction and screen family planning**: for multi-screen products, propose named directions when useful, preserve the selected direction, and define the shared object model, navigation, density, and state language across screens.
4. **Wireframe first**: define the user question, primary action, retreat path, failure state, and transition trigger.
5. **Flow layout**: for 3-5 screen app flows, use a wide left-to-right SVG canvas instead of wrapping screens into rows.
6. **Design system pass**: after the wireframe is clear, create or update `DESIGN.md` with design tokens and rationale.
7. **High-fidelity SVG**: apply the design system to an editable SVG screen or screen sequence.
8. **Verification**: render the SVG, run the smoke check, and lint `DESIGN.md` when available.

## Quick Route

Use the smallest route that fits the request:

- **Light single screen**: semantic primer, minimal plan, wireframe, rubric.
- **Normal app/product screen**: primer, semantic plan, information shape, screen pattern, unit pattern, input/display element, wireframe.
- **AI, audit, settings, import, approval, or regulated work**: normal route plus pattern quality audit and explicit evidence/provenance modeling.
- **Multi-screen flow**: normal route plus screen family continuity, flow wireframe template, and onboarding patterns when relevant.
- **High-fidelity or brand-sensitive work**: wireframe first, then design system and frontend art direction.

## DESIGN.md

Hachi UI adopts the useful parts of Google Labs `design.md`: a persistent `DESIGN.md` file combines machine-readable YAML tokens with human-readable design rationale.

Use `DESIGN.md` when:

- a wireframe is promoted to high fidelity,
- multiple screens should share a visual system,
- brand/product assets are supplied,
- the user asks for a design system, microinteractions, or reusable UI direction.

Typical output:

```text
examples/<project>/DESIGN.md
examples/<project>/<screen-or-flow>.svg
examples/<project>/screenshots/<screen-or-flow>.png
```

Validate a design system file with:

```bash
npx -p @google/design.md designmd lint examples/<project>/DESIGN.md
```

On Windows, use the `designmd` alias rather than invoking the `.md` binary directly.

## Install with Vercel Skills

From a published Git repository:

```bash
npx skills add <owner/repo> --skill hachi-ui
```

For local testing from this repository:

```bash
npx skills add . --skill hachi-ui
```

## Use with OpenClaw and ClawHub

Install locally into an OpenClaw workspace:

```bash
openclaw skills install ./skills/hachi-ui --as hachi-ui
```

Publish to ClawHub after signing in:

```bash
clawhub login
clawhub skill publish ./skills/hachi-ui --slug hachi-ui --name "Hachi UI" --version 0.1.0 --owner <owner>
```

For catalog publishing, run a dry run first:

```bash
clawhub sync --dry-run --owner <owner>
```

## Validate

```bash
npx skills add . --list
python skills/hachi-ui/scripts/svg_smoke_check.py path/to/prototype.svg
npx -p @google/design.md designmd lint path/to/DESIGN.md
```

For restricted Windows environments, keep tool caches inside this repository:

```powershell
New-Item -ItemType Directory -Force test | Out-Null
$env:npm_config_cache = (Resolve-Path .\test).Path + '\npm-cache'
$env:PIP_CACHE_DIR = (Resolve-Path .\test).Path + '\pip-cache'
```

## Curated Examples

This repository keeps only a small number of lightweight examples:

- `examples/wireframe-briefwell-onboarding.svg`: wireframe-first app flow with external screen contracts and transition triggers.
- `examples/briefwell-boardroom.svg`: high-fidelity business app screen after a design-system pass.
- `examples/nagare-ui-element-plan.md`: semantic UI planning example for an AI workflow engine.
- `examples/nagare-screen-family-plan.md`: screen-family continuity example for related product screens.
- `examples/nagare-conversation-replay-test.md`: planning regression example for direction, correction, auditability, and wide editing behavior.

Generated screenshots, exploratory variants, per-project `DESIGN.md` files, npm caches, and Python caches should stay untracked. Keep local validation output under `examples/` or `test/`.

## Pattern Quality

The semantic design entry point is `skills/hachi-ui/references/ui-semantic-design-primer.md`. The screen catalog is evaluated in `skills/hachi-ui/references/screen-pattern-quality-audit.md`. Patterns below 80 should be replaced or repaired rather than used as primary guidance. The catalog is layered: input/view information patterns live in `information-shape-catalog.md`, whole-screen patterns live in `screen-pattern-catalog.md`, middle-layer information units live in `information-unit-patterns.md`, and atomic controls/displays live in `input-element-catalog.md`.

Current pattern coverage:

- 27 input/view information patterns.
- 57 whole-screen work patterns.
- 15 information-unit patterns.
- 47 input/display element patterns.





