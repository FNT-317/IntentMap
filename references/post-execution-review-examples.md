# Post-execution review examples

These examples show review patterns, not fixed scripts.

## 1. A task completed correctly

**Confirmed task:** Create an unsaved product form with name, price, and description fields. Do not add persistence or change unrelated pages.

**Observed result:** All three fields render and accept input, relevant UI tests pass, no unrelated files changed.

**Good — IntentMap:** “The form now accepts the product name, price, and description. Saving was not added, as agreed, and the relevant checks pass. This step appears complete. Does it match what you expected?”

**Avoid:** Marking the task complete and starting persistence before the user accepts the result.

## 2. A partially completed task

**Observed result:** The name and description fields work, but the required price field is missing.

**Good — IntentMap:** “Part of the form is ready, but the price field we agreed on is missing. I would not mark this complete yet. The smallest correction is to add that field while leaving the working fields unchanged.”

**Avoid:** Calling the task complete because most of the form exists.

## 3. Unrelated code was changed

**Confirmed task:** Change only the login button color.

**Observed result:** The color changed, but authentication logic was also refactored.

**Good — IntentMap:** “The requested color change is present, but the login logic was also modified even though that was outside the task. I recommend restoring only those unrelated logic changes and then rechecking login. Would you like to make that correction?”

**Avoid:** Ignoring the refactor because login currently appears to work, or reverting it without checking whether it predated this execution.

## 4. Validation failed

**Observed result:** The feature appears in the page, but the relevant existing page test now fails.

**Good — IntentMap:** “The feature is visible, but a directly related test now fails. I cannot treat this step as complete yet. We need to understand and correct that failure, then review again.”

**Avoid:** Saying “done” merely because files were changed.

## 5. A focused correction loop

**Original task:** Create the basic product form.

**First review:** The price field is missing; name and description work.

**Focused correction:** Add only the price field, preserve the two working fields, do not add saving, and rerun the form checks.

**Second review:** All three fields work and tests pass.

**Good — IntentMap:** Summarize the corrected result and ask the user to accept it. Do not replay marketplace discovery, scope, or future stages in the correction prompt.

## 6. The user changes their mind after seeing the result

**Confirmed result:** One green login button was implemented correctly.

**User:** Actually, I now want separate “Sign in” and “Create account” buttons.

**Good — IntentMap:** “The original one-button task was completed as agreed. Two buttons are a new requirement rather than a correction. I will update the relevant scope and task plan before asking Codex to change it.”

**Avoid:** Calling the original execution a failure or silently adding the second button.

## 7. A task is blocked

**Task:** Verify sending through a production email service.

**Observed blocker:** No service credentials or test account are available.

**Good — IntentMap:** “The local notification behavior is ready, but actual delivery cannot be verified without service access. I cannot mark that delivery check complete. The minimum next step is access to a test account or approved credentials.”

**Avoid:** Claiming delivery works, inventing credentials, or changing providers without user approval.

## 8. A tiny UI change gets a tiny review

**Good — IntentMap:** “The login button is now green, its text and behavior are unchanged, and login still works. Does that look right to you?”

**Avoid:** Producing a multi-page project status report for this one-line change.

## 9. A risky change needs deeper validation

**Task:** Change account-password reset behavior.

**Good review:** Inspect the relevant diff and current reset flow; verify valid, expired, reused, and malformed reset links; confirm passwords are handled through established secure code; run the focused authentication tests; check that sign-in behavior remains intact; clearly report any failure.

**Avoid:** Checking only that the reset page renders, or running a huge unrelated test suite while skipping the important failure paths.

## 10. A completed task moves cleanly to the next task

**Accepted result:** The basic product form is complete.

**Good — IntentMap:**

```text
COMPLETED
✓ Sellers can enter a product name, price, and description.

CURRENT STAGE
Let sellers publish a product.

NEXT SUGGESTED TASK
Save the submitted product, because browsing later needs real listings to exist.
```

“Does this next task make sense, and do you want to use it?”

After confirmation, IntentMap returns to Module 4 to create and confirm a focused instruction. It does not execute the task automatically.

**Avoid:** Beginning product saving immediately after the form review passes.
