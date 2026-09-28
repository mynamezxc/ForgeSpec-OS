---
name: forgespec-security-review
description: Performs threat-led application security review across trust boundaries, authorization, input/data flows, configuration, static analysis, and authorized dynamic testing. Use for security-sensitive changes and release security gates.
---

# ForgeSpec Security Review

## Threat-led workflow
1. Map changed trust boundaries, assets, privileged actions, identities, tenants, external integrations, files, queues, callbacks, and agent/tool boundaries.
2. Write abuse cases for the affected feature, including business-logic abuse and authorization bypass.
3. Inspect authentication, authorization, tenant/data isolation, session/token behavior, and server-side enforcement.
4. Inspect input/output boundaries for injection, XSS, SSRF, path traversal, unsafe deserialization, command execution, redirect and file-upload risks as relevant.
5. Review secrets, logging, error disclosure, encryption/data retention, rate/size limits, timeouts, and privileged defaults.
6. Run targeted static analysis (for example Semgrep) on affected scope and relevant security rules.
7. Use DAST such as ZAP only against owned/explicitly authorized local, test, or staging targets.
8. Use Nuclei only when its templates and target scope are understood and authorized; do not make broad external scanning a default workflow.
9. Manually validate significant scanner findings for reachability, exploitability, and product context.
10. Add regression tests or guardrails for confirmed issues.

## Scanner interpretation
- clean SAST/DAST does not prove business logic is secure;
- scanner severity does not automatically equal product risk;
- confirmed auth/tenant boundary failures are high-priority regardless of scanner visibility;
- never paste secrets or sensitive payloads into reports.

## Exit evidence
Threat/abuse cases, reviewed boundaries, scan versions/scope, triaged findings, fixes/regression tests, and residual-risk statement.
