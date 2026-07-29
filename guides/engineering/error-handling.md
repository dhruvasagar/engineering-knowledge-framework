---
title: "Error Handling"
description: "Errors are an inevitable part of software operation."
type: guide
capability: engineering
status: published
tags: [error, handling]
last_reviewed: 2026-07-28
---

# Purpose

Errors are an inevitable part of software operation.

How a system handles errors determines its reliability, debuggability
and operational maturity. Good error handling transforms failures into
recoverable events. Poor error handling turns minor issues into
production incidents.

This guide defines the principles and patterns for handling errors in a
way that is consistent, predictable and maintainable.

# Background

Error handling is often treated as an afterthought — added reactively
after a production failure reveals a gap.

Proactive error handling treats errors as a design concern from the
start. Every function, service and system boundary should define:

- What can go wrong?
- How will it be detected?
- How will it be communicated?
- How will it be recovered?

# Principles

## Distinguish Recoverable from Unrecoverable Errors

Errors fall into two categories:

| Category      | Definition                         | Examples                  |
|---------------|------------------------------------|---------------------------|
| Recoverable   | The system can continue operating  | Validation failure,       |
|               | despite the error.                 | network timeout,          |
|               |                                    | resource not found        |
| Unrecoverable | The system cannot safely continue. | Null pointer dereference, |
|               | Fail fast and report.              | out of memory,            |
|               |                                    | configuration error       |

Recoverable errors should be handled gracefully.

Unrecoverable errors should be surfaced immediately with full context.

## Never Silently Swallow Errors

An error that is caught and discarded is worse than an error that
propagates.

Silently swallowed errors:

- Hide production issues.
- Create mysteries that take days to debug.
- Corrupt data silently.
- Undermine operational visibility.

If an error cannot be handled meaningfully at the current level, let it
propagate to a level that can handle it.

## Handle Errors at the Appropriate Level

Errors should be handled at the level of abstraction that has enough
context to make a decision about recovery.

A low-level database driver should not decide how to handle a
constraint violation. It should raise the error and let the business
logic layer decide.

## Provide Context with Every Error

Errors should include enough information to diagnose the problem
without requiring reproduction.

Good error messages include:

- What went wrong.
- What was being attempted.
- Relevant identifiers (user ID, request ID, record ID).
- The state of the operation when the error occurred.

***Good:***

```text
UserRegistrationFailed: Could not register user
  (email=john@example.com). Reason: Email already taken.
  Request ID: req-abc-123
```

***Avoid:***

```text
Error: Validation failed
```

## Fail Fast

Detect and report errors as early as possible.

Validating inputs at the boundary prevents corrupted state from
propagating deeper into the system. Validating preconditions before
execution prevents wasted work.

# Patterns

## Return Types vs Exceptions

Choose the error mechanism that matches the context:

| Mechanism    | Use When                                                |
|--------------|---------------------------------------------------------|
| Return types | The error is expected and callers should handle it      |
|              | (e.g., validation, not found).                          |
| Exceptions   | The error is unexpected or cannot be handled at the     |
|              | call site (e.g., network failure, configuration error). |
| Result types | You want type-safe error handling without exceptions    |
|              | (e.g., `Result[T, E]`, `Either`, `Ok`).                 |

Prefer return types or result types for expected errors. Reserve
exceptions for exceptional conditions.

## Error Boundaries

Define explicit boundaries where errors are caught, logged, and
transformed.

Common boundaries include:

- HTTP controller: catch application errors, return appropriate status
  codes.
- Service boundary: catch infrastructure errors, convert to domain
  errors.
- Background job: catch errors, implement retry logic with backoff.
- System boundary: catch unexpected errors, log with full context,
  crash gracefully.

## Retry with Backoff

Transient errors (network timeouts, database deadlocks) should be
retried with exponential backoff.

Retry guidelines:

- Define a maximum retry count.
- Use exponential backoff with jitter.
- Log each retry attempt.
- Escalate to an alert after exhausting retries.

## Circuit Breaker

For errors that indicate a downstream system is unavailable, use a
circuit breaker to fail fast rather than wasting resources on repeated
failed calls.

The circuit breaker trips after a threshold of failures, then allows
periodic test requests to determine if the downstream system has
recovered.

# Logging

## Log Levels

| Level | Use When                                                  |
|-------|-----------------------------------------------------------|
| ERROR | A failure that requires human investigation.              |
| WARN  | An unexpected condition that the system handled.          |
| INFO  | Significant lifecycle events (startup, shutdown, deploy). |
| DEBUG | Detailed information for diagnosing issues.               |
| TRACE | Very detailed diagnostic information.                     |

## Structured Logging

Always use structured logging (JSON or key-value format) rather than
free-text messages.

Good:

```json
{"event": "user_registration_failed",
 "user_id": "abc-123",
 "reason": "email_taken",
 "duration_ms": 45,
 "request_id": "req-xyz-789"}
```

Structured logs are searchable, filterable and machine-parseable.

# Anti-patterns

## Catching and Ignoring

```text
try:
    risky_operation()
except Exception:
    pass  # Never do this.
```

If you must catch an exception you cannot handle, log it with context
before continuing.

## Catching Too Broadly

Catching `Exception` or `RuntimeError` hides unexpected bugs that
should not be recovered from.

Catch specific exception types whenever possible.

## Error Codes Without Context

Returning a numeric error code without explanation forces engineers to
cross-reference documentation to understand the failure.

Use descriptive error messages and structured data instead.

# AI Integration

AI assistants can help with error handling by:

- Suggesting appropriate error types for new code.
- Identifying gaps in error handling coverage.
- Recommending retry and backoff configurations.
- Generating structured logging statements.
- Reviewing error messages for clarity and completeness.

When asking AI for error handling advice, provide:

- The operation being performed.
- Expected failure modes.
- System context (web service, background job, batch process).
- Existing error handling conventions.

# Related Documents

- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Software Architecture Handbook](../../handbooks/architecture/README.md)
- [Engineering Glossary](../../glossary/engineering/README.md)
- [Code Review Playbook](../../playbooks/code-review/README.md)
