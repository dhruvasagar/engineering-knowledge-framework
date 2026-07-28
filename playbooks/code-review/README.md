---
title: "Code Review Playbook"
description: "Repeatable workflow for conducting effective code reviews"
---


# Objective

Ensure every code change is reviewed for correctness, design quality,
maintainability and consistency before being merged.

Code review is the primary mechanism for maintaining engineering quality
and spreading knowledge across the team.

# Inputs

- A pull request or patch with proposed changes.
- Related documentation and specifications.
- Reference to any related issues or tickets.

# Prerequisites

Before requesting a review, the author should verify:

- [ ] Code compiles and builds without errors.
- [ ] All existing tests pass.
- [ ] New tests cover the change.
- [ ] Linting and style checks pass.
- [ ] Documentation is updated if needed.
- [ ] The change has a clear, descriptive title and description.

# Workflow

## Step 1: Prepare the Review

The reviewer begins by understanding the context of the change.

- Read the pull request title and description.
- Read linked issues or tickets.
- Understand what problem the change solves.
- Identify the scope of the change.

## Step 2: Review the Design

Before examining implementation details, evaluate the design.

| Question | Why It Matters |
| --- | --- |
|--------------------------------------------------------------+----------------------------------------|
| Does the approach solve the right problem? | Avoids wasted effort on wrong solution |
| --- | --- |
| Is the design consistent with the system architecture? | Prevents architectural drift |
| Does the change follow separation of concerns? | Ensures maintainability |
| Are the interfaces clear and well-defined? | Supports future change |
| Are there simpler alternatives? | Defends against over-engineering |
| Does the change introduce unnecessary dependencies? | Controls coupling |

If design issues are found, address them before proceeding to the
implementation review. Design issues are the most expensive to fix
later.

## Step 3: Review the Implementation

Examine the implementation for correctness and quality.

### Correctness

- Does the code do what it intends?
- Are edge cases handled?
- Are error conditions handled properly?
- Is there any race condition or thread safety issue?
- Are security concerns addressed (input validation, authentication,
  authorization, data exposure)?

#### Maintainability

- Is the code readable and well-structured?
- Are names descriptive and clear?
- Are functions and methods appropriately sized?
- Is there unnecessary duplication?
- Are comments meaningful (explaining why, not what)?
- Are complex sections documented?

#### Testing

- Are new features covered by tests?
- Are bug fixes accompanied by regression tests?
- Do tests follow the testing strategy (unit, integration, e2e)?
- Are tests readable and maintainable?
- Are edge cases and error paths tested?

## Step 4: Provide Feedback

Write clear, constructive review comments.

### Good Feedback

- ***Specific***: Reference specific lines or functions.
- ***Actionable***: Suggest what to improve, not just what is wrong.
- ***Explanatory***: Explain why the change is needed.
- ***Tone***: Assume good intent. Focus on the code, not the author.

Good:

#+BEGIN_QUOTE
This method handles both validation and persistence. Consider splitting
it into two methods to follow single responsibility. The validation
logic could go into a separate validator class that this method calls.
#+END_QUOTE

Avoid:

#+BEGIN_QUOTE
This is wrong. Fix it.
#+END_QUOTE

#### Prioritization

Use labels to indicate severity:

| Label | Meaning |
| --- | --- |
|-------------+----------------------------------------------------------|
| BLOCKER | Must be fixed before merge. Design flaw, correctness |
| --- | --- |
|  | issue, security vulnerability. |
| SHOULD FIX | Important but not blocking. Could be addressed in a |
|  | follow-up. |
| NICE TO HAVE | Suggestion for improvement. Can be deferred. |
| QUESTION | Clarification needed. Not necessarily a change request. |

## Step 5: Author Responds

The author should:

- Address every comment.
- Fix blocker and should-fix issues.
- Explain why nice-to-have suggestions are or are not addressed.
- Request re-review after addressing feedback.

## Step 6: Approval and Merge

The change is ready to merge when:

- All blocker comments are resolved.
- Should-fix comments are resolved or explicitly deferred.
- The reviewer has approved the change.
- CI checks pass.

# Checklist

The reviewer should verify:

- [ ] Change solves the stated problem.
- [ ] Design is appropriate for the system.
- [ ] Code is correct and handles edge cases.
- [ ] Errors are handled appropriately.
- [ ] Tests cover the change.
- [ ] No security concerns introduced.
- [ ] No unnecessary complexity introduced.
- [ ] No duplication of existing code.
- [ ] Documentation is updated.
- [ ] Naming is clear and descriptive.

# Escalation Points

| Situation | Action |
| --- | --- |
|---------------------------------------------+-------------------------------------|
| Reviewer and author disagree on approach | Escalate to a senior engineer or |
| --- | --- |
|  | tech lead for third-party review. |
| Change is large and difficult to review | Request the author split into |
|  | smaller, incremental changes. |
| Security concern identified | Involve security engineer in review. |
| Performance concern identified | Request performance review or |
|  | benchmark results. |

# AI Workflow

AI assistants can participate in code review by:

## Automated Analysis

- Detecting code smells and anti-patterns.
- Identifying missing error handling.
- Checking for test coverage gaps.
- Verifying style guideline compliance.

### Review Assistance

- Summarizing large diffs for human reviewers.
- Suggesting alternative implementations.
- Identifying duplicated code.
- Generating review comments for common issues.

### Limitations

- AI cannot evaluate design intent or business context.
- AI-generated review comments must be reviewed by a human.
- AI may produce false positives.
- AI cannot assess team or organizational conventions.

When using AI for code review, provide:

- The full diff or pull request.
- Context about the system and the change.
- Specific areas of concern (security, performance, design).
- Project coding standards and conventions.

# Expected Outputs

- Approved pull request or change with actionable review feedback.
- Knowledge shared between author and reviewer.
- Improved code quality through identified issues.
- Documented decisions for future reference.

# Related Documents

- [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)
- [Testing Strategies Guide](../../guides/engineering/testing-strategies/)
- [Code Organization Guide](../../guides/engineering/code-organization/)
- [Error Handling Guide](../../guides/engineering/error-handling/)
- [Engineering Glossary](../../glossary/engineering/README/)
