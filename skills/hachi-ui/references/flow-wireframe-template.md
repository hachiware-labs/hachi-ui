# Flow Wireframe Template

Use this reference for stable SVG output when the task asks for an app flow, onboarding flow, setup flow, state sequence, or 3-5 connected product screens.

## Default Layout

Use a single left-to-right row. Do not wrap to a second row unless the user asks for a compact poster, print layout, or comparison matrix.

Default constants:

- `marginX = 56`
- `topTitleY = 62`
- `screenW = 500`
- `screenH = 390`
- `gap = 96`
- `contractY = 126`
- `contractH = 58`
- `screenY = 210`
- `arrowY = 405`
- `canvasH = 760`
- `canvasW = marginX * 2 + screenCount * screenW + (screenCount - 1) * gap`

Common widths:

- 3 screens: `1804x760`
- 4 screens: `2400x760`
- 5 screens: `2996x760`

For larger UI frames, increase `screenW`, `screenH`, `gap`, and `canvasW` together. Keep one row.

## Not A Density Proof

フロー枠は導線と状態遷移を読むための圧縮表現です。デスクトップアプリ画面を表している場合でも、フロー枠だけで実UI密度、テーブル行数、エディタ容量、インスペクター幅、サイドバー幅、行折り返し、ファーストビュー内の操作収容を判断しないでください。

次のいずれかが重要なら、フロー承認後またはビジュアルデザイン前にフルスケール画面を別SVGで作成します:

- テーブル、密な一覧、カラム設計。
- タイムライン、監査ログ、実行トレース。
- プロンプト、長文エディタ、ルーブリック。
- 証跡レビュー、比較、差分、検証面。
- インスペクター、設定、フォーム、承認理由。
- 長い日本語ラベルや説明文。

フルスケール画面の既定:

- デスクトップ: `1440x1024`。
- モバイル: `390x844`。
- ファイル名: `work-request-composer-1440.svg`, `work-run-trace-1440.svg`, `result-review-1440.svg` のように画面名とサイズを含める。

## Screen Slots

For screen index `i`, zero-based:

- `x = marginX + i * (screenW + gap)`
- Contract block: `x, contractY, screenW, contractH`
- Screen frame: `x, screenY, screenW, screenH`
- Header inside screen: `x + 24, screenY + 24, screenW - 48, 48`
- Primary content starts around `screenY + 110`
- Primary action row starts around `screenY + screenH - 105`

Keep each screen self-contained. Align all screen frames to the same `y` and height.

## Screen Contract Blocks

Place one contract block above every screen frame. These blocks are review annotations, not product UI.

Required text:

- `SCREEN 01 CONTRACT`
- `問い: ...`
- `主操作: ...`
- Add `種別`, `退避`, `副操作`, `失敗`, or `空状態` when relevant.

Contract rules:

- Keep contracts outside the screen frame.
- Use at most two text lines per contract block.
- Do not repeat long UI explanations inside the screen.
- If the user's language is Japanese, write contracts and UI copy in Japanese.

## Transition Arrows

Between each adjacent screen:

- Draw a horizontal arrow from the right edge of screen `i` to the left edge of screen `i + 1`.
- Put the arrow on `arrowY`.
- Put the label in the gap between screens.
- Label the trigger, not the destination.

Good labels:

- `連携する`
- `次へ / OAuth成功`
- `検証エラー`
- `役割修正 / 生成完了`
- `保存 / プレビュー更新`

Avoid:

- `次へ` when validation or system result also matters.
- `詳細`, `完了`, or other destination-only labels.
- Labels that overlap a screen frame.

## State Coverage

Every flow must include:

- Entry or current state.
- Primary configuration, selection, or action screen.
- Validation, error, loading, or confirmation state when the system can block progress.
- First useful result screen.
- A back, cancel, skip, or edit path where the user may need to retreat.

Do not add a separate screen for every secondary action. If a secondary action matters, annotate its destination in the contract or add a lighter arrow.

## Per-Screen Minimum UI

Inside each screen frame, draw at least these semantic units:

- a dominant unit that answers the contract question;
- a compact state or exception unit, such as empty, blocked, invalid, failed, waiting, selected, or confirmed;
- a primary action control and one retreat control when retreat is plausible;
- a supporting evidence, detail, or option unit when the action would otherwise feel unjustified.
- a field responsibility cue on input-heavy screens, such as inherited value, selectable candidate, review-only evidence, correction table, or exception-only reason.

For AI, audit, moderation, checkout, booking, approval, import, and learning progress flows, show the reason or evidence that makes the next action trustworthy. A badge alone is not enough.

## Naming And Layers

Use stable SVG groups:

- `id="overview"`
- `id="screen-contracts"`
- `id="screen-01-..."`
- `id="screen-02-..."`
- `id="flow-arrows"`

Use editable text and simple primitives only. Keep monochrome colors: white, black, and grays.

## Review Checklist

Redraw before delivery if any item fails:

- The flow is not readable left to right.
- Screens wrap into rows without an explicit reason.
- A screen contract is inside a screen frame.
- A transition arrow lacks a trigger label.
- The target screen does not match the trigger.
- The primary action is unclear on any screen.
- Required details are drawn as blank inputs when they should be auto-filled, selected, reviewed, corrected, or displayed as evidence.
- A required failure or validation state is missing.
- A required recovery, edit, retry, undo, or cancellation path is missing.
- A supporting surface such as metrics, library, logs, or templates becomes the next screen without being the user's required decision.
- Japanese user requests produce English UI labels.
- Text overlaps, clips, or exceeds its button/card.
- The SVG canvas crops any screen, label, or arrow.
