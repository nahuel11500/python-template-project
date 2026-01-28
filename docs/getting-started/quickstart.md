# Quick Start

This guide will help you get up and running with Python Template quickly.

## Starting the Server

```bash
# Start with auto-reload for development
just dev
```

The API server will start at http://localhost:8000.

### Available Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Application info |
| `GET /health` | Health check |
| `GET /docs` | Swagger UI documentation |
| `GET /redoc` | ReDoc documentation |
| `GET /openapi.json` | OpenAPI schema |

## Using the CLI

The project includes a Typer-based CLI:

```bash
# Show help
just cli --help

# Show version
just cli --version

# Greet someone
just cli hello World

# Show application info
just cli info

# Start the server (alternative to just dev)
just cli serve --port 8080 --reload
```

## Running Tests

```bash
# Run all tests with coverage
just test

# Run only unit tests
just test-unit

# Run only integration tests
just test-integration

# Quick test run (no coverage)
just test-quick
```

## Code Quality

```bash
# Lint and auto-fix
just lint

# Format code
just format

# Type check
just typecheck

# Run all quality checks
just check

# Run everything (quality + tests)
just check-all
```

## Project Configuration

### Environment Variables

Create a `.env` file for local configuration:

```env
# Application
APP_NAME=my-app
DEBUG=true

# Server
HOST=0.0.0.0
PORT=8000

# Logging
LOG_LEVEL=DEBUG
```

### Settings

Settings are managed via [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/):

```python
from python_template.core.config import settings

print(settings.app_name)
print(settings.debug)
```

## Next Steps

- [Development Guide](../development.md) - Learn about development workflow
- [OpenCode Integration](../opencode.md) - Use AI agents and skills
- [Deployment](../deployment.md) - Deploy with containers
