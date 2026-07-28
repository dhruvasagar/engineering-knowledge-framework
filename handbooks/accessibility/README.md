---
title: "Accessibility Engineering Handbook"
description: "Engineering principles and practices for digital accessibility"
---


# Purpose

Accessibility engineering ensures that digital products are usable by
people with disabilities. This handbook provides the principles,
standards and practices for building accessible software.

Accessibility is not a feature — it is a fundamental quality attribute
of well-engineered software.

# Scope

This handbook covers:

- Accessibility principles and philosophy.
- Standards and compliance (WCAG, ARIA, Section 508).
- Inclusive design practices.
- Testing methodology and tooling.
- Integration into development workflows.
- AI-assisted accessibility workflows.

It does not cover:

- Legal or regulatory compliance advice (consult legal counsel).
- Specific assistive technology training.

# Principles

## Accessibility is a Quality Attribute

Accessibility is not separate from quality — it is a dimension of
quality alongside security, performance and maintainability. Accessible
software is typically better engineered software for all users.

## Inclusive by Default

Design and build for diverse users from the start. Retrofitting
accessibility is more expensive and produces worse outcomes than
building inclusively from the beginning.

## Standards Are the Floor, Not the Ceiling

WCAG compliance is the minimum standard. Truly accessible products go
beyond compliance to deliver excellent experiences for all users.

## Automation Augments, Not Replaces, Human Testing

Automated accessibility checks catch ~30% of issues. Manual testing
with assistive technologies and human judgement is essential.

## Accessibility is Everyone's Responsibility

Engineers, designers, product managers and QA all contribute to
accessibility. The engineering handbook focuses on the technical
aspects, but accessibility success requires organisational commitment.

# Standards

## WCAG (Web Content Accessibility Guidelines)

WCAG is the primary international standard for web accessibility. It is
organised around four principles (POUR):

| Principle | Description |
| --- | --- |
+-----------------+----------------------------------------------------+
| Perceivable | Users must be able to perceive the content. |
| --- | --- |
| Operable | Users must be able to operate the interface. |
| Understandable | Users must be able to understand the content. |
| Robust | Content must work with current and future tools. |

WCAG has three conformance levels:

| Level | Description |
| --- | --- |
+-------+----------------------------------------------------+
| A | Minimum level — essential accessibility support. |
| --- | --- |
| AA | Recommended level — removes common barriers. |
| AAA | Highest level — may not be achievable for all content. |

Target ***WCAG 2.2 AA*** as the minimum compliance level.

## ARIA (Accessible Rich Internet Applications)

ARIA provides attributes that enhance the accessibility of dynamic
content and custom widgets. Follow the [Accessibility References](../../references/accessibility/README/) for
ARIA usage guidelines.

# Testing Methodology

| Method | Coverage | When |
| --- | --- | --- |
+--------------------------+----------+------------------------------+
| Automated checks | ~30% | CI pipeline, every commit. |
| --- | --- | --- |
| Manual keyboard testing | ~50% | Every feature before merge. |
| Screen reader testing | ~80% | Before release, major features. |
| User testing | ~90%+ | Periodic, with diverse users. |

# Integration into Development

## Design Phase

- Accessibility requirements in user stories.
- Design reviews include accessibility checklist.
- Colour contrast verified early.

## Development Phase

- Use semantic HTML by default.
- Follow ARIA authoring practices.
- Keyboard accessibility tested continuously.
- Accessibility linting in IDE.

## Review Phase

- Accessibility checklist in PR review.
- Automated checks in CI pipeline.
- Manual keyboard and screen reader testing.

## Release Phase

- Full accessibility audit before major releases.
- QA includes accessibility test cases.
- Regression testing for accessibility.

# AI Integration

AI can assist with accessibility engineering:

- Automated accessibility auditing (detecting missing alt text, poor
  contrast, missing labels).
- Generating accessible code patterns (semantic HTML, ARIA attributes).
- Analysing colour contrast and suggesting alternatives.
- Reviewing forms for accessible error handling.
- Generating alternative text suggestions.
- Identifying focus management issues.

See [AI Workflows for Accessibility](../../prompts/accessibility-ai-workflows/) for prompt patterns.

# Capability Map

All documents in the Accessibility Engineering capability:

| Document Type | Document |
| --- | --- |
+---------------+----------------------------------------------+
| Handbook | [Accessibility Engineering Handbook](./README/) |
| --- | --- |
| Glossary | [Accessibility Glossary](../../glossary/accessibility/README/) |
| Guides | [Accessibility Guides](../../guides/accessibility/) |
| Playbooks | [Accessibility Review Playbook](../../playbooks/accessibility-review/README/) |
| Checklists | [Accessibility Checklists](../../checklists/accessibility/) |
| Templates | [Accessibility Templates](../../templates/accessibility/) |
| Learning Paths | [Accessibility Learning Paths](../../learning-paths/accessibility/README/) |
| References | [Accessibility References](../../references/accessibility/README/) |
| AI Workflows | [AI Workflows for Accessibility](../../prompts/accessibility-ai-workflows/) |

# Related Documents

- [Accessibility Glossary](../../glossary/accessibility/README/)
- [Accessibility References](../../references/accessibility/README/)
- [Accessibility Review Playbook](../../playbooks/accessibility-review/README/)
- [WCAG 2.2 Specification](https://www.w3.org/TR/WCAG22/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
