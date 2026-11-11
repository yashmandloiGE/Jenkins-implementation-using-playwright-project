
import requests


BASE_URL = "https://httpbin.org"


# Test 1: Working with Request Headers
def test_custom_headers():

    headers = {
        "X-QA-Client": "Python-Requests",
        "Accept": "application/json"
    }

    response = requests.get(
        f"{BASE_URL}/headers",
        headers=headers,
        timeout=15
    )

    assert response.status_code == 200

    # Read headers returned by the server
    received_headers = {
        key.lower(): value
        for key, value in response.json()["headers"].items()
    }

    assert received_headers["x-qa-client"] == "Python-Requests"

    print("Custom headers verified successfully!")


# Test 2: Bearer Token Authentication
def test_bearer_token():

    token = "demo-token-123"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/bearer",
        headers=headers,
        timeout=15
    )

    assert response.status_code == 200

    data = response.json()

    assert data["authenticated"] is True
    assert data["token"] == token

    print("Bearer token authentication successful!")
