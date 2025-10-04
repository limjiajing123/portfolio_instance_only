import requests

def test_frontend_homepage():
    r = requests.get("http://localhost:82")
    assert r.status_code == 200
    assert "Portfolio" in r.text  # adjust to your homepage content

def test_backend_health():
    r = requests.get("http://localhost:5000/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_chatbot_api():
    payload = {"message": "Hello"}
    r = requests.post("http://localhost:5000/api/chat", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "response" in data
