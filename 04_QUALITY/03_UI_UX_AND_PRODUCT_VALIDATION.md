# UI/UX and Product Validation

## Validate complete states
For applicable screens/components, verify:
- initial/loading;
- success;
- empty;
- validation error;
- server/network error;
- partial/degraded;
- unauthorized/forbidden;
- disabled/read-only;
- long content/large data;
- responsive behavior.

## Flow validation
Critical workflows should be validated from entry point to outcome, not screen-by-screen in isolation.

## Admin/operator UX
Production software often fails because only end-user UI is designed. If the Product SPEC needs administration, support, moderation, configuration or diagnostics, verify those flows with the same seriousness.

## Accessibility baseline
Where relevant: semantic structure, keyboard navigation, focus behavior, labels, readable error messages and contrast. Follow Product SPEC/regional requirements for stricter conformance.

## Design consistency
Reuse product design tokens/components/patterns. Do not introduce one-off styling that fragments the interface without reason.

## ForgeSpec skill integration

For significant user-facing changes, route through `07_SKILLS/skills/forgespec-ui-ux/SKILL.md`. Use external maker/checker providers only when they add value. Existing Product SPEC design systems have authority over generic design-skill defaults. Runtime verification and accessibility evidence remain separate from aesthetic review.
