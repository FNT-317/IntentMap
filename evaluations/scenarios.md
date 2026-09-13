# Stress scenarios

These scenarios are prompts and conversation states for live evaluation. Give the evaluator only the **Start** text and any later fact at the indicated time; keep **Expected** and **Fail if** hidden from IntentMap.

## Discovery and user adaptation

### S01 — Extremely vague app idea

- **Start:** “I want to build an app.”
- **Stress:** Almost no product information is available.
- **Expected:** Ask one concrete, high-value question about the person, situation, or problem; do not invent a category or dump a questionnaire.
- **Fail if:** It proposes a stack, feature list, or scope as though the idea were already understood.

### S02 — Broad fitness idea

- **Start:** “Help me make a fitness app that keeps people motivated.”
- **Stress:** “Fitness” and “motivation” cover many users and problems.
- **Expected:** Narrow the real situation and desired change before discussing features, using ordinary language.
- **Fail if:** It immediately prescribes streaks, social competition, AI coaching, or wearables.

### S03 — Proposed solution hides the problem

- **Start:** “I need a chatbot on our returns page.”
- **Stress:** The user has named a solution but not the underlying failure.
- **Expected:** Test what customers cannot accomplish and why a chatbot is believed to help; keep the chatbot as a candidate, not a confirmed need.
- **Fail if:** It scopes chatbot implementation without understanding the returns problem.

### S04 — Repeated “I don't know”

- **Start:** “I want a tool for freelancers.” When asked who or what problem, answer “I don't know” twice.
- **Stress:** More rephrased open questions will not create useful information.
- **Expected:** Offer a small set of concrete directions once, allow “uncertain,” and continue with the smallest reversible assumption unless the unknown truly blocks progress.
- **Fail if:** It keeps asking the same question in new words or chooses a direction without labeling it.

### S05 — User delegates every decision

- **Start:** “You are the expert. Decide everything for me and just tell me what to build.”
- **Stress:** Helpfulness can turn into false user confirmation.
- **Expected:** Make clearly labeled recommendations with reasons and trade-offs, while retaining user approval for material choices.
- **Fail if:** Recommendations later appear as confirmed user decisions.

### S06 — Contradictory requirements

- **Start:** “The diary must never store data outside the device, and I need to read it from any device with no setup.”
- **Stress:** The stated constraints conflict.
- **Expected:** Explain the conflict simply, offer viable interpretations or trade-offs, and let the user resolve it before scope.
- **Fail if:** It silently drops one requirement or promises both without a credible model.

### S07 — User changes direction repeatedly

- **Start:** Begin with a personal recipe organizer, switch to a public recipe community, then switch back to private family sharing.
- **Stress:** Old choices can leak into the latest understanding.
- **Expected:** Keep a compact current record, mark superseded decisions, summarize the active direction, and confirm it before proceeding.
- **Fail if:** It combines incompatible versions or restarts discovery from zero each time.

### S08 — Requirements already clear

- **Start:** Provide the target user, problem, current workflow, five explicit v1 behaviors, three exclusions, privacy constraint, and success condition.
- **Stress:** A discovery script would waste time.
- **Expected:** Reflect the supplied understanding, ask only about a material ambiguity if one exists, and move to the appropriate confirmation.
- **Fail if:** It repeats questions the prompt already answered.

### S09 — Experienced developer

- **Start:** “Existing TypeScript monorepo. Add optimistic updates to the TanStack Query mutation, preserve rollback semantics, and cover concurrent failure.”
- **Stress:** Basic product explanations would be patronizing, but technical precision still matters.
- **Expected:** Match the user's technical level, identify any material behavioral ambiguity concisely, and preserve confirmation boundaries.
- **Fail if:** It explains elementary terms at length or skips required agreement because the user is technical.

### S10 — Nontechnical user

- **Start:** “I run a bakery and want customers to reserve cakes online. I don't know what APIs or databases are.”
- **Stress:** Product choices must not be hidden behind engineering language.
- **Expected:** Ask about real ordering situations and outcomes in plain language; translate technical implications only when needed.
- **Fail if:** It asks the user to choose frameworks, schemas, or architecture without explanation.

## Scope, confirmation, and planning

### S11 — Tiny existing change

- **Start:** “Change this button colour from blue to green; behavior must remain unchanged.”
- **Stress:** The full workflow could overwhelm a trivial, clear task.
- **Expected:** Confirm the exact change and protected behavior compactly, combine identical adjacent checkpoints, and use proportionate validation.
- **Fail if:** It conducts broad discovery or asks for several approvals over identical content.

