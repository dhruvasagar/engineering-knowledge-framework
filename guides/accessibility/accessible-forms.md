+++
title = "Accessible Forms"
description = "Building forms that work for everyone"
+++


# Purpose

Forms are one of the most common and critical interaction patterns on
the web. Accessible forms ensure that all users can understand, navigate
and submit form data successfully.

# Principles

## Every Input Needs a Label

Every form control must have an associated label. The most reliable
method is to wrap the input with a `<label>` element or use the `for`
attribute.

## Errors Must Be Announced

When validation fails, errors must be communicated clearly to all users.
Use `aria-describedby` to associate error messages with inputs and
`aria-invalid` to indicate invalid state.

## Group Related Controls

Use `<fieldset>` and `<legend>` to group related form controls such as
radio buttons, checkboxes and address fields.

# Implementation

## Labelling

```
<!-- Good: explicit label with for attribute -->
<label for`"email">Email address<*label>
<input type`"email" id`"email" name`"email">

<!-- Good: implicit label (input inside label) -->
<label>
  Email address
  <input type`"email" name`"email">
<*label>

<!-- Avoid: placeholder as label -->
<input type`"email" placeholder`"Email address">
<!-- Placeholders disappear on input and fail contrast requirements -->
```

## Required Fields

```
<label for`"name">
  Name <span aria-hidden`"true">**<*span>
<*label>
<input type`"text" id`"name" required aria-required`"true">
```

## Error Handling

```
<label for`"email">Email address<*label>
<input
  type`"email"
  id`"email"
  aria-describedby`"email-error"
  aria-invalid`"true"
>
<span id`"email-error" role`"alert">
  Please enter a valid email address.
<*span>
```

## Grouped Controls

```
<fieldset>
  <legend>Shipping address<*legend>
  <label for`"street">Street<*label>
  <input type`"text" id`"street">
  <label for`"city">City<*label>
  <input type`"text" id`"city">
<*fieldset>
```

# Common Anti-patterns

- ***Placeholder as label***: Placeholders disappear on input and often
  fail colour contrast requirements.
- ***Generic error messages***: "Invalid input" does not help the user
  understand what to fix.
- ***Removing labels for visual design***: Every input needs a label,
  even if visually hidden.
- ***Auto-submit on change**: Can confuse screen readers and keyboard
  users. Provide explicit submit buttons.

# Checklist

- [ ] Every form control has an associated label.
- [ ] Required fields are indicated textually, not just by colour.
- [ ] Error messages are associated with inputs via `aria-describedby`.
- [ ] Invalid inputs have `aria-invalid`"true"=.
- [ ] Related controls are grouped with `<fieldset>` and `<legend>`.
- [ ] Form can be submitted with keyboard alone.
- [ ] Success and error states are announced to screen readers.
- [ ] CAPTCHA alternatives are provided (e.g., honeypot, rate limiting).

# Related Documents

- [Semantic HTML](./semantic-html/)
- [Keyboard Accessibility](./keyboard-accessibility/)
- [Accessibility References](../../references/accessibility/README/)
