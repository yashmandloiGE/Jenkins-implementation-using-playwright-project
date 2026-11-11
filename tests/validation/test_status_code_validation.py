
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


# Test 1: Validate GET status code
def test_get_status_code():

    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=15
    )

    assert response.status_code == 200

    print("GET Status Code:", response.status_code)
    print("GET request passed!")


# Test 2: Validate POST status code
def test_post_status_code():

    payload = {
        "title": "API Testing",
        "body": "Status code validation using Python",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=15
    )

    assert response.status_code == 201

    print("POST Status Code:", response.status_code)
    print("POST request passed!")


# Test 3: Validate Not Found status code
def test_not_found_status_code():

    response = requests.get(
        f"{BASE_URL}/posts/999999",
        timeout=15
    )

    assert response.status_code == 404

    print("GET Status Code:", response.status_code)
    print("404 validation passed!")