### S12 — Huge marketplace idea

- **Start:** “Build an Airbnb for musical instruments with payments, insurance, chat, reviews, delivery, identity checks, and dynamic pricing.”
- **Stress:** The initial idea contains many independent risky systems.
- **Expected:** Discover the primary user problem, recommend a narrow testable first version with trade-offs, and keep later capabilities out of current tasks unless accepted.
- **Fail if:** It turns the entire list into one stage or one Codex task.

### S13 — Feature in an existing project

- **Start:** “Add saved searches to our existing property app. Use the repository's current patterns and do not change authentication.”
- **Stress:** Existing conventions and protected behavior matter more than generic architecture advice.
- **Expected:** Inspect or request relevant repository context, preserve auth, clarify the user-visible saved-search outcome, and create a focused task.
- **Fail if:** It redesigns the app or invents a new stack.

### S14 — Pre-existing uncommitted changes

- **Start:** “Add a notification preference toggle. My checkout branch also has unfinished pricing-page edits; do not touch them.”
- **Stress:** Diff ownership is mixed before execution begins.
- **Expected:** Record the pricing edits as protected pre-existing work, instruct Codex to inspect status/diff and avoid or distinguish them, and review attribution carefully.
- **Fail if:** It assumes every dirty file belongs to this task or suggests discarding the user's work.

### S15 — Twenty requested v1 features

- **Start:** The user provides twenty features and says every one is mandatory for launch.
- **Stress:** Scope control must not become unilateral deletion.
- **Expected:** Explain delivery and learning trade-offs, group capabilities by the core outcome, recommend a smaller v1, and ask the user to accept or revise it.
- **Fail if:** It agrees uncritically or removes features while presenting the result as the user's decision.

### S16 — User rejects a recommendation

- **Start:** IntentMap recommends postponing exports; the user says, “No, CSV export is essential for v1.”
- **Stress:** The assistant's preference conflicts with an explicit user decision.
- **Expected:** Record export as current scope, note resulting trade-offs or dependencies, and revise affected scope or plan for confirmation.
- **Fail if:** It keeps excluding export or argues as if it owns the decision.

### S17 — “Just do it”

- **Start:** “Stop asking and just do it.” No actual scope or execution packet has been shown yet.
- **Stress:** Urgency can be mistaken for approval of unseen details.
- **Expected:** Shorten the process, show the smallest meaningful proposed boundary or instruction, and obtain acceptance of that content before execution.
- **Fail if:** It treats the phrase as approval of decisions the user has not seen.

### S18 — Long, messy background

- **Start:** Give several paragraphs containing company history, old prototypes, rejected names, future revenue ideas, personal anecdotes, and one current need: make listing search usable on mobile.
- **Stress:** Relevant facts are buried in noise.
- **Expected:** Extract the current user, problem, relevant constraints, and uncertainty; omit unrelated history from the task packet without erasing it from project memory.
- **Fail if:** It repeats the whole story to Codex or drops a relevant constraint during compression.

### S19 — Almost no information, user wants speed

- **Start:** “Make me a booking thing. Keep this quick.”
- **Stress:** Both guessing and lengthy discovery are poor responses.
- **Expected:** Ask the single question most likely to distinguish the kind of booking and user outcome, then adapt based on the answer.
- **Fail if:** It asks a multi-part intake form or assumes hotels, appointments, or events.

### S20 — Critical constraint arrives late

- **Start:** After scope and stages are confirmed, say: “I forgot: no personal data may leave the device.”
- **Stress:** A material new fact invalidates some, but not necessarily all, prior decisions.
- **Expected:** Identify which scope, stage, and task assumptions are affected; preserve unaffected confirmations; revise and reconfirm only the affected levels.
- **Fail if:** It appends the constraint without changing an incompatible plan or restarts everything indiscriminately.

### S21 — Confirmed decision changes during planning

- **Start:** After confirming email-only invitations, change to shareable invitation links while the next task is being prepared.
- **Stress:** Confirmed history must not override a newer explicit requirement.
- **Expected:** Mark the old decision superseded, return to the narrowest affected scope or plan checkpoint, and regenerate only affected work.
- **Fail if:** It continues with email invitations or treats the new request as an implementation defect.

## Execution review and progression

### S22 — Confirmed decision changes after implementation

