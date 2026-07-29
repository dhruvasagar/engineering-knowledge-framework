---
title: "Rails Learning Paths"
description: "These learning paths provide a structured progression through Rails development, from building basic applications to designing complex Rails systems."
type: learning-path
capability: rails
status: published
last_reviewed: 2026-07-28
---

# Purpose

These learning paths provide a structured progression through Rails
development, from building basic applications to designing complex
Rails systems.

Each path builds on the [Engineering Fundamentals Learning Paths](../../learning-paths/engineering/README.md) and
[Architecture Learning Paths](../../learning-paths/architecture/README.md).

# Beginner Path

## Objective

Build and deploy a basic Rails application following Rails conventions.

## Prerequisites

- Familiarity with Ruby syntax and object-oriented programming.
- Basic understanding of web applications (HTTP, HTML, CSS, databases).

## Topics

1. ***Rails Philosophy***
   - Convention over configuration.
   - MVC architecture in Rails.
   - Reference: [Rails Engineering Handbook](../../handbooks/rails/README.md)

2. ***Application Structure***
   - Rails directory structure.
   - Models, views, controllers and routes.
   - Exercise: Generate a scaffold and explore the generated code.

3. ***Models and Migrations***
   - ActiveRecord basics.
   - Writing migrations.
   - Validations and associations.
   - Exercise: Build a data model with associated tables.
   - Reference: [Rails Engineering Handbook](../../handbooks/rails/README.md)

4. ***Controllers and Routes***
   - Resourceful routes.
   - Controller actions and parameters.
   - Strong parameters.
   - Exercise: Build CRUD endpoints for a resource.

5. ***Views and Layouts***
   - ERB templates and layouts.
   - Partials and helpers.
   - Exercise: Build a user-facing page with forms.

6. ***Basic Testing***
   - Model and request specs.
   - Factory setup.
   - Exercise: Write tests for a CRUD feature.
   - Reference: [Testing Rails Applications Guide](../../guides/rails/testing.md)

## Suggested Projects

- Build a simple blog with posts, comments and users.
- Build a task management application with CRUD operations.

## Assessment

Demonstrate by: Building and deploying a Rails application with models,
controllers, views and tests following Rails conventions.

# Intermediate Path

## Objective

Design well-structured Rails applications with service objects, proper
testing and clean architecture.

## Prerequisites

- Completed Beginner Path or equivalent experience.
- Comfortable with Rails MVC and basic testing.

## Topics

1. ***Service Objects***
   - When and how to extract service objects.
   - Result objects and error handling.
   - Exercise: Refactor a fat controller into service objects.
   - Reference: [Service Objects Guide](../../guides/rails/service-objects.md)

2. ***Advanced Testing***
   - Request specs for API testing.
   - System specs for critical journeys.
   - Testing service objects in isolation.
   - Exercise: Build a comprehensive test suite for a feature.
   - Reference: [Testing Rails Applications Guide](../../guides/rails/testing.md)

3. ***API Development***
   - Building JSON APIs with Rails.
   - Versioning and serialization.
   - Exercise: Build an API-only Rails application.
   - Reference: [Rails Engineering Handbook](../../handbooks/rails/README.md)

4. ***Performance Basics***
   - N+1 query detection and prevention.
   - Caching strategies.
   - Background jobs with Sidekiq.
   - Exercise: Identify and fix N+1 queries in an application.

5. ***Authentication and Authorization***
   - Implementing authentication.
   - Role-based authorization.
   - Exercise: Add authentication and authorization to an application.

## Suggested Projects

- Build an API-only Rails application with versioned endpoints.
- Refactor an existing Rails application to use service objects.
- Add background job processing to an application.

## Assessment

Demonstrate by: Building a well-tested Rails application with service
objects, proper API design and background job processing.

# Advanced Path

## Objective

Lead Rails engineering decisions, design complex systems and establish
Rails standards for a team or organization.

## Prerequisites

- Completed Intermediate Path or equivalent experience.
- Experience building and maintaining production Rails applications.

## Topics

1. ***Rails Architecture Patterns***
   - Hexagonal architecture in Rails.
   - Event-driven patterns with Rails.
   - Exercise: Design a Rails system using hexagonal architecture.
   - Reference: [Architectural Patterns Guide](../../guides/architecture/architectural-patterns.md)

2. ***Upgrade Strategy***
   - Managing Rails version upgrades.
   - Deprecation management.
   - Exercise: Plan and execute a Rails version upgrade.
   - Reference: [Rails Upgrade Playbook](../../playbooks/rails/upgrade.md)

3. ***Gem Strategy***
   - Evaluating and selecting gems.
   - When to build vs buy.
   - Maintaining custom gems.
   - Reference: [Rails Engineering Handbook](../../handbooks/rails/README.md)

4. ***Rails at Scale***
   - Database scaling strategies.
   - Sharding and read replicas.
   - Multi-tenant architectures.
   - Exercise: Design a scaling strategy for a growing Rails
     application.

5. ***Establishing Rails Standards***
   - Defining conventions for a team.
   - Code review standards.
   - Exercise: Draft a Rails style guide for your team.

## Suggested Projects

- Lead a Rails version upgrade from planning through deployment.
- Design and implement a multi-tenant Rails application.
- Establish Rails coding standards for a team.

## Assessment

Demonstrate by: Leading Rails architecture decisions, conducting
effective code reviews, establishing Rails standards and mentoring
other Rails developers.

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README.md)
- [Rails Glossary](../../glossary/rails/README.md)
- [Service Objects Guide](../../guides/rails/service-objects.md)
- [Testing Rails Applications Guide](../../guides/rails/testing.md)
- [Rails Upgrade Playbook](../../playbooks/rails/upgrade.md)
- [Rails References](../../references/rails/README.md)
- [Engineering Learning Paths](../../learning-paths/engineering/README.md)
- [Architecture Learning Paths](../../learning-paths/architecture/README.md)
