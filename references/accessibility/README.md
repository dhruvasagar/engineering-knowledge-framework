# Purpose

Quick-reference material for accessibility engineering. Use this for
rapid lookup during development and review.

# WCAG Levels

| Level | Description                                      |
|-------|--------------------------------------------------|
| A     | Essential accessibility support.                 |
| AA    | Recommended — removes common barriers.           |
| AAA   | Highest — may not be achievable for all content. |

# WCAG Principles (POUR)

| Principle      | Meaning                                         |
|----------------|-------------------------------------------------|
| Perceivable    | Users can perceive the content.                 |
| Operable       | Users can operate the interface.                |
| Understandable | Users can understand the content and interface. |
| Robust         | Content works with current and future tools.    |

# Colour Contrast Ratios

| Text Type                  | AA    | AAA   |
|----------------------------|-------|-------|
| Normal text (< 18px)       | 4.5:1 | 7:1   |
| Large text (>= 18px, bold) | 3:1   | 4.5:1 |
| UI components              | 3:1   | 3:1   |
| Graphical objects          | 3:1   | 3:1   |

# Touch Target Size

| Target Size | Minimum          |
|-------------|------------------|
| All targets | 44x44 CSS pixels |

# ARIA Landmark Roles

| Role                 | HTML Equivalent | Purpose              |
|----------------------|-----------------|----------------------|
| role="banner"        | `<header>`      | Site-wide header     |
| role="navigation"    | `<nav>`         | Navigation sections  |
| role="main"          | `<main>`        | Primary content      |
| role="complementary" | `<aside>`       | Supporting content   |
| role="contentinfo"   | `<footer>`      | Footer information   |
| role="form"          | `<form>`        | Form sections        |
| role="search"        | `<search>`      | Search functionality |

# Keyboard Interaction Reference

| Element     | Keys                                      |
|-------------|-------------------------------------------|
| Button      | Enter / Space                             |
| Link        | Enter                                     |
| Checkbox    | Space to toggle                           |
| Radio group | Arrow keys to change, Tab to enter*exit   |
| Select      | Arrow keys, Enter to expand               |
| Tab panel   | Tab to tablist, Arrow keys to switch tabs |
| Dialog      | Tab within, Escape to close               |
| Slider      | Arrow keys, Home*End                      |

# Testing Tools

| Tool                             | Type          |
|----------------------------------|---------------|
| axe DevTools                     | Browser ext   |
| WAVE                             | Browser ext   |
| Lighthouse Accessibility         | Built-in      |
| Colour Contrast Analyser (TPGi)  | Desktop app   |
| Silktide Colour Contrast Checker | Web app       |
| VoiceOver (macOS)                | Screen reader |
| NVDA (Windows)                   | Screen reader |

# Common WCAG Failure Patterns

| Failure                      | SC    |
|------------------------------|-------|
| Missing alt text             | 1.1.1 |
| Low colour contrast          | 1.4.3 |
| No keyboard access           | 2.1.1 |
| Missing form labels          | 3.3.2 |
| No skip link                 | 2.4.1 |
| Empty or duplicate link text | 2.4.4 |
| No heading structure         | 2.4.6 |
| Missing language declaration | 3.1.1 |
| No focus indicator           | 2.4.7 |
| Colour-only indicators       | 1.4.1 |

# Accessibility Statement Requirements

- Commitment statement.
- Compliance level (WCAG X.X Level X).
- Accessibility features.
- Known limitations.
- Feedback mechanism.
- Testing methodology.

# Recommended Reading

- [[https:*/www.w3.org*TR*WCAG22*][WCAG 2.2 Specification]]
- [[https:*/www.w3.org*WAI*ARIA*apg*][ARIA Authoring Practices Guide]]
- [[https:/*developer.mozilla.org*en-US*docs*Web*Accessibility][MDN Accessibility Guide]]
- [[https:*/webaim.org*resources*][WebAIM Resources]]
- [[https:/*inclusive-components.design/][Inclusive Components]]

# Related Documents

- [Accessibility Engineering Handbook](../../handbooks/accessibility/README.md)
- [Accessibility Glossary](../../glossary/accessibility/README.md)
- [Accessibility Guides](../../guides/accessibility/README.md)
