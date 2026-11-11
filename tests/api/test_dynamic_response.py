
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_dynamic_response_handling():

    # Send GET request
    response = requests.get(
        f"{BASE_URL}/posts",
        timeout=15
    )

    assert response.status_code == 200

    # Extract response data
    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) > 0

    # Dynamically find a post belonging to user 1
    selected_post = next(
        (post for post in posts if post["userId"] == 1),
        None
    )

    assert selected_post is not None

    # Extract dynamic values
    post_id = selected_post["id"]
    post_title = selected_post["title"]
    user_id = selected_post["userId"]

    # Validate dynamic data
    assert isinstance(post_id, int)
    assert isinstance(post_title, str)
    assert user_id == 1

    print("Dynamic Post ID:", post_id)
    print("Dynamic User ID:", user_id)
    print("Dynamic Post Title:", post_title)

    print("Dynamic response handling successful!")


def test_dynamic_array_handling():

    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=15
    )

    assert response.status_code == 200

    data = response.json()

    # Extract values dynamically
    for key, value in data.items():
        print(f"{key}: {value}")

    assert data.get("id") == 1

    print("Dynamic JSON extraction successful!")
