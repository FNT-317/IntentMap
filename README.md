# IntentMap

IntentMap is a reusable Codex Skill that helps people turn an uncertain software idea into confirmed product decisions, one focused implementation task, and an evidence-based review before continuing.

**Status: v0.1 release candidate for local testing.** It has passed structural checks and a static walkthrough of 32 stress scenarios. It has not yet been validated through a recorded suite of live model conversations or published as a plugin.

## What IntentMap does

- discovers the real problem without forcing a fixed questionnaire;
- separates user decisions, suggestions, assumptions, and unresolved questions;
- defines and confirms a realistic first-version scope;
- decomposes work progressively and prepares one appropriately sized task at a time;
- filters project context into a focused Codex execution instruction;
- reviews actual changes and validation evidence before proposing the next task.

## What IntentMap does not do

- make important product decisions on the user's behalf;
- treat planning approval as permission for unrelated, external, or destructive actions;
- design the whole future project when only the next stage needs detail;
- guarantee that generated code is correct without inspecting evidence;
- provide hosting, a backend, a website, or a publishing service;
- replace product, security, legal, or accessibility specialists where specialist judgment is needed.

## Test it locally

Codex discovers a skill from a folder containing `SKILL.md`. For repository-only testing, place this project at or symlink it to:

```text
<your-repository>/.agents/skills/intentmap
```

For user-wide testing, place or symlink it to:

```text
$HOME/.agents/skills/intentmap
```

Then start Codex in the relevant repository and invoke it explicitly with `$intentmap` (or choose it from `/skills` where available). Codex may also select it implicitly when a request matches the description. Skill edits are normally detected automatically; restart Codex if an edit is not picked up. See the [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills) for current discovery and invocation details.

This repository is already usable from its present folder for inspection and development; the paths above describe how to expose it as an installed local skill. Module 6 does not install, publish, or distribute it automatically.

## Example starting messages

```text
$intentmap I have an app idea but I haven't thought it through.
```

```text
$intentmap I want to add a feature to my existing project, but I'm not sure exactly how it should work.
```

```text
$intentmap I have a big project and I want to break it into smaller Codex tasks.
```

```text
$intentmap I know roughly what I want. Help me make sure I'm not missing anything before Codex starts.
```

## Workflow

```text
rough idea
  -> discover and confirm the real need
  -> define and confirm first-version scope
  -> confirm user-centred stages
  -> expand and confirm one next task
  -> filter and confirm one Codex instruction
  -> execute outside IntentMap's planning conversation
  -> inspect actual changes and validation
  -> correct, report a blocker, or request result acceptance
  -> update compact project memory
  -> propose, but do not automatically start, the next task
```

`SKILL.md` is the short routing entry point. Detailed operating rules and examples live in `references/` so Codex loads them only when that part of the workflow is relevant. Evaluation-only material lives in `evaluations/` and is not part of the production instruction path.

## Evaluation

Run the dependency-free structural check from the project root:

```powershell
python .\evaluations\check_release.py
```

Use `evaluations/scenarios.md` and `evaluations/rubric.md` for live conversational testing. The included stress-test report is a transparent static trace from each scenario to the applicable rules; it is not a claim that 32 model runs passed.

## Current limitations

- No recorded live multi-model evaluation suite has been run yet.
- Project memory is an instruction pattern, not a separate persistence service.
- Post-execution review depends on access to the actual diff, files, commands, and test evidence.
- “Meaningful” versus “trivial” decisions and ideal task size still require model judgment.
- The skill has not been packaged, installed for the user, published, or production-proven.

## Project structure

- `SKILL.md` — concise entry point and workflow router.
- `agents/openai.yaml` — user-facing name, description, and starter prompt.
- `docs/product-principles.md` — stable product principles.
- `references/` — detailed instructions and examples for Modules 1–5.
- `evaluations/` — Module 6 scenarios, rubric, failure catalogue, report, and structural checker.
