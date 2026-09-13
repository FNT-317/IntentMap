# Module 6 stress-test report

## Method and claim boundary

This report is a **manual static rule walkthrough** of the v0.1 release candidate. Each scenario was traced to the relevant instructions, and gaps found during that trace were corrected. No claim is made that 32 live model conversations, multiple models, or automated behavioral evaluations passed. Those runs remain local release-candidate testing work.

“Covered” below means the production instructions contain an explicit response rule. “Gap found → fixed” means the walkthrough exposed a missing or underspecified rule and the named reference was changed.

## Scenario trace

| Scenario | Static status | Primary rule evidence |
| --- | --- | --- |
| S01 | Covered | `requirement-discovery.md`, `dynamic-questioning.md` |
| S02 | Covered | `requirement-discovery.md`, `scope-definition.md` |
| S03 | Covered | `requirement-discovery.md` |
| S04 | Gap found → fixed | `dynamic-questioning.md`: repeated “I don't know” now stops after useful choices and can remain uncertain unless blocking |
| S05 | Covered | `product-principles.md`, `confirmation-checkpoints.md` |
| S06 | Covered | `dynamic-questioning.md`, `confirmation-checkpoints.md` |
| S07 | Covered | `requirement-discovery.md`, `post-execution-review.md` project memory rules |
| S08 | Covered | `dynamic-questioning.md`: skip questions already answered |
| S09 | Gap found → fixed | `dynamic-questioning.md`: match the user's demonstrated level |
| S10 | Covered | `product-principles.md`, `dynamic-questioning.md` |
| S11 | Covered | `task-decomposition.md`, `final-codex-task-generation.md` tiny-task rules |
| S12 | Covered | `scope-definition.md`, `task-decomposition.md` |
| S13 | Covered | `task-decomposition.md`, `final-codex-task-generation.md` |
| S14 | Gap found → fixed | `final-codex-task-generation.md`: identify and preserve pre-existing uncommitted work |
| S15 | Covered | `scope-definition.md`: explain trade-offs without deciding for the user |
| S16 | Covered | `scope-definition.md`: user decisions override unaccepted recommendations |
| S17 | Gap found → fixed | `confirmation-checkpoints.md`: “just do it” is not approval of unseen content |
| S18 | Covered | `final-codex-task-generation.md`: minimum useful current-task context |
| S19 | Covered | `dynamic-questioning.md`: one high-value question, scaled to the request |
| S20 | Gap found → fixed | `confirmation-checkpoints.md`: reopen only confirmations affected by a late material fact |
| S21 | Covered | `task-decomposition.md`, `post-execution-review.md`: return to the narrowest affected module |
| S22 | Covered | `post-execution-review.md`: distinguish changed requirements from execution defects and return to the narrowest affected module |
| S23 | Covered | `post-execution-review.md`: focused correction loop |
| S24 | Covered | `post-execution-review.md`: report out-of-scope changes |
| S25 | Covered | `post-execution-review.md`: failed relevant validation keeps the task incomplete |
| S26 | Covered | `post-execution-review.md`: state blockers without guessing |
| S27 | Covered | `final-codex-task-generation.md`: return to Module 3 if the task grows materially |
| S28 | Covered | `post-execution-review.md`: recommend, then let the user choose |
| S29 | Covered | `final-codex-task-generation.md`, `post-execution-review.md`: separate project memory from current context |
| S30 | Covered | `final-codex-task-generation.md`: preserve relevant early constraints |
| S31 | Gap found → fixed | `task-decomposition.md` and `final-codex-task-generation.md`: one confirmation may cover identical adjacent tiny-task content |
| S32 | Gap found → fixed | `post-execution-review.md`: unavailable actual evidence blocks verification |

## Over-questioning

The highest-risk cases are S04, S08, S11, and S19: repeated uncertainty, already-complete requirements, a trivial change, and sparse information under time pressure. The rules now require one high-value question at a time, forbid asking for information already supplied, allow unresolved non-blocking uncertainty, and scale discovery to task size. This is adequate in the static trace; live conversations are still needed to measure how consistently a model judges a question to be valuable.

Use R03–R06 and the rubric's question-by-question necessity check. Total question count alone is not a meaningful target: a vague high-risk product can justify several adaptive questions, while one unnecessary question can be excessive for S11.

## Confirmation fatigue

The walkthrough found one structural duplication risk: for a tiny fully specified change, Module 3's next-task confirmation and Module 4's execution-preview confirmation could show identical content consecutively. The rules now allow one explicit confirmation to cover both only when action, boundary, completion condition, and validation are identical. If Module 4 introduces any material implementation constraint or choice, it still requires a fresh preview and acceptance.

Meaningful gates remain for shared understanding, first-version scope, stage map, active task, materially new execution packet, and post-execution result. “Just do it,” silence, or general planning approval does not approve content the user has not seen.

## Task-size findings

S12, S15, and S27 expose oversized work; S11 and S31 expose artificial fragmentation. Existing decomposition rules already require one coherent, independently verifiable outcome and a return to planning if the task grows. The separate [context and task-sizing guide](context-and-task-sizing.md) now supplies concrete too-large, too-small, and appropriate examples. Live tests should score R16–R18 rather than assume the examples guarantee correct judgment.

## Context-efficiency findings

Four representative comparisons reduced current packets by 42–57% of **topic groups** while retaining current constraints and validation needs. For example, the messy marketplace case retains 6 of 14 groups and removes 8 unrelated groups (57%). These are editorial comparisons, not token measurements or model-performance results.

Compression is a failure if it drops privacy, protected behavior, dependencies, ownership of uncommitted work, completion conditions, or validation. The intended optimization is relevance, not shortest prompt length.

## Failure modes found and rule changes

The static walkthrough directly caused seven narrow changes:

1. stop rephrasing the same question after repeated “I don't know” answers;
2. match an experienced or nontechnical user's demonstrated language level;
3. distinguish and protect pre-existing uncommitted work;
4. reject “just do it” as approval of unseen content while shortening the process;
5. reopen only decisions affected by a late material constraint;
6. combine identical adjacent tiny-task confirmations;
7. block completion claims when actual execution evidence is unavailable.

The complete anticipated catalogue is in [failure modes](failure-modes.md). It is a prevention and diagnosis list, not evidence that each behavior has been observed in a live run.

## Remaining weaknesses

- No recorded live, adversarial, or multi-model conversational suite has run yet.
- Project memory is maintained through instructions; there is no persistence implementation or schema enforcement.
- Review quality depends on access to diffs, files, screenshots, commands, and test evidence.
- The boundary between meaningful and trivial confirmation still requires judgment.
- Task sizing and context relevance still require judgment and may vary by repository risk.
- The structural checker validates organization and traceability, not behavior.
- Packaging, installation, publishing, marketplace behavior, and production reliability are outside this module.

## Release recommendation

The project is ready to be labeled **IntentMap v0.1 release candidate for local testing**. Its structure is coherent, the full workflow is represented, evaluation artifacts are separated from production instructions, and the static scenario trace has no known unaddressed rule gap. It should not yet be described as published, production-proven, or behaviorally validated until live runs are recorded and scored with the rubric.
