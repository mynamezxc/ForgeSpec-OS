# Curated GitHub Skills and Tools

**Research snapshot:** 2026-09-28. Re-verify upstream state before adopting or upgrading.

This registry is intentionally curated. Popularity is not sufficient; selection favors active maintenance, evidence quality, fit with coding agents, portability, and complementary roles.

## UI/UX and design

### Anthropic frontend-design
- Repository: `https://github.com/anthropics/claude-code` (frontend-design plugin/skill) and related Anthropic skills repositories.
- Role: distinctive visual direction and intentional frontend design.
- ForgeSpec use: optional **maker** for new UI or major visual redesign.
- Guardrail: never override an established product design system, accessibility requirement, or Product SPEC brand rule.

### pbakaus/impeccable
- Repository: `https://github.com/pbakaus/impeccable`
- Role: design critique, anti-generic patterns, polish, bounded browser iteration, deterministic detectors.
- ForgeSpec use: optional maker/checker for high-visibility UI.
- Guardrail: do not let aesthetic ambition increase interaction complexity or violate product density, performance, or accessibility goals.

### vercel-labs/agent-skills — web-design-guidelines
- Repository: `https://github.com/vercel-labs/agent-skills`
- Role: UI review against a broad set of interface, accessibility, form, interaction, typography, state, and performance practices.
- ForgeSpec use: preferred **checker** for web UI review.
- Guardrail: Product SPEC decisions win when a guideline is stylistic rather than correctness-related.

### addyosmani/agent-skills — frontend-ui-engineering
- Repository: `https://github.com/addyosmani/agent-skills`
- Role: production UI engineering, responsive behavior, accessibility, state and component discipline.
- ForgeSpec use: implementation-oriented UI skill, especially when design and engineering must meet.

## Web quality, accessibility, and performance

### addyosmani/web-quality-skills
- Repository: `https://github.com/addyosmani/web-quality-skills`
- Role: measurement-first web quality, Lighthouse, Core Web Vitals, accessibility, SEO, best practices.
- ForgeSpec use: primary web-quality audit provider.
- Key principle adopted by ForgeSpec: keep field data, first-party RUM, controlled lab measurements, and static inspection as distinct evidence classes.

### GoogleChrome/lighthouse
- Repository: `https://github.com/GoogleChrome/lighthouse`
- Role: reproducible browser lab audits for web quality categories.
- ForgeSpec use: measurement provider, not a substitute for field telemetry.

### dequelabs/axe-core
- Repository: `https://github.com/dequelabs/axe-core`
- Role: automated accessibility engine with WCAG rule coverage.
- ForgeSpec use: automate accessibility checks inside browser tests.
- Guardrail: automated checks are incomplete by design; keyboard, focus, semantics, reading order, and task usability may still require manual verification.

## Browser, E2E, and component testing

### microsoft/playwright
- Repository: `https://github.com/microsoft/playwright`
- Role: cross-browser E2E, browser automation, traces, screenshots, isolated contexts; current project also exposes agent-oriented CLI/MCP workflows.
- ForgeSpec use: preferred default for new web E2E unless the Product SPEC/repository standard chooses otherwise.

### storybookjs/storybook
- Repository: `https://github.com/storybookjs/storybook`
- Role: isolated component development, documentation, state coverage, interaction and visual workflows.
- ForgeSpec use: conditional for component-heavy products and design systems.
- Guardrail: stories do not replace real end-to-end flows.

### obra/superpowers
- Repository: `https://github.com/obra/superpowers`
- Role: process skills including TDD, verification-before-completion, subagent workflows, and pressure-testing skills.
- ForgeSpec use: methodology reference for **testing ForgeSpec skills themselves**, especially RED/GREEN/REFACTOR pressure scenarios.
- Guardrail: ForgeSpec precedence, task model, and Product SPEC authority remain canonical in ForgeSpec-managed projects.

## Static analysis and application security

### semgrep/semgrep and semgrep/skills
- Repositories: `https://github.com/semgrep/semgrep`, `https://github.com/semgrep/skills`
- Role: pattern-based static analysis across many languages; agent-oriented Semgrep skill exists upstream.
- ForgeSpec use: targeted SAST and project-specific guardrails.
- Guardrail: Community Edition limitations mean a clean result cannot be treated as complete interprocedural security proof.

### zaproxy/zaproxy
- Repository: `https://github.com/zaproxy/zaproxy`
- Role: dynamic web application scanning and manual security testing support.
- ForgeSpec use: staging/local DAST for web products.
- Guardrail: active scanning must remain inside explicitly authorized targets and environments.

### projectdiscovery/nuclei
- Repository: `https://github.com/projectdiscovery/nuclei`
- Role: template-driven vulnerability detection across HTTP and other protocols.
- ForgeSpec use: conditional, primarily for owned/authorized infrastructure and regression checks for known classes.
- Guardrail: pin templates/tool version where reproducibility matters; review template behavior; never turn broad internet scanning into a default ForgeSpec action.

## Dependency, container, configuration, and secret security

### google/osv-scanner
- Repository: `https://github.com/google/osv-scanner`
- Role: dependency vulnerability matching using OSV data, multiple ecosystems, container support, guided remediation.
- ForgeSpec use: preferred dependency-focused SCA provider where supported.

### aquasecurity/trivy
- Repository: `https://github.com/aquasecurity/trivy`
- Role: repository, filesystem, image, vulnerability, misconfiguration, secret and license scanning.
- ForgeSpec use: broad supply-chain/container/configuration coverage.
- Guardrail: pin and verify releases. Scanner tooling is part of the supply chain and must itself be treated as a dependency.

## Agent-skill and AI/LLM security

### NVIDIA/SkillSpector
- Repository: `https://github.com/NVIDIA/SkillSpector`
- Role: static/semantic security review of agent skills for prompt injection, data exfiltration, excessive agency, risky scripts, MCP/tool issues, and supply-chain concerns.
- ForgeSpec use: preferred pre-install gate for external skills when available.

### NVIDIA/garak
- Repository: `https://github.com/NVIDIA/garak`
- Role: adversarial probing and vulnerability assessment for LLM applications/models.
- ForgeSpec use: conditional AI/LLM security profile only.

## Not bundled

ForgeSpec OS does not vendor the upstream repositories or copy their full skills. This avoids stale forks, license confusion, context bloat, and silent behavior drift. ForgeSpec provides:

- routing;
- activation criteria;
- evidence contracts;
- trust/supply-chain gates;
- compatibility and precedence rules;
- provider-neutral fallbacks.

Projects may install approved upstream providers separately and pin them in their own toolchain lock or infrastructure definition.
