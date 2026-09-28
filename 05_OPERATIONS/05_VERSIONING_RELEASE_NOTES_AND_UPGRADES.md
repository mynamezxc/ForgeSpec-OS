# Versioning, Release Notes and Upgrade Discipline

## Version changes should communicate
- user-visible behavior;
- schema/config requirements;
- breaking contract changes;
- migration steps;
- deprecations;
- rollback caveats.

## Compatibility
When supporting multiple client/server versions, define the compatibility window explicitly.

## Upgrade testing
Test at least the supported previous production version -> new version path for release-critical upgrades.

## Deprecation
A deprecation needs replacement guidance and a removal trigger/version. Do not accumulate permanent compatibility branches without ownership.
