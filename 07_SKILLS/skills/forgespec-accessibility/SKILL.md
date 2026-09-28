---
name: forgespec-accessibility
description: Audits and verifies accessibility using automated WCAG-oriented tooling plus manual interaction checks that automation cannot prove. Use for user-facing UI, forms, navigation, dialogs, and release accessibility gates.
---

# ForgeSpec Accessibility

## Workflow
1. Resolve Product SPEC accessibility target and supported platforms/assistive technology assumptions.
2. Run automated checks with axe-core or an approved equivalent in representative rendered states.
3. Verify keyboard-only flow for critical tasks: focus order, focus visibility, traps, escape/close behavior, and skip/navigation behavior as applicable.
4. Verify semantics and accessible names/relationships for interactive controls.
5. Verify form labels, instructions, validation, error recovery, and status announcements.
6. Check contrast, zoom/reflow, touch target constraints, reduced motion, and content resizing when relevant.
7. Check dynamic content and dialogs after state transitions, not only initial page load.
8. Record items requiring manual assistive-technology validation for the project's risk/requirements.

## Rules
- Automated tools can detect many problems but cannot prove full conformance.
- Do not suppress a rule solely to make a report green. Document legitimate exceptions.
- Do not add ARIA where semantic native HTML already expresses the behavior correctly.
- Accessibility regressions in release-critical tasks block the relevant gate according to Product SPEC severity.
