# Offline, Distributed and Hardware Capability Profile

This file is conditional: apply only when the Product SPEC requires offline use, local devices, edge nodes or unreliable connectivity.

## Offline-first requirements
Define:
- local authoritative/temporary state;
- operation queue/outbox;
- sync protocol;
- conflict strategy by entity/field;
- idempotent replay;
- ordering assumptions;
- local encryption/security;
- sync status visible to user/operator;
- recovery from corrupt/partial local state.

## Hardware integration
Use a device-adapter boundary. Discovery may include LAN/Wi-Fi/Bluetooth/USB/native bridge as required by the Product SPEC.

Device handling should model:
- discover;
- identify/capabilities;
- pair/authorize;
- health/status;
- reconnect;
- execute command;
- timeout/retry;
- fallback/manual selection;
- diagnostics.

## Smooth UX rule
Offline/degraded behavior must be intentional: users should know what is local, queued, synced, failed or conflicting without being forced to understand transport internals.
