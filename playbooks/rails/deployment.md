---
title: "Rails Deployment Playbook"
description: "Repeatable workflow for safe Rails deployments with database migrations"
---


# Objective

Deploy Rails application changes to production safely, with particular
attention to database migrations that can cause downtime or data loss.

# Inputs

- Commit or release to be deployed.
- Database migrations included in the release.
- Release notes documenting changes.

# Prerequisites

- [ ] All CI checks pass (RuboCop, Brakeman, bundler-audit, tests).
- [ ] Code coverage meets the project threshold.
- [ ] No known blocking issues in the release.
- [ ] Database migrations reviewed for safety.
- [ ] Rollback plan is documented.
- [ ] Team is notified of the deployment window.

# Workflow

## Step 1: Migration Review

Review all pending migrations for safety concerns.

Use `strong_migrations` to detect dangerous operations:

```
bundle exec strong_migrations --check
```

| Dangerous Operation | Safe Alternative |
| --- | --- |
|-----------------------------------+----------------------------------------|
| Adding a column with a default | Add column, then backfill default. |
| --- | --- |
| value to a large table |  |
|-----------------------------------+----------------------------------------|
| Adding an index on a large table | Use `CONCURRENTLY` (see below). |
| --- | --- |
|-----------------------------------+----------------------------------------|
| Removing a column | Mark as ignored first, remove later. |
| --- | --- |
|-----------------------------------+----------------------------------------|
| Renaming a column | Add new column, backfill, drop old. |
| --- | --- |
|-----------------------------------+----------------------------------------|
| Changing column type | Add new column, backfill, drop old. |
| --- | --- |
|-----------------------------------+----------------------------------------|

## Step 2: Deploy Migrations First

For zero-downtime deployments, run migrations before deploying new
application code.

```
# Deploy step 1: Run migrations
bundle exec rails db:migrate

# Deploy step 2: Deploy application code
capistrano deploy  # or equivalent
```

This ensures the database schema is ready before the new code runs.

## Step 3: Monitor Deployment

Watch for:

- Migration duration — long migrations may indicate lock contention.
- Error rates — spikes may indicate code incompatible with old schema.
- Queue depth — background jobs may fail if schema changed.
- Response times — new queries may be unoptimized.

## Step 4: Verify Deployment

Run smoke tests against the deployed version:

- Critical user journeys.
- API health endpoints.
- Background job processing.
- Admin functionality.

## Step 5: Rollback if Needed

If issues are detected:

1. Revert the application code to the previous version.
2. Roll back migrations only if they are reversible and no data has
   been written.
3. Investigate and document the issue before re-deploying.

# Migration Patterns

## Adding an Index Concurrently

```
class AddIndexToUsersOnEmail < ActiveRecord::Migration[7.1]
  disable_ddl_transaction!

  def change
    add_index :users, :email, algorithm: :concurrently
  end
end
```

## Backfilling Data

Backfill in a separate Rake task, not in the migration:

```
# db*migrate*20260101000000_add_status_to_users.rb
class AddStatusToUsers < ActiveRecord::Migration[7.1]
  def change
    add_column :users, :status, :string, default: "active", null: false
  end
end

# lib*tasks*backfill.rake
namespace :backfill do
  desc "Backfill user status"
  task user_status: :environment do
    User.where(status: nil).find_each do |user|
      user.update!(status: "active")
    end
  end
end
```

## Removing a Column Safely

1. Mark the column as ignored in the model.
2. Deploy.
3. Remove the column in a subsequent migration.
4. Deploy again.

```
class User < ApplicationRecord
  self.ignored_columns = %w[legacy_column]
end

# Subsequent migration
class RemoveLegacyColumnFromUsers < ActiveRecord::Migration[7.1]
  def change
    remove_column :users, :legacy_column
  end
end
```

# Checklist

- [ ] All CI checks pass.
- [ ] Migrations reviewed for safety.
- [ ] No dangerous operations (add column with default, rename, etc.).
- [ ] Migrations use `CONCURRENTLY` for indexes on large tables.
- [ ] Backfilling is in Rake tasks, not migrations.
- [ ] Rollback plan documented.
- [ ] Team notified of deployment window.
- [ ] Smoke tests pass after deployment.

# Expected Outputs

- New version deployed to production.
- Database schema updated safely.
- No downtime or data loss.
- Deployment documented in the release log.

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README/)
- [ActiveRecord Patterns Guide](../../guides/rails/active-record/)
- [Rails Upgrade Playbook](../../playbooks/rails/upgrade/)
- [Rails Deployment Checklist](../../checklists/rails/deployment/)
