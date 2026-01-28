"""Test configuration and shared fixtures."""

import pytest
from fastapi.testclient import TestClient

from python_template.api.app import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def sample_data() -> dict[str, str]:
    """Provide sample test data."""
    return {
        "name": "test",
        "value": "example",
    }
