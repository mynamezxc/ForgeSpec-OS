# Capability Profile Selection

During Product SPEC generation, explicitly decide which profiles apply.

Possible profiles:
- offline-first / unreliable network;
- local hardware/device integration;
- multi-tenant SaaS;
- single-tenant/on-premise;
- public API/SDK;
- plugin/tool execution;
- realtime collaboration;
- high-volume ingestion;
- financial/money/accounting;
- regulated/sensitive data;
- mobile/native;
- desktop/native bridge;
- AI/agent workflows;
- scheduled/background jobs;
- internationalization/multi-language;
- multi-region/high availability.

For each selected profile, Product SPEC must include its specific risks, contracts and tests. For unselected profiles, do not burden the implementation with speculative infrastructure.
