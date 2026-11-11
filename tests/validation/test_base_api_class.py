
from utils.base_api import BaseAPI


BASE_URL = "https://jsonplaceholder.typicode.com"


# Test 1: GET using Base API class
def test_base_api_get():

    api = BaseAPI(BASE_URL)

    try:
        response = api.get("/posts/1")

        assert response.status_code == 200

        data = response.json()

        assert data["id"] == 1

        print("Base API GET successful!")

    finally:
        api.close()


# Test 2: POST using Base API class
def test_base_api_post():

    api = BaseAPI(BASE_URL)

    payload = {
        "title": "API Automation",
        "body": "Testing Base API Class",
        "userId": 1
    }

    try:
        response = api.post(
            "/posts",
            json=payload
        )

        assert response.status_code == 201

        data = response.json()

        assert data["title"] == payload["title"]

        print("Base API POST successful!")

    finally:
        api.close()
