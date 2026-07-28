# Purpose

Screen reader testing is essential for verifying that content and
interactions are accessible to users who rely on assistive technology.
Automated checks catch ~30% of issues — screen reader testing catches
the rest.

# Screen Readers

| Screen Reader | Platform | Browser | Notes |
| --- | --- | --- | --- |
+---------------+---------------+---------------+---------------+------------------------------+
| VoiceOver | macOS, iOS | Safari | Built into Apple devices. |
| --- | --- | --- | --- |
| NVDA | Windows | Firefox | Free, most common on Windows. |
| JAWS | Windows | Chrome, Edge | Paid, widely used in enterprise. |
| TalkBack | Android | Chrome | Built into Android devices. |
| ChromeVox | ChromeOS | Chrome | Built into Chromebooks. |

# Testing Workflow

## Step 1: Navigate by Headings

1. Open the page and navigate by headings only.
2. Is the heading hierarchy logical?
3. Can you understand the page structure from headings alone?
4. Are there any missing or misleading headings?

## Step 2: Navigate by Landmarks

1. Navigate by landmark regions.
2. Are all major sections identified as landmarks?
3. Is the navigation order logical?

## Step 3: Navigate by Links

1. Navigate by links only.
2. Is every link description meaningful out of context?
3. Are there empty or duplicate links?
4. Are there "click here" or "read more" links?

## Step 4: Interactive Elements

1. Tab through all interactive elements.
2. Is each element announced correctly (role, name, state)?
3. Can you operate all functionality?
4. Are custom widgets announced correctly?

## Step 5: Forms

1. Navigate to each form control.
2. Is the label announced correctly?
3. Are required fields indicated?
4. Submit with errors — are errors announced?
5. Is the success message announced?

## Step 6: Dynamic Content

1. Trigger dynamic content updates.
2. Is new content announced (via `aria-live` or `role`"alert"=)?
3. Does focus move correctly after dynamic updates?

# Common Issues Found by Screen Reader Testing

| Issue | How to Detect |
| --- | --- |
+--------------------------------+----------------------------------------+
| Missing or incorrect labels | Tab to input, no label announced. |
| --- | --- |
| Unlabelled buttons | Navigate buttons, hear "button" only. |
| Missing heading structure | Navigate headings, no structure. |
| No landmark regions | Navigate landmarks, none found. |
| Unannounced dynamic content | Trigger update, no announcement. |
| Focus not managed | Open dialog, focus not inside. |
| Keyboard trap | Tab into widget, cannot tab out. |

# Checklist

- [ ] Navigate by headings — structure is logical.
- [ ] Navigate by landmarks — all regions identified.
- [ ] Navigate by links — all descriptions meaningful.
- [ ] Tab through all interactive elements — all operable.
- [ ] Forms have correct label announcements.
- [ ] Errors announced and associated with inputs.
- [ ] Dynamic content changes announced.
- [ ] Dialogs and modals manage focus correctly.
- [ ] No keyboard traps.
- [ ] Tested with at least two screen reader/browser combinations.

# Related Documents

- [Semantic HTML](./semantic-html.md)
- [Keyboard Accessibility](./keyboard-accessibility.md)
- [ARIA Patterns](./aria-patterns.md)
- [Accessibility Review Playbook](../../playbooks/accessibility-review/README.md)
