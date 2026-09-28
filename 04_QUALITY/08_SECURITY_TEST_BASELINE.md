# Security Test Baseline

Risk-based verification should include where applicable:
- authentication failure/session expiry;
- authorization/IDOR/cross-tenant access;
- unsafe input/injection;
- upload/path/content handling;
- SSRF/outbound URL controls;
- secret exposure;
- privilege escalation;
- CSRF/CORS/session protections appropriate to stack;
- rate/abuse controls for exposed expensive actions;
- audit trail integrity for privileged operations.

For agent/tool products additionally test:
- tool permission bypass;
- untrusted content attempting to alter tool policy;
- destructive action confirmation boundaries;
- connector credential isolation;
- argument validation.

Security testing depth must match the product threat model; this list is not a substitute for one.

## Security skill/tool routing

Use `07_SKILLS/skills/forgespec-security-review/SKILL.md` for threat-led application review and `forgespec-supply-chain` for dependencies/images/configuration. Static and dynamic scanners supplement authorization/business-logic review. Active DAST must remain inside owned or explicitly authorized targets.
