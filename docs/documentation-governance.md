# Documentation Governance

Last updated: 2026-04-01

## Goal

Prevent documentation debt and reduce future technical debt by ensuring docs evolve with code.

## Documentation Principles (2026 best practice)

1. Docs-as-code: versioned in repo and reviewed with code changes.
2. Single source of truth: avoid duplicated conflicting instructions.
3. Runnable examples: commands in docs should be executable as written.
4. Audience-based structure: separate onboarding, reference, and operations.
5. Change traceability: maintain explicit change logs for major feature additions.

## Required Update Triggers

When any of the following changes, update docs in the same PR:
- CLI command names, options, output fields.
- API endpoint paths, params, response schema.
- Setup/run prerequisites.
- Test strategy or quality gates.
- Production/local operational workflow.

## Ownership

- Feature owner updates feature docs.
- Reviewer verifies docs impact in code review.
- Maintainer blocks merges with stale docs for user-facing changes.

## Doc Quality Checklist

- [ ] Commands are copy-paste runnable.
- [ ] Paths and filenames are correct.
- [ ] Constraints and defaults are explicit.
- [ ] Error behavior is described.
- [ ] Cross-links to related docs are present.
- [ ] Dates are present on top-level docs.
- [ ] Media use follows `docs/media-policy.md`.

## Anti-Tech-Debt Requirements

- Keep domain logic in Python backend modules (`src/`), not duplicated in frontend.
- Keep API thin and typed through explicit parameter validation.
- Keep tests aligned with public interfaces.
- Record architectural changes in `docs/web-enablement-change-log.md`.

## Review Cadence

- Per change: update impacted docs.
- Monthly: quick docs health pass for stale sections.
- Release candidate: run smoke checklist from `docs/runbooks.md`.
