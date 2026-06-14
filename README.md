# Hachi UI Skill

Hachi UI is an agent skill for creating editable UI prototype screens as standalone SVG files.

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
```
