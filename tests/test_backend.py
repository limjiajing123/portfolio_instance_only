import requests

BASE_URL = "http://localhost:5000"

def test_chatbot_missing_message():
    """Should return 400 if no message is provided"""
    response = requests.post(f"{BASE_URL}/api/chat", json={})
    assert response.status_code == 400
    assert "error" in response.json()

def test_chatbot_with_message():
    """Should return a botResponse when message is provided"""
    payload = {"message": "Hello"}
    response = requests.post(f"{BASE_URL}/api/chat", json=payload)
    # API should return success (200)
    assert response.status_code == 200
    data = response.json()
    assert "botResponse" in data
    assert isinstance(data["botResponse"], str)
    assert len(data["botResponse"]) > 0
