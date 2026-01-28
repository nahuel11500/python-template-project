"""Unit tests for the CLI module."""

import pytest
from typer.testing import CliRunner

from python_template import __app_name__, __version__
from python_template.cli import app

runner = CliRunner()


@pytest.mark.unit
class TestCLI:
    """Tests for the CLI commands."""

    def test_version_flag(self) -> None:
        """Test --version flag shows version."""
        result = runner.invoke(app, ["--version"])

        assert result.exit_code == 0
        assert __version__ in result.stdout

    def test_hello_default(self) -> None:
        """Test hello command with default argument."""
        result = runner.invoke(app, ["hello"])

        assert result.exit_code == 0
        assert "Hello, World!" in result.stdout

    def test_hello_with_name(self) -> None:
        """Test hello command with custom name."""
        result = runner.invoke(app, ["hello", "Python"])

        assert result.exit_code == 0
        assert "Hello, Python!" in result.stdout

    def test_info_command(self) -> None:
        """Test info command shows application info."""
        result = runner.invoke(app, ["info"])

        assert result.exit_code == 0
        assert "Application Info" in result.stdout
        assert __app_name__ in result.stdout

    def test_no_args_shows_help(self) -> None:
        """Test that running with no args shows help."""
        result = runner.invoke(app, [])

        assert result.exit_code == 0
        assert "Usage" in result.stdout or "Commands" in result.stdout
