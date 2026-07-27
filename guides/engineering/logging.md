+++
title = "Logging"
description = "Principles and standards for effective application logging"
+++


# Purpose

Logging is the practice of recording events, state changes and errors
during software execution to support operations, debugging and analysis.

Well-structured logs are the primary tool for understanding production
behaviour, diagnosing incidents and monitoring system health.

This guide defines the principles and standards for logging across all
services and applications.

# Background

Logs serve three primary audiences:

| Audience | Need |
| --- | --- |
|---------------+---------------------------------------------------------|
| Operators | Real-time visibility into system health and incidents. |
| --- | --- |
| Engineers | Historical record for debugging and post-mortem analysis. |
| Systems | Machine consumption for monitoring, alerting and analytics. |

Each audience benefits from logs that are structured, consistent and
context-rich.

# Principles

## Log in Structured Format

Always use a structured, machine-parseable format (JSON, key-value).

Structured logs are searchable, filterable and consumable by log
aggregation systems.

***Good (JSON):***

```
{"timestamp": "2026-07-27T10:00:00Z", "level": "ERROR",
 "service": "order-service", "request_id": "req-abc-123",
 "message": "Payment processing failed",
 "error": "payment_declined", "duration_ms": 452}
```

***Avoid (free-text):***

```
[2026-07-27 10:00:00] ERROR: Payment failed after 452ms
```

## Log at the Appropriate Level

| Level | Use When |
| --- | --- |
|---------+-----------------------------------------------------------|
| ERROR | A failure that requires human investigation. The system |
| --- | --- |
|  | cannot complete the requested operation. |
| WARN | An unexpected condition that the system handled |
|  | gracefully. Does not require immediate action but may |
|  | indicate a future problem. |
| INFO | Significant lifecycle events: service startup, shutdown, |
|  | configuration load, successful deployment, state |
|  | transitions. |
| DEBUG | Detailed information for diagnosing issues during |
|  | development or incident investigation. Should be disabled |
|  | in production under normal operation. |
| TRACE | Very detailed diagnostic information. Typically used only |
|  | for tracing specific requests through the system. |

## Include Context with Every Log Event***

Every log event should include enough context to understand what
happened without requiring additional investigation.

Essential context fields:

- `timestamp`: ISO 8601 with timezone.
- `service`: Service or application name.
- `request_id`: Correlation ID for the request or operation.
- `trace_id`: Distributed tracing ID.
- `message`: Human-readable description of the event.
- `level`: Log level.

Additional context for relevant events:

- `user_id`, `customer_id`: Affected entity.
- `resource_id`: Affected resource.
- `error`, `error_code`: Machine-readable error identifier.
- `duration_ms`: Operation duration.
- `attempt`: Retry attempt number.

## Never Log Sensitive Information***

Sensitive data must never appear in logs.

This includes:

- Passwords, tokens, secrets and API keys.
- Personal identifiable information (PII).
- Payment card information.
- Health or protected data.
- Session tokens or authentication cookies.

Logs are a common target for attackers. Treat log content as a security
concern.

If sensitive data must be logged for debugging, ensure it is:

- Redacted or masked (e.g., `email: j***@example.com`).
- Logged at DEBUG level only.
- Excluded from production log aggregation.

# Standards

## Log Event Structure

Every log event should include these standard fields:

```
{
  "timestamp":   "2026-07-27T10:00:00.123Z",
  "level":       "INFO",
  "service":     "order-service",
  "environment": "production",
  "request_id":  "req-abc-123",
  "trace_id":    "trace-xyz-789",
  "message":     "Order created successfully"
}
```

## Request Correlation

Every request should carry a unique `request_id` that is propagated
across service boundaries.

The `request_id` enables tracing a request through multiple services
and log sources.

## Error Logging

When logging errors:

- Log the error when it occurs, not just when it is caught.
- Include the error type and message.
- Include the stack trace for unexpected errors.
- Include the operation that was being attempted.
- Do not log the same error at multiple levels.

# Anti-patterns

## Logging in Loops

Logging inside a loop produces excessive volume and obscures meaningful
events.

Log after the loop completes, or log periodically with a summary.

## Logging Control Flow

Logging the entry and exit of every function produces noise.

Log at meaningful boundaries: service entry points, external calls,
state transitions and errors.

## Logging Without Context

A log message like `User not found` without identifying which user or
which operation is useless.

Always include relevant identifiers.

## Mixing Log Levels

Using INFO for errors or ERROR for warnings undermines the meaning of
log levels and makes filtering unreliable.

# AI Integration

AI assistants can help with logging by:

- Generating structured log statements for new code.
- Reviewing log statements for completeness and context.
- Identifying missing context fields.
- Detecting sensitive data in log statements.
- Suggesting appropriate log levels.

When asking AI for logging advice, provide:

- The operation being logged.
- The relevant context fields.
- The system's logging conventions and format.
- Any compliance requirements for log content.

# Related Documents

- [Engineering Fundamentals Handbook](../../handbooks/engineering/README/)
- [Error Handling Guide](../../guides/engineering/error-handling/)
- [Code Review Playbook](../../playbooks/code-review/README/)
