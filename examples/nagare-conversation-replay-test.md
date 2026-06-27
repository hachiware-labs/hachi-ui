# Nagare Conversation Replay Test

This file captures expected planning behavior for a conversation similar to the Nagare/Moonchild design session. It is not a visual snapshot test. It is a planning and reasoning regression example.

## Initial Brief

```text
白基調のハイセンスなワークフローエンジン。
AIにワークを依頼し、複数のエージェントで処理する。
左ペインにタブ形式で、ワーク画面/設定画面を切り替える。
右エリアに新規ワーク依頼と過去ワークの処理状況一覧を表示する。
設定には知識、ドメイン、成果物、評価基準がある。
```

## Expected Behavior 1: Direction Varianting

```yaml
expected_directions:
  - name: Frost
    density: moderate
    posture: high_trust_minimal
    navigation: left_pane_tabs
  - name: Slate
    density: high
    posture: operational_dense
    navigation: left_sidebar_dense
```

## User Selects Direction 1

```text
Direction 1 側のほうがいいかな。
```

Expected plan patch:

```yaml
selected_direction: Frost
preserve_for_followups: true
```

## User Corrects Work Home Layout

```text
3列構成ではなく、左ペインとメインの2列。メインは新規依頼とワーク一覧を縦積み。
エージェント数設定はいらない。
実行中だけでなく過去も含める。
回答がすぐにわかるようにする。
```

Expected patches:

```yaml
patches:
  - class: screen_pattern
    from: three_column_dashboard
    to: Work Intake + History Stack
  - class: speculative_control
    remove: agent_count_control
  - class: object_model
    from: running_work_only
    to: all_work_history
  - class: information_hierarchy
    move: answer_preview
    to: history_row
```

## User Clarifies Product Core

```text
このアプリの特徴は、ワークを実施するエージェントの記録をしっかりとって、各ステップの動きが正しいかを検証できるようにすることです。
```

Expected product thesis update:

```yaml
product_thesis: "AIエージェントの仕事を依頼し、各ステップの入出力・評価・判断を検証できる。"
required_evidence_units:
  - step_input
  - step_output
  - reviewer_evaluation
  - organizer_decision
  - next_instruction
screen_pattern: Agent Execution Trace
```

## User Defines Domain Knowledge

```text
複数のドメインがある。ドメインにはナレッジファイルを追加できる。生成物の指定もできる。生成物にはルーブリックと生成時のプロンプトが指定できる。
```

Expected screen pattern:

```yaml
screen: Domain Knowledge Settings
pattern: Domain Knowledge Workspace
objects: [Domain, KnowledgeFile, ArtifactSpec, Rubric, Prompt]
```

## User Corrects Editor Area

```text
生成物の評価項目やプロンプトの指定は広い領域が必要です。右列が狭すぎます。
```

Expected patches:

```yaml
patches:
  - class: area_budget
    affected: [rubric, generation_prompt]
    from: narrow_right_column
    to: wide_artifact_editor_dialog
  - class: element_choice
    rubric: editable_rubric_table
    prompt: large_markdown_prompt_editor
```

## Acceptance Criteria

A generated plan passes if it:

- proposes named directions for the broad initial brief;
- preserves the selected direction across follow-up screens;
- treats user corrections as planning patches;
- uses Work Intake + History Stack for the home screen;
- uses Agent Execution Trace for the detail screen;
- uses Domain Knowledge Workspace for domain settings;
- uses Wide Artifact Editor for prompt/rubric editing;
- shows answer previews in work history;
- removes unnecessary agent count control;
- models input/output/review/decision evidence for agent steps.
