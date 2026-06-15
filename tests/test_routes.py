# ---------------------------------------------------------------
# Donovan-Codes : Defining Pytest Unit Tests for API Routes
# ---------------------------------------------------------------

# Donovan-Codes : Importing Pytest and the Application Factory
import pytest
from app import create_app


# Donovan-Codes : Building a Fresh Test Client Fixture in Testing Mode
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


# Donovan-Codes : Asserting the Health Endpoint Returns 200 and Healthy Status
def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


# Donovan-Codes : Asserting the Info Endpoint Returns Correct Service Metadata
def test_info_endpoint(client):
    response = client.get("/api/info")
    assert response.status_code == 200
    assert response.get_json()["service"] == "flask-k8s-pipeline"
