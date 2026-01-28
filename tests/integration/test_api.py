"""Integration tests for the API module."""

import pytest
from fastapi.testclient import TestClient

from python_template.api.app import app


@pytest.mark.integration
class TestAPIIntegration:
    """Integration tests for the FastAPI application."""

    def test_full_request_cycle(self) -> None:
        """Test a complete request/response cycle."""
        with TestClient(app) as client:
            # Check health first
            health_response = client.get("/health")
            assert health_response.status_code == 200

            # Then check root
            root_response = client.get("/")
            assert root_response.status_code == 200

            # Verify data consistency
            root_data = root_response.json()
            health_data = health_response.json()
            assert root_data["version"] == health_data["version"]

    def test_openapi_schema_available(self) -> None:
        """Test that OpenAPI schema is accessible."""
        with TestClient(app) as client:
            response = client.get("/openapi.json")

            assert response.status_code == 200
            schema = response.json()
            assert "openapi" in schema
            assert "paths" in schema
            assert "/" in schema["paths"]
            assert "/health" in schema["paths"]

    def test_docs_endpoint_available(self) -> None:
        """Test that Swagger docs are accessible."""
        with TestClient(app) as client:
            response = client.get("/docs")

            assert response.status_code == 200
            assert "swagger" in response.text.lower() or "html" in response.headers.get(
                "content-type", ""
            )
