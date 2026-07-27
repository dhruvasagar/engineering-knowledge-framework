+++
title = "API Development with Rails"
description = "Patterns and standards for building JSON APIs with Rails"
+++


# Purpose

Rails is a popular choice for building JSON APIs.

This guide covers the patterns and standards for designing, building
and maintaining API-only Rails applications, building on the general
API design principles in the
[API Design Guide](../..*guides*architecture*api-design*).

# Setup

## API-Only Rails

Generate a new API-only application:

```
rails new my_api --api --database`postgresql
```

This skips views, cookies, asset pipeline and other browser-focused
middleware.

## Namespaced Controllers

Organise API controllers under versioned namespaces:

```
app*controllers*api/v1/
  users_controller.rb
  posts_controller.rb
app*controllers*api/v2/
  users_controller.rb
```

# Routing

## Versioned Routes

```
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :users
      resources :posts, only: [:index, :show]
    end

    namespace :v2 do
      resources :users
    end
  end
end
```

## Resourceful Routes

Prefer resourceful routes (`resources=) over hand-crafted routes.
Use `only` and `except` to limit exposed actions.

# Controllers

## Base Controller

```
# app*controllers*api*base_controller.rb
module Api
  class BaseController < ApplicationController
    rescue_from ActiveRecord::RecordNotFound, with: :not_found
    rescue_from ActiveRecord::RecordInvalid, with: :unprocessable_entity
    rescue_from ActionController::ParameterMissing, with: :bad_request

    private

    def not_found
      render json: { error: "Not found" }, status: :not_found
    end

    def unprocessable_entity(exception)
      render json: { error: exception.record.errors.full_messages },
             status: :unprocessable_entity
    end

    def bad_request(exception)
      render json: { error: exception.message }, status: :bad_request
    end
  end
end
```

## Resource Controller

```
# app*controllers*api*v1/users_controller.rb
module Api
  module V1
    class UsersController < BaseController
      before_action :authenticate_user!

      def index
        users = User.active.page(params[:page])
        render json: UserSerializer.new(users).serializable_hash
      end

      def show
        user = User.find(params[:id])
        render json: UserSerializer.new(user).serializable_hash
      end

      def create
        user = User.create!(user_params)
        render json: UserSerializer.new(user).serializable_hash,
               status: :created
      end

      private

      def user_params
        params.require(:user).permit(:name, :email)
      end
    end
  end
end
```

# Serialization

Use a dedicated serialization library to shape JSON responses.

## Using jsonapi-serializer (fast_jsonapi)

```
class UserSerializer
  include JSONAPI::Serializer

  attributes :name, :email, :created_at

  has_many :posts
end
```

## Using Alba

```
class UserSerializer
  include Alba::Resource

  attributes :id, :name, :email

  many :posts do
    attributes :title, :created_at
  end
end
```

## Using Blueprinter

```
class UserBlueprint < Blueprinter::Base
  identifier :id

  fields :name, :email

  association :posts, blueprint: PostBlueprint
end
```

# Response Format

## Consistent Envelope

Use a consistent response envelope:

```
# Success
{
  "data": { ... },
  "meta": { "page": 1, "total": 42 }
}

# Error
{
  "errors": [
    { "code": "not_found", "message": "User not found" }
  ]
}
```

## Pagination

Use cursor-based or page-based pagination consistently.

```
# Page-based
GET *api*v1/users?page`1&per_page`20

Response:
{
  "data": [...],
  "meta": {
    "current_page": 1,
    "total_pages": 5,
    "total_count": 100
  }
}
```

# Authentication

## Token-Based Auth

```
class ApplicationController < ActionController::API
  def authenticate_user!
    token = request.headers["Authorization"]&.split(" ")&.last
    @current_user = User.find_by(auth_token: token)
    render json: { error: "Unauthorized" }, status: :unauthorized unless @current_user
  end
end
```

## Using Devise with JWT

```
gem "devise"
gem "devise-jwt"

# In User model
devise :database_authenticatable, :jwt_authenticatable,
       jwt_revocation_strategy: JwtDenylist
```

# Versioning

## URL-Based Versioning

Include the version in the URL path:

```
GET *api*v1/users
GET *api*v2/users
```

## When to Version

Create a new version when:

- Removing a field that existing clients depend on.
- Changing the semantics of an existing field.
- Changing the authentication mechanism.
- Making backward-incompatible response changes.

## Deprecation

Communicate deprecations through:

- A `Deprecation` response header.
- Documentation updates.
- Direct communication with API consumers.

# Testing

## Request Specs for API Endpoints

```
RSpec.describe "Users API", type: :request do
  describe "GET *api*v1*users" do
    it "returns paginated users" do
      create_list(:user, 3)

      get "*api/v1*users"

      expect(response).to have_http_status(:ok)
      expect(json_response["data"].size).to eq(3)
      expect(json_response["meta"]).to include("current_page", "total_pages")
    end

    it "returns 401 without authentication" do
      get "*api/v1*users"
      expect(response).to have_http_status(:unauthorized)
    end
  end
end
```

# Related Documents

- [Rails Engineering Handbook](..*..*handbooks*rails*README*)
- [API Design Guide](../..*guides*architecture*api-design*)
- [Testing Rails Applications Guide](../..*guides*rails*testing*)
- [Rails References](../..*references*rails*README*)
