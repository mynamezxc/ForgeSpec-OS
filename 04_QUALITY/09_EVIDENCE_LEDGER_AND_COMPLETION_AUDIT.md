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
For each critical requirement and release-blocking scope variant record:
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
1. compare the Project Goal mandatory scope inventory against the Product SPEC;
2. compare all in-scope requirement IDs and release-blocking scope items against the ledger;
3. inspect all failed/skipped/quarantined checks;
4. inspect known TODO/FIXME/stub/mock markers in touched production scope;
5. inspect migration/config/deployment diffs;
6. review open critical/high risks;
7. independently verify the most business-critical journey;
8. confirm there is no `CONTINUATION_REQUIRED` state or known executable mandatory work remaining.

No evidence ledger entry should claim broader coverage than the scenario actually proved.
