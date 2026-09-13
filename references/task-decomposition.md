# Task decomposition

## Purpose and boundary

Turn a confirmed first-version scope into an understandable project map, then prepare one small, confirmed next task. This module plans progressively; it does not generate the final Codex execution instruction and does not implement software.

Begin only after the user explicitly confirms the Module 2 scope summary. If the scope has changed or was not confirmed, return to scope definition.

Use this progression without skipping its confirmation gates:

```text
Confirmed first version
  -> propose project stages
  -> explain the stages
  -> user confirms the stage structure
  -> expand only the next relevant stage
  -> explain its small tasks
  -> user confirms those tasks
  -> present one next task
  -> user confirms it
  -> mark it ready for Codex and stop
```

Silence does not confirm any level.

## Keep two planning levels

Maintain two distinct views:

- **Project map:** a short, user-facing overview of the stages and where the project is going. Keep future stages high-level.
- **Current task:** the one task that needs enough detail to be understood, confirmed, and later given to Codex.

The project map provides orientation. The current task provides focus. Do not repeatedly load Codex with detailed plans for work that is not active.

## Decide whether stages are useful

Use stages for a project with several meaningful outcomes, flows, or areas of work. Skip stages when the confirmed request is already one small, independently verifiable change. For a tiny request, define and confirm the single task directly.

Do not invent stages merely to make the plan look complete.

When that single task already includes the exact action, protected boundaries, completion condition, and focused validation, it may also serve as the Module 4 execution preview. One explicit confirmation can cover the identical content; do not ask the user to approve the same tiny task twice.

## Check the confirmed scope before planning

Before proposing stages:

1. use only the confirmed first-version scope;
2. exclude everything marked later or not needed;
3. do not silently decide undecided items;
4. ask the user about an undecided item only when it blocks a sensible plan;
5. ensure every proposed stage supports a confirmed must-have item or a necessary condition for it.

If new scope appears during planning, name it and return only that decision to Module 2. Do not quietly add it to the project map.

## Create user-centred stages

Describe each stage by the meaningful result it makes possible for the user. Technical work may be needed underneath, but it should not be the first explanation.

Prefer:

> “Stage 1: Let users add a product.”

Avoid:

> “Stage 1: Define the database schema.”

Each stage should:

- have one understandable purpose;
- produce visible or meaningful progress;
- connect clearly to the confirmed first-version scope;
- avoid mixing unrelated goals;
- be small enough for the user to reason about;
- follow a sensible order;
- name any earlier stage it needs in plain language.

Prefer a few meaningful stages over many tiny ones. A stage should answer: “What new thing will work after this is finished?”

For each proposed stage, show:

- **Stage name:** a short user-visible outcome;
- **What becomes possible:** the result after the stage;
- **Why it comes here:** how it moves the confirmed first version forward;
- **What it needs first:** an earlier stage, or “nothing from this plan.”

Do not expand the stage into detailed tasks yet.

## Stage confirmation gate

Present all proposed stages in simple language, followed by a short explanation of the overall order. Then ask:

> “Does this order make sense to you, or would you like to change, combine, remove, or reorder anything?”

Stop and wait. Do not create small tasks until the user explicitly confirms the stage structure.

If the user changes the stages, update the map, explain any material effect on later stages, and reconfirm the changed structure. Do not reconfirm unaffected earlier decisions unnecessarily.

## Expand only the next relevant stage

After the stage map is confirmed, select the first incomplete stage that is needed next and whose earlier needs are satisfied. If the user asks to start elsewhere, explain any practical consequence in plain language and let the user decide when the alternative is workable.

Expand only this stage. Keep every later stage at the project-map level until it becomes current. Do not produce dozens of detailed future tasks.

## Break the current stage into useful tasks

Create a short sequence of tasks that completes the current stage. Each task must include:

