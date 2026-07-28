---
title: "Service Object Template"
description: "Template for Rails service objects"
---


# Purpose

Service objects encapsulate a single business operation.

Use this template when the operation involves multiple models, external
services or complex orchestration.

# Template

```
# app*services*OPERATION_NAME.rb
class OPERATION_NAME
  Result = Struct.new(:success?, :data, :error, keyword_init: true)

  def initialize(params)
    @params = params
  end

  def call
    validate_params
    perform_operation
    Result.new(success?: true, data: result_data)
  rescue StandardError => e
    Result.new(success?: false, error: e)
  end

  private

  attr_reader :params

  def validate_params
    # Raise if required params are missing or invalid
  end

  def perform_operation
    # Business logic here
  end

  def result_data
    # Return the operation result
  end
end
```

# Usage

```
result = OPERATION_NAME.new(param1: value1).call

if result.success?
  # Handle success
else
  # Handle failure
end
```

# Related Documents

- [Service Objects Guide](../../guides/rails/service-objects/)
- [Rails Engineering Handbook](../../handbooks/rails/README/)
