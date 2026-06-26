---
version: alpha
name: Briefwell Verdant Boardroom
description: Provisional high-trust design system for a meeting intelligence SaaS that turns company signals into executive meeting briefs.
colors:
  primary: "#0E2F2D"
  graphite: "#263C39"
  text-muted: "#637672"
  paper: "#EFF6F3"
  vellum: "#F8FCFA"
  surface: "#FFFFFD"
  surface-raised: "#FFFFFF"
  border: "#CBDDD7"
  hairline: "#E4EFEB"
  accent: "#0D6F62"
  accent-pressed: "#064D45"
  accent-soft: "#DCEFEA"
  success: "#22765F"
  warning: "#65724A"
  danger: "#365C6B"
  focus: "#276B91"
  selected: "#CFEAE2"
typography:
  display-md:
    fontFamily: "Yu Mincho, Hiragino Mincho ProN, Georgia, serif"
    fontSize: 34px
    fontWeight: 600
    lineHeight: 1.16
  headline-md:
    fontFamily: "Inter, Yu Gothic, Meiryo, sans-serif"
    fontSize: 20px
    fontWeight: 720
    lineHeight: 1.24
  body-md:
    fontFamily: "Inter, Yu Gothic, Meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.58
  label-md:
    fontFamily: "Inter, Yu Gothic, Meiryo, sans-serif"
    fontSize: 11px
    fontWeight: 720
    lineHeight: 1.2
  data-sm:
    fontFamily: "IBM Plex Mono, Consolas, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
rounded:
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
components:
  page-shell:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.primary}"
  desk-mat:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface-raised}"
    rounded: "{rounded.lg}"
  ledger-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: 24px
  raised-sheet:
    backgroundColor: "{colors.surface-raised}"
    rounded: "{rounded.sm}"
    padding: 16px
  metadata-label:
    textColor: "{colors.text-muted}"
    typography: "{typography.label-md}"
  divider-border:
    backgroundColor: "{colors.border}"
    size: 1px
  divider-hairline:
    backgroundColor: "{colors.hairline}"
    size: 1px
  accent-rule:
    backgroundColor: "{colors.accent}"
    size: 5px
  focus-ring:
    backgroundColor: "{colors.focus}"
    size: 2px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface-raised}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.surface-raised}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-active:
    backgroundColor: "{colors.accent-pressed}"
    textColor: "{colors.surface-raised}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-secondary:
    backgroundColor: "{colors.vellum}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px
  evidence-selected:
    backgroundColor: "{colors.selected}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  attention-note:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.graphite}"
    rounded: "{rounded.xs}"
  input-focus:
    backgroundColor: "{colors.surface-raised}"
    rounded: "{rounded.sm}"
  input-error:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.danger}"
    rounded: "{rounded.sm}"
  status-ready:
    backgroundColor: "{colors.success}"
    textColor: "{colors.surface-raised}"
    rounded: "{rounded.xs}"
  status-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.surface-raised}"
    rounded: "{rounded.xs}"
  status-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.surface-raised}"
    rounded: "{rounded.xs}"
---

## Overview

Briefwell should feel like a private boardroom desk prepared before an executive walks in: a deep verdant desk mat, a crisp white board packet, narrow teal markers, and proof that can be audited line by line. The product is not a chat assistant, a colorful dashboard, or a decorative AI companion. It is a quiet decision instrument for people who need to trust a generated brief before a meeting begins.

This system is provisional and inferred from the product brief, not extracted from supplied brand assets. The reference world is private banking operations, board packets, clinical research binders, and high-quality Japanese stationery. Use those references for restraint, hierarchy, and material feel; do not imitate old paper texture or luxury ornament.

## Colors

