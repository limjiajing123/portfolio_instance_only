import requests

def test_backend_health():
    """Backend should be running and healthy"""
    r = requests.get("http://localhost:5000/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_litellm_is_reachable():
    """LiteLLM proxy should be running and accepting requests"""
    r = requests.post(
        "http://localhost:4000/chat/completions",
        json={
            "model": "portfolio-default",
            "messages": [{"role": "user", "content": "hi"}]
        },
        headers={"Authorization": "Bearer dummy"}
    )
    # Any response except connection error means LiteLLM is up
    # 200 = success, 401 = auth issue, 429 = rate limit, 503 = model busy
    # all of these mean the service is running
    assert r.status_code in [200, 401, 429, 503]

def test_mcp_server_is_reachable():
    """MCP server SSE endpoint should be reachable"""
    r = requests.get("http://localhost:8000/sse", stream=True, timeout=5)
    assert r.status_code == 200