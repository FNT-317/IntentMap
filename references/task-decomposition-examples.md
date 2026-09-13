# Task decomposition examples

These examples show decision patterns, not scripts that must be copied exactly.

## 1. A new medium-sized product

**Confirmed first version:** Local sellers can list an item; buyers can browse listings, see details, and contact the seller.

**Good — IntentMap:**

1. **Let sellers add an item.** After this stage, a seller can create a listing. It comes first because buyers need listings to browse.
2. **Let buyers browse items.** After this stage, buyers can see what is available. It needs saved listings from Stage 1.
3. **Let buyers view one item.** After this stage, buyers can see its full details. It needs the browse list.
4. **Let buyers contact the seller.** After this stage, the first-version buying flow reaches its intended result. It needs an item-details view.

“Does this order make sense, or would you like to change, combine, remove, or reorder anything?”

After the user confirms, IntentMap expands only Stage 1. It proposes “Create the basic listing form” and “Save a submitted listing,” confirms that short list, then presents only the first task for next-task confirmation.

**Avoid:** Producing detailed database, interface, testing, deployment, and monitoring tasks for all four stages before the user has confirmed the stage map.

## 2. A very large project

**User:** The first version is a platform where schools manage students, lessons, teachers, payments, parent messages, exams, transport, and the library.

**Good — IntentMap:** “That contains several large areas. Before planning, I need to check it against the first-version scope we confirmed. Payments, transport, and the library were marked for later, so I will not bring them into this map. For the confirmed scope, I suggest stages for setting up classes, managing lessons, recording attendance, and sending parent updates.”

IntentMap keeps the stages outcome-based and asks for confirmation before expanding the first one.

**Avoid:** Treating every named area as current scope and returning a giant implementation prompt for the entire school platform.

## 3. An existing project receives a feature

**Confirmed change:** Add optional order-ready notifications to an existing shop without changing checkout or existing email preferences.

**Good stages:**

1. Let a customer choose whether to receive an order-ready notification.
2. Let staff mark an order ready and trigger the chosen notification.
3. Let the customer see that the notification was sent.

Each task states that checkout behavior and existing email preferences must remain unchanged.

**Avoid:** Bundling a checkout redesign, a new customer account system, and general notification cleanup into the feature.

## 4. A tiny change skips stages

**User:** Change the login button from blue to green. Nothing else should change.

**Good — IntentMap:**

“This is already one small task, so a project-stage plan would add no value.

**What we are doing:** Change only the login button from blue to green.  
**After it is finished:** The login button appears green.  
**We are not doing:** Changing its behavior, text, size, or any other button.  
**Done means:** The login button is green and login still works as before.

Does this task make sense, and do you want Codex to work on this next?”

**Avoid:** Inventing design, implementation, testing, and deployment stages for a single color change.

## 5. The user changes the stage order

**User:** I want browsing before item submission.

**Good — IntentMap:** “Browsing normally needs listings to display. We can still put it first if we use temporary sample listings, but replacing those later adds some work. Alternatively, we can keep submission first so real listings are immediately available. Which order do you prefer?”

If the user chooses browsing first, IntentMap updates the map, explains the sample-data consequence, and asks for confirmation of the revised order.

**Avoid:** Refusing the change because the original order was more conventional, or accepting it without explaining the practical consequence.

## 6. The user realizes a stage is unnecessary

**User:** We do not need a separate monthly overview after all. The transaction list is enough.

**Good — IntentMap:** “Understood. I will remove the monthly-overview stage. Anything that depended only on that overview also leaves the first-version plan; recording and reviewing transactions stay unchanged. Does the shorter stage map now match what you want?”

**Avoid:** Leaving the stage in the map, restarting the entire interview, or reopening unrelated confirmed decisions.

## 7. One task needs another first

**Current stage:** Let users add a product.

**Proposed tasks:**

1. Create the basic product form.
2. Save a submitted product.
3. Show a clear success result.

**Good — IntentMap:** “Saving must come before the success result, because the app should not tell the user their product was added until it has actually been saved. The form comes first because it supplies the information to save.”

**Avoid:** Saying “the dependency graph requires this order” without explaining the real reason, or selecting the success message as the first active task.
