---
title: "Human Review Strategies"
description: "AI-generated output requires human review, but reviewing AI output is different from reviewing human output."
type: guide
capability: ai
status: published
tags: [human, review, strategies]
last_reviewed: 2026-07-28
---

# Purpose

AI-generated output requires human review, but reviewing AI output is
different from reviewing human output. AI can produce confident-looking
incorrect answers, plausible but suboptimal designs and code that passes
tests but has subtle issues.

This guide describes strategies for reviewing AI output effectively
across different engineering contexts.

# Principles

## Review the Reasoning, Not Just the Result

AI output often looks correct on the surface. Evaluate the reasoning
behind the output, not just whether the output appears reasonable.

## Trust but Verify

AI output should be treated as a draft from a junior engineer who works
fast but needs supervision. Trust increases with experience, but
verification never goes away.

## Review at the Right Level

Different types of AI output need different review approaches:
- Code: correctness, security, style, edge cases.
- Architecture: trade-offs, constraints, consistency.
- Documentation: accuracy, clarity, completeness.

## Invest in Good Prompts to Reduce Review Burden

Better prompts produce better output. Investing time in prompt quality
reduces the time needed for review.

# Review Strategies

## Strategy 1: Read-Through

Best for: Short code snippets, configuration, documentation.

1. Read the output carefully as if written by a human.
2. Look for logical errors, not just syntax.
3. Verify against your mental model of what correct output looks like.
4. Check for signs of hallucination (confident-sounding incorrect facts).

| Do                           | Don't                                  |
|------------------------------|----------------------------------------|
| Read every line.             | Skim and assume it is correct.         |
| Question assumptions.        | Trust because it looks well-formatted. |
| Compare with your knowledge. | Accept without understanding.          |

## Strategy 2: Test-Driven Review

Best for: Generated code, algorithms, business logic.

1. Run the generated code against existing tests.
2. Write additional tests for edge cases the AI might have missed.
3. Verify the code handles error paths, not just the happy path.
4. Check for security implications (input validation, injection, auth).

| Do                                           | Don't                                   |
|----------------------------------------------|-----------------------------------------|
| Run tests before reading the code.           | Review code in isolation from tests.    |
| Add edge case tests the AI did not consider. | Assume passing tests mean correct code. |
| Test with realistic data.                    | Use only minimal test data.             |

## Strategy 3: Decomposition Review

Best for: Complex architectural output, multi-file changes.

1. Break the AI output into independent sections.
2. Review each section separately.
3. Verify that sections work together (interfaces, data flow).
4. Check for consistency across the output.

| Do                                    | Don't                               |
|---------------------------------------|-------------------------------------|
| Review interfaces between components. | Review each file in isolation.      |
| Trace data flow through the system.   | Assume the AI handled cross-cutting |
|                                       | concerns correctly.                 |
| Check for duplicated logic.           | Accept repetition without question. |

## Strategy 4: Comparison Review

Best for: Alternative implementations, refactoring, migrations.

1. Ask AI to produce two or more approaches.
2. Compare them against each other and against your requirements.
3. Identify where they agree — those areas are likely correct.
4. Investigate where they differ — those areas need human judgment.

| Do                                   | Don't                                 |
|--------------------------------------|---------------------------------------|
| Ask for multiple approaches.         | Accept the first response.            |
| Compare trade-offs explicitly.       | Choose based on presentation quality. |
| Use differences to identify areas of | Assume agreement means correctness.   |
| uncertainty.                         |                                       |

## Strategy 5: Walkaway Review

Best for: Large or complex output where fresh eyes help.

1. Review the AI output briefly for obvious issues.
2. Walk away for at least 30 minutes (or overnight).
3. Return and review with fresh perspective.
4. Issues that were invisible before often become obvious.

| Do                                           | Don't                             |
|----------------------------------------------|-----------------------------------|
| Take a break before final review.            | Review complex output when tired. |
| Return with specific questions.              | Trust your first impression.      |
| Use the second review as the final decision. | Rush through the second review.   |

# Review Depth by Risk

| Risk Level | Examples                  | Review Strategy                        | Time Budget |
|------------|---------------------------|----------------------------------------|-------------|
| Critical   | Auth, payments, security  | Test-Driven + Decomposition + Walkaway | 30-60 min   |
| High       | Core business logic, APIs | Test-Driven + Read-Through             | 15-30 min   |
| Medium     | Standard features, CRUD   | Read-Through + Spot-check              | 5-15 min    |
| Low        | Boilerplate, tests, docs  | Spot-check or automated                | < 5 min     |

# Common AI Failure Modes

| Failure Mode        | What to Look For                                  |
|---------------------|---------------------------------------------------|
| Hallucination       | Confident-sounding but incorrect facts,           |
|                     | references to non-existent APIs or papers.        |
| Plausible but wrong | Code that looks correct but has subtle bugs       |
|                     | (off-by-one, wrong operator, missing null check). |
| Missing edge cases  | Only the happy path is handled; errors and        |
|                     | boundary conditions are ignored.                  |
| Inconsistency       | Different parts of the output contradict          |
|                     | each other (variable names, interfaces,           |
|                     | assumptions).                                     |
| Over-engineering    | More complex than necessary — abstractions        |
|                     | that do not add value for the current use case.   |
| Security blindness  | No input validation, no auth checks, secrets      |
|                     | hardcoded, SQL injection vulnerable.              |
| Style drift         | Output does not match project conventions         |
|                     | (naming, formatting, patterns).                   |

# Anti-patterns

- ***Blind acceptance***: Using AI output without any review.
- ***Superficial review***: Skimming without reading carefully.
- ***Over-correction***: Spending as much time reviewing low-risk output
  as high-risk output.
- ***Confirmation bias***: Accepting output that matches your expectations
  without verification.
- ***Review fatigue***: Reviewing too much AI output in one session leads
  to missed issues.

# Related Documents

- [Agentic Workflows](./agentic-workflows.md)
- [AI Collaboration Patterns](./collaboration-patterns.md)
- [AI-Assisted Code Review Playbook](../../playbooks/ai/ai-assisted-code-review.md)
- [AI Usage Checklist](../../checklists/ai-usage.md)
- [AI Safety and Verification](../ai/ai-safety.md)
