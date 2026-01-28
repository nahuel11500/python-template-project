# Installation

## Prerequisites

The only prerequisite is [just](https://github.com/casey/just) - a command runner.

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

=== "Windows (Scoop)"
    ```powershell
    scoop install just
    ```

See [just installation docs](https://just.systems/man/en/chapter_4.html) for more options.

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/nahuel11500/python-template-project.git
cd python-template-project
```

### 2. Run Setup

```bash
just setup
```

That's it! The setup command automatically installs:

- ✅ **uv** - Fast Python package manager
- ✅ **Python 3.14** - Via uv
- ✅ **OpenCode** - AI coding agent
- ✅ **Project dependencies** - FastAPI, Typer, pytest, ruff, ty, etc.
- ✅ **Pre-commit hooks** - Code quality and conventional commit validation

### 3. Verify Installation

```bash
# Run all quality checks
just check-all

# Start the development server
just dev
```

Visit http://localhost:8000 to see the API documentation.

## Next Steps

- [Quick Start Guide](quickstart.md) - Learn the basics
- [Development Guide](../development.md) - Set up your development environment
