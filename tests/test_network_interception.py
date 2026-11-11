
from playwright.sync_api import expect


def test_network_interception(page):

    page.goto("https://www.saucedemo.com/")

    # Intercept API request
    def handle_request(route):

        print("Intercepted URL:", route.request.url)
        print("Request Method:", route.request.method)

        # Replace actual API response with mock data
        route.fulfill(
            status=200,
            content_type="application/json",
            body="""
            {
                "products": [
                    {
                        "id": 1,
                        "name": "Laptop",
                        "price": 50000
                    }
                ]
            }
            """
        )

    page.route("**/api/products", handle_request)

    # Trigger intercepted API request
    response = page.evaluate("""
        async () => {
            const response = await fetch('/api/products');
            return await response.json();
        }
    """)

    # Validate intercepted response
    assert response["products"][0]["name"] == "Laptop"
    assert response["products"][0]["price"] == 50000

    print("Network interception successful!")
