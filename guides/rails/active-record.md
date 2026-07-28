# Purpose

ActiveRecord is the heart of most Rails applications.

Well-designed database access code is fast, maintainable and resilient
to growth. Poorly designed access code — N+1 queries, missing indexes,
over-fetching — is the most common source of performance problems.

This guide covers patterns for writing efficient, maintainable
ActiveRecord code.

# Scopes

Scopes encapsulate common queries on a model.

## Define Scopes for Common Queries

```
class User < ApplicationRecord
  scope :active, -> { where(last_active_at: 30.days.ago..) }
  scope :admins, -> { where(role: :admin) }
  scope :by_name, ->(name) { where("name ILIKE ?", "%#{name}%") }
end
```

## Chainable Scopes

Design scopes to be chainable:

```
User.active.admins.by_name("Alice")
```

## Avoid Default Scopes

Default scopes cause unexpected behaviour when loading and
associating records. Prefer explicit scoping at the call site.

# Query Optimization

## Select Only What You Need

Avoid loading entire tables when you only need a few columns.

```
# Bad — loads all columns
User.all.each { |u| puts u.email }

# Good — loads only the needed column
User.select(:email).find_each { |u| puts u.email }
```

## Use find_each for Large Datasets

`all` loads every record into memory at once. Use `find_each` or
`find_in_batches` for large datasets.

```
# Bad — loads 100k users into memory
User.all.each { |u| u.send_newsletter }

# Good — batches 1000 at a time
User.find_each(batch_size: 1000) { |u| u.send_newsletter }
```

## Use pluck for Single Columns

When you only need an array of values from one column, use `pluck`
instead of loading records.

```
# Bad
emails = User.active.map(&:email)

# Good
emails = User.active.pluck(:email)
```

# N+1 Prevention

## Identify N+1 Queries

An N+1 query occurs when code loads a collection and then accesses an
association on each record individually, generating one query per
record.

Use the `bullet` gem to detect N+1 queries automatically.

## Eager Load with includes

Use `includes` to eager load associations:

```
# Bad — generates 1 + N queries
Post.all.each { |p| puts p.author.name }

# Good — generates 2 queries
Post.includes(:author).each { |p| puts p.author.name }
```

## Preload vs Eager Load vs Joins

| Method | Behaviour | Use When |
| --- | --- | --- |
|-------------+----------------------------------------------+---------------------------------|
| `includes` | Smart loading — uses one query per | Default choice. |
| --- | --- | --- |
|  | association, or JOINs if needed by |  |
|  | conditions. |  |
|-------------+----------------------------------------------+---------------------------------|
| `preload` | Always loads in separate queries. | You always want separate |
| --- | --- | --- |
|  |  | queries (e.g., across shards). |
|-------------+----------------------------------------------+---------------------------------|
| `eager_load` | Uses LEFT OUTER JOIN to load everything | You need to reference the |
| --- | --- | --- |
|  | in one query. | joined table in a WHERE clause. |
|-------------+----------------------------------------------+---------------------------------|

# Indexing Strategy

## Index Foreign Keys

Every foreign key used in associations or queries should have an index.

```
add_index :posts, :author_id
add_index :comments, :post_id
```

## Index Frequently Queried Columns

Columns used in `WHERE`, `ORDER BY`, or `GROUP BY` clauses should be
indexed.

## Use Composite Indexes for Multi-Column Queries

When querying on multiple columns together, use a composite index:

```
add_index :users, [:organization_id, :last_active_at]
```

The order matters: put the most selective column first.

## Avoid Redundant Indexes

Indexes have a write cost. Remove indexes that are not used.

Use PgHero or `pg_stat_statements` to identify unused indexes.

# Counter Caches

Use counter caches for frequently accessed counts:

```
class Post < ApplicationRecord
  belongs_to :author, counter_cache: true
end

class Author < ApplicationRecord
  has_many :posts
end
```

Add the column via migration:

```
add_column :authors, :posts_count, :integer, default: 0, null: false
```

# Transactions

Wrap multi-step operations in transactions:

```
ActiveRecord::Base.transaction do
  user.save!
  account.save!
  log_entry.save!
end
```

Use `save!` and `create!` (with bang) inside transactions so that any
failure triggers a rollback.

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README.md)
- [Testing Rails Applications Guide](../../guides/rails/testing.md)
- [Rails Upgrade Playbook](../../playbooks/rails/upgrade.md)
- [Rails Glossary](../../glossary/rails/README.md)
- [Rails References](../../references/rails/README.md)
