
from playwright.sync_api import expect


def test_debug_flaky_test(page):

    # Create webpage with delayed content
    page.set_content("""
        <h2 id="status">Loading...</h2>

        <script>
            setTimeout(() => {
                document.querySelector("#status").innerText =
                    "Data Loaded Successfully";
            }, 2000);
        </script>
    """)

    # Locate dynamic element
    status = page.locator("#status")

    # Debug information
    print("Page URL:", page.url)
    print("Initial status:", status.inner_text())

    # Stable validation using auto-retrying assertion
    expect(status).to_have_text(
        "Data Loaded Successfully",
        timeout=5000
    )

    print("Dynamic content loaded successfully!")
