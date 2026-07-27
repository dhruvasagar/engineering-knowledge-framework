+++
title = "Design Review Accessibility Checklist"
description = "Accessibility checks during the design phase"
+++


# Purpose

Verify accessibility requirements during the design phase. Catching
issues early is significantly cheaper than fixing them in development.

# Colour and Contrast

- [ ] Colour palette includes sufficient contrast ratios.
- [ ] Colour is not the only differentiator for states and categories.
- [ ] Focus indicators are designed (not browser default or removed).
- [ ] Designs have been tested with colour blindness simulation.

# Layout and Structure

- [ ] Heading hierarchy is defined for each page/screen.
- [ ] Landmark regions are identified.
- [ ] Tab order follows the visual design.
- [ ] Touch targets are at least 44x44 pixels.
- [ ] Content is readable at 200% zoom.

# Content

- [ ] Link text is meaningful out of context (no "click here").
- [ ] Error messages are clear and actionable.
- [ ] Instructions do not rely solely on sensory characteristics.
- [ ] Language is clear and readable.

# Forms

- [ ] Label placement is clear and consistent.
- [ ] Error states are visually distinct.
- [ ] Required fields are marked.
- [ ] Grouped controls use `<fieldset>` pattern in design.

# Motion and Animation

- [ ] Motion is not essential for understanding content.
- [ ] Animations respect reduced motion preferences.
- [ ] Auto-playing content can be paused.

# Related Documents

- [Accessibility Engineering Handbook](../../handbooks/accessibility/README/)
- [Colour and Contrast](../../guides/accessibility/colour-and-contrast/)
- [Accessible Forms](../../guides/accessibility/accessible-forms/)
