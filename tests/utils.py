from fastapi.testclient import TestClient
from app import api  # imports the FastAPI() instance from app.py

_client = TestClient(api)

def chat(msg: str):
    """Send a message directly to the FastAPI app in-memory."""
    r = _client.post("/chat", json={"message": msg})
    return r.json()

def similar(a: str, b: str) -> bool:
    return a.strip() == b.strip()

