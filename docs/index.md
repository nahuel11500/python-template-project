# Python Template

A modern, opinionated Python project template featuring FastAPI, Typer CLI, and OpenCode AI integration.

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

- Python 3.14+
- [uv](https://github.com/astral-sh/uv)
- [just](https://github.com/casey/just)

### Installation

```bash
# Install dependencies and set up pre-commit hooks
just setup
```

### Development

```bash
# Start the development server
just dev

# Run the CLI
just cli --help

# Run all quality checks and tests
just check-all
```

## 📖 Documentation

Visit the [full documentation](https://nahuel11500.github.io/python-template-project) for detailed guides.

- [Installation](getting-started/installation.md)
- [Quick Start](getting-started/quickstart.md)
- [Development Guide](development.md)
- [OpenCode Integration](opencode.md)
- [Deployment](deployment.md)
