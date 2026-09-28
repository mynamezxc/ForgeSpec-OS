# Evidence Ledger and Completion Audit

The final completion claim should be reconstructable from evidence rather than trust in the coding agent.

## Evidence types
- automated test ID/output;
- build/type/lint result;
- API/contract verification;
- database/migration validation;
- E2E scenario result;
- benchmark result;
- security review/test;
- UI/manual verification where automation is impractical;
- deployment/smoke verification.

## Evidence record
For each critical requirement record:
- requirement ID;
- evidence ID;
- environment/version;
- command/scenario;
- result;
- artifact/log reference;
- verifier;
- date/session if needed.

## Completion audit
Before final `DONE` / `PRODUCTION_READY`:
1. compare all in-scope requirement IDs against the ledger;
2. inspect all failed/skipped/quarantined checks;
3. inspect known TODO/FIXME/stub/mock markers in touched production scope;
4. inspect migration/config/deployment diffs;
5. review open critical/high risks;
6. independently verify the most business-critical journey.

No evidence ledger entry should claim broader coverage than the scenario actually proved.
