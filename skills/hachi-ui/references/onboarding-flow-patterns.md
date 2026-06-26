# Onboarding And Initial Setup Flows

Use this reference when designing signup, workspace creation, first run, empty states, imports, integrations, permissions, or product activation.

## Principle

Initial setup is not a decorative welcome flow. It is the bridge from an empty product to the first useful screen.

Every transition must show what caused it: a user click, OAuth success/failure, validation result, import completion, skipped optional step, or system-generated first useful view.

## Common Flow Types

### Workspace Creation

Flow:

`Account -> Workspace name -> Team/role -> Preferences -> First workspace`

Typical triggers:

- `「ワークスペースを作成」をクリック`
- `チーム名を入力`
- `「招待をスキップ」をクリック`
- `作成成功`

Must show:

- What is being created.
- Who can access it.
- Whether settings can be changed later.
- The first useful destination after creation.

### Data Import

Flow:

`Choose source -> Map fields -> Validate -> Preview -> Import progress -> First useful view`

Typical triggers:

- `CSVを選択`
- `フィールド対応を保存`
- `検証エラー`
- `「インポート開始」をクリック`
- `インポート完了`

Must show:

- Sample rows or objects.
- Required vs optional fields.
- Validation errors and fix path.
- Cancel or save draft.
- Progress and partial failure.

### Integration / OAuth

Flow:

`Select provider -> Explain permissions -> Connect -> Validate access -> Configure sync -> Done`

Typical triggers:

- `「連携する」をクリック`
- `OAuth成功`
- `OAuth拒否`
- `権限不足`
- `同期設定を保存`

Must show:

- Why the permission is needed.
- What data is read or written.
- Failure state for denied, expired, or insufficient permissions.
- Reconnect path.

### Invite Team

Flow:

`Invite people -> Assign roles -> Confirm access -> Track pending invites`

Typical triggers:

- `メールアドレスを追加`
- `ロールを選択`
- `「招待を送信」をクリック`
- `招待失敗`
- `招待送信完了`

Must show:

- Role differences.
- Pending, accepted, expired, and failed invite states.
- Skip path when invites are optional.

### First Useful Empty State

Flow:

`Empty product -> Explain value -> One recommended setup action -> Example preview -> Activated state`

Typical triggers:

- `推奨アクションをクリック`
- `サンプルを表示`
- `初回データ生成完了`
- `任意ステップをスキップ`

Must show:

- The object that will appear once setup is complete.
- One primary action, not many choices.
- Example data only if clearly marked.
- A way to learn or skip without blocking.

### Guided Activation Checklist

Flow:

`Checklist -> Step detail -> Completion feedback -> Next best action`

Typical triggers:

- `チェック項目を選択`
- `設定を保存`
- `完了条件を満たす`
- `ブロック状態を解消`

Must show:

- 3-5 steps max.
- Required vs optional.
- Progress and blocked state.
- The final screen unlocked by completing the checklist.

## States To Include

- Not started.
- In progress.
- Validating.
- Error with fix.
- Permission denied.
- Partial success.
- Done.
- Skipped optional step.
- Resume later.

## Wireframe Requirements

For setup flows, draw at least three screens:

1. Setup entry or empty state.
2. Most important configuration or connection step.
3. First useful post-setup screen.

Add the failure or validation state if it changes user trust or the next action.
Add trigger labels to all arrows between screens.
