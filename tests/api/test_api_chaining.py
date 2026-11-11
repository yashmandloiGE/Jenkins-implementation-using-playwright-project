
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_api_chaining():

    # STEP 1: Get user details
    user_response = requests.get(
        f"{BASE_URL}/users/1",
        timeout=15
    )

    assert user_response.status_code == 200

    user_data = user_response.json()

    # Extract dynamic user ID
    user_id = user_data["id"]

    print("User ID:", user_id)


    # STEP 2: Use user ID to get their posts
    posts_response = requests.get(
        f"{BASE_URL}/posts",
        params={"userId": user_id},
        timeout=15
    )

    assert posts_response.status_code == 200

    posts = posts_response.json()

    assert len(posts) > 0

    # Extract post ID dynamically
    post_id = posts[0]["id"]

    print("Post ID:", post_id)


    # STEP 3: Use post ID to get its comments
    comments_response = requests.get(
        f"{BASE_URL}/comments",
        params={"postId": post_id},
        timeout=15
    )

    assert comments_response.status_code == 200

    comments = comments_response.json()

    # Validate comments belong to the selected post
    assert len(comments) > 0

    for comment in comments:
        assert comment["postId"] == post_id

    print("Comments found:", len(comments))
    print("API chaining completed successfully!")
