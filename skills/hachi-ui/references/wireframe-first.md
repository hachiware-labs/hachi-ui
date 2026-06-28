# Wireframe First

Use this reference before visual design for SaaS, tools, dashboards, mobile apps, onboarding, settings, admin, CRM, workflow, and other application screens.

## Purpose

Use monochrome wireframes to prove navigation, information hierarchy, state, and user decisions before adding beauty. Before wireframing product UI, complete semantic UI planning: product thesis, user decisions, information units, information shapes, screen pattern, element mapping, area budget, gaze route, and evidence/provenance needs. A beautiful screen with a broken workflow is a failed prototype.

For reusable app/product work, create or update `UI_PLAN.md` before drawing. The wireframe should visualize the screen inventory, flow causality, information plan, field responsibility, input friction audit, state, and recovery paths from that file.

## Constraints

- Use only white, black, and grays.
- Do not use brand colors, gradients, shadows, textures, photos, decorative icons, or visual effects.
- Use simple boxes, lines, labels, arrows, tabs, tables, forms, timelines, input/output pairs, evidence blocks, and status chips.
- Use real labels, not lorem ipsum.
- Prefer 3-5 linked screens for workflows.
- Prefer left-to-right flow for sequential app journeys. Use `flow-wireframe-template.md` and a wider SVG canvas instead of wrapping screens into multiple rows when that improves readability.
- Avoid left/right split layouts in the first pass unless the task explicitly requires simultaneous comparison, selection/detail, edit/preview, or canvas/inspector.
- Match the user's language for UI labels, notes, and screen contracts. If the user writes Japanese, produce Japanese wireframes.
- Place screen contracts outside each screen frame, near the screen they describe. Do not put review annotations inside the product UI.

## Before The Screen Contract

For product UI, write or infer the UI Element Plan from `semantic-ui-planning.md` first. The screen contract should be a result of that plan, not a substitute for it. If long prompts, rubrics, logs, or evidence review appear in the plan, allocate enough space before drawing.

If the screen contains input, also run the field responsibility classification and input friction audit from `input-friction-patterns.md`. The wireframe should show whether values are inherited, copied from earlier steps, extracted from files, suggested from history, selected from templates, corrected, reviewed only, exception-only, or genuinely typed from blank.

When `UI_PLAN.md` exists, update it before changing the wireframe. Do not make the SVG the only place where screen purpose, handled information, or transition logic is recorded.

## Flow Wireframes vs Full-Scale Screens

フロー用ワイヤーフレームは、ナビゲーション、状態遷移、画面契約、フロー因果を検証するためのものです。小さなフロー枠は、デスクトップ画面の実UI密度が成立している証明ではありません。

フロー画面がデスクトップアプリケーションの画面を表す場合、その小さな枠を最終レイアウトとして扱わないでください。フローが受け入れられた後、または密度、コピー量、テーブル、エディタ、タイムライン、証跡、レビュー面が重要な場合は、少なくとも1つのフルスケール画面ワイヤーフレームを作成してください。

既定サイズ:

- フローストーリーボード: `flow-wireframe-template.md` の左から右へのテンプレート。
- デスクトップフルスケール画面: `1440x1024`。
- モバイルフルスケール画面: `390x844`。

フロー枠ではUI領域を圧縮してもよいですが、次の判断には使わないでください:

- 最終フォントサイズ。
- テーブル密度。
- 行折り返し。
- サイドバー幅。
- インスペクター幅。
- エディタやタイムラインの収容量。
- 必要な操作がすべてファーストビューに収まるか。

デスクトップのフルスケールワイヤーフレームでは、現実的なUI密度を使ってください:

- 補助テキスト `12px`、本文/テーブル `13-14px`、セクション見出し `16-18px`、ページ見出し `20-24px` を目安にする。
- SVGプロトタイプだからといって文字を大きくしない。
- コントロールを実プロダクトとして妥当な寸法にする。
- 現実的な行高、列数、スクロール領域を示す。
- 意図的なスクロール領域を明示する。
- 長い日本語ラベルが重ならず収まることを確認する。

