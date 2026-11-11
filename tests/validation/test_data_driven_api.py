
import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


# Different test data sets
@pytest.mark.parametrize(
    "post_id, expected_user_id",
    [
        (1, 1),
        (11, 2),
        (21, 3),
        (31, 4),
        (41, 5)
    ]
)
def test_get_post_with_multiple_data(post_id, expected_user_id):

    # Send GET request using dynamic post ID
    response = requests.get(
        f"{BASE_URL}/posts/{post_id}",
        timeout=15
    )

    # Validate status code
    assert response.status_code == 200

    # Extract response data
    data = response.json()

    # Validate dynamic values
    assert data["id"] == post_id
    assert data["userId"] == expected_user_id

    print(
        f"Post ID: {post_id}, "
        f"User ID: {data['userId']} - Passed"
    )
