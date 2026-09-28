# Dependency and Third-Party Policy

Add a dependency only when it provides clear value over a simple native implementation.

## Evaluate before adding
- maintenance activity;
- license fit;
- security history;
- transitive dependency size;
- runtime footprint;
- lock-in/replacement cost;
- offline/self-host requirements;
- version compatibility;
- API stability.

## Critical integrations
Wrap external providers behind product-owned interfaces when multiple providers, future replacement or failure isolation are realistic needs.

## Version discipline
Pin/lock dependencies appropriately for the ecosystem. Record upgrade strategy for security-critical/runtime-critical packages.

## Do not over-abstract
A single stable provider does not automatically require a multi-provider framework. Add abstraction when a concrete variability requirement exists.

## Agent skills and scanner tooling are dependencies

External agent skills, MCP/plugin packages, scanners, and generated install scripts follow the same provenance and lifecycle discipline as code dependencies. Before activation, follow `07_SKILLS/04_SKILL_SECURITY_GATE.md`; for production work, pin approved versions/commits and update intentionally using `07_SKILLS/03_INSTALL_PIN_UPDATE_POLICY.md`.
