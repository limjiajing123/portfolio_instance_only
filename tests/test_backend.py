import requests

BASE_URL = "http://localhost:5000"

def test_chatbot_missing_message():
    """Should return 400 when message is missing"""
    payload = {}
    r = requests.post(f"{BASE_URL}/api/chat", json=payload)
    assert r.status_code == 400
    assert "Message is required" in r.text

def test_chatbot_with_message():
    """Should return mocked bot response when message is provided.
    
    NODE_ENV=test is set in CI which:
    - mocks native fetch for LiteLLM calls
    - skips MCP server connection and returns mock tools
    This tests that the backend correctly handles a successful LLM response.
    We are NOT testing whether Gemini works — that's non-deterministic.
    We ARE testing that our backend logic correctly returns a botResponse.
    """
    payload = {"message": "Hello"}
    r = requests.post(f"{BASE_URL}/api/chat", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert "botResponse" in body
    assert body["botResponse"].strip() != ""

def test_chatbot_returns_error_gracefully():
    """Backend should return structured error, not crash"""
    # Send a very long message to stress test
    payload = {"message": "x" * 10000}
    r = requests.post(f"{BASE_URL}/api/chat", json=payload)
    # Should return either a response or a structured error, never a raw crash
    assert r.status_code in [200, 400, 500]
    body = r.json()
    assert "botResponse" in body or "error" in body