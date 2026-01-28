# justfile - Command runner for python-template
# https://github.com/casey/just

# Default recipe - show available commands
default:
    @just --list

# =============================================================================
# Setup & Installation
# =============================================================================

# Check if a command exists
[private]
has command:
    @command -v {{ command }} >/dev/null 2>&1

# Ensure dev/test dependencies are installed
[private]
ensure-dev-deps:
    #!/usr/bin/env bash
    set -e
    if ! uv run python -c "import pytest" >/dev/null 2>&1; then
        echo "📦 Installing dev dependencies..."
        uv sync --all-extras
    fi

# Install uv if not present
[private]
ensure-uv:
    #!/usr/bin/env bash
    if ! command -v uv &> /dev/null; then
        echo "📦 Installing uv..."
        curl -LsSf https://astral.sh/uv/install.sh | sh
        echo "✅ uv installed. You may need to restart your shell or run: source ~/.bashrc"
    else
        echo "✅ uv is already installed"
    fi

# Install OpenCode if not present
[private]
ensure-opencode:
    #!/usr/bin/env bash
    if ! command -v opencode &> /dev/null; then
        echo "🤖 Installing OpenCode..."
        curl -fsSL https://opencode.ai/install | bash
        echo "✅ OpenCode installed"
    else
        echo "✅ OpenCode is already installed"
    fi

# Install Python 3.14 via uv
[private]
ensure-python:
    #!/usr/bin/env bash
    echo "🐍 Ensuring Python 3.14..."
    uv python install 3.14
    echo "✅ Python 3.14 is available"

# Full setup: install all tools, dependencies, and pre-commit hooks
setup:
    #!/usr/bin/env bash
    set -e
    echo "🚀 Setting up Python Template Project..."
    echo ""

    # Install uv
    just ensure-uv

    # Ensure uv is in PATH for this session
    export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"

    # Install Python
    just ensure-python

    # Install OpenCode
    just ensure-opencode

    # Install project dependencies
    echo ""
    echo "📦 Installing project dependencies..."
    uv sync --all-extras

    # Install pre-commit hooks
    echo ""
    echo "🔧 Setting up pre-commit hooks..."
    uv run pre-commit install
    uv run pre-commit install --hook-type commit-msg

    echo ""
    echo "✅ Setup complete! Run 'just dev' to start developing."

# Install project dependencies only (assumes uv is installed)
install:
    uv sync --all-extras

# =============================================================================
# Development
# =============================================================================

# Start the development server with auto-reload
dev:
    uv run uvicorn python_template.api.app:app --reload --host 0.0.0.0 --port 8000

# Run the CLI
cli *ARGS:
    uv run python-template {{ ARGS }}

# =============================================================================
# Testing
# =============================================================================

# Run all tests with coverage
test:
    just ensure-dev-deps
    uv run pytest

# Run unit tests only
test-unit:
    just ensure-dev-deps
    uv run pytest -m unit

# Run integration tests only
test-integration:
    just ensure-dev-deps
    uv run pytest -m integration

# Run tests without coverage requirement (for development)
test-quick:
    just ensure-dev-deps
    uv run pytest --no-cov -x

# Run tests and generate HTML coverage report
test-cov:
    just ensure-dev-deps
    uv run pytest --cov-report=html
    @echo "Coverage report generated at htmlcov/index.html"

# =============================================================================
# Code Quality
# =============================================================================

# Run linter and auto-fix issues
lint:
    uv run ruff check --fix .

# Format code
format:
    uv run ruff format .

# Run type checker
typecheck:
    uv run ty check

# Run all checks (lint, format, typecheck)
check: lint format typecheck

# Run all quality checks and tests
check-all: check test

# =============================================================================
# Documentation
# =============================================================================

# Serve documentation locally
docs:
    uv run mkdocs serve

# Build documentation
docs-build:
    uv run mkdocs build

# =============================================================================
# Build & Release
# =============================================================================

# Build the package
build:
    uv build

# Clean build artifacts
clean:
    rm -rf dist/
    rm -rf build/
    rm -rf *.egg-info/
    rm -rf .pytest_cache/
    rm -rf .ruff_cache/
    rm -rf .coverage
    rm -rf htmlcov/
    rm -rf coverage.xml
    rm -rf .mypy_cache/
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true

# =============================================================================
# Container
# =============================================================================

# Build container image
container-build:
    podman build -f Containerfile -t python-template:latest .

# Run container
container-run:
    podman run -p 8000:8000 python-template:latest

# =============================================================================
# Utilities
# =============================================================================

# Show project info
info:
    @echo "Python Template Project"
    @echo "======================="
    @uv run python -c "import python_template; print(f'Version: {python_template.__version__}')"
    @uv python find

# Update dependencies
update:
    uv sync --upgrade
