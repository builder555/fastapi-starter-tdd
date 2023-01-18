from fastapi import FastAPI
import pytest
from fastapi.testclient import TestClient
from app.module import router

@pytest.fixture(autouse=True)
def _app():
    a = FastAPI()
    a.include_router(router)
    return a

@pytest.fixture()
def client(_app):
    client = TestClient(_app)
    return client

class TestMain:
    def test_ping(self, client):
        response = client.get("/modping")
        assert response.status_code == 200
        assert response.json() == {"modping": "pong!"}