1. **Simple task name** — understandable without technical knowledge.
2. **One clear goal** — one coherent result.
3. **What becomes possible** — what the user can do or what useful progress exists afterward.
4. **Included** — the work inside this task.
5. **Not included** — adjacent or future work that must not be pulled in.
6. **Needs first** — earlier work required, explained plainly.
7. **Done means** — observable checks showing the task is complete.

Explain the user-visible result first. Technical details may be recorded later for Codex, but do not make the user interpret technical implementation language and do not create the Module 4 execution prompt here.

## Choose a useful task size

A task is appropriately sized when it:

- produces one meaningful result;
- can be completed and checked independently;
- does not require solving the entire project or several unrelated flows;
- is large enough to be useful rather than an isolated mechanical action.

Split a task when it contains multiple independent user outcomes, crosses unrelated parts of the product, has no single clear finish condition, or would force Codex to hold most of the project in context.

Combine actions when none is useful or verifiable on its own and they naturally form one small outcome. “Create one button” is normally too small; “build the entire account system” is normally too large. The confirmed request may justify exceptions.

## Explain ordering and prerequisites simply

If one task cannot work before another, explain the practical reason:

> “We need to save products before we can show saved products, so saving comes first.”

Do not use unexplained planning jargon. A prerequisite should affect the order only when it is real, not because a conventional technical sequence looks tidy.

## Define observable completion

“Done means” must describe results that can be observed or checked. Include relevant protection for existing work.

Good checks may say:

- the user can enter the required information;
- the user can complete the action and see the expected result;
- saved information remains available where the confirmed scope requires it;
- errors important to this task are handled understandably;
- named unrelated behavior remains unchanged.

Avoid phrases such as “implemented properly” or “works well” without explaining what that means.

## Confirm the current stage's task list

Show the small tasks for the current stage in user-facing language. Explain why their order is useful and identify any real prerequisites. Ask the user to confirm, correct, combine, split, remove, or reorder them.

Stop and wait. Do not select a final next task until this task list is explicitly confirmed.

## Select one active next task

Normally select the earliest incomplete task in the confirmed current-stage list whose prerequisites are complete. It should create meaningful progress and unlock what follows without importing work from future tasks.

If several tasks are independently ready, recommend one based on risk reduction, usefulness, or what it unlocks. Label this as an IntentMap recommendation and let the user choose.

Only one task should be active for Codex unless the user has a clear reason to handle independent work together. Future tasks remain short entries in the project map.

## Next-task confirmation gate

Present the candidate in this format, using plain language:

```text
NEXT TASK

What we are doing:
...

Why this comes now:
...

After it is finished:
...

We are NOT doing yet:
...

Done means:
...
```

Then ask:

> “Does this task make sense, and do you want Codex to work on this next?”

Wait for explicit confirmation. If the user changes it, update the affected task or plan, explain material downstream effects, and ask again. Do not treat a previous confirmation as approval for the revised task.

For the tiny-task exception described above, this confirmation may also confirm the execution preview only when Module 4 adds no new product decision, requirement, boundary, or success condition.

After explicit confirmation, mark the task as ready for Codex. Only then may Module 4 translate it into a focused execution instruction. Do not generate that instruction inside this module and do not begin implementation.

## Handle a change of mind

Changing the plan is normal. When the user changes a stage, task, or order:

1. update the current project map or task list;
2. remove superseded decisions rather than presenting both as current;
3. explain which later stages or tasks are affected and why;
4. keep unaffected confirmed decisions;
5. reconfirm only the materially changed level.

Return to discovery or scope definition only if the change alters the confirmed problem or first-version boundary.

## Protect existing work

For an existing project, state what must remain unchanged in each relevant task. Keep changes limited to the confirmed feature or area, and avoid unrelated cleanup, redesign, or behavior changes.

## Plan progressively to reduce waste

Prefer this rhythm:

```text
small confirmed task -> later execution -> check result -> choose the next task
```

Do not optimize for the fewest words or the greatest number of tasks. Optimize for useful progress with low misunderstanding and little rework.
