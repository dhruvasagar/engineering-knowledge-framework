+++
title = "Accessibility Review Playbook"
description = "Workflow for reviewing digital accessibility"
+++


# Objective

Perform systematic accessibility reviews to identify and remediate
accessibility barriers. Reviews combine automated checks, manual
testing and assistive technology verification.

# Inputs

- Application or component to review.
- WCAG compliance target (default: WCAG 2.2 AA).
- Accessibility requirements from design phase.

# Prerequisites

- Familiarity with [Accessibility Engineering principles](../../handbooks/accessibility/README/).
- Accessibility testing tools installed (axe DevTools, colour contrast
  checker, screen reader).
- [Accessibility checklists](../../checklists/accessibility/) available.

# Workflow

## Step 1: Automated Scan

Run automated accessibility checks:

1. Use axe DevTools or WAVE browser extension.
2. Run CI-based accessibility linter (e.g., axe-core, Pa11y).
3. Document all automated findings.
4. Filter false positives.

## Step 2: Manual Keyboard Test

1. Tab through all interactive elements.
2. Verify visible focus indicators.
3. Test all custom widget keyboard interactions.
4. Verify no keyboard traps.

## Step 3: Screen Reader Test

1. Test with VoiceOver (macOS) or NVDA (Windows).
2. Navigate by headings, landmarks and links.
3. Verify form labels and error announcements.
4. Test dynamic content updates.

## Step 4: Visual Review

1. Check colour contrast for all text and UI components.
2. Verify content is readable at 200% zoom.
3. Check responsive layout at different viewport sizes.
4. Verify reduced motion preferences are respected.

## Step 5: Document Findings

1. Record all findings with severity labels (see [Accessibility References](../../references/accessibility/README/)).
2. Include the WCAG criterion violated for each finding.
3. Provide reproduction steps and remediation guidance.
4. Prioritise findings by impact.

# Severity Labels

| Severity | Description |
| --- | --- |
+----------+-------------------------------------------------------+
| Critical | Complete barrier — user cannot complete a task. |
| --- | --- |
| High | Significant barrier — task is very difficult. |
| Medium | Moderate barrier — task is more difficult than needed. |
| Low | Minor issue — does not block task completion. |

# Checklist

- [ ] Automated scan completed.
- [ ] Manual keyboard test completed.
- [ ] Screen reader test completed.
- [ ] Colour contrast verified.
- [ ] Zoom and responsiveness checked.
- [ ] Reduced motion verified.
- [ ] Findings documented with severity.
- [ ] Remediation guidance provided.
- [ ] Follow-up review scheduled for critical/high issues.

# Escalation Points

- Critical blocking issues: escalate to product owner.
- Pattern-level failures (e.g., all dialogs have the same issue): create
  a component fix and apply globally.
- Legal compliance concerns: escalate to legal team.

# Expected Outputs

- Accessibility review report with findings and severity.
- Remediation recommendations for each finding.
- Updated WCAG compliance status.

# Related Documents

- [Accessibility Engineering Handbook](../../handbooks/accessibility/README/)
- [Accessibility Checklists](../../checklists/accessibility/)
- [Accessibility References](../../references/accessibility/README/)
- [Accessibility Guides](../../guides/accessibility/)
