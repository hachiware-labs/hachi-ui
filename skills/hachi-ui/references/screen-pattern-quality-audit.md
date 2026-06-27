# Screen Pattern Quality Audit

Use this audit to keep the screen pattern catalog honest. It scores whether each pattern is specific enough to guide an agent before drawing SVG.

## Scoring

- `90-100`: strong pattern. It has a clear user job, object model, information shape, required states, and anti-patterns.
- `85-89`: production-usable. It may still need domain-specific judgment.
- `80-84`: usable but watch closely. It can drift generic if the brief is vague.
- `<80`: replace or repair. Do not keep as a primary pattern without a sharper object, decision, or evidence model.

## Audit Results

| # | Pattern | Score | Verdict | Notes / Action |
|---:|---|---:|---|---|
| 1 | Work Intake + History Stack | 88 | Pass | Strong for AI/request workflows; answer preview requirement prevents log-first UI. |
| 2 | Agent Execution Trace | 92 | Pass | One of the strongest patterns; explicit trust model and step evidence. |
| 3 | Evidence Drilldown | 87 | Pass | Good provenance pattern; pair with Evidence Strip/Detail unit patterns. |
| 4 | Tool Permission Review | 85 | Pass | Strong when scope, risk, expiration, and audit are visible. |
| 5 | Prompt And Rubric Studio | 90 | Pass | Strong because prompt, rubric, variables, examples, and validation are first-class. |
| 6 | Evaluation Lab | 88 | Pass | Good for AI quality work; failure clustering keeps it from being a table only. |
| 7 | Human Handoff Console | 84 | Watch | Useful but can become a support ticket screen; keep evidence and SLA visible. |
| 8 | Automation Rule Builder | 86 | Pass | Clear trigger-condition-action model and simulation requirement. |
| 9 | Domain Knowledge Workspace | 84 | Watch | Good for hachi-ui's AI context; avoid starving prompt/rubric editing. |
| 10 | Source Governance Library | 86 | Pass | Replaced weaker Knowledge Library; adds owner, freshness, downstream impact. |
| 11 | Settings Dependency Map | 86 | Pass | Replaced weaker Settings Matrix; adds dependency and impact preview. |
| 12 | Permission / Role Matrix | 88 | Pass | Clear comparison model with inheritance and overrides. |
| 13 | Feature Flag Console | 84 | Watch | Usable; always require environment, segment, rollout, and conflict states. |
| 14 | Integration Health Console | 85 | Pass | Good operational pattern when auth, freshness, and retry are visible. |
| 15 | Data Import + Field Mapping | 90 | Pass | Strong because it maps source, target, validation, dry run, and commit. |
| 16 | Form Builder / Schema Designer | 83 | Watch | Common and useful; strengthen with preview and selected-field inspector. |
| 17 | Wide Artifact Editor / Full Editor Surface | 88 | Pass | Corrects the narrow-rail editing failure mode. |
| 18 | Review / Approval Queue | 84 | Watch | Solid but broad; pair with Decision Queue Item and Evidence Strip. |
| 19 | Comparison / Diff Review | 89 | Pass | Strong for version/change decisions; requires conflict/no-change states. |
| 20 | Document Draft + Review | 85 | Pass | Clear combination of body, comments, evidence, and export/share. |
| 21 | Annotation / Labeling Review | 83 | Watch | Useful for data work; needs progress and conflict state to avoid being generic. |
| 22 | Version History / Rollback | 84 | Watch | Usable; restore confirmation and audit metadata are essential. |
| 23 | Search Investigation Surface | 86 | Pass | Replaced weaker Search Results + Preview; adds relevance, refinement, evidence. |
| 24 | Template Decision Gallery | 83 | Watch | Replaced weak gallery picker; still watch for decorative card grids. |
| 25 | Exception Command Center | 86 | Pass | Replaced generic Command Center; centered on exceptions and actionability. |
| 26 | Object Profile / 360 Detail | 82 | Watch | Common and needed; must anchor one object and avoid unrelated panels. |
| 27 | List + Bulk Action Review | 84 | Watch | Good admin pattern; preview/undo/partial failure keep it safe. |
| 28 | Pipeline / Kanban Board | 81 | Watch | Useful but familiar; use only when stage movement is the job. |
| 29 | SLA Triage Queue | 87 | Pass | Strong time-to-action pattern. |
| 30 | Incident War Room | 86 | Pass | Good live-ops pattern with severity, roles, action checklist, comms. |
| 31 | Schedule / Resource Planner | 84 | Watch | Good when conflicts and capacity are explicit. |
| 32 | Appointment Readiness Board | 83 | Watch | Replaced weak Calendar Operations Board; now tied to prep and follow-up. |
| 33 | Plan Usage Entitlement Console | 85 | Pass | Replaced generic billing screen; connects limits to product impact. |
| 34 | Report Builder | 83 | Watch | Useful but broad; require outline, chart config, filters, export state. |
| 35 | Metric Explorer | 86 | Pass | Good analytic pattern when anomalies and selected points are represented. |
| 36 | Segment / Cohort Builder | 84 | Watch | Good rule-preview pattern; zero-member and loading states matter. |
| 37 | Alert Triage Center | 86 | Pass | Strong when grouping and suppression prevent alert fatigue. |
| 38 | Canvas + Inspector | 84 | Watch | Useful; must show selected object, toolbar, minimap/legend, and invalid edges. |
| 39 | Edit Preview Workbench | 86 | Pass | Replaced weak Split Preview; requires linked editing, preview, and stale state. |
| 40 | Guided Setup / Migration Flow | 85 | Pass | Replaced generic Wizard / Stepper; staged validation and consequence preview. |
| 41 | Mobile Field Task Flow | 84 | Watch | Replaced generic Mobile Task Stack; now tied to mobile field action and sync. |
| 42 | Access Gate / Recovery | 84 | Watch | Added common missing pattern for auth, invite, role, and session failures. |
| 43 | First-Run Activation Checklist | 86 | Pass | Added missing empty/onboarding activation pattern. |
| 44 | Object Creation Studio | 85 | Pass | Added missing create/configure/validate pattern. |
| 45 | Notification / Activity Inbox | 83 | Watch | Added common collaboration pattern; must group by action required. |
| 46 | Help / Support Resolution Center | 82 | Watch | Added recovery pattern; avoid static FAQ layout. |
| 47 | Data Quality Resolution Queue | 87 | Pass | Added common governance/cleanup pattern. |
| 48 | Communication Thread Console | 82 | Watch | Added conversation-work pattern; avoid chat-first misuse. |
| 49 | Relationship / Dependency Map | 86 | Pass | Added dependency/lineage pattern; relationships must be selectable and consequential. |

