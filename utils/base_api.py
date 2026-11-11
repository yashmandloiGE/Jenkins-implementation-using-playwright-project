
import requests


class BaseAPI:

    def __init__(self, base_url, timeout=15):

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        # Create reusable session
        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/json"
        })

    # Common request method
    def request(self, method, endpoint, **kwargs):

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        response = self.session.request(
            method=method,
            url=url,
            timeout=self.timeout,
            **kwargs
        )

        return response

    # GET request
    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    # POST request
    def post(self, endpoint, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    # PUT request
    def put(self, endpoint, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    # PATCH request
    def patch(self, endpoint, **kwargs):
        return self.request("PATCH", endpoint, **kwargs)

    # DELETE request
    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)

    # Close session
    def close(self):
        self.session.close()
