# {{PROJECT_NAME}} Agent Memory

## Project State (updated {{DATE_TODAY}})

- **Phase:** M0 — Project scaffold initialized
- **Test count:** 0 passing
- **Branch:** `main`
- **Next:** Define research strategy, implement evaluation pipeline

## Architecture Patterns

*(Record stable patterns confirmed across multiple sessions here.)*

## Key File Locations

- Training script: `scripts/train.py` (TODO)
- Evaluation script: `scripts/eval.py` (TODO)
- Job scripts: `jobs/`
- Tests: `tests/`

## User Preferences

*(Record user's confirmed workflow preferences here.)*

## Common Pitfalls

- Shell env vars don't expand in Bash tool — use hardcoded paths (e.g., `{{DATA_ROOT_DEFAULT}}`)
- Always run `ruff format` after edits
- Val/test data paths may differ from train — verify before assuming
