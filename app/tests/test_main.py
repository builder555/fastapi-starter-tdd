from fastapi import FastAPI
import pytest
from fastapi.testclient import TestClient
from main import _app


@pytest.fixture()
def client():
    client = TestClient(_app)
    return client

class TestMain:
    def test_ping(self, client):
        response = client.get("/ping")
        assert response.status_code == 200
        assert response.json() == {"ping": "pong!"}
