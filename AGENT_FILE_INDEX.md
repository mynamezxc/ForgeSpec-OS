# ForgeSpec OS Agent File Index

This index is optimized for selective loading. Do not read every file on every task. Start with `AGENT_ENTRYPOINT.md`, identify the active risk/capability, then load only the rules that materially affect the current work.

## Root control files

| File | When to read | Purpose |
|---|---|---|
| `AGENT_ENTRYPOINT.md` | Always first | Machine-oriented root directive, precedence, execution, completion, context, testing, and stop semantics. |
| `CAPABILITY_ACTIVATION_MATRIX.md` | Session/spec start | Activates only conditional profiles justified by the Product SPEC. |
| `AGENT_START_PROMPT.md` | Starting or resuming implementation | Compact execution prompt for a coding agent. |
| `PROMPT_BUILD_PRODUCT_SPEC.md` | Creating a Product SPEC | Converts product intent into an implementation-grade production SPEC. |
| `forgespec-policy.json` | Tooling/automation integration | Machine-readable stable policy metadata. |
| `FORGESPEC_OS_REVIEW_CHECKLIST.md` | Editing ForgeSpec OS itself | Prevents global-rule pollution and unnecessary bureaucracy. |
| `README.md` | Human/public overview only | GitHub overview, architecture, strengths, modeled benchmarks, and quick start. Do not use as the primary agent instruction file. |

## 00_GOVERNANCE — always relevant to completion or conflicts

- `00_GOVERNANCE/01_PRECEDENCE_SCOPE_AND_CONFLICTS.md` — authority order, product-vs-process boundaries, conflict isolation, blast-radius obligation.
- `00_GOVERNANCE/02_STATUS_STOP_AND_CONTINUATION_RULES.md` — valid task states and legitimate stop conditions.
- `00_GOVERNANCE/03_DEFINITION_OF_DONE.md` — evidence-based completion semantics.
- `00_GOVERNANCE/04_PRODUCTION_READINESS_GATES.md` — release-level readiness gates.
- `00_GOVERNANCE/05_RULE_CLASSIFICATION.md` — invariant/default/conditional-profile classification.
- `00_GOVERNANCE/06_ANTI_FAKE_DONE_AND_ANTI_HARDCODE.md` — detects UI-only, hardcoded, mocked, stubbed, or disconnected false completion.
- `00_GOVERNANCE/07_PROJECT_GOAL_AND_TERMINAL_STATE.md` — mandatory Project Goal, terminal predicate, scope enumeration, and known-remaining-work guard.

## 01_AGENT_RUNTIME — load by execution need

- `01_AGENT_RUNTIME/01_EXECUTION_PROTOCOL.md` — end-to-end coding execution loop.
- `01_AGENT_RUNTIME/02_SUBAGENT_ORCHESTRATION.md` — delegation packets, ownership, return evidence, integration authority.
- `01_AGENT_RUNTIME/03_TASK_GRAPH_AND_WORK_MANAGEMENT.md` — requirement/task graph and task-state management.
- `01_AGENT_RUNTIME/04_CONTEXT_COMPRESSION_AND_RECOVERY.md` — checkpointing, compression, deterministic rehydration.
- `01_AGENT_RUNTIME/05_DECISION_LOG_CHANGE_CONTROL.md` — durable decisions and controlled requirement/architecture changes.
- `01_AGENT_RUNTIME/06_CONTEXT_BUDGET_AND_TOKEN_ECONOMY.md` — selective context loading and token discipline.
- `01_AGENT_RUNTIME/07_PARALLEL_WORK_AND_GIT_DISCIPLINE.md` — parallel ownership and integration conflict control.
- `01_AGENT_RUNTIME/08_FAILURE_ESCALATION_AND_RECOVERY.md` — recoverable failure, blockers, escalation, and continued unaffected work.
- `01_AGENT_RUNTIME/09_ACTION_BIAS_AND_PLANNING_BUDGET.md` — prevents endless planning and repeated redesign.
- `01_AGENT_RUNTIME/10_AUTONOMOUS_CONTINUATION_CONTROLLER.md` — executable post-task/post-milestone continuation loop and blocker classification.

