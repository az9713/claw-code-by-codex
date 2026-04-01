# Media Policy

Last updated: 2026-04-01

## Purpose

Use media to improve comprehension, not decoration. Every image or video must teach something specific.

## Allowed Media Types

- Hero screenshot: one per major user-facing surface.
- Feature screenshot: only when it shows a distinct state not already captured.
- Short demo video: one canonical walkthrough per feature cluster.

## Keep/Skip Rules

Keep media only if it answers one of:
- What does this feature look like?
- What should I expect after running command X?
- How do I verify success/failure visually?

Skip media if it duplicates existing content with no new information.

## Canonical Assets

Prefer one canonical file per concept:
- UI hero: `docs/frontend.jpg`
- Agentic demo video (repo asset): `docs/demo_agents_github.mp4`
- Agentic demo URL (external): maintain in docs links

Avoid multiple near-identical screenshots of the same UI state.

## File Constraints

- Images: target under 500 KB when practical.
- Videos committed to repo: target under 10 MB.
- Do not commit raw/uncompressed recordings unless explicitly required.
- Use descriptive stable names: `<feature>_<state>.<ext>`.

## Placement Rules

- README: only high-signal media (max one screenshot plus one video link per feature section).
- Deep docs (`docs/...`): implementation/state-specific media allowed with short captions.
- Every media item should have a one-line caption or context sentence.

## Update and Lifecycle

- When UI changes materially, replace canonical media rather than accumulating similar versions.
- If historical media must be preserved, use release assets instead of git history where possible.
- Broken media links block release readiness.

## Source of Truth Link Strategy

- Prefer linking to:
  1. canonical local compressed asset in repo
  2. canonical external URL (if hosted)
- Keep both synchronized in the same PR when one changes.

## Media Review Checklist

- [ ] Non-duplicative and high-signal.
- [ ] File size acceptable.
- [ ] Caption/context included.
- [ ] Correct placement (README vs deep docs).
- [ ] Links valid and tested.
