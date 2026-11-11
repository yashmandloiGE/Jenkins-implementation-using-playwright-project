
from utils.api_utils import (
    api_request,
    validate_status,
    get_response_data
)


# Test 1: Reusable GET request
def test_get_using_utility():

    response = api_request("GET", "/posts/1")

    validate_status(response, 200)

    data = get_response_data(response)

    assert data["id"] == 1

    print("GET request utility verified!")


# Test 2: Reusable POST request
def test_post_using_utility():

    payload = {
        "title": "API Automation",
        "body": "Testing reusable utilities",
        "userId": 1
    }

    response = api_request(
        "POST",
        "/posts",
        json=payload
    )

    validate_status(response, 201)

    data = get_response_data(response)

    assert data["title"] == payload["title"]
    assert data["userId"] == 1

    print("POST request utility verified!")
