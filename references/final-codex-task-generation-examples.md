# Codex execution instruction examples

These examples show how much context to keep. They are patterns, not mandatory templates.

## 1. A tiny UI change

**Confirmed task:** Change the login button from blue to green; nothing else should change.

**Good focused instruction:** “Change only the login-page submit button from blue to green. Keep its text, size, behavior, and all other page styling unchanged. Verify that login still works.”

**Bad oversized instruction:** A seven-section packet repeating the product history, target users, future account plans, and full test strategy for one color change.

**Bad underspecified instruction:** “Make the button green.” It does not identify the button or protect other styling and behavior.

## 2. A new feature in an existing project

**Confirmed task:** Let shop staff mark an order ready and send the customer's already-selected notification. Existing checkout and email preferences must remain unchanged.

**Good focused instruction:**

```text
TASK
Add an order-ready action for shop staff and trigger the notification channel the customer already selected.

RELEVANT CONTEXT
This is an existing shop. First inspect the current order-status and notification code and nearby tests. Reuse current conventions.

DO NOT CHANGE
- Do not redesign checkout.
- Do not change how email preferences are stored or selected.
- Do not add another notification channel.
- Avoid unrelated refactoring or new dependencies.

DONE WHEN
- Staff can mark an eligible order ready.
- The existing selected notification is sent once.
- Checkout and preference behavior remain unchanged.

VALIDATION
Run relevant order and notification tests and verify this flow directly.
```

**Avoid:** Telling Codex to rebuild order handling or inspect the entire repository.

## 3. A task in a new project

**Confirmed task:** Create the basic product submission form. Saving belongs to the next task.

**Good focused instruction:**

```text
TASK
Create the basic product submission form.

REQUIREMENTS
- Provide fields for product name, price, and description.
- Follow the current project's UI conventions where they exist.

DO NOT CHANGE
- Do not save products yet.
- Do not add browsing, messaging, payment, or account features.

DONE WHEN
- The form renders correctly.
- A user can enter all three values.

VALIDATION
Check the form directly and run relevant existing UI tests if available.
```

The marketplace's later stages are omitted because they do not affect this form task.

## 4. A long conversation contains mostly irrelevant history

**Conversation history:** The user discussed marketplace names, logo colors, possible subscriptions, international expansion, seller ratings, delivery partnerships, and several rejected payment ideas. The confirmed current task is only the basic unsaved product form with name, price, and description.

**Good result:** Use the focused instruction from Example 3. Remove branding discussion, rejected payments, subscriptions, expansion, ratings, delivery, and the full project story.

**Bad oversized prompt:** Copying the entire conversation “for context.” This makes unrelated ideas look active and distracts Codex from the form.

**Bad underspecified prompt:** “Build the marketplace form.” This loses the three confirmed fields and the boundary that saving is not part of this task.

## 5. An earlier decision must be preserved

**Earlier confirmed decision:** A private journal must store entries only on the user's device and must not use analytics.

**Current task:** Save a journal entry after the user finishes writing it.

**Good focused context:** Include local-only storage and no analytics because those decisions constrain implementation. Exclude unrelated discussion about future themes and optional sharing, which was rejected.

**Avoid:** Dropping the privacy decision because it came from an earlier conversation, or adding cloud sync because it is technically convenient.

## 6. A material question is unresolved

**Confirmed task:** Add dark mode and remember the user's choice.

**Unresolved point:** It is unclear whether the site should follow the device setting until the user makes a choice, or always start in light mode.

**Good — IntentMap:** “Before I prepare the Codex instruction, one choice could change how the feature behaves: should the site initially follow the device's light or dark setting, or stay light until the user changes it?”

Only after the answer is confirmed should IntentMap generate the packet.

**Avoid:** Guessing one behavior and writing it as though the user decided it.

## 7. The task has become too large

**Supposed current task:** Build sign-up, login, password reset, profile editing, two-factor authentication, and administrator access.

**Good — IntentMap:** “This now contains several independently useful flows and more than one finish condition. I recommend returning to the current-stage task list and starting with the basic sign-up flow. Does that split match what you want?”

**Avoid:** Hiding all six outcomes inside one giant execution prompt.

## 8. Codex should inspect existing code first

**Confirmed task:** Add a percentage discount to an existing checkout that already supports fixed discounts.

**Good focused instruction:** Tell Codex to inspect the current discount calculation, checkout display, and related tests; extend the established pattern where practical; preserve fixed discounts; and avoid replacing the pricing library or refactoring unrelated checkout code.

**Avoid:** Dictating new file names and a new calculation architecture without seeing the code, or saying only “add percentage discounts” with no requirement to protect fixed discounts.
