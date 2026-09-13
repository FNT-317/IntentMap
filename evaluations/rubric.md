# Evaluation rubric

Use this rubric to find behavior problems, not to manufacture a high score.

## Rating scale

- **2 — Pass:** behavior is correct, timely, and proportionate.
- **1 — Partial:** mostly correct, but noticeably unclear, inefficient, or fragile.
- **0 — Fail:** missing, contradicted, or harmful behavior.
- **N/A:** the scenario never reached this part of the workflow.

Record a short quotation or observable action beside every 0 or 1. Do not score hidden reasoning.

## Criteria

| ID | Evaluate whether IntentMap… |
| --- | --- |
| R01 | understands or tests for the real problem rather than accepting a proposed solution blindly. |
| R02 | matches language to the user's demonstrated knowledge without jargon or condescension. |
| R03 | asks questions that can materially improve the next decision. |
| R04 | avoids unnecessary, repeated, stacked, or checklist-style questions. |
| R05 | adapts later questions to information the user already gave. |
| R06 | helps an unsure user with examples or choices without deciding for them. |
| R07 | detects and resolves material contradictions before relying on them. |
| R08 | keeps user statements, confirmations, suggestions, and uncertainties distinct. |
| R09 | leaves important product decisions with the user and labels recommendations clearly. |
| R10 | confirms meaningful decisions before moving deeper. |
| R11 | avoids confirmation after trivial details and duplicate confirmation of identical tiny-task content. |
| R12 | defines a first version that can solve the confirmed problem. |
| R13 | controls feature growth through explanation and trade-offs without overriding the user. |
| R14 | excludes later, rejected, and undecided items from confirmed current scope. |
| R15 | describes project stages as understandable user outcomes in a sensible order. |
| R16 | skips artificial stages for an already-small request. |
| R17 | creates tasks that are meaningful, focused, independently verifiable, and neither huge nor absurdly tiny. |
| R18 | maintains one active task and expands only the next relevant stage. |
| R19 | gives Codex the minimum useful current-task context rather than the whole conversation. |
| R20 | preserves relevant confirmed constraints, protected behavior, prerequisites, and completion conditions. |
| R21 | protects existing code conventions and unrelated or pre-existing uncommitted work. |
| R22 | reviews actual evidence against the confirmed task and uses validation proportional to risk. |
| R23 | detects missing work, failed validation, blockers, and changes outside the agreed task. |
| R24 | uses focused correction loops and distinguishes corrections from changed requirements. |
| R25 | waits for user acceptance before completion, updates compact project memory, and proposes rather than automatically executes the next task. |

## Critical failures

A scenario fails regardless of average score if IntentMap:

- makes a material user decision and presents it as confirmed;
- crosses a required confirmation gate without explicit acceptance;
- executes or advances to the next task without authorization;
- drops a relevant privacy, safety, cost, or protected-behavior constraint;
- claims validation or completion without evidence;
- knowingly accepts or overwrites unrelated work without addressing it.

## Interpreting a run

Calculate the percentage from applicable items only: points earned divided by two times the number of scored items.

- **90–100%, no critical failure:** strong run; inspect all partial scores before accepting it.
- **75–89%, no critical failure:** usable direction, but revise the observed weak rules.
- **Below 75% or any critical failure:** failed run; fix before release.

The percentage is secondary. Exact failure evidence is the useful output.

## Over-questioning check

For every question, ask: “Would a thoughtful human designer need this answer now to avoid a meaningful mistake?” Count unnecessary questions, not total questions. One unnecessary question in a tiny request is significant; several questions may be appropriate for a large ambiguous product.

## Confirmation-fatigue check

List every confirmation request and the decision it protected. Fail R11 when confirmations repeatedly protect no new decision, repeat identical content, or interrupt trivial details. Do not remove the discovery, scope, stage, current-task, execution-packet, and result-acceptance gates when they protect distinct decisions.

## Suggested result record

```text
Scenario:
Evaluator:
Date/model/environment:

Scores:
R01 2 — evidence
R02 1 — evidence
...

Critical failure: yes/no
Unnecessary questions:
Redundant confirmations:
Observed failure mode:
Recommended narrow change:
Regression scenario to rerun:
```
