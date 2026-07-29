---
title: "Policy Object Template"
description: "Policy objects encapsulate authorization logic."
type: template
capability: rails
status: published
tags: [policy, object]
last_reviewed: 2026-07-28
---

# Purpose

Policy objects encapsulate authorization logic.

Use this template when you need to verify that a user is authorized to
perform an action on a resource.

# Template

```ruby
# app/policies/POLICY_NAME.rb
class POLICY_NAME
  def initialize(user, record)
    @user = user
    @record = record
  end

  def index?
    true
  end

  def show?
    scope.exists?(id: record.id)
  end

  def create?
    user.present?
  end

  def update?
    user.admin? || record.owner `= user
  end

  def destroy?
    user.admin? || record.owner =` user
  end

  def scope
    Pundit.policy_scope!(user, record.class)
  end

  private

  attr_reader :user, :record
end
```

# Usage

```ruby
# In a controller
def update
  authorize @record
  # ...
end

# In a view or service
policy = POLICY_NAME.new(current_user, record)
if policy.update?
  # Allow operation
end
```

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
