# Failure Escalation and Recovery

When an implementation/test command fails:
1. classify the failure: code defect, test defect, environment/config, dependency, data, flaky infrastructure, permission, external provider;
2. preserve the useful error output;
3. reproduce with the smallest relevant command;
4. fix root cause where feasible;
5. rerun narrow verification;
6. expand regression based on impact.

## Repeated failure threshold
If the same approach fails repeatedly, stop retrying mechanically. Reinspect assumptions, versions, contracts and environment state.

## External dependency failure
Implement/test defined degraded behavior if the product requires resilience. Do not fake provider success simply to make tests green.

## Recovery from a bad change
Prefer a controlled revert/patch based on diff and requirement intent, not broad deletion or regeneration of the subsystem.
