# Capability Activation Matrix

Use this at the start of each Product SPEC and coding session. Blank/inactive capabilities do not create implementation scope.

| Capability | Active? | Product SPEC reference | Main profile / skill to read |
|---|---:|---|---|
| User-facing UI / web UX |  |  | `04_QUALITY/03_UI_UX_AND_PRODUCT_VALIDATION.md` + `07_SKILLS/skills/forgespec-ui-ux/SKILL.md` |
| Accessibility target |  |  | `07_SKILLS/skills/forgespec-accessibility/SKILL.md` |
| Browser/E2E critical journeys |  |  | `07_SKILLS/skills/forgespec-browser-verification/SKILL.md` |
| Web performance / CWV / SEO |  |  | `07_SKILLS/skills/forgespec-web-quality/SKILL.md` |
| Component/design-system heavy UI |  |  | `07_SKILLS/skills/forgespec-component-quality/SKILL.md` |
| External agent skills/plugins |  |  | `07_SKILLS/04_SKILL_SECURITY_GATE.md` + `forgespec-skill-inspector` |
| Security-sensitive/public attack surface |  |  | `03_ENGINEERING/05_SECURITY_PRIVACY_AND_PERMISSION_BASELINE.md` + `forgespec-security-review` |
| Dependency/container/CI supply chain |  |  | `07_SKILLS/skills/forgespec-supply-chain/SKILL.md` |
| AI/LLM/agent security |  |  | `03_ENGINEERING/11_AI_AGENT_TOOLING_PROFILE.md` + `forgespec-ai-security` |
| Offline/unreliable network |  |  | `03_ENGINEERING/06_OFFLINE_DISTRIBUTED_AND_HARDWARE_CAPABILITY.md` |
| Local hardware/devices |  |  | same profile |
| AI agents/tools/connectors |  |  | `03_ENGINEERING/11_AI_AGENT_TOOLING_PROFILE.md` |
| Multi-tenant |  |  | security/data rules |
| Public API/events |  |  | data/API/event rules |
| High-risk migrations |  |  | DB migration rules |
| High concurrency |  |  | reliability/concurrency rules |
| Financial/accounting |  |  | Product SPEC must define precision, audit, reversal |
| High availability |  |  | Product SPEC must define topology/SLO/failover |

## Skill activation note

A capability being active does **not** mean every listed third-party provider must be installed. Route the minimum provider set through `07_SKILLS/01_SKILL_ROUTER.md`. Existing project tooling may satisfy the capability when it produces equivalent evidence.
