+++
title = "PR Accessibility Checklist"
description = "Quick accessibility checks for every pull request"
+++


# Purpose

Quick accessibility verification for every pull request. Completing these
checks before requesting review prevents accessibility regressions.

# Markup

- [ ] Semantic HTML elements used where possible (`<nav>`, `<main>`, `<button>`, etc.).
- [ ] Heading hierarchy maintained (no skipped levels).
- [ ] All images have appropriate alt text.
- [ ] ARIA attributes are used correctly (if applicable).

# Keyboard

- [ ] New interactive elements are keyboard reachable.
- [ ] Focus indicator is visible.
- [ ] Tab order follows visual order.
- [ ] No keyboard traps introduced.

# Forms

- [ ] Every input has an associated label.
- [ ] Error messages are linked to inputs via `aria-describedby`.
- [ ] Required fields are indicated.

# Visual

- [ ] Colour is not the only means of conveying information.
- [ ] Colour contrast meets WCAG AA for new elements.
- [ ] Text is readable at 200% zoom.

# Testing

- [ ] Automated accessibility scan passes (axe DevTools or CI tool).
- [ ] Quick screen reader spot-check performed.

# Related Documents

- [Accessibility Engineering Handbook](../../handbooks/accessibility/README/)
- [Semantic HTML](../../guides/accessibility/semantic-html/)
- [Keyboard Accessibility](../../guides/accessibility/keyboard-accessibility/)
