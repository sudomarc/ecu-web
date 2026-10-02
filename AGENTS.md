# AGENTS.md

This repository follows the Vibe Coding Instructions governance model as a portable, evidence-driven operating system for AI-assisted engineering.

## Mission

- Keep changes small, explicit, and verifiable.
- Prefer repository evidence over assumptions.
- Preserve user work and avoid silent scope expansion.
- Require verification before claiming success.

## Core rules

1. Inspect the repository and applicable instructions before changing code.
2. Plan before meaningful implementation.
3. Prefer the smallest coherent change that satisfies the request.
4. Verify behavior using the narrowest useful tests, type checks, lint, or runtime checks.
5. Treat credential, production, remote execution, and destructive Git/database actions as high-risk.
6. Report uncertainty explicitly.
7. Review the final diff before telling the user it is complete.

## Operating loop

REQUEST → UNDERSTAND → INSPECT → PLAN → IMPLEMENT → TEST → REVIEW → VERIFY → REPORT

## Evidence protocol

When a decision depends on a fact or a result, label it as one of:

- FACT
- OBSERVED
- VERIFIED
- INFERENCE
- ASSUMPTION
- UNKNOWN
- CONFLICT
- UNVERIFIED

## Scope and routing

- Use only the matching skill for the current task.
- Keep retrieval bounded and targeted.
- Avoid broad repository dumps unless the task truly requires it.
- Prefer local, low-risk changes over global rewrites.

## Repository bootstrap

This project should keep a minimal governance skeleton that includes:

- "AGENTS.md"
- ".ai/" for core guidance, skills, templates, and agent profiles
- ".github/instructions/" for repo-local instructions
- relevant skill files aligned to the changed surface

## Repository-specific conventions

- Read project-local instructions before editing.
- Adapt commands and tooling to the actual stack in this repository.
- When the repository is empty or intentionally minimal, create the governance skeleton first and then add project implementation on top.

## Completion standard

Completion requires:

- in-scope implementation,
- relevant verification,
- final diff inspection,
- explicit remaining uncertainty, if any.
