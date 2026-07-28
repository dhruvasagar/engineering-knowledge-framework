# Purpose

Testing is essential to maintaining a healthy Rails application.

Rails provides powerful testing tools, but their flexibility means
teams must establish clear conventions to keep tests fast, reliable
and maintainable.

This guide defines the testing strategy for Rails applications, building
on the general testing principles in the
[Testing Strategies Guide](../../guides/engineering/testing-strategies.md).

# Test Distribution

Follow the test pyramid for Rails applications:

```
        /\
       /  \
      / E2E\    Few: system specs, critical user journeys
     /------\
    / Request\  Some: controller behaviour, API responses
   /  specs   \
  /------------\
 / Model & Unit\ Many: models, services, forms, presenters
/    specs      \
-----------------
```

| Type | Speed | Purpose | Proportion |
| --- | --- | --- | --- |
|--------------+---------+--------------------------------------+------------|
| Model specs | Fast | Validations, associations, scopes. | 40% |
| --- | --- | --- | --- |
|--------------+---------+--------------------------------------+------------|
| Unit specs | Fast | Services, forms, presenters, | 30% |
| --- | --- | --- | --- |
|  |  | queries. |  |
|--------------+---------+--------------------------------------+------------|
| Request specs | Moderate | Controller behaviour, status codes, | 20% |
| --- | --- | --- | --- |
|  |  | response format, authentication. |  |
|--------------+---------+--------------------------------------+------------|
| System specs | Slow | Critical user journeys through the | 10% |
| --- | --- | --- | --- |
|  |  | full stack. |  |
|--------------+---------+--------------------------------------+------------|

# Model Specs

Test validations, associations, scopes and custom methods.

```
RSpec.describe User, type: :model do
  describe "validations" do
    it { is_expected.to validate_presence_of(:email) }
    it { is_expected.to validate_uniqueness_of(:email).case_insensitive }
  end

  describe "associations" do
    it { is_expected.to have_many(:posts).dependent(:destroy) }
  end

  describe "scopes" do
    describe ".active" do
      it "returns users active within the last 30 days" do
        active_user = create(:user, last_active_at: 1.day.ago)
        inactive_user = create(:user, last_active_at: 31.days.ago)

        expect(User.active).to contain_exactly(active_user)
      end
    end
  end
end
```

# Request Specs

Test controller behaviour at the HTTP level.

Request specs replace controller specs in modern Rails. They test the
entire request-response cycle without rendering views.

```
RSpec.describe "Users API", type: :request do
  describe "POST *api*v1*users" do
    let(:params) { { user: { email: "user@example.com", name: "Alice" } } }

    it "creates a user" do
      expect { post "*api/v1*users", params: params }
        .to change(User, :count).by(1)
    end

    it "returns 201" do
      post "*api/v1*users", params: params
      expect(response).to have_http_status(:created)
    end

    context "with invalid params" do
      let(:params) { { user: { email: "" } } }

      it "returns 422" do
        post "*api/v1/users", params: params
        expect(response).to have_http_status(:unprocessable_entity)
      end
    end
  end
end
```

# System Specs

Test critical user journeys through the full stack, including
JavaScript.

Use system specs sparingly. Cover only the most important business
flows.

```
RSpec.describe "User Registration", type: :system do
  it "allows a new user to register" do
    visit root_path
    click_on "Sign Up"

    fill_in "Email", with: "user@example.com"
    fill_in "Password", with: "securepassword"
    click_on "Create Account"

    expect(page).to have_text("Welcome!")
  end
end
```

# Factory Patterns

Use factories for test data. Keep factories simple and focused.

```
FactoryBot.define do
  factory :user do
    email { generate(:email) }
    password { "password123" }
    name { "Alice" }
  end
end
```

## Factory Guidelines

- Use sequences for unique attributes.
- Only include attributes required for a valid record.
- Use traits for variations.
- Never use factories to set up complex state — use service objects
  or dedicated setup methods.

# What to Avoid

## Controller Specs

Prefer request specs over controller specs. Request specs test the
full HTTP layer and are more reliable.

## View Specs

Prefer system specs or request specs over view specs. View specs are
brittle and test implementation details.

## Heavy Fixtures

Prefer factories over fixtures. Factories are more flexible and
easier to maintain.

# AI Integration

AI assistants can help with Rails testing by:

- Generating test files from model or controller code.
- Identifying untested code paths.
- Suggesting edge cases for existing tests.
- Converting controller specs to request specs.
- Writing factory definitions from model schemas.

When asking AI for testing help, provide:

- The model, service or controller code.
- Existing test conventions in the project.
- The testing framework (RSpec, Minitest).
- Factory definitions for related models.

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README.md)
- [Testing Strategies Guide](../../guides/engineering/testing-strategies.md)
- [Code Review Playbook](../../playbooks/code-review/README.md)
- [Rails Glossary](../../glossary/rails/README.md)
