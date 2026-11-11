
import requests


BASE_URL = "https://httpbin.org"


# Test 1: Basic Authentication
def test_basic_authentication():

    response = requests.get(
        f"{BASE_URL}/basic-auth/qauser/qapass",
        auth=("qauser", "qapass"),
        timeout=15
    )

    assert response.status_code == 200

    data = response.json()

    assert data["authenticated"] is True
    assert data["user"] == "qauser"

    print("Basic authentication successful!")


# Test 2: Bearer Token Authentication
def test_bearer_token_authentication():

    # Practice access token
    token = "practice-access-token-123"

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
