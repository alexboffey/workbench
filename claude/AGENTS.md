# Agent Instructions

Coding style, testing, security, git and patterns live in `~/.claude/rules/ecc/` and load automatically. Do not restate them here.

On-demand detail lives in skills:

- `dev-workflow`: research, plan, TDD, review, commit
- `review-standards`: review checklist and severity levels
- `agent-orchestration`: which subagent fits which task
- `web-hooks`: hook setup for frontend repos

## Capturing knowledge

- Personal debugging notes, preferences and temporary context go to auto memory.
- Team or project knowledge (architecture decisions, API changes, runbooks) goes in the project's existing docs.
- If the current task already produces the docs or code comments, do not duplicate them elsewhere.
- If there is no obvious doc location, ask before creating a new top-level file.