## 02_SPEC_FACTORY — load when generating or materially revising a Product SPEC

- `02_SPEC_FACTORY/01_PRODUCT_SPEC_GENERATION_WORKFLOW.md`
- `02_SPEC_FACTORY/02_SELF_CRITIQUE_AND_DESIGN_REVIEW.md`
- `02_SPEC_FACTORY/03_REALITY_BENCHMARK_PROTOCOL.md`
- `02_SPEC_FACTORY/04_PRODUCT_SPEC_REQUIRED_STRUCTURE.md`
- `02_SPEC_FACTORY/05_BUSINESS_LOGIC_SPEC_METHOD.md`
- `02_SPEC_FACTORY/06_REQUIREMENT_QUALITY_LINT.md`
- `02_SPEC_FACTORY/07_CAPABILITY_PROFILE_SELECTION.md`
- `02_SPEC_FACTORY/08_SPEC_FREEZE_AND_CHANGE_MANAGEMENT.md`
- `02_SPEC_FACTORY/09_RELEASE_GOAL_AND_SCOPE_CLOSURE.md`

## 03_ENGINEERING — load by implementation surface

- `03_ENGINEERING/01_ARCHITECTURE_AND_MODULARITY.md`
- `03_ENGINEERING/02_CODING_AGENT_IMPLEMENTATION_RULES.md`
- `03_ENGINEERING/03_DEPENDENCY_AND_THIRD_PARTY_POLICY.md`
- `03_ENGINEERING/04_DATA_API_EVENT_AND_IDEMPOTENCY.md`
- `03_ENGINEERING/05_SECURITY_PRIVACY_AND_PERMISSION_BASELINE.md`
- `03_ENGINEERING/06_OFFLINE_DISTRIBUTED_AND_HARDWARE_CAPABILITY.md` — conditional profile only.
- `03_ENGINEERING/07_FRONTEND_BACKEND_AUTHORITY_BOUNDARIES.md`
- `03_ENGINEERING/08_CONFIG_FLAGS_AND_ENVIRONMENT.md`
- `03_ENGINEERING/09_DATABASE_SCHEMA_AND_MIGRATION_RULES.md`
- `03_ENGINEERING/10_RELIABILITY_TIMEOUT_RETRY_AND_CONCURRENCY.md`
- `03_ENGINEERING/11_AI_AGENT_TOOLING_PROFILE.md` — conditional profile only.

## 04_QUALITY — load by test/release risk

- `04_QUALITY/01_TEST_STRATEGY_AND_CADENCE.md`
- `04_QUALITY/02_TESTER_AND_VERIFIER_WORKFLOW.md`
- `04_QUALITY/03_UI_UX_AND_PRODUCT_VALIDATION.md`
- `04_QUALITY/04_PERFORMANCE_CAPACITY_AND_COST_VALIDATION.md`
- `04_QUALITY/05_RELEASE_ACCEPTANCE_CHECKLIST.md`
- `04_QUALITY/06_TEST_DATA_AND_ENVIRONMENT_MANAGEMENT.md`
- `04_QUALITY/07_E2E_STABILITY_AND_MAINTENANCE.md`
- `04_QUALITY/08_SECURITY_TEST_BASELINE.md`
- `04_QUALITY/09_EVIDENCE_LEDGER_AND_COMPLETION_AUDIT.md`
- `04_QUALITY/10_AGENT_BEHAVIOR_REGRESSION_TESTS.md` — pressure tests for false termination, scope collapse, blocker misuse, and forced-boundary recovery.

## 05_OPERATIONS — load when the Product SPEC makes the concern applicable

- `05_OPERATIONS/01_OBSERVABILITY_AND_DEBUGGABILITY.md`
- `05_OPERATIONS/02_DEPLOYMENT_MIGRATION_ROLLBACK.md`
- `05_OPERATIONS/03_INCIDENT_AND_PRODUCTION_FEEDBACK_LOOP.md`
- `05_OPERATIONS/04_RUNBOOK_SUPPORT_AND_ADMIN.md`
- `05_OPERATIONS/05_VERSIONING_RELEASE_NOTES_AND_UPGRADES.md`

