# Security, Privacy and Permission Baseline

Apply according to Product SPEC and risk; do not invent compliance claims.

## Minimum baseline
- authenticate trusted identity where required;
- authorize every privileged server-side action;
- validate external inputs;
- protect secrets and credentials;
- use secure transport where networked;
- avoid sensitive data in logs;
- protect destructive operations;
- make important admin actions auditable;
- define session/token lifecycle;
- define upload/file handling constraints if applicable.

## Permission modeling
Prefer explicit roles/capabilities/policies over scattered boolean checks. Test both allowed and denied paths.

## Multi-tenant systems
Tenant boundaries must be enforced in authoritative backend/data access, not only in client filters.

## Security review triggers
Mandatory deeper review for auth changes, permission changes, money movement, file execution, plugin/tool execution, user-controlled queries, secrets, network tunnels, remote control and cross-tenant data.
