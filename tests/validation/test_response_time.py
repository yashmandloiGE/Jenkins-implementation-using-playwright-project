
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"

MAX_RESPONSE_TIME = 5  # Maximum allowed time in seconds


def test_get_response_time():

    # Send API request
    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=15
    )

    # Validate status code
    assert response.status_code == 200

    # Capture response time
    response_time = response.elapsed.total_seconds()

    print("Response Time:", response_time, "seconds")

    # Validate response time
    assert response_time < MAX_RESPONSE_TIME, (
        f"API response too slow: {response_time} seconds"
    )

    print("Response time validation successful!")


def test_post_response_time():

    payload = {
        "title": "QA Testing",
        "body": "Testing API response time",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=15
    )

    assert response.status_code == 201

    response_time = response.elapsed.total_seconds()

    print("POST Response Time:", response_time, "seconds")

    assert response_time < MAX_RESPONSE_TIME

    print("POST response time validation successful!")
