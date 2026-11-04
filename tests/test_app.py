"""
Pytest test suite for the Result-Check application.
5 tests covering the Flask app, API, and result calculation logic.
"""

import pytest
from app import app
from results import calculate_result


@pytest.fixture
def client():
    """Create a Flask test client."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    """Test that /health returns 200 and healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["students_loaded"] == 5


def test_api_result_found(client):
    """Test API returns correct data for a valid roll number."""
    response = client.get("/api/result/21CS001")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Alice Johnson"
    assert data["status"] == "Pass"


def test_api_result_not_found(client):
    """Test API returns 404 for an unknown roll number."""
    response = client.get("/api/result/99XX999")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data


def test_calculate_result_pass():
    """Test that calculate_result returns correct percentage and Pass status."""
    result = calculate_result("21CS001")
    assert result is not None
    assert result["percentage"] == 82.6
    assert result["status"] == "Pass"


def test_calculate_result_fail():
    """Test that a student below 50 in any subject gets Fail status."""
    result = calculate_result("21CS004")
    assert result is not None
    assert result["status"] == "Fail"

