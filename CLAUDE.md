# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**hdx-scraper-tokentest** tests whether the HDX API token has write access. It calls `User.check_current_user_write_access("hdx")` and is run periodically to verify that the configured HDX bot token is still valid.

## Commands

Install dependencies:
```bash
uv sync
```

Run the scraper:
```bash
uv run python -m hdx.scraper.tokentest
```

Run tests:
```bash
uv run pytest
```

Run a single test:
```bash
uv run pytest tests/test_tokentest.py
```

Lint check:
```bash
pre-commit run --all-files
```

## Architecture

The pipeline in `__main__.py`:

1. **`main`** — Calls `User.check_current_user_write_access("hdx")` to verify the configured HDX API token has write access. Logs success or raises an exception on failure.

### Key design points

- **No config files**: Unlike most scrapers, this project has no `config/` directory — there is no dataset to create or API to query beyond the HDX user check.
- **Single dependency**: Only `hdx-python-api` is required at runtime.

## Environment

Requires `~/.hdx_configuration.yaml` with HDX credentials, or env vars: `HDX_KEY`, `HDX_SITE`, `USER_AGENT`, `TEMP_DIR`, `LOG_FILE_ONLY`.

Requires `~/.useragents.yaml` with a `hdx-scraper-tokentest` entry.

## Collaboration Style

- Be objective, not agreeable. Act as a partner, not a sycophant. Push back when you disagree, flag tradeoffs honestly, and don't sugarcoat problems.
- Keep explanations brief and to the point.
- Don't rely on recalled knowledge for facts that could be stale (API behaviour, library versions, external systems). Search or read the actual source first.

## Scope of Changes

When fixing a bug or addressing PR feedback, change only what is necessary to resolve the specific issue. Do not refactor surrounding code, rename variables, adjust formatting, or make improvements in the same commit unless they are directly required by the fix.