## 06_TEMPLATES — instantiate only when needed

- `06_TEMPLATES/ADR_TEMPLATE.md`
- `06_TEMPLATES/BUG_REPORT_TEMPLATE.md`
- `06_TEMPLATES/CHECKPOINT_TEMPLATE.md`
- `06_TEMPLATES/EVIDENCE_LEDGER_TEMPLATE.md`
- `06_TEMPLATES/REQUIREMENT_COVERAGE_MATRIX.md`
- `06_TEMPLATES/REQUIREMENT_TEMPLATE.md`
- `06_TEMPLATES/TASK_TEMPLATE.md`
- `06_TEMPLATES/PROJECT_GOAL_TEMPLATE.md`
- `06_TEMPLATES/EXECUTION_STATE_TEMPLATE.md`

## 07_SKILLS — task-scoped specialist capabilities

Start with `07_SKILLS/01_SKILL_ROUTER.md`; do not load this whole directory by default.

- `07_SKILLS/00_SKILL_SYSTEM_OVERVIEW.md` — provider-neutral skill architecture and authority boundaries.
- `07_SKILLS/01_SKILL_ROUTER.md` — maps task signals to the minimum applicable skill set.
- `07_SKILLS/02_CURATED_GITHUB_SKILLS.md` — researched upstream providers for UI/UX, quality, testing, and security.
- `07_SKILLS/03_INSTALL_PIN_UPDATE_POLICY.md` — reproducible install, pinning, upgrade, and rollback rules.
- `07_SKILLS/04_SKILL_SECURITY_GATE.md` — provenance, instruction, script, permission, and supply-chain review before external skill activation.
- `07_SKILLS/05_SKILL_EVALUATION_AND_PRESSURE_TESTING.md` — behavioral evaluation for skills using pressure scenarios.
- `07_SKILLS/06_SKILL_CONFLICT_AND_PRECEDENCE.md` — resolves skill conflicts without changing product authority.
- `07_SKILLS/07_EVIDENCE_AND_HANDOFF_CONTRACT.md` — required result packet for significant skill invocations.
- `07_SKILLS/08_PROVIDER_SETUP_AND_ADAPTERS.md` — safe adoption patterns for curated providers without automatic unpinned installation.
- `07_SKILLS/skills/forgespec-ui-ux/SKILL.md` — UI/UX maker/checker workflow.
- `07_SKILLS/skills/forgespec-web-quality/SKILL.md` — measurement-first performance/web-quality workflow.
- `07_SKILLS/skills/forgespec-browser-verification/SKILL.md` — deterministic real-browser/E2E verification.
- `07_SKILLS/skills/forgespec-accessibility/SKILL.md` — automated + manual accessibility verification.
- `07_SKILLS/skills/forgespec-component-quality/SKILL.md` — isolated component/state coverage.
- `07_SKILLS/skills/forgespec-security-review/SKILL.md` — threat-led SAST/DAST application security review.
- `07_SKILLS/skills/forgespec-supply-chain/SKILL.md` — dependency/container/configuration/secret risk.
- `07_SKILLS/skills/forgespec-ai-security/SKILL.md` — conditional AI/LLM threat and adversarial evaluation.
- `07_SKILLS/skills/forgespec-skill-inspector/SKILL.md` — third-party skill pre-install gate.
- `07_SKILLS/skills/forgespec-release-verifier/SKILL.md` — final evidence-oriented release verification.
- `07_SKILLS/skill-registry.json` — machine-readable upstream provider registry.
- `07_SKILLS/scripts/validate_skill_system.py` — read-only standard-library validator for local skill metadata and registry/version integrity.


## 08_FAILURE_PATTERNS — load only when diagnosing agent-control regressions

- `08_FAILURE_PATTERNS/01_PARTIAL_SLICE_FALSE_TERMINATION.md` — post-task false-terminal pattern and behavioral regression test.
- `08_FAILURE_PATTERNS/02_SCOPE_COLLAPSE_TO_REPRESENTATIVE_VARIANT.md` — prevents one representative industry/channel/module from replacing an explicit multi-variant release scope.
