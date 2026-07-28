# Purpose

Code review is the most effective quality practice in software
engineering.

This guide defines the standards for conducting code reviews that catch
defects, spread knowledge and improve design.

# Review Expectations

## Velocity

- Reviews should begin within 4 business hours of request.
- Changes should be fully reviewed within 1 business day.
- Large changes (> 400 lines) should be split into smaller PRs.

## Workflow

1. Author submits pull request with description and context.
2. Reviewer is assigned or self-selects.
3. Reviewer performs the review within the expected timeframe.
4. Author responds to comments and makes changes.
5. Reviewer approves or requests further changes.
6. Change is merged.

# What to Review

## Design

| Question | Why It Matters |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Does the approach solve the right problem? | Avoids wasted effort. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Is the design consistent with the system architecture? | Prevents architectural drift. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Does the change follow separation of concerns? | Ensures maintainability. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Are the interfaces clear and well-defined? | Supports future change. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+

## Correctness

| Question | Why It Matters |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Does the code do what it intends? | Obvious but essential. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Are edge cases handled? | Prevents subtle bugs. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Are error conditions handled properly? | Ensures reliability. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Are security concerns addressed? | Prevents vulnerabilities. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+

## Maintainability

| Question | Why It Matters |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Is the code readable and well-structured? | Reduces future cognitive load. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Are names descriptive and clear? | Improves readability. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Is there unnecessary duplication? | Increases maintenance cost. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Are comments meaningful (why, not what)? | Preserves intent. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+

## Testing

| Question | Why It Matters |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Are new features covered by tests? | Prevents regression. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Are bug fixes accompanied by regression tests? | Ensures bugs stay fixed. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Are tests readable and maintainable? | Reduces test maintenance cost. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+
| Are edge cases and error paths tested? | Ensures robustness. |
| --- | --- |
+--------------------------------------------------------------+----------------------------------------+

# Review Quality

## Good Review Comments

- ***Specific***: Reference specific lines or functions.
- ***Actionable***: Suggest what to improve, not just what is wrong.
- ***Explanatory***: Explain why the change is needed.
- ***Respectful***: Assume good intent. Focus on the code.

Good:

```
This method handles both validation and persistence. Consider
splitting it to follow single responsibility — the validation logic
could go into a validator class.
```

Avoid:

```
This is wrong. Fix it.
```

## Severity Labels

| Label | Meaning |
| --- | --- |
+-------------+----------------------------------------------------------+
| BLOCKER | Must be fixed before merge. Design flaw, correctness |
| --- | --- |
|  | issue, security vulnerability. |
+-------------+----------------------------------------------------------+
| SHOULD FIX | Important but not blocking. Can be addressed in a |
| --- | --- |
|  | follow-up. |
+-------------+----------------------------------------------------------+
| NICE TO HAVE | Suggestion for improvement. Can be deferred. |
| --- | --- |
+-------------+----------------------------------------------------------+
| QUESTION | Clarification needed. Not necessarily a change request. |
| --- | --- |
+-------------+----------------------------------------------------------+

# Related Documents

- [Engineering Quality Handbook](../../handbooks/quality/README.md)
- [Code Review Playbook](../../playbooks/code-review/README.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Rails Pull Request Checklist](../../checklists/rails/pull-request.md)
