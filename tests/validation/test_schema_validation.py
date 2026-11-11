import requests
from jsonschema import validate


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_post_response_schema():

    # Send GET request
    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=15
    )

    assert response.status_code == 200

    # Extract JSON response
    data = response.json()

    # Define expected JSON schema
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": [
            "userId",
            "id",
            "title",
            "body"
        ],
        "additionalProperties": False
    }

    # Validate response against schema
    validate(
        instance=data,
        schema=schema
    )

    print("Response schema validated successfully!")
    print("All required fields and data types are correct!")