+++
title = "WCAG Audit Checklist"
description = "Comprehensive WCAG compliance audit"
+++


# Purpose

Complete WCAG 2.2 AA audit checklist. Use this for full accessibility
audits before major releases or as part of a quality review.

# Perceivable

## Text Alternatives

- [ ] All images have appropriate alt text (decorative images use empty alt).
- [ ] Complex images (charts, graphs) have long descriptions.
- [ ] CAPTCHAs have alternative forms.
- [ ] Audio and video content has text transcripts.

## Time-Based Media

- [ ] Prerecorded video has captions.
- [ ] Live video has captions.
- [ ] Audio descriptions are available for video content.

## Adaptable

- [ ] Content maintains meaning when linearised (without CSS).
- [ ] Information is not conveyed solely by sensory characteristics
      (shape, size, colour, sound).
- [ ] Orientation (portrait*landscape) is not locked.

## Distinguishable

- [ ] Colour is not the only means of conveying information.
- [ ] Normal text meets 4.5:1 contrast ratio.
- [ ] Large text meets 3:1 contrast ratio.
- [ ] UI components meet 3:1 contrast ratio.
- [ ] Text can be resized to 200% without loss of content or functionality.
- [ ] Images of text are not used (except logos).
- [ ] Content respects reduced motion preferences.

# Operable

## Keyboard Accessible

- [ ] All functionality is operable via keyboard.
- [ ] No keyboard traps exist.
- [ ] Keyboard focus order is logical.
- [ ] Custom widgets have appropriate keyboard handling.

## Enough Time

- [ ] Time limits have an option to extend, adjust or remove.
- [ ] Moving, blinking or auto-updating content can be paused, stopped
      or hidden.
- [ ] No content flashes more than three times per second.

## Seizures and Physical Reactions

- [ ] No content flashes more than three times per second.

## Navigable

- [ ] Skip link is present and functional.
- [ ] Page has descriptive title.
- [ ] Heading hierarchy is logical and does not skip levels.
- [ ] Link text is meaningful out of context.
- [ ] Multiple ways are available to find content (search, sitemap, navigation).

## Input Modalities

- [ ] All functionality can be operated with a pointer alone.
- [ ] Touch targets are at least 44x44 pixels.
- [ ] Motion actuation can be disabled.

# Understandable

## Readable

- [ ] Language is declared on the page (`lang` attribute on `<html>`).
- [ ] Unusual words and abbreviations are defined.
- [ ] Reading level is appropriate for the audience.

## Predictable

- [ ] Navigation is consistent across pages.
- [ ] Components with the same label have the same functionality.
- [ ] Significant changes (new window, focus change) are triggered by
      user action, not automatically.

## Input Assistance

- [ ] Input errors are identified and described to the user.
- [ ] Labels and instructions are provided for all inputs.
- [ ] Error suggestions are provided when possible.
- [ ] Legal and financial transactions are reversible or confirmed.

# Robust

## Compatible

- [ ] HTML is valid and parses correctly.
- [ ] ARIA attributes are used correctly.
- [ ] Status messages are announced to assistive technology.

# Related Documents

- [Accessibility Engineering Handbook](..*..*handbooks*accessibility*README*)
- [Accessibility Review Playbook](../..*playbooks*accessibility-review*README*)
- [Accessibility References](../..*references*accessibility*README*)
