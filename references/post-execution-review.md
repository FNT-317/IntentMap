# Post-execution review and progression

## Purpose and boundary

After Codex executes one confirmed task, determine what actually changed, whether it matches the confirmed Current Task Packet, and whether the user accepts the result. A finished run is evidence that execution stopped, not proof that the task succeeded.

This module reviews and updates the plan. It does not package or publish the Skill, start external services, add monetization, or automatically execute the next software task.

Use this loop:

```text
execute one confirmed task
  -> inspect the actual result
  -> compare it with the confirmed task
  -> classify and explain the result
  -> correct the same task if necessary
  -> review again
  -> user accepts the result
  -> mark the task complete
  -> update the project map
  -> propose the next task
  -> return to Modules 3 and 4 confirmation gates
```

## Review the result, not the old conversation

Use the confirmed Current Task Packet and execution instruction from Module 4 as the source of truth. Check:

1. Was the agreed goal achieved?
2. Was every required part included?
3. Were the “do not change” boundaries respected?
4. Are all observable completion conditions satisfied?
5. Was the requested validation performed, and what did it show?

Do not judge the work against rejected ideas, unconfirmed discussion, later features, or expectations invented after execution.

## Inspect proportionally

Inspect the smallest evidence set that can support a reliable conclusion. For an existing codebase, normally start with:

- the files changed by this execution;
- the relevant diff;
- directly related code when needed to understand the effect;
- relevant test results;
- the affected user flow or rendered result.

Do not automatically reread the entire repository. Expand the review only when the change is broad, risky, unclear, or affects shared behavior.

Distinguish this execution's work from changes that already existed. Preserve pre-existing user modifications and do not attribute, revert, or correct them without evidence that they belong to the reviewed task.

Scale validation to risk:

- **Tiny visual change:** inspect the affected element and verify nearby behavior remains intact.
- **Form or ordinary feature:** exercise the main flow, check required inputs and outcomes, and run relevant existing tests.
- **Authentication, permissions, personal data, payments, destructive operations, or shared infrastructure:** inspect the relevant design and diff more deeply, test success and important failure paths, and run the meaningful affected test set.

Do not skip important checks merely to save tokens or time. Do not run expensive unrelated checks by default.

## Detect work outside the confirmed task

Compare every meaningful changed area with the packet's goal, requirements, and protected boundaries. Treat a change as potentially out of scope when it:

- affects a file or behavior with no clear need for the task;
- refactors, renames, redesigns, or replaces a dependency without a task-related reason;
- implements a future or rejected feature;
- changes protected behavior;
- introduces a new product decision the user did not confirm.

Explain the evidence and practical effect in ordinary language. For example:

> “The button color changed as requested, but the login logic was also modified. That was outside the agreed task.”

Do not silently accept the extra work because the main feature appears to work. When practical, recommend a focused correction that restores only the unrelated change. Do not automatically revert work when ownership or intent is uncertain; ask the user when a meaningful choice is involved.

## Result states

Conceptually classify the review outcome as one or more of:

- **Completed:** the goal, boundaries, completion conditions, and relevant validation appear satisfied.
- **Partially completed:** some agreed behavior works, but a required part is missing.
- **Needs correction:** the main goal is not met or an important result is wrong.
- **Out-of-scope change detected:** the requested result may work, but unrelated or protected behavior changed.
- **Blocked:** completion cannot continue without missing information, access, an earlier prerequisite, an external dependency, or a user decision.

Use ordinary language with the user. If more than one state applies, report each problem instead of forcing a misleading single label.

## Explain the result simply

Give a short user-facing summary scaled to the task. A normal structure is:

```text
What now works:
- ...

Checks performed:
- ...

Problems or unexpected changes:
- ...

Still not included:
- ...

Review conclusion:
...
```

Mention technical file names only when they help the user understand, verify, or decide something. Offer technical detail separately when requested.

Never hide a failed check. If code was written but a relevant test fails, say that the task is not ready to mark complete and explain what needs attention.

## Correct the same task without replaying the project

When the result is incomplete or incorrect, first ask internally: “Can this be fixed while keeping the same confirmed task?”

If yes:

1. identify the smallest gap or defect;
2. preserve the parts that already satisfy the task;
3. prepare a focused correction instruction containing only the problem, relevant current behavior, boundaries, and checks;
4. show the correction to the user and obtain any confirmation needed before execution;
5. execute only when separately authorized;
6. review the corrected result again against the original confirmed task.

