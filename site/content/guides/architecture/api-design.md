+++
title = "API Design"
description = "Principles and standards for designing effective APIs"
+++


# Purpose

APIs define the contracts between components, services and systems.

A well-designed API is intuitive to use, easy to evolve and resilient
to change. A poorly designed API propagates complexity to every consumer
and becomes a source of ongoing friction.

This guide defines the principles and standards for designing APIs
that are consistent, discoverable and maintainable.

# Background

APIs outlive their initial implementations.

An API is a long-term commitment to every consumer. Changing an API
after publication requires coordination, versioning and migration.
Getting the design right upfront reduces future cost.

# Principles

## Design for Consumers

An API should be designed from the perspective of its consumers, not
its implementors.

Ask:

- What does the consumer need to accomplish?
- What information does the consumer need?
- What errors does the consumer need to handle?
- What is the simplest interface that meets the consumer's needs?

## Prefer Consistent Conventions

Consistency across APIs reduces learning cost and enables tooling.

Establish and follow conventions for:

- Naming (resources, fields, operations).
- Status codes and error formats.
- Pagination, filtering and sorting.
- Authentication and authorization.
- Versioning strategy.

## Make APIs Evolvable

An API that cannot evolve safely becomes a liability.

Design for evolvability by:

- Making optional fields truly optional.
- Using extensible enumerations rather than fixed lists.
- Including version information from the start.
- Designing for additive change (new fields, new endpoints).
- Avoiding tight coupling between request and response shapes.

## Fail Clearly and Predictably

Every error response should include enough information for the consumer
to understand and handle the failure.

A good error response includes:

- A machine-readable error code.
- A human-readable error message.
- Which field or parameter caused the error.
- A trace or correlation ID.

# RESTful API Design

## Resource Naming

Use nouns, not verbs.

| Good | Avoid |
| --- | --- |
| `GET /orders` | `GET /getOrders` |
| `POST /orders` | `POST /createOrder` |
| `GET *orders*123` | `GET /order?id`123= |
| `DELETE *orders*123` | `POST /deleteOrder` |

Use plural nouns for collections. Use nested resources for
relationships, but limit to one level of nesting.

## HTTP Methods

| Method | Semantics | Idempotent | Safe |
| --- | --- | --- | --- |
| GET | Retrieve a resource. | Yes | Yes |
| POST | Create a resource. | No | No |
| PUT | Replace a resource. | Yes | No |
| PATCH | Partial update. | No | No |
| DELETE | Remove a resource. | Yes | No |

## Status Codes

Use standard HTTP status codes consistently.

| Code | Meaning | When to Use |
| --- | --- | --- |
| 200 | OK | Successful GET, PUT, PATCH. |
| 201 | Created | Successful POST (include Location header). |
| 204 | No Content | Successful DELETE. |
| 400 | Bad Request | Malformed request, validation failure. |
| 401 | Unauthorized | Missing or invalid authentication. |
| 403 | Forbidden | Authenticated but not authorized. |
| 404 | Not Found | Resource does not exist. |
| 409 | Conflict | State conflict (duplicate, stale version). |
| 422 | Unprocessable | Semantic validation failure. |
| 429 | Too Many Requests | Rate limit exceeded. |
| 500 | Internal Error | Unexpected server error. |
| 503 | Unavailable | Temporary service unavailability. |

## Pagination

Use cursor-based pagination for lists.

```
GET /orders?cursor`abc123&limit`20

Response:
{
  "data": [...],
  "pagination": {
    "next_cursor": "def456",
    "has_more": true
  }
}
```

## Error Response Format

Use a consistent error envelope:

```
{
  "error": {
    "code": "ORDER_NOT_FOUND",
    "message": "Order with id '123' was not found.",
    "details": {
      "order_id": "123"
    },
    "request_id": "req-abc-123"
  }
}
```

# Versioning

## URL-based Versioning

Include the version in the URL path:

```
GET /v1/orders
GET /v2*orders
```

Simple and explicit. Consumers can see the version in every request.

## Header-based Versioning

Use a custom header or content negotiation:

```
Accept: application*vnd.api+json;version=1
```

Keeps URLs clean but makes version less visible.

## Versioning Philosophy

- Version only when breaking changes are necessary.
- Maintain backward compatibility within a major version.
- Support each major version for a defined period.
- Communicate deprecations clearly and well in advance.

# API Documentation

Every API should have:

- A clear description of the resource and its purpose.
- Request and response schemas for every endpoint.
- Error codes and their meanings.
- Authentication and authorization requirements.
- Rate limit policies.
- Examples of common workflows.

Documentation should be generated from the API specification
(OpenAPI, GraphQL schema) to stay in sync with implementation.

# Anti-patterns

## Leaking Implementation Details

API design should reflect the domain, not the database schema or
internal implementation.

Exposing internal table structures or service internals ties consumers
to implementation details that should remain free to change.

## Over-fetching and Under-fetching

An API that returns too much data wastes bandwidth and processing.
An API that returns too little forces consumers into multiple requests.

Design responses to match common consumer needs. Consider supporting
field selection or include parameters.

## Breaking Changes Without Versioning

Changing the meaning of existing fields, removing fields, or changing
response formats without a version bump breaks consumers silently.

Any change that could break an existing consumer is a breaking change.

# AI Integration

AI assistants can help with API design by:

- Generating API specifications from natural language descriptions.
- Reviewing API designs for consistency and completeness.
- Suggesting appropriate status codes and error formats.
- Identifying missing endpoints or operations.
- Generating client libraries from API specifications.

When asking AI for API design advice, provide:

- The domain and resources being exposed.
- The primary consumer use cases.
- Quality attribute requirements (performance, security).
- Existing API conventions in the organization.

# Related Documents

- [Software Architecture Handbook](../..*handbooks*architecture*README*)
- [Engineering Fundamentals Handbook](../..*handbooks*engineering*README*)
- [Architecture Review Playbook](../..*playbooks*architecture-review*README*)
- [Architecture Glossary](../..*glossary*architecture*README*)