- **Primary** `{colors.primary}` is deep verdant ink. It anchors the desk-mat band, primary controls, and decisive text.
- **Graphite** `{colors.graphite}` supports secondary headings and serious explanatory copy without becoming gray filler.
- **Paper** `{colors.paper}` is the page foundation: pale blue-green linen, quiet, and suitable for long review sessions without the cheap warm cast of generic cream backgrounds.
- **Vellum** `{colors.vellum}` and **Surface** `{colors.surface}` create a layered document feel without visible texture.
- **Surface raised** `{colors.surface-raised}` is reserved for active sheets, modal decisions, and selected working objects.
- **Border** `{colors.border}` is a structural rule; **Hairline** `{colors.hairline}` is used inside panels for ledger-like separation.
- **Accent** `{colors.accent}` is clear teal, not decoration. Use it for one selected evidence source, one important transition, or one executive attention marker.
- **Selected** `{colors.selected}` and **Accent soft** `{colors.accent-soft}` are pale attention fields for selected evidence and review notes.
- **Status colors** are semantic only: success means ready, warning means review before sharing, danger means blocked or risky, and focus means keyboard or validation focus.

## Typography

Use a restrained Japanese serif display style for the main boardroom claim and meeting title. It should appear at most once per screen. Use the sans stack for all operational labels, controls, rows, and descriptions. Use the mono data style only for timestamps, source IDs, confidence values, version stamps, and audit details. Numerals should feel tabular in data regions and human in prose.

## Layout

The memorable anchor is a deep verdant desk-mat band behind a floating board packet. Prefer one broad working surface over habitual left/right splitting. The screen should read from meeting claim, to decision cards, to the brief excerpt, to evidence and action. Use generous outer margins, asymmetry, and internal hairlines rather than equal card grids.

## Elevation & Depth

Depth must imply current decision, selected evidence, or share readiness. The board packet may float above the desk mat with a restrained shadow. Static content should rely on hairlines, spacing, and tonal surfaces rather than repeated shadows.

## Shapes

Corners are precise. Use `{rounded.xs}` for status marks and attention tabs, `{rounded.sm}` for buttons and rows, `{rounded.md}` for small panels, and `{rounded.lg}` for the desk mat and main board packet. Avoid pill-heavy SaaS styling unless the object is a status capsule.

## Components

Primary buttons are deep verdant ink and should be used for exactly one next action. Hover moves to teal; active moves to pressed teal. Secondary buttons sit on vellum with a border. Evidence rows may use a selected teal rule, but the row copy must still carry the meaning. Validation and error regions must preserve the user's previous input and show the specific recovery path.

## Data Visualization

Charts should look like annotations in a board packet: thin rules, muted labels, one teal highlight, and direct notes near the data. Avoid saturated multi-series color. Confidence should be shown as a reviewable value with source count, not as a decorative gauge.

## Motion

Feedback should be immediate and controlled. Use 120ms for button state changes, 180ms for sheet transitions, and 240ms for selected evidence expansion. Long-running generation must show queued, generating, ready, and blocked states. Nothing should bounce, overshoot, shimmer, or feel playful.

## Microinteractions

- **Connect source:** rest -> focus -> connecting -> OAuth success or denial -> validation summary.
- **Generate brief:** rest -> queued -> generating with source count -> ready with confidence -> blocked with exact missing source.
- **Fix role mapping:** dirty -> validating -> saved -> generation resumes.
- **Select evidence:** row rest -> hover hairline -> selected teal rule -> provenance drawer updates.
- **Share brief:** confirm recipient -> sending -> shared -> undo available.

## Do's and Don'ts

- Do make the selected meeting or brief the strongest signal, even without the logo.
- Do use the dark desk mat, blue-green linen field, deep ink, teal emphasis, and hairline rules as a system, not as decoration.
- Do keep the main action near the evidence needed to decide.
- Do show failure causes and recovery paths in the same region.
- Do keep colors semantic and scarce.
- Do use source and provenance labels whenever generated content appears.
- Don't use generic purple or blue SaaS gradients.
- Don't hide blocked states behind a toast.
- Don't use equal-weight cards when a ledger sheet, row group, or evidence list is clearer.
- Don't make luxury mean low contrast, ornate borders, or decorative texture.
- Don't make the assistant persona louder than the meeting brief.
