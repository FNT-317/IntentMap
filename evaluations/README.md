# IntentMap evaluations

This directory contains evaluation material for the v0.1 release candidate. It is deliberately separate from the production instructions in `SKILL.md` and `references/`.

## Files

- `scenarios.md` — 32 realistic prompts and situations that stress the full workflow.
- `rubric.md` — a simple 0–2 behavior-scoring system and critical failure rules.
- `failure-modes.md` — likely ways IntentMap can fail and the safer expected response.
- `context-and-task-sizing.md` — concrete task-size examples and current-context comparisons.
- `stress-test-report.md` — the static walkthrough results, rule changes, limitations, and release recommendation.
- `check_release.py` — a dependency-free structural check for frontmatter, links, scenario coverage, and file organization.

## How to evaluate a conversation

1. Choose one scenario without giving IntentMap its expected behavior.
2. Run the conversation naturally and preserve the complete output.
3. Score only behavior that the conversation reached; mark other rubric items `N/A`.
4. Record exact evidence for every score of 0 or 1.
5. Treat any critical failure as a release blocker even when the average score is high.
6. Improve the narrow rule that caused the observed failure, then rerun the affected scenario and one nearby regression scenario.

The included report is a static rule-coverage walkthrough, not a claim that 32 live model conversations passed.
