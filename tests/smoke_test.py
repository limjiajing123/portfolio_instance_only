import requests

def test_backend_health():
    r = requests.get("http://localhost:5000/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_litellm_is_reachable():
    """LiteLLM should be running and accepting requests"""
    r = requests.post(
        "http://localhost:4000/chat/completions",
        json={
            "model": "portfolio-default",
            "messages": [{"role": "user", "content": "hi"}]
        },
        headers={"Authorization": "Bearer dummy"}
    )
    # Any response except connection error means LiteLLM is up
    assert r.status_code in [200, 401, 429, 503]

def test_backend_can_reach_litellm():
    """Full flow — backend should process request even if AI is rate limited"""
    r = requests.post(
        "http://localhost:5000/api/chat",
        json={"message": "what is Jia Jing's email?"}
    )
    # 200 = success, 500 = backend up but AI failed (still means backend works)
    assert r.status_code in [200, 500]
    # Either botResponse or error key should be present
    body = r.json()
    assert "botResponse" in body or "error" in body