# Provider Setup and Adapter Recipes

ForgeSpec OS does not auto-install external skills. Installation changes agent behavior and may execute third-party scripts, so provider adoption is an explicit engineering task.

## Safe adoption sequence

1. Select the capability from `01_SKILL_ROUTER.md`.
2. Check whether the repository already has an equivalent tool or skill.
3. Review the upstream repository and current installation instructions.
4. Pass `04_SKILL_SECURITY_GATE.md`.
5. Choose and record an exact release/tag/commit for production work.
6. Install in the narrowest project/workspace scope that satisfies the need.
7. Run `05_SKILL_EVALUATION_AND_PRESSURE_TESTING.md` for high-impact behavior skills.
8. Record the provider in the Product SPEC `SKILL_AND_TOOL_ACTIVATION_PLAN.md` or equivalent project record.
9. Add CI/release integration only after local evidence is stable.

## UI/UX adapters

### Anthropic frontend-design
Use as a visual-direction maker when the Product SPEC leaves meaningful design freedom. If the project already has a design system, constrain the skill to that system rather than allowing a new visual language to emerge accidentally.

### Impeccable
Use for high-value design creation or critique with bounded browser iteration. Keep a hard exit condition based on Product SPEC acceptance criteria; do not create open-ended polish loops.

### Vercel web-design-guidelines
Use primarily as a checker. A common upstream installation path is through the Agent Skills/skills CLI ecosystem; always verify the current upstream command and pin/review the acquired source before production use.

### Addy Osmani frontend-ui-engineering
Use when UI implementation quality, state handling, responsive behavior, and accessibility engineering are the primary problem rather than pure visual exploration.

## Browser and web-quality adapters

### Playwright
Choose one integration mode according to the repository:

- Playwright Test for committed E2E suites;
- Playwright CLI for agent-driven browser automation where appropriate;
- Playwright MCP when the agent runtime supports MCP and policy allows it;
- Playwright library for custom automation infrastructure.

Pin package versions through the project's package manager for reproducible CI. Do not rely on a floating `latest` version in release gates.

### axe-core
Prefer integration inside existing browser tests so accessibility regressions fail close to the affected feature. Keep manual interaction checks for critical paths.

### Storybook
Adopt only when isolated component/state development has meaningful value. Do not add Storybook to a small product merely because it is available.

### Web Quality Skills / Lighthouse
Use web-quality skills as an orchestration layer and Lighthouse/DevTools as evidence providers. Record whether each result is field, RUM, lab, or static evidence.

## Security adapters

### Semgrep
Use repository-native configuration where it exists. Add targeted rulesets for changed attack surfaces rather than enabling every rule and drowning the project in noise. Pin CI tooling and preserve rule/config version where release reproducibility matters.

### OSV-Scanner
Use for dependency-focused SCA across supported ecosystems. Scan lockfiles/source manifests and record remediation decisions rather than blindly applying upgrades that can break the product.

### Trivy
Use when repository, image, configuration, secret, or license coverage is needed. Treat Trivy itself as a supply-chain dependency: pin a reviewed release, monitor advisories, and avoid unreviewed plugin execution.

### ZAP
Prefer local/staging automation for owned applications. Configure authentication context carefully for private routes and preserve non-production safety controls. Active scanning of third-party systems is outside the default ForgeSpec workflow.

### Nuclei
Use as a conditional regression/discovery provider for known vulnerability classes on explicitly authorized targets. Pin tool/templates for release reproducibility and review template behavior before running high-impact templates.

### NVIDIA SkillSpector
Use before enabling unfamiliar external skills, especially those with scripts, broad tool access, MCP integration, or network behavior. A clean scan is supportive evidence, not a replacement for source/permission review.

### NVIDIA garak
Use only for activated AI/LLM products. Build project-specific adversarial tests first; use garak to broaden coverage, not to replace product threat modeling.

## Cross-runtime portability

ForgeSpec's local `SKILL.md` files are provider-neutral. Runtime-specific install paths (Codex, Claude Code, Cursor, Copilot, Gemini CLI, etc.) belong in the project/tooling configuration, not in ForgeSpec's global product rules.

If a runtime cannot load a provider directly, translate only the required capability into that runtime's supported skill/plugin mechanism while preserving:

- pinned source identity;
- permission restrictions;
- Product SPEC authority;
- ForgeSpec evidence contract;
- removal/rollback path.
