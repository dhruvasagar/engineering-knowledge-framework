+++
title = "Query Object Template"
description = "Template for Rails query objects"
+++


# Purpose

Query objects encapsulate complex database queries that do not belong
in a model scope.

Use this template when a query involves multiple conditions,
join logic or aggregation that would overly bloat the model.

# Template

```
# app*queries*QUERY_NAME.rb
class QUERY_NAME
  def initialize(relation = Model.all)
    @relation = relation
  end

  def call(params = {})
    # Chain scopes and conditions
    # scope = @relation
    # scope = scope.where(active: true) if params[:active_only]
    # scope = scope.includes(:association) if params[:include_association]
    # scope
  end

  private

  attr_reader :relation
end
```

# Usage

```
# In a controller or service
query = QUERY_NAME.new
results = query.call(active_only: true)

# With a specific starting relation
relation = Model.where(tenant: current_tenant)
query = QUERY_NAME.new(relation)
results = query.call
```

# Related Documents

- [Rails Engineering Handbook](../..*handbooks*rails*README*)
- [Service Objects Guide](../..*guides*rails*service-objects*)
