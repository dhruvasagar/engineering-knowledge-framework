+++
title = "Accessibility Glossary"
description = "Canonical terminology for accessibility engineering"
+++


# Purpose

Canonical definitions for accessibility engineering terminology. Every
term should have one clear meaning across all framework documents.

# Glossary

## Accessibility

The design of products, devices, services or environments for people
with disabilities. In software engineering, accessibility ensures that
digital products can be used by people with diverse abilities.

## Alternative Text (Alt Text)

A text alternative for non-text content such as images. Alt text is
read by screen readers and displayed when images do not load. It should
convey the purpose and content of the image.

## ARIA (Accessible Rich Internet Applications)

A W3C specification that provides attributes to enhance the
accessibility of dynamic content and custom user interface widgets.
ARIA supplements HTML semantics but should not be used as a substitute
for semantic HTML when native elements are available.

## Assistive Technology (AT)

Tools used by people with disabilities to interact with digital content.
Examples include screen readers (JAWS, NVDA, VoiceOver), screen
magnifiers, speech recognition software and switch devices.

## Colour Contrast

The difference in luminance between foreground text and its background.
Sufficient contrast is essential for readability. WCAG requires a
contrast ratio of at least 4.5:1 for normal text and 3:1 for large text
(Level AA).

## Focus Indicator

A visual cue that shows which element on the page currently has
keyboard focus. Custom focus indicators should have sufficient contrast
and not be removed unless a replacement is provided.

## Keyboard Accessibility

The ability to navigate and operate all functionality using a keyboard
alone. Keyboard accessibility is a fundamental requirement for users
with motor disabilities and screen reader users.

## Landmark

An ARIA role or HTML element that identifies the major regions of a
page (navigation, main, complementary, contentinfo). Landmarks enable
screen reader users to navigate quickly between sections.

## Screen Reader

An assistive technology that reads digital content aloud. Users rely on
semantic HTML, ARIA attributes and keyboard navigation to understand
and interact with content.

## Semantic HTML

The use of HTML elements according to their intended meaning rather than
their visual appearance. Semantic HTML provides built-in accessibility
support and is the foundation of accessible web development.

## Skip Link

A link at the top of a page that allows keyboard and screen reader users
to skip directly to the main content, bypassing repeated navigation
elements.

## WCAG (Web Content Accessibility Guidelines)

The international standard for web accessibility published by the W3C.
WCAG is organised around four principles: Perceivable, Operable,
Understandable and Robust (POUR).

## WAI-ARIA Authoring Practices

A W3C guide that provides recommendations for making advanced user
interface patterns accessible. It covers patterns for menus, dialogs,
tabs, carousels and other common widgets.

# Related Documents

- [Accessibility Engineering Handbook](../..*handbooks*accessibility*README*)
- [Accessibility References](../..*references*accessibility*README*)
- [Accessibility Guides](../..*guides*accessibility/)
