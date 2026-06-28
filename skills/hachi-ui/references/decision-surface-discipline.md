# Decision Surface Discipline

Use this reference when a full-scale wireframe must prove density, evidence, state, and operational detail without turning the product screen into a rubric checklist.

## Core Rule

A full-scale screen is not a checklist of all available information. It must answer one dominant user question.

Do not make the SVG prove the rubric by showing every rubric item inside the product UI. Prove secondary rubric items through `UI_PLAN.md`, annotations outside the screen frame, variant frames, state sheets, or collapsed states. The product screen itself must remain plausible for the user's immediate task.

## Source Screen Alignment

When a full-scale screen is created from a flow frame, its primary surface must answer the same user question as the source frame. Do not replace the selected screen's job with a generic app-wide operations board.

Use this alignment test before drawing:

- Source question: what is the exact user question written for the flow frame?
- Source object: what object is the user inspecting, editing, selecting, validating, or committing?
- Source pattern: is the frame a gate, editor, lesson, procedure, review, queue, comparison, timeline, or handoff?
- Primary surface: does the largest visible area directly support that question, object, and pattern?

Examples:

- A mitigation confirmation screen should be a confirmation gate with steps, risk, metrics, rollback, and one proceed/recover action, not a general incident ledger.
- A lesson screen should be a focused problem, answer, hint, and grading surface, not a learning weakness map.
- An onsite work screen should be a guided procedure with safety, current step, measurement, photo, and interruption controls, not a retrospective evidence packet.
- A queue screen may use a ledger, board, or table because simultaneous state comparison is part of the user's current job.

If the source screen is not a queue, ledger, board, or monitoring console, avoid making the largest region a multi-state ledger just to prove state coverage.

## Visibility Tiers

Separate information into three visibility tiers before drawing:

1. Always-visible decision surface
   - current state;
   - primary object;
   - active actor or owner;
   - immediate user action;
   - one concise outcome or progress summary.

2. Selected supporting detail
   - one selected timeline item, artifact, evidence, validation result, queue item, or record;
   - shown only because it supports the current decision.

3. Collapsed or separate diagnostic detail
   - raw logs;
   - full evidence chain;
   - assignment resolution;
   - policy explanation;
   - review criteria details;
   - state variants not currently active.

## State Variant Rule

State variants should not be packed into the primary product screen unless the real product would show them simultaneously, such as a queue, ledger, kanban board, operations board, or monitoring console.

Prefer one of:

- separate variant frames;
- small annotations outside the product UI;
- `UI_PLAN.md` state table;
- side-by-side state sheet.

The main screen should show the current state only, plus one nearby recovery or next-state hint when it affects confidence.

## Area Budget

Allocate visible area by decision priority:

- `50-70%`: primary working/decision surface;
- `15-30%`: selected supporting context;
- `0-20%`: secondary diagnostics;
- `0%` initial visibility for raw logs unless the current state is failure or debug.

If diagnostics exceed the selected supporting detail, collapse them, move them outside the product UI, or create a separate diagnostic screen.

## Overexposure Checks

Penalize overexposed information when:

- more than one dominant user question is visible;
- the largest region answers a different question than the selected source screen;
- rubric evidence is displayed as product UI instead of plan annotation;
- diagnostic details compete with the primary action;
- state variants appear as controls even though they are not available in the current state;
- the screen feels like a system audit sheet rather than a user decision surface.

## Full-Scale Proof Strategy

When a rubric asks for concrete data, evidence chains, scroll capacity, state-specific actions, or stop conditions:

- keep the always-visible product UI focused on the immediate decision;
- show one selected supporting detail if it directly helps that decision;
- put full chains, review criteria, inactive variants, or capacity proofs in collapsed diagnostic sections, side sheets, external annotations, or `UI_PLAN.md`;
- use variant frames only when comparing states is the point of the artifact.

## User-Facing Explainability Gate

Before accepting any full-scale screen, classify every visible label, ID, status, button, and data item into one of these categories:

1. User-facing decision information.
2. User-facing context.
3. Supporting evidence.
4. Diagnostic detail.
5. Internal implementation detail.

The primary screen may show only categories 1-3 by default. Hide or collapse internal implementation details unless the current user is explicitly debugging internals and the detail changes the next action.

Details that should usually be hidden or translated:

- internal IDs such as `run_0014`, `evt_0001`, `dsp_0007`, or code-like row IDs;
- runtime names such as `Codex CLI`;
- implementation terms such as `ledger`, `evidence`, `criteria`, `input-output chain`, and `state variants`;
- pending or workflow labels that require product-model knowledge before the user can act.

Translate internal terms into user work language:

- `ledger` -> `履歴`;
- `evidence` -> `根拠`;
- `criteria` -> `確認条件`;
- `diff draft` -> `変更案`;
- `runtime` -> `実行環境`, only when needed;
- `agent` -> `担当AI` or `作業担当`.

## Detail Screen Rule

A detail screen is not a place to show all details.

A detail screen should show the minimum information needed to decide the next action for one selected object. Additional system facts belong in collapsed metadata, diagnostics, side sheets, or developer/debug views.

Default detail screen hierarchy:

1. Human-readable state sentence.
2. Current object and current owner or actor in user language.
3. Immediate action or no-action-needed state.
4. One reason or proof that supports the action.
5. Optional `詳細を開く` entry point.

Avoid making IDs, logs, runtime names, assignment records, or provenance chains visible by default unless the screen's dominant job is diagnostic review.

## Plain-Language Review

After rendering the SVG, inspect the screen and answer:

- Which visible words require prior knowledge of the product internals?
- Which visible facts do not change the user's next action?
- Which labels can be translated into normal work language?
- Which details should move behind `詳細を開く`?
- Would this still make sense if internal IDs were removed?

If the answer reveals unexplained internal terminology in the main surface, redraw before claiming 90+.
