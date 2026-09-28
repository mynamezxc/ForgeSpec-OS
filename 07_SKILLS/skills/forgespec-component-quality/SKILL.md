---
name: forgespec-component-quality
description: Uses isolated component states to improve design-system consistency, visual/state coverage, and interaction quality without confusing component tests with full E2E proof. Use for reusable UI systems and component-heavy products.
---

# ForgeSpec Component Quality

## Workflow
1. Identify reusable components and meaningful variants/states.
2. Represent realistic state combinations, not only the ideal example.
3. Include loading, empty, long content, disabled, invalid, error, permission, and responsive states where applicable.
4. Use Storybook or the repository's equivalent if already adopted or justified.
5. Add interaction/accessibility checks that are stable at component scope.
6. Detect visual regressions for high-value stable surfaces when the project has a trusted visual baseline.
7. Keep API/prop contracts aligned with the actual product implementation.

## Boundary
Component isolation proves component behavior and presentation. It does not prove routing, persistence, permissions, backend integration, or multi-step user journeys; those remain E2E/integration responsibilities.
