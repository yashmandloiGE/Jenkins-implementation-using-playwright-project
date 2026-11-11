
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# 1. GET Request - Fetch data
def test_get_request():

    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1

    print("GET request successful!")


# 2. POST Request - Create data
def test_post_request():

    payload = {
        "title": "QA API Testing",
        "body": "Testing POST using Python",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]

    print("POST request successful!")


# 3. PUT Request - Update complete data
def test_put_request():

    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"

    print("PUT request successful!")


# 4. PATCH Request - Update partial data
def test_patch_request():

    payload = {
        "title": "Partially Updated Title"
    }

    response = requests.patch(
        f"{BASE_URL}/posts/1",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]

    print("PATCH request successful!")


# 5. DELETE Request - Delete data
def test_delete_request():

    response = requests.delete(
        f"{BASE_URL}/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    print("DELETE request successful!")
