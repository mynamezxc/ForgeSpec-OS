---
name: forgespec-web-quality
description: Measures and improves web performance, Core Web Vitals, browser quality, and related SEO/best-practice signals using explicit field, lab, and static evidence classes. Use for web quality audits or regressions.
---

# ForgeSpec Web Quality

## Principle
Measure first. Keep field evidence, first-party RUM, controlled lab runs, and static inspection distinct.

## Process
1. Resolve Product SPEC budgets/SLOs and critical routes.
2. Record environment/build mode/device/network/cache conditions.
3. Use field data or first-party RUM when available to prioritize real user impact.
4. Reproduce with controlled lab tooling such as Lighthouse/DevTools when diagnosis is needed.
5. Inspect network, main-thread work, rendering, assets, caching, server timing, and route-specific bottlenecks.
6. Form a concrete hypothesis tied to a metric.
7. Implement the smallest architecture-compatible fix.
8. Re-measure under comparable conditions.
9. Check for functional, visual, SEO, accessibility, cost, or cache-correctness regressions.
10. Store before/after evidence and variance notes.

## Preferred providers
- Addy Osmani web-quality-skills for measurement workflow;
- Lighthouse/Chrome tooling for controlled lab evidence;
- Product RUM/observability for field evidence.

## Rules
- Do not present one local run as population-level user experience.
- Do not optimize a Lighthouse number by breaking functionality or semantics.
- Do not add complexity for a micro-optimization that is below measurement noise.
- Do not claim improvement without comparable before/after evidence.
