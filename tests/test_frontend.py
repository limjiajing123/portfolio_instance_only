import requests

def test_frontend_homepage():
    url = "http://localhost:82"
    response = requests.get(url)

    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.text or "<html" in response.text.lower()
