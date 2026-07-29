---
title: "Authentication and Authorization"
description: "Authentication verifies who a user is."
type: guide
capability: rails
status: published
tags: [authentication, authorization]
last_reviewed: 2026-07-28
---

# Purpose

Authentication verifies who a user is. Authorization determines what a
user can do.

This guide covers the patterns and tools for implementing both
effectively in Rails applications.

# Authentication with Devise

Devise is the most widely used authentication framework for Rails.

## Setup

```ruby
gem "devise"

rails generate devise:install
rails generate devise User
rails db:migrate
```

## Configuration

```ruby
# config/initializers/devise.rb
Devise.setup do |config|
  config.mailer_sender = "please-change-me@config.com"
  config.reset_password_within = 6.hours
  config.sign_out_via = :delete
  config.case_insensitive_keys = [:email]
  config.strip_whitespace_keys = [:email]
end
```

## Strong Parameters

Permit additional fields in the application controller:

```ruby
class ApplicationController < ActionController::Base
  before_action :configure_permitted_parameters, if: :devise_controller?

  protected

  def configure_permitted_parameters
    devise_parameter_sanitizer.permit(:sign_up, keys: [:name])
    devise_parameter_sanitizer.permit(:account_update, keys: [:name])
  end
end
```

# Authorization with Pundit

Pundit provides a simple, object-oriented authorization system.

## Setup

```ruby
gem "pundit"

include Pundit::Authorization in ApplicationController
```

## Policies

Generate policies for each resource:

```bash
rails generate pundit:install
rails generate pundit:policy post
```

```ruby
# app/policies/post_policy.rb
class PostPolicy < ApplicationPolicy
  def index?
    true
  end

  def show?
    scope.where(id: record.id).exists?
  end

  def create?
    user.present?
  end

  def update?
    user.admin? || record.author `= user
  end

  def destroy?
    user.admin? || record.author =` user
  end
end
```

## Usage

```ruby
class PostsController < ApplicationController
  def show
    @post = Post.find(params[:id])
    authorize @post
  end

  def create
    @post = Post.new(post_params)
    authorize @post
    @post.save!
  end
end
```

## Scopes

Use policy scopes to scope queries:

```ruby
class PostPolicy < ApplicationPolicy
  class Scope < Scope
    def resolve
      if user.admin?
        scope.all
      else
        scope.where(author: user)
      end
    end
  end
end

# In controller
def index
  @posts = policy_scope(Post)
end
```

# Common Patterns

## Current User

```ruby
class ApplicationController < ActionController::Base
  private

  def current_user
    @current_user ||= User.find_by(id: session[:user_id])
  end

  def authenticate_user!
    redirect_to login_path unless current_user
  end
end
```

## Roles

Use enums or a role model for role-based authorization:

```ruby
class User < ApplicationRecord
  enum :role, { member: 0, admin: 1, super_admin: 2 }

  def admin?
    role `= "admin" || role =` "super_admin"
  end

  def super_admin?
    role `= "super_admin"
  end
end
```

## Authorization in Views

```erb
<% if policy(@post).update? %>
  <%` link_to "Edit", edit_post_path(@post) %>
<% end %>
```

# Anti-patterns

## skip_before_action :authenticate_user!

Using `skip_before_action` to bypass authentication on individual
controllers is a code smell. Prefer explicit `before_action` on the
controllers that need authentication.

## Authorization Only at the Controller Level

Authorize at the service or model level too, not just in controllers.
If a background job or Rake task bypasses the controller, it should
still enforce authorization.

## Overly Permissive Policies

A policy that always returns `true` provides no protection. Every
action should have an explicit authorization check.

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README.md)
- [Policy Object Template](../../templates/rails/policy-object.md)
- [API Development with Rails](../../guides/rails/api-development.md)
- [Rails Pull Request Checklist](../../checklists/rails/pull-request.md)
