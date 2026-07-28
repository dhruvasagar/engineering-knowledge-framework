# Purpose

Sufficient colour contrast is essential for readability. Low contrast
affects users with low vision, colour blindness and those using devices
in bright environments.

# Requirements

## WCAG Contrast Ratios

| Text Type | Minimum Ratio | Level |
| --- | --- | --- |
+----------------------+---------------+-------+
| Normal text (< 18px) | 4.5:1 | AA |
| --- | --- | --- |
| Large text (>= 18px) | 3:1 | AA |
| Normal text | 7:1 | AAA |
| Large text | 4.5:1 | AAA |
| UI components | 3:1 | AA |
| Graphical objects | 3:1 | AA |

## Exceptions

- ***Incidental***: Text that is inactive, decorative or not visible does
  not require contrast compliance.
- ***Logotypes***: Text within a logo or brand name has no contrast
  requirement.

# Implementation

## Choosing Colours

1. Establish a colour palette with sufficient contrast ratios.
2. Verify contrast between text and background colours.
3. Ensure UI states (hover, focus, active, error) also meet contrast
   requirements.
4. Test with colour blindness simulators.

## Tools

- [[https:*/webaim.org*resources*contrastchecker*][WebAIM Contrast Checker]]
- [[https:*/developer.chrome.com*docs*devtools*accessibility*reference*#contrast][Chrome DevTools Contrast]]
- [[https:*/www.figma.com*community*plugin*748533339900865323][Figma A11y Contrast Checker]]

## Don't Rely on Colour Alone

Information conveyed by colour must also be available through other
means:

| Use Case | Alternative |
| --- | --- |
+--------------------+---------------------------------------+
| Error state | Icon + text + colour |
| --- | --- |
| Status indicator | Text label + colour |
| Link colour | Underline + colour |
| Graph legend | Patterns + labels + colour |

# Anti-patterns

- ***Low contrast text***: Gray-on-light or light-on-dark without checking ratios.
- ***Colour-only indicators***: Using red*green for pass*fail without text labels.
- ***Focus only on text***: UI components, borders and icons also need sufficient contrast.
- ***Assuming WCAG AA is enough***: Some users benefit from AAA ratios for normal text.

# Testing

1. Test all text elements with a contrast checker.
2. Test focus indicators, borders and icon contrast.
3. Simulate common colour blindness types (deuteranopia, protanopia, tritanopia).
4. Test in bright sunlight (high ambient light reduces perceived contrast).
5. Verify with a greyscale filter — all information should remain visible.

# Checklist

- [ ] Normal text meets 4.5:1 contrast ratio.
- [ ] Large text meets 3:1 contrast ratio.
- [ ] UI components and graphical objects meet 3:1 ratio.
- [ ] Colour is not the only means of conveying information.
- [ ] Focus indicators have sufficient contrast.
- [ ] Error states are indicated with icon and text.
- [ ] Tested with colour blindness simulation.

# Related Documents

- [Accessibility Glossary](../../glossary/accessibility/README.md)
- [Accessibility References](../../references/accessibility/README.md)
