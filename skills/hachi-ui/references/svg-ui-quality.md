# SVG UI Quality Checklist

Use this checklist after drafting a UI prototype SVG, especially for dense product screens.

## Structure

- Root `<svg>` has `width`, `height`, and `viewBox`.
- The file has a short `<title>` and `<desc>`.
- Major regions are grouped with meaningful IDs.
- The root composition has a named visual strategy: F-pattern, Z-pattern, center-out, radial, comparison, process flow, or another explicit structure.
- The SVG has no script tags and no external remote asset references.
- Repeated elements use consistent spacing, sizes, and alignment.

## Layout

- Header, navigation, content, and persistent actions have clear zones.
- The primary workflow can be understood without explanatory text outside the UI.
- Claim, evidence, detail, and action are visually separated.
- The intended gaze path is visible from spacing, alignment, lines, and emphasis.
- For landing or brand screens, the first viewport works as one strong composition with a clear visual anchor.
- For product or app screens, the working surface is primary and marketing copy is secondary or absent.
- Important controls remain visible at the chosen viewport size.
- No text, icon, badge, or chart label overlaps another element.
- Tables and lists use stable row heights and predictable column alignment.

## Interface Detail

- Use native-looking UI patterns for the domain: tabs for views, segmented controls for modes, toggles for binary settings, sliders or steppers for numeric settings, menus for option sets, and icon buttons for common tools.
- Keep headings compact inside panels and dense tools.
- Avoid nested cards. Use cards only for repeated items, modals, or genuinely framed tools.
- Use icons as symbols or simple paths only when they improve recognition.
- Include realistic data labels and state text, not placeholder lorem ipsum.
- Include active, loading, empty, error, disabled, warning, confirmation, or undo states when they are part of the user's decision.

## Visual Design

- Avoid a palette dominated by one hue family.
- Reserve strong color for action, status, selection, or alerting.
- Use contrast high enough to read labels and data at 100% zoom.
- Use shadows sparingly and consistently.
- Keep rounded corners modest unless the user gives a design system with different values.
- Choose a specific aesthetic direction and make it visible through spacing, line weight, type scale, color roles, and one memorable anchor.
- Reject default AI patterns such as generic white cards, soft shadows, vague purple gradients, and decorative shapes without semantic role.
- Use no more than one accent color by default; add more only for status semantics or a supplied brand system.

## Final Verification

- Open or render the SVG and inspect it at 100% zoom.
- Check the file at a narrower preview size if the user asked for mobile or responsive variants.
- Score with `svg-composition-rubric.md`; redesign if below 80.
- Run `python scripts/svg_smoke_check.py path/to/file.svg`.
- Fix all errors from the script and decide whether warnings are acceptable for the requested fidelity.
