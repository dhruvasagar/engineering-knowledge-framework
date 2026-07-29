---
title: "Tech Debt Assessment"
description: "Ensure technical debt is identified, classified, tracked and addressed systematically."
type: checklist
capability: quality
status: published
tags: [tech, debt, assessment]
last_reviewed: 2026-07-28
---

# Purpose

Ensure technical debt is identified, classified, tracked and addressed
systematically.

# Identification

- [ ] Code area exhibits frequent defects or regressions.
- [ ] Changes in this area are slower than expected.
- [ ] Tests are missing, brittle or slow.
- [ ] Code is difficult to understand or modify.
- [ ] Duplicated logic exists across multiple locations.
- [ ] Dependencies are outdated or unmaintained.
- [ ] Architectural boundaries are violated or unclear.

# Classification

- [ ] Debt type is identified: strategic or accidental.
- [ ] Severity is assessed: low, medium, high, critical.
- [ ] Impact is understood: velocity, quality, risk.
- [ ] Effort to remediate is estimated.
- [ ] Business value of remediation is articulated.

# Tracking

- [ ] Debt is recorded in the team's tracking system.
- [ ] Context and rationale are documented.
- [ ] Responsible team or owner is identified.
- [ ] Related issues or areas are linked.

# Remediation Planning

- [ ] Remediation is scheduled in a future iteration.
- [ ] Incremental approach is preferred over rewrite.
- [ ] Tests exist to prevent regression during remediation.
- [ ] Stakeholders are aware of the debt and plan.

# Related Documents

- [Engineering Fundamentals Handbook](../handbooks/engineering/README.md)
- [Software Architecture Handbook](../handbooks/architecture/README.md)
- [Code Review Playbook](../playbooks/code-review/README.md)
- [Engineering Glossary](../glossary/engineering/README.md)
