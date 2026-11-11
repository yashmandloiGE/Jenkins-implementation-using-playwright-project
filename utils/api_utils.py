import requests


BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 15


# Reusable API request function
def api_request(method, endpoint, **kwargs):

    response = requests.request(
        method=method,
        url=f"{BASE_URL}{endpoint}",
        timeout=TIMEOUT,
        **kwargs
    )

    return response


# Reusable status code validation
def validate_status(response, expected_status):

    assert response.status_code == expected_status, (
        f"Expected {expected_status}, "
        f"but received {response.status_code}"
    )


# Reusable JSON response extraction
def get_response_data(response):

    return response.json()