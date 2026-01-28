# Python Template

A modern, opinionated Python project template featuring FastAPI, Typer CLI, and OpenCode AI integration.

[![CI](https://github.com/nahuel11500/python-template-project/actions/workflows/ci.yml/badge.svg)](https://github.com/nahuel11500/python-template-project/actions/workflows/ci.yml)
[![Security](https://github.com/nahuel11500/python-template-project/actions/workflows/security.yml/badge.svg)](https://github.com/nahuel11500/python-template-project/actions/workflows/security.yml)
[![codecov](https://codecov.io/gh/nahuel11500/python-template-project/branch/main/graph/badge.svg)](https://codecov.io/gh/nahuel11500/python-template-project)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.14+](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## ✨ Features

- **🚀 Modern Python** - Python 3.14+ with strict type hints
- **📦 uv** - Fast, reliable dependency management
- **🔧 Ruff** - Lightning-fast linting and formatting
- **🔍 ty** - Fast type checking
- **🌐 FastAPI** - High-performance async API framework
- **⌨️ Typer** - Beautiful CLI with auto-completion
- **🧪 pytest** - Comprehensive testing with 90% coverage requirement
- **🤖 OpenCode** - AI agent and skill integration
- **🔄 Semantic Release** - Automated versioning and changelog
- **🐳 Container Ready** - Multi-stage Containerfile for production
- **🔒 Security** - Bandit, pip-audit, and CodeQL scanning
- **📚 MkDocs** - Beautiful documentation with Material theme

## 🚀 Quick Start

### Prerequisites

- [just](https://github.com/casey/just) - Command runner (the only prerequisite!)

=== "Cargo"
    ```bash
    cargo install just
    ```

=== "Homebrew"
    ```bash
    brew install just
    ```

=== "Arch Linux"
    ```bash
    pacman -S just
    ```

=== "apt (Debian/Ubuntu)"
    ```bash
    apt install just
    ```

See [just installation](https://just.systems/man/en/chapter_4.html) for more options.

### Installation

```bash
# Clone the repository
git clone https://github.com/nahuel11500/python-template-project.git
cd python-template-project

# Setup everything (installs uv, Python 3.14, OpenCode, dependencies, pre-commit hooks)
just setup
```

That's it! `just setup` automatically installs:
- **uv** - Fast Python package manager
- **Python 3.14** - Via uv
- **OpenCode** - AI coding agent
- **All project dependencies** - Including ruff, ty, pytest, etc.
- **Pre-commit hooks** - For code quality and conventional commits

### Development

```bash
# Start the development server
just dev

# Run the CLI
just cli --help
just cli hello World
just cli info

# Run all quality checks and tests
just check-all
```

Note: `just check-all` expects dev dependencies (like pytest). If you ran `just install`
without extras, run `uv sync --all-extras` before `just check-all`.

### Available Commands

```bash
just              # Show all available commands
just install      # Install dependencies
just setup        # Install deps + pre-commit hooks
just dev          # Start dev server with hot reload
just test         # Run tests with coverage
just test-unit    # Run unit tests only
just lint         # Lint and auto-fix
just format       # Format code
just typecheck    # Type check with ty
just check        # Run all quality checks
just docs         # Serve documentation locally
just clean        # Remove build artifacts
```

## 📁 Project Structure

```
python-template-project/
├── src/python_template/     # Main package
│   ├── api/                 # FastAPI application
│   │   └── app.py          # API routes and setup
│   ├── core/               # Business logic
│   │   └── config.py       # Settings management
│   └── cli.py              # Typer CLI
├── tests/                   # Test suite
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── docs/                    # MkDocs documentation
├── .opencode/              # OpenCode agent configs
│   ├── agents/             # Custom AI agents
│   └── skills/             # Reusable skills
├── .github/                # GitHub Actions workflows
├── pyproject.toml          # Project configuration
├── justfile                # Task automation
├── Containerfile           # Container build
└── AGENTS.md              # OpenCode instructions
```

## 🤖 OpenCode Integration

This template includes OpenCode AI integration for enhanced development:

### Skills

- **test-generator**: Generate pytest tests from source code

### Agents

- **reviewer**: Code review agent with read-only access

See [AGENTS.md](AGENTS.md) for detailed agent instructions.

## 🐳 Container

```bash
# Build the container
just container-build

# Run the container
just container-run

# Or manually
podman build -f Containerfile -t python-template:latest .
podman run -p 8000:8000 python-template:latest
```

## 📖 Documentation

```bash
# Serve documentation locally
just docs

# Build documentation
just docs-build
```

Visit http://localhost:8000 after running `just docs`.

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | python-template | Application name |
| `DEBUG` | false | Enable debug mode |
| `HOST` | 0.0.0.0 | Server host |
| `PORT` | 8000 | Server port |
| `LOG_LEVEL` | INFO | Logging level |

Create a `.env` file for local development:

```env
DEBUG=true
LOG_LEVEL=DEBUG
```

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Commit Convention

This project uses [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

# Examples
feat(api): add user authentication endpoint
fix(cli): handle missing config file gracefully
docs(readme): update installation instructions
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
