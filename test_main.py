from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "docs" in response.text

def test_random_number():
    # Test range logic
    payload = {"bottom": 1, "top": 10}
    response = client.post("/random-number", json=payload)
    assert response.status_code == 200
    assert 1 <= response.json() <= 10

def test_coin_flip():
    response = client.post("/coin-flip")
    assert response.status_code == 200
    assert response.json() in ["Heads", "Tails"]

def test_dice_roll():
    payload = {"number_of_dice": 3}
    response = client.post("/dice-roll", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3
    for roll in data:
        assert 1 <= roll <= 6