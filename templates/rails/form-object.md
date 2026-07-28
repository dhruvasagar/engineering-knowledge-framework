# Purpose

Form objects encapsulate validation and data processing for forms that
do not map directly to a single model.

Use this template when a form collects data for multiple models or has
validation logic that does not belong to any single model.

# Template

```
# app*forms*FORM_NAME.rb
class FORM_NAME
  include ActiveModel::Model
  include ActiveModel::Attributes

  # Define attributes
  # attribute :name, :string
  # attribute :email, :string
  # attribute :age, :integer

  # Validations
  # validates :name, :email, presence: true
  # validates :email, format: { with: URI::MailTo::EMAIL_REGEXP }
  # validates :age, numericality: { greater_than: 0 }, allow_nil: true

  def save
    return false unless valid?

    persist!
    true
  end

  private

  def persist!
    # Persist data across one or more models
    # ActiveRecord::Base.transaction do
    #   user = User.create!(name: name, email: email)
    #   Profile.create!(user: user, age: age)
    # end
  end
end
```

# Usage

```
form = FORM_NAME.new(name: "Alice", email: "alice@example.com")
if form.save
  # Handle success
else
  # Handle errors — form.errors is available
end
```

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README.md)
- [Service Objects Guide](../../guides/rails/service-objects.md)
