"""Unit tests for the API module."""

import pytest
from fastapi.testclient import TestClient

from python_template import __app_name__, __version__


@pytest.mark.unit
class TestRootEndpoint:
    """Tests for the root endpoint."""

    def test_root_returns_app_info(self, client: TestClient) -> None:
        """Test that root endpoint returns application information."""
        response = client.get("/")

        assert response.status_code == 200
        data = response.json()
        assert data["name"] == __app_name__
        assert data["version"] == __version__
        assert data["status"] == "running"


@pytest.mark.unit
class TestHealthEndpoint:
    """Tests for the health endpoint."""

    def test_health_returns_healthy(self, client: TestClient) -> None:
        """Test that health endpoint returns healthy status."""
        response = client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["version"] == __version__

    def test_health_content_type(self, client: TestClient) -> None:
        """Test that health endpoint returns JSON content type."""
        response = client.get("/health")

        assert response.headers["content-type"] == "application/json"
