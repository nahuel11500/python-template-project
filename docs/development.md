# Development Guide

This guide covers the development workflow and tools used in Python Template.

## Available Commands

All commands are run using `just`:

```bash
just              # Show all available commands
```

### Setup & Installation

| Command | Description |
|---------|-------------|
| `just install` | Install dependencies |
| `just setup` | Install deps + pre-commit hooks |
| `just update` | Update dependencies |

### Development

| Command | Description |
|---------|-------------|
| `just dev` | Start dev server with hot reload |
| `just cli ARGS` | Run the CLI with arguments |

### Testing

| Command | Description |
|---------|-------------|
| `just test` | Run all tests with coverage |
| `just test-unit` | Run unit tests only |
| `just test-integration` | Run integration tests only |
| `just test-quick` | Quick run without coverage |
| `just test-cov` | Generate HTML coverage report |

### Code Quality

| Command | Description |
|---------|-------------|
| `just lint` | Lint with ruff (auto-fix) |
| `just format` | Format with ruff |
| `just typecheck` | Type check with ty |
| `just check` | Run all quality checks |
| `just check-all` | Quality checks + tests |

### Documentation

| Command | Description |
|---------|-------------|
| `just docs` | Serve docs locally |
| `just docs-build` | Build documentation |

### Build & Container

| Command | Description |
|---------|-------------|
| `just build` | Build the package |
| `just container-build` | Build container image |
| `just container-run` | Run container |
| `just clean` | Remove build artifacts |

## Pre-commit Hooks

Pre-commit hooks run automatically on each commit:

1. **Trailing whitespace** - Remove trailing whitespace
2. **End of file** - Ensure files end with newline
3. **YAML/TOML/JSON** - Validate config files
4. **Ruff** - Lint and format Python code
5. **ty** - Type check Python code
6. **Commitizen** - Validate commit message format

### Manual Run

```bash
# Run all hooks on staged files
uv run pre-commit run

# Run all hooks on all files
uv run pre-commit run --all-files

# Run specific hook
uv run pre-commit run ruff
```

## Testing Strategy

### Test Structure

```
tests/
├── conftest.py          # Shared fixtures
├── unit/                # Fast, isolated tests
│   ├── test_api.py
│   ├── test_cli.py
│   └── test_core.py
└── integration/         # Integration tests
    └── test_api.py
```

### Markers

Use markers to categorize tests:

```python
import pytest

@pytest.mark.unit
def test_fast_isolated():
    """Unit test - fast and isolated."""
    pass

@pytest.mark.integration
def test_with_dependencies():
    """Integration test - may use external services."""
    pass

@pytest.mark.slow
def test_long_running():
    """Slow test - can be skipped for quick runs."""
    pass
```

### Running Specific Tests

```bash
# Run tests matching a pattern
uv run pytest -k "test_health"

# Run tests in a specific file
uv run pytest tests/unit/test_api.py

# Run with verbose output
uv run pytest -v

# Stop on first failure
uv run pytest -x
```

### Coverage

Coverage is configured to:

- **Minimum**: 90% required
- **Report**: Terminal + HTML + XML
- **Exclude**: `__init__.py`, type checking blocks

View HTML coverage report:

```bash
just test-cov
# Open htmlcov/index.html
```

## Code Style

### Ruff Configuration

Ruff is configured in `pyproject.toml`:

- **Line length**: 100 characters
- **Target**: Python 3.14
- **Rules**: E, W, F, I, B, C4, UP, SIM, TCH, PTH, RUF

### Type Checking

ty is used for type checking:

```bash
# Run type checker
just typecheck

# Or directly
uvx ty check
```

All functions should have type hints:

```python
def process_data(data: dict[str, Any]) -> list[str]:
    """Process data and return results."""
    ...
```

## Debugging

### VS Code

Recommended extensions are configured in `.vscode/extensions.json`:

- Python
- Ruff
- Pylance

Debug configurations are in `.vscode/launch.json`.

### Logging

Configure logging via environment:

```bash
LOG_LEVEL=DEBUG just dev
```

Or in code:

```python
import logging

logger = logging.getLogger(__name__)
logger.debug("Debug message")
```

## Troubleshooting

### Common Issues

**Dependencies not installing**

```bash
# Clear cache and reinstall
uv cache clean
just install
```

**Pre-commit hooks failing**

```bash
# Update hooks
uv run pre-commit autoupdate

# Run manually to see errors
uv run pre-commit run --all-files
```

**Type errors**

```bash
# Check specific file
uvx ty check src/python_template/module.py
```
