# Objective

Ensure architectural decisions are sound, well-documented, aligned with
principles, and appropriate for the system's context and goals.

Architecture reviews provide a structured forum for evaluating
significant design decisions before they become costly to reverse.

# Inputs

- Architecture Decision Record (ADR) or RFC proposing the change.
- Current architecture documentation (diagrams, decision log, system
  context).
- Relevant quality attribute requirements.
- Business context and constraints.

# Prerequisites

Before requesting an architecture review, the author should verify:

- [ ] An ADR or RFC is drafted with context, decision and consequences.
- [ ] Alternatives have been identified and evaluated.
- [ ] Quality attribute trade-offs are documented.
- [ ] Architecture diagrams are current (C4 model preferred).
- [ ] Relevant stakeholders have been identified.
- [ ] The proposal is ready for review, not early exploration.

# Workflow

## Step 1: Determine Review Scope

Not every decision needs a full architecture review.

| Decision Type | Review Level | Participants |
| --- | --- | --- |
|---------------------------------+-------------------+---------------------------|
| Technology introduction | Full review | Architects, senior |
| --- | --- | --- |
|  |  | engineers, operations |
| Architecture pattern change | Full review | Architects, affected team |
| Service boundary change | Full review | Architects, service owners |
| API design decision | Lightweight | Technical lead, reviewer |
| Library or framework upgrade | Lightweight | Team, platform |
| Internal component refactor | Self-service | Team only |

## Step 2: Assemble Review Team

Select reviewers based on scope:

- At least one architect or senior engineer not on the proposing team.
- Representatives from affected teams.
- Subject matter experts (security, performance, data) as needed.
- Operations or platform team if deployment or infrastructure is
  affected.

## Step 3: Distribute Materials

Share the following at least two business days before the review:

- ADR or RFC document.
- Current architecture diagrams.
- Alternatives analysis.
- Quality attribute trade-off matrix.
- Any relevant performance, security or scalability data.

## Step 4: Conduct the Review

### Presentation (15-20 minutes)

The author presents:

- The problem or opportunity.
- The proposed approach.
- Alternatives considered.
- Trade-offs and consequences.

#### Discussion and Questions (30-40 minutes)

Reviewers evaluate the proposal against:

| Criterion | Questions |
| --- | --- |
|----------------------------------+--------------------------------------------------------------|
| Problem alignment | Does the proposal solve the stated problem? Is the problem |
| --- | --- |
|  | correctly understood? |
|----------------------------------+--------------------------------------------------------------|
| Principle alignment | Is the proposal consistent with engineering and architecture |
| --- | --- |
|  | principles? Does it follow separation of concerns, |
|  | encapsulation and dependency management? |
|----------------------------------+--------------------------------------------------------------|
| Quality attributes | Are the relevant quality attributes addressed (performance, |
| --- | --- |
|  | scalability, security, maintainability, evolvability)? |
|  | Are trade-offs explicitly acknowledged? |
|----------------------------------+--------------------------------------------------------------|
| Alternatives | Were meaningful alternatives considered? Is the chosen |
| --- | --- |
|  | approach justified relative to the alternatives? |
|----------------------------------+--------------------------------------------------------------|
| Consequences | Are the consequences (both positive and negative) fully |
| --- | --- |
|  | understood? Are there hidden dependencies or risks? |
|----------------------------------+--------------------------------------------------------------|
| Documentation | Is the decision adequately documented? Can a future engineer |
| --- | --- |
|  | understand the reasoning? |
|----------------------------------+--------------------------------------------------------------|

#### Decision and Next Steps (10-15 minutes)

The review concludes with one of:

| Outcome | Meaning |
| --- | --- |
|---------------+--------------------------------------------------------|
| Approved | The decision is accepted. Proceed with implementation. |
| --- | --- |
| Conditional | Approved pending specific changes. Address conditions |
|  | and confirm with reviewers. |
| Revise | Significant issues identified. Revise and resubmit. |
| Rejected | The proposal is not accepted. Document the reasoning |
|  | and explore alternatives. |

## Step 5: Document the Outcome

The author updates the ADR or RFC with:

- Review date and participants.
- Review outcome.
- Conditions or action items.
- Rationale for any changes made during review.

## Step 6: Follow Up

For approved or conditional decisions:

- Schedule implementation milestones.
- Identify monitoring points to validate the decision.
- Schedule a post-implementation review if appropriate.

# Checklist

The reviewer should verify:

- [ ] The problem is clearly defined and understood.
- [ ] The proposal is consistent with architecture principles.
- [ ] Quality attributes are explicitly addressed.
- [ ] Trade-offs are documented and acknowledged.
- [ ] Meaningful alternatives were considered.
- [ ] Consequences are fully understood.
- [ ] The decision is documented in an ADR or RFC.
- [ ] All stakeholders have been consulted.
- [ ] Risks are identified and mitigated.
- [ ] The proposal can be implemented incrementally.

# Escalation Points

| Situation | Action |
| --- | --- |
|---------------------------------------------+-------------------------------------|
| Disagreement cannot be resolved in review | Escalate to the architecture forum |
| --- | --- |
|  | or chief architect. |
| Decision affects multiple organizations | Involve all affected teams before |
|  | finalizing. |
| Security or compliance implications | Require security review sign-off. |
| Significant cost or resource impact | Include budget or resource owner |
|  | in the review. |

# AI Workflow

AI assistants can support architecture reviews by:

## Preparation

- Summarizing the proposal and alternatives for reviewers.
- Generating trade-off matrices from the ADR.
- Identifying related ADRs and architectural decisions.
- Drafting review questions based on the proposal.

### During Review

- Recording decisions and action items.
- Comparing the proposal against stored principles and patterns.
- Identifying potential blind spots or unaddressed quality attributes.

### Post-Review

- Updating ADRs with review outcomes.
- Generating decision logs from review conclusions.
- Tracking conditions and action items.

When using AI for architecture review support, provide:

- The ADR or RFC under review.
- Current architecture documentation.
- Relevant principles and standards.
- Review criteria and evaluation framework.

# Expected Outputs

- Reviewed and documented architectural decision.
- Updated ADR or RFC with review outcome.
- Clear decision on whether to proceed.
- Action items and conditions documented.
- Knowledge shared across the team and stakeholders.

# Related Documents

- [Software Architecture Handbook](../../handbooks/architecture/README.md)
- [Engineering Fundamentals Handbook](../../handbooks/engineering/README.md)
- [ADR Writing Guide](../../guides/architecture/adr-writing-guide.md)
- [Architectural Patterns Guide](../../guides/architecture/architectural-patterns.md)
- [ADR Template](../../templates/adr/README.md)
- [Architecture Glossary](../../glossary/architecture/README.md)
