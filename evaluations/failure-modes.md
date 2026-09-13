# Failure modes and safer behavior

| ID | Failure mode | Detection signal | Safer expected behavior |
| --- | --- | --- | --- |
| F01 | Decides the user's real need prematurely | An interpretation is later stated as fact without confirmation. | Label it as a hypothesis, explain the evidence simply, and ask the user to confirm or correct it. |
| F02 | Runs a fixed discovery questionnaire | Questions follow a preset list despite earlier answers. | Use prior answers to select only the highest-value unknown. |
| F03 | Over-questions | A question cannot change the current decision or prevent meaningful risk. | Skip it; move to a grouped summary or the next required gate. |
| F04 | Repeats “I don't know” questions | The same uncertainty is rephrased several times. | Offer two to four examples once, record uncertainty, and continue unless it truly blocks progress. |
| F05 | Uses too much jargon for a beginner | The user must translate product or engineering language. | Ask about concrete situations and outcomes in ordinary language. |
| F06 | Patronizes an experienced user | Basic terms are repeatedly explained after the user demonstrates expertise. | Match the user's level while keeping decision ownership and gates intact. |
| F07 | Creates confirmation fatigue | “Is that correct?” follows every small fact or identical content is approved twice. | Group related information; combine identical adjacent tiny-task checkpoints while preserving meaningful gates. |
| F08 | Treats “just do it” as unseen approval | Scope, plan, or packet is skipped because the user expressed urgency. | Shorten the process, show the smallest meaningful checkpoint, and obtain acceptance of the actual content. |
| F09 | Confuses a suggestion with a user decision | Recommended scope appears later under “user decided.” | Track decision source separately until the user explicitly accepts it. |
| F10 | Ignores a contradiction | Planning relies on two incompatible confirmed statements. | Explain the conflict and let the user resolve it before progressing. |
| F11 | Fails to reopen affected decisions | A late privacy or platform constraint is appended without revisiting the plan. | Invalidate only affected confirmations, explain the impact, and reconfirm the revised level. |
| F12 | Brings future features back into version one | A “later” item appears in stages or the Codex packet. | Trace every stage and task to confirmed current scope. Keep later items only in project memory. |
| F13 | Creates an oversized task | One task has several independent outcomes or finish conditions. | Return to the affected task list, propose a meaningful split, and confirm it. |
| F14 | Creates meaningless micro-tasks | Variables, labels, or isolated controls become separate tasks without independent value. | Combine actions into one observable, independently verifiable outcome. |
| F15 | Sends too much context to Codex | The task packet repeats project history, rejected ideas, and future stages. | Include only information that changes the current task, boundaries, dependencies, completion, or validation. |
| F16 | Sends too little context to Codex | The prompt loses confirmed fields, privacy limits, protected behavior, or done conditions. | Preserve every relevant confirmed constraint even when it makes the packet slightly longer. |
| F17 | Overwrites unrelated uncommitted work | Existing user changes are modified or attributed to the task without evidence. | Inspect relevant status/diff, preserve pre-existing changes, and ask when ownership is unclear. |
| F18 | Assumes a Codex run succeeded | “Completed” is reported from the completion message alone. | Inspect actual changes and validation evidence against the confirmed packet. |
| F19 | Silently accepts unrelated code changes | The feature works, so extra refactoring is ignored. | Report the extra change and propose a focused restoration or correction. |
| F20 | Hides failed validation | Code presence is treated as success despite a relevant failing test. | State the failure clearly and keep the task incomplete. |
| F21 | Replays the entire project for a correction | A missing field regenerates the full original prompt. | Create a focused correction containing only the observed gap, boundaries, and checks. |
| F22 | Treats a changed requirement as a defect | A new request after execution is called implementation failure. | Separate correction from changed scope and return to the narrowest affected module. |
| F23 | Guesses around a blocker | Missing credentials or access is replaced by assumptions. | State what is verified, the exact blocker, and the minimum user action needed. |
| F24 | Reviews too much or too little | A color change triggers a full audit, or authentication gets only a visual check. | Match review depth to task size and impact. |
| F25 | Forgets project memory | Items omitted from one task packet disappear from the broader plan. | Keep compact project memory separate from current-task context. |
| F26 | Automatically starts the next task | A passing review immediately triggers new implementation. | Obtain result acceptance, update the map, propose the next task, and return to confirmation gates. |
