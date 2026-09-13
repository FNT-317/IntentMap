# Context efficiency and task sizing

Shorter is not automatically better. IntentMap should remove history that cannot affect the current task while preserving every relevant constraint, dependency, protected behavior, completion condition, and validation requirement.

The counts below are **topic-group comparisons**, not measured tokens and not live-model benchmark results. A topic group is one distinct project fact or discussion thread.

## Current-task context comparisons

| Case | Full project conversation | Focused current-task packet | Removed | Must remain |
| --- | ---: | ---: | ---: | --- |
| Messy marketplace background; current task is listing search | 14 topic groups | 6 topic groups | 8/14 (57%) | target user, search outcome, current data shape, filters in scope, untouched checkout, done checks |
| Private journal; current task is local entry creation | 10 | 5 | 5/10 (50%) | local-only storage, no analytics, entry fields, existing style, validation |
| Existing app; current task is notification preferences | 12 | 7 | 5/12 (42%) | checkout and auth must remain unchanged, preferences behavior, conventions, pre-existing uncommitted work, tests |
| Project with many later ideas; current task is first empty state | 9 | 5 | 4/9 (44%) | empty-state user outcome, confirmed copy boundary, relevant component, accessibility, visual check |

Typical removed topics include rejected names, old alternatives, future monetization, unrelated later stages, biographies that do not alter behavior, and explanations already represented by a confirmed constraint.

A packet fails for **too much context** when it repeats this material and makes the active outcome or boundaries harder to find. It fails for **too little context** when compression drops a relevant privacy rule, protected behavior, dependency, ownership warning, done condition, or validation step. The target is minimum useful context, not minimum text.

## Task-size examples

### Too large

- “Build the marketplace” combines identity, listings, search, booking, payment, messaging, moderation, and deployment. Each area has independent user outcomes and failure modes.
- “Add authentication” is too large when it silently includes registration, recovery, social login, permissions, session management, migration, and audit logging.
- “Finish the v1 backlog” crosses stages and cannot be reviewed against one coherent completion condition.

Split at user-visible or risk boundaries, then expand only the next relevant stage. A good split should still deliver an observable outcome rather than merely create scaffolding.

### Too small

- Rename one local variable with no independent user, safety, or verification value.
- Create a button component, then style it, then connect its click handler as three separate tasks when together they form one tiny behavior.
- Add a test fixture as a standalone task when it only exists to validate the immediately following change.

Combine tightly coupled actions when they share one outcome, boundary, and validation path.

### Appropriate

- “In the existing listings page, let users filter by one confirmed category using the current query-state pattern; preserve sorting and pagination; add focused tests and verify the filter in the UI.”
- “Store new journal entries locally with the three confirmed fields; do not add accounts, sync, or analytics; verify reload persistence and the empty-field behavior.”
- “Add the existing-design-system empty state to the saved-items view; do not change fetching or navigation; verify keyboard focus and the empty/non-empty states.”

Each example has one coherent outcome, clear boundaries, relevant context, observable completion, and a proportionate validation path.

## Sizing decision test

Before confirming a task, check:

1. Can its outcome be explained in one short paragraph?
2. Can it be completed and reviewed without also finishing another independent outcome?
3. Would splitting it further create fragments with no independently useful result?
4. Are its protected behaviors and validation steps understandable now?

If 1 or 2 is no, split it. If 3 is yes, combine it. If 4 is no, resolve the material uncertainty before generating the execution instruction.
