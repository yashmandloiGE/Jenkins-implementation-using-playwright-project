
import requests


BASE_URL = "https://httpbin.org"


def test_send_json_payload():

    # JSON request payload
    payload = {
        "name": "Yash",
        "role": "QA Engineer",
        "experience": 2,
        "skills": ["Python", "Playwright", "API Testing"]
    }

    # Send POST request with JSON data
    response = requests.post(
        f"{BASE_URL}/post",
        json=payload,
        timeout=15
    )

    # Validate status code
    assert response.status_code == 200

    # Extract JSON response
    data = response.json()

    # Validate returned JSON payload
    response_data = data["json"]

    assert response_data["name"] == "Yash"
    assert response_data["role"] == "QA Engineer"
    assert response_data["experience"] == 2
    assert response_data["skills"] == [
        "Python", "Playwright", "API Testing"
    ]

    # Validate content type
    assert response.headers["Content-Type"].startswith(
        "application/json"
    )

    print("JSON payload sent successfully!")
    print("JSON response validated successfully!")


def test_get_json_response():

    response = requests.get(
        f"{BASE_URL}/json",
        timeout=15
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    print("JSON response extracted successfully!")
    print(data)
