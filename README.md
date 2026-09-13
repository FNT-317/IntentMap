# IntentMap

IntentMap is a reusable Codex Skill for helping people turn a vague software idea into a clear, user-confirmed understanding of the project, a user-confirmed scope, and later a sequence of manageable development tasks.

It is designed for people who may not know software-development language. It should explain decisions simply, separate the user's choices from its own suggestions, and ask for confirmation before moving to each major step.

## Current state

The project skeleton, Module 1 (Requirement Discovery), and Module 2 (Scope Definition) are complete. The project contains:

- the required Codex Skill entry point;
- user-facing skill metadata;
- the product principles;
- working instructions for requirement discovery, scope definition, and their confirmation points;
- short examples of good and poor discovery and scope conversations;
- placeholder areas for the later workflow parts;
- a place for future behavior tests.

Task decomposition and final task generation have not been implemented yet. No dependencies are required.

## Planned flow

```text
Rough idea
  -> understand the real problem
  -> confirm that understanding
  -> agree what belongs in the first version
  -> confirm the scope
  -> divide the project into understandable stages
  -> confirm the stages
  -> prepare one small next task
  -> confirm the task
  -> allow implementation to begin
```

## Project map

- `SKILL.md` — the entry point Codex loads when the skill is used.
- `agents/openai.yaml` — the name, description, and starter prompt shown in Codex.
- `docs/product-principles.md` — the lasting rules for how IntentMap should behave.
- `references/` — working Module 1 and Module 2 instructions, with placeholders for later modules.
- `evaluations/` — planned behavior checks for the finished skill.
