# Hachi UI Skill

Hachi UI is an agent skill for creating editable UI prototype screens as standalone SVG files. It is optimized for product UI work that needs to move from a clear wireframe to a reusable design system and then to a higher-fidelity SVG prototype.

## Workflow

Hachi UI uses a staged workflow:

1. **Wireframe first**: define the user question, primary action, retreat path, failure state, and transition trigger.
2. **Flow layout**: for 3-5 screen app flows, use a wide left-to-right SVG canvas instead of wrapping screens into rows.
3. **Design system pass**: after the wireframe is clear, create or update `DESIGN.md` with design tokens and rationale.
4. **High-fidelity SVG**: apply the design system to an editable SVG screen or screen sequence.
5. **Verification**: render the SVG, run the smoke check, and lint `DESIGN.md` when available.

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

Generated prototype examples, screenshots, npm caches, and Python caches should stay untracked. Keep them under `examples/` or `test/` for local validation only.

