"""Unit tests for the core module."""

import pytest

from python_template.core.config import Settings, get_settings


@pytest.mark.unit
class TestSettings:
    """Tests for the Settings class."""

    def test_default_settings(self) -> None:
        """Test default settings values."""
        settings = Settings()

        assert settings.app_name == "python-template"
        assert settings.debug is False
        assert settings.host == "0.0.0.0"
        assert settings.port == 8000
        assert settings.log_level == "INFO"

    def test_settings_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test settings loaded from environment variables."""
        monkeypatch.setenv("APP_NAME", "custom-app")
        monkeypatch.setenv("DEBUG", "true")
        monkeypatch.setenv("PORT", "9000")

        settings = Settings()

        assert settings.app_name == "custom-app"
        assert settings.debug is True
        assert settings.port == 9000

    def test_get_settings_cached(self) -> None:
        """Test that get_settings returns cached instance."""
        settings1 = get_settings()
        settings2 = get_settings()

        assert settings1 is settings2
