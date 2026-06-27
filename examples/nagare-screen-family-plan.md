# Nagare Screen Family Plan

## Product Thesis

Nagare is an inspectable AI workflow engine. It lets users request work from AI agents, read the answer, and verify each agent step through structured evidence.

## Selected Direction: Frost

```yaml
name: Frost
visual_thesis: "白基調、細い罫線、静かな高信頼感。AIの作業結果と証跡を読みやすくする。"
density: moderate
navigation: left_pane_tabs
surface_model: flat_bordered
status_color: restrained
primary_rule: "回答を先に、証跡を次に、ログは最後に。"
heavy_edit_rule: "長文・表・プロンプト・ルーブリックは広い編集面を使う。"
```

## Core Objects

```yaml
objects:
  Work: "ユーザーの依頼"
  Run: "ワークの実行単位"
  AgentStep: "各エージェントが行った工程"
  Input: "ステップに渡された情報"
  Output: "ステップが生成した結果"
  Review: "レビューエージェントの評価行為"
  Evaluation: "評価基準ごとの結果"
  OrganizerDecision: "次に何をするかの判断"
  Domain: "知識と生成物定義のまとまり"
  KnowledgeFile: "ドメインに追加されたナレッジ"
  ArtifactSpec: "生成物の定義"
  Rubric: "生成物の評価基準"
  Prompt: "生成時の指示"
```

## Screens

| Screen | Pattern | Primary job | Opens |
|---|---|---|---|
| Work Home | Work Intake + History Stack | 新規依頼と回答履歴確認 | Work Detail |
| Work Detail | Agent Execution Trace | 最終回答と各工程の検証 | Artifact Preview / Raw Logs |
| Domain Knowledge Settings | Domain Knowledge Workspace | ドメイン、ファイル、生成物定義の管理 | Artifact Editor Dialog |
| Artifact Editor Dialog | Wide Artifact Editor | ルーブリックとプロンプト編集 | Save/Cancel/Delete |

## Shared State Language

```yaml
work_status: [queued, running, reviewing, completed, failed]
verification_status: [passed, needs_revision, failed]
config_status: [draft, dirty, saved, invalid]
```

## Screen Relationship Map

```text
Work Home
  -> click work history row
  -> Work Detail

Work Detail
  -> open artifact
  -> Artifact Preview

Domain Knowledge Settings
  -> select domain
  -> update file/artifact summary

Domain Knowledge Settings
  -> edit artifact spec
  -> Artifact Editor Dialog

Artifact Editor Dialog
  -> save
  -> Domain Knowledge Settings with saved state
```

## Continuity Checks

- Work Home and Work Detail use the same Work/Run status language.
- Work Detail uses the same role labels as any agent configuration screen.
- Domain Knowledge Settings uses the same ArtifactSpec/Rubric/Prompt names as Work Detail evidence.
- Prompt/rubric editing always uses wide editor treatment.
- Raw logs are never the primary representation when structured evidence is available.
