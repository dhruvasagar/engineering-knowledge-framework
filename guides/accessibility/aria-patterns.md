---
title: "ARIA Patterns"
description: "ARIA (Accessible Rich Internet Applications) provides attributes that enhance accessibility when native HTML elements are insufficient."
type: guide
capability: accessibility
status: published
tags: [aria, patterns]
last_reviewed: 2026-07-28
---

# Purpose

ARIA (Accessible Rich Internet Applications) provides attributes that
enhance accessibility when native HTML elements are insufficient. This
guide covers correct ARIA usage for common widget patterns.

# Principles

## First Rule of ARIA

Do not use ARIA if a native HTML element exists that provides the
semantics and behaviour you need. Semantic HTML is always preferred
over ARIA.

## No ARIA is Better than Bad ARIA

Incorrect ARIA can make content less accessible. Only add ARIA when
you fully understand its effects.

## ARIA Does Not Change Behaviour

ARIA only changes how assistive technologies present elements. It does
not add keyboard handling, focus management or event handling. You must
implement those separately.

# Common Patterns

## Tabs

```html
<div role`"tablist">
  <button role`"tab" aria-selected`"true" aria-controls`"panel1" id`"tab1">
    Tab 1
  <*button>
  <button role`"tab" aria-selected`"false" aria-controls`"panel2" id`"tab2">
    Tab 2
  <*button>
<*div>
<div role`"tabpanel" id`"panel1" aria-labelledby`"tab1">
  Content for tab 1
<*div>
<div role`"tabpanel" id`"panel2" aria-labelledby`"tab2" hidden>
  Content for tab 2
</div>
```

Keyboard: Arrow keys to switch tabs, Tab to move into tab panel.

## Dialog / Modal

```html
<div role`"dialog" aria-modal`"true" aria-labelledby`"dialog-title">
  <h2 id`"dialog-title">Confirm Action<*h2>
  <p>Are you sure?<*p>
  <button>Confirm<*button>
  <button>Cancel<*button>
<*div>
```

Keyboard: Tab cycles through dialog elements, Escape closes.

## Alert

```html
<div role`"alert">
  Your changes have been saved.
<*div>
```

Use `role="alert"` for time-sensitive information that should be
announced immediately. Do not use for persistent page content.

## Progress Bar

```html
<div role`"progressbar" aria-valuenow`"50" aria-valuemin`"0" aria-valuemax`"100">
  50% complete
</div>
```

# Landmark Roles

| ARIA Role            | HTML Equivalent | When to Use                           |
|----------------------|-----------------|---------------------------------------|
| role="banner"        | `<header>`      | Site-wide header (use once per page). |
| role="navigation"    | `<nav>`         | Navigation sections.                  |
| role="main"          | `<main>`        | Primary content (use once per page).  |
| role="complementary" | `<aside>`       | Supporting content.                   |
| role="contentinfo"   | `<footer>`      | Footer information.                   |
| role="form"          | `<form>`        | Form sections.                        |
| role="search"        | `<search>`      | Search functionality.                 |

# Anti-patterns

- ***Redundant ARIA***: Do not add `role="button"` to a `<button>` element.
- ***Missing focus management***: ARIA roles do not manage focus —
  implement it manually.
- ***aria-hidden misuse***: Do not hide focusable elements with
  `aria-hidden="true"` — this traps screen reader users.
- ***Overuse of role="application"***: This removes standard keyboard
  handling — use sparingly.

# Checklist

- [ ] Native HTML elements preferred over ARIA.
- [ ] ARIA roles, states and properties are used correctly.
- [ ] Keyboard handling is implemented for custom widgets.
- [ ] Focus management is implemented for dialogs and menus.
- [ ] `aria-hidden` is not applied to focusable elements.
- [ ] `aria-label` and `aria-labelledby` provide accessible names where needed.
- [ ] Dynamic content changes are announced with `aria-live` or `role="alert"`.

# Related Documents

- [Semantic HTML](./semantic-html.md)
- [Keyboard Accessibility](./keyboard-accessibility.md)
- [Accessibility References](../../references/accessibility/README.md)
