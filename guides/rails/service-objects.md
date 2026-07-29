---
title: "Service Objects"
description: "Service objects encapsulate a single business operation into a dedicated class."
type: guide
capability: rails
status: published
tags: [service, objects]
last_reviewed: 2026-07-28
---

# Purpose

Service objects encapsulate a single business operation into a
dedicated class.

They are the primary pattern for extracting complex logic from
controllers and models, improving testability, reusability and
separation of concerns.

This guide explains when to use service objects, how to structure them
and common patterns.

# Background

In a typical Rails application, business logic starts in controllers
(for quick implementation) or models (as the natural home for domain
logic).

Both approaches become problematic as the application grows:

- Controllers become fat with orchestration logic.
- Models accumulate responsibilities beyond persistence.

Service objects provide a third home for business logic that belongs
between controllers and models.

# When to Use a Service Object

Use a service object when:

- The operation involves multiple models.
- The operation calls external services or APIs.
- The operation has complex error handling or retry logic.
- The operation is invoked from multiple entry points (controller,
  job, Rake task).
- The operation has side effects that should be tested in isolation.

Do not use a service object for:

- Simple CRUD operations that belong in the controller.
- Model-specific logic that belongs in the model.
- Operations that are already well-served by a Rails concern.

# Structure

## Convention

A service object is a plain Ruby class with a single public method,
conventionally named `call`.

```ruby
class InviteUser
  def initialize(team:, email:, inviter:)
    @team = team
    @email = email
    @inviter = inviter
  end

  def call
    # Business logic here
  end
end
```

## Return Value

Service objects should return a consistent result object.

Use a simple result object with success and failure states:

```ruby
class InviteUser
  Result = Struct.new(:success?, :user, :error)

  def call
    # ...
    Result.new(true, user, nil)
  rescue StandardError => e
    Result.new(false, nil, e)
  end
end
```

This enables callers to handle success and failure uniformly:

```ruby
result = InviteUser.new(team:, email:, inviter:).call

if result.success?
  # Handle success
else
  # Handle failure
end
```

## Naming

Name service objects after the operation they perform.

| Good               | Avoid            |
|--------------------|------------------|
| `RegisterUser`     | `UserService`    |
| `ProcessPayment`   | `PaymentHandler` |
| `SendWelcomeEmail` | `EmailManager`   |

The name should describe what the object does, not what it is.

# Patterns

## Basic Service Object

A simple, single-purpose operation.

```ruby
class ArchiveInactiveUsers
  def initialize(cutoff_date:)
    @cutoff_date = cutoff_date
  end

  def call
    User.where("last_active_at < ?", @cutoff_date)
        .where(archived: false)
        .find_each { |user| user.update!(archived: true) }
  end
end
```

## Service Object with External API

When the operation depends on an external service, inject the
dependency.

```ruby
class SendNotification
  def initialize(user:, message:, client: NotificationClient.new)
    @user = user
    @message = message
    @client = client
  end

  def call
    @client.send(user_id: @user.id, text: @message)
  end
end
```

Dependency injection makes testing easier — the API client can be
stubbed in tests.

## Service Object with Multiple Steps

When an operation has multiple steps, keep each step as a private
method and compose them in `call`.

```ruby
class CreateOrder
  def initialize(cart:, customer:)
    @cart = cart
    @customer = customer
  end

  def call
    validate_cart
    create_order
    process_payment
    send_confirmation
    order
  end

  private

  def validate_cart
    # ...
  end

  def create_order
    # ...
  end

  def process_payment
    # ...
  end

  def send_confirmation
    # ...
  end
end
```

# Testing

Service objects are easy to test because they are plain Ruby classes.

```ruby
RSpec.describe InviteUser do
  subject(:result) { described_class.new(team:, email:, inviter:).call }

  let(:team) { create(:team) }
  let(:email) { "user@example.com" }
  let(:inviter) { create(:user) }

  it "creates a membership" do
    expect { result }.to change(Membership, :count).by(1)
  end

  it "returns success" do
    expect(result.success?).to be true
  end

  context "when the email is already taken" do
    let!(:existing_user) { create(:user, email: email) }

    it "returns failure" do
      expect(result.success?).to be false
    end

    it "includes the error" do
      expect(result.error).to be_present
    end
  end
end
```

# Anti-patterns

## God Service Objects

A service object that does too many things.

If a service object has multiple public methods or handles unrelated
operations, split it into multiple service objects.

## Service Objects as Repositories

Do not use service objects to wrap simple database queries.

Use scopes or query objects for queries. Use service objects for
operations.

## Leaking Persistence Details

Service objects should not expose database implementation details to
callers. Return domain objects, not database records directly.

# AI Integration

AI assistants can help with service objects by:

- Generating service objects from operation descriptions.
- Identifying controller actions that should be extracted into service
  objects.
- Writing tests for existing service objects.
- Suggesting improvements to error handling and result objects.

When asking AI for service object help, provide:

- The operation description.
- The models involved.
- Error conditions to handle.
- Existing service object conventions in the project.

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [Rails Glossary](../../glossary/rails/README.md)
- [Code Review Playbook](../../playbooks/code-review/README.md)
- [Testing Strategies Guide](../../guides/engineering/testing-strategies.md)
