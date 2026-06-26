# Wireframe First

Use this reference before visual design for SaaS, tools, dashboards, mobile apps, onboarding, settings, admin, CRM, workflow, and other application screens.

## Purpose

Use monochrome wireframes to prove navigation, information hierarchy, state, and user decisions before adding beauty. A beautiful screen with a broken workflow is a failed prototype.

## Constraints

- Use only white, black, and grays.
- Do not use brand colors, gradients, shadows, textures, photos, decorative icons, or visual effects.
- Use simple boxes, lines, labels, arrows, tabs, tables, forms, and status chips.
- Use real labels, not lorem ipsum.
- Prefer 3-5 linked screens for workflows.
- Prefer left-to-right flow for sequential app journeys. Use `flow-wireframe-template.md` and a wider SVG canvas instead of wrapping screens into multiple rows when that improves readability.
- Avoid left/right split layouts in the first pass unless the task explicitly requires simultaneous comparison, selection/detail, edit/preview, or canvas/inspector.
- Match the user's language for UI labels, notes, and screen contracts. If the user writes Japanese, produce Japanese wireframes.
- Place screen contracts outside each screen frame, near the screen they describe. Do not put review annotations inside the product UI.

## Screen Contract

Define this for every screen:

| Field | Question |
|---|---|
| User question | What does the user need answered here? |
| Object | What entity is the screen about? |
| State | What current status is being represented? |
| Primary action | What is the next intended action? |
| Secondary action | What else can the user safely do? |
| Back/cancel | How does the user retreat? |
| Failure/empty | What happens when there is no data, invalid input, or a blocked action? |
| Next screen | Where does the primary action lead? |
| Transition trigger | What exact click, selection, submit, validation result, or system event moves to that screen? |

Screen contracts are not UI copy. Keep them outside the drawn screen, like annotations around a wireframe.

## App Flow Skeletons

For 3-5 screen flows, apply `flow-wireframe-template.md` before drawing.

Use one of these before high fidelity:

- `Entry -> Overview -> Detail -> Action -> Result`
- `Empty -> Connect data -> Validate -> First useful view`
- `Inbox -> Item detail -> Assign/resolve -> Confirmation -> Next item`
- `List -> Filter -> Bulk select -> Review changes -> Apply`
- `Create -> Configure -> Preview -> Confirm -> Done`

## Transition Labels

Label every arrow between screens. The label must describe the trigger, not only the destination.

Good labels:

- `「連携する」をクリック`
- `OAuth成功`
- `「次へ」をクリック`
- `検証エラー: 役割未設定`
- `「役割を修正」をクリック`
- `生成完了`
- `「レビューする」をクリック`

Bad labels:

- `次へ`
- `詳細`
- `完了`
- `画面遷移`
- Unlabeled arrows

## Wireframe Review

Reject and redraw if any of these are true:

- The user cannot tell what to do next.
- A transition arrow is unlabeled or says only where it goes.
- The target screen does not match the action or validation result that caused it.
- A screen contract appears inside the product UI frame.
- A sequential flow wraps into rows even though a wider left-to-right canvas would be clearer.
- The primary action appears before enough context to decide.
- There is no back, cancel, or recovery path.
- Empty, error, loading, or confirmation states are missing where they affect the flow.
- The selected layout pattern fights the object model.
- The screen is split into two large panes without a clear reason both must stay visible.
- The wireframe depends on color to explain state.
- The flow skips setup, permissions, import, or validation when those are necessary.

## Promotion To Visual Design

Only move to visual design when:

- The flow can be explained in one sentence.
- Each screen has one dominant job.
- The next action and recovery path are visible.
- The object model is stable.
- The wireframe would still work if visual polish were removed.
