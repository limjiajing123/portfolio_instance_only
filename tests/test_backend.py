import requests

BASE_URL = "http://localhost:5000"

def test_chatbot_missing_message():
    """Should return 400 when message is missing"""
    payload = {}  # no message
    r = requests.post(f"{BASE_URL}/api/chat", json=payload)
    assert r.status_code == 400
    assert "Message is required" in r.text

def test_chatbot_with_message():
    """Should return mocked bot response when message is provided"""
    payload = {"message": "Hello"}
    r = requests.post(f"{BASE_URL}/api/chat", json=payload)

    # API should return success (200) since axiosMock kicks in
    assert r.status_code == 200
    body = r.json()
    assert "botResponse" in body
    assert "mocked response" in body["botResponse"]  # comes from axiosMock.js
