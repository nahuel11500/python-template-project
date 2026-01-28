# Python Template Project - OpenCode Agent Instructions

This file provides instructions for AI coding agents (like OpenCode) working in this repository.

## Project Overview

This is a modern Python project template using:
- **Python 3.14+** with type hints
- **uv** for dependency management
- **FastAPI** for the web API
- **Typer** for the CLI
- **Ruff** for linting and formatting
- **ty** for type checking
- **pytest** with 90% coverage requirement
- **Semantic Release** for automated versioning

## Commands

### Development

```bash
# Install dependencies
just install

# Setup development environment (install + pre-commit hooks)
just setup

# Run development server
just dev

# Run CLI
just cli --help
```

### Testing

```bash
# Run all tests with coverage
just test

# Run unit tests only
just test-unit

# Run integration tests only
just test-integration

# Quick test run (no coverage)
just test-quick
```

### Code Quality

```bash
# Run linter with auto-fix
just lint

# Format code
just format

# Type check
just typecheck

# Run all quality checks
just check

# Run all checks and tests
just check-all
```

### Documentation

```bash
# Serve docs locally
just docs

# Build docs
just docs-build
```

### Container

```bash
# Build container image
just container-build

# Run container
just container-run
```

## Code Style Guidelines

### Python

- **Line length**: 100 characters
- **Quotes**: Double quotes for strings
- **Imports**: Sorted with isort (via ruff)
- **Type hints**: Required for all function signatures
- **Docstrings**: Google style, required for public functions/classes

### Example

```python
"""Module description."""

from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    """User model representing an application user.

    Attributes:
        name: The user's display name.
        email: The user's email address.
    """

    name: str
    email: str
    age: Optional[int] = None


def greet_user(user: User) -> str:
    """Generate a greeting message for a user.

    Args:
        user: The user to greet.

    Returns:
        A personalized greeting string.
    """
    return f"Hello, {user.name}!"
```

### Naming Conventions

- **Files**: `snake_case.py`
- **Classes**: `PascalCase`
- **Functions/Methods**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: Prefix with `_`

### Error Handling

- Use specific exception types
- Include context in error messages
- Log errors appropriately

```python
from python_template.core.config import settings

def process_data(data: dict) -> dict:
    """Process input data with validation."""
    if not data:
        raise ValueError("Data cannot be empty")

    try:
        result = transform(data)
    except TransformError as e:
        raise ProcessingError(f"Failed to transform data: {e}") from e

    return result
```

## Testing Guidelines

### Structure

- `tests/unit/` - Fast, isolated unit tests
- `tests/integration/` - Tests involving multiple components
- `tests/conftest.py` - Shared fixtures

### Markers

```python
import pytest

@pytest.mark.unit
def test_something_fast():
    """Unit test - fast and isolated."""
    pass

@pytest.mark.integration
def test_something_with_dependencies():
    """Integration test - may use external services."""
    pass
```

### Coverage

- **Minimum**: 90% coverage required
- **Exclude**: `__init__.py`, type checking blocks

## Commit Message Format

Use conventional commits:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Test additions/changes
- `build`: Build system changes
- `ci`: CI/CD changes
- `chore`: Maintenance tasks

### Examples

```
feat(api): add user authentication endpoint
fix(cli): handle missing config file gracefully
docs(readme): update installation instructions
test(core): add unit tests for config validation
```

## Project Structure

```
python-template-project/
├── src/python_template/
│   ├── __init__.py          # Package init with version
│   ├── cli.py               # Typer CLI application
│   ├── api/
│   │   ├── __init__.py
│   │   └── app.py           # FastAPI application
│   └── core/
│       ├── __init__.py
│       └── config.py        # Settings management
├── tests/
│   ├── conftest.py          # Shared fixtures
│   ├── unit/                # Unit tests
│   └── integration/         # Integration tests
├── docs/                    # MkDocs documentation
├── .opencode/               # OpenCode agent configs
│   ├── agents/              # Custom agents
│   └── skills/              # Reusable skills
├── .github/                 # GitHub Actions workflows
├── pyproject.toml           # Project configuration
├── justfile                 # Task automation
├── Containerfile            # Container build
└── AGENTS.md               # This file
```

## OpenCode Integration

This project supports OpenCode AI agents with:

- **Custom agents** in `.opencode/agents/`
- **Reusable skills** in `.opencode/skills/`

### Available Skills

- `test-generator`: Generate pytest tests from code

### Available Agents

- `reviewer`: Code review agent with read-only access

## Important Notes

1. Always run `just check-all` before committing
2. Ensure tests pass with 90% coverage
3. Follow conventional commit format
4. Type hints are mandatory
5. Update documentation when adding features
