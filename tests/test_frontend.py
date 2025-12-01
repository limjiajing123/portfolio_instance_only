# import os
import pytest
# import requests

@pytest.mark.skip(reason="Frontend not part of preprod tests currently")
def test_frontend_homepage():
    url = "http://localhost:82"
    response = requests.get(url, timeout=120) # Adjust timeout as needed

    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.text or "<html" in response.text.lower()