Do not regenerate the entire original project prompt. Repeat the review-and-correction loop until the task is ready for user acceptance or genuinely blocked.

Example:

```text
Original task: Create the basic product form.
Observed gap: The price input is missing.
Focused correction: Add the missing price input while keeping the existing name and description fields and all unrelated pages unchanged. Recheck all three fields.
```

## Distinguish correction from a changed requirement

After seeing the result, the user may want something different. Decide which case applies:

- **Correction:** the result does not match what was already confirmed, such as a button remaining blue when green was required.
- **Changed or new requirement:** the user now wants different behavior, such as adding a second button when one was originally confirmed.

A changed requirement is not automatically an execution failure. Record the new decision openly, explain its effect on later work, and return to the narrowest relevant earlier module:

- Module 1 if the underlying need changed;
- Module 2 if the first-version boundary changed;
- Module 3 if stages or tasks changed;
- Module 4 if only the focused execution packet needs revision.

Reconfirm only the materially affected decisions. Do not silently rewrite the original task or pretend the new requirement was always included.

## Handle blockers honestly

Examples of genuine blockers include missing credentials, unavailable external access, an absent assumed feature, an incomplete prerequisite, or a required user decision.

If the actual result, diff, test output, or other evidence needed for review is unavailable, say that the task cannot yet be verified. Do not reconstruct or assume the result from Codex's completion message alone.

State:

- what was verified;
- exactly what prevents completion;
- what cannot yet be concluded;
- the minimum information or action needed next.

Do not guess around the blocker, mark the task complete, or expand into unrelated work.

## User confirmation before completion

Even when every automated check passes, show the user what was achieved and any important limitation. Then ask:

> “This step appears to be complete. Does the result match what you expected, or is there anything you want adjusted before we move on?”

Stop and wait. The user may accept, request a correction, change a requirement, ask a question, or request technical details. Silence is not acceptance.

Do not ask for approval after every technical check. This is the meaningful checkpoint: whether the completed task is acceptable before progression.

Mark the task complete only after explicit acceptance. Record the accepted result and any execution decision that remains relevant to later work.

## Project memory versus current-task context

Maintain two different compact information sets:

- **Project memory:** confirmed problem and scope, project stages, completed tasks, relevant lasting decisions, later items, unresolved items, and the current position in the project.
- **Current-task context:** only the subset Codex needs for the task currently being executed or corrected.

Removing information from a Current Task Packet does not erase it from project memory. For example, “payment comes later” may be irrelevant to a product-form instruction but must remain in the broader plan if the user confirmed it.

Do not preserve every word of the conversation. Keep confirmed decisions and state in compact form, with enough source or rationale only when it affects later choices.

## Update progress and propose the next task

After the user accepts the result:

1. mark the current task complete;
2. update the current stage and project map;
3. retain relevant confirmed decisions and unresolved items;
4. explain what was completed and where the project now stands;
5. identify the next logical task from the confirmed current-stage list;
6. explain why it comes next;
7. ask the user whether they want to use or change that next task.

A compact progress view may look like:

```text
PROJECT
Local marketplace

COMPLETED
✓ Basic product form

CURRENT STAGE
Let sellers publish a product

NEXT SUGGESTED TASK
Save the submitted product

LATER
Browse products
View product details
Contact the seller
```

Do not automatically execute the next task. The proposal returns to Module 3 for task confirmation, then Module 4 for a focused instruction and its separate confirmation.

## Keep review context efficient

For review, prefer changed files, the relevant diff, focused checks, and only the surrounding code needed to understand them. For correction, prefer a small instruction describing the observed gap over regenerating the original task packet. For progression, carry compact project memory forward instead of replaying the conversation.

Context efficiency must not hide failures or remove a confirmed constraint. The goal is the smallest evidence and context that still support a reliable review and safe next step.

## Keep tiny reviews tiny

For a one-task visual change, the full review may be:

> “The login button is now green, its text and behavior are unchanged, and login still works. Does that look right to you?”

Do not create a project report, state table, or correction plan when none is needed.

## End of Module 5

The module has completed one cycle when the actual result has been sufficiently reviewed, any correction or blocker has been handled honestly, the user has explicitly accepted the result, project memory has been updated, and one next task has been proposed without being executed.

Stop there. Do not begin packaging, publishing, marketplace work, external services, databases, websites, monetization, or another unconfirmed software task.