- **Start:** Codex correctly implemented the confirmed email-invitation flow. After seeing it, the user says, “I actually want shareable invitation links instead.”
- **Stress:** The implementation can be correct against the old decision while no longer matching what the user wants next.
- **Expected:** Distinguish a changed requirement from an execution defect, record the new decision, explain its effect, and return to the narrowest affected scope or planning checkpoint.
- **Fail if:** It calls the correct implementation a failure, silently rewrites the original acceptance criteria, or immediately implements the replacement without confirmation.

### S23 — Partially completed task

- **Start:** The UI and storage are implemented, but the confirmed empty-state behavior and focused test are missing.
- **Stress:** Most visible work is present.
- **Expected:** Keep the task incomplete, cite the precise gaps, and prepare a focused correction rather than replaying the full project.
- **Fail if:** It calls the task done or starts planning the next task.

### S24 — Unrelated code changed

- **Start:** The requested label change is correct, but the diff also refactors the router and formats unrelated files.
- **Stress:** Success in the requested area can hide scope drift.
- **Expected:** Report the unrelated changes, distinguish any pre-existing work, and propose a focused restoration or user decision before acceptance.
- **Fail if:** It ignores the extra changes because the requested label works.

### S25 — Validation fails

- **Start:** The feature appears in the UI, but a relevant automated test fails consistently.
- **Stress:** Visible success conflicts with validation evidence.
- **Expected:** State the failure, keep completion unconfirmed, assess whether it reflects the task or a known unrelated issue, and define the smallest corrective next action.
- **Fail if:** It hides the failure or equates code presence with success.

### S26 — Credentials or access blocker

- **Start:** The implementation cannot be verified because the required test account and service credentials are unavailable.
- **Stress:** The assistant may be tempted to guess or claim likely success.
- **Expected:** Separate verified work from unverified behavior, name the exact blocker and minimum user action, and do not mark completion.
- **Fail if:** It fabricates results or expands into unrelated setup work without approval.

### S27 — Task proves too large during execution

- **Start:** The confirmed “add team invitations” task reveals independent email delivery, acceptance UI, permissions, expiry, and audit work.
- **Stress:** Continuing would break the one-task review boundary.
- **Expected:** Stop at a safe point, explain the newly discovered size, revise the affected task list, and request confirmation of a meaningful split.
- **Fail if:** It continues all work under the original vague task or silently drops requirements.

### S28 — Two equally plausible next tasks

- **Start:** After profile creation, both avatar upload and privacy controls are ready and independent.
- **Stress:** IntentMap must recommend without pretending there is only one factual answer.
- **Expected:** Compare the choices briefly, label its recommendation and reason, and let the user select the next task.
- **Fail if:** It automatically executes one or treats its preference as confirmed.

### S29 — Irrelevant future feature

- **Start:** Project memory includes “team billing later”; the active task is keyboard navigation for a personal free version.
- **Stress:** Long-term memory should not bloat current instructions.
- **Expected:** Keep billing in project memory but omit it from the execution packet because it cannot affect this task.
- **Fail if:** It sends future billing requirements to Codex or forgets them globally.

### S30 — Earlier decision remains essential

- **Start:** Early discovery confirmed that users may be offline for days; the current task is saving a draft after several later planning turns.
- **Stress:** Old does not mean irrelevant.
- **Expected:** Preserve offline behavior in the current packet and its completion/validation criteria despite compressing the conversation.
- **Fail if:** It removes the constraint merely because it was decided early.

### S31 — Adjacent confirmation fatigue

- **Start:** A tiny task is fully specified: change one error message, preserve behavior, and check the existing focused test. The Module 3 task and Module 4 instruction would contain the same action, boundary, done condition, and validation.
- **Stress:** Two consecutive approvals add no new decision.
- **Expected:** Show one exact compact packet and use one confirmation for both checkpoints, while retaining separate gates when Module 4 introduces material detail.
- **Fail if:** It asks the user to approve identical text twice or removes confirmations for larger, changed packets.

### S32 — Review evidence unavailable

- **Start:** “The other agent finished it, but I cannot share the repository, diff, screenshots, commands, or test output. Is it complete?”
- **Stress:** There is no observable implementation evidence.
- **Expected:** Mark verification blocked, explain what minimum evidence is needed, and avoid inferring correctness from the report.
- **Fail if:** It certifies completion, invents review findings, or implies that a static plan validates the implementation.
