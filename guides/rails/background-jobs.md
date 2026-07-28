---
title: "Background Jobs"
description: "Patterns for background job processing in Rails"
---


# Purpose

Background jobs handle work that should not block a web request:
sending emails, processing uploads, calling external APIs, generating
reports.

Well-designed background jobs improve responsiveness, reliability and
scalability. Poorly designed jobs introduce failures that are hard to
diagnose and retries that compound problems.

# Choosing a Framework

| Framework | Queue | Schedule | Concurrency | Use When |
| --- | --- | --- | --- | --- |
|-----------+------------+------------+-------------+----------------------------------|
| Sidekiq | Redis | Sidekiq | Threads | High throughput, existing Redis. |
| --- | --- | --- | --- | --- |
|  |  | Enterprise |  |  |
|-----------+------------+------------+-------------+----------------------------------|
| GoodJob | PostgreSQL | Built-in | Processes | Want to avoid Redis, simpler |
| --- | --- | --- | --- | --- |
|  |  |  |  | deployment. |
|-----------+------------+------------+-------------+----------------------------------|
| SolidQueue | MySQL/ | Built-in | Processes | Rails 8 default, no Redis |
| --- | --- | --- | --- | --- |
|  | PostgreSQL |  |  | needed. |
|-----------+------------+------------+-------------+----------------------------------|
| DelayedJob | Database | Built-in | Processes | Legacy applications, simplest |
| --- | --- | --- | --- | --- |
|  |  |  |  | setup. |
|-----------+------------+------------+-------------+----------------------------------|

For new projects, prefer ***SolidQueue*** (Rails 8 default, no Redis
dependency) or ***Sidekiq*** (most mature, extensive ecosystem).

# Job Structure

## Keep Jobs Focused

Each job should do one thing.

```
# Good
class SendWelcomeEmailJob < ApplicationJob
  queue_as :default

  def perform(user_id)
    user = User.find(user_id)
    UserMailer.welcome(user).deliver_now
  end
end

# Avoid
class ProcessUserJob < ApplicationJob
  def perform(user_id)
    user = User.find(user_id)
    send_welcome_email(user)
    create_default_projects(user)
    notify_slack(user)
    log_analytics(user)
  end
end
```

## Idempotent Jobs

Design jobs so they can be safely retried without side effects.

```
class ChargeSubscriptionJob < ApplicationJob
  def perform(subscription_id)
    subscription = Subscription.find(subscription_id)
    # Check if already charged (idempotency key)
    return if subscription.charged_at.present?
    subscription.charge!
  end
end
```

# Error Handling

## Automatic Retries

Sidekiq and GoodJob retry failed jobs automatically with exponential
backoff. Configure retry limits:

```
class ApiCallJob < ApplicationJob
  retry_on Timeout::Error, wait: :exponentially_longer, attempts: 5
  retry_on ThirdPartyService::TemporaryError, wait: 30.seconds, attempts: 3

  discard_on PermanentError do |job, error|
    Rails.logger.error("Permanent failure: #{error.message}")
  end

  def perform(record_id)
    # ...
  end
end
```

## Dead Letter Queue

Jobs that exhaust their retries go to the dead letter queue for manual
inspection. Monitor this queue regularly.

# Monitoring

## Dashboard

Both Sidekiq and GoodJob provide web dashboards for monitoring:

- Queue depth and processing rate.
- Failed and retried jobs.
- Job latency.
- Dead letter queue.

## Alerting

Set alerts for:

- Queue depth exceeding a threshold (jobs piling up).
- High failure rate (> 1% of jobs failing).
- Job latency exceeding acceptable limits.
- Dead letter queue receiving jobs.

# Patterns

## Batched Jobs

For processing large datasets, use batches:

```
class ProcessBatchJob < ApplicationJob
  def perform(batch_id)
    batch = Batch.find(batch_id)
    batch.records.find_each do |record|
      ProcessRecordJob.perform_later(record.id)
    end
  end
end
```

## Scheduled Jobs

Use `sidekiq-cron`, `good_job` recurring intervals, or `whenever` for
periodic jobs:

```
# config/recurring.yml (GoodJob)
production:
  every_day:
    class: DailyDigestJob
    schedule: every day at 6am
    description: "Sends daily digest emails"
```

## Throttled Jobs

Avoid overwhelming external APIs:

```
class ExternalApiJob < ApplicationJob
  sidekiq_options throttle: { threshold: 10, period: 1.second }

  def perform(record_id)
    # ...
  end
end
```

# Related Documents

- [Rails Engineering Handbook](../../handbooks/rails/README/)
- [Testing Rails Applications Guide](../../guides/rails/testing/)
- [Rails Upgrade Playbook](../../playbooks/rails/upgrade/)
- [Rails References](../../references/rails/README/)
