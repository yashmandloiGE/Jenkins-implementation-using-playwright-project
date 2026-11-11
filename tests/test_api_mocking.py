
import json
from playwright.sync_api import expect


def test_mock_api_response(page):

    # Predefined mock API data
    mock_data = {
        "products": [
            {"id": 1, "name": "Laptop", "price": 75000},
            {"id": 2, "name": "Mobile", "price": 30000}
        ]
    }

    # Intercept and mock API response
    def mock_api(route):

        route.fulfill(
            status=200,
            content_type="application/json",
            headers={"Access-Control-Allow-Origin": "*"},
            body=json.dumps(mock_data)
        )

    page.route("https://api.example.test/products", mock_api)

    # Create test webpage
    page.set_content("""
        <h1>Product List</h1>
        <ul id="products"></ul>

        <script>
            async function loadProducts() {

                const response = await fetch(
                    "https://api.example.test/products"
                );

                const data = await response.json();

                document.querySelector("#products").innerHTML =
                    data.products.map(product =>
                        `<li>${product.name} - ${product.price}</li>`
                    ).join("");
            }
        </script>
    """)

    # Trigger API request
    page.evaluate("loadProducts()")

    # Validate mocked response
    expect(page.locator("#products li")).to_have_count(2)

    expect(
        page.locator("#products")
    ).to_contain_text("Laptop")

    expect(
        page.locator("#products")
    ).to_contain_text("Mobile")

    print("Mock API response verified successfully!")
