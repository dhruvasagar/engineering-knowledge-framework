---
title: "AI Workflows for Accessibility"
description: "Prompt patterns for AI-assisted accessibility engineering"
---


# Purpose

This document provides prompt patterns for using AI to assist with
accessibility engineering tasks — auditing, remediation, form review
and alternative text generation.

# Principles

- AI can accelerate accessibility work but cannot replace human testing
  with assistive technologies.
- Automated checks catch ~30% of issues — AI-augmented manual testing
  catches more, but screen reader testing remains essential.
- All AI-generated accessibility fixes must be verified by a human.

# Workflows

## Accessibility Audit

Use AI to perform a preliminary accessibility audit of HTML content.

Context:

```
Audit the following HTML for accessibility issues:

[paste HTML]

Check for:
1. Missing or incorrect ARIA attributes.
2. Heading hierarchy violations.
3. Missing form labels.
4. Missing alt text.
5. Keyboard accessibility issues.
6. Colour contrast concerns (list colours used).

For each issue, reference the relevant WCAG success criterion.
```

## Alt Text Generation

Use AI to generate alternative text for images.

Context:

```
Generate concise, descriptive alt text for the following image:

[image description or URL]

Context: [what is the image's purpose on the page?]
Is the image: [informative / decorative / functional / complex]

If decorative, suggest empty alt (alt="").
If complex (chart, graph), suggest a short alt text plus a longer
description.
```

## Form Accessibility Review

Use AI to review form implementations for accessibility.

Context:

```
Review this form for accessibility issues:

[paste HTML]

Check:
1. Every input has an associated label.
2. Error messages use aria-describedby.
3. Required fields use aria-required.
4. Grouped controls use fieldset and legend.
5. Submit button is present and labelled.
6. Autocomplete attributes are used where appropriate.

Suggest specific fixes for each issue.
```

## Colour Contrast Analysis

Use AI to analyse and suggest colour palette improvements.

Context:

```
Analyse these colours for WCAG AA contrast compliance:

Text colour: [colour value]
Background colour: [colour value]
Primary UI colour: [colour value]

Calculate the contrast ratio for each combination and suggest
alternatives if they do not meet:
- 4.5:1 for normal text.
- 3:1 for large text and UI components.

Suggest alternative colours that maintain the design intent while
meeting contrast requirements.
```

## ARIA Pattern Review

Use AI to review ARIA implementations for correctness.

Context:

```
Review this ARIA implementation for correctness:

[paste HTML]

Check:
1. Are ARIA roles used correctly?
2. Are ARIA states and properties managed properly?
3. Are there redundant ARIA (native HTML already provides semantics)?
4. Is keyboard handling implemented for custom widgets?
5. Is focus management correct?

Follow the WAI-ARIA Authoring Practices for pattern guidance.
```

# Anti-patterns

- ***AI as sole auditor***: AI catches ~30% of issues. Always pair with
  manual screen reader testing.
- ***Over-reliance on generated alt text***: AI-generated alt text should
  be reviewed — it often misses context or generates verbose descriptions.
- ***Assuming ARIA fixes everything***: Incorrect ARIA is worse than no
  ARIA. Review all ARIA additions carefully.

# Related Documents

- [Accessibility Engineering Handbook](../handbooks/accessibility/README/)
- [Accessibility Guides](../guides/accessibility/)
- [Accessibility Review Playbook](../playbooks/accessibility-review/README/)
- [WCAG Audit Checklist](../checklists/accessibility/wcag-audit/)
- [AI Usage Checklist](../checklists/ai-usage/)
