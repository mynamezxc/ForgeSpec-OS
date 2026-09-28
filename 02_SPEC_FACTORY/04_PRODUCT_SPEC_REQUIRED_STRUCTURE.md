# Required Product SPEC Structure

A strong Product SPEC folder should normally contain:
```text
SPEC/<product>/
  PRODUCT_SPEC_ENTRYPOINT.md
  00_VISION/
    PRODUCT_GOALS.md
    USERS_AND_JOBS.md
    SCOPE_AND_NON_GOALS.md
    SUCCESS_METRICS.md
  01_REQUIREMENTS/
    FUNCTIONAL_REQUIREMENTS.md
    NON_FUNCTIONAL_REQUIREMENTS.md
    PERMISSIONS_AND_ROLES.md
    EDGE_CASES.md
  02_DOMAIN/
    DOMAIN_MODEL.md
    STATE_MACHINES.md
    BUSINESS_RULES.md
    WORKFLOWS.md
  03_ARCHITECTURE/
    SYSTEM_ARCHITECTURE.md
    DATA_OWNERSHIP.md
    API_CONTRACTS.md
    EVENTS_JOBS_AND_SYNC.md
    INTEGRATIONS.md
    ADR/
  04_EXPERIENCE/
    INFORMATION_ARCHITECTURE.md
    USER_FLOWS.md
    UI_STATES.md
    ADMIN_AND_SETTINGS.md
    ACCESSIBILITY.md
  05_PRODUCTION/
    SECURITY.md
    OBSERVABILITY.md
    PERFORMANCE_AND_CAPACITY.md
    DATA_LIFECYCLE_AND_MIGRATION.md
    DEPLOYMENT_AND_ROLLBACK.md
  06_QUALITY/
    TEST_PLAN.md
    ACCEPTANCE_MATRIX.md
    BENCHMARK_PLAN.md
    SKILL_AND_TOOL_ACTIVATION_PLAN.md
  07_DELIVERY/
    PHASES_AND_MILESTONES.md
    BACKLOG.md
    RISKS_AND_ASSUMPTIONS.md
  WORKLOG/
    CHECKPOINT.md
    DECISIONS.md
    OPEN_QUESTIONS.md
```

The generator may add/remove files when justified. The structure serves clarity, not bureaucracy.


`06_QUALITY/SKILL_AND_TOOL_ACTIVATION_PLAN.md` should describe capabilities and evidence needs first. External provider names are optional/replaceable unless the product itself depends on a specific provider.

Use `06_TEMPLATES/SKILL_ACTIVATION_PLAN_TEMPLATE.md` as a starting point when specialist capabilities materially affect delivery or release evidence.
