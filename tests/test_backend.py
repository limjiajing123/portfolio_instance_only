import requests
import requests_mock
import pytest

BASE_URL = "http://localhost:5000"

def test_chatbot_missing_message():
    """Should return 400 if no message is provided"""
    response = requests.post(f"{BASE_URL}/api/chat", json={})
    assert response.status_code == 400
    assert "error" in response.json()

def test_chatbot_with_message():
    payload = {"message": "Hello"}

    with requests_mock.Mocker() as m:
        # Mock the POST to OpenRouter API
        m.post('https://openrouter.ai/api/v1/chat/completions', json={
            "choices": [{"message": {"content": "Hi there!"}}]
        })

        response = requests.post(f"{BASE_URL}/api/chat", json=payload)
        assert response.status_code == 200
        assert "botResponse" in response.json()
        assert response.json()["botResponse"] == "Hi there!"
