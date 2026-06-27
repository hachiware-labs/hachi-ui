# Nagare UI Element Plan Example

This example shows semantic UI planning for Nagare, an AI workflow engine where users request work, inspect answers, and verify what each agent did.

## Product Thesis

Nagare is not just a workflow runner. It is an inspectable AI work engine: the user can request work, see the answer, and verify whether each agent step acted correctly through inputs, outputs, reviews, and organizer decisions.

## Selected Direction

```yaml
name: Frost
visual_thesis: "白基調、細いグレーライン、余白のある高信頼UI。回答と証跡を静かに読ませる。"
density: moderate
navigation_model: left_pane_tabs
rules:
  - final answer appears before raw logs
  - evidence is structured as timeline steps
  - heavy prompt/rubric editing opens wide editor
```

## Screen 1: Work Home

```yaml
screen: Work Home
viewport: desktop
user_job: "AIに新しいワークを依頼し、過去を含むワーク履歴と回答をすぐ確認する。"
pattern: Work Intake + History Stack
core_objects: [Work, Answer, WorkStatus]
user_decision_points:
  - "何を依頼するか？"
  - "過去の依頼に対する回答は何か？"
  - "どのワークを詳細確認するか？"
information_units:
  - id: new_work_request
    shape: structured_text
    element: prompt_composer
    area_need: large
    reason: "依頼文が作業の入口。"
  - id: work_history
    shape: tabular_records
    element: vertical_history_list
    area_need: large
    reason: "実行中・完了・失敗・過去をまとめて確認する。"
  - id: answer_preview
    shape: long_text_summary
    element: answer_preview_row
    area_need: medium
    reason: "詳細を開かずに依頼への答えを確認する。"
states: [empty, running, completed, failed, retrying]
gaze_route: [new_work_request, submit_action, latest_work_answer_preview, status, open_detail]
rejected:
  - pattern: three_column_dashboard
    reason: "新規依頼と履歴が分断され、回答確認が遅れる。"
  - element: agent_count_control
    reason: "現在のユーザー判断に不要。"
```

## Screen 2: Work Detail

```yaml
screen: Work Detail
viewport: desktop
user_job: "最終回答を確認し、各エージェントの入出力・評価・判断が正しいか検証する。"
pattern: Agent Execution Trace
core_objects: [Work, Run, AgentStep, Input, Output, Review, Evaluation, OrganizerDecision]
user_decision_points:
  - "依頼への最終回答は何か？"
  - "どのステップで何が行われたか？"
  - "レビューは何を評価したか？"
  - "オーガナイザはなぜ次の指示を出したか？"
information_units:
  - id: final_answer
    shape: long_text_summary
    element: summary_card
    area_need: medium
  - id: agent_timeline
    shape: ordered_steps
    element: vertical_timeline
    area_need: large
  - id: step_input_output
    shape: paired_evidence
    element: expandable_input_output_pair
    area_need: large
  - id: review_scores
    shape: rubric_scores
    element: evaluation_score_panel
    area_need: medium
  - id: organizer_decision
    shape: structured_text
    element: decision_note
    area_need: medium
  - id: raw_logs
    shape: audit_log
    element: collapsed_log_viewer
    area_need: compact
gaze_route: [final_answer, overall_verification_status, current_or_failed_step, input_output_pair, reviewer_evaluation, organizer_decision, raw_logs_if_needed]
states: [running, reviewing, needs_revision, verified, failed]
rejected:
  - pattern: raw_log_viewer
    reason: "検証に必要なのはログそのものではなく、入出力・評価・判断の構造。"
```

## Screen 3: Domain Knowledge Settings

```yaml
screen: Domain Knowledge Settings
viewport: desktop
user_job: "複数ドメインごとにナレッジファイル、生成物、ルーブリック、生成プロンプトを管理する。"
pattern: Domain Knowledge Workspace
core_objects: [Domain, KnowledgeFile, ArtifactSpec, Rubric, Prompt]
information_units:
  - id: domain_list
    shape: tabular_records
    element: vertical_domain_list
    area_need: medium
  - id: knowledge_files
    shape: file_collection
    element: file_table_with_upload
    area_need: large
  - id: artifact_specs
    shape: tabular_records
    element: artifact_summary_list
    area_need: large
  - id: rubric
    shape: rubric_scores
    element: wide_rubric_table_editor
    area_need: very_large
  - id: generation_prompt
    shape: structured_text
    element: wide_prompt_editor
    area_need: very_large
layout:
  base: [domain_list_and_domain_detail_left_column, artifact_summary_right_area]
  heavy_edit: [wide_artifact_editor_dialog]
rejected:
  - pattern: four_pane_equal_columns
    reason: "プロンプトとルーブリック編集に必要な面積が足りない。"
```

## Screen 4: Artifact Editor Dialog

```yaml
screen: Artifact Editor Dialog
viewport: desktop_modal
user_job: "生成物のルーブリックと生成プロンプトを広い領域で編集し、保存・キャンセル・削除する。"
pattern: Wide Artifact Editor
information_units:
  - id: artifact_name
    shape: short_text
    element: single_line_input
    area_need: compact
  - id: rubric
    shape: rubric_scores
    element: editable_rubric_table
    area_need: large
  - id: generation_prompt
    shape: structured_text
    element: large_markdown_prompt_editor
    area_need: large
  - id: validation
    shape: error_recovery
    element: validation_banner
    area_need: medium
states: [dirty, saved, invalid, deleting, locked]
```
