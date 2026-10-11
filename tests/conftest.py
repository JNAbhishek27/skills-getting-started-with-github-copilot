import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def activities():
    return {
        "Test Activity": {
            "description": "An activity used for API tests",
            "schedule": "Mondays, 3:00 PM",
            "max_participants": 10,
            "participants": ["existing@example.edu"],
        }
    }


@pytest.fixture
def client(activities, monkeypatch):
    monkeypatch.setattr(app_module, "activities", activities)
    return TestClient(app_module.app)
