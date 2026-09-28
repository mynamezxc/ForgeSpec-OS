---
name: forgespec-ui-ux
description: Routes UI/UX design, implementation, critique, and polish through Product SPEC authority, real state coverage, accessibility, responsive behavior, and independent rendered verification. Use for any user-facing interface change.
---

# ForgeSpec UI/UX

## Objective
Build or review UI that is product-specific, usable, accessible, responsive, implementation-realistic, and verifiable in the running product.

## Process
1. Read the Product SPEC experience, users/jobs, design-system/brand rules, target platforms, and acceptance criteria.
2. Inspect the existing UI and design tokens/components before inventing a new system.
3. Define the primary user job, information hierarchy, interaction path, and required states.
4. For significant new design, create a small number of meaningfully different directions only when the Product SPEC leaves visual direction open. Select against product criteria, not novelty alone.
5. Implement using the repository's established system unless an approved change explicitly evolves it.
6. Cover realistic data: empty, minimal, dense, long text, localization expansion, loading, partial, error, permission-denied, destructive confirmation, success/recovery, and offline/degraded states when applicable.
7. Verify responsive behavior, keyboard/focus behavior, touch targets when relevant, content hierarchy, form recovery, and state continuity.
8. Render and inspect the actual implementation. Use a separate checker skill/provider for high-impact UI.
9. Fix findings in bounded batches, then re-verify.

## Optional providers
- maker: Anthropic frontend-design or Impeccable;
- engineering: Addy Osmani frontend-ui-engineering;
- checker: Vercel web-design-guidelines or Impeccable critique;
- runtime proof: Playwright/DevTools plus accessibility tooling.

Do not load all providers by default.

## Red flags
- generic dashboard/landing-page patterns unrelated to the user's job;
- new local styles when canonical components/tokens exist;
- attractive static screen with fake data and no real flow;
- missing non-happy states;
- desktop-only review;
- color/motion used without semantic purpose;
- inaccessible custom controls;
- redesigning a stable design system without a Product SPEC/ADR reason;
- polishing indefinitely after acceptance criteria are met.

## Exit evidence
- implemented or reviewed screens/routes/components;
- state and viewport coverage;
- accessibility checks applicable to the change;
- runtime interaction proof;
- resolved findings or explicitly accepted residual issues;
- requirement/evidence links.