テーブル、タイムライン、プロンプトエディタ、ルーブリック、証跡レビュー、インスペクターを含む画面は、ビジュアルデザインへ進む前にフルスケール版を作成してください。

90点台を狙うフルスケール画面では、次の具体性まで描いてください:

- 実データの具体性: 抽象ラベルだけでなく、成果物名、差分概要、レビュー観点、次の停止条件が読めること。
- 状態バリエーション: 処理中だけでなく、質問あり、回復が必要、承認待ち、失敗、完了などの断片が同じ画面内で確認できること。
- 証跡密度: インスペクターや証跡ペインに `入力 -> 出力 -> 判断 -> 次の指示` のつながりが見えること。
- 状態別主操作: `次へ` のような汎用操作ではなく、状態に応じて `Reviewを実行`、`質問に回答`、`回復案を見る`、`承認を依頼` のように操作が変わること。
- スクロール検証: 長いタイムラインや証跡が入った時の表示容量、折りたたみルール、残件数、スクロール位置がわかること。
- 視線誘導: 主領域、文脈領域、証跡領域の強弱を明確にし、均等な3カラムに見せないこと。
- プロダクト固有性: ledger、agent handoff、evidence trail、run recordなど、対象プロダクトらしい構造をモノクロでも表現すること。

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

## Primary Path Discipline

Before drawing a multi-screen flow, classify each screen as one of these:

- `primary`: required to complete the user's main job.
- `recovery`: required when validation, failure, empty state, or risk blocks progress.
- `supporting`: useful reference such as library, metrics, logs, templates, settings, or help.
- `result`: confirmation, first useful output, or next actionable state.

The default flow should be mostly `primary`, `recovery`, and `result`. Do not place a `supporting` screen in the middle of the main path unless the user must decide from that supporting information before acting. When supporting information matters, show a compact card, optional branch note, or secondary action instead of making it the next primary screen.

Required for each drawn screen:

- one dominant information unit answering the screen contract;
- one visible primary action;
- one retreat path such as back, cancel, edit, undo, or skip when the user might need it;
- one state or exception fragment when the product can be empty, invalid, blocked, failed, waiting, or completed.

For input-heavy screens, also include at least one friction-reduction unit when relevant:

- inherited value row, such as `プロフィールから`, `前回値`, `選択中の対象から`, or `申請者から`;
- extracted value correction, such as `OCRから`, `CSVから`, `検査結果から`, or `ログから`;
- review-only block for values that matter to judgment but should not be retyped;
- same-as or copy control, such as `前回と同じ`, `請求先と同じ`, `テンプレートから作成`, or `複製`;
- exception-only reason field that appears only after override, rejection, escalation, or deviation;
- owner handoff row instead of asking the current user to fill another role's information.

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
- The SVG introduces screens, inputs, states, or transitions that are not represented in `UI_PLAN.md`.
- A sequential flow wraps into rows even though a wider left-to-right canvas would be clearer.
- The primary action appears before enough context to decide.
- There is no back, cancel, or recovery path.
- Empty, error, loading, or confirmation states are missing where they affect the flow.
- A supporting screen interrupts the main path where a decision, recovery, or result screen should follow.
- The plan names empty, error, blocked, or recovery states but the wireframe does not show them as visible UI fragments.
- The same meaning is entered more than once instead of being inherited, copied, confirmed, or corrected.
- Required details from `UI_PLAN.md` are drawn as blank fields without separating user input, selection, auto-filled, review-only, exception-only, and evidence/display.
- Extracted or uploaded data is shown and then retyped from blank instead of corrected.
- Repeated similar rows have no copy, template, bulk-add, import, or generation option.
- Exception reason fields appear before the user chooses an exception action.
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

