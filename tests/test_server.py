from fastapi.testclient import TestClient
from tradingsignal.service import server

app = server.create_app()
client = TestClient(app)


def test_root():
    response = client.get("/")
    print(response.text)
    assert response.status_code == 200
    assert response.json().startswith("Hello from TradingSignal Version:")
