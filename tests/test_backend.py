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
    """Should return a botResponse when message is provided"""
    payload = {"message": "Hello"}

    # Patch the requests.post inside your server code (axios or requests) to mock OpenRouter API
    with requests_mock.Mocker(real_http=True) as m:
        # Mock only the external OpenRouter API call
        m.post(
            'https://openrouter.ai/api/v1/chat/completions',
            json={"choices": [{"message": {"content": "Hi there!"}}]}
        )

        # Now your local server can still be called
        response = requests.post(f"{BASE_URL}/api/chat", json=payload)

        assert response.status_code == 200
        data = response.json()
        assert "botResponse" in data
        assert data["botResponse"] == "Hi there!"