## Replaced Patterns

- `Knowledge Library` -> `Source Governance Library`: the old name was too file-browser-like and did not require trust, freshness, owner, or downstream impact.
- `Settings Matrix` -> `Settings Dependency Map`: the old name encouraged generic settings pages; the replacement requires dependency and impact modeling.
- `Search Results + Preview` -> `Search Investigation Surface`: the old name was too standard; the replacement requires relevance, evidence, and refinement state.
- `Template / Gallery Picker` -> `Template Decision Gallery`: the old name encouraged decorative galleries; the replacement requires fit criteria and adaptation effort.
- `Command Center` -> `Exception Command Center`: the old name was too vague; the replacement centers exceptions and recommended action.
- `Calendar Operations Board` -> `Appointment Readiness Board`: the old name was calendar-generic; the replacement focuses preparation and follow-up.
- `Billing / Usage Console` -> `Plan Usage Entitlement Console`: the old name was finance-generic; the replacement ties usage to product entitlement.
- `Split Preview` -> `Edit Preview Workbench`: the old name reinforced arbitrary split layouts; the replacement requires linked editing and preview states.
- `Wizard / Stepper` -> `Guided Setup / Migration Flow`: the old name described chrome, not user work; the replacement requires staged validation and consequence preview.
- `Mobile Task Stack` -> `Mobile Field Task Flow`: the old name was generic; the replacement requires mobile context, sync, recovery, and a focused field action.

## Coverage Gaps Closed

The catalog now covers the common missing product cases that were not well represented by the first 41 patterns:

- authentication, authorization, invite, and recovery states;
- first-run activation and empty product state;
- primary object creation/configuration;
- notification and activity processing;
- help/support diagnosis and escalation;
- data quality cleanup and deduplication;
- communication threads tied to work objects;
- relationship, dependency, and lineage understanding.

## Remaining Caution

Do not try to cover every possible UI noun. The catalog should cover decision shapes, not surface nouns. Add a new pattern only when it introduces a distinct user decision, information shape, area budget, or state model that cannot be handled by existing patterns plus information-unit patterns.
