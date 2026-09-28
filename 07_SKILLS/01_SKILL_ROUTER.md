# Skill Router

Use this router after resolving the active task, acceptance criteria, and risk.

## Routing table

| Task signal | Primary ForgeSpec skill | Optional specialist providers | Required evidence class |
|---|---|---|---|
| New or substantially redesigned UI | `07_SKILLS/skills/forgespec-ui-ux/SKILL.md` | Anthropic frontend-design, Impeccable, Addy Osmani frontend-ui-engineering | rendered states + responsive review + interaction proof |
| UI review / polish | `07_SKILLS/skills/forgespec-ui-ux/SKILL.md` | Vercel web-design-guidelines, Impeccable | issue list tied to files/screens + resolved proof |
| Web performance / CWV / SEO / browser quality | `07_SKILLS/skills/forgespec-web-quality/SKILL.md` | Addy Osmani web-quality-skills, Lighthouse | measured lab/field evidence with environment |
| Accessibility | `07_SKILLS/skills/forgespec-accessibility/SKILL.md` | axe-core, Playwright + axe, web-quality accessibility skill | automated results + manual keyboard/semantic checks where relevant |
| Browser E2E / real runtime verification | `07_SKILLS/skills/forgespec-browser-verification/SKILL.md` | Playwright Test/CLI/MCP, Chrome DevTools workflow | trace/screenshot/log/network/test result |
| Component isolation / state matrix | `07_SKILLS/skills/forgespec-component-quality/SKILL.md` | Storybook | representative stories/states + tests |
| Static security review | `07_SKILLS/skills/forgespec-security-review/SKILL.md` | Semgrep, language-native linters, optional CodeQL | findings triaged by exploitability and reachability |
| Dependency/container/secret risk | `07_SKILLS/skills/forgespec-supply-chain/SKILL.md` | OSV-Scanner, Trivy | lockfile/image/repo scan + remediation decision |
| Runtime web security | `07_SKILLS/skills/forgespec-security-review/SKILL.md` | ZAP; Nuclei only when authorized and appropriate | scoped scan report + manual validation of significant findings |
| AI/LLM feature security | `07_SKILLS/skills/forgespec-ai-security/SKILL.md` | NVIDIA garak, project-specific adversarial evals | prompt/tool/data boundary eval report |
| Installing/updating an external agent skill | `07_SKILLS/skills/forgespec-skill-inspector/SKILL.md` | NVIDIA SkillSpector + manual source review | provenance + permission + script + version gate |
| Release acceptance | `07_SKILLS/skills/forgespec-release-verifier/SKILL.md` | all applicable evidence providers | coverage matrix + unresolved-risk statement |

## Selection rules

1. Activate the **minimum** set of skills that covers the task.
2. Prefer one maker skill and one checker skill over several overlapping maker skills.
3. Do not run three design-generation skills sequentially and average their opinions.
4. Do not run all security scanners on every edit. Match scanner type to changed attack surface.
5. A tool result is not automatically a defect. Triage false positives, exploitability, reachability, and product context.
6. A clean scanner result is not proof of absence. Maintain manual review for logic, authorization, trust boundaries, and business abuse cases.
7. For UI tasks, existing Product SPEC design tokens and established repository design systems have higher authority than third-party aesthetic defaults.
8. For performance, measure before and after. Static guesses do not count as measured improvement.
9. For external skills, pass `04_SKILL_SECURITY_GATE.md` before first activation and after material upstream changes.

## Context budget

Use a small skill packet:

- current requirement/task;
- relevant Product SPEC section;
- affected files/screens/contracts;
- acceptance criteria;
- one primary skill;
- only the references required by that skill;
- previous evidence if this is a verification pass.

Do not load the full external skill catalog into the main context.
