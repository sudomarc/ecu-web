# Capability routing

Treat external systems and tools as replaceable providers behind stable capabilities.

## Capability pattern

CAPABILITY → PRIMARY → FALLBACK → HEALTH CHECK → ACTIVE ROUTE

## Requirements

- define the capability needed,
- select a primary provider,
- keep an explicit fallback path,
- verify provider health before relying on it,
- log the final routing decision and its evidence.
